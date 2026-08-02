# jsbsim_workflow 교훈 정리

`jsbsim_workflow` 폴더(2026-06-15 ~ 2026-07-31, 약 6주간의 Codex 중심 작업 이력)에서
반복적으로 나타난 함정과, 앞으로 틸트로터 본체 작업에 그대로 재사용할 만한 기법을
정리한다. 원본 `docs/agent-log/*.md`는 총 1만 줄이 넘어 그대로 옮기지 않고, 실제로
직접 읽거나(로그 발췌, `LiftCruise2kg`/`F450` 스크립트 원문) 이 프로젝트에서 실행
검증까지 거친 항목만 근거를 남겨 정리했다. 확인 수준이 다른 항목은 각기 표시했다.

## 1. `initialize/altitude`는 AGL로 해석된다 (실행 검증됨)

JSBSim 1.2.4는 `initialize/altitude`를 문서상 기대와 달리 지형 고도(elevation) 위의
AGL 높이로 처리한다. 이 프로젝트의 QuadX_Baseline을 Codex가 실제로 실행해 직접
확인한 사실이며(`docs/STATUS.md` 2026-08-01 로그), `jsbsim_workflow`의
`LiftCruise2kg`/`F450` 미션 스크립트들도 같은 전제로 작성되어 있다. 예를 들어
`scripts/LiftCruise2kg/initial_condition/1.0__ground_init.xml`은 이륙 전 고도를
`altitude unit="FT">0.52` (스키드 높이 정도)로 두고, 호버 목표는
`ap/altitude-setpoint-ft = 32.80839895`(=10 m)를 `position/h-agl-ft`와 직접
비교하는 이벤트 조건으로 판정한다. 즉 이 프로젝트 전체가 MSL이 아니라 AGL 기준으로
설계·검증되어 있다는 뜻이며, 틸트로터 본체의 초기조건/미션 스크립트를 새로 쓸 때도
동일하게 AGL 기준으로 접근해야 한다.

## 2. JSBSim 1.2.4는 `--aircraft-path`/`--engine-path`/`--systems-path`를 지원하지 않는다 (실행 검증됨)

master(1.3.2.dev1) 문서에 있는 이 세 옵션이 실제 설치된 1.2.4 바이너리에는 없다.
Codex는 `/tmp` 아래에 표준 JSBSim 루트 구조(aircraft/engine/systems 하위 폴더)를
심볼릭 링크로 구성해 우회했다(`docs/STATUS.md`, `docs/agent-log/DECISIONS.md`).
틸트로터 본체 실행 스크립트를 고정할 때는 이 우회 구조를 재현 가능한 셸 스크립트로
만들어 둘 필요가 있다(현재 `docs/STATUS.md` 미해결 이슈로 남아 있음).

## 3. 시간 기반 단일 이벤트보다 "오차 허용범위 + 시간" 이중 게이트가 안정적이다 (원문 확인)

`jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml`은
`simulation/mission-state`라는 정수 프로퍼티로 상태를 관리하는 상태 머신 패턴을 쓴다.
다음 상태로 넘어가는 조건은 단순히 "몇 초가 지났는가"가 아니라, 아래 조건을
`logic="AND"`로 모두 만족해야 한다.

- 최소 경과 시간(`simulation/sim-time-sec ge …`)
- 목표 지점과의 위치 오차가 ±2 m 이내(`ap/north-position-error-m`, `ap/east-position-error-m`)
- 고도 오차가 ±3 ft 이내(`ap/altitude-error-ft`)
- 수평/수직 속도가 ±2~3 fps 이내(정지 상태에 수렴했는지 확인)

이 패턴은 이 프로젝트에서 실제로 발생했던 문제와 정확히 대응된다.
`scripts/QuadX_nominal_mission.xml` 최초 버전은 시간만으로 스로틀 단계를 전환하는
open-loop 방식이어서, 관성 때문에 목표 고도를 지나쳐(약 243.8 ft 오버슈트) 90초
종료 시점까지 착지하지 못하는 실패를 냈다(Codex 실행 검증, `docs/STATUS.md`
2026-08-01 로그). `LiftCruise2kg`의 상태 머신 패턴을 미리 참고했다면 같은 실패를
설계 단계에서 피할 수 있었을 것이다. 틸트로터 본체의 웨이포인트/천이 미션을 설계할
때는 시간 게이트만 쓰지 말고, 이 "오차수렴 + 시간" 이중 조건 패턴을 기본값으로
채택할 것.

