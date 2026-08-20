# output/MiniTalon_output.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `output/MiniTalon_output.xml`

상태: 별도 output definition. 특정 runscript가 직접 포함하지 않으면 자동 로드되지 않는다.

| 값 | 현재 값 | 의미 |
|---|---:|---|
| output file | `MiniTalon_output.csv` | 기본 CSV output name |
| rate | `50 Hz` | logging rate |
| kinematic properties | time, true speed, alpha, beta, attitude, rates, altitude | 비행 상태 확인 |
| FCS properties | command norm, aileron/ruddervator positions | 제어 입력/출력 확인 |
| propulsion properties | RPM, advance ratio, current, power, thrust, torque | motor/prop 작동 확인 |
| aero force/moment properties | aero forces and moments | 공력 모델 반응 확인 |
