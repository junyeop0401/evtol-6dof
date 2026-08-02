from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path("/home/junyeopkwon/jsbsim_workflow")
SCRIPTS = ROOT / "scripts"

KNOWN_AIRCRAFT = [
    "ball_validated",
    "ball",
    "c172p",
    "c172x",
    "F450",
    "737",
]

ARTIFACT_ROOTS = [
    (ROOT / "logs" / "csv" / "raw", "raw", ".csv"),
    (ROOT / "logs" / "csv" / "si", "si", ".csv"),
    (ROOT / "logs" / "console", "console", ".log"),
    (ROOT / "logs" / "generated_runscripts", "runscript", ".xml"),
    (ROOT / "plots", "plot", ".png"),
]


@dataclass(frozen=True)
class OutputFile:
    path: Path
    root: Path
    root_kind: str
    aircraft: str
    scenario: str
    label: str
    artifact: str
    stamp: str


def version_map() -> dict[tuple[str, str], str]:
    mapping: dict[tuple[str, str], str] = {}
    for path in SCRIPTS.rglob("*.xml"):
        rel = path.relative_to(SCRIPTS)
        if len(rel.parts) < 3:
            continue
        aircraft = rel.parts[0]
        stem = path.stem
        if "__" not in stem:
            continue
        version, label = stem.split("__", 1)
        for suffix in ["_run", "_init"]:
            if label.endswith(suffix):
                label = label[: -len(suffix)]
        mapping[(aircraft, label)] = version
    return mapping


def split_aircraft(stem: str) -> tuple[str, str] | None:
    for aircraft in sorted(KNOWN_AIRCRAFT, key=len, reverse=True):
        prefix = f"{aircraft}_"
        if stem == aircraft:
            return aircraft, ""
        if stem.startswith(prefix):
            return aircraft, stem[len(prefix):]
    return None


def strip_stamp(text: str) -> tuple[str, str]:
    match = re.search(r"_(\d{8,}|\d{8}|\d{6})$", text)
    if not match:
        return text, "nostamp"
    return text[: match.start()], match.group(1)


def parse_output(path: Path, root: Path, root_kind: str, versions: dict[tuple[str, str], str]) -> OutputFile | None:
    if path.parent != root:
        return None
    if path.suffix in {".m", ".Identifier"} or path.name.startswith("."):
        return None

    stem = path.stem
    artifact = root_kind

    if root_kind == "plot":
        for suffix in ["_states_vs_time", "_trajectory_3d"]:
            base, stamp = strip_stamp(stem)
            if base.endswith(suffix):
                artifact = suffix[1:]
                stem = base[: -len(suffix)]
                break
            si_suffix = f"{suffix}_si"
            if base.endswith(si_suffix):
                artifact = suffix[1:]
                stem = base[: -len(si_suffix)]
                break
        else:
            stem, stamp = strip_stamp(stem)
            artifact = "plot"
            if stem in {"validated_vs_builtin_overlay", "validated_vs_builtin_overlay_si"}:
                stem = "ball_validated_500m_drop_comparison"
                artifact = "validated_vs_builtin_overlay"
            elif stem in {"validated_minus_builtin_deltas", "validated_minus_builtin_deltas_si"}:
                stem = "ball_validated_500m_drop_comparison"
                artifact = "validated_minus_builtin_deltas"
    elif root_kind == "runscript":
        stem, stamp = strip_stamp(stem)
        if stem.endswith("_runscript"):
            stem = stem[:-10]
    else:
        stem, stamp = strip_stamp(stem)
        suffix = f"_{root_kind}"
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
        elif root_kind == "console" and stem.endswith("_console"):
            stem = stem[:-8]

    split = split_aircraft(stem)
    if split is None:
        return None
    aircraft, label = split
    if not label:
        label = "default"

    if "__" in label:
        version, clean_label = label.split("__", 1)
        scenario = f"{version}__{clean_label}"
        label = clean_label
    else:
        version = versions.get((aircraft, label), "0.0")
        scenario = f"{version}__{label}"

    return OutputFile(path, root, root_kind, aircraft, scenario, label, artifact, stamp)


