from __future__ import annotations

import argparse
import csv
import math
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from copy import deepcopy
from datetime import datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg", force=True)
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter


ROOT = Path("/home/junyeopkwon/jsbsim_workflow")
SCRIPTS_DIR = ROOT / "scripts"
EARTH_MODEL_DIR = ROOT / "earth_models"
RAW_CSV_DIR = ROOT / "logs" / "csv" / "raw"
SI_CSV_DIR = ROOT / "logs" / "csv" / "si"
SIXDOF_CSV_DIR = ROOT / "logs" / "csv" / "sixdof_raw"
SIXDOF_SI_CSV_DIR = ROOT / "logs" / "csv" / "sixdof_si"
CONSOLE_DIR = ROOT / "logs" / "console"
PLOTS_DIR = ROOT / "plots"
PLOTING_DIR = ROOT / "ploting"
GENERATED_DIR = ROOT / "logs" / "generated_runscripts"
JSBSIM_DIR = Path("/home/junyeopkwon/jsbsim")
AIRCRAFT_DIR = JSBSIM_DIR / "aircraft"
WORKFLOW_EXCEL = ROOT / "workflow_all_cases_initial_settings.xlsx"
WORKFLOW_EXCEL_SCRIPT = SCRIPTS_DIR / "update_workflow_excel.py"
DEFAULT_FLIGHTGEAR_LOGDIRECTIVE = SCRIPTS_DIR / "c172x" / "output" / "fg_visual_5500.xml"

FT_TO_M = 0.3048
FPS_TO_MPS = 0.3048
SLUG_TO_KG = 14.593902937206363
SLUG_FT2_TO_KG_M2 = SLUG_TO_KG * FT_TO_M * FT_TO_M
FT_S2_TO_M_S2 = 0.3048
RAD_TO_DEG = 180.0 / math.pi

OUTPUT_PROPERTIES = [
    "position/lat-gc-deg",
    "position/lat-geod-deg",
    "position/long-gc-deg",
    "position/h-sl-meters",
    "position/geod-alt-ft",
    "position/h-agl-ft",
    "position/ecef-x-ft",
    "position/ecef-y-ft",
    "position/ecef-z-ft",
    "velocities/vt-fps",
    "velocities/vc-kts",
    "velocities/h-dot-fps",
    "velocities/v-north-fps",
    "velocities/v-east-fps",
    "velocities/v-down-fps",
    "velocities/u-fps",
    "velocities/v-fps",
    "velocities/w-fps",
    "velocities/p-rad_sec",
    "velocities/q-rad_sec",
    "velocities/r-rad_sec",
    "attitude/phi-deg",
    "attitude/theta-deg",
    "attitude/psi-deg",
    "ap/elevator_cmd",
    "fcs/elevator-cmd-norm",
    "fcs/pitch-trim-cmd-norm",
    "fcs/pitch-trim-sum",
    "fcs/elevator-control",
    "fcs/elevator-pos-rad",
    "fcs/left-aileron-pos-rad",
    "fcs/right-aileron-pos-rad",
    "fcs/rudder-pos-rad",
    "fcs/rudder-cmd-norm",
    "fcs/throttle-cmd-norm",
    "fcs/throttle-pos-norm",
    "fcs/mixture-cmd-norm",
    "fcs/mixture-pos-norm",
    "propulsion/magneto_cmd",
    "propulsion/starter_cmd",
    "propulsion/engine/power-hp",
    "propulsion/engine/thrust-lbs",
    "propulsion/engine/engine-rpm",
    "propulsion/engine/propeller-rpm",
    "propulsion/engine/propeller-power-ftlbps",
    "propulsion/engine/advance-ratio",
    "accelerations/gravity-ft_sec2",
    "inertia/mass-slugs",
    "inertia/cg-x-in",
    "inertia/cg-y-in",
    "inertia/cg-z-in",
    "inertia/ixx-slugs_ft2",
    "inertia/iyy-slugs_ft2",
    "inertia/izz-slugs_ft2",
    "aero/alpha-deg",
]

LANDING_OUTPUT_PROPERTIES = [
    "simulation/mission-state",
    "simulation/stall-detected",
    "simulation/cruise-active",
    "simulation/cruise-timer-sec",
    "simulation/landing-authorized",
    "simulation/target-altitude-ft",
    "ap/attitude_hold",
    "ap/heading_hold",
    "ap/altitude_hold",
    "ap/heading_setpoint",
    "ap/altitude_setpoint",
    "ap/aileron_cmd",
    "fcs/aileron-cmd-norm",
    "fcs/flap-cmd-norm",
    "fcs/flap-pos-deg",
    "fcs/left-brake-cmd-norm",
    "fcs/right-brake-cmd-norm",
    "fcs/center-brake-cmd-norm",
    "gear/unit[0]/WOW",
    "gear/unit[1]/WOW",
    "gear/unit[2]/WOW",
    "gear/unit[0]/compression-ft",
    "gear/unit[1]/compression-ft",
    "gear/unit[2]/compression-ft",
    "mission/runway-along-ft",
    "mission/runway-cross-ft",
    "simulation/circular-loiter-active",
    "mission/circular-bank-target-rad",
    "mission/circular-bank-error-rad",
    "mission/circular-bank-cmd-norm",
    "ap/roll-cmd-norm-output",
]

F450_OUTPUT_PROPERTIES = [
    'simulation/mission-state',
    'ap/mode',
    'ap/altitude-reference',
    'ap/heading-setpoint-rad',
    'ap/north-setpoint-m',
    'ap/east-setpoint-m',
    'ap/altitude-setpoint-ft',
    'ap/hover-throttle-base',
    'ap/altitude-error-ft',
    'ap/climb-rate-setpoint-fps',
    'ap/climb-rate-error-fps',
    'ap/altitude-collective-unclipped',
    'ap/altitude-collective-clipped',
    'position/distance-from-start-lat-mt',
    'position/distance-from-start-lon-mt',
    'ap/north-position-error-m',
    'ap/east-position-error-m',
    'ap/north-velocity-setpoint-mps',
    'ap/east-velocity-setpoint-mps',
    'ap/north-velocity-error-fps',
    'ap/east-velocity-error-fps',
    'ap/hover-roll-reference-rad',
    'ap/hover-pitch-reference-rad',
    'ap/selected-roll-reference-rad',
    'ap/selected-pitch-reference-rad',
    'ap/roll-error-rad',
    'ap/pitch-error-rad',
    'ap/heading-error-rad',
    'ap/roll-cmd-norm',
    'ap/pitch-cmd-norm',
    'ap/yaw-cmd-norm',
    'ap/collective-cmd-norm',
    'fcs/ScasEngage',
    'fcs/aileron-cmd-norm',
    'fcs/elevator-cmd-norm',
    'fcs/rudder-cmd-norm',
    'fcs/refRoll_rps',
    'fcs/refPitch_rps',
    'fcs/refYaw_rps',
    'velocities/pi-rad_sec',
    'velocities/qi-rad_sec',
    'velocities/ri-rad_sec',
    'fcs/errRoll_rps',
    'fcs/errPitch_rps',
    'fcs/errYaw_rps',
    'fcs/cmdRoll_rps',
    'fcs/cmdPitch_rps',
    'fcs/cmdYaw_rps',
    'fcs/cmdFR_nd',
    'fcs/cmdAL_nd',
    'fcs/cmdFL_nd',
    'fcs/cmdAR_nd',
    'fcs/cmdEscFR_nd',
    'fcs/cmdEscAL_nd',
    'fcs/cmdEscFL_nd',
    'fcs/cmdEscAR_nd',
    'fcs/throttle-pos-norm',
    'fcs/throttle-pos-norm[1]',
    'fcs/throttle-pos-norm[2]',
    'fcs/throttle-pos-norm[3]',
    'propulsion/engine/propeller-rpm',
    'propulsion/engine[1]/propeller-rpm',
    'propulsion/engine[2]/propeller-rpm',
    'propulsion/engine[3]/propeller-rpm',
    'propulsion/engine/thrust-lbs',
    'propulsion/engine[1]/thrust-lbs',
    'propulsion/engine[2]/thrust-lbs',
    'propulsion/engine[3]/thrust-lbs',
    'gear/unit[0]/WOW',
    'gear/unit[1]/WOW',
    'gear/unit[2]/WOW',
]

