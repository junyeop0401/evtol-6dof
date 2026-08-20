# FlightControl.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `aircraft/MiniTalon/FlightControl.xml`

이 파일은 normalized command를 조종면 radian 위치로 변환하고 V-tail mixer를 만든다. 모든 servo limit/rate/mixer sign은 논문에 직접 공개되지 않은 seed다.

### 9.1 공통 command 구조

| 구조 | 의미 | 현재 값/동작 | 근거 |
|---|---|---|---|
| `*-cmd-norm` | 사용자/스크립트가 주는 normalized command | 보통 `-1..+1` | JSBSim/FCS 관례 |
| trim summer | command와 trim command 합산 | `cmd + trim`, `clip -1..+1` | 제어 편의 seed |
| `aerosurface_scale` | normalized command를 degree 범위로 변환 | `-25..+25 deg`, gain `pi/180` | `ASSUMPTION-SEED` |
| actuator lag | 1차 지연 | `20.0` | servo 동특성 seed |
| actuator rate_limit | rate 제한 | `2.50 rad/s` | servo 동특성 seed |
| actuator clip | 최종 조종면 제한 | `±0.436332 rad` = `±25 deg` | `ASSUMPTION-SEED` |

### 9.2 Roll channel

| component | 주요 값 | 의미 | 근거 |
|---|---|---|---|
| `fcs/roll-trim-sum` | inputs `aileron-cmd-norm`, `roll-trim-cmd-norm`; clip `[-1,1]` | roll command와 trim 합산 | 제어 편의 seed |
| `fcs/aileron-command-rad` | range `[-25,25]`, gain `0.0174532925199433` | deg command를 rad로 변환 | `25 deg` seed |
| `fcs/aileron-actuator` | lag `20`, rate `2.50`, clip `±0.436332` | servo 동특성 | `ASSUMPTION-SEED` |
| `left-aileron-position` | gain `+1.0` | 왼쪽 aileron 부호 | mixer/sign seed |
| `right-aileron-position` | gain `-1.0` | 오른쪽 aileron 반대 부호 | mixer/sign seed |

### 9.3 Pitch channel

| component | 주요 값 | 의미 | 근거 |
|---|---|---|---|
| `fcs/pitch-trim-sum` | inputs `elevator-cmd-norm`, `pitch-trim-cmd-norm`; clip `[-1,1]` | pitch command와 trim 합산 | seed |
| `fcs/elevator-command-rad` | range `[-25,25]`, gain `pi/180` | normalized elevator command를 rad로 변환 | `ASSUMPTION-SEED` |
| `fcs/elevator-actuator` | lag `20`, rate `2.50`, clip `±0.436332` | elevator servo 동특성 | `ASSUMPTION-SEED` |

### 9.4 Yaw channel

| component | 주요 값 | 의미 | 근거 |
|---|---|---|---|
| `fcs/yaw-trim-sum` | inputs `rudder-cmd-norm`, `yaw-trim-cmd-norm`; clip `[-1,1]` | yaw command와 trim 합산 | seed |
| `fcs/rudder-command-rad` | range `[-25,25]`, gain `pi/180` | normalized rudder command를 rad로 변환 | `ASSUMPTION-SEED` |
| `fcs/rudder-actuator` | lag `20`, rate `2.50`, clip `±0.436332` | rudder/V-tail yaw servo 동특성 | `ASSUMPTION-SEED` |

### 9.5 V-tail physical mixer

| component | 수식 | 의미 | 근거 |
|---|---|---|---|
| `left-ruddervator-mix` | `left = elevator + rudder` | 좌측 ruddervator 물리 deflection | nominal V-tail mixer seed |
| `right-ruddervator-mix` | `right = elevator - rudder` | 우측 ruddervator 물리 deflection | nominal V-tail mixer seed |
| clip | `±0.436332 rad` | ruddervator 최대변위 | `±25 deg` seed |

주의: 실제 RC transmitter/servo linkage에서 positive elevator/rudder가 어느 방향인지 반드시 실기체에서 확인해야 한다.
