# c172x_4x75kg_cg_aligned_ksfo28r_landing — 기체 제원

기체 폴더: `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_ksfo28r_landing/`
구성: 단일 파일 `c172x_4x75kg_cg_aligned_ksfo28r_landing.xml`(fdm_config,
version="2.0" release="BETA")에 metrics/mass_balance/ground_reactions/
propulsion/system(5개)/autopilot/flight_control/aerodynamics를 전부 포함
(F450처럼 서브파일로 쪼개지 않은 JSBSim 표준 단일파일 스타일). 원본은 JSBSim
공식 예제 c172p(Tony Peden 작성, 1982 Cessna 172P 모델)를 기반으로, 조종사 4인
(각 75kg)을 포인트매스로 얹고 KSFO 28R 랜딩 미션용 커스텀 시스템(순환선회
뱅크홀드, 활주로축 좌표 변환)을 추가한 변형. 이 문서는 이 기체를 쓰는 모든
시나리오 리포트가 공통으로 참조한다(시나리오별 파일에서 중복 기술하지 않음).

## Metrics

| 항목 | 값 |
|---|---|
| WingArea | 174.0 ft² |
| WingSpan | 36.0 ft |
| Chord | 4.9 ft |
| HTailArea / HTailArm | 21.9 ft² / 15.7 ft |
| VTailArea / VTailArm | 16.5 ft² / 15.7 ft |
| AERORP | (43.2, 0.0, 59.4) in |
| EYEPOINT | (37.0, 0.0, 48.0) in |
| VRP | (42.6, 0.0, 38.5) in |

## Mass & Balance

| 항목 | 값 |
|---|---|
| Empty Weight | 1454.0 lbs |
| CG 위치 | (41.0, 0.0, 36.5) in |
| Ixx / Iyy / Izz | 948.0 / 1346.0 / 1967.0 slug·ft² |
| Ixz | 0.0 |
| 탑승 포인트매스 | PILOT/CO-PILOT/PASSENGER 1/PASSENGER 2 각 165.346697 lbs
  (=75 kg) — 이 변형(`4x75kg_cg_aligned`)의 정의. LUGGAGE/PesticideBomb 포인트
  매스는 0 |
| 최대 총중량(콘솔 실측, 연료 포함) | 2375.386788 lbs(런 5.16.5 STATE 0 notify
  값 — 위 empty+탑승 포인트매스+연료 합산 결과, 별도 XML 필드 아님) |

## Propulsion

엔진 `eng_io320`(Lycoming IO-320 계열, 파일이 이 변형 폴더에 없어 정확한
마력/추력 수치는 JSBSim 표준 엔진 라이브러리 참조 필요 — 미확인) + 프로펠러
`prop_75in2f` 1기. 스러스터 위치 (-37.7, 0, 26.6) in, sense=-1, P-factor
계수 10.0. 연료탱크 2개(좌우, 각 130 lbs 용량/탑재).

## Aerodynamics

`aero/qbar-area` 기반 정통 안정미계수(stability derivative) 모델 — F450의
최소 멀티콥터 모델과 달리 알파/플랩/사이드슬립/각속도에 의존하는 다차원
테이블을 갖춘 정식 고정익 공력 모델. LIFT축(CLwbh: alpha×flap×실속 히스테리시스
3차원 테이블, CLDf/CLDe/CLadot/CLq), DRAG축(CDo, CDDf, CDwbh: alpha×flap
테이블, CDDe, CDbeta), SIDE/ROLL/YAW축도 별도 테이블 구성. 지면효과(양력/항력
보정 테이블, `aero/h_b-mac-ft` 기준)와 알파 실속 히스테리시스(`alphalimits`
-0.087~0.28 rad, `hysteresis_limits` 0.09~0.36 rad)를 갖춤 — F450에는 없는
요소.

## Ground Reactions

3점 트라이시클 기어(Nose/Left Main/Right Main) + 날개끝(LEFT_TIP/RIGHT_TIP)과
꼬리(TAIL_SKID) 구조 접촉점 2개(비정상 자세 시 접지 감지용, BOGEY 아님). Nose
Gear 스프링 1800 lbs/ft·댐핑 500 lbs/ft/s, Main Gear 스프링 5400 lbs/ft·댐핑
160 lbs/ft/s(우측은 함수식으로 재구현된 동일 특성 + 리바운드 시 댐핑 2배).
정지/동/구름 마찰 0.8/0.5/0.022(주기어 공통).

## Autopilot / FCS 특이사항

**F450과 근본적으로 다른 아키텍처** — F450은 `ap/mode` 정수 하나로 게이팅되는
SWITCH 체인이지만, 이 기체는 `ap/attitude_hold`/`ap/altitude_hold`/
`ap/heading_hold` **3개의 독립 불리언 플래그**로 각 채널을 따로 켜고 끈다.

- Roll 채널: `ap/attitude_hold`(윙레벨러, phi PID) 또는 `ap/heading_hold`
  (헤딩 PI, `ap/heading_setpoint`와 현재 헤딩 오차를 ±30° 클립 후 PI) 중
  `ap/heading_hold==1`이 우선 선택되어 `ap/aileron_cmd`로 출력. **두 홀드
  모두 `gear/unit[2]/WOW==0`(우측 주기어 공중)일 때만 작동** — 접지 중에는
  자동조종 롤 출력이 자동으로 0이 됨(안전 인터록).
