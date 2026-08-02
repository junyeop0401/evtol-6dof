from __future__ import annotations

import csv
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "logs" / "csv" / "raw"
SI_DIR = ROOT / "logs" / "csv" / "si"

FT_TO_M = 0.3048
FPS_TO_MPS = 0.3048
SLUG_TO_KG = 14.593902937206363
SLUG_FT2_TO_KG_M2 = SLUG_TO_KG * FT_TO_M * FT_TO_M
FT_S2_TO_M_S2 = 0.3048
RAD_TO_DEG = 180.0 / math.pi


RAW_TO_SI_FIELDS = [
    ("Time", "time_s", 1.0),
    ("/fdm/jsbsim/position/lat-geod-deg", "lat_deg", 1.0),
    ("/fdm/jsbsim/position/long-gc-deg", "lon_deg", 1.0),
    ("/fdm/jsbsim/position/h-sl-meters", "altitude_m", 1.0),
    ("/fdm/jsbsim/position/ecef-x-ft", "ecef_x_m", FT_TO_M),
    ("/fdm/jsbsim/position/ecef-y-ft", "ecef_y_m", FT_TO_M),
    ("/fdm/jsbsim/position/ecef-z-ft", "ecef_z_m", FT_TO_M),
    ("/fdm/jsbsim/velocities/vt-fps", "v_total_raw_mps", FPS_TO_MPS),
    ("/fdm/jsbsim/velocities/v-north-fps", "v_n_mps", FPS_TO_MPS),
    ("/fdm/jsbsim/velocities/v-east-fps", "v_e_mps", FPS_TO_MPS),
    ("/fdm/jsbsim/velocities/v-down-fps", "v_d_mps", FPS_TO_MPS),
    ("/fdm/jsbsim/velocities/u-fps", "u_body_mps", FPS_TO_MPS),
    ("/fdm/jsbsim/velocities/v-fps", "v_body_mps", FPS_TO_MPS),
    ("/fdm/jsbsim/velocities/w-fps", "w_body_mps", FPS_TO_MPS),
    ("/fdm/jsbsim/attitude/phi-deg", "roll_deg", 1.0),
    ("/fdm/jsbsim/attitude/theta-deg", "pitch_deg", 1.0),
    ("/fdm/jsbsim/attitude/psi-deg", "yaw_deg", 1.0),
    ("/fdm/jsbsim/velocities/p-rad_sec", "p_radps", 1.0),
    ("/fdm/jsbsim/velocities/q-rad_sec", "q_radps", 1.0),
    ("/fdm/jsbsim/velocities/r-rad_sec", "r_radps", 1.0),
    ("/fdm/jsbsim/ap/elevator_cmd", "ap_elevator_cmd_norm", 1.0),
    ("/fdm/jsbsim/fcs/elevator-cmd-norm", "elevator_cmd_norm", 1.0),
    ("/fdm/jsbsim/fcs/pitch-trim-cmd-norm", "pitch_trim_cmd_norm", 1.0),
    ("/fdm/jsbsim/fcs/pitch-trim-sum", "pitch_trim_sum_norm", 1.0),
    ("/fdm/jsbsim/fcs/elevator-control", "elevator_control_deg", RAD_TO_DEG),
    ("/fdm/jsbsim/fcs/elevator-pos-rad", "elevator_deg", RAD_TO_DEG),
    ("/fdm/jsbsim/fcs/left-aileron-pos-rad", "aileron_left_deg", RAD_TO_DEG),
    ("/fdm/jsbsim/fcs/right-aileron-pos-rad", "aileron_right_deg", RAD_TO_DEG),
    ("/fdm/jsbsim/fcs/rudder-pos-rad", "rudder_deg", RAD_TO_DEG),
    ("/fdm/jsbsim/fcs/throttle-cmd-norm", "throttle_cmd_norm", 1.0),
    ("/fdm/jsbsim/fcs/throttle-pos-norm", "throttle_pos_norm", 1.0),
    ("/fdm/jsbsim/fcs/mixture-cmd-norm", "mixture_cmd_norm", 1.0),
    ("/fdm/jsbsim/fcs/mixture-pos-norm", "mixture_pos_norm", 1.0),
    ("/fdm/jsbsim/propulsion/magneto_cmd", "magneto_cmd", 1.0),
    ("/fdm/jsbsim/propulsion/starter_cmd", "starter_cmd", 1.0),
    ("/fdm/jsbsim/propulsion/engine/power-hp", "engine_power_hp", 1.0),
    ("/fdm/jsbsim/propulsion/engine/thrust-lbs", "thrust_lbs", 1.0),
    ("/fdm/jsbsim/propulsion/engine/engine-rpm", "engine_rpm", 1.0),
    ("/fdm/jsbsim/propulsion/engine/propeller-rpm", "propeller_rpm", 1.0),
    ("/fdm/jsbsim/propulsion/engine/propeller-power-ftlbps", "propeller_power_ftlbps", 1.0),
    ("/fdm/jsbsim/propulsion/engine/advance-ratio", "prop_advance_ratio", 1.0),
    ("/fdm/jsbsim/accelerations/gravity-ft_sec2", "gravity_m_s2", FT_S2_TO_M_S2),
    ("/fdm/jsbsim/inertia/mass-slugs", "mass_kg", SLUG_TO_KG),
    ("/fdm/jsbsim/inertia/ixx-slugs_ft2", "ixx_kg_m2", SLUG_FT2_TO_KG_M2),
    ("/fdm/jsbsim/inertia/iyy-slugs_ft2", "iyy_kg_m2", SLUG_FT2_TO_KG_M2),
    ("/fdm/jsbsim/inertia/izz-slugs_ft2", "izz_kg_m2", SLUG_FT2_TO_KG_M2),
]

