#!/usr/bin/env python3
"""AD3000 JSBSim 구성값 검증 스크립트.

목적:
- AD3000.xml이 include한 하위 XML 파일이 존재하는지 확인한다.
- Mass.xml 값이 SOURCE_MATRIX.csv의 기준값과 일치하는지 확인한다.
- Propulsion.xml의 engine/thruster 참조와 위치가 source component 좌표와 일치하는지 확인한다.
- 제품 기반 motor/prop XML 값이 PROPULSION_SOURCE_DATA.csv에서 계산한 Ct/Cp와 일치하는지 확인한다.

이 스크립트는 비행 안정성 검증이 아니라, XML에 적용된 수치와 참조 관계의 적용 여부를 검증한다.
"""

from __future__ import annotations

import argparse
import csv
import math
import subprocess
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

JSBSIM_ROOT = Path('/home/junyeopkwon/jsbsim')
AIRCRAFT = 'AD3000'
AIRCRAFT_DIR = JSBSIM_ROOT / 'aircraft' / AIRCRAFT
ENGINE_DIR = JSBSIM_ROOT / 'engine'
SOURCE_MATRIX = AIRCRAFT_DIR / 'SOURCE_MATRIX.csv'
PROPULSION_SOURCE = AIRCRAFT_DIR / 'PROPULSION_SOURCE_DATA.csv'

EXPECTED_INCLUDES = {
    'metrics': 'Metrics.xml',
    'mass_balance': 'Mass.xml',
    'ground_reactions': 'Gear.xml',
    'propulsion': 'Propulsion.xml',
    'system': 'Effectors.xml',
    'flight_control': 'FlightControl.xml',
    'aerodynamics': 'Aero.xml',
}

EXPECTED_MOTORS = {
    'AD3000_lift_motor_V6212_180KV': {
        'velocityconstant': 180.0,
        'coilresistance': 0.084,
        'noloadcurrent': 1.53,
        'maxvolts': 46.0,
    },
    'AD3000_cruise_motor_V6215_210KV': {
        'velocityconstant': 210.0,
        'coilresistance': 0.0482,
        'noloadcurrent': 2.60,
        'maxvolts': 46.0,
    },
}

EXPECTED_ROTORS = [
    ('lift front right', 'AD3000_lift_motor_V6212_180KV', 'AD3000_lift_prop_Hobbywing_VSC_22x7_4', 'VTOL 프로펠러 #3', 1.0),
    ('lift aft left', 'AD3000_lift_motor_V6212_180KV', 'AD3000_lift_prop_Hobbywing_VSC_22x7_4', 'VTOL 프로펠러 #1', 1.0),
    ('lift front left', 'AD3000_lift_motor_V6212_180KV', 'AD3000_lift_prop_Hobbywing_VSC_22x7_4', 'VTOL 프로펠러 #2', -1.0),
    ('lift aft right', 'AD3000_lift_motor_V6212_180KV', 'AD3000_lift_prop_Hobbywing_VSC_22x7_4', 'VTOL 프로펠러 #4', -1.0),
    ('cruise pusher', 'AD3000_cruise_motor_V6215_210KV', 'AD3000_cruise_prop_Hobbywing_VSC_22x7_4', '고정익 프로펠러', 1.0),
]

EXPECTED_PROP_SOURCE = {
    'AD3000_lift_prop_Hobbywing_VSC_22x7_4': 'V6212 180KV + VSC 22.1x7.4',
    'AD3000_cruise_prop_Hobbywing_VSC_22x7_4': 'V6215 210KV + VSC 22.1x7.4',
}


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str


