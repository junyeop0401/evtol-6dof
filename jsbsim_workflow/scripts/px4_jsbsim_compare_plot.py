#!/usr/bin/env python3
"""Build PX4 ULog plus JSBSim property combined CSV and comparison plots."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from typing import Iterable, List

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from px4_ulog_to_combined_csv import choose_ulog, convert_ulog, parse_messages


DEFAULT_MODEL = "standard_vtol_demo_hover_px4"
DEFAULT_PX4_LOG_ROOT = Path("/home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log")
DEFAULT_JSBSIM_CSV = Path("/home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/jsbsim_bridge/standard_vtol_demo_hover_px4/latest_jsbsim_properties.csv")
DEFAULT_OUTPUT_ROOT = Path(__file__).resolve().parents[1] / "logs" / "csv"
DEFAULT_MESSAGES = (
    "actuator_outputs",
    "actuator_motors",
    "actuator_servos",
    "actuator_controls_0",
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


def make_unique(columns: Iterable[str]) -> List[str]:
    seen = {}
    result = []

    for column in columns:
        base = str(column).strip()
        count = seen.get(base, 0)
        seen[base] = count + 1
        result.append(base if count == 0 else f"{base}.{count}")

    return result


def read_jsbsim_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = make_unique(df.columns)

    if "Time" not in df.columns:
        raise RuntimeError(f"JSBSim CSV has no Time column: {path}")

    df = df.rename(columns={"Time": "time_s"})
    df["time_s"] = pd.to_numeric(df["time_s"], errors="coerce")
    df = df.dropna(subset=["time_s"]).sort_values("time_s")
    df["time_s"] = df["time_s"] - df["time_s"].iloc[0]

    rename = {column: f"jsbsim.{column}" for column in df.columns if column != "time_s"}
    return df.rename(columns=rename)


def read_px4_combined(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = make_unique(df.columns)
    df["time_s"] = pd.to_numeric(df["time_s"], errors="coerce")
    return df.dropna(subset=["time_s"]).sort_values("time_s")


def merge_logs(px4_csv: Path, jsbsim_csv: Path, output_root: Path, model: str, run_name: str) -> Path:
    px4 = read_px4_combined(px4_csv)
    jsb = read_jsbsim_csv(jsbsim_csv)
    merged = pd.merge_asof(px4, jsb, on="time_s", direction="nearest", tolerance=0.05)
    out_dir = output_root / "combined_px4_jsbsim" / model / run_name
    out_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%m%d%H%M%S")
    out_path = out_dir / f"{run_name}_px4_jsbsim_combined_{stamp}.csv"
    merged.to_csv(out_path, index=False)
    return out_path


def find_columns(df: pd.DataFrame, needle: str) -> List[str]:
    return [column for column in df.columns if needle.lower() in column.lower()]


def plot_if_columns(df: pd.DataFrame, columns: List[str], title: str, ylabel: str, output: Path) -> bool:
    columns = [column for column in columns if column in df.columns]
    if not columns:
        return False

    plt.figure(figsize=(13, 7))
    for column in columns:
        plt.plot(df["time_s"], pd.to_numeric(df[column], errors="coerce"), label=column)
    plt.title(title)
    plt.xlabel("time_s")
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    plt.legend(loc="best", fontsize=8)
    plt.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output, dpi=140)
    plt.close()
    return True


def build_plots(combined_csv: Path) -> List[Path]:
    df = pd.read_csv(combined_csv)
    plot_dir = combined_csv.parent / "plots"
    outputs = []

    esc_cmd = find_columns(df, "jsbsim./fdm/jsbsim/fcs/esc-cmd-norm")
    esc_out = find_columns(df, "jsbsim./fdm/jsbsim/fcs/esc-out")
    px4_motor = find_columns(df, "actuator_motors.control")
    if plot_if_columns(df, px4_motor[:5] + esc_cmd[:5] + esc_out[:5], "PX4 motor commands vs JSBSim ESC command/output", "normalized command", plot_dir / "actuator_px4_vs_jsbsim.png"):
        outputs.append(plot_dir / "actuator_px4_vs_jsbsim.png")

    altitude_cols = []
    if "vehicle_local_position.z" in df.columns:
        df["px4.local_altitude_up_m"] = -pd.to_numeric(df["vehicle_local_position.z"], errors="coerce")
        altitude_cols.append("px4.local_altitude_up_m")
    for candidate in ("jsbsim.Altitude AGL (ft)", "jsbsim.Distance AGL (ft)", "jsbsim.Altitude ASL (ft)"):
        if candidate in df.columns:
            altitude_cols.append(candidate)
    if plot_if_columns(df, altitude_cols, "PX4 local altitude vs JSBSim altitude", "m or ft", plot_dir / "altitude_px4_vs_jsbsim.png"):
        outputs.append(plot_dir / "altitude_px4_vs_jsbsim.png")

    force_cols = find_columns(df, "Total Gear Force") + find_columns(df, "F_{Aero") + find_columns(df, "F_{Weight")
    if plot_if_columns(df, force_cols[:12], "JSBSim forces", "lbs", plot_dir / "jsbsim_forces.png"):
        outputs.append(plot_dir / "jsbsim_forces.png")

    aero_cols = [column for column in ("jsbsim.Alpha (deg)", "jsbsim.Beta (deg)", "jsbsim.q bar (psf)", "jsbsim./fdm/jsbsim/aero/alpha-rad", "jsbsim./fdm/jsbsim/aero/beta-rad") if column in df.columns]
    if plot_if_columns(df, aero_cols, "JSBSim aerodynamic state", "mixed", plot_dir / "jsbsim_aero.png"):
        outputs.append(plot_dir / "jsbsim_aero.png")

    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ulg", type=Path, nargs=chr(63), help="PX4 ULog. If omitted, choose from recent PX4 logs.")
    parser.add_argument("--jsbsim-csv", type=Path, default=DEFAULT_JSBSIM_CSV)
    parser.add_argument("--px4-log-root", type=Path, default=DEFAULT_PX4_LOG_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--messages", default=",".join(DEFAULT_MESSAGES))
    parser.add_argument("--list-limit", type=int, default=30)
    parser.add_argument("--no-plots", action="store_true")
    args = parser.parse_args()

    ulg = args.ulg.resolve() if args.ulg else choose_ulog(args.px4_log_root.resolve(), args.list_limit)
    jsbsim_csv = args.jsbsim_csv.resolve()
    if not jsbsim_csv.exists():
        raise RuntimeError(f"JSBSim CSV not found: {jsbsim_csv}")

    px4_csv = convert_ulog(
        ulg_path=ulg,
        output_root=args.output_root.resolve(),
        model=args.model,
        messages=parse_messages(args.messages),
        forward_fill=True,
    )
    combined = merge_logs(px4_csv, jsbsim_csv, args.output_root.resolve(), args.model, ulg.stem)

    print(f"PX4 combined CSV: {px4_csv}")
    print(f"JSBSim CSV: {jsbsim_csv}")
    print(f"PX4 plus JSBSim combined CSV: {combined}")

    if not args.no_plots:
        plots = build_plots(combined)
        for plot in plots:
            print(f"Plot: {plot}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