def destination(item: OutputFile, patch: int) -> Path:
    version = item.scenario.split("__", 1)[0]
    run_id = f"{version}.{patch}__{item.label}"
    directory = item.root / item.aircraft / item.scenario
    suffix = "" if item.stamp == "nostamp" else f"_{item.stamp}"
    if item.root_kind == "plot":
        filename = f"{run_id}_{item.artifact}{suffix}{item.path.suffix}"
    else:
        filename = f"{run_id}_{item.root_kind}{suffix}{item.path.suffix}"
    return directory / filename


def next_available_destination(item: OutputFile, patch: int) -> Path:
    candidate = destination(item, patch)
    while candidate.exists():
        patch += 1
        candidate = destination(item, patch)
    return candidate


def main() -> None:
    versions = version_map()
    items: list[OutputFile] = []
    for root, root_kind, suffix in ARTIFACT_ROOTS:
        if not root.exists():
            continue
        for path in root.glob(f"*{suffix}"):
            parsed = parse_output(path, root, root_kind, versions)
            if parsed:
                items.append(parsed)

    grouped_stamps: dict[tuple[str, str], list[str]] = defaultdict(list)
    for item in items:
        key = (item.aircraft, item.scenario)
        if item.stamp not in grouped_stamps[key]:
            grouped_stamps[key].append(item.stamp)

    patch_by_stamp: dict[tuple[str, str, str], int] = {}
    for key, stamps in grouped_stamps.items():
        for index, stamp in enumerate(sorted(stamps), start=1):
            patch_by_stamp[(key[0], key[1], stamp)] = index

    moved = 0
    for item in sorted(items, key=lambda item: str(item.path)):
        patch = patch_by_stamp[(item.aircraft, item.scenario, item.stamp)]
        dst = next_available_destination(item, patch)
        dst.parent.mkdir(parents=True, exist_ok=True)
        item.path.rename(dst)
        moved += 1

    renamed = normalize_nested_outputs()
    print(f"Moved {moved} output files into aircraft/scenario folders.")
    print(f"Renumbered {renamed} nested output files.")


def nested_output_files() -> list[Path]:
    paths: list[Path] = []
    for root, _, suffix in ARTIFACT_ROOTS:
        if not root.exists():
            continue
        paths.extend(path for path in root.glob(f"*/*/*{suffix}") if path.is_file())
    return paths


def normalize_nested_outputs() -> int:
    paths = nested_output_files()
    stamps_by_scenario: dict[tuple[Path, str, str], set[str]] = defaultdict(set)
    for path in paths:
        root = path.parents[2]
        aircraft = path.parents[1].name
        scenario = path.parent.name
        _, stamp = strip_stamp(path.stem)
        stamps_by_scenario[(root, aircraft, scenario)].add(stamp)

    patch_by_scenario_stamp: dict[tuple[Path, str, str, str], int] = {}
    for (root, aircraft, scenario), stamps in stamps_by_scenario.items():
        for index, stamp in enumerate(sorted(stamps), start=1):
            patch_by_scenario_stamp[(root, aircraft, scenario, stamp)] = index

    renamed = 0
    for path in sorted(paths, key=lambda p: str(p)):
        root = path.parents[2]
        aircraft = path.parents[1].name
        scenario = path.parent.name
        if "__" not in scenario:
            continue
        version, label = scenario.split("__", 1)
        marker = f"__{label}"
        if marker not in path.name:
            continue
        _, stamp = strip_stamp(path.stem)
        patch = patch_by_scenario_stamp[(root, aircraft, scenario, stamp)]
        rest = path.name.split(marker, 1)[1]
        new_name = f"{version}.{patch}{marker}{rest}"
        if new_name == path.name:
            continue
        candidate = path.with_name(new_name)
        if candidate.exists():
            continue
        path.rename(candidate)
        renamed += 1
    return renamed


if __name__ == "__main__":
    main()
