# Aero_SourceOnly.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `aircraft/MiniTalon/Aero_SourceOnly.xml`

이 파일은 active model에서 로드되지 않는다. 논문 기반 longitudinal force만 떼어 두어 seed 항목과 섞이지 않게 검토하기 위한 audit module이다.

| 항목 | 값 | 의미 | 근거 |
|---|---|---|---|
| `alphalimits` | `-0.174532925` to `0.174532925 rad` | source-supported `-10..+10 deg` | 논문 그래프 범위 |
| `aero/source-only/Lift_alpha` | `Aero.xml`의 CL table과 동일 | 논문 기반 lift만 검토 | `PAPER-DIGITIZED` |
| `aero/source-only/Drag_alpha` | `Aero.xml`의 CD table과 동일 | 논문 기반 drag만 검토 | `PAPER-DIGITIZED` |

이 파일에는 pitch/side/roll/yaw/control/damping seed가 없다.