PLOT_CSV_FIELDS = [
    "time_s",
    "lat_deg",
    "lon_deg",
    "local_N_m",
    "local_E_m",
    "altitude_m",
    "local_D_m",
    "v_n_mps",
    "v_e_mps",
    "v_d_mps",
    "roll_deg",
    "pitch_deg",
    "yaw_deg",
    "p_radps",
    "q_radps",
    "r_radps",
    "ap_elevator_cmd_norm",
    "elevator_cmd_norm",
    "pitch_trim_cmd_norm",
    "pitch_trim_sum_norm",
    "elevator_control_deg",
    "elevator_deg",
    "aileron_left_deg",
    "aileron_right_deg",
    "rudder_deg",
    "throttle_cmd_norm",
    "throttle_pos_norm",
    "mixture_cmd_norm",
    "mixture_pos_norm",
    "magneto_cmd",
    "starter_cmd",
    "engine_power_hp",
    "thrust_lbs",
    "engine_rpm",
    "distance_m",
    "v_total_mps",
    "propeller_rpm",
    "propeller_power_ftlbps",
    "prop_advance_ratio",
    "mass_kg",
    "ixx_kg_m2",
    "iyy_kg_m2",
    "izz_kg_m2",
]

OPTIONAL_RAW_DEFAULTS = {
    "/fdm/jsbsim/velocities/p-rad_sec": 0.0,
    "/fdm/jsbsim/velocities/q-rad_sec": 0.0,
    "/fdm/jsbsim/velocities/r-rad_sec": 0.0,
    "/fdm/jsbsim/ap/elevator_cmd": 0.0,
    "/fdm/jsbsim/fcs/elevator-cmd-norm": 0.0,
    "/fdm/jsbsim/fcs/pitch-trim-cmd-norm": 0.0,
    "/fdm/jsbsim/fcs/pitch-trim-sum": 0.0,
    "/fdm/jsbsim/fcs/elevator-control": 0.0,
    "/fdm/jsbsim/fcs/elevator-pos-rad": 0.0,
    "/fdm/jsbsim/fcs/left-aileron-pos-rad": 0.0,
    "/fdm/jsbsim/fcs/right-aileron-pos-rad": 0.0,
    "/fdm/jsbsim/fcs/rudder-pos-rad": 0.0,
    "/fdm/jsbsim/fcs/throttle-cmd-norm": 0.0,
    "/fdm/jsbsim/fcs/throttle-pos-norm": 0.0,
    "/fdm/jsbsim/fcs/mixture-cmd-norm": 0.0,
    "/fdm/jsbsim/fcs/mixture-pos-norm": 0.0,
    "/fdm/jsbsim/propulsion/magneto_cmd": 0.0,
    "/fdm/jsbsim/propulsion/starter_cmd": 0.0,
    "/fdm/jsbsim/propulsion/engine/power-hp": 0.0,
    "/fdm/jsbsim/propulsion/engine/thrust-lbs": 0.0,
    "/fdm/jsbsim/propulsion/engine/engine-rpm": 0.0,
    "/fdm/jsbsim/propulsion/engine/propeller-rpm": 0.0,
    "/fdm/jsbsim/propulsion/engine/propeller-power-ftlbps": 0.0,
    "/fdm/jsbsim/propulsion/engine/advance-ratio": 0.0,
}


