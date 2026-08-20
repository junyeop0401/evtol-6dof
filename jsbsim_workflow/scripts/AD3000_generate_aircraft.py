#!/usr/bin/env python3
"""Generate the AD3000 JSBSim aircraft package from provided source files."""

from __future__ import annotations

import csv
import math
import re
import shutil
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET


JSBSIM_ROOT = Path("/home/junyeopkwon/jsbsim")
WORKFLOW_ROOT = Path("/home/junyeopkwon/evtol-6dof/jsbsim_workflow")

SOURCE_DIR = Path("/mnt/d/ADSystem/ad3000")
XLSX_PATH = SOURCE_DIR / "DB 정리.xlsx"
AERO_DB_PATH = SOURCE_DIR / "jsbsim_aerodynamic_database.xml"
STEP_PATH = SOURCE_DIR / "AD3000_CFD.step"

AIRCRAFT_NAME = "AD3000"
AIRCRAFT_DIR = JSBSIM_ROOT / "aircraft" / AIRCRAFT_NAME
ENGINE_DIR = JSBSIM_ROOT / "engine"
WORKFLOW_VARIANT_DIR = WORKFLOW_ROOT / "aircraft_variants" / AIRCRAFT_NAME
WORKFLOW_SCRIPT_DIR = WORKFLOW_ROOT / "scripts" / AIRCRAFT_NAME


def cell_values(path: Path) -> tuple[dict[str, float | str], list[dict[str, float | str]]]:
    ns = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
    with zipfile.ZipFile(path) as zf:
        shared: list[str] = []
        root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
        for si in root.findall(ns + "si"):
            shared.append("".join((t.text or "") for t in si.iter(ns + "t")))

        sheet = ET.fromstring(zf.read("xl/worksheets/sheet1.xml"))
        values: dict[str, float | str] = {}
        rows: list[dict[str, float | str]] = []
        for row in sheet.iter(ns + "row"):
            row_values: dict[str, float | str] = {}
            for c in row.findall(ns + "c"):
                ref = c.attrib.get("r", "")
                col = re.sub(r"\d+", "", ref)
                v = c.find(ns + "v")
                if v is None:
                    continue
                raw: float | str = v.text or ""
                if c.attrib.get("t") == "s":
                    raw = shared[int(str(raw))]
                else:
                    try:
                        raw = float(str(raw))
                    except ValueError:
                        pass
                values[ref] = raw
                row_values[col] = raw
            if row_values:
                rows.append(row_values)
        return values, rows


def get_float(values: dict[str, float | str], ref: str) -> float:
    value = values[ref]
    if not isinstance(value, (float, int)):
        raise ValueError(f"{ref} is not numeric: {value!r}")
    return float(value)


def transform_sheet_to_jsbsim(f_mm: float, g_mm: float, h_mm: float) -> tuple[float, float, float]:
    """Map AD3000 workbook/STEP axes to JSBSim structural coordinates.

    Inferred from component names and CAD extents:
    - sheet F/STEP X is spanwise left-positive, so JSBSim y-right is -F.
    - sheet G/STEP Y is vertical up-positive, so JSBSim z-up is G.
    - sheet H/STEP Z is nose-to-tail negative aft, so JSBSim x-aft is -H.
    """

    return -h_mm / 1000.0, -f_mm / 1000.0, g_mm / 1000.0


