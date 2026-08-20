from __future__ import annotations

import csv
import re
import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from create_workflow_excel import (
    cell_ref,
    content_types_xml,
    root_rels_xml,
    styles_xml,
    workbook_rels_xml,
    workbook_xml,
    worksheet_xml,
)


WORKFLOW = Path(__file__).resolve().parents[1]
SCRIPTS = WORKFLOW / "scripts"
LOGS = WORKFLOW / "logs"
GENERATED_RUNSCRIPTS = LOGS / "generated_runscripts"
PLOTS = WORKFLOW / "plots"
OUT = WORKFLOW / "workflow_all_cases_initial_settings.xlsx"

COMMON_INIT_TAGS = [
    "vt",
    "vc",
    "ubody",
    "vbody",
    "wbody",
    "latitude",
    "longitude",
    "altitude",
    "elevation",
    "phi",
    "theta",
    "psi",
    "gamma",
    "running",
    "hwind",
    "xwind",
]


def safe_text(el):
    return (el.text or "").strip() if el is not None else ""


def aircraft_from_name(name: str) -> str:
    low = name.lower()
    if "__" in low:
        low = low.split("__", 1)[1]
    if low.startswith("ball_builtin"):
        return "ball"
    if low.startswith("ball_"):
        return "ball_validated"
    if low.startswith("c172p"):
        return "c172p"
    if low.startswith("c172x"):
        return "c172x"
    if low.startswith("737"):
        return "737"
    return low.split("_")[0] if "_" in low else "other"


def scenario_from_name(name: str) -> str:
    stem = Path(name).stem
    if "__" in stem:
        stem = stem.split("__", 1)[1]
    for suffix in ["_run", "_init", "_raw", "_si"]:
        stem = re.sub(re.escape(suffix) + r"(_\d+)?$", "", stem)
    stem = re.sub(r"_\d{8,}$", "", stem)
    stem = re.sub(r"_\d{6}$", "", stem)
    return stem


def parse_xml(path: Path):
    try:
        return ET.fromstring(path.read_text(encoding="utf-8", errors="replace"))
    except Exception:
        return None


def parse_init(path: Path, linked_aircraft=""):
    root = parse_xml(path)
    if root is None or root.tag != "initialize":
        return None
    row = {
        "aircraft": linked_aircraft or aircraft_from_name(path.name),
        "scenario": scenario_from_name(path.name),
        "file": path.name,
        "init_name": root.attrib.get("name", ""),
    }
    for tag in COMMON_INIT_TAGS:
        el = root.find(tag)
        row[tag] = safe_text(el)
        row[f"{tag}_unit"] = el.attrib.get("unit", "") if el is not None else ""
        if tag == "latitude":
            row["latitude_type"] = el.attrib.get("type", "") if el is not None else ""
    extra = []
    for child in root:
        if child.tag not in COMMON_INIT_TAGS:
            extra.append(f"{child.tag}={safe_text(child)}")
    row["extra"] = "; ".join(extra)
    return row


def parse_run(path: Path):
    root = parse_xml(path)
    if root is None or root.tag != "runscript":
        return None
    use = root.find("use")
    run = root.find("run")
    aircraft = use.attrib.get("aircraft", "") if use is not None else aircraft_from_name(path.name)
    initialize = use.attrib.get("initialize", "") if use is not None else ""
    events = []
    sets = []
    outputs = []
    if run is not None:
        for ev in run.findall("event"):
            events.append(ev.attrib.get("name", ""))
            for st in ev.findall("set"):
                sets.append(f"{st.attrib.get('name','')}={st.attrib.get('value','')}")
        for out in root.findall("output"):
            outputs.append(out.attrib.get("name", ""))
    return {
        "aircraft": aircraft,
        "scenario": scenario_from_name(path.name),
        "file": path.name,
        "runscript_name": root.attrib.get("name", ""),
        "description": safe_text(root.find("description")),
        "initialize": initialize,
        "init_file": Path(initialize).name if initialize else "",
        "start": run.attrib.get("start", "") if run is not None else "",
        "end": run.attrib.get("end", "") if run is not None else "",
        "dt": run.attrib.get("dt", "") if run is not None else "",
        "event_count": len(events),
        "events": "; ".join(events[:12]),
        "set_count": len(sets),
        "sets_sample": "; ".join(sets[:20]),
        "outputs": "; ".join(outputs),
    }