class Checker:
    def __init__(self, tolerance: float = 1e-4) -> None:
        self.tolerance = tolerance
        self.results: list[CheckResult] = []

    def pass_(self, name: str, detail: str) -> None:
        self.results.append(CheckResult(name, True, detail))

    def fail(self, name: str, detail: str) -> None:
        self.results.append(CheckResult(name, False, detail))

    def check_close(self, name: str, actual: float, expected: float, tol: float | None = None, unit: str = '') -> None:
        limit = self.tolerance if tol is None else tol
        delta = abs(actual - expected)
        suffix = f' {unit}' if unit else ''
        if delta <= limit:
            self.pass_(name, f'actual={actual:.8g}{suffix}, expected={expected:.8g}{suffix}, delta={delta:.3g}')
        else:
            self.fail(name, f'actual={actual:.8g}{suffix}, expected={expected:.8g}{suffix}, delta={delta:.3g}, tol={limit}')

    def check_equal(self, name: str, actual: object, expected: object) -> None:
        if actual == expected:
            self.pass_(name, f'actual={actual!r}')
        else:
            self.fail(name, f'actual={actual!r}, expected={expected!r}')

    def summarize(self) -> int:
        passed = sum(1 for r in self.results if r.ok)
        failed = len(self.results) - passed
        print(f'AD3000 XML 적용값 검증 결과: PASS {passed}, FAIL {failed}')
        print('')
        for r in self.results:
            mark = 'PASS' if r.ok else 'FAIL'
            print(f'[{mark}] {r.name}: {r.detail}')
        return 0 if failed == 0 else 1


def parse_xml(path: Path) -> ET.Element:
    return ET.parse(path).getroot()


def text_float(parent: ET.Element, tag: str) -> float:
    node = parent.find(tag)
    if node is None or node.text is None:
        raise KeyError(tag)
    return float(node.text)


def location_tuple(node: ET.Element) -> tuple[float, float, float]:
    return (text_float(node, 'x'), text_float(node, 'y'), text_float(node, 'z'))


def read_source_matrix() -> tuple[dict[tuple[str, str], float], dict[str, dict[str, str]]]:
    values: dict[tuple[str, str], float] = {}
    components: dict[str, dict[str, str]] = {}
    component_fields = [
        'kind', 'system', 'part', 'mass_g', 'source_F_mm', 'source_G_mm',
        'source_H_mm', 'jsbsim_x_m', 'jsbsim_y_m', 'jsbsim_z_m',
    ]
    with SOURCE_MATRIX.open(encoding='utf-8', newline='') as f:
        for row in csv.reader(f):
            if not row or not row[0]:
                continue
            if row[0] == 'kind':
                continue
            if row[0] == 'component':
                if len(row) > 1 and row[1] == 'system':
                    continue
                if len(row) < len(component_fields):
                    continue
                item = dict(zip(component_fields, row[:len(component_fields)]))
                components[item['part']] = item
                continue
            if len(row) >= 3:
                try:
                    values[(row[0], row[1])] = float(row[2])
                except ValueError:
                    pass
    return values, components


def read_propulsion_coefficients() -> dict[str, tuple[float, float]]:
    grouped: dict[str, list[tuple[float, float]]] = {}
    with PROPULSION_SOURCE.open(encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f):
            if row.get('used_for_coefficient') and row.get('used_for_coefficient') != 'Y':
                continue
            grouped.setdefault(row['configuration'], []).append((float(row['derived_ct']), float(row['derived_cp'])))
    return {
        cfg: (
            sum(ct for ct, _ in rows) / len(rows),
            sum(cp for _, cp in rows) / len(rows),
        )
        for cfg, rows in grouped.items()
    }


def first_table_value(propeller: ET.Element, table_name: str) -> float:
    for table in propeller.findall('table'):
        if table.attrib.get('name') != table_name:
            continue
        table_data = table.findtext('tableData') or ''
        for line in table_data.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                return float(parts[1])
    raise KeyError(table_name)


