# 공통 표기법 (Notation) — 모든 기체 공용

미션 리포트의 "초기조건"/"runscript 이벤트별 조건·명령" 표는 JSBSim 프로퍼티
경로(`position/h-agl-ft` 등)를 그대로 쓰지 않고, 아래 정의한 기호로 바꿔
수식처럼 쓴다(예: `simulation/sim-time-sec ge 1.0` → `t_sim ≥ 1.0`). 여기
정의한 기호는 harness/runscript 구조 자체에서 오는 것이라 기체가 달라져도
동일하게 쓴다. 기체별 FCS/자동조종 프로퍼티 기호는 해당 기체의
`_aircraft_spec.md` "표기법(기체 고유)" 절에 별도 정의한다.

**단위 표기 원칙**: 아래 "단위" 열은 이 프로젝트에서 실제로 관측된 대표 단위를
적은 것이며 XML의 `unit` 속성이 다르면(m vs ft 등) 그 리포트에서 실제 단위로
바꿔 적는다 — 기호 자체는 단위와 무관하게 고정.

## 초기조건(Initial Condition) 기호

| 기호 | JSBSim 프로퍼티 | 단위(대표) | 설명 |
|---|---|---|---|
| V₀ | `initialize/vt` | m/s | 초기 속도 크기(진대기속도) — 방향은 동체 X축
  기본. `ubody/vbody/wbody`로 초기조건을 주는 기체는 아래 u₀/v₀/w₀ 참고 |
| u₀,v₀,w₀ | `initialize/ubody`,`vbody`,`wbody` | ft/s | 동체좌표계 초기 속도
  성분(X/Y/Z) — V₀ 대신 이 세 값으로 초기조건을 주는 방식도 있음(둘 중
  하나만 쓰임) |
| Lat | `initialize/latitude` | deg | 위도(geodetic, `type` 속성 확인) |
| Lon | `initialize/longitude` | deg | 경도(geodetic/geocentric 구분 없음) |
| h₀ | `initialize/altitude` | m | 초기 고도 — **AGL로 해석됨**(JSBSim 1.2.4
  실행검증, `reference/docs/lessons_learned.md` 1절). MSL 값이 아니므로
  `h_terr`와 같은 값을 넣으면 안 됨(그 값만큼 공중에서 스폰됨) |
| h_terr | `initialize/elevation` | m | 지형 고도(MSL 기준, 참고용 — 초기
  스폰 높이 계산에 직접 쓰이지 않음) |
| φ₀ | `initialize/phi` | deg | 초기 롤각(동체좌표계) |
| θ₀ | `initialize/theta` | deg | 초기 피치각(동체좌표계) |
| ψ₀ | `initialize/psi` | deg | 초기 헤딩(진북 기준 시계방향, 동체좌표계) |

## 시뮬레이션 제어/상태머신 기호 (runscript 공통)

| 기호 | JSBSim 프로퍼티 | 단위 | 설명 |
|---|---|---|---|
| t_sim | `simulation/sim-time-sec` | s | 시뮬레이션 경과시간 |
| k_frame | `simulation/frame` | – | 프레임 번호(정수 카운터, 주로 초기 1~2
  프레임 게이팅에 사용) |
| s_mis | `simulation/mission-state` | – | 미션 상태 인덱스(정수, runscript가
  직접 정의하는 상태머신 — 기체/시나리오마다 상태 수·의미가 다름) |
| trim | `simulation/do_simple_trim` | – | 트림 실행 명령(2 = 지상 트림) |
| term | `simulation/terminate` | – | 시뮬레이션 종료 플래그(1 = 종료) |
| t_trig | `simulation/notify-time-trigger` | s | 다음 notify(콘솔 출력) 발동
  시각 — 매 notify 이벤트가 자기 자신을 갱신(Δ)하며 반복 출력을 구현 |

## 비행상태/착지 공통 기호

