# Gear.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `aircraft/MiniTalon/Gear.xml`

이 파일은 landing gear가 아니라 belly/skid/wingtip ground contact를 수치적으로 정의한다. Mini Talon은 hand launch / belly landing을 가정하므로 구조 접촉점으로 모델링되어 있다.

| contact | 위치 `(x,y,z) m` | 의미 | 근거 | 신뢰도 |
|---|---:|---|---|---|
| `NOSE_SKID` | `(0.210, 0.000, -0.100)` | nose 쪽 하부 skid 접촉 seed | 기존 `x=-0.300`을 nose datum으로 `+0.510 m` shift | `ASSUMPTION-SEED` |
| `BELLY_SKID` | `(0.560, 0.000, -0.110)` | 동체 배면 주 접촉점 seed | 기존 `x=0.050` shift | `ASSUMPTION-SEED` |
| `TAIL_SKID` | `(0.910, 0.000, -0.060)` | tail 하부 접촉점 seed | 기존 `x=0.400` shift | `ASSUMPTION-SEED` |
| `LEFT_WINGTIP` | `(0.510, -0.630, -0.020)` | 좌측 wingtip 접촉점 seed | span `1.280 m`의 half-span 근사 | `ASSUMPTION-SEED` |
| `RIGHT_WINGTIP` | `(0.510, 0.630, -0.020)` | 우측 wingtip 접촉점 seed | span `1.280 m`의 half-span 근사 | `ASSUMPTION-SEED` |

각 contact의 반력/마찰 파라미터:

| contact | static friction | dynamic friction | spring `LBS/FT` | damping `LBS/FT/SEC` | 의미/근거 |
|---|---:|---:|---:|---:|---|
| `NOSE_SKID` | `0.60` | `0.45` | `2000` | `100` | ground test 수치 안정용 seed |
| `BELLY_SKID` | `0.65` | `0.50` | `2500` | `120` | belly contact를 조금 더 강하게 둔 seed |
| `TAIL_SKID` | `0.55` | `0.40` | `1200` | `80` | tail 접촉 seed |
| `LEFT_WINGTIP` | `0.50` | `0.40` | `800` | `60` | wingtip scrape 방지/검사용 seed |
| `RIGHT_WINGTIP` | `0.50` | `0.40` | `800` | `60` | 동일 |

이 값들은 crash/landing load 검증용이 아니다. 실제 ground contact 위치와 foam deformation/stiffness 측정값이 필요하다.