def check_root_includes(checker: Checker) -> None:
    root = parse_xml(AIRCRAFT_DIR / 'AD3000.xml')
    checker.check_equal('루트 aircraft 이름', root.attrib.get('name'), AIRCRAFT)
    for tag, expected_file in EXPECTED_INCLUDES.items():
        node = root.find(tag)
        if node is None:
            checker.fail(f'AD3000.xml include {tag}', '태그가 없음')
            continue
        actual = node.attrib.get('file')
        checker.check_equal(f'AD3000.xml include {tag}', actual, expected_file)
        if actual:
            path = AIRCRAFT_DIR / actual
            if path.exists():
                checker.pass_(f'include 파일 존재 {actual}', str(path))
            else:
                checker.fail(f'include 파일 존재 {actual}', str(path))


def check_mass(checker: Checker, source_values: dict[tuple[str, str], float]) -> None:
    mass = parse_xml(AIRCRAFT_DIR / 'Mass.xml')
    checker.check_close('Mass emptywt', text_float(mass, 'emptywt'), source_values[('mass', 'total_mass')], unit='kg')
    cg = mass.find("location[@name='CG']")
    if cg is None:
        checker.fail('Mass CG location', 'CG location 태그가 없음')
    else:
        actual = location_tuple(cg)
        expected = (
            source_values[('mass', 'cg_x')],
            source_values[('mass', 'cg_y')],
            source_values[('mass', 'cg_z')],
        )
        for axis, a, e in zip('xyz', actual, expected):
            checker.check_close(f'Mass CG {axis}', a, e, unit='m')
    for key in ['ixx', 'iyy', 'izz']:
        checker.check_close(f'Mass {key}', text_float(mass, key), source_values[('mass', key)], unit='kg*m2')


def check_metrics(checker: Checker) -> None:
    text = (AIRCRAFT_DIR / 'Metrics.xml').read_text(encoding='utf-8')
    checker.check_equal('Metrics.xml XML declaration 개수', text.count('<?xml'), 1)
    metrics = parse_xml(AIRCRAFT_DIR / 'Metrics.xml')
    for tag in ['wingarea', 'wingspan', 'chord', 'wing_incidence', 'htailarea', 'vtailarea', 'htailarm', 'vtailarm']:
        try:
            value = text_float(metrics, tag)
        except KeyError:
            checker.fail(f'Metrics {tag}', '태그가 없음')
        else:
            checker.pass_(f'Metrics {tag}', f'value={value:g}')
    for loc in ['AERORP', 'EYEPOINT', 'VRP']:
        if metrics.find(f"location[@name='{loc}']") is None:
            checker.fail(f'Metrics location {loc}', '태그가 없음')
        else:
            checker.pass_(f'Metrics location {loc}', '존재')


