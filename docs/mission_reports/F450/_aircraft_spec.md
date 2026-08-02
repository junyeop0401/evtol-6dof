# F450 — 기체 제원

기체 폴더: `/home/junyeopkwon/jsbsim/aircraft/F450/`
구성: `F450.xml`(top-level) → `Metrics.xml` + `Mass.xml` + `Gear.xml` +
`Propulsion.xml` + `Effectors.xml`(system) + `FlightControl.xml` +
`F450AP.xml`(autopilot) + PX4 IMU/baro/GPS 센서 3종(system) + `Aero.xml`.
release="ALPHA", version="2.0". 이 문서는 이 기체를 쓰는 모든 시나리오 리포트가
공통으로 참조한다(시나리오별 파일에서 중복 기술하지 않음).

## Metrics (`Metrics.xml`)

| 항목 | 값 |
|---|---|
| WingArea | 0.016129 m² |
| WingSpan | 0.127 m |
| Chord | 0.127 m |
| AERORP / EYEPOINT / VRP 위치 | 전부 원점 (0,0,0) m |

## Mass & Balance (`Mass.xml`)

| 항목 | 값 |
|---|---|
| Empty Weight | 1.4 kg |
| CG 위치 | 원점 (0,0,0) m |
| Ixx | 0.0190 kg·m² |
| Iyy | 0.0190 kg·m² |
| Izz | 0.0252 kg·m² |
| Ixy, Ixz, Iyz | 0 |

## Propulsion (`Propulsion.xml`) — DJI E305 모터 × DJI 9450 프로펠러 × 4

| 모터 | 위치 (x,y,z) [m] | Sense | 회전방향 |
|---|---|---|---|
| Front Right | (-0.1651, 0.1651, 0.025) | +1.0 | (전방=구조좌표계 X 음수) |
| Aft Left | (0.1651, -0.1651, 0.025) | +1.0 | |
| Front Left | (-0.1651, -0.1651, 0.025) | -1.0 | FR/AL과 반대 |
| Aft Right | (0.1651, 0.1651, 0.025) | -1.0 | FR/AL과 반대 |

모두 `pitch=90deg` 방향(추력이 -Z, 즉 위쪽)으로 장착. FR/AL과 FL/AR이
서로 반대 회전(sense 부호)으로 짝을 이루는 표준 X-쿼드 배치(요 토크 상쇄).

모터/프로펠러 스펙(콘솔 로그 기준, 4기 동일):

| 항목 | 값 |
|---|---|
| 모터(DJI E305) 정격출력 | 1835.9587 W |
| Speed Factor | 960 |
| Coil Resistance | 0.1170 Ω |
| No-Load Current | 0.45 A |
| 프로펠러(DJI 9450) 직경 | 0.7833 ft (≈ 23.9 cm) |
| 블레이드 수 | 2 |

## Aerodynamics (`Aero.xml`)

멀티콥터라 실질적인 양력/항력면은 없고, 수치 안정성을 위한 최소 모델만 존재:
CD__zero=1.0(항력계수 상수), 나머지(CL, CY, CMl/CMm/CMn)는 전부 0. 6축 모두
`aero/qbar-area`(모멘트축은 `metrics/bw-ft`/`cbarw-ft`도 추가)를 곱해 힘/모멘트
단위로 정확히 환산하고 있음 — 이 곱셈을 빠뜨리면 QuadX_Baseline 초기 버전처럼
호버 트림이 오염되는 버그가 생기는데, F450은 처음부터 올바르게 되어 있음.

## Ground Reactions (`Gear.xml`)

3점 착륙기어(Front_Center, Aft_Left, Aft_Right — "JSBSim은 4점 지상트림을
어려워한다"는 원문 주석에 따라 의도적으로 3점 구성). 스프링 3000 N/m,
댐핑 100 N/m/s, 정지마찰 0.8, 동마찰 0.5, 구름마찰 0.02, 3점 모두 동일.

## Autopilot (`F450AP.xml`) — 호버 자동조종

North-East 위치홀드 → 자세홀드(PID) → 고도홀드(PID) → F450 명령 출력까지
이어지는 4단 체인. `ap/mode`로 게이팅됨(0=비활성, 1/2=자세/속도 계열,
3=호버 전체 폐루프). `ap/hover-throttle-base = 0.31`(실측 선언값 — 호버
스로틀 베이스라인). 실측 호버 중 `ap/collective-cmd-norm`은 약 0.412로
수렴(베이스라인 0.31 + 고도오차 보정분). **`ap/mode`를 거치지 않고
FCS 명령 프로퍼티를 런스크립트에서 직접 `<set>`하면 이 자동조종이 매 프레임
덮어써서 무효화된다** — `2.0__nominal_mission_profile.md` 참고.

## 표기법 (기체 고유)

F450 FCS/자동조종 프로퍼티에 쓰는 기호. 공통 기호(t_sim, s_mis, k_frame 등)는
`../_notation_common.md` 참고.

| 기호 | JSBSim 프로퍼티 | 단위 | 설명 |
|---|---|---|---|
| δ_thr | `fcs/throttle-cmd-norm` | – | 정규화 스로틀 명령(-1~1 또는 0~1) |
| δ_ail | `fcs/aileron-cmd-norm` | – | 정규화 에일러론 명령 |
| δ_ele | `fcs/elevator-cmd-norm` | – | 정규화 엘리베이터 명령 |
| δ_rud | `fcs/rudder-cmd-norm` | – | 정규화 러더 명령 |
| SCAS | `fcs/ScasEngage` | – | SCAS(안정성증강장치) 인게이지 플래그(0/1).
  `ap/mode`가 1/2/3이 아니면 자동조종이 매 프레임 0으로 강제 |
| m_ap | `ap/mode` | – | 자동조종 모드(0=비활성/1,2=자세·속도 계열/3=호버
  전체 폐루프) |
| N_sp | `ap/north-setpoint-m` | m | 북방향 목표 위치(로컬) |
| E_sp | `ap/east-setpoint-m` | m | 동방향 목표 위치(로컬) |
| h_sp | `ap/altitude-setpoint-ft` | ft | 목표 고도(AGL) |
| ψ_sp | `ap/heading-setpoint-rad` | rad | 목표 헤딩 |
| ref_alt | `ap/altitude-reference` | – | 고도 기준 선택 플래그 |
| e_N | `ap/north-position-error-m` | m | 북방향 위치오차(목표−현재) |
| e_E | `ap/east-position-error-m` | m | 동방향 위치오차 |
| e_h | `ap/altitude-error-ft` | ft | 고도오차 |
| h_AGL | `position/h-agl-ft` | ft | 지면고도(AGL) |
| ḣ | `velocities/h-dot-fps` | ft/s | 수직속도(상승률, +가 상승) |
| v_N | `velocities/v-north-fps` | ft/s | 북방향 속도 |
| v_E | `velocities/v-east-fps` | ft/s | 동방향 속도 |
| rpm_i | `propulsion/engine[i]/propeller-rpm` (i=0..3) | rpm | 모터 i 프로펠러 회전수 |