SIXDOF_VALIDATION_PROPERTIES = [
    "simulation/sim-time-sec",
    "position/h-sl-ft",
    "inertia/cg-x-in",
    "inertia/cg-y-in",
    "inertia/cg-z-in",
    "position/h-sl-meters",
    "position/lat-gc-rad",
    "position/long-gc-rad",
    "position/lat-gc-deg",
    "position/long-gc-deg",
    "position/lat-geod-rad",
    "position/lat-geod-deg",
    "position/geod-alt-ft",
    "position/h-agl-ft",
    "position/geod-alt-km",
    "position/h-agl-km",
    "position/radius-to-vehicle-ft",
    "position/terrain-elevation-asl-ft",
    "position/eci-x-ft",
    "position/eci-y-ft",
    "position/eci-z-ft",
    "position/ecef-x-ft",
    "position/ecef-y-ft",
    "position/ecef-z-ft",
    "position/epa-rad",
    "position/distance-from-start-lon-mt",
    "position/distance-from-start-lat-mt",
    "position/distance-from-start-mag-mt",
    "position/vrp-gc-latitude_deg",
    "position/vrp-longitude_deg",
    "position/vrp-radius-ft",
    "position/from-start-neu-n-ft",
    "position/from-start-neu-e-ft",
    "position/from-start-neu-u-ft",
    "attitude/phi-deg",
    "attitude/theta-deg",
    "attitude/psi-deg",
    "velocities/p-rad_sec",
    "velocities/q-rad_sec",
    "velocities/r-rad_sec",
    "velocities/phidot-rad_sec",
    "velocities/thetadot-rad_sec",
    "velocities/psidot-rad_sec",
    "position/lat-geod-deg",
    "position/long-gc-deg",
    "position/h-sl-meters",
    "position/h-agl-ft",
    "velocities/v-north-fps",
    "velocities/v-east-fps",
    "velocities/v-down-fps",
    "velocities/u-fps",
    "velocities/v-fps",
    "velocities/w-fps",
    "forces/fbx-total-lbs",
    "forces/fby-total-lbs",
    "forces/fbz-total-lbs",
    "moments/l-total-lbsft",
    "moments/m-total-lbsft",
    "moments/n-total-lbsft",
    "accelerations/udot-ft_sec2",
    "accelerations/vdot-ft_sec2",
    "accelerations/wdot-ft_sec2",
    "accelerations/pdot-rad_sec2",
    "accelerations/qdot-rad_sec2",
    "accelerations/rdot-rad_sec2",
    "aero/alpha-deg",
    "aero/beta-deg",
    "aero/qbar-psf",
    "aero/qbar-area",
    "aero/coefficient/CLalpha",
    "aero/coefficient/CD0",
    "aero/coefficient/CDo",
    "aero/coefficient/Cmalpha",
    "aero/coefficient/Cmq",
    "forces/fbx-aero-lbs",
    "forces/fby-aero-lbs",
    "forces/fbz-aero-lbs",
    "moments/l-aero-lbsft",
    "moments/m-aero-lbsft",
    "moments/n-aero-lbsft",
    "fcs/throttle-cmd-norm",
    "fcs/elevator-cmd-norm",
    "fcs/rudder-cmd-norm",
    "velocities/vc-kts",
    "velocities/h-dot-fps",
    "propulsion/engine/thrust-lbs",
    "propulsion/engine[1]/thrust-lbs",
    "propulsion/engine[2]/thrust-lbs",
    "propulsion/engine[3]/thrust-lbs",
    "propulsion/engine[0]/rpm",
    "propulsion/engine[1]/rpm",
    "propulsion/engine[2]/rpm",
    "propulsion/engine[3]/rpm",
    "propulsion/engine/thrust-lbs",
    "propulsion/engine/engine-rpm",
    "propulsion/engine/propeller-rpm",
    "position/h-agl-ft",
    "velocities/v-down-fps",
    "forces/fbz-total-lbs",
    "gear/unit/WOW",
    "gear/unit[0]/WOW",
    "gear/unit[1]/WOW",
    "gear/unit[2]/WOW",
    "gear/unit/compression-ft",
    "gear/unit[0]/compression-ft",
    "gear/unit[1]/compression-ft",
    "gear/unit[2]/compression-ft",
    "gear/unit/compression-velocity-fps",
    "gear/unit[0]/compression-velocity-fps",
    "gear/unit[1]/compression-velocity-fps",
    "gear/unit[2]/compression-velocity-fps",
    "gear/unit/maximum-force-lbs",
    "gear/unit[0]/maximum-force-lbs",
    "gear/unit[1]/maximum-force-lbs",
    "gear/unit[2]/maximum-force-lbs",
    "forces/fbx-gear-lbs",
    "forces/fby-gear-lbs",
    "forces/fbz-gear-lbs",
    "moments/l-gear-lbsft",
    "moments/m-gear-lbsft",
    "moments/n-gear-lbsft",
    "fcs/center-brake-cmd-norm",
    "fcs/left-brake-cmd-norm",
    "fcs/right-brake-cmd-norm",
    "atmosphere/rho-slugs_ft3",
    "atmosphere/P-psf",
    "atmosphere/T-R",
    "atmosphere/wind-north-fps",
    "atmosphere/wind-east-fps",
    "atmosphere/wind-down-fps",
    "atmosphere/total-wind-north-fps",
    "atmosphere/total-wind-east-fps",
    "atmosphere/total-wind-down-fps",
]

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

