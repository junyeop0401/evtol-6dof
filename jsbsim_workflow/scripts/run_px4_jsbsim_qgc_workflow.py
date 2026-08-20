#!/usr/bin/env python3
"""Run PX4 JSBSim SITL for QGC, then convert the latest ULog to combined CSV."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterable, Optional

from px4_ulog_to_combined_csv import convert_ulog, parse_messages
from px4_jsbsim_compare_plot import DEFAULT_JSBSIM_CSV, DEFAULT_MESSAGES, build_plots, merge_logs


DEFAULT_WORKFLOW_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PX4_ROOT = Path("/home/junyeopkwon/px4_versions/PX4-v1.16.0")
DEFAULT_MODEL = "standard_vtol_demo_hover_px4"
DEFAULT_WORLD = "RKSS"
DEFAULT_QGC = Path("/home/junyeopkwon/Downloads/QGroundControl-x86_64.AppImage")


def iter_ulg_files(px4_root: Path) -> Iterable[Path]:
    log_root = px4_root / "build" / "px4_sitl_default" / "rootfs" / "log"

    if not log_root.exists():
        return []

    return log_root.glob("*/*.ulg")


def latest_ulg_after(px4_root: Path, started_at: float) -> Optional[Path]:
    candidates = [
        path
        for path in iter_ulg_files(px4_root)
        if path.is_file() and path.stat().st_mtime >= started_at - 2.0
    ]

    if not candidates:
        return None

    return max(candidates, key=lambda path: path.stat().st_mtime)


def launch_qgc(qgc_path: Path) -> Optional[subprocess.Popen]:
    if not qgc_path.exists():
        print(f"[WARN] QGC executable not found: {qgc_path}", flush=True)
        return None

    print(f"[INFO] Launching QGC: {qgc_path}", flush=True)
    return subprocess.Popen([str(qgc_path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def run_px4(args: argparse.Namespace) -> int:
    env = os.environ.copy()
    env["HEADLESS"] = "1"

    if args.quiet_jsbsim:
        env["JSBSIM_QUIET"] = "1"

    target = "jsbsim_" + args.model if args.world == "LSZH" else "jsbsim_" + args.model + "__" + args.world
    command = ["make", "px4_sitl", target]

    print("[INFO] PX4 command:", " ".join(command), flush=True)
    print(f"[INFO] PX4 root: {args.px4_root}", flush=True)
    print("[INFO] QGC should auto-connect on UDP 14550.", flush=True)
    print("[INFO] Stop PX4 with `shutdown` at the pxh> prompt after the mission/log check.", flush=True)

    try:
        result = subprocess.run(command, cwd=args.px4_root, env=env)
        return result.returncode
    except KeyboardInterrupt:
        print("\n[WARN] Interrupted by user. Trying to convert the latest ULog if one exists.", flush=True)
        return 130


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--px4-root", type=Path, default=DEFAULT_PX4_ROOT)
    parser.add_argument("--workflow-root", type=Path, default=DEFAULT_WORKFLOW_ROOT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--world", default=DEFAULT_WORLD, help="JSBSim scene world. Default RKSS uses RKSS target variant.")
    parser.add_argument("--launch-qgc", action="store_true", help="Launch WSL QGroundControl AppImage first")
    parser.add_argument("--qgc", type=Path, default=DEFAULT_QGC)
    parser.add_argument("--no-convert", action="store_true", help="Do not convert latest ULog after PX4 exits")
    parser.add_argument("--no-jsbsim-combine", action="store_true", help="Skip PX4 plus JSBSim combined CSV and plots")
    parser.add_argument("--jsbsim-csv", type=Path, default=DEFAULT_JSBSIM_CSV)
    parser.add_argument("--messages", default=",".join(DEFAULT_MESSAGES))
    parser.add_argument("--quiet-jsbsim", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    args.px4_root = args.px4_root.resolve()
    args.workflow_root = args.workflow_root.resolve()

    if not args.px4_root.exists():
        print(f"[ERROR] PX4 root not found: {args.px4_root}", file=sys.stderr)
        return 2

    if args.launch_qgc:
        launch_qgc(args.qgc.expanduser())
        time.sleep(2.0)

    started_at = time.time()
    return_code = run_px4(args)

    if args.no_convert:
        return return_code

    ulg = latest_ulg_after(args.px4_root, started_at)

    if ulg is None:
        print("[WARN] No new ULog found. Nothing converted.", flush=True)
        return return_code

    try:
        output = convert_ulog(
            ulg_path=ulg,
            output_root=args.workflow_root / "logs" / "csv",
            model=args.model,
            messages=parse_messages(args.messages),
            forward_fill=True,
        )
    except Exception as exc:
        print(f"[ERROR] ULog conversion failed: {exc}", file=sys.stderr)
        return return_code if return_code else 1

    print(f"[INFO] Latest ULog: {ulg}", flush=True)
    print(f"[INFO] PX4 combined CSV: {output}", flush=True)

    jsbsim_csv = args.jsbsim_csv.resolve()
    if not args.no_jsbsim_combine:
        if jsbsim_csv.exists():
            source_dir = args.workflow_root / "logs" / "csv" / "combined_px4_jsbsim" / args.model / ulg.stem
            source_dir.mkdir(parents=True, exist_ok=True)
            preserved_jsbsim = source_dir / f"{ulg.stem}_jsbsim_properties.csv"
            shutil.copy2(jsbsim_csv, preserved_jsbsim)
            combined = merge_logs(output, preserved_jsbsim, args.workflow_root / "logs" / "csv", args.model, ulg.stem)
            print(f"[INFO] JSBSim CSV: {preserved_jsbsim}", flush=True)
            print(f"[INFO] PX4 plus JSBSim combined CSV: {combined}", flush=True)
            for plot in build_plots(combined):
                print(f"[INFO] Plot: {plot}", flush=True)
        else:
            print(f"[WARN] JSBSim CSV not found: {jsbsim_csv}", flush=True)

    return return_code


if __name__ == "__main__":
    raise SystemExit(main())
