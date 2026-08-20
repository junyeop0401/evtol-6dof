#!/usr/bin/env python3
"""Convert a PX4 ULog into one forward-filled combined CSV."""

from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from pyulog import ULog


DEFAULT_PX4_LOG_ROOT = Path('/home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log')


DEFAULT_MESSAGES = (
    "actuator_outputs",
    "actuator_armed",
    "vehicle_status",
    "vehicle_local_position",
    "vehicle_global_position",
    "vehicle_attitude",
    "vehicle_angular_velocity",
    "vehicle_acceleration",
    "vehicle_gps_position",
    "estimator_status",
    "sensor_combined",
)


def parse_messages(value: str) -> List[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def iter_ulog_files(log_root: Path) -> List[Path]:
    if not log_root.exists():
        return []

    return sorted(
        (path for path in log_root.glob('*/*.ulg') if path.is_file()),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )


def format_size(size: int) -> str:
    value = float(size)

    for unit in ('B', 'KB', 'MB', 'GB'):
        if value < 1024 or unit == 'GB':
            return f'{int(value)} {unit}' if unit == 'B' else f'{value:.1f} {unit}'
        value /= 1024

    return f'{value:.1f} GB'


def choose_ulog(log_root: Path, limit: int) -> Path:
    candidates = iter_ulog_files(log_root)[:limit]

    if not candidates:
        raise RuntimeError(f'No .ulg files found under {log_root}')

    print('Select PX4 ULog:')

    for index, path in enumerate(candidates, start=1):
        stat = path.stat()
        modified = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        print(f'  {index}. {path}  ({modified}, {format_size(stat.st_size)})')

    while True:
        raw = input(f'ulog number [1-{len(candidates)}] (default 1): ').strip()

        if not raw:
            return candidates[0]

        try:
            choice = int(raw)
        except ValueError:
            print('Enter a number from the list.')
            continue

        if 1 <= choice <= len(candidates):
            return candidates[choice - 1]

        print(f'Enter a number between 1 and {len(candidates)}.')


def scalar(value):
    if hasattr(value, "item"):
        return value.item()
    return value


def iter_dataset_rows(dataset) -> Iterable[Tuple[int, Dict[str, object]]]:
    data = dataset.data
    timestamps = data.get("timestamp")

    if timestamps is None:
        return

    keys = [key for key in data.keys() if key != "timestamp"]
    prefix = dataset.name if dataset.multi_id == 0 else f"{dataset.name}_{dataset.multi_id}"

    for index, timestamp in enumerate(timestamps):
        row: Dict[str, object] = {}

        for key in keys:
            values = data[key]

            if index < len(values):
                row[f"{prefix}.{key}"] = scalar(values[index])

        yield int(timestamp), row


def convert_ulog(
    ulg_path: Path,
    output_root: Path,
    model: str,
    messages: List[str],
    forward_fill: bool,
) -> Path:
    ulog = ULog(str(ulg_path), messages)
    events: Dict[int, Dict[str, object]] = {}
    columns = set()

    for dataset in ulog.data_list:
        for timestamp, row in iter_dataset_rows(dataset):
            events.setdefault(timestamp, {}).update(row)
            columns.update(row.keys())

    if not events:
        raise RuntimeError(f"No selected ULog messages found in {ulg_path}")

    timestamp_tag = datetime.now().strftime("%m%d%H%M%S")
    run_name = ulg_path.stem
    out_dir = output_root / "combined" / model / run_name
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{run_name}_px4_combined_{timestamp_tag}.csv"

    fieldnames = ["timestamp", "time_s", *sorted(columns)]
    state: Dict[str, object] = {}
    first_timestamp = min(events)

    with out_path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()

        for timestamp in sorted(events):
            current = events[timestamp]

            if forward_fill:
                state.update(current)
                payload = dict(state)
            else:
                payload = current

            writer.writerow(
                {
                    "timestamp": timestamp,
                    "time_s": (timestamp - first_timestamp) / 1_000_000.0,
                    **payload,
                }
            )

    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ulg', type=Path, nargs=chr(63), help='PX4 .ulg file. If omitted, choose from recent PX4 logs.')
    parser.add_argument("--model", default="standard_vtol_demo_hover_px4")
    parser.add_argument(
        "--messages",
        default=",".join(DEFAULT_MESSAGES),
        help="Comma-separated ULog topics to include",
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "logs" / "csv",
    )
    parser.add_argument("--no-forward-fill", action="store_true")
    parser.add_argument(
        '--log-root',
        type=Path,
        default=DEFAULT_PX4_LOG_ROOT,
        help='PX4 SITL log root used by interactive selection',
    )
    parser.add_argument('--list-limit', type=int, default=30, help='Maximum ULogs to show when selecting interactively')
    args = parser.parse_args()

    ulg_path = args.ulg.resolve() if args.ulg else choose_ulog(args.log_root.resolve(), args.list_limit)

    output = convert_ulog(
        ulg_path,
        args.output_root.resolve(),
        args.model,
        parse_messages(args.messages),
        not args.no_forward_fill,
    )
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
