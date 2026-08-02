from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
SI_DIR = ROOT / "logs" / "csv" / "si"
PLOTS_DIR = ROOT / "plots"


def read_rows(path: Path) -> list[dict[str, float]]:
    with path.open(newline="", encoding="utf-8") as src:
        return [
            {key: float(value) for key, value in row.items()}
            for row in csv.DictReader(src)
        ]


def series(rows: list[dict[str, float]], name: str) -> list[float]:
    return [row[name] for row in rows]


def unwrap_degrees(values: list[float]) -> list[float]:
    if not values:
        return []
    unwrapped = [values[0]]
    offset = 0.0
    previous = values[0]
    for value in values[1:]:
        delta = value - previous
        if delta > 180.0:
            offset -= 360.0
        elif delta < -180.0:
            offset += 360.0
        unwrapped.append(value + offset)
        previous = value
    return unwrapped


def set_axes_equal(ax, x: list[float], y: list[float], z: list[float]) -> None:
    x_mid = (max(x) + min(x)) / 2.0
    y_mid = (max(y) + min(y)) / 2.0
    z_mid = (max(z) + min(z)) / 2.0
    max_range = max(max(x) - min(x), max(y) - min(y), max(z) - min(z))
    half_range = max_range / 2.0
    ax.set_xlim(x_mid - half_range, x_mid + half_range)
    ax.set_ylim(y_mid - half_range, y_mid + half_range)
    ax.set_zlim(z_mid - half_range, z_mid + half_range)
    ax.set_box_aspect((1, 1, 1))


def plot_standalone(rows: list[dict[str, float]]) -> None:
    n = series(rows, "local_N_m")
    e = series(rows, "local_E_m")
    altitude = series(rows, "altitude_m")

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(n, e, altitude, linewidth=1.4)
    ax.scatter([n[0]], [e[0]], [altitude[0]], label="start", s=28)
    ax.scatter([n[-1]], [e[-1]], [altitude[-1]], label="end", s=28)
    set_axes_equal(ax, n, e, altitude)
    ax.set_xlabel("N north (m)")
    ax.set_ylabel("E east (m)")
    ax.set_zlabel("Altitude AGL (m)")
    ax.set_title("JSBSim cannonball trajectory in SI units")
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "ball_validated_trajectory_3d_si.png", dpi=160)
    plt.close(fig)

    t = series(rows, "time_s")
    yaw_unwrapped = unwrap_degrees(series(rows, "yaw_deg"))
    outputs = [
        ("local_N_m", "N north (m)"),
        ("local_E_m", "E east (m)"),
        ("altitude_m", "Altitude (m)"),
        ("local_D_m", "D down (m)"),
        ("v_n_mps", "V north (m/s)"),
        ("v_e_mps", "V east (m/s)"),
        ("v_d_mps", "V down (m/s)"),
        ("roll_deg", "roll body (deg)"),
        ("pitch_deg", "pitch body (deg)"),
        ("yaw_unwrapped_deg", "yaw body unwrapped (deg)"),
        ("p_radps", "p (rad/s)"),
        ("q_radps", "q (rad/s)"),
        ("r_radps", "r (rad/s)"),
        ("ap_elevator_cmd_norm", "AP elevator cmd"),
        ("elevator_cmd_norm", "manual elevator cmd"),
        ("pitch_trim_cmd_norm", "pitch trim cmd"),
        ("pitch_trim_sum_norm", "pitch trim sum"),
        ("elevator_control_deg", "elevator control (deg)"),
        ("elevator_deg", "elevator (deg)"),
        ("aileron_left_deg", "left aileron (deg)"),
        ("aileron_right_deg", "right aileron (deg)"),
        ("rudder_deg", "rudder (deg)"),
        ("throttle_cmd_norm", "throttle cmd"),
        ("mixture_cmd_norm", "mixture cmd"),
        ("magneto_cmd", "magneto cmd"),
        ("starter_cmd", "starter cmd"),
        ("engine_rpm", "engine RPM"),
        ("distance_m", "distance (m)"),
        ("v_total_mps", "V total (m/s)"),
        ("propeller_rpm", "propeller RPM"),
        ("prop_advance_ratio", "prop J"),
    ]
    fig, axes = plt.subplots(10, 3, figsize=(16, 24), sharex=True)
    flat_axes = list(axes.ravel())
    for ax, (name, label) in zip(flat_axes, outputs):
        values = yaw_unwrapped if name == "yaw_unwrapped_deg" else series(rows, name)
        ax.plot(t, values, linewidth=1.1)
        ax.set_ylabel(label)
        ax.grid(True, alpha=0.35)
    for ax in flat_axes[len(outputs):]:
        ax.set_visible(False)
    for ax in axes[-1, :]:
        ax.set_xlabel("time (s)")
    fig.suptitle("JSBSim cannonball states vs time (SI)", y=0.995)
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "ball_validated_states_vs_time_si.png", dpi=160)
    plt.close(fig)


def plot_comparison(validated: list[dict[str, float]], builtin: list[dict[str, float]]) -> None:
    time = series(validated, "time_s")
    specs = [
        ("altitude_m", "Altitude (m)"),
        ("local_D_m", "D down (m)"),
        ("v_n_mps", "V north (m/s)"),
        ("v_e_mps", "V east (m/s)"),
        ("v_d_mps", "V down (m/s)"),
        ("v_total_mps", "V total (m/s)"),
        ("distance_m", "Distance (m)"),
        ("propeller_rpm", "Propeller RPM"),
    ]
    fig, axes = plt.subplots(4, 2, figsize=(13, 12), sharex=True)
    for ax, (name, label) in zip(axes.ravel(), specs):
        ax.plot(time, series(validated, name), label="ball_validated", linewidth=1.4)
        ax.plot(time, series(builtin, name), label="ball.xml", linestyle="--", linewidth=1.2)
        ax.set_ylabel(label)
        ax.grid(True, alpha=0.35)
    for ax in axes[-1, :]:
        ax.set_xlabel("Time (s)")
    axes[0, 0].legend()
    fig.suptitle("ball_validated vs ball.xml comparison (SI)", y=0.995)
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "validated_vs_builtin_overlay_si.png", dpi=160)
    plt.close(fig)

    delta_specs = specs[:6]
    fig, axes = plt.subplots(3, 2, figsize=(13, 9), sharex=True)
    for ax, (name, label) in zip(axes.ravel(), delta_specs):
        delta = [left[name] - right[name] for left, right in zip(validated, builtin)]
        ax.plot(time, delta, linewidth=1.3)
        ax.set_ylabel(f"Delta {label}")
        ax.grid(True, alpha=0.35)
    for ax in axes[-1, :]:
        ax.set_xlabel("Time (s)")
    fig.suptitle("ball_validated minus ball.xml trajectory deltas (SI)", y=0.995)
    fig.tight_layout()
    fig.savefig(PLOTS_DIR / "validated_minus_builtin_deltas_si.png", dpi=160)
    plt.close(fig)


def main() -> None:
    PLOTS_DIR.mkdir(exist_ok=True)
    validated = read_rows(SI_DIR / "ball_validated_si.csv")
    builtin = read_rows(SI_DIR / "ball_builtin_si.csv")
    plot_standalone(validated)
    plot_comparison(validated, builtin)
    print(f"Wrote SI plots to {PLOTS_DIR}")


if __name__ == "__main__":
    main()
