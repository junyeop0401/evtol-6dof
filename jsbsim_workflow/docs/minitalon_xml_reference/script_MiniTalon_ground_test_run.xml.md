# scripts/MiniTalon_ground_test_run.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

| 값 | 현재 값 | 의미 |
|---|---:|---|
| initialize | `initGround` | ground contact test |
| run time | `0..10 s` | ground reaction 확인 |
| throttle | `0.0`, then `0.10` at `t>=5 s` | 저추력 지상 거동 확인 |
| output file/rate | `MiniTalon_ground_test.csv`, `50 Hz` | h-agl, attitude, speed, thrust logging |