| 기호 | JSBSim 프로퍼티 | 단위 | 설명 |
|---|---|---|---|
| h_AGL | `position/h-agl-ft` | ft | 지면고도(AGL) |
| ḣ | `velocities/h-dot-fps` | ft/s | 수직속도(상승률, +가 상승) |
| V_cas | `velocities/vc-kts` | kts | 보정대기속도(calibrated airspeed) —
  고정익 runscript에서 rotate/flare 속도 게이트에 자주 쓰임 |
| α | `aero/alpha-deg` | deg | 받음각(angle of attack) |
| φ,θ,ψ | `attitude/phi-deg`,`theta-deg`,`psi-deg` | deg | 롤/피치/헤딩(진행 중
  자세, 초기조건의 φ₀/θ₀/ψ₀와 구분해 아래첨자 없이 표기) |
| WOW_i | `gear/unit[i]/WOW` | – | 착륙기어 i의 Weight-On-Wheels 플래그(0/1,
  1=접지) |

## Runscript 구성요소 표기

- **`<delay>X</delay>`**: 이벤트의 `<condition>`이 참이 된 뒤 X초를 더
  기다렸다가 `<set>`을 실행하는 지연 구성요소. 표에서는 조건 뒤에
  `+delay Xs`로 붙여 쓴다(예: `s_mis = 5 AND cruise = 1  +delay 30s`).
- **`action="FG_RAMP" value="V" tc="T"`**: 즉시 값을 바꾸지 않고 시정수
  T(초)로 현재값에서 V까지 점진 변화(1차 지연 램프)시키는 `<set>` 옵션.
  표에서는 `δ ↝ V (τ=T s)`로 표기한다(↝는 "즉시 아님, 램프"를 뜻함 — 시정수
  없이 즉시 반영되는 일반 `<set>`은 그냥 `δ = V`).

## 표에서 생략하는 부기(bookkeeping) 프로퍼티

- `simulation/next-event-time`: 일부 runscript(F450 1.2 계열)에서 매 이벤트마다
  `<set>`되지만, 어떤 `<condition>`에서도 조회되지 않는 **미사용 부기
  프로퍼티**로 확인됨(전체 runscript 원문 대조 완료). 미션 로직에 영향이
  없으므로 이벤트표의 명령 목록에서 생략하고, 생략 사실만 표 위에 한 줄로
  밝힌다.

## 일반화 확인 이력

- **F450(멀티콥터, `ap/mode` 단일 스위치 기반) → c172x_4x75kg_cg_aligned_ksfo28r_landing
  (고정익, `ATT_hold`/`ALT_hold`/`HDG_hold` 3개 독립 플래그 기반, 24개 상태 +
  4개 안전중단 이벤트, `<delay>`/`FG_RAMP` 구성요소 사용)로 일반화 검증
  완료(2026-08-02).** 이 과정에서 추가된 게 정확히 이 문서의 "비행상태/착지
  공통 기호"절과 "Runscript 구성요소 표기"절이다 — 기체가 바뀌어도
  t_sim/s_mis/h_AGL 같은 harness/상태머신 공통 기호는 그대로 재사용됐고,
  새로 필요해진 것(V_cas, α, WOW_i, delay, FG_RAMP)은 여기 공용 표기법에
  추가했으며, 그 기체만의 FCS 프로퍼티(δ_thr 등 구체적 매핑, ATT_h/ALT_h/HDG_h
  등)만 해당 기체의 `_aircraft_spec.md`에 추가하는 것으로 충분했다 — 애초
  설계한 "공용/기체고유 2단 분리" 원칙이 실제로 작동함을 확인.

## 사용 예

`simulation/frame le 1` → `k_frame ≤ 1`
`simulation/sim-time-sec ge 3.0` → `t_sim ≥ 3.0`
`simulation/mission-state eq 0` → `s_mis = 0`
`<set name="fcs/throttle-cmd-norm" action="FG_RAMP" value="1.0" tc="1.0"/>` →
`δ_thr ↝ 1.0 (τ=1.0 s)`
`<condition>...</condition><delay>30.0</delay>` → 조건 뒤에 `+delay 30s`
