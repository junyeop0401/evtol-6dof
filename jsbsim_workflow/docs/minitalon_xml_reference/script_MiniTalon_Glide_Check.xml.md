# scripts/MiniTalon_Glide_Check.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

| 값 | 현재 값 | 의미 | 근거 |
|---|---:|---|---|
| aircraft/init | `MiniTalon`, `MiniTalon_glide` | geometry-locked glide 시작 | smoke test |
| run time | `0..20 s` | 20초 short run | load/time integration 확인 |
| dt | `0.0083333333 s` | 120 Hz | JSBSim test resolution seed |
| initial controls | all `0.0` | neutral controls/throttle off | smoke test |
| throttle step | `0.35` at `t>=2.0 s` | moderate pusher throttle | propulsion activation 확인 |
