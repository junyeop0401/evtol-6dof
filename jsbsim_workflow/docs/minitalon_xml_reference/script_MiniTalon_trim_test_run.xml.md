# scripts/MiniTalon_trim_test_run.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

| 값 | 현재 값 | 의미 | 현재 판단 |
|---|---:|---|---|
| initialize | `initAir` | trim test 초기조건 | legacy |
| throttle | `0.40` | trim 중 throttle seed | legacy |
| `simulation/do_simple_trim` | `0` | 현재는 simple trim trigger가 꺼진 상태 | 과거 trim 실패 이후 비활성화 |
| output file/rate | `MiniTalon_trim_test.csv`, `20 Hz` | trim 변수 logging | 참고용 |
