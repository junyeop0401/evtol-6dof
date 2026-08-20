# initAir.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

상태: legacy airborne bootstrap scripts에서 사용.

| XML 값 | 현재 값 | 의미 | 근거 |
|---|---:|---|---|
| `vt` | `34.989 KTS` | 약 `18.0 m/s` 초기 true airspeed | 과거 smoke/quasi-trim seed |
| `theta` | `2.0 deg` | 초기 pitch attitude | quasi-trim 전 seed |
| `altitude` | `250.0 M` | 초기 고도 | 프로젝트에서 AGL로 해석되는 조건으로 사용한 seed |
| `p/q/r` | `0 rad/s` | 초기 각속도 | steady start seed |
