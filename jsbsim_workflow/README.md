# Ball JSBSim Workflow

This folder keeps the ball comparison workflow separate from the JSBSim source tree.

## Layout

- `scripts/`: JSBSim runscript XML files and workflow helper scripts
- `logs/csv/raw/`: raw JSBSim CSV outputs using JSBSim property units such as `fps` and `slugs`
- `logs/csv/si/`: converted SI CSV outputs and SI comparison summary
- `logs/console/`: JSBSim console logs
- `plots/`: generated PNG plots

## Run

From WSL:

```bash
bash /home/junyeopkwon/jsbsim_workflow/scripts/run_workflow.sh
```

The workflow uses the current contents of:

- `/home/junyeopkwon/ball_validated/ball_validated_ned_500m_init.xml`
- `/home/junyeopkwon/ball_validated/aircraft/ball_validated/ball_validated.xml`
- `/home/junyeopkwon/jsbsim/aircraft/ball/ball.xml`
- `scripts/ball_validated/runscript/1.0__500m_drop_run.xml`
- `scripts/ball/runscript/1.0__builtin_500m_drop_run.xml`

Edit any of those files, run the command again, and the CSV logs, summary, console logs, and plots are regenerated.

Note: the runscript XML files request JSBSim's raw internal output properties, so names like
`velocities/u-fps` and `inertia/mass-slugs` appear there. The workflow converts those raw
outputs into SI CSV files before summary and plotting.
