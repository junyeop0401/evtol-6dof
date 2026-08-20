# scripts/MiniTalon_smoke_test_run.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

| 값 | 현재 값 | 의미 |
|---|---:|---|
| initialize | `initAir` | airborne bootstrap |
| run time | `0..20 s` | smoke test |
| throttle | `0.45` from start | propulsion active test |
| output file/rate | `MiniTalon_smoke_test.csv`, `50 Hz` | 속도/자세/RPM/current/thrust 확인 |