- Pitch 채널: `ap/altitude_hold==1`이면 `ap/altitude_setpoint`와
  `position/h-agl-ft`(주석은 "sea level, not AGL"이라고 적혀 있으나 실제
  코드 입력은 h-agl-ft — **주석과 코드가 불일치**, 코드 기준이 맞음)의 오차를
  hdot 명령으로 변환 → PID → `ap/elevator_cmd`. 이 채널도 `gear/unit[2]/WOW==0`
  일 때만 출력.
- `ap/elevator_cmd`/`ap/aileron_cmd`(자동조종 출력)는 `fcs/pitch-trim-sum`/
  `fcs/roll-trim-sum`에서 `fcs/elevator-cmd-norm`/`fcs/aileron-cmd-norm`
  (런스크립트 직접 명령)과 **합산**된다 — F450처럼 서로 배타적으로 덮어쓰는
  게 아니라 더해지는 구조이므로, 자동조종 비활성(hold=0) 상태에서 런스크립트가
  `fcs/aileron-cmd-norm`을 직접 `<set>`해도 안전하게 반영된다.
- 별도의 "Circular loiter bank hold" 시스템(`mission/circular-bank-target-rad`,
  `mission/circular-roll-output`)이 아치파일에 정의되어 있으나, 게이팅 조건
  `simulation/circular-bank-hold-active==1`을 이 기체가 쓰는 어떤 런스크립트
  이벤트도 1로 설정하지 않는 경우가 있다 — 해당 시나리오에서는 이 서브시스템이
  항상 0을 출력하는 죽은 경로가 된다(시나리오별로 실제 사용 여부 확인 필요,
  `5.16` 리포트의 분석 절 참고).

## 표기법 (기체 고유)

공통 기호(t_sim, s_mis, h_AGL, V_cas, α, WOW_i 등)는 `../_notation_common.md`
참고. 아래는 이 기체의 FCS/미션 프로퍼티에 쓰는 기호.

| 기호 | JSBSim 프로퍼티 | 단위 | 설명 |
|---|---|---|---|
| δ_thr | `fcs/throttle-cmd-norm` | – | 정규화 스로틀 명령 |
| δ_ail | `fcs/aileron-cmd-norm` | – | 정규화 에일러론 명령(런스크립트 직접) |
| δ_ele | `fcs/elevator-cmd-norm` | – | 정규화 엘리베이터 명령(런스크립트 직접) |
| δ_rud | `fcs/rudder-cmd-norm` | – | 정규화 러더 명령 |
| δ_flap | `fcs/flap-cmd-norm` | – | 정규화 플랩 명령(0~1) |
| δ_mix | `fcs/mixture-cmd-norm` | – | 정규화 믹스처 명령 |
| δ_lb,δ_rb,δ_cb | `fcs/left/right/center-brake-cmd-norm` | – | 좌/우/센터 브레이크 |
| δ_steer | `fcs/steer-cmd-norm` | – | 노즈기어 조향 명령 |
| δ_ptrim,δ_rtrim,δ_ytrim | `fcs/pitch/roll/yaw-trim-cmd-norm` | – | 피치/롤/요 트림 |
| ATT_h | `ap/attitude_hold` | – | 자동조종 자세(윙레벨러) 홀드 플래그 |
| ALT_h | `ap/altitude_hold` | – | 자동조종 고도홀드 플래그 |
| HDG_h | `ap/heading_hold` | – | 자동조종 헤딩홀드 플래그 |
| ψ_sp | `ap/heading_setpoint` | deg | 목표 헤딩(자동조종) |
| h_sp | `ap/altitude_setpoint` | ft | 목표 고도(AGL, 자동조종) |
| stall | `simulation/stall-detected` | – | 실속 감지 플래그(안전 이벤트가 설정) |
| cruise | `simulation/cruise-active` | – | 순항 구간 활성 플래그 |
| t_cruise | `simulation/cruise-timer-sec` | s | 순항 타이머 |
| land_auth | `simulation/landing-authorized` | – | 착륙 인가 플래그(안전 이벤트가
  참조) |
| loiter | `simulation/circular-loiter-active` | – | 원형 선회 활성 플래그 |
| bank_h | `simulation/circular-bank-hold-active` | – | 원형 선회 뱅크홀드
  서브시스템 게이트(위 "Autopilot/FCS 특이사항" 참고 — 5.16에서는 항상 0) |
| φ_tgt | `mission/circular-bank-target-rad` | rad | 뱅크홀드 목표 뱅크각(고정값
  -0.30 rad) |
| h_tgt | `simulation/target-altitude-ft` | ft | 미션 목표 고도(모니터링용) |
| x_rwy | `mission/runway-along-ft` | ft | 활주로축 along 좌표(시작점 기준,
  활주로 진입 방향이 음수) |
| y_rwy | `mission/runway-cross-ft` | ft | 활주로축 cross 좌표(활주로 중심선
  기준 좌우 편차) |
| magneto | `propulsion/magneto_cmd` | – | 점화 마그네토 명령(0=off, 3=both) |
| starter | `propulsion/starter_cmd` | – | 시동 명령 |
| run | `propulsion/set-running` | – | 엔진 강제 구동 플래그(-1=자동) |