def read_last_csv_row(path: Path):
    try:
        with path.open("r", encoding="utf-8", errors="replace", newline="") as f:
            count = 0
            last = {}
            for row in csv.DictReader(f):
                count += 1
                last = row
        return last, count
    except Exception:
        return {}, 0


def csv_index_rows():
    rows = [[
        "aircraft",
        "scenario",
        "kind",
        "file",
        "modified",
        "rows",
        "last_time_s",
        "last_altitude_m",
        "last_local_D_m",
        "last_v_total_mps",
        "last_v_n_mps",
        "last_v_e_mps",
        "last_v_d_mps",
        "last_lat_deg",
        "last_lon_deg",
    ]]
    for path in sorted((LOGS / "csv").rglob("*.csv"), key=lambda p: str(p).lower()):
        rel = path.relative_to(LOGS / "csv")
        kind = "si" if "si" in rel.parts else "raw" if "raw" in rel.parts else "summary"
        last, row_count = read_last_csv_row(path)
        name = path.name
        rows.append([
            aircraft_from_name(name),
            scenario_from_name(name),
            kind,
            str(rel),
            path.stat().st_mtime,
            row_count,
            last.get("time_s", last.get("Time", "")),
            last.get("altitude_m", last.get("h_sl_m", "")),
            last.get("local_D_m", last.get("h_agl_m", "")),
            last.get("v_total_mps", last.get("vt_mps", "")),
            last.get("v_n_mps", last.get("v_north_mps", "")),
            last.get("v_e_mps", last.get("v_east_mps", "")),
            last.get("v_d_mps", last.get("v_down_mps", "")),
            last.get("lat_deg", last.get("lat_gc_deg", "")),
            last.get("lon_deg", last.get("lon_gc_deg", "")),
        ])
    return rows


def aircraft_from_path(base: Path, path: Path) -> str:
    try:
        rel = path.relative_to(base)
    except ValueError:
        return aircraft_from_name(path.name)
    if base == SCRIPTS and len(rel.parts) > 1:
        return rel.parts[0]
    return aircraft_from_name(path.name)


def file_index_rows(base: Path, label: str):
    rows = [["aircraft", "scenario", "kind", "relative_path", "size_bytes", "modified"]]
    for path in sorted(base.rglob("*"), key=lambda p: str(p).lower()):
        if path.is_file():
            rel = path.relative_to(base)
            rows.append([
                aircraft_from_path(base, path),
                scenario_from_name(path.name),
                label,
                str(rel),
                path.stat().st_size,
                path.stat().st_mtime,
            ])
    return rows


def by_aircraft_rows(runs, inits, csv_rows, plot_rows):
    counts = defaultdict(lambda: {"runs": 0, "inits": 0, "csv": 0, "plots": 0, "scenarios": set()})
    for r in runs:
        counts[r["aircraft"]]["runs"] += 1
        counts[r["aircraft"]]["scenarios"].add(r["scenario"])
    for r in inits:
        counts[r["aircraft"]]["inits"] += 1
        counts[r["aircraft"]]["scenarios"].add(r["scenario"])
    for r in csv_rows[1:]:
        counts[r[0]]["csv"] += 1
        counts[r[0]]["scenarios"].add(r[1])
    for r in plot_rows[1:]:
        counts[r[0]]["plots"] += 1
        counts[r[0]]["scenarios"].add(r[1])
    rows = [["aircraft", "init_count", "run_count", "csv_count", "plot_count", "scenario_count", "scenarios"]]
    for ac in sorted(counts):
        c = counts[ac]
        rows.append([ac, c["inits"], c["runs"], c["csv"], c["plots"], len(c["scenarios"]), "; ".join(sorted(c["scenarios"]))])
    return rows


def rows_from_dicts(dicts, columns):
    rows = [columns]
    for d in dicts:
        rows.append([d.get(c, "") for c in columns])
    return rows