SIXDOF_POSITION_SI_FIELDS = [
    "time_s",
    "sim_time_s",
    "lat_gc_rad",
    "lon_gc_rad",
    "lat_gc_deg",
    "lon_gc_deg",
    "lat_geod_rad",
    "lat_geod_deg",
    "h_sl_m",
    "h_agl_m",
    "geod_alt_m",
    "geod_alt_km",
    "h_agl_km",
    "terrain_elevation_asl_m",
    "radius_to_vehicle_m",
    "eci_x_m",
    "eci_y_m",
    "eci_z_m",
    "ecef_x_m",
    "ecef_y_m",
    "ecef_z_m",
    "epa_rad",
    "distance_from_start_lon_m",
    "distance_from_start_lat_m",
    "distance_from_start_mag_m",
    "vrp_gc_latitude_deg",
    "vrp_longitude_deg",
    "vrp_radius_m",
    "from_start_neu_n_m",
    "from_start_neu_e_m",
    "from_start_neu_u_m",
    "from_start_ned_d_m",
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


def discover_aircraft() -> list[str]:
    aircraft: list[str] = []
    for path in sorted(AIRCRAFT_DIR.glob("*/*.xml")):
        if path.parent.name == path.stem:
            aircraft.append(path.stem)
    return aircraft


def aircraft_catalog_properties(aircraft: str) -> set[str]:
    proc = subprocess.run(
        [
            str(JSBSIM_DIR / "build" / "src" / "JSBSim"),
            f"--root={JSBSIM_DIR}",
            f"--aircraft={aircraft}",
            "--catalog",
            "--nohighlight",
        ],
        cwd=JSBSIM_DIR,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    properties: set[str] = set()
    for line in proc.stdout.splitlines():
        text = line.strip()
        if not text.endswith((" (R)", " (RW)", " (W)")):
            continue
        properties.add(text.rsplit(" ", 1)[0])
    return properties


def unique_existing_properties(requested: list[str], available: set[str]) -> tuple[list[str], list[str]]:
    selected: list[str] = []
    skipped: list[str] = []
    seen: set[str] = set()
    for prop in requested:
        if prop in seen:
            continue
        seen.add(prop)
        if prop in available:
            selected.append(prop)
        else:
            skipped.append(prop)
    return selected, skipped


def template_output_definition(root):
    for output in root.findall('output'):
        properties = [
            (prop.text or '').strip()
            for prop in output.findall('property')
            if (prop.text or '').strip()
        ]
        if properties:
            return properties, output.get('rate')
    return [], None

def script_aircraft(path: Path) -> str:
    """Return the aircraft folder name for nested scripts, or infer it from legacy flat filenames."""
    try:
        rel = path.relative_to(SCRIPTS_DIR)
    except ValueError:
        return ""
    if len(rel.parts) > 1:
        return rel.parts[0]
    stem = path.stem
    if "__" in stem:
        stem = stem.split("__", 1)[1]
    return stem.split("_", 1)[0]


def script_sort_key(path: Path) -> tuple[str, list[int], str]:
    stem = path.stem
    version = stem.split("__", 1)[0] if "__" in stem else ""
    version_parts: list[int] = []
    for part in version.split("."):
        if part.isdigit():
            version_parts.append(int(part))
        else:
            version_parts = []
            break
    return (str(path.parent), version_parts, path.name)


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def discover_init_files(aircraft: str | None = None) -> list[Path]:
    paths = [
        path
        for path in SCRIPTS_DIR.rglob("*init*.xml")
        if path.is_file() and "__pycache__" not in path.parts
    ]
    if aircraft:
        paths = [path for path in paths if script_aircraft(path) == aircraft]
    return sorted(paths, key=script_sort_key)


def discover_runscripts(aircraft: str | None = None) -> list[Path]:
    paths = [
        path
        for path in SCRIPTS_DIR.rglob("*run*.xml")
        if path.is_file() and path.name != "nonrotating_earth.xml" and "__pycache__" not in path.parts
    ]
    if aircraft:
        paths = [path for path in paths if script_aircraft(path) == aircraft]
    return sorted(paths, key=script_sort_key)


def choose(label: str, options: list[str]) -> str:
    if not options:
        raise RuntimeError(f"No {label} options found")

    print(f"\nSelect {label}:")
    for index, option in enumerate(options, start=1):
        print(f"  {index}. {option}")

    while True:
        answer = input(f"{label} number [1-{len(options)}]: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print("Invalid selection.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run JSBSim with selected aircraft/init/runscript and timestamp outputs.")
    parser.add_argument("--aircraft", help="Aircraft name under /home/junyeopkwon/jsbsim/aircraft")
    parser.add_argument("--init", type=Path, help="Initialize XML path")
    parser.add_argument("--runscript", type=Path, help="Runscript template XML path")
    parser.add_argument(
        "--planet",
        default=None,
        help="Planet XML path, or 'builtin' to use JSBSim's default Earth model",
    )
    parser.add_argument("--show", action="store_true", help="Show plots interactively after saving, if the backend supports it")
    fg_group = parser.add_mutually_exclusive_group()
    fg_group.add_argument("--flightgear", action="store_true", dest="flightgear", help="Run JSBSim in real time and stream FlightGear native-fdm output")
    fg_group.add_argument("--no-flightgear", action="store_false", dest="flightgear", help="Disable FlightGear native-fdm streaming")
    parser.add_argument(
        "--flightgear-logdirective",
        type=Path,
        default=DEFAULT_FLIGHTGEAR_LOGDIRECTIVE,
        help="JSBSim output directive XML for FlightGear streaming",
    )
    parser.set_defaults(flightgear=False)
    return parser.parse_args()


def choose_flightgear_stream(requested: bool | None) -> bool:
    return bool(requested)


def resolve_selection(args: argparse.Namespace) -> tuple[str, Path, Path, Path | None]:
    aircraft = args.aircraft
    if aircraft is None:
        aircraft = choose("aircraft", discover_aircraft())
    elif aircraft not in discover_aircraft():
        raise RuntimeError(f"Aircraft not found: {aircraft}")

    init_path = args.init
    if init_path is None:
        init_options = discover_init_files(aircraft)
        init_choice = choose("init XML", [display_path(path) for path in init_options])
        init_path = init_options[[display_path(path) for path in init_options].index(init_choice)]
    init_path = init_path.expanduser().resolve()
    if not init_path.exists():
        raise RuntimeError(f"Init XML not found: {init_path}")

    runscript_path = args.runscript
    if runscript_path is None:
        runscript_options = discover_runscripts(aircraft)
        runscript_choice = choose("runscript template", [display_path(path) for path in runscript_options])
        runscript_path = runscript_options[[display_path(path) for path in runscript_options].index(runscript_choice)]
    runscript_path = runscript_path.expanduser().resolve()
    if not runscript_path.exists():
        raise RuntimeError(f"Runscript XML not found: {runscript_path}")

    if args.planet is None:
        planet_path = None
    elif str(args.planet).lower() in {"builtin", "default", "none"}:
        planet_path = None
    else:
        planet_path = Path(args.planet).expanduser().resolve()
        if not planet_path.exists():
            raise RuntimeError(f"Planet XML not found: {planet_path}")

    return aircraft, init_path, runscript_path, planet_path


def indent_xml(element: ET.Element, level: int = 0) -> None:
    prefix = "\n" + level * "  "
    child_prefix = "\n" + (level + 1) * "  "
    children = list(element)
    if children:
        if not element.text or not element.text.strip():
            element.text = child_prefix
        for child in children:
            indent_xml(child, level + 1)
        if not children[-1].tail or not children[-1].tail.strip():
            children[-1].tail = prefix
    if level and (not element.tail or not element.tail.strip()):
        element.tail = prefix


def gravity_model_for_planet(planet_path: Path) -> int:
    root = ET.parse(planet_path).getroot()
    gravity_model_text = root.findtext("gravity_model")
    if gravity_model_text is not None:
        gravity_model = gravity_model_text.strip()
        if gravity_model in {"gtStandard", "standard", "0"}:
            return 0
        if gravity_model in {"gtWGS84", "wgs84", "1"}:
            return 1
        raise RuntimeError(f"Unknown gravity_model in {planet_path}: {gravity_model}")

    j2_text = root.findtext("J2")
    if j2_text is None:
        return 1
    return 0 if float(j2_text.strip()) == 0.0 else 1


def ensure_gravity_model(root: ET.Element, gravity_model: int) -> None:
    run = root.find("run")
    if run is None:
        run = ET.Element("run")
        insert_at = 1 if root.find("use") is not None else 0
        root.insert(insert_at, run)

    for prop in run.findall("property"):
        if (prop.text or "").strip() == "simulation/gravity-model":
            prop.set("value", str(gravity_model))
            prop.set("persistent", "true")
            return

    prop = ET.Element("property", {"value": str(gravity_model), "persistent": "true"})
    prop.text = " simulation/gravity-model "
    run.insert(0, prop)


def build_runscript(
    aircraft: str,
    init_path: Path,
    template_path: Path,
    planet_path: Path | None,
    raw_path: Path,
    sixdof_path: Path,
    stamp: str,
    scenario: str,
    run_id: str,
) -> tuple[Path, list[str]]:
    tree = ET.parse(template_path)
    root = tree.getroot()
    root.set("name", f"{aircraft}_selected_{stamp}")
    template_output_properties, template_output_rate = template_output_definition(root)

    use = root.find("use")
    if use is None:
        use = ET.Element("use")
        root.insert(0, use)
    use.set("aircraft", aircraft)
    use.set("initialize", str(init_path))

    if planet_path is not None:
        ensure_gravity_model(root, gravity_model_for_planet(planet_path))

    for old_output in list(root.findall("output")):
        root.remove(old_output)

    if aircraft == 'LiftCruise2kg' and template_output_properties:
        output_properties = template_output_properties
        output_rate = template_output_rate or '120'
    else:
        output_properties = list(OUTPUT_PROPERTIES)
        output_rate = '120'
    if aircraft.endswith("_landing"):
        output_properties.extend(prop for prop in LANDING_OUTPUT_PROPERTIES if prop not in output_properties)
    if aircraft == "F450":
        output_properties.extend(prop for prop in F450_OUTPUT_PROPERTIES if prop not in output_properties)

    output_name = "../jsbsim_workflow/" + raw_path.relative_to(ROOT).as_posix()
    output = ET.SubElement(root, 'output', {'name': output_name, 'type': 'CSV', 'rate': output_rate})
    for prop in output_properties:
        prop_element = ET.SubElement(output, "property")
        prop_element.text = f" {prop} "

    sixdof_name = "../jsbsim_workflow/" + sixdof_path.relative_to(ROOT).as_posix()
    available_properties = aircraft_catalog_properties(aircraft)
    sixdof_properties, skipped_properties = unique_existing_properties(SIXDOF_VALIDATION_PROPERTIES, available_properties)
    sixdof_output = ET.SubElement(root, "output", {"name": sixdof_name, "type": "CSV", "rate": "120"})
    for prop in sixdof_properties:
        prop_element = ET.SubElement(sixdof_output, "property")
        prop_element.text = f" {prop} "

    generated_path = GENERATED_DIR / aircraft / scenario / f"{run_id}_runscript_{stamp}.xml"
    generated_path.parent.mkdir(parents=True, exist_ok=True)
    indent_xml(root)
    ET.ElementTree(root).write(generated_path, encoding="UTF-8", xml_declaration=True)
    return generated_path, skipped_properties


def run_jsbsim(
    planet_path: Path | None,
    runscript_path: Path,
    console_path: Path,
    *,
    realtime: bool = False,
    logdirective_path: Path | None = None,
) -> None:
    cmd = [
        str(JSBSIM_DIR / "build" / "src" / "JSBSim"),
        f"--script={runscript_path}",
        "--root=.",
    ]
    if planet_path is not None:
        cmd.insert(1, f"--planet={planet_path}")
    if realtime:
        cmd.insert(1, "--realtime")
    if logdirective_path is not None:
        cmd.insert(1, f"--logdirectivefile={logdirective_path}")
    with console_path.open("w", encoding="utf-8") as console:
        subprocess.run(cmd, cwd=JSBSIM_DIR, stdout=console, stderr=subprocess.STDOUT, check=True)


def update_workflow_excel() -> None:
    if not WORKFLOW_EXCEL_SCRIPT.exists():
        print(f"Workflow Excel updater not found: {WORKFLOW_EXCEL_SCRIPT}")
        return
    try:
        subprocess.run(
            ["python3", str(WORKFLOW_EXCEL_SCRIPT)],
            cwd=ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        print("Workflow Excel update failed.")
        if exc.stderr:
            print(exc.stderr.strip())


def convert_raw_to_si(raw_path: Path, si_path: Path) -> list[dict[str, float]]:
    with raw_path.open(newline="", encoding="utf-8") as src:
        raw_rows = list(csv.DictReader(src))

    if not raw_rows:
        raise RuntimeError(f"No rows found in {raw_path}")

    missing = [
        source
        for source, _, _ in RAW_TO_SI_FIELDS
        if source not in raw_rows[0] and source not in OPTIONAL_RAW_DEFAULTS
    ]
    if missing:
        raise RuntimeError(f"Raw CSV is missing required properties: {missing}")

    rows: list[dict[str, float]] = []
    for raw in raw_rows:
        rows.append(
            {
                target: float(raw[source]) * scale if source in raw else OPTIONAL_RAW_DEFAULTS[source]
                for source, target, scale in RAW_TO_SI_FIELDS
            }
        )

    add_plot_csv_fields(rows)

    si_path.parent.mkdir(parents=True, exist_ok=True)
    with si_path.open("w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(dst, fieldnames=PLOT_CSV_FIELDS)
        writer.writeheader()
        writer.writerows({field: row[field] for field in PLOT_CSV_FIELDS} for row in rows)

    return rows


def raw_value(row: dict[str, str], source: str) -> float:
    value = row.get(source, "")
    return float(value) if value != "" else math.nan


def convert_sixdof_raw_to_si(sixdof_raw_path: Path, sixdof_si_path: Path) -> None:
    with sixdof_raw_path.open(newline="", encoding="utf-8") as src:
        raw_rows = list(csv.DictReader(src))

    if not raw_rows:
        raise RuntimeError(f"No rows found in {sixdof_raw_path}")

    prefix = "/fdm/jsbsim/"
    rows: list[dict[str, float]] = []
    for raw in raw_rows:
        from_start_u_m = raw_value(raw, prefix + "position/from-start-neu-u-ft") * FT_TO_M
        rows.append(
            {
                "time_s": raw_value(raw, "Time"),
                "sim_time_s": raw_value(raw, prefix + "simulation/sim-time-sec"),
                "lat_gc_rad": raw_value(raw, prefix + "position/lat-gc-rad"),
                "lon_gc_rad": raw_value(raw, prefix + "position/long-gc-rad"),
                "lat_gc_deg": raw_value(raw, prefix + "position/lat-gc-deg"),
                "lon_gc_deg": raw_value(raw, prefix + "position/long-gc-deg"),
                "lat_geod_rad": raw_value(raw, prefix + "position/lat-geod-rad"),
                "lat_geod_deg": raw_value(raw, prefix + "position/lat-geod-deg"),
                "h_sl_m": raw_value(raw, prefix + "position/h-sl-meters"),
                "h_agl_m": raw_value(raw, prefix + "position/h-agl-ft") * FT_TO_M,
                "geod_alt_m": raw_value(raw, prefix + "position/geod-alt-ft") * FT_TO_M,
                "geod_alt_km": raw_value(raw, prefix + "position/geod-alt-km"),
                "h_agl_km": raw_value(raw, prefix + "position/h-agl-km"),
                "terrain_elevation_asl_m": raw_value(raw, prefix + "position/terrain-elevation-asl-ft") * FT_TO_M,
                "radius_to_vehicle_m": raw_value(raw, prefix + "position/radius-to-vehicle-ft") * FT_TO_M,
                "eci_x_m": raw_value(raw, prefix + "position/eci-x-ft") * FT_TO_M,
                "eci_y_m": raw_value(raw, prefix + "position/eci-y-ft") * FT_TO_M,
                "eci_z_m": raw_value(raw, prefix + "position/eci-z-ft") * FT_TO_M,
                "ecef_x_m": raw_value(raw, prefix + "position/ecef-x-ft") * FT_TO_M,
                "ecef_y_m": raw_value(raw, prefix + "position/ecef-y-ft") * FT_TO_M,
                "ecef_z_m": raw_value(raw, prefix + "position/ecef-z-ft") * FT_TO_M,
                "epa_rad": raw_value(raw, prefix + "position/epa-rad"),
                "distance_from_start_lon_m": raw_value(raw, prefix + "position/distance-from-start-lon-mt"),
                "distance_from_start_lat_m": raw_value(raw, prefix + "position/distance-from-start-lat-mt"),
                "distance_from_start_mag_m": raw_value(raw, prefix + "position/distance-from-start-mag-mt"),
                "vrp_gc_latitude_deg": raw_value(raw, prefix + "position/vrp-gc-latitude_deg"),
                "vrp_longitude_deg": raw_value(raw, prefix + "position/vrp-longitude_deg"),
                "vrp_radius_m": raw_value(raw, prefix + "position/vrp-radius-ft") * FT_TO_M,
                "from_start_neu_n_m": raw_value(raw, prefix + "position/from-start-neu-n-ft") * FT_TO_M,
                "from_start_neu_e_m": raw_value(raw, prefix + "position/from-start-neu-e-ft") * FT_TO_M,
                "from_start_neu_u_m": from_start_u_m,
                "from_start_ned_d_m": -from_start_u_m,
            }
        )

    sixdof_si_path.parent.mkdir(parents=True, exist_ok=True)
    with sixdof_si_path.open("w", newline="", encoding="utf-8") as dst:
        writer = csv.DictWriter(dst, fieldnames=SIXDOF_POSITION_SI_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


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


def add_local_enu(rows: list[dict[str, float]]) -> None:
    origin = rows[0]
    for row in rows:
        east, north, up = ecef_delta_to_enu(row, origin)
        row["local_E_m"] = east
        row["local_N_m"] = north
        row["local_D_m"] = -up


def add_plot_csv_fields(rows: list[dict[str, float]]) -> None:
    add_local_enu(rows)
    for row in rows:
        row["distance_m"] = math.sqrt(
            row["local_N_m"] ** 2 + row["local_E_m"] ** 2 + row["local_D_m"] ** 2
        )
        row["v_total_mps"] = math.sqrt(
            row["v_n_mps"] ** 2 + row["v_e_mps"] ** 2 + row["v_d_mps"] ** 2
        )


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


def series(rows: list[dict[str, float]], name: str) -> list[float]:
    return [row[name] for row in rows]


def scenario_name(aircraft: str, template_path: Path) -> str:
    name = template_path.stem
    prefix = f"{aircraft}_"
    if name.startswith(prefix):
        name = name[len(prefix):]
    if name.endswith("_run"):
        name = name[:-4]
    return name


def split_versioned_scenario(scenario: str) -> tuple[str, str]:
    if "__" not in scenario:
        return "0.0", scenario
    version, label = scenario.split("__", 1)
    parts = version.split(".")
    if len(parts) >= 2 and all(part.isdigit() for part in parts[:2]):
        return ".".join(parts[:2]), label
    return "0.0", label


def next_run_id(aircraft: str, scenario: str) -> str:
    version, label = split_versioned_scenario(scenario)
    scenario_dirs = [
        RAW_CSV_DIR / aircraft / scenario,
        SI_CSV_DIR / aircraft / scenario,
        SIXDOF_CSV_DIR / aircraft / scenario,
        SIXDOF_SI_CSV_DIR / aircraft / scenario,
        CONSOLE_DIR / aircraft / scenario,
        PLOTS_DIR / aircraft / scenario,
        GENERATED_DIR / aircraft / scenario,
    ]
    max_patch = 0
    prefix = f"{version}."
    marker = f"__{label}"
    for directory in scenario_dirs:
        if not directory.exists():
            continue
        for path in directory.iterdir():
            name = path.name
            if not name.startswith(prefix) or marker not in name:
                continue
            patch_text = name[len(prefix):].split("__", 1)[0]
            if patch_text.isdigit():
                max_patch = max(max_patch, int(patch_text))
    return f"{version}.{max_patch + 1}__{label}"


def set_axes_equal(ax, x: list[float], y: list[float], z: list[float]) -> None:
    x_mid = (max(x) + min(x)) / 2.0
    y_mid = (max(y) + min(y)) / 2.0
    z_mid = (max(z) + min(z)) / 2.0
    max_range = max(max(x) - min(x), max(y) - min(y), max(z) - min(z))
    half_range = max_range / 2.0 if max_range > 0.0 else 1.0
    ax.set_xlim(x_mid - half_range, x_mid + half_range)
    ax.set_ylim(y_mid - half_range, y_mid + half_range)
    ax.set_zlim(z_mid - half_range, z_mid + half_range)
    ax.set_box_aspect((1, 1, 1))


def plot_trajectory(aircraft: str, rows: list[dict[str, float]], output_path: Path, *, show: bool) -> None:
    east = series(rows, "local_E_m")
    north = series(rows, "local_N_m")
    altitude = series(rows, "altitude_m")

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(east, north, altitude, linewidth=1.4)
    ax.scatter([east[0]], [north[0]], [altitude[0]], label="start", s=28)
    ax.scatter([east[-1]], [north[-1]], [altitude[-1]], label="end", s=28)
    set_axes_equal(ax, east, north, altitude)
    z_top = max(ax.get_zlim()[1], max(altitude) * 1.05, 1.0)
    ax.set_zlim(0.0, z_top)
    ax.set_xlabel("East (m)")
    ax.set_ylabel("North (m)")
    ax.set_zlabel("Altitude AGL (m)")
    ax.set_title(f"{aircraft} trajectory")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    if show:
        plt.show()
    plt.close(fig)



def plot_trajectory_xy(aircraft, rows, output_path, *, show):
    e0 = rows[0]["local_E_m"]
    n0 = rows[0]["local_N_m"]
    east = [row["local_E_m"] - e0 for row in rows]
    north = [row["local_N_m"] - n0 for row in rows]
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.plot(east, north, linewidth=1.4, label="trajectory")
    ax.scatter([0.0], [0.0], label="start", s=36, zorder=3)
    ax.scatter([east[-1]], [north[-1]], label="end", s=36, zorder=3)
    ax.axhline(0.0, color="0.75", linewidth=0.8)
    ax.axvline(0.0, color="0.75", linewidth=0.8)
    mid_e = (max(east) + min(east)) / 2.0
    mid_n = (max(north) + min(north)) / 2.0
    span = max(max(east) - min(east), max(north) - min(north))
    half = span / 2.0 if span > 0.0 else 1.0
    ax.set_xlim(mid_e - half, mid_e + half)
    ax.set_ylim(mid_n - half, mid_n + half)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("East from start (m)")
    ax.set_ylabel("North from start (m)")
    ax.set_title(str(aircraft) + " XY trajectory")
    ax.grid(True, linewidth=0.4, alpha=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    if show:
        plt.show()
    plt.close(fig)

def plot_states_vs_time(aircraft: str, rows: list[dict[str, float]], output_path: Path, *, show: bool) -> None:
    t = series(rows, "time_s")
    yaw_unwrapped = unwrap_degrees(series(rows, "yaw_deg"))
    outputs = [
        ("local_E_m", "East (m)"),
        ("local_N_m", "North (m)"),
        ("local_D_m", "Down from start (m)"),
        ("altitude_m", "Altitude (m)"),
        ("v_n_mps", "V north NED (m/s)"),
        ("v_e_mps", "V east NED (m/s)"),
        ("v_d_mps", "V down NED (m/s)"),
        ("roll_deg", "roll (deg)"),
        ("pitch_deg", "pitch (deg)"),
        ("yaw_unwrapped_deg", "yaw unwrapped (deg)"),
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
        ax.set_xlabel("Time (s)")
    fig.suptitle(f"{aircraft} states vs time", y=0.995)
    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    if show:
        plt.show()
    plt.close(fig)


def strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def parse_event_markers(console_path: Path) -> list[tuple[float, str]]:
    if not console_path.exists():
        return []
    markers: list[tuple[float, str]] = []
    seen: set[tuple[int, float]] = set()
    pattern = re.compile(r"\(Event\s+(\d+)\)\s+executed at time:\s*([0-9]+(?:\.[0-9]+)?)")
    for line in console_path.read_text(encoding="utf-8", errors="replace").splitlines():
        clean = strip_ansi(line)
        match = pattern.search(clean)
        if not match:
            continue
        event_id = int(match.group(1))
        time_s = float(match.group(2))
        key = (event_id, time_s)
        if key in seen:
            continue
        seen.add(key)
        markers.append((time_s, str(event_id)))
    return markers if len(markers) >= 2 else []


def safe_filename(name: str) -> str:
    clean = name.strip().replace("/fdm/jsbsim/", "")
    clean = clean.replace("/", "_")
    clean = re.sub(r"[^A-Za-z0-9_.-]+", "_", clean)
    clean = clean.strip("._")
    return clean[:150] or "property"


def parse_float(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def read_numeric_csv(path: Path) -> tuple[str, list[float], dict[str, list[float]]]:
    with path.open(newline="", encoding="utf-8") as src:
        reader = csv.DictReader(src)
        raw_rows = list(reader)
        fieldnames = reader.fieldnames or []
    if not raw_rows:
        return "", [], {}
    time_col = "time_s" if "time_s" in fieldnames else "Time" if "Time" in fieldnames else "simulation/sim-time-sec"
    if time_col not in fieldnames and "/fdm/jsbsim/simulation/sim-time-sec" in fieldnames:
        time_col = "/fdm/jsbsim/simulation/sim-time-sec"
    if time_col not in fieldnames:
        raise RuntimeError(f"No time column found in {path}")
    time_s = [parse_float(row.get(time_col, "")) for row in raw_rows]
    data: dict[str, list[float]] = {}
    for field in fieldnames:
        if field == time_col:
            continue
        values = [parse_float(row.get(field, "")) for row in raw_rows]
        if any(math.isfinite(value) for value in values):
            data[field] = values
    return time_col, time_s, data


def merge_secondary_numeric_csv(
    data: dict[str, list[float]],
    base_time_s: list[float],
    secondary_path: Path,
) -> None:
    try:
        _, secondary_time_s, secondary_data = read_numeric_csv(secondary_path)
    except Exception:
        return
    if len(secondary_time_s) != len(base_time_s):
        return
    for name, values in secondary_data.items():
        if name not in data and len(values) == len(base_time_s):
            data[name] = values


def converted_series(name: str, values: list[float]) -> tuple[str, str, list[float]] | None:
    lower = name.lower()
    if "rad_sec2" in lower:
        return f"{name} [deg/s^2]", "deg/s^2", [value * RAD_TO_DEG for value in values]
    if "rad_sec" in lower:
        return f"{name} [deg/s]", "deg/s", [value * RAD_TO_DEG for value in values]
    if lower.endswith("-rad") or lower.endswith("/rad") or lower.endswith("_rad") or lower.endswith("rad"):
        return f"{name} [deg]", "deg", [value * RAD_TO_DEG for value in values]
    if "ft_sec2" in lower:
        return f"{name} [m/s^2]", "m/s^2", [value * FT_S2_TO_M_S2 for value in values]
    if lower.endswith("-fps") or lower.endswith("/fps") or lower.endswith("_fps") or "-ft_sec" in lower:
        return f"{name} [m/s]", "m/s", [value * FPS_TO_MPS for value in values]
    if lower.endswith("-ft") or lower.endswith("/ft") or lower.endswith("_ft"):
        return f"{name} [m]", "m", [value * FT_TO_M for value in values]
    if "slugs_ft2" in lower:
        return f"{name} [kg*m^2]", "kg*m^2", [value * SLUG_FT2_TO_KG_M2 for value in values]
    if lower.endswith("-slugs") or lower.endswith("/slugs") or lower.endswith("_slugs"):
        return f"{name} [kg]", "kg", [value * SLUG_TO_KG for value in values]
    return None


def finite_xy(time_s: list[float], values: list[float]) -> tuple[list[float], list[float]]:
    pairs = [(t, value) for t, value in zip(time_s, values) if math.isfinite(t) and math.isfinite(value)]
    if not pairs:
        return [], []
    x, y = zip(*pairs)
    return list(x), list(y)



def configure_plain_y_axis(ax) -> None:
    formatter = ScalarFormatter(useOffset=False)
    formatter.set_scientific(False)
    ax.yaxis.set_major_formatter(formatter)


def is_absolute_position_series(name: str) -> bool:
    lower = name.lower()
    position_tokens = (
        'position/ecef-',
        'position/eci-',
        '/ecef-',
        '/eci-',
        'ecef_',
        'eci_',
    )
    unit_tokens = ('-ft', '_ft', '/ft', '[m]', '_m', '-m', '/m')
    return any(token in lower for token in position_tokens) and any(token in lower for token in unit_tokens)


def is_start_relative_position_series(name: str) -> bool:
    lower = name.lower()
    return (
        'from_start' in lower
        or 'distance-from-start' in lower
        or 'distance_from_start' in lower
    )


def zero_initial_value(values: list[float]) -> list[float]:
    baseline = next((value for value in values if math.isfinite(value)), 0.0)
    return [value - baseline if math.isfinite(value) else value for value in values]


def set_default_origin(ax, x_values: list[float], y_values: list[float]) -> None:
    finite_x = [value for value in x_values if math.isfinite(value)]
    finite_y = [value for value in y_values if math.isfinite(value)]
    if finite_x and min(finite_x) >= -1.0e-9:
        ax.set_xlim(left=0.0)
    if finite_y and min(finite_y) >= -1.0e-2:
        ax.set_ylim(bottom=0.0)


def display_series_for_axis(name: str, ylabel: str, values: list[float]) -> tuple[str, str, list[float]]:
    finite = [value for value in values if math.isfinite(value)]
    if not finite:
        return name, ylabel, values
    if is_start_relative_position_series(name):
        return name, ylabel, zero_initial_value(values)
    if not is_absolute_position_series(name):
        return name, ylabel, values

    baseline = finite[0]
    span = max(finite) - min(finite)
    magnitude = max(abs(value) for value in finite)
    if magnitude > 10000.0 and span < magnitude * 0.05:
        return f'{name} delta from initial', f'Delta {ylabel} from initial', [value - baseline for value in values]
    return name, ylabel, values

def add_event_lines(ax, event_markers: list[tuple[float, str]]) -> None:
    if len(event_markers) < 2:
        return
    for time_s, _label in sorted(event_markers, key=lambda item: item[0]):
        ax.axvline(time_s, color='red', linestyle='--', linewidth=0.8, alpha=0.62, label='_nolegend_')


def add_event_strip(event_ax, event_markers: list[tuple[float, str]]) -> None:
    markers = sorted(event_markers, key=lambda item: item[0])
    if len(markers) < 2:
        event_ax.set_axis_off()
        return

    event_ax.set_ylim(0.0, 1.0)
    event_ax.set_yticks([])
    event_ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    event_ax.grid(False)
    for side in ('left', 'right', 'top'):
        event_ax.spines[side].set_visible(False)
    event_ax.spines['bottom'].set_visible(False)

    label_y = 0.96
    for time_s, label in markers:
        event_ax.axvline(time_s, ymin=0.03, ymax=0.96, color='red', linestyle='--', linewidth=0.8, alpha=0.72)
        event_ax.text(
            time_s,
            label_y,
            label,
            ha='center',
            va='center',
            fontsize=7,
            color='white',
            fontweight='bold',
            bbox=dict(boxstyle='circle,pad=0.24', facecolor='red', edgecolor='red', linewidth=0.5, alpha=0.90),
            clip_on=False,
        )



def legend_outside(ax, handles: list[object], labels: list[str]) -> None:
    unique: dict[str, object] = {}
    for handle, label in zip(handles, labels):
        if label and not label.startswith('_') and label not in unique:
            unique[label] = handle
    if unique:
        ax.legend(unique.values(), unique.keys(), loc='upper left', bbox_to_anchor=(1.015, 1.0), borderaxespad=0.0, fontsize=8)


def legend_below_x_axis(ax, handles: list[object], labels: list[str]) -> None:
    unique: dict[str, object] = {}
    for handle, label in zip(handles, labels):
        if label and not label.startswith('_') and label not in unique:
            unique[label] = handle
    if unique:
        ax.legend(
            unique.values(),
            unique.keys(),
            loc='upper center',
            bbox_to_anchor=(0.5, -0.18),
            borderaxespad=0.0,
            fontsize=8,
            ncol=1,
        )


def plot_single_time_series(time_s: list[float], values: list[float], name: str, ylabel: str, output_path: Path, event_markers: list[tuple[float, str]]) -> bool:
    plot_name, plot_ylabel, plot_values = display_series_for_axis(name, ylabel, values)
    x, y = finite_xy(time_s, plot_values)
    if not x:
        return False
    output_path.parent.mkdir(parents=True, exist_ok=True)
    has_events = len(event_markers) >= 2
    if has_events:
        fig, (event_ax, ax) = plt.subplots(2, 1, figsize=(10, 5.1), sharex=True, gridspec_kw=dict(height_ratios=[0.32, 4.0], hspace=0.02))
    else:
        fig, ax = plt.subplots(figsize=(10, 5))
        event_ax = None
    ax.plot(x, y, linewidth=1.1)
    set_default_origin(ax, x, y)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel(plot_ylabel)
    fig.suptitle(plot_name, y=0.985)
    configure_plain_y_axis(ax)
    ax.grid(True, alpha=0.35)
    add_event_lines(ax, event_markers)
    if event_ax is not None:
        event_ax.set_xlim(ax.get_xlim())
        add_event_strip(event_ax, event_markers)
        fig.subplots_adjust(left=0.09, right=0.98, bottom=0.10, top=0.91, hspace=0.02)
    else:
        fig.subplots_adjust(left=0.09, right=0.98, bottom=0.10, top=0.92)
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return True


def plot_csv_time_series(csv_path: Path, output_dir: Path, event_markers: list[tuple[float, str]], *, converted_dir: Path | None = None) -> tuple[int, int]:
    _, time_s, data = read_numeric_csv(csv_path)
    count = 0
    converted_count = 0
    for name, values in data.items():
        filename = safe_filename(name) + ".png"
        if plot_single_time_series(time_s, values, name, name, output_dir / filename, event_markers):
            count += 1
        conversion = converted_series(name, values)
        if converted_dir is not None and conversion is not None:
            converted_name, unit, converted_values = conversion
            converted_filename = safe_filename(converted_name) + ".png"
            if plot_single_time_series(time_s, converted_values, converted_name, unit, converted_dir / converted_filename, event_markers):
                converted_count += 1
    return count, converted_count


def get_series(data: dict[str, list[float]], candidates: list[str]) -> tuple[str, list[float]] | None:
    for name in candidates:
        if name in data:
            return name, data[name]
        prefixed = f"/fdm/jsbsim/{name}"
        if prefixed in data:
            return prefixed, data[prefixed]
    return None


def convert_for_axis(name: str, values: list[float]) -> tuple[str, list[float]]:
    conversion = converted_series(name, values)
    if conversion is None:
        return name, values
    converted_name, _, converted_values = conversion
    return converted_name, converted_values


def derive_total_speed_series(data: dict[str, list[float]]) -> None:
    if "derived/v-total-fps" in data:
        return
    north = get_series(data, ["velocities/v-north-fps"])
    east = get_series(data, ["velocities/v-east-fps"])
    down = get_series(data, ["velocities/v-down-fps"])
    if north is not None and east is not None and down is not None:
        data["derived/v-total-fps"] = [
            math.sqrt(n * n + e * e + d * d) if math.isfinite(n) and math.isfinite(e) and math.isfinite(d) else math.nan
            for n, e, d in zip(north[1], east[1], down[1])
        ]
        return

    u = get_series(data, ["velocities/u-fps"])
    v = get_series(data, ["velocities/v-fps"])
    w = get_series(data, ["velocities/w-fps"])
    if u is not None and v is not None and w is not None:
        data["derived/v-total-fps"] = [
            math.sqrt(u_value * u_value + v_value * v_value + w_value * w_value)
            if math.isfinite(u_value) and math.isfinite(v_value) and math.isfinite(w_value)
            else math.nan
            for u_value, v_value, w_value in zip(u[1], v[1], w[1])
        ]


def plot_dual_axis_multi_right(
    time_s: list[float],
    left_name: str,
    left_values: list[float],
    right_items: list[tuple[str, list[float]]],
    output_path: Path,
    event_markers: list[tuple[float, str]],
    *,
    right_axis_label: str,
) -> bool:
    left_label, left = convert_for_axis(left_name, left_values)
    left_title, left_axis_label, left = display_series_for_axis(left_label, left_label, left)
    converted_right: list[tuple[str, list[float]]] = [convert_for_axis(name, values) for name, values in right_items]
    valid = [
        (index, t, left_value, [values[index] for _, values in converted_right])
        for index, (t, left_value) in enumerate(zip(time_s, left))
        if math.isfinite(t)
        and math.isfinite(left_value)
        and all(math.isfinite(values[index]) for _, values in converted_right)
    ]
    if not valid:
        return False

    x = [item[1] for item in valid]
    y_left = [item[2] for item in valid]
    y_right_sets = [[item[3][series_index] for item in valid] for series_index in range(len(converted_right))]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    has_events = len(event_markers) >= 2
    if has_events:
        fig, (event_ax, ax_left) = plt.subplots(2, 1, figsize=(10, 5.1), sharex=True, gridspec_kw=dict(height_ratios=[0.32, 4.0], hspace=0.02))
    else:
        fig, ax_left = plt.subplots(figsize=(10, 5))
        event_ax = None
    ax_right = ax_left.twinx()

    left_line, = ax_left.plot(x, y_left, color='tab:blue', linewidth=1.1, label=left_label)
    colors = ['tab:orange', 'tab:green', 'tab:red', 'tab:purple']
    right_lines = []
    for (label, _), y_values, color in zip(converted_right, y_right_sets, colors):
        line, = ax_right.plot(x, y_values, color=color, linewidth=1.1, label=label)
        right_lines.append(line)

    ax_left.set_xlabel('Time (s)')
    ax_left.set_ylabel(left_axis_label, color='tab:blue')
    ax_right.set_ylabel(right_axis_label, color='tab:orange')
    configure_plain_y_axis(ax_left)
    configure_plain_y_axis(ax_right)
    ax_left.tick_params(axis='y', labelcolor='tab:blue')
    ax_right.tick_params(axis='y', labelcolor='tab:orange')
    ax_left.grid(True, alpha=0.35)
    set_default_origin(ax_left, x, y_left)
    flat_right_values = [value for values in y_right_sets for value in values]
    set_default_origin(ax_right, x, flat_right_values)
    add_event_lines(ax_left, event_markers)
    if event_ax is not None:
        event_ax.set_xlim(ax_left.get_xlim())
        add_event_strip(event_ax, event_markers)
    handles = [left_line, *right_lines]
    labels = [left_label, *[label for label, _ in converted_right]]
    legend_below_x_axis(ax_left, handles, labels)
    right_title = " vs ".join(label for label, _ in converted_right)
    fig.suptitle(f'{left_title} vs {right_title}', y=0.985)
    if event_ax is not None:
        fig.subplots_adjust(left=0.09, right=0.90, bottom=0.31, top=0.91, hspace=0.02)
    else:
        fig.subplots_adjust(left=0.09, right=0.90, bottom=0.31, top=0.92)
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return True


def plot_dual_axis(time_s: list[float], left_name: str, left_values: list[float], right_name: str, right_values: list[float], output_path: Path, event_markers: list[tuple[float, str]]) -> bool:
    left_label, left = convert_for_axis(left_name, left_values)
    right_label, right = convert_for_axis(right_name, right_values)
    left_title, left_axis_label, left = display_series_for_axis(left_label, left_label, left)
    right_title, right_axis_label, right = display_series_for_axis(right_label, right_label, right)
    valid = [(t, l, r) for t, l, r in zip(time_s, left, right) if math.isfinite(t) and math.isfinite(l) and math.isfinite(r)]
    if not valid:
        return False
    x = [item[0] for item in valid]
    y_left = [item[1] for item in valid]
    y_right = [item[2] for item in valid]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    has_events = len(event_markers) >= 2
    if has_events:
        fig, (event_ax, ax_left) = plt.subplots(2, 1, figsize=(10, 5.1), sharex=True, gridspec_kw=dict(height_ratios=[0.32, 4.0], hspace=0.02))
    else:
        fig, ax_left = plt.subplots(figsize=(10, 5))
        event_ax = None
    ax_right = ax_left.twinx()
    left_line, = ax_left.plot(x, y_left, color='tab:blue', linewidth=1.1, label=left_label)
    right_line, = ax_right.plot(x, y_right, color='tab:orange', linewidth=1.1, label=right_label)
    ax_left.set_xlabel('Time (s)')
    ax_left.set_ylabel(left_axis_label, color='tab:blue')
    ax_right.set_ylabel(right_axis_label, color='tab:orange')
    configure_plain_y_axis(ax_left)
    configure_plain_y_axis(ax_right)
    ax_left.tick_params(axis='y', labelcolor='tab:blue')
    ax_right.tick_params(axis='y', labelcolor='tab:orange')
    ax_left.grid(True, alpha=0.35)
    set_default_origin(ax_left, x, y_left)
    set_default_origin(ax_right, x, y_right)
    add_event_lines(ax_left, event_markers)
    if event_ax is not None:
        event_ax.set_xlim(ax_left.get_xlim())
        add_event_strip(event_ax, event_markers)
    legend_below_x_axis(ax_left, [left_line, right_line], [left_label, right_label])
    fig.suptitle(f'{left_title} vs {right_title}', y=0.985)
    if event_ax is not None:
        fig.subplots_adjust(left=0.09, right=0.90, bottom=0.27, top=0.91, hspace=0.02)
    else:
        fig.subplots_adjust(left=0.09, right=0.90, bottom=0.27, top=0.92)
    fig.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return True


def plot_sixdof_dual_axis(sixdof_raw_path: Path, raw_path: Path, output_dir: Path, event_markers: list[tuple[float, str]]) -> int:
    _, time_s, data = read_numeric_csv(sixdof_raw_path)
    merge_secondary_numeric_csv(data, time_s, raw_path)
    derive_total_speed_series(data)
    pairs = [
        ("altitude_vs_vertical_speed", ["position/h-agl-ft"], ["velocities/v-down-fps"]),
        ("altitude_vs_total_speed", ["position/h-agl-ft"], ["derived/v-total-fps"]),
        ("altitude_vs_calibrated_airspeed", ["position/h-agl-ft"], ["velocities/vc-kts"]),
        ("alt_vs_vc_kts", ["position/h-agl-ft"], ["velocities/vc-kts"]),
        ("elevator_command_vs_pitch", ["fcs/elevator-cmd-norm"], ["attitude/theta-deg"]),
        ("rudder_command_vs_heading", ["fcs/rudder-cmd-norm"], ["attitude/psi-deg"]),
        ("altitude_capture_vs_climb_rate", ["position/h-agl-ft"], ["velocities/h-dot-fps"]),
        ("pitch_vs_pitch_rate", ["attitude/theta-deg"], ["velocities/q-rad_sec"]),
        ("roll_vs_roll_rate", ["attitude/phi-deg"], ["velocities/p-rad_sec"]),
        ("yaw_vs_yaw_rate", ["attitude/psi-deg"], ["velocities/r-rad_sec"]),
        ("alpha_vs_qbar", ["aero/alpha-deg"], ["aero/qbar-psf"]),
        ("u_vs_udot", ["velocities/u-fps"], ["accelerations/udot-ft_sec2"]),
        ("v_vs_vdot", ["velocities/v-fps"], ["accelerations/vdot-ft_sec2"]),
        ("w_vs_wdot", ["velocities/w-fps"], ["accelerations/wdot-ft_sec2"]),
        ("aero_normal_force_vs_pitch_moment", ["forces/fbz-aero-lbs"], ["moments/m-aero-lbsft"]),
        ("gear_contact_vs_agl", ["gear/unit[1]/WOW", "gear/unit/WOW"], ["position/h-agl-ft"]),
        ("gear_compression_vs_vertical_speed", ["gear/unit[1]/compression-ft", "gear/unit/compression-ft"], ["velocities/v-down-fps"]),
    ]
    count = 0
    for filename, left_candidates, right_candidates in pairs:
        left = get_series(data, left_candidates)
        right = get_series(data, right_candidates)
        if left is None or right is None:
            continue
        if plot_dual_axis(time_s, left[0], left[1], right[0], right[1], output_dir / f"{filename}.png", event_markers):
            count += 1

    total_speed = get_series(data, ["derived/v-total-fps"])
    engine_rpm = get_series(data, ["propulsion/engine/engine-rpm", "propulsion/engine/rpm"])
    propeller_rpm = get_series(data, ["propulsion/engine/propeller-rpm"])
    if total_speed is not None and engine_rpm is not None and propeller_rpm is not None:
        if plot_dual_axis_multi_right(
            time_s,
            total_speed[0],
            total_speed[1],
            [engine_rpm, propeller_rpm],
            output_dir / "total_speed_vs_engine_propeller_rpm.png",
            event_markers,
            right_axis_label="RPM",
        ):
            count += 1
    return count


def write_event_index(event_markers: list[tuple[float, str]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as dst:
        writer = csv.writer(dst)
        writer.writerow(["label", "time_s"])
        for time_s, label in event_markers:
            writer.writerow([label, f"{time_s:.9g}"])


def build_detailed_ploting_outputs(aircraft: str, run_id: str, raw_path: Path, si_path: Path, sixdof_path: Path, sixdof_si_path: Path, console_path: Path, si_rows: list[dict[str, float]], *, show: bool) -> tuple[Path, dict[str, int]]:
    event_markers = parse_event_markers(console_path)
    base_dir = PLOTING_DIR / aircraft / run_id
    counts: dict[str, int] = {}
    write_event_index(event_markers, base_dir / "events.csv")
    counts["raw_time_series"], counts["raw_converted_units"] = plot_csv_time_series(raw_path, base_dir / "raw_time_series", event_markers, converted_dir=base_dir / "raw_converted_units")
    counts["si_time_series"], _ = plot_csv_time_series(si_path, base_dir / "si_time_series", event_markers)
    counts["sixdof_raw_time_series"], counts["sixdof_raw_converted_units"] = plot_csv_time_series(sixdof_path, base_dir / "sixdof_raw_time_series", event_markers, converted_dir=base_dir / "sixdof_raw_converted_units")
    counts["sixdof_si_time_series"], _ = plot_csv_time_series(sixdof_si_path, base_dir / "sixdof_si_time_series", event_markers)
    counts["sixdof_dual_axis"] = plot_sixdof_dual_axis(sixdof_path, raw_path, base_dir / "sixdof_dual_axis", event_markers)
    trajectory_dir = base_dir / "trajectory_3d"
    trajectory_dir.mkdir(parents=True, exist_ok=True)
    plot_trajectory(aircraft, si_rows, trajectory_dir / "trajectory_3d.png", show=show)
    counts["trajectory_3d"] = 1
    trajectory_xy_dir = base_dir / "trajectory_xy"
    trajectory_xy_dir.mkdir(parents=True, exist_ok=True)
    plot_trajectory_xy(aircraft, si_rows, trajectory_xy_dir / "trajectory_xy.png", show=show)
    counts["trajectory_xy"] = 1
    return base_dir, counts


def main() -> None:
    args = parse_args()
    aircraft, init_path, template_path, planet_path = resolve_selection(args)
    flightgear = choose_flightgear_stream(args.flightgear)
    flightgear_logdirective = args.flightgear_logdirective.expanduser().resolve()
    if flightgear and not flightgear_logdirective.exists():
        raise RuntimeError(f"FlightGear logdirective not found: {flightgear_logdirective}")
    stamp = datetime.now().strftime("%m%d%H%M")
    scenario = scenario_name(aircraft, template_path)
    run_id = next_run_id(aircraft, scenario)

    raw_dir = RAW_CSV_DIR / aircraft / scenario
    si_dir = SI_CSV_DIR / aircraft / scenario
    sixdof_dir = SIXDOF_CSV_DIR / aircraft / scenario
    sixdof_si_dir = SIXDOF_SI_CSV_DIR / aircraft / scenario
    console_dir = CONSOLE_DIR / aircraft / scenario
    plot_dir = PLOTS_DIR / aircraft / scenario

    raw_dir.mkdir(parents=True, exist_ok=True)
    si_dir.mkdir(parents=True, exist_ok=True)
    sixdof_dir.mkdir(parents=True, exist_ok=True)
    sixdof_si_dir.mkdir(parents=True, exist_ok=True)
    console_dir.mkdir(parents=True, exist_ok=True)
    plot_dir.mkdir(parents=True, exist_ok=True)

    raw_path = raw_dir / f"{run_id}_raw_{stamp}.csv"
    si_path = si_dir / f"{run_id}_si_{stamp}.csv"
    sixdof_path = sixdof_dir / f"{run_id}_sixdof_raw_{stamp}.csv"
    sixdof_si_path = sixdof_si_dir / f"{run_id}_sixdof_si_{stamp}.csv"
    console_path = console_dir / f"{run_id}_console_{stamp}.log"
    states_plot_path = plot_dir / f"{run_id}_states_vs_time_{stamp}.png"
    trajectory_plot_path = plot_dir / f"{run_id}_trajectory_3d_{stamp}.png"
    trajectory_xy_plot_path = plot_dir / f'{run_id}_trajectory_xy_{stamp}.png'
    generated_runscript, skipped_sixdof_properties = build_runscript(
        aircraft, init_path, template_path, planet_path, raw_path, sixdof_path, stamp, scenario, run_id
    )

    run_jsbsim(
        planet_path,
        generated_runscript,
        console_path,
        realtime=flightgear,
        logdirective_path=flightgear_logdirective if flightgear else None,
    )
    rows = convert_raw_to_si(raw_path, si_path)
    convert_sixdof_raw_to_si(sixdof_path, sixdof_si_path)
    plot_states_vs_time(aircraft, rows, states_plot_path, show=args.show)
    plot_trajectory(aircraft, rows, trajectory_plot_path, show=args.show)
    plot_trajectory_xy(aircraft, rows, trajectory_xy_plot_path, show=args.show)
    detailed_plot_dir, detailed_plot_counts = build_detailed_ploting_outputs(
        aircraft,
        run_id,
        raw_path,
        si_path,
        sixdof_path,
        sixdof_si_path,
        console_path,
        rows,
        show=args.show,
    )
    update_workflow_excel()

    print(f"Timestamp: {stamp}")
    print(f"Aircraft: {aircraft}")
    print(f"Scenario: {scenario}")
    print(f"Run ID: {run_id}")
    print(f"FlightGear stream: {'enabled' if flightgear else 'disabled'}")
    if flightgear:
        print(f"FlightGear logdirective: {flightgear_logdirective}")
    print(f"Init XML: {init_path}")
    print(f"Template runscript: {template_path}")
    print(f"Generated runscript: {generated_runscript}")
    print(f"Console: {console_path}")
    print(f"Raw CSV: {raw_path}")
    print(f"SI CSV: {si_path}")
    print(f"6DOF raw CSV: {sixdof_path}")
    print(f"6DOF SI CSV: {sixdof_si_path}")
    if skipped_sixdof_properties:
        print("Skipped 6DOF properties not found in aircraft catalog:")
        for prop in skipped_sixdof_properties:
            print(f"  {prop}")
    print(f"States plot: {states_plot_path}")
    print(f"Trajectory plot: {trajectory_plot_path}")
    print(f'XY trajectory plot: {trajectory_xy_plot_path}')
    print(f"Detailed ploting dir: {detailed_plot_dir}")
    print("Detailed plot counts:")
    for label, count in sorted(detailed_plot_counts.items()):
        print(f"  {label}: {count}")
    print(f"Workflow Excel: {WORKFLOW_EXCEL}")


if __name__ == "__main__":
    main()
