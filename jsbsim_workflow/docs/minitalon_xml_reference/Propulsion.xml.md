# Propulsion.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `aircraft/MiniTalon/Propulsion.xml`

이 파일은 motor model과 propeller model을 연결하고, propeller/thruster의 구조 위치와 방향을 정의한다.

| XML 값 | 현재 값 | 의미 | 근거 | 신뢰도 |
|---|---|---|---|---|
| `<engine file=Cobra_C2820_14>` | `Cobra_C2820_14` | Cobra C-2820/14 840 Kv motor XML 로드 | Bacchini propulsion selection / manufacturer data | `PAPER-DIRECT / MANUFACTURER` |
| `<thruster file=APC_10x8E>` | `APC_10x8E` | APC 10x8E propeller XML 로드 | Bacchini selection / APC data | `PAPER-DIRECT / MANUFACTURER` |
| thruster location | `(0.920, 0.000, -0.030) m` | nose tip 기준 pusher prop/motor 위치 seed | ArduPilot Gazebo `motor_link pose=-0.41 0 -0.03`을 JSBSim structural axes로 변환 후 `+0.510 m` shift | `SUPPLEMENTARY-SEED / DATUM-SHIFTED` |
| orient roll/pitch/yaw | `(0.0, 0.0, 0.0) deg` | 추력축이 기본 body/structural 방향과 정렬됐다고 가정 | 실제 thrust line 미측정 | `ASSUMPTION-SEED` |
| `<sense>` | `-1` | propeller 회전방향 | rear view 기준 counter-clockwise 주석, 실제 장착 미확인 | `ASSUMPTION-SEED` |
| `<p_factor>` | `0.05` | propeller P-factor 효과 seed | 실측/식별 없음 | `ASSUMPTION-SEED` |

주의:

- motor/prop 모델명은 논문/제조사 기반이지만, 위치/방향/회전방향은 실제 장착 검증 전까지 seed다.
- 실제 motor hub 중심은 STEP/CAD 또는 실기체 측정으로 교체해야 한다.
- battery voltage sag, ESC dynamics, thermal limit, battery depletion은 현재 모델에 없다.
