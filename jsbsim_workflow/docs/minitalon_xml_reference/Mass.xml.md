# Mass.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `aircraft/MiniTalon/Mass.xml`

이 파일은 전체 질량, CG, 관성텐서를 정의한다.

| XML 값 | 현재 값 | 의미 | 근거 | 신뢰도 |
|---|---:|---|---|---|
| `<emptywt unit="KG">` | `1.875` | JSBSim empty/base weight로 들어가는 all-up seed mass | public ArduPilot Gazebo Mini Talon aggregate | `SUPPLEMENTARY-SEED` |
| `<ixx unit="KG*M2">` | `0.02794484` | roll axis inertia | Gazebo aggregate reconstruction | `SUPPLEMENTARY-SEED` |
| `<iyy unit="KG*M2">` | `0.09438062` | pitch axis inertia | Gazebo aggregate reconstruction | `SUPPLEMENTARY-SEED` |
| `<izz unit="KG*M2">` | `0.11469593` | yaw axis inertia | Gazebo aggregate reconstruction | `SUPPLEMENTARY-SEED` |
| `<ixy unit="KG*M2">` | `0.0` | product of inertia | frame/sign 및 실제 장비 배치 미검증이라 0 처리 | `ASSUMPTION-SEED` |
| `<ixz unit="KG*M2">` | `0.0` | product of inertia | 동일 | `ASSUMPTION-SEED` |
| `<iyz unit="KG*M2">` | `0.0` | product of inertia | 동일 | `ASSUMPTION-SEED` |
| `CG` | `(0.510, 0.000, 0.000) m` | nose tip 기준 provisional CG | 기존 base-link/provisional CG 원점을 nose datum으로 `+0.510 m` shift | `ASSUMPTION-SEED / DATUM-SHIFTED` |

주의:

- `emptywt=1.875 kg`는 bare airframe empty mass가 아니라 all-up seed mass로 취급해야 한다.
- 실제 배터리, avionics, motor, servo 장착 위치가 반영된 CG/관성이 아니다.
- 고정밀 trajectory prediction이나 crash dynamics에는 CAD mass property 또는 pendulum 실측으로 교체해야 한다.
