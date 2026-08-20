# Metrics.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `aircraft/MiniTalon/Metrics.xml`

이 파일은 JSBSim이 공력계수와 모멘트 기준 길이를 계산할 때 사용하는 기준 형상값을 담는다.

### 5.1 주익 기준 형상

| XML 값 | 현재 값 | 의미 | 근거 | 신뢰도 |
|---|---:|---|---|---|
| `<wingarea unit="M2">` | `0.314` | 공력 기준 면적 `Sref` | Bacchini dissertation table / 계수 정규화 기준 | `GEOMETRY-LOCKED / PAPER-DIRECT` |
| `<wingspan unit="M">` | `1.280` | 주익 전체 span `b` | 논문값, 실기체 실측 `0.570+0.140+0.570`, CAD 확인 | `GEOMETRY-LOCKED / LAB-MEASURED / CAD-CONFIRMED` |
| `<chord unit="M">` | `0.245` | 기준시위 `c_ref`, MAC 근사 기준 | 논문값, CAD 약 `0.243832 m`, 실측 local chord `0.230-0.240 m` | `GEOMETRY-LOCKED / PAPER-DIRECT / CAD-SUPPORTED` |
| `<wing_incidence unit="DEG">` | `0.0` | 동체 기준 주익 장착각 | 명시 실측 없음 | `ASSUMPTION-SEED` |

`0.314 m2`는 CAD planform을 적분한 실제 면적이라고 확정한 값이 아니다. 현재 논문에서 사용한 공력계수와 일관성을 유지하기 위한 aerodynamic reference area다. `1.280 * 0.245 = 0.3136 m2`이므로 논문 `0.314 m2`와 수치적으로 정합된다.

### 5.2 V-tail 등가 기준값

| XML 값 | 현재 값 | 의미 | 근거 | 신뢰도 |
|---|---:|---|---|---|
| `<htailarea unit="M2">` | `0.03182` | V-tail을 수평꼬리 등가 투영으로 본 면적 | `2 * 0.0225 * cos(45 deg)` 가정 | `SUPPLEMENTARY-SEED` |
| `<htailarm unit="M">` | `0.330` | CG/AERORP 기준 수평꼬리 모멘트 암 seed | public ArduPilot Gazebo geometry | `SUPPLEMENTARY-SEED` |
| `<vtailarea unit="M2">` | `0.03182` | V-tail을 수직꼬리 등가 투영으로 본 면적 | 45도 V-tail projection 가정 | `SUPPLEMENTARY-SEED` |
| `<vtailarm unit="M">` | `0.330` | 수직꼬리 모멘트 암 seed | public ArduPilot Gazebo geometry | `SUPPLEMENTARY-SEED` |

주의: 이 값들은 현재 `Aero.xml`의 seed lateral/directional derivative 구조를 채우기 위한 보조 기준값이다. stock V-tail의 실제 면적, 각도, aerodynamic center를 CAD 또는 실측으로 교체해야 한다.

### 5.3 기준점 위치

| location | 현재 좌표 `(x,y,z) m` | 의미 | 근거 | 신뢰도 |
|---|---:|---|---|---|
| `AERORP` | `(0.510, 0.000, 0.000)` | aerodynamic reference point | 현재 provisional CG와 같은 위치로 둠 | `ASSUMPTION-SEED / DATUM-SHIFTED` |
| `EYEPOINT` | `(0.260, 0.000, 0.080)` | 시점/cockpit view reference | 기존 `(-0.250,0,0.080)`을 nose datum으로 shift | `VISUAL-SEED` |
| `VRP` | `(0.510, 0.000, 0.000)` | visual reference point | 현재 provisional CG와 같은 위치로 둠 | `ASSUMPTION-SEED / DATUM-SHIFTED` |

`AERORP`가 실제 aerodynamic center라는 뜻은 아니다. 현재는 모멘트 기준점을 provisional CG에 맞춰 둔 seed다.
