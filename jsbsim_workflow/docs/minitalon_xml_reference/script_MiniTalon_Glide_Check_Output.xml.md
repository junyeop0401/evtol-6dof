# scripts/MiniTalon_Glide_Check_Output.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

`MiniTalon_Glide_Check.xml`와 같은 조건이지만 CSV output을 추가한다.

| output | 값 | 의미 |
|---|---|---|
| output file | `MiniTalon_Glide_Check_Output.csv` | 결과 CSV |
| rate | `50 Hz` | 후처리용 logging rate |
| 주요 property | `vtrue`, `alpha`, `beta`, attitude, `h-agl`, body rates, FCS command/position, RPM/current/power/thrust, aero forces/moments | smoke test와 propulsion 활성 확인 |
