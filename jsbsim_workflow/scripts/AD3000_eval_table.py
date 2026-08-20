#!/usr/bin/env python3
"""AD3000 XML table 보간값 확인 도구.

예시:
  # propeller 1D table: J=0.45에서 C_THRUST 확인
  python3 AD3000_eval_table.py \
    --xml /home/junyeopkwon/jsbsim/engine/AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml \
    --table C_THRUST --x 0.45

  # Aero.xml function table: alpha=2 deg, mach=0.2에서 CL_base table 값 확인
  python3 AD3000_eval_table.py \
    --xml /home/junyeopkwon/jsbsim/aircraft/AD3000/Aero.xml \
    --function aero/coefficient/CL_base \
    --var aero/alpha-deg=2 --var velocities/mach=0.2

  # 3D aero table: alpha=2 deg, elevator=7.5 deg, mach=0.15에서 CL_de 확인
  python3 AD3000_eval_table.py \
    --xml /home/junyeopkwon/jsbsim/aircraft/AD3000/Aero.xml \
    --function aero/coefficient/CL_de \
    --var aero/alpha-deg=2 --var fcs/elevator-pos-deg=7.5 --var velocities/mach=0.15
"""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Table2D:
    columns: list[float]
    rows: list[float]
    values: list[list[float]]
    break_point: float | None = None


def parse_vars(items: list[str]) -> dict[str, float]:
    out: dict[str, float] = {}
    for item in items:
        if '=' not in item:
            raise SystemExit(f'--var 형식 오류: {item!r}. 예: aero/alpha-deg=2')
        key, value = item.split('=', 1)
        out[key] = float(value)
    return out


def numbers(line: str) -> list[float]:
    return [float(x) for x in line.split()]


def parse_table_data(node: ET.Element) -> Table2D:
    text = node.text or ''
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        raise ValueError('tableData가 비어 있음')
    columns = numbers(lines[0])
    rows: list[float] = []
    values: list[list[float]] = []
    for line in lines[1:]:
        vals = numbers(line)
        if len(vals) != len(columns) + 1:
            raise ValueError(f'tableData 행 길이 오류: {line!r}')
        rows.append(vals[0])
        values.append(vals[1:])
    bp = node.attrib.get('breakPoint')
    return Table2D(columns=columns, rows=rows, values=values, break_point=float(bp) if bp is not None else None)


def clamp_segment(points: list[float], x: float) -> tuple[int, int, float, bool]:
    if len(points) < 2:
        return 0, 0, 0.0, x == points[0]
    if x <= points[0]:
        return 0, 1, 0.0, x == points[0]
    if x >= points[-1]:
        return len(points)-2, len(points)-1, 1.0, x == points[-1]
    for i in range(len(points)-1):
        lo, hi = points[i], points[i+1]
        if lo <= x <= hi:
            frac = 0.0 if hi == lo else (x - lo) / (hi - lo)
            return i, i+1, frac, x == lo or x == hi
    raise RuntimeError('segment 탐색 실패')


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def interp_table(table: Table2D, row_value: float, col_value: float) -> tuple[float, str]:
    r0, r1, rt, row_exact = clamp_segment(table.rows, row_value)
    c0, c1, ct, col_exact = clamp_segment(table.columns, col_value)
    v00 = table.values[r0][c0]
    v01 = table.values[r0][c1]
    v10 = table.values[r1][c0]
    v11 = table.values[r1][c1]
    row0 = lerp(v00, v01, ct)
    row1 = lerp(v10, v11, ct)
    value = lerp(row0, row1, rt)
    detail = (
        f'row {table.rows[r0]}..{table.rows[r1]} t={rt:.6g}, '
        f'column {table.columns[c0]}..{table.columns[c1]} t={ct:.6g}, '
        f'grid=({v00:g}, {v01:g}, {v10:g}, {v11:g})'
    )
    if row_exact and col_exact:
        detail += ', 정확한 breakpoint 값'
    return value, detail


def interp_breakpoint(tables: list[Table2D], table_value: float, row_value: float, col_value: float) -> tuple[float, str]:
    tables = sorted(tables, key=lambda t: t.break_point if t.break_point is not None else 0.0)
    breakpoints = [t.break_point for t in tables]
    if any(bp is None for bp in breakpoints):
        raise ValueError('breakPoint 없는 tableData가 섞여 있음')
    bps = [float(bp) for bp in breakpoints]
    if len(tables) == 1:
        value, detail = interp_table(tables[0], row_value, col_value)
        return value, f'breakPoint {bps[0]} 단일 table, {detail}'
    b0, b1, bt, exact = clamp_segment(bps, table_value)
    v0, d0 = interp_table(tables[b0], row_value, col_value)
    v1, d1 = interp_table(tables[b1], row_value, col_value)
    value = lerp(v0, v1, bt)
    detail = f'table breakPoint {bps[b0]}..{bps[b1]} t={bt:.6g}; low=({v0:g}; {d0}); high=({v1:g}; {d1})'
    if exact:
        detail += ', 정확한 table breakpoint 값'
    return value, detail