def build_sheets():
    run_paths = sorted(SCRIPTS.rglob("*_run.xml")) + sorted(GENERATED_RUNSCRIPTS.glob("*.xml"))
    runs = [r for p in run_paths if (r := parse_run(p))]
    run_aircraft_by_init = {r["init_file"]: r["aircraft"] for r in runs if r["init_file"]}
    inits = []
    for p in sorted(SCRIPTS.rglob("*.xml")):
        if "_run" in p.name or p.name == "nonrotating_earth.xml":
            continue
        linked = run_aircraft_by_init.get(p.name, "")
        row = parse_init(p, linked)
        if row:
            inits.append(row)

    csv_rows = csv_index_rows()
    plot_rows = file_index_rows(PLOTS, "plot")
    script_rows = file_index_rows(SCRIPTS, "script")
    generated_runscript_rows = file_index_rows(GENERATED_RUNSCRIPTS, "generated_runscript")

    run_cols = [
        "aircraft",
        "scenario",
        "file",
        "runscript_name",
        "description",
        "initialize",
        "init_file",
        "start",
        "end",
        "dt",
        "event_count",
        "events",
        "set_count",
        "sets_sample",
        "outputs",
    ]
    init_cols = [
        "aircraft",
        "scenario",
        "file",
        "init_name",
        "vt",
        "vt_unit",
        "vc",
        "vc_unit",
        "ubody",
        "ubody_unit",
        "vbody",
        "vbody_unit",
        "wbody",
        "wbody_unit",
        "latitude",
        "latitude_unit",
        "latitude_type",
        "longitude",
        "longitude_unit",
        "altitude",
        "altitude_unit",
        "elevation",
        "elevation_unit",
        "phi",
        "theta",
        "psi",
        "running",
        "hwind",
        "xwind",
        "extra",
    ]
    sheets = {
        "README": [
            ["항목", "내용"],
            ["파일 목적", "workflow 폴더의 모든 케이스를 기체별로 구분해 초기값, run 설정, 결과 파일을 비교"],
            ["포함 대상", "ball, ball_validated, c172p, c172x, 737 등 workflow 폴더 내 파일 전체"],
            ["제외", "WGS84 손계산/검산 수식 시트는 포함하지 않음"],
            ["원본 폴더", str(WORKFLOW)],
            ["생성 파일", str(OUT)],
        ],
        "By Aircraft": by_aircraft_rows(runs, inits, csv_rows, plot_rows),
        "Initial Conditions": rows_from_dicts(inits, init_cols),
        "Runs": rows_from_dicts(runs, run_cols),
        "CSV Results": csv_rows,
        "Plots": plot_rows,
        "Scripts": script_rows,
        "Generated Runscripts": generated_runscript_rows,
    }

    grouped = defaultdict(list)
    for row in runs:
        grouped[row["aircraft"]].append(["RUN", row["scenario"], row["file"], row["init_file"], row["start"], row["end"], row["dt"], row["events"]])
    for row in inits:
        grouped[row["aircraft"]].append(["INIT", row["scenario"], row["file"], row["latitude"], row["longitude"], row["altitude"], row["vt"] or row["ubody"], row["psi"]])
    for ac in sorted(grouped):
        name = ac[:28] if ac else "other"
        rows = [["type", "scenario", "file", "field1", "field2", "field3", "field4", "field5"]]
        rows.extend(grouped[ac])
        sheets[f"AC {name}"] = rows
    return sheets


def main():
    sheets = build_sheets()
    sheet_names = list(sheets.keys())
    widths = {1: 18, 2: 28, 3: 34, 4: 40, 5: 24, 6: 24, 7: 24, 8: 50, 9: 24, 10: 24, 11: 16, 12: 60, 13: 16, 14: 80, 15: 42}
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types_xml(sheet_names))
        z.writestr("_rels/.rels", root_rels_xml())
        z.writestr("xl/workbook.xml", workbook_xml(sheet_names))
        z.writestr("xl/_rels/workbook.xml.rels", workbook_rels_xml(sheet_names))
        z.writestr("xl/styles.xml", styles_xml())
        for i, name in enumerate(sheet_names, start=1):
            z.writestr(f"xl/worksheets/sheet{i}.xml", worksheet_xml(sheets[name], widths))
    print(OUT)


if __name__ == "__main__":
    main()
