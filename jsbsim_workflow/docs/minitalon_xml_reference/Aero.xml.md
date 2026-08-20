# Aero.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `aircraft/MiniTalon/Aero.xml`

이 파일은 JSBSim 6DOF force/moment를 채우는 핵심 공력 모델이다. 단, 고정밀 최종 공력 모델이 아니라 `PAPER-CORE`와 `ASSUMPTION-SEED`가 섞인 bootstrap 모델이다.

### 10.1 alpha limits

| XML 값 | 현재 값 | 의미 | 근거 |
|---|---:|---|---|
| `<alphalimits min>` | `-0.174532925 rad` = `-10 deg` | source-supported alpha 하한 | 논문 wind-tunnel curve 지원 범위 |
| `<alphalimits max>` | `0.174532925 rad` = `+10 deg` | source-supported alpha 상한 | 논문 wind-tunnel curve 지원 범위 |

이 범위 밖에서 JSBSim table은 clamp된다. 따라서 post-stall, spin, tumble, crash aerodynamics가 아니다.

### 10.2 Lift axis

#### `aero/force/Lift_alpha_paper`

의미: clean Mini Talon 1의 `CL(alpha)`를 `qbar * Sref`와 곱해 lift force를 만든다.  
근거: Bacchini dissertation clean Mini Talon 1 wind-tunnel curve 수동 digitizing.  
신뢰도: `PAPER-DIGITIZED`, 단 absolute CL은 논문에서 언급된 load-cell/fixture offset 이슈가 남아 있다.

| alpha rad | alpha deg | CL |
|---:|---:|---:|
| `-0.174532925` | `-10` | `-0.25000` |
| `-0.157079633` | `-9` | `-0.20000` |
| `-0.139626340` | `-8` | `-0.14000` |
| `-0.122173048` | `-7` | `-0.08000` |
| `-0.104719755` | `-6` | `-0.02000` |
| `-0.087266463` | `-5` | `0.06000` |
| `-0.069813170` | `-4` | `0.14000` |
| `-0.052359878` | `-3` | `0.22000` |
| `-0.034906585` | `-2` | `0.31000` |
| `-0.017453293` | `-1` | `0.40000` |
| `0.000000000` | `0` | `0.48000` |
| `0.017453293` | `1` | `0.56000` |
| `0.034906585` | `2` | `0.65000` |
| `0.052359878` | `3` | `0.73000` |
| `0.069813170` | `4` | `0.81000` |
| `0.087266463` | `5` | `0.87000` |
| `0.104719755` | `6` | `0.90000` |
| `0.122173048` | `7` | `0.92000` |
| `0.139626340` | `8` | `0.90000` |
| `0.157079633` | `9` | `0.87000` |
| `0.174532925` | `10` | `0.85000` |

#### Seed lift terms

| function | 수식 구조 | 계수 | 의미 | 근거 |
|---|---|---:|---|---|
| `Lift_pitch_rate_seed` | `qbar*S*q*aero/ci2vel*value` | `3.50` | pitch rate에 따른 lift 변화 seed | `ASSUMPTION-SEED` |
| `Lift_elevator_seed` | `qbar*S*elevator_pos*value` | `0.25` | elevator/ruddervator 대칭 조작 lift 변화 seed | `ASSUMPTION-SEED` |

### 10.3 Drag axis

#### `aero/force/Drag_alpha_paper`

의미: clean Mini Talon 1의 `CD(alpha)`를 `qbar * Sref`와 곱해 drag force를 만든다.  
근거: Bacchini dissertation clean Mini Talon 1 drag curve 수동 digitizing.  
신뢰도: `PAPER-DIGITIZED`.

