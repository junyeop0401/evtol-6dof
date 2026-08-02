from __future__ import annotations

import argparse
import csv
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

import run_jsbsim_timestamped_no_fg_prompt_csv_only as base


COMBINED_CSV_DIR = base.ROOT / "logs" / "csv" / "combined"


def unique_preserve_order(items: list[str]) -> list[str]:
    selected: list[str] = []
    seen: set[str] = set()
    for item in items:
        prop = item.strip()
        if not prop or prop in seen:
            continue
        selected.append(prop)
        seen.add(prop)
    return selected


def combined_output_properties(
    aircraft: str,
    template_root: ET.Element,
    available_properties: set[str],
) -> tuple[list[str], list[str]]:
    template_properties, _template_rate = base.template_output_definition(template_root)

    requested: list[str] = []
    requested.extend(base.OUTPUT_PROPERTIES)
    requested.extend(template_properties)

    if aircraft.endswith("_landing"):
        requested.extend(base.LANDING_OUTPUT_PROPERTIES)
    if aircraft == "F450":
        requested.extend(base.F450_OUTPUT_PROPERTIES)

    sixdof_properties, skipped_sixdof = base.unique_existing_properties(
        base.SIXDOF_VALIDATION_PROPERTIES,
        available_properties,
    )
    requested.extend(sixdof_properties)
    return unique_preserve_order(requested), skipped_sixdof


def combined_scenario_dirs(aircraft: str, scenario: str) -> list[Path]:
    return [
        COMBINED_CSV_DIR / aircraft / scenario,
        base.CONSOLE_DIR / aircraft / scenario,
        base.GENERATED_DIR / aircraft / scenario,
    ]


def next_combined_run_id(aircraft: str, scenario: str) -> str:
    version, label = base.split_versioned_scenario(scenario)
    max_patch = 0
    prefix = f"{version}."
    marker = f"__{label}"
    for directory in combined_scenario_dirs(aircraft, scenario):
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


def build_combined_runscript(
    aircraft: str,
    init_path: Path,
    template_path: Path,
    planet_path: Path | None,
    combined_path: Path,
    stamp: str,
    scenario: str,
    run_id: str,
) -> tuple[Path, list[str], int]:
    tree = ET.parse(template_path)
    root = tree.getroot()
    root.set("name", f"{aircraft}_combined_selected_{stamp}")

    available_properties = base.aircraft_catalog_properties(aircraft)
    output_properties, skipped_sixdof_properties = combined_output_properties(
        aircraft,
        root,
        available_properties,
    )

    use = root.find("use")
    if use is None:
        use = ET.Element("use")
        root.insert(0, use)
    use.set("aircraft", aircraft)
    use.set("initialize", str(init_path))

    if planet_path is not None:
        base.ensure_gravity_model(root, base.gravity_model_for_planet(planet_path))

    for old_output in list(root.findall("output")):
        root.remove(old_output)

    output_name = "../jsbsim_workflow/" + combined_path.relative_to(base.ROOT).as_posix()
    output = ET.SubElement(root, "output", {"name": output_name, "type": "CSV", "rate": "120"})
    for prop in output_properties:
        prop_element = ET.SubElement(output, "property")
        prop_element.text = f" {prop} "

    generated_path = base.GENERATED_DIR / aircraft / scenario / f"{run_id}_combined_runscript_{stamp}.xml"
    generated_path.parent.mkdir(parents=True, exist_ok=True)
    base.indent_xml(root)
    ET.ElementTree(root).write(generated_path, encoding="UTF-8", xml_declaration=True)
    return generated_path, skipped_sixdof_properties, len(output_properties)


def run_jsbsim(
    planet_path: Path | None,
    runscript_path: Path,
    console_path: Path,
    *,
    realtime: bool = False,
    logdirective_path: Path | None = None,
) -> None:
    cmd = [
        str(base.JSBSIM_DIR / "build" / "src" / "JSBSim"),
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
        subprocess.run(cmd, cwd=base.JSBSIM_DIR, stdout=console, stderr=subprocess.STDOUT, check=True)


def csv_shape(path: Path) -> tuple[int, int, str]:
    with path.open(newline="", encoding="utf-8") as src:
        reader = csv.reader(src)
        header = next(reader, [])
        rows = list(reader)
    last_time = rows[-1][0] if rows and rows[-1] else ""
    return len(header), len(rows), last_time


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run JSBSim and write one combined CSV output. Plotting and split SI CSV generation are disabled.",
    )
    parser.add_argument("--aircraft", help="Aircraft name under /home/junyeopkwon/jsbsim/aircraft")
    parser.add_argument("--init", type=Path, help="Initialize XML path")
    parser.add_argument("--runscript", type=Path, help="Runscript template XML path")
    parser.add_argument(
        "--planet",
        default=None,
        help="Planet XML path, or 'builtin' to use JSBSim's default Earth model",
    )
    fg_group = parser.add_mutually_exclusive_group()
    fg_group.add_argument("--flightgear", action="store_true", dest="flightgear", help="Run JSBSim in real time and stream FlightGear native-fdm output")
    fg_group.add_argument("--no-flightgear", action="store_false", dest="flightgear", help="Disable FlightGear native-fdm streaming")
    parser.add_argument(
        "--flightgear-logdirective",
        type=Path,
        default=base.DEFAULT_FLIGHTGEAR_LOGDIRECTIVE,
        help="JSBSim output directive XML for FlightGear streaming",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    aircraft, init_path, template_path, planet_path = base.resolve_selection(args)
    flightgear = bool(args.flightgear)
    flightgear_logdirective = args.flightgear_logdirective.expanduser().resolve()
    if flightgear and not flightgear_logdirective.exists():
        raise RuntimeError(f"FlightGear logdirective not found: {flightgear_logdirective}")

    stamp = datetime.now().strftime("%m%d%H%M")
    scenario = base.scenario_name(aircraft, template_path)
    run_id = next_combined_run_id(aircraft, scenario)

    combined_dir = COMBINED_CSV_DIR / aircraft / scenario
    console_dir = base.CONSOLE_DIR / aircraft / scenario
    combined_dir.mkdir(parents=True, exist_ok=True)
    console_dir.mkdir(parents=True, exist_ok=True)

    combined_path = combined_dir / f"{run_id}_combined_{stamp}.csv"
    console_path = console_dir / f"{run_id}_combined_console_{stamp}.log"

    generated_runscript, skipped_sixdof_properties, property_count = build_combined_runscript(
        aircraft,
        init_path,
        template_path,
        planet_path,
        combined_path,
        stamp,
        scenario,
        run_id,
    )

    run_jsbsim(
        planet_path,
        generated_runscript,
        console_path,
        realtime=flightgear,
        logdirective_path=flightgear_logdirective if flightgear else None,
    )

    columns, rows, last_time = csv_shape(combined_path)

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
    print(f"Combined CSV: {combined_path}")
    print(f"Combined requested properties: {property_count}")
    print(f"Combined CSV columns: {columns}")
    print(f"Combined CSV rows: {rows}")
    print(f"Combined CSV last time: {last_time}")
    if skipped_sixdof_properties:
        print("Skipped 6DOF properties not found in aircraft catalog:")
        for prop in skipped_sixdof_properties:
            print(f"  {prop}")
    print("Raw/SI/sixdof split CSV generation: disabled")
    print("Plotting: disabled")
    print(f"Workflow Excel: {base.WORKFLOW_EXCEL}")


if __name__ == "__main__":
    main()