def check_propulsion(checker: Checker, components: dict[str, dict[str, str]], coeffs: dict[str, tuple[float, float]]) -> None:
    propulsion_text = (AIRCRAFT_DIR / 'Propulsion.xml').read_text(encoding='utf-8')
    has_cruise_intent = '20*10' in propulsion_text or 'Falcon C2E 20x10' in propulsion_text
    has_public_data_note = '공개 thrust/power sheet' in propulsion_text and 'VSC 22.1x7.4' in propulsion_text
    if has_cruise_intent and has_public_data_note:
        checker.pass_('Propulsion cruise 임시 적용 주석', 'cruise 의도 prop과 VSC22.1x7.4 임시 적용이 한글 주석으로 명시됨')
    else:
        checker.fail('Propulsion cruise 임시 적용 주석', '필수 한글 주석을 찾지 못함')

    propulsion = parse_xml(AIRCRAFT_DIR / 'Propulsion.xml')
    engines = propulsion.findall('engine')
    checker.check_equal('Propulsion engine 개수', len(engines), len(EXPECTED_ROTORS))

    for idx, expected in enumerate(EXPECTED_ROTORS):
        if idx >= len(engines):
            continue
        name, engine_file, thruster_file, component_name, sense = expected
        engine = engines[idx]
        checker.check_equal(f'engine[{idx}] name', engine.attrib.get('name'), name)
        checker.check_equal(f'engine[{idx}] file', engine.attrib.get('file'), engine_file)
        thruster = engine.find('thruster')
        if thruster is None:
            checker.fail(f'engine[{idx}] thruster', 'thruster 태그가 없음')
            continue
        checker.check_equal(f'engine[{idx}] thruster file', thruster.attrib.get('file'), thruster_file)
        checker.check_close(f'engine[{idx}] sense', text_float(thruster, 'sense'), sense)
        location = thruster.find('location')
        comp = components.get(component_name)
        if location is None:
            checker.fail(f'engine[{idx}] location', 'location 태그가 없음')
        elif comp is None:
            checker.fail(f'engine[{idx}] source component {component_name}', 'SOURCE_MATRIX.csv에서 component를 찾지 못함')
        else:
            actual = location_tuple(location)
            expected_xyz = (float(comp['jsbsim_x_m']), float(comp['jsbsim_y_m']), float(comp['jsbsim_z_m']))
            for axis, a, e in zip('xyz', actual, expected_xyz):
                checker.check_close(f'engine[{idx}] location {axis}', a, e, tol=1e-5, unit='m')

    for motor_name, expected_values in EXPECTED_MOTORS.items():
        path = ENGINE_DIR / f'{motor_name}.xml'
        if not path.exists():
            checker.fail(f'motor 파일 {motor_name}', f'{path} 없음')
            continue
        motor = parse_xml(path)
        for tag, expected in expected_values.items():
            checker.check_close(f'{motor_name} {tag}', text_float(motor, tag), expected)

    for prop_name, cfg in EXPECTED_PROP_SOURCE.items():
        path = ENGINE_DIR / f'{prop_name}.xml'
        if not path.exists():
            checker.fail(f'prop 파일 {prop_name}', f'{path} 없음')
            continue
        prop = parse_xml(path)
        checker.check_close(f'{prop_name} diameter', text_float(prop, 'diameter'), 22.1, unit='inch')
        if cfg not in coeffs:
            checker.fail(f'{prop_name} source coefficient', f'PROPULSION_SOURCE_DATA.csv에 {cfg} 없음')
            continue
        expected_ct, expected_cp = coeffs[cfg]
        actual_ct = first_table_value(prop, 'C_THRUST')
        actual_cp = first_table_value(prop, 'C_POWER')
        checker.check_close(f'{prop_name} C_THRUST J=0', actual_ct, expected_ct, tol=5e-5)
        checker.check_close(f'{prop_name} C_POWER J=0', actual_cp, expected_cp, tol=5e-5)


def run_jsbsim_checks(checker: Checker) -> None:
    jsbsim = JSBSIM_ROOT / 'build/src/JSBSim'
    if not jsbsim.exists():
        checker.fail('JSBSim 실행 파일', f'{jsbsim} 없음')
        return
    cmd = [str(jsbsim), f'--root={JSBSIM_ROOT}', f'--aircraft={AIRCRAFT}', '--catalog']
    proc = subprocess.run(cmd, cwd=JSBSIM_ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=20)
    if proc.returncode == 0:
        checker.pass_('JSBSim catalog load', 'returncode=0')
    else:
        checker.fail('JSBSim catalog load', f'returncode={proc.returncode}\n{proc.stdout[-1000:]}')


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='AD3000 JSBSim XML 적용값 검증')
    parser.add_argument('--run-jsbsim', action='store_true', help='JSBSim catalog load까지 실행한다')
    args = parser.parse_args(argv)

    checker = Checker()
    source_values, components = read_source_matrix()
    coeffs = read_propulsion_coefficients()

    check_root_includes(checker)
    check_mass(checker, source_values)
    check_metrics(checker)
    check_propulsion(checker, components, coeffs)
    if args.run_jsbsim:
        run_jsbsim_checks(checker)
    return checker.summarize()


if __name__ == '__main__':
    raise SystemExit(main())
