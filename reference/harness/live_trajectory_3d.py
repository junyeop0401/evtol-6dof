#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import math
import time
from pathlib import Path

FT_TO_M = 0.3048
FPS_TO_MPS = 0.3048

TIME_COL = 'Time'
LAT_COL = '/fdm/jsbsim/position/lat-geod-deg'
LON_COL = '/fdm/jsbsim/position/long-gc-deg'
ECEF_X_COL = '/fdm/jsbsim/position/ecef-x-ft'
ECEF_Y_COL = '/fdm/jsbsim/position/ecef-y-ft'
ECEF_Z_COL = '/fdm/jsbsim/position/ecef-z-ft'
AGL_COL = '/fdm/jsbsim/position/h-agl-ft'
PHI_COL = '/fdm/jsbsim/attitude/phi-deg'
THETA_COL = '/fdm/jsbsim/attitude/theta-deg'
PSI_COL = '/fdm/jsbsim/attitude/psi-deg'
VT_COL = '/fdm/jsbsim/velocities/vt-fps'

REQUIRED_COLUMNS = [
    TIME_COL,
    LAT_COL,
    LON_COL,
    ECEF_X_COL,
    ECEF_Y_COL,
    ECEF_Z_COL,
    AGL_COL,
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Show a live 3D trajectory from a JSBSim CSV file while it is being written.')
    parser.add_argument('--csv', type=Path, required=True, help='JSBSim raw CSV path')
    parser.add_argument('--done-file', type=Path, help='File touched by the runner when JSBSim finishes')
    parser.add_argument('--title', default='JSBSim live 3D trajectory')
    parser.add_argument('--interval-ms', type=int, default=100)
    parser.add_argument('--final-hold-sec', type=float, default=3.0)
    parser.add_argument('--headless', action='store_true', help=argparse.SUPPRESS)
    parser.add_argument('--max-frames', type=int, help=argparse.SUPPRESS)
    return parser.parse_args()


def configure_matplotlib(headless: bool):
    import matplotlib

    if headless:
        matplotlib.use('Agg', force=True)
    import matplotlib.pyplot as plt

    return plt


def read_complete_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    text = path.read_text(encoding='utf-8', errors='replace')
    lines = text.splitlines()
    if not lines:
        return []
    if text and not text.endswith('\n'):
        lines = lines[:-1]
    if len(lines) < 2:
        return []
    return list(csv.DictReader(lines))


def float_or_nan(row: dict[str, str], key: str) -> float:
    try:
        return float(row.get(key, 'nan'))
    except ValueError:
        return math.nan


def missing_required(row: dict[str, str]) -> list[str]:
    return [col for col in REQUIRED_COLUMNS if col not in row]


def ecef_to_enu(dx_m: float, dy_m: float, dz_m: float, lat_deg: float, lon_deg: float) -> tuple[float, float, float]:
    lat = math.radians(lat_deg)
    lon = math.radians(lon_deg)
    sin_lat = math.sin(lat)
    cos_lat = math.cos(lat)
    sin_lon = math.sin(lon)
    cos_lon = math.cos(lon)

    east = -sin_lon * dx_m + cos_lon * dy_m
    north = -sin_lat * cos_lon * dx_m - sin_lat * sin_lon * dy_m + cos_lat * dz_m
    up = cos_lat * cos_lon * dx_m + cos_lat * sin_lon * dy_m + sin_lat * dz_m
    return east, north, up


def set_equal_axes(ax, xs: list[float], ys: list[float], zs: list[float]) -> None:
    if not xs:
        return
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    zmin, zmax = min(zs), max(zs)
    xmid = 0.5 * (xmin + xmax)
    ymid = 0.5 * (ymin + ymax)
    zmid = 0.5 * (zmin + zmax)
    span = max(xmax - xmin, ymax - ymin, zmax - zmin, 20.0)
    half = 0.55 * span
    ax.set_xlim(xmid - half, xmid + half)
    ax.set_ylim(ymid - half, ymid + half)
    ax.set_zlim(max(0.0, zmid - half), zmid + half)


def main() -> None:
    args = parse_args()
    plt = configure_matplotlib(args.headless)

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    line, = ax.plot([], [], [], color='tab:blue', lw=1.8)
    point, = ax.plot([], [], [], marker='o', color='tab:red', markersize=5)
    info = ax.text2D(0.02, 0.96, 'waiting for CSV...', transform=ax.transAxes)

    ax.set_title(args.title)
    ax.set_xlabel('East from start (m)')
    ax.set_ylabel('North from start (m)')
    ax.set_zlabel('Up from start (m)')
    ax.grid(True, alpha=0.35)

    if not args.headless:
        plt.show(block=False)

    origin = None
    frames = 0
    final_seen_at = None
    interval_s = max(args.interval_ms, 10) / 1000.0

    while args.headless or plt.fignum_exists(fig.number):
        rows = read_complete_rows(args.csv)
        if rows:
            first = rows[0]
            missing = missing_required(first)
            if missing:
                info.set_text('missing columns: ' + ', '.join(missing[:4]))
            else:
                if origin is None:
                    origin = (
                        float_or_nan(first, ECEF_X_COL) * FT_TO_M,
                        float_or_nan(first, ECEF_Y_COL) * FT_TO_M,
                        float_or_nan(first, ECEF_Z_COL) * FT_TO_M,
                        float_or_nan(first, LAT_COL),
                        float_or_nan(first, LON_COL),
                    )

                ox, oy, oz, lat0, lon0 = origin
                xs: list[float] = []
                ys: list[float] = []
                zs: list[float] = []
                for row in rows:
                    x = float_or_nan(row, ECEF_X_COL) * FT_TO_M
                    y = float_or_nan(row, ECEF_Y_COL) * FT_TO_M
                    z = float_or_nan(row, ECEF_Z_COL) * FT_TO_M
                    if math.isnan(x) or math.isnan(y) or math.isnan(z):
                        continue
                    east, north, up = ecef_to_enu(x - ox, y - oy, z - oz, lat0, lon0)
                    xs.append(east)
                    ys.append(north)
                    zs.append(up)

                if xs:
                    line.set_data(xs, ys)
                    line.set_3d_properties(zs)
                    point.set_data([xs[-1]], [ys[-1]])
                    point.set_3d_properties([zs[-1]])
                    set_equal_axes(ax, xs, ys, zs)
                    last = rows[-1]
                    t = float_or_nan(last, TIME_COL)
                    agl = float_or_nan(last, AGL_COL) * FT_TO_M
                    phi = float_or_nan(last, PHI_COL)
                    theta = float_or_nan(last, THETA_COL)
                    psi = float_or_nan(last, PSI_COL)
                    vt = float_or_nan(last, VT_COL) * FPS_TO_MPS
                    info.set_text(
                        f't={t:.2f} s | AGL={agl:.1f} m | VT={vt:.1f} m/s\n'
                        f'phi={phi:.1f} deg | theta={theta:.1f} deg | psi={psi:.1f} deg | samples={len(rows)}'
                    )

        fig.canvas.draw_idle()
        frames += 1
        if args.max_frames is not None and frames >= args.max_frames:
            break

        done = bool(args.done_file and args.done_file.exists())
        if done and final_seen_at is None:
            final_seen_at = time.monotonic()
        if final_seen_at is not None and time.monotonic() - final_seen_at >= args.final_hold_sec:
            break

        if args.headless:
            time.sleep(interval_s)
        else:
            plt.pause(interval_s)

    plt.close(fig)


if __name__ == '__main__':
    main()
