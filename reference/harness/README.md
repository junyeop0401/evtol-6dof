# JSBSim Workflow Scripts

XML scripts are grouped by aircraft:

```text
scripts/
  aircraft_name/
    initial_condition/
      major.minor__scenario_init.xml
    runscript/
      major.minor__scenario_run.xml
```

Version convention:

- `1.0`: main baseline for a mission family
- `1.1`, `1.2`: small variants of the same mission family
- `2.0`: first baseline of a different mission family

`run_jsbsim_timestamped.py` discovers XML files recursively. Without explicit `--init` and `--runscript`, selection proceeds as:

```text
aircraft -> initial condition -> runscript
```

New timestamped outputs are grouped with the same aircraft and scenario version:

```text
logs/csv/raw/aircraft_name/major.minor__scenario/major.minor.patch__scenario_raw_timestamp.csv
logs/csv/si/aircraft_name/major.minor__scenario/major.minor.patch__scenario_si_timestamp.csv
logs/console/aircraft_name/major.minor__scenario/major.minor.patch__scenario_console_timestamp.log
logs/generated_runscripts/aircraft_name/major.minor__scenario/major.minor.patch__scenario_runscript_timestamp.xml
plots/aircraft_name/major.minor__scenario/major.minor.patch__scenario_states_vs_time_timestamp.png
plots/aircraft_name/major.minor__scenario/major.minor.patch__scenario_trajectory_3d_timestamp.png
```

The third version number is the repeat count for the same script family. For example, repeated `2.1__cruise_4k_trimmed_engineout_apoff` runs become `2.1.1`, `2.1.2`, and so on.

The legacy `nonrotating_earth.xml` remains at the `scripts/` root, but aircraft-specific XML should live under an aircraft folder.

## Live 3D trajectory animation - deprecated

`--live-3d` was previously available as a Matplotlib-based live trajectory viewer.
It is no longer exposed from `run_jsbsim_timestamped.py` because FlightGear is now the preferred visualization path.
The helper file `scripts/live_trajectory_3d.py` is intentionally kept in the repository as a reference/backup utility, but the normal runner no longer calls it.

## Optional FlightGear visualization stream

`run_jsbsim_timestamped.py` can optionally stream JSBSim native-fdm output to FlightGear.

Start FlightGear first from Windows PowerShell:

```powershell
& "C:\Program Files\FlightGear 2024.1\bin\fgfs.exe" --aircraft=c172p --fdm=external "--native-fdm=socket,in,60,,5500,udp"
```

Then run JSBSim with FlightGear streaming enabled:

```bash
python3 scripts/run_jsbsim_timestamped.py \
  --aircraft c172x_4x75kg_cg_aligned \
  --init scripts/c172x/initial_condition/2.2__rkss_14l_default_earth_init.xml \
  --runscript scripts/c172x/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml \
  --planet default \
  --flightgear
```

Interactive runs ask whether to enable FlightGear after the aircraft, init, and runscript selections. Non-interactive runs default to FlightGear disabled unless `--flightgear` is explicitly provided. The default output directive is `scripts/c172x/output/fg_visual_5500.xml`, which currently targets UDP `172.29.80.1:5500`.
