# initAir_quasitrim.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

상태: open-loop quasi-trim script에서 사용.

| XML 값 | 현재 값 | 의미 | 근거 |
|---|---:|---|---|
| `vt` | `34.989 KTS` | 초기 true airspeed | 기존 initAir와 동일 |
| `theta` | `0.800 deg` | 손계산 quasi-trim 근처 pitch attitude | open-loop sweep 결과 seed |
| `altitude` | `250.0 M` | 초기 고도 | quasi-trim test seed |
| `p/q/r` | `0 rad/s` | 초기 각속도 | quasi-steady start seed |