def find_named_internal_table(root: ET.Element, table_name: str) -> ET.Element:
    for table in root.iter('table'):
        if table.attrib.get('name') == table_name:
            return table
    raise SystemExit(f'table name={table_name!r}를 찾지 못함')


def find_function_table(root: ET.Element, function_name: str) -> ET.Element:
    for func in root.iter('function'):
        if func.attrib.get('name') == function_name:
            table = func.find('.//table')
            if table is None:
                raise SystemExit(f'function {function_name!r} 안에 table이 없음')
            return table
    raise SystemExit(f'function name={function_name!r}를 찾지 못함')


def eval_internal_table(root: ET.Element, table_name: str, x: float) -> tuple[float, str]:
    table = find_named_internal_table(root, table_name)
    data = table.find('tableData')
    if data is None or data.text is None:
        raise SystemExit(f'{table_name} tableData가 없음')
    lines = [line.strip() for line in data.text.splitlines() if line.strip()]
    xs: list[float] = []
    ys: list[float] = []
    for line in lines:
        vals = numbers(line)
        if len(vals) != 2:
            raise SystemExit(f'1D table 행은 2개 값이어야 함: {line!r}')
        xs.append(vals[0])
        ys.append(vals[1])
    i0, i1, t, exact = clamp_segment(xs, x)
    value = lerp(ys[i0], ys[i1], t)
    detail = f'x {xs[i0]}..{xs[i1]} t={t:.6g}, y={ys[i0]:g}..{ys[i1]:g}'
    if exact:
        detail += ', 정확한 breakpoint 값'
    return value, detail


def eval_function_table(root: ET.Element, function_name: str, var_values: dict[str, float]) -> tuple[float, str]:
    table = find_function_table(root, function_name)
    independent = table.findall('independentVar')
    by_lookup = {node.attrib.get('lookup', ''): (node.text or '').strip() for node in independent}
    table_data = table.findall('tableData')
    if not table_data:
        raise SystemExit(f'{function_name} tableData가 없음')
    row_var = by_lookup.get('row')
    col_var = by_lookup.get('column')
    table_var = by_lookup.get('table')
    if row_var is None or col_var is None:
        raise SystemExit(f'{function_name}에는 row/column independentVar가 필요함')
    missing = [name for name in [row_var, col_var, table_var] if name and name not in var_values]
    if missing:
        raise SystemExit(f'필요한 --var가 없음: {", ".join(missing)}')
    parsed = [parse_table_data(node) for node in table_data]
    if table_var:
        return interp_breakpoint(parsed, var_values[table_var], var_values[row_var], var_values[col_var])
    if len(parsed) != 1:
        raise SystemExit(f'{function_name}에 tableVar 없이 tableData가 여러 개 있음')
    return interp_table(parsed[0], var_values[row_var], var_values[col_var])


def main() -> int:
    parser = argparse.ArgumentParser(description='AD3000 XML table 보간값 확인')
    parser.add_argument('--xml', required=True, type=Path, help='검사할 XML 파일')
    parser.add_argument('--table', help='propeller C_THRUST/C_POWER 같은 1D table name')
    parser.add_argument('--function', help='Aero.xml function name')
    parser.add_argument('--x', type=float, help='1D table 입력값. prop table에서는 advance ratio J로 보면 됨')
    parser.add_argument('--var', action='append', default=[], help='function table 입력값. 예: aero/alpha-deg=2')
    args = parser.parse_args()

    root = ET.parse(args.xml).getroot()
    if args.table:
        if args.x is None:
            raise SystemExit('--table 사용 시 --x가 필요함')
        value, detail = eval_internal_table(root, args.table, args.x)
        print(f'XML: {args.xml}')
        print(f'table: {args.table}')
        print(f'input x: {args.x}')
        print(f'value: {value:.10g}')
        print(f'interpolation: {detail}')
        return 0
    if args.function:
        value, detail = eval_function_table(root, args.function, parse_vars(args.var))
        print(f'XML: {args.xml}')
        print(f'function: {args.function}')
        print(f'value: {value:.10g}')
        print(f'interpolation: {detail}')
        return 0
    raise SystemExit('--table 또는 --function 중 하나가 필요함')


if __name__ == '__main__':
    raise SystemExit(main())