def parse_components(rows: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    components: list[dict[str, float | str]] = []
    for r in rows:
        if not isinstance(r.get("E"), (float, int)):
            continue
        if not isinstance(r.get("F"), (float, int)):
            continue
        if not isinstance(r.get("G"), (float, int)):
            continue
        if not isinstance(r.get("H"), (float, int)):
            continue
        x, y, z = transform_sheet_to_jsbsim(float(r["F"]), float(r["G"]), float(r["H"]))
        components.append(
            {
                "system": r.get("B", ""),
                "part": r.get("C", ""),
                "note": r.get("D", ""),
                "mass_g": float(r["E"]),
                "source_F_mm": float(r["F"]),
                "source_G_mm": float(r["G"]),
                "source_H_mm": float(r["H"]),
                "jsbsim_x_m": x,
                "jsbsim_y_m": y,
                "jsbsim_z_m": z,
            }
        )
    return components


def step_bbox(path: Path) -> dict[str, float]:
    text = path.read_text(errors="ignore")
    pts: list[tuple[float, float, float]] = []
    pat = re.compile(r"CARTESIAN_POINT\s*\([^,]*,\s*\(([^)]*)\)\s*\)", re.I)
    for m in pat.finditer(text):
        try:
            nums = tuple(float(s.strip()) for s in m.group(1).split(","))
        except ValueError:
            continue
        if len(nums) == 3:
            pts.append(nums)  # type: ignore[arg-type]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    zs = [p[2] for p in pts]
    return {
        "points": float(len(pts)),
        "step_x_min_mm": min(xs),
        "step_x_max_mm": max(xs),
        "step_y_min_mm": min(ys),
        "step_y_max_mm": max(ys),
        "step_z_min_mm": min(zs),
        "step_z_max_mm": max(zs),
    }


def component(components: list[dict[str, float | str]], part: str) -> dict[str, float | str]:
    for item in components:
        if item["part"] == part:
            return item
    raise KeyError(part)


def fmt(value: float) -> str:
    return f"{value:.6f}"


def xml_header() -> str:
    return '<?xml version="1.0" encoding="UTF-8"?>\n'


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def convert_aero_database(source: Path, target: Path) -> None:
    tree = ET.parse(source)
    root = tree.getroot()
    aero = root.find("aerodynamics")
    if aero is None:
        raise ValueError("aerodynamics section not found")

    for table in aero.iter("table"):
        ivars = table.findall("independentVar")
        table_datas = table.findall("tableData")
        if len(ivars) != 2 or len(table_datas) < 2:
            continue
        if ivars[1].attrib.get("lookup") != "table":
            continue
        matrices: list[tuple[str, list[tuple[str, str]]]] = []
        row_keys: list[str] = []
        eligible = True
        for td in table_datas:
            bp = td.attrib.get("breakPoint")
            if bp is None:
                eligible = False
                break
            entries: list[tuple[str, str]] = []
            for line in (td.text or "").splitlines():
                parts = line.split()
                if not parts:
                    continue
                if len(parts) != 2:
                    eligible = False
                    break
                entries.append((parts[0], parts[1]))
            if not eligible:
                break
            if not row_keys:
                row_keys = [row for row, _ in entries]
            elif row_keys != [row for row, _ in entries]:
                eligible = False
                break
            matrices.append((bp, entries))
        if not eligible:
            continue
        ivars[1].set("lookup", "column")
        for td in table_datas:
            table.remove(td)
        new_td = ET.SubElement(table, "tableData")
        lines = [" " + " ".join(bp for bp, _ in matrices)]
        for idx, row_key in enumerate(row_keys):
            vals = [entries[idx][1] for _, entries in matrices]
            lines.append(row_key + " " + " ".join(vals))
        new_td.text = "\n" + "\n".join(lines) + "\n"

    ET.indent(aero, space="  ")
    write(target, xml_header() + ET.tostring(aero, encoding="unicode") + "\n")


def main() -> None:
    values, rows = cell_values(XLSX_PATH)
    components = parse_components(rows)
    bbox = step_bbox(STEP_PATH)

    mass_kg = get_float(values, "E59") / 1000.0
    # Workbook row 60 uses H/G as CG values. F60 is labeled "mac LE" in the sheet,
    # so lateral CG is recomputed from all listed component point masses instead.
    total_g = sum(float(c["mass_g"]) for c in components)
    cg_source_f = sum(float(c["mass_g"]) * float(c["source_F_mm"]) for c in components) / total_g
    cg_source_g = get_float(values, "G60")
    cg_source_h = get_float(values, "H60")
    cg_x, cg_y, cg_z = transform_sheet_to_jsbsim(cg_source_f, cg_source_g, cg_source_h)

    # Remap sheet inertia axes to JSBSim X-aft/Y-right/Z-up using the inferred CAD axes.
    sheet_i_f = get_float(values, "E63")
    sheet_i_g = get_float(values, "E64")
    sheet_i_h = get_float(values, "E65")
    jsb_ixx = sheet_i_h
    jsb_iyy = sheet_i_f
    jsb_izz = sheet_i_g

    main_xml = f"""{xml_header()}<?xml-stylesheet type="text/xsl" href="http://jsbsim.sourceforge.net/JSBSim.xsl"?>
<fdm_config name="AD3000" version="2.0" release="ALPHA_SOURCE_ASSEMBLY"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:noNamespaceSchemaLocation="http://jsbsim.sourceforge.net/JSBSim.xsd">
  <fileheader>
    <author>junyeopkwon / OpenAI Codex</author>
    <filecreationdate>2026-08-11</filecreationdate>
    <version>0.1.0</version>
    <description>
      AD3000 lift-plus-cruise VTOL JSBSim seed model assembled from the provided
      AD3000 workbook, DATCOM aerodynamic XML, and STEP geometry. Structural
      locations use a nose datum with JSBSim x-aft, y-right, z-up coordinates.
    </description>
  </fileheader>

  <metrics file="Metrics.xml"/>
  <mass_balance file="Mass.xml"/>
  <ground_reactions file="Gear.xml"/>
  <propulsion file="Propulsion.xml"/>
  <system file="Effectors.xml"/>
  <flight_control file="FlightControl.xml"/>
  <aerodynamics file="Aero.xml"/>
</fdm_config>
"""
    write(AIRCRAFT_DIR / "AD3000.xml", main_xml)

    metrics_xml = f"""{xml_header()}<metrics>
  <documentation>
    Reference geometry is copied from jsbsim_aerodynamic_database.xml. The STEP
    bounding box is recorded in SOURCE_MATRIX.csv but not used to override the
    DATCOM reference area/span because the aerodynamic tables were generated
    against S=1.0650005 m2, b=3.0 m, c=0.36967129 m.
  </documentation>
  <wingarea unit="M2">1.0650005</wingarea>
  <wingspan unit="M">3.000000</wingspan>
  <chord unit="M">0.369671</chord>
  <htailarea unit="M2">0.000000</htailarea>
  <vtailarea unit="M2">0.180000</vtailarea>
  <vtailarm unit="M">0.950000</vtailarm>
  <location name="AERORP" unit="M">
    <x>{fmt(cg_x)}</x><y>{fmt(cg_y)}</y><z>{fmt(cg_z)}</z>
  </location>
  <location name="EYEPOINT" unit="M">
    <x>0.200000</x><y>0.000000</y><z>0.080000</z>
  </location>
  <location name="VRP" unit="M">
    <x>0.000000</x><y>0.000000</y><z>0.000000</z>
  </location>
</metrics>
"""
    write(AIRCRAFT_DIR / "Metrics.xml", metrics_xml)

    mass_xml = f"""{xml_header()}<mass_balance>
  <documentation>
    Total mass is the workbook displayed sum E59. Inertias are the workbook
    final MOI values remapped from the inferred STEP/workbook axes to JSBSim
    x-aft/y-right/z-up. F60 is labeled mac LE in the workbook, so lateral CG is
    recomputed from listed component masses rather than used as a lateral CG.
  </documentation>
  <emptywt unit="KG">{fmt(mass_kg)}</emptywt>
  <location name="CG" unit="M">
    <x>{fmt(cg_x)}</x><y>{fmt(cg_y)}</y><z>{fmt(cg_z)}</z>
  </location>
  <ixx unit="KG*M2">{fmt(jsb_ixx)}</ixx>
  <iyy unit="KG*M2">{fmt(jsb_iyy)}</iyy>
  <izz unit="KG*M2">{fmt(jsb_izz)}</izz>
  <ixy unit="KG*M2">0.000000</ixy>
  <ixz unit="KG*M2">0.000000</ixz>
  <iyz unit="KG*M2">0.000000</iyz>
</mass_balance>
"""
    write(AIRCRAFT_DIR / "Mass.xml", mass_xml)

    front_gear = component(components, "전방 랜딩기어")
    rear_gear = component(components, "후방 랜딩기어")
    fgx, _, fgz = float(front_gear["jsbsim_x_m"]), float(front_gear["jsbsim_y_m"]), float(front_gear["jsbsim_z_m"])
    rgx, _, rgz = float(rear_gear["jsbsim_x_m"]), float(rear_gear["jsbsim_y_m"]), float(rear_gear["jsbsim_z_m"])
    gear_xml = f"""{xml_header()}<ground_reactions>
  <contact name="Nose_Gear" type="BOGEY">
    <location unit="M"><x>{fmt(fgx)}</x><y>0.000000</y><z>{fmt(fgz)}</z></location>
    <static_friction>0.80</static_friction>
    <dynamic_friction>0.55</dynamic_friction>
    <rolling_friction>0.03</rolling_friction>
    <spring_coeff unit="N/M">18000</spring_coeff>
    <damping_coeff unit="N/M/SEC">1200</damping_coeff>
    <damping_coeff_rebound unit="N/M/SEC">600</damping_coeff_rebound>
    <max_steer unit="DEG">0</max_steer>
    <brake_group>NONE</brake_group>
    <retractable>0</retractable>
  </contact>
  <contact name="Main_Left" type="BOGEY">
    <location unit="M"><x>{fmt(rgx)}</x><y>-0.350000</y><z>{fmt(rgz)}</z></location>
    <static_friction>0.80</static_friction>
    <dynamic_friction>0.55</dynamic_friction>
    <rolling_friction>0.03</rolling_friction>
    <spring_coeff unit="N/M">18000</spring_coeff>
    <damping_coeff unit="N/M/SEC">1200</damping_coeff>
    <damping_coeff_rebound unit="N/M/SEC">600</damping_coeff_rebound>
    <max_steer unit="DEG">0</max_steer>
    <brake_group>NONE</brake_group>
    <retractable>0</retractable>
  </contact>
  <contact name="Main_Right" type="BOGEY">
    <location unit="M"><x>{fmt(rgx)}</x><y>0.350000</y><z>{fmt(rgz)}</z></location>
    <static_friction>0.80</static_friction>
    <dynamic_friction>0.55</dynamic_friction>
    <rolling_friction>0.03</rolling_friction>
    <spring_coeff unit="N/M">18000</spring_coeff>
    <damping_coeff unit="N/M/SEC">1200</damping_coeff>
    <damping_coeff_rebound unit="N/M/SEC">600</damping_coeff_rebound>
    <max_steer unit="DEG">0</max_steer>
    <brake_group>NONE</brake_group>
    <retractable>0</retractable>
  </contact>
  <contact name="Left_Wing_Tip" type="STRUCTURE">
    <location unit="M"><x>0.450000</x><y>-1.500000</y><z>-0.050000</z></location>
    <static_friction>0.20</static_friction>
    <dynamic_friction>0.20</dynamic_friction>
    <spring_coeff unit="N/M">6000</spring_coeff>
    <damping_coeff unit="N/M/SEC">800</damping_coeff>
  </contact>
  <contact name="Right_Wing_Tip" type="STRUCTURE">
    <location unit="M"><x>0.450000</x><y>1.500000</y><z>-0.050000</z></location>
    <static_friction>0.20</static_friction>
    <dynamic_friction>0.20</dynamic_friction>
    <spring_coeff unit="N/M">6000</spring_coeff>
    <damping_coeff unit="N/M/SEC">800</damping_coeff>
  </contact>
</ground_reactions>
"""
    write(AIRCRAFT_DIR / "Gear.xml", gear_xml)

    # Rotor order: FR, AL, FL, AR, pusher. 생성되는 AD3000 XML 주석은 한글로 남긴다.
    rotor_map = [
        ("lift front right", "VTOL 프로펠러 #3", 1.0),
        ("lift aft left", "VTOL 프로펠러 #1", 1.0),
        ("lift front left", "VTOL 프로펠러 #2", -1.0),
        ("lift aft right", "VTOL 프로펠러 #4", -1.0),
    ]
    engines = []
    for name, part, sense in rotor_map:
        c = component(components, part)
        engines.append(
            f'''  <engine file="AD3000_lift_motor_V6212_180KV" name="{name}">
    <thruster file="AD3000_lift_prop_Hobbywing_VSC_22x7_4">
      <location unit="M"><x>{fmt(float(c["jsbsim_x_m"]))}</x><y>{fmt(float(c["jsbsim_y_m"]))}</y><z>{fmt(float(c["jsbsim_z_m"]))}</z></location>
      <orient unit="DEG"><roll>0.0</roll><pitch>90.0</pitch><yaw>0.0</yaw></orient>
      <sense>{sense:.1f}</sense>
      <p_factor>0.0</p_factor>
    </thruster>
  </engine>'''
        )
    pusher = component(components, "고정익 프로펠러")
    engines.append(
        f'''  <!-- cruise 실기 의도 prop은 기체 Spec 시트의 20*10이다. 해당 조합의 공개 thrust/power sheet가 없어 우선 같은 시트의 V6215 210KV와 VSC 22.1x7.4 공식 공개 데이터를 사용한다. -->
  <engine file="AD3000_cruise_motor_V6215_210KV" name="cruise pusher">
    <thruster file="AD3000_cruise_prop_Hobbywing_VSC_22x7_4">
      <location unit="M"><x>{fmt(float(pusher["jsbsim_x_m"]))}</x><y>{fmt(float(pusher["jsbsim_y_m"]))}</y><z>{fmt(float(pusher["jsbsim_z_m"]))}</z></location>
      <orient unit="DEG"><roll>0.0</roll><pitch>0.0</pitch><yaw>0.0</yaw></orient>
      <sense>1.0</sense>
      <p_factor>0.02</p_factor>
    </thruster>
  </engine>'''
    )
    propulsion_intro = "  <!-- lift rotor 4기는 DB 정리.xlsx의 기체 Spec 시트에 있는 V6212 180KV와 VSC 22.1x7.4 공식 pull test 데이터를 기준으로 구성했다. -->\n"
    write(AIRCRAFT_DIR / "Propulsion.xml", xml_header() + "<propulsion>\n  <!-- 주의: 기체 Spec 시트의 pull test는 static data라서 J=0 Ct/Cp만 직접 계산된다. J>0 table 값은 임시 advance-ratio shape를 곱한 초기 가정이다. -->\n" + propulsion_intro + "\n\n".join(engines) + "\n</propulsion>\n")

    flight_control_xml = f"""{xml_header()}<flight_control name="AD3000 lift-plus-cruise mixer">
  <property value="0.0">fcs/pusher-throttle-cmd-norm</property>
  <property value="0.0">fcs/fw-aileron-cmd-norm</property>
  <property value="0.0">fcs/fw-elevator-cmd-norm</property>
  <property value="0.0">fcs/fw-rudder-cmd-norm</property>

  <channel name="Manual multicopter inputs">
    <pure_gain name="fcs/manual-roll-mix">
      <input>fcs/aileron-cmd-norm</input><gain>0.18</gain>
      <clipto><min>-0.25</min><max>0.25</max></clipto>
    </pure_gain>
    <pure_gain name="fcs/manual-pitch-mix">
      <input>fcs/elevator-cmd-norm</input><gain>0.18</gain>
      <clipto><min>-0.25</min><max>0.25</max></clipto>
    </pure_gain>
    <pure_gain name="fcs/manual-yaw-mix">
      <input>fcs/rudder-cmd-norm</input><gain>0.12</gain>
      <clipto><min>-0.20</min><max>0.20</max></clipto>
    </pure_gain>
  </channel>

  <channel name="Lift motor mixer">
    <summer name="fcs/cmdEscFR-norm">
      <input>fcs/throttle-cmd-norm</input>
      <input>-fcs/manual-roll-mix</input>
      <input>fcs/manual-pitch-mix</input>
      <input>fcs/manual-yaw-mix</input>
      <clipto><min>0.0</min><max>1.0</max></clipto>
    </summer>
    <summer name="fcs/cmdEscAL-norm">
      <input>fcs/throttle-cmd-norm</input>
      <input>fcs/manual-roll-mix</input>
      <input>-fcs/manual-pitch-mix</input>
      <input>fcs/manual-yaw-mix</input>
      <clipto><min>0.0</min><max>1.0</max></clipto>
    </summer>
    <summer name="fcs/cmdEscFL-norm">
      <input>fcs/throttle-cmd-norm</input>
      <input>fcs/manual-roll-mix</input>
      <input>fcs/manual-pitch-mix</input>
      <input>-fcs/manual-yaw-mix</input>
      <clipto><min>0.0</min><max>1.0</max></clipto>
    </summer>
    <summer name="fcs/cmdEscAR-norm">
      <input>fcs/throttle-cmd-norm</input>
      <input>-fcs/manual-roll-mix</input>
      <input>-fcs/manual-pitch-mix</input>
      <input>-fcs/manual-yaw-mix</input>
      <clipto><min>0.0</min><max>1.0</max></clipto>
    </summer>
  </channel>

  <channel name="Fixed-wing control surfaces">
    <aerosurface_scale name="fcs/effective-aileron-control-deg">
      <input>fcs/fw-aileron-cmd-norm</input>
      <range><min>-20.0</min><max>20.0</max></range>
      <output>fcs/effective-aileron-pos-deg</output>
    </aerosurface_scale>
    <aerosurface_scale name="fcs/elevator-control-deg">
      <input>fcs/fw-elevator-cmd-norm</input>
      <range><min>-15.0</min><max>15.0</max></range>
      <output>fcs/elevator-pos-deg</output>
    </aerosurface_scale>
  </channel>
</flight_control>
"""
    write(AIRCRAFT_DIR / "FlightControl.xml", flight_control_xml)

    effectors_xml = f"""{xml_header()}<system name="AD3000 effectors">
  <channel name="Electronic speed controllers">
    <actuator name="Lift Front Right">
      <input>fcs/cmdEscFR-norm</input>
      <clipto><min>0.0</min><max>1.0</max></clipto>
      <output>fcs/throttle-pos-norm[0]</output>
    </actuator>
    <actuator name="Lift Aft Left">
      <input>fcs/cmdEscAL-norm</input>
      <clipto><min>0.0</min><max>1.0</max></clipto>
      <output>fcs/throttle-pos-norm[1]</output>
    </actuator>
    <actuator name="Lift Front Left">
      <input>fcs/cmdEscFL-norm</input>
      <clipto><min>0.0</min><max>1.0</max></clipto>
      <output>fcs/throttle-pos-norm[2]</output>
    </actuator>
    <actuator name="Lift Aft Right">
      <input>fcs/cmdEscAR-norm</input>
      <clipto><min>0.0</min><max>1.0</max></clipto>
      <output>fcs/throttle-pos-norm[3]</output>
    </actuator>
    <actuator name="Cruise Pusher">
      <input>fcs/pusher-throttle-cmd-norm</input>
      <clipto><min>0.0</min><max>1.0</max></clipto>
      <output>fcs/throttle-pos-norm[4]</output>
    </actuator>
  </channel>
</system>
"""
    write(AIRCRAFT_DIR / "Effectors.xml", effectors_xml)

    convert_aero_database(AERO_DB_PATH, AIRCRAFT_DIR / "Aero.xml")

    init_xml = f"""{xml_header()}<initialize name="Gimpo ground">
  <vt unit="M/S">0.0</vt>
  <latitude type="geodetic" unit="DEG">37.5583</latitude>
  <longitude unit="DEG">126.7906</longitude>
  <altitude unit="M">18.0</altitude>
  <elevation unit="M">18.0</elevation>
  <psi unit="DEG">315.0</psi>
</initialize>
"""
    write(AIRCRAFT_DIR / "initGrnd.xml", init_xml)

    lift_hover = mass_kg * 9.80665 / 4.0
    lift_max = mass_kg * 9.80665 * 2.0 / 4.0
    lift_hover_throttle = math.sqrt(lift_hover / lift_max)
    readme = '# AD3000 JSBSim 시드 모델\n\n이 폴더는 제공된 AD3000 자료를 기준으로 구성한 JSBSim용 lift-plus-cruise VTOL 시드 모델이다. 기존 ADS, F450, MiniTalon 모델은 수정하지 않고 AD3000 신규 aircraft로 분리했다.\n\n## 사용한 원본 자료\n\n- 질량, 부품 위치, 관성 계산: D:/ADSystem/ad3000/DB 정리.xlsx\n- 공력 계수: D:/ADSystem/ad3000/jsbsim_aerodynamic_database.xml\n- 형상 범위 확인: D:/ADSystem/ad3000/AD3000_CFD.step\n- 구조 참고: D:/ProjectAirSim-jsbsim/core_sim/jsbsim/models/aircraft/standard_vtol_demo/standard_vtol_demo.xml\n\n## 주요 적용 값\n\n- 총 질량: 14.9425 kg\n- JSBSim nose datum 기준 CG: x=0.3727 m aft, y=-0.0002 m right, z=-0.0140 m up\n- JSBSim 축 기준 관성: Ixx=0.5270, Iyy=1.7727, Izz=2.2370 kg*m2\n- DATCOM 기준 공력 형상: S=1.0650005 m2, b=3.0 m, c=0.36967129 m\n- lift rotor 크기 산정 목표: rotor별 정지 최대추력 약 73.3 N, hover 기준 rotor별 평균 추력 약 36.6 N\n- 동일 collective 기준 hover throttle 추정값: 약 0.71\n\n## 좌표계\n\n기체 XML의 구조 좌표는 nose datum 기준 JSBSim 좌표계인 x aft, y right, z up을 사용한다.\n\nXLSX/STEP 축은 부품 배치와 STEP bounding box를 기준으로 다음처럼 해석했다.\n\n- workbook/STEP F/X: spanwise left-positive\n- workbook/STEP G/Y: vertical up-positive\n- workbook/STEP H/Z: longitudinal aft-negative\n\n따라서 JSBSim 위치 변환은 다음과 같다.\n\n- x_jsbsim = -H_mm / 1000\n- y_jsbsim = -F_mm / 1000\n- z_jsbsim = G_mm / 1000\n\n## 추진계 산정 근거\n\n모터와 프롭은 아직 실측/제품 확정값이 없으므로 질량 기반 placeholder로 구성했다.\n\n- lift motor/prop: 총 thrust-to-weight 약 2.0을 목표로 4개 rotor에 분배했다.\n- rotor별 최대 추력 목표는 14.9425 kg * 9.80665 * 2 / 4 = 73.27 N이다.\n- hover 평균 추력은 14.9425 kg * 9.80665 / 4 = 36.63 N이다.\n- 20 inch급 저 KV 12S lift prop/motor placeholder를 적용했다.\n- pusher는 transition/cruise 초기 검토용으로 15 inch급 12S placeholder를 적용했다.\n\n## 현재 검증 상태\n\n- XML well-formed 검사는 통과했다.\n- JSBSim --aircraft=AD3000 --catalog 로딩은 통과했다.\n- smoke runscript --end=1.5 짧은 통합 실행은 통과했다.\n- 8초 전체 hover smoke run은 약 2초 이후 Floating point exception으로 실패했다.\n\n## 남은 주요 리스크\n\n현재 CG가 전방 rotor 쪽에 가까워 동일 collective 입력만으로는 큰 pitch moment가 발생한다. hover 안정화를 위해 front/rear rotor 추력 split 또는 실제 CG/rotor 위치 재검토가 필요하다.\n'
    write(AIRCRAFT_DIR / "README.md", readme)

    assumptions = '# AD3000 가정 및 한계\n\n## 현재 가정\n\n- 이 모델은 JSBSim 통합용 시드 모델이며, 비행시험으로 검증된 최종 모델이 아니다.\n- 공력 기준값은 제공된 jsbsim_aerodynamic_database.xml의 DATCOM 형상과 계수 테이블을 우선한다.\n- STEP bounding box는 SOURCE_MATRIX.csv에 추적용으로 기록했지만 DATCOM span을 대체하지 않았다. STEP에서 추출한 span-like extent와 공력 DB의 wingspan 값이 서로 다르기 때문이다.\n- DB 정리.xlsx의 F60 셀은 mac LE로 표시되어 있어 lateral CG로 직접 사용하지 않았다. lateral CG는 부품 질량과 F 좌표로 재계산했다.\n- products of inertia, 즉 Ixy, Ixz, Iyz는 최종 CAD mass property가 JSBSim 좌표계로 export되기 전까지 0으로 둔다.\n- lift motor와 propeller는 총 질량 기준으로 산정한 placeholder다. 현재 목표는 VTOL 제어 여유를 위해 총 thrust-to-weight 약 2.0을 확보하는 것이다.\n- pusher motor와 propeller는 15 kg급 기체의 초기 cruise/transition 검토용 placeholder다.\n\n## 추진계 산정 한계\n\n- lift rotor 최대 추력 목표는 rotor별 약 73.27 N이다.\n- hover 평균 추력은 rotor별 약 36.63 N이다.\n- 현재 FlightControl.xml은 동일 collective를 4개 lift rotor에 배분한다.\n- 하지만 CG가 전방 rotor 쪽에 가까우므로 실제 hover에는 front/rear 추력 split이 필요하다.\n- 현재 CG와 rotor x 위치 기준 정적 pitch moment 균형 추력은 front rotor 약 60.3 N each, aft rotor 약 13.0 N each로 추정된다.\n- 이 split은 실제 CG, rotor hub 위치, thrust line이 확정되면 다시 계산해야 한다.\n\n## 현재 검증 한계\n\n- XML 문법 검사는 통과했다.\n- JSBSim catalog load는 통과했다.\n- 1.5초 짧은 통합 실행은 통과했다.\n- 8초 smoke hover 실행은 Floating point exception으로 실패했다.\n- 따라서 현재 모델은 aircraft 구성과 초기 로딩 검증까지 완료된 상태이며, 안정 hover 모델로 간주하면 안 된다.\n\n## 필요한 후속 작업\n\n- 실제 CAD에서 nose datum 기준 CG와 inertia tensor를 export한다.\n- DATCOM moment reference point를 확인하고 AERORP가 CG와 다른 경우 Metrics.xml을 수정한다.\n- lift rotor front/rear collective split을 FlightControl.xml에 반영한다.\n- ground reaction의 spring, damping, contact 위치를 정지 자세 기준으로 재튜닝한다.\n- 실제 모터, 프롭, ESC, 배터리 전압 강하 데이터를 확보해 제품 기반 motor/prop XML을 재보정한다. 특히 cruise는 원래 의도한 Falcon C2E 20x10 직접 thrust/power sheet 확보 후 AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml의 임시 적용값을 교체해야 한다.\n- 조종면 최대 deflection과 부호를 실측한 뒤 DATCOM control property와 연결한다.\n'
    write(AIRCRAFT_DIR / "ASSUMPTIONS_AND_LIMITATIONS.md", assumptions)

    source_matrix = AIRCRAFT_DIR / "SOURCE_MATRIX.csv"
    with source_matrix.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["kind", "name", "value", "unit", "source", "note"])
        writer.writerow(["mass", "total_mass", f"{mass_kg:.6f}", "kg", str(XLSX_PATH), "displayed E59"])
        writer.writerow(["mass", "cg_x", f"{cg_x:.6f}", "m", str(XLSX_PATH), "from H60, transformed to JSBSim x aft"])
        writer.writerow(["mass", "cg_y", f"{cg_y:.6f}", "m", str(XLSX_PATH), "computed from listed point masses, transformed to JSBSim y right"])
        writer.writerow(["mass", "cg_z", f"{cg_z:.6f}", "m", str(XLSX_PATH), "from G60, transformed to JSBSim z up"])
        writer.writerow(["mass", "ixx", f"{jsb_ixx:.6f}", "kg*m2", str(XLSX_PATH), "sheet E65 remapped to JSBSim x axis"])
        writer.writerow(["mass", "iyy", f"{jsb_iyy:.6f}", "kg*m2", str(XLSX_PATH), "sheet E63 remapped to JSBSim y axis"])
        writer.writerow(["mass", "izz", f"{jsb_izz:.6f}", "kg*m2", str(XLSX_PATH), "sheet E64 remapped to JSBSim z axis"])
        for key, value in bbox.items():
            writer.writerow(["geometry", key, f"{value:.6f}", "mm/count", str(STEP_PATH), "raw STEP CARTESIAN_POINT bounding box"])
        writer.writerow(["propulsion", "lift_rotor_static_max_target_each", f"{lift_max:.6f}", "N", "mass based sizing", "2.0 total T/W divided across four rotors"])
        writer.writerow(["propulsion", "lift_rotor_static_hover_each", f"{lift_hover:.6f}", "N", "mass based sizing", "aircraft weight divided across four rotors"])
        writer.writerow(["propulsion", "lift_rotor_hover_throttle_estimate", f"{lift_hover_throttle:.6f}", "norm", "mass based sizing", "sqrt(hover thrust / max thrust)"])
        writer.writerow([])
        writer.writerow(["component", "system", "part", "mass_g", "source_F_mm", "source_G_mm", "source_H_mm", "jsbsim_x_m", "jsbsim_y_m", "jsbsim_z_m"])
        for c in components:
            writer.writerow([
                "component",
                c["system"],
                c["part"],
                f'{float(c["mass_g"]):.6f}',
                f'{float(c["source_F_mm"]):.6f}',
                f'{float(c["source_G_mm"]):.6f}',
                f'{float(c["source_H_mm"]):.6f}',
                f'{float(c["jsbsim_x_m"]):.6f}',
                f'{float(c["jsbsim_y_m"]):.6f}',
                f'{float(c["jsbsim_z_m"]):.6f}',
            ])

    lift_motor = f"""{xml_header()}<brushless_dc_motor name="Hobbywing V6212 180KV lift motor">
  <documentation>Hobbywing V6212-180KV lift motor 기준 모델이다. 공식 공개 사양의 12S 46V, KV 180, 무부하전류 1.53A, 최대전류 58A, 저항 84mOhm, 질량 292g을 반영했다.</documentation>
  <velocityconstant>180</velocityconstant>
  <coilresistance>0.084</coilresistance>
  <noloadcurrent>1.53</noloadcurrent>
  <maxvolts>46.0</maxvolts>
</brushless_dc_motor>
"""
    write(ENGINE_DIR / "AD3000_lift_motor_V6212_180KV.xml", lift_motor)

    lift_prop = f"""{xml_header()}<propeller name="Hobbywing VSC 22.1x7.4 lift prop" version="1.1">
  <documentation>DB 정리.xlsx의 기체 Spec 시트에 정리된 Hobbywing V6212 180KV와 VSC 22.1x7.4 46V 공식 pull test 표 전체 33-100% throttle 행을 기준으로 한다. 전체 22개 행 평균으로 Ct0=0.07460, Cp0=0.02795를 환산했다. 주의: 기체 Spec 시트의 pull test 데이터는 정지 시험(static test)이므로 전진속도 V=0, 전진비 J=0 조건의 Ct/Cp만 직접 산출할 수 있다. 현재 XML의 J>0 C_THRUST/C_POWER 값은 전진비별 실측 데이터가 아니라 J=0 Ct/Cp에 일반적인 임시 advance-ratio 감소 shape를 곱한 초기 가정이다. 정확한 전진비 table을 만들려면 airspeed, RPM, thrust, power가 함께 있는 prop performance map이 필요하다.</documentation>
  <ixx unit="KG*M2">0.0030</ixx>
  <diameter unit="IN">22.1</diameter>
  <numblades>2</numblades>
  <constspeed>0</constspeed>
  <table name="C_THRUST" type="internal">
    <tableData>
      0.00  0.07460
      0.10  0.07385
      0.20  0.07087
      0.30  0.06565
      0.40  0.05819
      0.50  0.04774
      0.60  0.03506
      0.70  0.02089
      0.80  0.00746
      0.90  0.00000
      1.00  -0.00298
    </tableData>
  </table>
  <table name="C_POWER" type="internal">
    <tableData>
      0.00  0.02795
      0.10  0.02767
      0.20  0.02683
      0.30  0.02544
      0.40  0.02348
      0.50  0.02068
      0.60  0.01733
      0.70  0.01342
      0.80  0.00894
      0.90  0.00447
      1.00  0.00112
    </tableData>
  </table>
</propeller>
"""
    write(ENGINE_DIR / "AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml", lift_prop)

    pusher_motor = f"""{xml_header()}<brushless_dc_motor name="Hobbywing V6215 210KV cruise motor">
  <documentation>Hobbywing V6215-210KV cruise motor 기준 모델이다. 공식 공개 사양의 12S, KV 210, 무부하전류 2.6A, 최대전류 81A, 저항 48.2mOhm, 질량 354g을 반영했다.</documentation>
  <velocityconstant>210</velocityconstant>
  <coilresistance>0.0482</coilresistance>
  <noloadcurrent>2.60</noloadcurrent>
  <maxvolts>46.0</maxvolts>
</brushless_dc_motor>
"""
    write(ENGINE_DIR / "AD3000_cruise_motor_V6215_210KV.xml", pusher_motor)

    pusher_prop = f"""{xml_header()}<propeller name="Hobbywing VSC 22.1x7.4 cruise prop" version="1.1">
  <documentation>AD3000 실기 cruise prop 의도 규격은 기체 Spec 시트의 Curise Prop 항목에 있는 20*10이다. 다만 해당 조합의 공개 thrust/power sheet가 기체 Spec 시트에 없으므로, 우선 같은 시트에 정리된 Hobbywing V6215 210KV와 VSC 22.1x7.4 46V 공식 pull test 표 전체 33-100% throttle 행을 사용한다. 전체 22개 행 평균으로 Ct0=0.07388, Cp0=0.02772를 환산했다. 주의: 기체 Spec 시트의 pull test 데이터는 정지 시험(static test)이므로 전진속도 V=0, 전진비 J=0 조건의 Ct/Cp만 직접 산출할 수 있다. 현재 XML의 J>0 C_THRUST/C_POWER 값은 전진비별 실측 데이터가 아니라 J=0 Ct/Cp에 일반적인 임시 advance-ratio 감소 shape를 곱한 초기 가정이다. 정확한 전진비 table을 만들려면 airspeed, RPM, thrust, power가 함께 있는 prop performance map이 필요하다.</documentation>
  <ixx unit="KG*M2">0.0030</ixx>
  <diameter unit="IN">22.1</diameter>
  <numblades>2</numblades>
  <constspeed>0</constspeed>
  <table name="C_THRUST" type="internal">
    <tableData>
      0.00  0.07388
      0.10  0.07314
      0.20  0.07018
      0.30  0.06501
      0.40  0.05762
      0.50  0.04728
      0.60  0.03472
      0.70  0.02069
      0.80  0.00739
      0.90  0.00000
      1.00  -0.00296
    </tableData>
  </table>
  <table name="C_POWER" type="internal">
    <tableData>
      0.00  0.02772
      0.10  0.02745
      0.20  0.02662
      0.30  0.02523
      0.40  0.02329
      0.50  0.02052
      0.60  0.01719
      0.70  0.01331
      0.80  0.00887
      0.90  0.00444
      1.00  0.00111
    </tableData>
  </table>
</propeller>
"""
    write(ENGINE_DIR / "AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml", pusher_prop)

    workflow_engine_dir = WORKFLOW_ROOT / "engine_variants" / AIRCRAFT_NAME
    workflow_engine_dir.mkdir(parents=True, exist_ok=True)
    for engine_file in [
        "AD3000_lift_motor_V6212_180KV.xml",
        "AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml",
        "AD3000_cruise_motor_V6215_210KV.xml",
        "AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml",
    ]:
        shutil.copy2(ENGINE_DIR / engine_file, workflow_engine_dir / engine_file)

    if WORKFLOW_VARIANT_DIR.exists():
        shutil.rmtree(WORKFLOW_VARIANT_DIR)
    shutil.copytree(AIRCRAFT_DIR, WORKFLOW_VARIANT_DIR)

    write(WORKFLOW_SCRIPT_DIR / "initial_condition" / "1.0__ground_init.xml", init_xml)
    runscript = f"""{xml_header()}<?xml-stylesheet type="text/xsl" href="http://jsbsim.sf.net/JSBSimScript.xsl"?>
<runscript xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="http://jsbsim.sf.net/JSBSimScript.xsd"
  name="AD3000 smoke hover sizing run">
  <use aircraft="AD3000" initialize="initGrnd"/>
  <run start="0.0" end="8.0" dt="0.004">
    <event name="Initialize controls">
      <condition>simulation/frame le 1</condition>
      <set name="fcs/throttle-cmd-norm" value="0.0"/>
      <set name="fcs/pusher-throttle-cmd-norm" value="0.0"/>
      <set name="fcs/aileron-cmd-norm" value="0.0"/>
      <set name="fcs/elevator-cmd-norm" value="0.0"/>
      <set name="fcs/rudder-cmd-norm" value="0.0"/>
      <set name="fcs/fw-aileron-cmd-norm" value="0.0"/>
      <set name="fcs/fw-elevator-cmd-norm" value="0.0"/>
      <set name="fcs/fw-rudder-cmd-norm" value="0.0"/>
    </event>
    <event name="Lift rotor static thrust check">
      <condition>simulation/sim-time-sec ge 1.0</condition>
      <set name="fcs/throttle-cmd-norm" value="{lift_hover_throttle:.3f}"/>
    </event>
  </run>
  <output name="AD3000_smoke_hover.csv" type="CSV" rate="50">
    <property>simulation/sim-time-sec</property>
    <property>position/h-agl-ft</property>
    <property>velocities/vc-kts</property>
    <property>attitude/phi-rad</property>
    <property>attitude/theta-rad</property>
    <property>propulsion/engine[0]/propeller-rpm</property>
    <property>propulsion/engine[0]/thrust-lbs</property>
    <property>propulsion/engine[1]/propeller-rpm</property>
    <property>propulsion/engine[1]/thrust-lbs</property>
    <property>propulsion/engine[2]/propeller-rpm</property>
    <property>propulsion/engine[2]/thrust-lbs</property>
    <property>propulsion/engine[3]/propeller-rpm</property>
    <property>propulsion/engine[3]/thrust-lbs</property>
    <property>propulsion/engine[4]/propeller-rpm</property>
    <property>propulsion/engine[4]/thrust-lbs</property>
  </output>
</runscript>
"""
    write(WORKFLOW_SCRIPT_DIR / "runscript" / "1.0__smoke_hover_run.xml", runscript)
    write(JSBSIM_ROOT / "scripts" / "AD3000_smoke_hover_run.xml", runscript)


if __name__ == "__main__":
    main()