| alpha rad | alpha deg | CD |
|---:|---:|---:|
| `-0.174532925` | `-10` | `0.03400` |
| `-0.157079633` | `-9` | `0.03100` |
| `-0.139626340` | `-8` | `0.02900` |
| `-0.122173048` | `-7` | `0.02700` |
| `-0.104719755` | `-6` | `0.02600` |
| `-0.087266463` | `-5` | `0.02500` |
| `-0.069813170` | `-4` | `0.02400` |
| `-0.052359878` | `-3` | `0.02500` |
| `-0.034906585` | `-2` | `0.02700` |
| `-0.017453293` | `-1` | `0.02900` |
| `0.000000000` | `0` | `0.03200` |
| `0.017453293` | `1` | `0.03500` |
| `0.034906585` | `2` | `0.04000` |
| `0.052359878` | `3` | `0.04600` |
| `0.069813170` | `4` | `0.06000` |
| `0.087266463` | `5` | `0.07000` |
| `0.104719755` | `6` | `0.08500` |
| `0.122173048` | `7` | `0.10500` |
| `0.139626340` | `8` | `0.15000` |
| `0.157079633` | `9` | `0.20000` |
| `0.174532925` | `10` | `0.23000` |

### 10.4 Side axis seed terms

| function | 수식 구조 | 계수 | 의미 | 근거 |
|---|---|---:|---|---|
| `Side_beta_seed` | `qbar*S*beta*value` | `-0.30` | sideslip에 대한 side force | `ASSUMPTION-SEED` |
| `Side_yaw_rate_seed` | `qbar*S*r*aero/bi2vel*value` | `0.12` | yaw rate side force | `ASSUMPTION-SEED` |
| `Side_rudder_seed` | `qbar*S*rudder_pos*value` | `0.18` | rudder/V-tail differential side force | `ASSUMPTION-SEED` |

### 10.5 Roll moment seed terms

| function | 수식 구조 | 계수 | 의미 | 근거 |
|---|---|---:|---|---|
| `Roll_beta_seed` | `qbar*S*b*beta*value` | `-0.10` | dihedral effect seed | `ASSUMPTION-SEED` |
| `Roll_roll_rate_seed` | `qbar*S*b*p*bi2vel*value` | `-0.45` | roll damping seed | `ASSUMPTION-SEED` |
| `Roll_yaw_rate_seed` | `qbar*S*b*r*bi2vel*value` | `0.10` | yaw-rate-to-roll coupling seed | `ASSUMPTION-SEED` |
| `Roll_aileron_seed` | `qbar*S*b*aileron_pos*value` | `0.18` | aileron roll control power seed | `ASSUMPTION-SEED` |
| `Roll_rudder_seed` | `qbar*S*b*rudder_pos*value` | `0.02` | rudder-to-roll coupling seed | `ASSUMPTION-SEED` |

### 10.6 Pitch moment seed terms

| function | 수식 구조 | 계수 | 의미 | 근거 |
|---|---|---:|---|---|
| `Pitch_zero_seed` | `qbar*S*c*value` | `0.030` | zero-alpha pitching moment seed | `ASSUMPTION-SEED` |
| `Pitch_alpha_seed` | `qbar*S*c*alpha*value` | `-0.65` | static longitudinal stability seed | `ASSUMPTION-SEED` |
| `Pitch_rate_seed` | `qbar*S*c*q*ci2vel*value` | `-7.0` | pitch damping seed | `ASSUMPTION-SEED` |
| `Pitch_elevator_seed` | `qbar*S*c*elevator_pos*value` | `-0.80` | elevator/ruddervator pitch control power seed | `ASSUMPTION-SEED` |

### 10.7 Yaw moment seed terms

| function | 수식 구조 | 계수 | 의미 | 근거 |
|---|---|---:|---|---|
| `Yaw_beta_seed` | `qbar*S*b*beta*value` | `0.08` | weathercock stability seed | `ASSUMPTION-SEED` |
| `Yaw_roll_rate_seed` | `qbar*S*b*p*bi2vel*value` | `-0.04` | roll-rate-to-yaw coupling seed | `ASSUMPTION-SEED` |
| `Yaw_yaw_rate_seed` | `qbar*S*b*r*bi2vel*value` | `-0.15` | yaw damping seed | `ASSUMPTION-SEED` |
| `Yaw_aileron_seed` | `qbar*S*b*aileron_pos*value` | `-0.02` | adverse yaw seed | `ASSUMPTION-SEED` |
| `Yaw_rudder_seed` | `qbar*S*b*rudder_pos*value` | `0.10` | rudder/V-tail yaw control power seed | `ASSUMPTION-SEED` |
