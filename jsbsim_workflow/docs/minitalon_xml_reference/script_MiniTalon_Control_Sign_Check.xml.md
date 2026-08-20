# scripts/MiniTalon_Control_Sign_Check.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

| 값 | 현재 값 | 의미 |
|---|---:|---|
| run time | `0..18 s` | control sign smoke test |
| aileron step | `+0.35` at `2..5 s` | roll moment sign 확인 |
| elevator step | `+0.35` at `7..10 s` | pitch moment sign 확인 |
| rudder step | `+0.35` at `12..15 s` | yaw moment sign 확인 |
| output file/rate | `MiniTalon_Control_Sign_Check.csv`, `50 Hz` | 조종면/모멘트 logging |