## 4. 구조좌표계 vs 동체좌표계 부호 반전 (실행 검증됨, 기존 문서와 정합)

`docs/coordinate_frame_checklist.md`에 이미 상세히 정리되어 있으나, 결론만 다시
적으면: `<location>` 요소(엔진/기어/CG 위치)는 구조좌표계(X=후방 양수, Z=위 양수)를
쓰고, 속도·각속도·공력 계산은 동체좌표계(X=전방 양수, Z=아래 양수)를 쓴다. 두
좌표계의 X, Z 부호가 반대다. F450 공식 예제와 이를 계승한
`aircraft_variants/LiftCruise2kg/Propulsion.xml`(전방 모터 x=-0.250, 후방 모터
x=+0.250) 모두 이 관례를 따르고 있어, 별개의 두 기체 정의에서 동일한 부호 규약이
재확인된 셈이다. 틸트로터 본체에서도 `<location>`을 채울 때 이 부호를 그대로 따를 것.

## 5. 지구 모델은 목적에 맞게 단순화해서 고른다 (원문 확인, 실행 미검증)

`jsbsim_workflow/earth_models/`는 4가지 지구 모델(기본/구형/무자전 기본/무자전
구형)을 미리 만들어 두고, `c172x_fixedwing_test_plan.md`에서 "먼저 무자전+구형
지구로 단순화해 결과가 안정적인지 보고, 이후 WGS84 형상/J2 영향만 따로 비교하고,
마지막에 지리좌표 기반 결과가 필요할 때만 기본(자전+타원체) 지구로 재검증한다"는
단계적 접근을 명시하고 있다. 이는 원인 규명을 위한 좋은 실험 설계 습관이다. 다만
이 항목은 실제 비행 결과가 지구 모델별로 어떻게 달라졌는지까지는 이번 정리에서
직접 확인하지 않았으므로, 기법 자체만 참고하고 수치적 결론은 인용하지 않는다.

## 6. 모터 타입: `brushless_dc_motor` 대신 `electric_engine` (실행 검증됨)

F450 공식 예제가 쓰는 `brushless_dc_motor` 타입은 "failed to tie property" 버그
(JSBSim GitHub Discussion #1183)가 있어, 이 프로젝트의 QuadX_Baseline은 처음부터
`electric_engine`(FGElectric)으로 대체해 작성했고 Codex 실행에서 `power-hp`,
`propeller-rpm` 프로퍼티가 정상적으로 tie됨을 확인했다. 틸트로터 본체의 리프트
모터도 동일하게 `electric_engine`을 기본으로 채택할 것.

## 7. 아직 workflow에 연결되지 않은 자산이 있다는 점 (원문 확인)

`jsbsim_workflow/aircraft_models_comparison.md`에 따르면 `F450`(실체 quadcopter
모델)과 `c172p_2kg_vtol`은 아직 `jsbsim_workflow/scripts/*_run.xml`에 연결되어
검증된 적이 없다고 명시되어 있다. `F450`의 실제 소스는
`/home/junyeopkwon/jsbsim/aircraft/F450/`에 있으며, 이 프로젝트(evtol-6dof)는
현재 그 폴더에 접근 권한이 없다(Cowork 폴더 연결 도구의 UNC 경로 버그로 요청이
반복 실패함). 이 폴더를 수동으로 evtol-6dof 안에 복사해 넣어 주면, F450의 실제
질량/추진/FCS 파라미터까지 비교 근거로 확보할 수 있다.

## 요약: 다음 설계에 바로 적용할 것

1. 틸트로터 초기조건/미션은 AGL 기준으로 설계한다.
2. JSBSim 1.2.4 실행 시 `/tmp` 표준 루트 심볼릭 링크 구조를 스크립트로 고정해
   재현 가능하게 만든다.
3. 웨이포인트/모드 전환 이벤트는 시간 게이트만 쓰지 말고 위치·고도·속도 오차
   수렴 조건을 함께 검사하는 상태 머신 패턴을 쓴다(`ap/*-position-error-m`,
   `ap/altitude-error-ft`, 속도 오차 패턴 참고).
4. `<location>` 부호는 구조좌표계(X=후방+, Z=위+) 기준으로 채운다.
5. 리프트 모터는 `electric_engine`을 기본으로 채택한다.
6. 기회가 되면 `/home/junyeopkwon/jsbsim/aircraft/F450/` 실체 모델 접근을
   확보해 QuadX_Baseline과 교차 검증한다.
