# scripts/MiniTalon_control_sign_test_run.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

상태: legacy control sign test. `initAir.xml`와 throttle `0.40`을 사용한다.

| 값 | 현재 값 | 의미 |
|---|---:|---|
| run time | `0..18 s` | legacy sign test |
| throttle | `0.40` | powered condition sign test |
| aileron steps | `+0.25`, `-0.25` | roll sign 양/음 확인 |
| elevator steps | `+0.20`, `-0.20` | pitch sign 확인 |
| rudder steps | `+0.25`, `-0.25` | yaw sign 확인 |
| output rate | `100 Hz` | legacy detailed logging |