def ecef_delta_to_enu(row: dict[str, float], origin: dict[str, float]) -> tuple[float, float, float]:
    dx = row["ecef_x_m"] - origin["ecef_x_m"]
    dy = row["ecef_y_m"] - origin["ecef_y_m"]
    dz = row["ecef_z_m"] - origin["ecef_z_m"]
    lat = math.radians(origin["lat_deg"])
    lon = math.radians(origin["lon_deg"])

    sin_lat = math.sin(lat)
    cos_lat = math.cos(lat)
    sin_lon = math.sin(lon)
    cos_lon = math.cos(lon)

    east = -sin_lon * dx + cos_lon * dy
    north = -sin_lat * cos_lon * dx - sin_lat * sin_lon * dy + cos_lat * dz
    up = cos_lat * cos_lon * dx + cos_lat * sin_lon * dy + sin_lat * dz
    return east, north, up


def add_plot_csv_fields(rows: list[dict[str, float]]) -> None:
    origin = rows[0]
    for row in rows:
        east, north, up = ecef_delta_to_enu(row, origin)
        row["local_E_m"] = east
        row["local_N_m"] = north
        row["local_D_m"] = -up
        row["distance_m"] = math.sqrt(north**2 + east**2 + row["local_D_m"] ** 2)
        row["v_total_mps"] = math.sqrt(
            row["v_n_mps"] ** 2 + row["v_e_mps"] ** 2 + row["v_d_mps"] ** 2
        )


def convert_file(input_path: Path, output_path: Path) -> None:
    with input_path.open(newline="", encoding="utf-8") as src:
        raw_rows = list(csv.DictReader(src))

    if not raw_rows:
        raise RuntimeError(f"No rows found in {input_path}")

    missing = [
        source
        for source, _, _ in RAW_TO_SI_FIELDS
        if source not in raw_rows[0] and source not in OPTIONAL_RAW_DEFAULTS
    ]
    if missing:
        raise RuntimeError(f"Raw CSV is missing required properties: {missing}")

    rows = [
        {
            target: float(row[source]) * scale if source in row else OPTIONAL_RAW_DEFAULTS[source]
            for source, target, scale in RAW_TO_SI_FIELDS
        }
        for row in raw_rows
    ]
    add_plot_csv_fields(rows)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(dst, fieldnames=PLOT_CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in PLOT_CSV_FIELDS})


def main() -> None:
    convert_file(RAW_DIR / "ball_validated_raw.csv", SI_DIR / "ball_validated_si.csv")
    convert_file(RAW_DIR / "ball_builtin_raw.csv", SI_DIR / "ball_builtin_si.csv")
    print(f"Wrote SI CSV logs to {SI_DIR}")


if __name__ == "__main__":
    main()
