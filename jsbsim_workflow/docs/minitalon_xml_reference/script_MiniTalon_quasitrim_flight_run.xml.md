# scripts/MiniTalon_quasitrim_flight_run.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

| 값 | 현재 값 | 의미 | 근거 |
|---|---:|---|---|
| initialize | `initAir_quasitrim` | quasi-trim 초기조건 | open-loop trim attempt seed |
| run time | `0..90 s` | 장시간 open-loop 확인 | user-requested quasi-trim task |
| dt | `0.008333 s` | 120 Hz | test seed |
| aileron/elevator/rudder | `0.0 / 0.0000 / 0.0` | neutral controls | sweep 결과 가장 안정 조합 seed |
| throttle | `0.4500` | open-loop throttle | quasi-trim sweep seed |
| output rate | `20 Hz` | 90초 CSV logging | 후처리용 |
