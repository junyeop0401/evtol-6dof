## [2026-06-15 17:51] DECISION-20260615-1751-001 — ACCEPTED

- 문제:
  - 캡쳐본의 `(x, y, z)` 로컬 좌표계를 JSBSim 지리 좌표/Local NED 결과로 어떻게 보고할지 결정 필요
- 고려한 대안:
  - `x=East, y=North`로 보고하고 초기 `psi=90 deg`를 사용
  - `x=North, y=East`로 보고하고 캡쳐본 yaw `0 deg`를 JSBSim `psi=0 deg`로 그대로 사용
- 최종 선택:
  - `x=North, y=East`, `z=ground altitude`로 보고하고, 초기 `psi=0 deg`를 유지
- 선택 이유:
  - 캡쳐본 초기 자세각의 yaw `0 deg`를 JSBSim heading `psi=0 deg`로 직접 반영하는 해석이 최소 변환임
  - JSBSim Local NED에서 heading 0 deg는 North 방향이므로 local North를 보고용 x로 둠
- 영향 범위:
  - 결과 요약 파일의 충돌 좌표 필드명
  - 초기 진행 방향
- 장점:
  - 캡쳐본 자세각 입력을 그대로 유지
  - 좌표 변환 가정이 명시됨
- 단점:
  - 사용자가 x축을 East로 의도했다면 좌표 해석이 달라질 수 있음
- 검증 결과:
  - 최종 실행 `4.0.4__450m_60ms_pitch25_no_trim_drop` 성공
- 남은 리스크:
  - 좌표축 의도가 다르면 `psi=90 deg` 또는 summary mapping 변경 필요
- 기존 결정과의 관계:
  - 신규 결정

## [2026-06-15 18:00] DECISION-20260615-1800-001 — SUPERSEDED

- 대상 기존 결정:
  - `TASK-20260615-1751-001` 및 `PROGRESS-20260615-1751-001`의 `4.0` 직접 초기상태 추락 해석
- 교체 이유:
  - 사용자가 의도한 시나리오는 “초기 pitch 상태를 그대로 둔 자유응답”이 아니라 “x 방향 60 m/s cruise 중 engine-out”임을 정정
- 기존 방식:
  - 450 m, 60 m/s, pitch 2.5 deg를 직접 초기조건으로 넣고 trim/autopilot/propulsion 없이 적분
- 신규 방식:
  - 450 m, 60 m/s, heading 0 deg 조건에서 powered cruise trim 및 hold를 만든 뒤 31초에 engine-out
- 고려한 대안:
  - `4.0` 파일을 직접 수정
  - `4.1` 새 케이스로 보존하며 추가
- 영향 범위:
  - wrapper 기본 실행 대상
  - README의 4.x 설명
  - 결과 요약 기준 Run ID
- 검증 결과:
  - `4.1.1__450m_60ms_x_cruise30_engineout_headinghold` 실행 성공
- 남은 리스크:
  - heading hold 유지가 autopilot 개입이므로 완전 무조종 추락과는 다름

## [2026-06-15 18:13] DECISION-20260615-1813-001 — ACCEPTED

- 문제:
  - 추락 시작 시점을 `t=0`으로 직접 실행할 때 제어 입력을 어떻게 둘지 결정 필요
- 고려한 대안:
  - heading hold와 pitch trim을 유지해 직진 활공 형태를 재현
  - 기존 최초 요청의 trim/autopilot 없이 조건을 반영해 AP/trim 모두 off
- 최종 선택:
  - `4.2.2` 기준 AP/trim 모두 off
- 선택 이유:
  - 사용자가 초기 좌표, 초기 속도, 시간 0, 지구 모델을 명확히 지정했고, 최초 요청의 `trim/autopilot 없이` 조건과 일관됨
  - cruise 30초 절차를 제거하는 목적과도 더 직접적으로 맞음
- 영향 범위:
  - 최종 궤적이 직진 활공이 아니라 실속/회전 거동을 포함
  - 최종 x 방향 변위가 작고 y 방향/자세 변화가 커질 수 있음
- 장점:
  - 초기조건 기반 순수 JSBSim 동역학 응답에 가까움
- 단점:
  - 사용자가 기대한 직진 추락/활공 그래프와 다르게 보일 수 있음
- 검증 결과:
  - `4.2.2__450m_60ms_x_engineout_t0_spherical` 실행 성공
- 남은 리스크:
  - 직진 활공 해석이 필요하면 heading hold/trim 유지 케이스가 별도 필요
- 기존 결정과의 관계:
  - `DECISION-20260615-1800-001`의 cruise 후 engine-out 해석을 직접 초기조건 실행 방식으로 대체

## [2026-06-15 18:20] DECISION-20260615-1820-001 — ACCEPTED

- 문제:
  - 기존 ballistic 결과 이미지와 유사한 형태를 `c172x`에서 얻기 위해 어떤 케이스를 기준으로 둘지 결정 필요
- 고려한 대안:
  - `4.2` AP/trim off 결과 유지
  - ballistic 전용 질점/drag-only 모델 생성
  - `c172x` 원본 모델에 heading hold와 glide trim을 적용한 별도 케이스 생성
- 최종 선택:
  - `4.3` heading hold + pitch trim `0.18` glide 케이스를 별도 생성
- 선택 이유:
  - 사용자가 제공한 ballistic 결과는 방향 고정 활공 추락 느낌에 가깝다고 판단
  - `4.2` AP/trim off는 실속/회전이 커서 비교 목적에 부적합
  - 질점 모델 생성보다 `c172x` 기반 비교 케이스로 빠르게 확인 가능
- 영향 범위:
  - `4.2`는 순수 AP/trim off 기준으로 보존
  - `4.3`은 ballistic-like 비교용 기준으로 추가
- 장점:
  - 루프 없이 방향을 유지하는 궤적 확보
  - 같은 초기조건과 지구 모델을 유지해 비교 가능
- 단점:
  - heading hold와 trim이 개입하므로 순수 무조종 추락은 아님
  - `c172x` 양력 때문에 기존 ballistic보다 비행거리와 시간이 크게 늘어남
- 검증 결과:
  - `4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical` 실행 성공
- 남은 리스크:
  - ballistic과 거리까지 맞추려면 별도 ballistic/drag-only 모델 또는 공력 보정 필요
- 기존 결정과의 관계:
  - `DECISION-20260615-1813-001`의 AP/trim off 기준을 대체하지 않고 비교용으로 보완

## [2026-06-15 17:51] DECISION-20260615-1751-002 — ACCEPTED

- 문제:
  - 지면 도달 시간을 어떤 조건으로 산출할지 결정 필요
- 고려한 대안:
  - `position/h-sl-meters <= 0` 기준
  - `position/h-agl-ft <= 0` 기준
  - `gear/unit[0]/WOW eq 1` 기준
- 최종 선택:
  - `gear/unit[0]/WOW eq 1` 기준 첫 지면 접촉
- 선택 이유:
  - `c172x`는 착륙장치 지면 반력이 있어 CG 고도 0 m 이전에 실제 지면 접촉이 발생함
  - JSBSim 항공기 모델에서 접촉 이벤트를 직접 표현하는 property가 `WOW`임
- 영향 범위:
  - 지면 도달 시간과 최종 자세각 산출 시점
  - 요약 파일의 `cg_altitude_at_contact_m`가 0보다 큰 값으로 기록됨
- 장점:
  - JSBSim 항공기 모델의 물리 접촉 상태와 일치
- 단점:
  - 캡쳐본처럼 질점/CG가 지면 z=0에 도달하는 해석과는 다름
- 검증 결과:
  - 최종 접촉 시 `cg_altitude_at_contact_m = 1.5949587921649218 m`
- 남은 리스크:
  - 사용자가 CG 기준 지면 도달을 원하면 종료 조건과 충돌 보간 방식을 변경해야 함
- 기존 결정과의 관계:
  - 신규 결정
## [2026-06-16 11:56] DECISION-20260616-1156-001 — ACCEPTED

- 문제:
  - 27개 `c172x.xml` 변형을 workflow 내부에 보관하면서도 JSBSim의 aircraft 로딩 규칙에 맞게 실행해야 함
- 고려한 대안:
  - 원본 `/home/junyeopkwon/jsbsim/aircraft/c172x/c172x.xml`을 직접 덮어쓰기
  - 27개 변형을 JSBSim aircraft 폴더에 직접 생성
  - workflow 내부에 변형 원본을 두고 실행 시 선택 변형만 JSBSim aircraft 폴더에 설치
- 최종 선택:
  - `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_groundreaction/{variant}/c172x.xml`에 변형 원본을 보관하고, 실행 시 `/home/junyeopkwon/jsbsim/aircraft/{variant}/{variant}.xml`로 복사/rename
- 선택 이유:
  - 사용자가 요청한 `jsbsim_workflow` 내부 정리 요구를 만족
  - 원본 `c172x.xml`을 수정하지 않음
  - 기존 `run_jsbsim_timestamped.py`의 로그/plot 생성 흐름을 그대로 재사용 가능
- 영향 범위:
  - workflow 내부에 27개 변형 XML과 manifest 생성
  - 실행한 variant는 JSBSim aircraft 폴더에도 설치 복사본 생성
- 장점:
  - 변형 XML 추적과 결과 로그가 workflow 기준으로 정리됨
  - 각 variant가 독립 aircraft 이름을 가지므로 로그 경로가 섞이지 않음
- 단점:
  - JSBSim 실행 전 설치 복사 단계가 필요함
  - 설치된 variant aircraft 폴더는 workflow 밖 `/home/junyeopkwon/jsbsim/aircraft/`에 남음
- 검증 결과:
  - 기본 계수 변형 설치 및 실행 성공
- 남은 리스크:
  - 27개 전체 실행 시 JSBSim aircraft 폴더에 변형별 설치 복사본이 추가됨
- 기존 결정과의 관계:
  - 신규 결정

## [2026-06-16 11:56] DECISION-20260616-1156-002 — ACCEPTED

- 문제:
  - `c172x.xml`의 right main gear는 명시적 `spring_coeff`/`damping_coeff`가 아니라 equivalent `strut_force` 함수로 같은 힘을 정의하므로 계수 변형 대상 처리 방식 결정 필요
- 고려한 대안:
  - 명시적 coefficient 태그만 조정하고 right main gear의 `strut_force`는 유지
  - right main gear의 `strut_force`를 삭제하고 `spring_coeff`/`damping_coeff` 태그로 교체
  - 기존 `strut_force` 구조를 유지하면서 내부 spring/damping `<value>`를 배율 조정
- 최종 선택:
  - 기존 `strut_force` 구조를 유지하고 원본 값 `-5400`, `-160`, `-320`을 각각 spring/damping 배율에 맞춰 조정
- 선택 이유:
  - 원본 XML의 구조와 의도를 최대한 보존하면서 좌우 main gear 모두 같은 배율 실험 대상에 포함하기 위함
- 영향 범위:
  - right main gear의 spring/damping 변형이 left main gear와 동등하게 반영됨
- 장점:
  - 계수 비교에서 오른쪽 main gear만 기본값으로 남는 오류를 방지
- 단점:
  - 원본 `strut_force` 값 구조가 바뀌면 생성기 업데이트 필요
- 검증 결과:
  - 기본 배율 `1.0`에서 실행 성공
- 남은 리스크:
  - `0` 배율 변형은 비물리적 조건이라 실행 안정성을 별도 보장하지 않음
- 기존 결정과의 관계:
  - 신규 결정
## [2026-06-16 12:08] DECISION-20260616-1208-001 — ACCEPTED

- 문제:
  - FlightGear C172 매뉴얼 기반 자동이륙 절차를 JSBSim runscript로 구현할 때, 순수 수동 입력만 사용할지 AP 안정화를 함께 사용할지 결정 필요
- 고려한 대안:
  - FlightGear 수동 절차를 그대로 고정 조종 입력만으로 구현
  - 50 ft 이후 기존 C172X 성공 패턴처럼 attitude/heading/altitude hold를 일부 사용
  - Python closed-loop controller로 heading, airspeed, climb rate를 매 step 보정
- 최종 선택:
  - `5.1` runscript에는 FlightGear 임계값 기반 상태 전이를 구현하되, 50 ft 이후 `ap/attitude_hold`, 250 ft 이후 `ap/heading_hold`/`ap/altitude_hold`를 사용하는 하이브리드 절차 적용
- 선택 이유:
  - 순수 고정 조종 입력만으로는 기본 계수 variant가 지면 재접촉 또는 수치 발산을 일으킴
  - 기존 `3.0` 이륙 스크립트도 50 ft 이후 AP 안정화를 사용해 성공했음
  - 사용자의 목적은 ground reaction 계수별 이륙 가능성 비교이므로, 반복 가능한 안정 상승 절차가 우선
- 영향 범위:
  - `run_c172x_groundreaction_takeoff.py` 기본 실행은 `5.1` flightgear 절차가 됨
  - 기존 단순 100 ft 확인 절차는 `--procedure basic`으로 유지
- 장점:
  - FlightGear 문서의 40 kt, 55 kt, 70 kt, 500 ft 상태 기준을 보존
  - 기본 계수 variant에서 500 ft AGL 도달 성공
- 단점:
  - 50 ft 이후 AP가 개입하므로 완전한 수동 이륙 재현은 아님
  - 70 kt target은 상태 기준으로 반영했지만 최종 속도 유지 성능은 아직 부족
- 검증 결과:
  - `5.1.10__takeoff_flightgear_state_machine` 실행에서 `climb_500ft_confirmed=True`
- 남은 리스크:
  - 일부 계수 변형에서는 AP 안정화 이전 지상 활주/rotation 단계에서 실패할 수 있음
- 기존 결정과의 관계:
  - `DECISION-20260616-1156-001`의 variant 설치/실행 구조를 유지하면서 procedure만 확장
## [2026-06-16 12:34] DECISION-20260616-1234-001 — ACCEPTED

- 문제:
  - 30초 부근 고도 꺾임을 만들던 `ap/attitude_hold` 조기 개입을 제거하면서도 원본 `c172x`가 500 ft까지 안정 상승해야 함
- 고려한 대안:
  - 20 ft 이후 attitude hold 유지
  - 모든 AP를 제거하고 고정 조종 입력만 사용
  - 20 ft 이후 attitude hold는 제거하고 100 ft 이후 heading hold, 250 ft 이후 altitude hold만 사용
- 최종 선택:
  - 20 ft 이후 attitude hold 제거, 100 ft 이후 heading hold, 250 ft 이후 altitude hold
- 선택 이유:
  - attitude hold 조기 개입은 altitude plot의 비정상 꺾임을 유발
  - 완전 고정 입력만으로는 C172X가 wing tip 접촉 또는 지면 재접촉을 일으킴
  - heading/altitude hold를 늦게 분리 적용하면 500 ft 도달과 방향 안정성을 동시에 확보 가능
- 영향 범위:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.3__takeoff_to_500ft_c172x_run.xml`
- 장점:
  - 30초 부근 altitude/attitude hold 개입 제거
  - 원본 `c172x`로 500 ft AGL 도달 유지
- 단점:
  - 완전 수동 고정 입력은 아님
  - 70 kt target 유지 성능은 아직 부족
- 검증 결과:
  - `5.3.6__takeoff_to_500ft_c172x` 실행 성공
- 남은 리스크:
  - 100 ft 이후 heading hold와 250 ft 이후 altitude hold에 따른 작은 과도응답은 남을 수 있음
- 기존 결정과의 관계:
  - `DECISION-20260616-1208-001`의 조기 attitude hold 방식에서 안정화 시점을 늦추는 개정
## [2026-06-16 18:23] DECISION-20260616-1823-001 — ACCEPTED

- 문제:
  - 사용자가 요청한 "엔진 없는상태"를 runscript만으로 구현할지, 별도 no-engine aircraft variant를 생성할지 결정 필요
- 고려한 대안:
  - 기존 `c172x.xml`을 그대로 사용하고 runscript/초기조건에서 engine off 명령을 강제
  - `c172x.xml`에서 `<propulsion>`을 제거한 별도 aircraft variant 생성
- 최종 선택:
  - runscript/초기조건 수준의 engine off 케이스 `4.4`를 추가
- 선택 이유:
  - 사용자 요청이 runscript 작성으로 한정됨
  - 기존 `4.x` 실험 구조와 호환되고 기존 aircraft 파일을 변경하지 않아 회귀 위험이 낮음
  - timestamp runner, SI 변환, plot, summary 생성 흐름을 그대로 사용할 수 있음
- 영향 범위:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 장점:
  - 기존 `c172x` 모델과 비교 가능
  - 실행 명령이 단순함
  - 기존 JSBSim runner 출력 체계를 재사용
- 단점:
  - aircraft XML에 propulsion/propeller 모델이 남아 있어 windmilling 관련 로그가 완전 0이 아닐 수 있음
- 검증 결과:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_drop.py` 실행 성공
- 남은 리스크:
  - "엔진 없는상태"가 실제 엔진 질량/추력/프로펠러 공력 제거를 의미한다면 별도 aircraft variant가 필요
- 기존 결정과의 관계:
  - 기존 `4.2`, `4.3` engine-out 케이스는 유지하고, AP/trim 없는 더 직접적인 no-engine drop 케이스를 추가
## [2026-06-16 18:32] DECISION-20260616-1832-001 — ACCEPTED

- 문제:
  - 기존 `4.4` runscript는 engine off 명령을 적용하지만 원본 aircraft의 propeller windmilling 출력이 남음
- 고려한 대안:
  - `<propulsion>` 전체 제거
  - `<propulsion>`은 유지하고 `<engine>`만 제거
  - output 변환에서 engine/propeller 값을 강제로 0으로 후처리
- 최종 선택:
  - `<propulsion>`은 유지하고 `<engine>`만 제거한 `c172x_noengine` aircraft variant 생성
- 선택 이유:
  - `<engine>` 제거로 engine thrust와 propeller thruster를 실제 모델에서 제거할 수 있음
  - fuel tank를 유지해 원본 기체 질량/연료 조건 변화가 과도하게 커지는 것을 피함
  - 후처리 0 처리보다 동역학 모델 차원에서 요구조건을 충족함
- 영향 범위:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_noprop_drop.py`
- 장점:
  - 원본 `c172x`를 변경하지 않음
  - engine/thrust/propeller 출력이 전 구간 0으로 검증됨
  - 기존 timestamp runner와 호환됨
- 단점:
  - 엔진/프로펠러의 구조 질량 제거까지 반영하지는 않음
- 검증 결과:
  - `engine_count=0`, `thruster_count=0`, `tank_count=2`
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_noprop_drop.py` 실행 성공
- 남은 리스크:
  - 질량 모델까지 엄밀한 no-engine airframe이 필요하면 `mass_balance` 보정 필요
- 기존 결정과의 관계:
  - `DECISION-20260616-1823-001`의 후속 결정이며, runscript 수준 engine off에서 aircraft variant 수준 engine/propeller 제거로 확장
## [2026-06-16 20:54] DECISION-20260616-2054-001 — ACCEPTED

- 문제:
  - roll/yaw가 조종면 문제인지 pointmass 비대칭 문제인지 분리 필요
- 고려한 대안:
  - 조종면 command만 보정
  - elevator bias만 제거
  - pointmass를 모두 0으로 만든 기본 기체 variant 생성
- 최종 선택:
  - engine/propeller 제거, elevator bias 제거, 모든 pointmass weight 0 variant 생성
- 선택 이유:
  - 사용자가 기본 기체 공력 영향만 보고 싶다고 명시
  - `PesticideBomb` 등 비대칭 pointmass가 roll/yaw에 영향을 줄 가능성이 큼
  - 원본 파일 변경 없이 variant로 분리 가능
- 영향 범위:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty/`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/`
- 장점:
  - payload/비대칭 질량 영향 제거
  - 실제 조종면 0 상태 확인 가능
  - roll/yaw 원인 분리가 명확함
- 단점:
  - 실제 탑승/연료/외부 하중 조건과는 다른 empty-airframe 조건
- 검증 결과:
  - roll/yaw가 수치오차 수준으로 감소
- 남은 리스크:
  - 180초 내 지면 접촉 전이라 전체 낙하 완료점은 미확인
- 기존 결정과의 관계:
  - `DECISION-20260616-1832-001`, `DECISION-20260616-1823-001`의 no-engine/no-propeller 흐름을 기본 기체 공력 확인용으로 확장
## [2026-06-17 10:49] DECISION-20260617-1049-001 — ACCEPTED

- 문제:
  - pitch-up 원인 분리를 위해 `Cmo`만 바꾼 비교 모델이 필요
- 고려한 대안:
  - 기존 aircraft XML 직접 수정
  - 기존 generated variant 수정
  - 새 `c172x_noengine_surface_neutral_empty_cm0` variant 생성
- 최종 선택:
  - 새 `c172x_noengine_surface_neutral_empty_cm0` aircraft variant 생성
- 선택 이유:
  - 기존 결과와 모델을 보존
  - `Cmo` 외 조건을 동일하게 유지해 비교 가능
  - 반복 생성 가능
- 영향 범위:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/`
- 장점:
  - `Cmo=0.1` 대비 `Cmo=0.0` 효과를 명확히 비교 가능
- 단점:
  - 실제 C172 모델 물리성보다는 원인 분리용 실험 모델임
- 검증 결과:
  - `Cmo=0`에서 고도 상승이 0 m로 감소
- 남은 리스크:
  - 전체 longitudinal dynamics 해석에는 추가 coefficient sweep이 필요할 수 있음
- 기존 결정과의 관계:
  - `DECISION-20260616-2054-001`의 empty-airframe/surface-neutral 실험을 `Cmo` 민감도 확인으로 확장
## [2026-06-17 14:15] DECISION-20260617-1415-001 — DONE

- 문제:
  - 6DOF 검증용 property 묶음을 모든 aircraft에 동일하게 `<output>`에 넣으면 모델별로 존재하지 않는 property 때문에 실행 실패 또는 무의미한 로그가 생길 수 있음
- 고려한 대안:
  - 요청 property를 그대로 모두 `<output>`에 삽입
  - aircraft별로 수동 property 목록 관리
  - 실행 시 `--catalog`로 available property를 확인한 뒤 존재하는 항목만 삽입
- 최종 선택:
  - `--catalog` 기반으로 요청 property를 필터링하고, 존재하는 property만 별도 6DOF output에 삽입
- 선택 이유:
  - C172X, VTOL, multicopter처럼 서로 다른 aircraft variant에 같은 runner를 적용할 수 있음
  - 없는 engine/gear/aero coefficient property로 인한 실행 리스크를 줄임
  - 모델별 catalog 차이를 기록 가능한 skipped list로 남길 수 있음
- 영향 범위:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
- 장점:
  - 기존 raw/SI 로그와 독립적으로 6DOF 검증용 raw CSV를 추가 가능
  - aircraft별 property 차이를 자동 반영
- 단점:
  - 실행 전 catalog 호출이 추가되어 약간의 오버헤드가 생김
  - catalog에 없는 property는 CSV에 빈 컬럼으로 남지 않고 제외됨
- 검증 결과:
  - `c172x_noengine_surface_neutral_empty_cm0`에서 76개 property가 선택되어 `sixdof_raw` CSV 생성 성공
- 남은 리스크:
  - PX4 비교용으로는 raw 단위와 frame 변환 후처리가 여전히 필요함
- 기존 결정과의 관계:
  - 기존 timestamped runner의 raw/SI 출력 구조를 유지하면서 별도 검증 로그를 추가하는 확장 결정

## [2026-06-21 15:54] DECISION-20260621-1554-001 — 확정

- 문제: 기존 pointmass-zero 모델은 noengine 구성이라 이륙 활주를 수행할 수 없고, 전체 크루즈 튜닝 중 3·4단계 원인 분리가 어려움
- 고려한 대안: 기존 noengine 모델 사용, 기본 c172x 탑승점질량 유지, 동력 계통을 보존한 pointmass-zero 변형 생성
- 최종 선택: 원본 엔진·공력·지상반력 계통을 보존하고 조종자·승객 pointmass만 0으로 만든 c172x_empty_cg_aligned 사용
- 선택 이유: 추진 이륙 능력과 원본 비행 특성을 최대한 유지하면서 좌우 무게중심 비대칭 원인을 제거하기 위함
- 영향 범위: 3·4단계 진단 runscript와 해당 로그·plot
- 장점: inertia/cg-y-in 0을 유지하며 실제 엔진 이륙 가능
- 단점: 빈 탑승 상태로 총중량과 종방향 무게중심이 기본 탑승 모델과 달라짐
- 검증 결과: 모델 로드·엔진 출력·55 kt 회전·이륙 확인
- 남은 리스크: 연료에 따른 inertia/cg-x-in 및 inertia/cg-z-in 변화는 존재하며, 이는 좌우 비대칭 제거와 별개의 문제
- 기존 결정과의 관계: noengine surface-neutral 모델을 이륙 시나리오에 직접 사용하는 방식을 대체

## [2026-06-21 15:54] DECISION-20260621-1554-002 — 작업 중단

- 문제: 4단계 완료 조건의 성공 오판과 개루프 자세 불안정이 확인됨
- 최종 선택: 사용자 지시에 따라 완료 조건 보정과 제어 튜닝을 수행하지 않고 현재 현상과 로그를 그대로 보존
- 선택 이유: 요청 범위가 문제 수정이 아니라 현황과 문제점 정리로 변경됨
- 영향 범위: scripts/c172x/runscript/5.5__takeoff_stage3_stage4_diagnostic_run.xml은 현재 조건을 유지
- 검증 결과: 원본 완료 이벤트 이름 Stage 4 complete - 70 kt above 150 ft 유지 확인
- 남은 리스크: 해당 이벤트 발생을 안전한 초기상승 완료로 해석하면 안 됨


## [2026-06-21 18:45] DECISION-20260621-1845-001 — 확정

- 문제: 사용자 요구는 JSBSim 기본 지구이나 공용 runner의 C172X 기본값은 04_nonrotating_spherical_earth.xml
- 고려한 대안: 공용 runner 기본값 전역 변경, 신규 시나리오에서 --planet default 명시
- 최종 선택: 공용 동작을 보존하고 신규 시나리오 실행 명령에 --planet default를 필수로 명시
- 선택 이유: 기존 추락·비자전 지구 워크플로 회귀를 방지하면서 이번 요구를 정확히 만족
- 영향 범위: 5.6 RKSS 이륙 시나리오와 README 실행 명령
- 장점: 기존 API·기존 시나리오 영향 없음
- 단점: 옵션 누락 시 다른 지구 모델이 선택됨
- 검증 결과: 생성된 JSBSim 명령에서 --planet 인자가 제거되고 내장 지구로 전체 시퀀스 완료
- 남은 리스크: 수동 실행 시 옵션 누락 가능

## [2026-06-21 18:45] DECISION-20260621-1845-002 — 확정

- 문제: 첨부 초기조건의 altitude, running, latitude가 JSBSim 실제 파서 의미와 일부 다름
- 고려한 대안: 첨부 XML을 문자 그대로 적용, JSBSim 소스와 실행 로그에 맞게 의미 보정
- 최종 선택: elevation=38.0 ft, altitude=4.305 ft AGL, latitude type=geodetic, running 요소 생략
- 선택 이유: 바퀴를 활주로에 놓고 측지 좌표를 보존하며 t=0 엔진 정지를 실제 데이터로 보장
- 영향 범위: 2.2__rkss_14l_default_earth_init.xml
- 장점: 초기 AGL 4.305 ft, MSL 42.305 ft, geodetic latitude 37.5707083333 deg를 정확히 재현
- 단점: 첨부 설명의 altitude=38.0 및 running=0 표기와 문자적으로 다름
- 검증 결과: raw CSV t=0 위치·속도·RPM 확인, 초기 자세·좌표 정상
- 남은 리스크: 없음

## [2026-06-21 18:45] DECISION-20260621-1845-003 — 확정

- 문제: 이전 4단계에서 heading setpoint=0 deg가 RKSS 14L heading=135.01 deg와 충돌해 과대 롤 발생
- 최종 선택: AGL 20 ft에서 heading_setpoint=135.01 deg와 altitude_setpoint=1000 ft를 동시에 결합
- 선택 이유: 활주로 진행방향 유지와 종·횡 자세 폐루프 안정화를 함께 확보
- 영향 범위: 5.6__rkss14l_default_earth_takeoff_cruise30_run.xml
- 검증 결과: 30초 순항 roll -0.067375~-0.039563 deg, heading 최종 약 135.09 deg
- 남은 리스크: 자동조종 안정화까지 약 224초가 소요되어 운용 효율 개선 여지 존재


## [2026-06-23 08:56] DECISION-20260623-0856-001 — 확정

- 문제: 순항 종료 후 추락을 비행제어 유지 활공과 완전 비제어 추락 중 어떤 방식으로 정의할지 결정 필요
- 고려한 대안: heading hold 유지 활공, glide trim 적용, autopilot·조종면·trim 완전 중립
- 최종 선택: 엔진과 모든 autopilot을 끄고 수동 조종면·trim을 0으로 설정한 비제어 추락
- 선택 이유: 사용자 요청의 엔진 정지 후 추락을 추가 제어 없이 가장 직접적으로 재현
- 영향 범위: 5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml
- 장점: 엔진 정지 이후 기체 고유 동역학과 불안정성을 관찰 가능
- 단점: 실제 조종사의 최적 활공이나 비상착륙 절차를 나타내지 않음
- 검증 결과: 엔진 정지 23.70 s 후 지면 충돌, RPM·추력 0
- 남은 리스크: 충돌 이후 구조 파손 모델은 없으므로 첫 랜딩기어 접촉을 충돌 완료로 사용
- 기존 결정과의 관계: 5.6 순항 완료 시 terminate하던 동작을 확장

## [2026-06-23 08:56] DECISION-20260623-0856-002 — 확정

- 문제: JSBSim 실행 파일만으로 QGroundControl에서 기체를 볼 수 있는지 판단
- 고려한 대안: JSBSim native socket 직접 연결, PX4 jsbsim_bridge 사용, CSV를 MAVLink로 변환
- 최종 선택: JSBSim 단독 직접 연결은 불가로 판정하고 PX4 SITL bridge 또는 별도 MAVLink adapter를 필수 구성으로 분류
- 선택 이유: QGC는 MAVLink vehicle telemetry가 필요하지만 JSBSim 코어 실행은 heartbeat·vehicle state를 송신하지 않음
- 영향 범위: QGC 연동 설계와 scripts/c172x/README.md
- 장점: 동역학 계산기, autopilot, GCS의 역할을 명확히 분리
- 단점: QGC 실시간 표시에는 추가 프로세스가 필요
- 검증 결과: 로컬 PX4 jsbsim_bridge에서 HIL_SENSOR·HIL_GPS·MAVLink 포트 14550 구현 확인, JSBSim 코어에서는 대응 구현 미확인
- 남은 리스크: QGC와 PX4 버전 조합별 포트·HIL 설정은 실제 통합 실행으로 추가 확인 필요


## [2026-06-23 09:25] DECISION-20260623-0925-001 — 완료

- 문제: `c172x_empty_cg_aligned` aircraft는 존재하지만 `scripts/c172x_empty_cg_aligned/` 시나리오 폴더가 없어 대화형 runner가 초기조건 후보를 찾지 못함
- 고려한 대안: runner에 `c172x_empty_cg_aligned -> c172x` 매핑 추가, `scripts/c172x/` 전체 복사, 현재 필요한 RKSS 14L 시나리오만 전용 폴더로 복사
- 최종 선택: 현재 필요한 `2.2` 초기조건과 `5.6`, `5.7` runscript만 `scripts/c172x_empty_cg_aligned/`로 분리
- 선택 이유: runner의 기존 `scripts/<aircraft>/` 규칙을 유지하면서 대화형 선택 문제를 해결하고, 오래된 실험 스크립트를 대량 복사해 메뉴를 혼잡하게 만들지 않기 위함
- 영향 범위: `c172x_empty_cg_aligned` 선택 시 초기조건 1개와 runscript 2개가 표시됨
- 장점: runner 코드 변경 없음, 기존 `scripts/c172x/` 보존, 현재 5.7 시나리오 실행 경로 명확화
- 단점: `scripts/c172x/`와 `scripts/c172x_empty_cg_aligned/` 사이에 일부 XML 복사본이 생겨 향후 동기화 관리 필요
- 검증 결과: XML 문법 검증, runner 컴파일, 새 경로 기반 5.7 JSBSim 실행 성공
- 남은 리스크: 기존 README 일부에는 아직 `scripts/c172x/` 경로 예시가 남아 있음
- 기존 결정과의 관계: 2026-06-21과 2026-06-23의 RKSS 14L 시나리오 자체는 유지하고, 파일 배치만 aircraft명 기준으로 분리

## [2026-06-23 09:50] DECISION-20260623-0950-001 — 완료

- 문제: 기존 runner는 저장용 plot 생성을 위해 `matplotlib.use("Agg", force=True)`를 사용하므로 같은 프로세스에서 GUI live animation을 안정적으로 띄우기 어려움
- 고려한 대안: runner 내부에서 Matplotlib GUI 백엔드로 전환, JSBSim 후처리 plot만 생성, 별도 프로세스 live animator 실행, QGC/PX4 연동
- 최종 선택: 별도 프로세스 `scripts/live_trajectory_3d.py`를 실행하고, runner는 live 모드에서 JSBSim에 `--realtime`만 추가
- 선택 이유: 기존 batch plot 동작을 유지하면서 GUI 백엔드 충돌을 피하고, C172X 외 다른 JSBSim CSV에도 재사용 가능하게 하기 위함
- 영향 범위: `scripts/run_jsbsim_timestamped.py`, `scripts/live_trajectory_3d.py`, `scripts/README.md`
- 장점: 기존 비실시간 실행은 `--no-live-3d` 또는 비대화형 기본값으로 유지, live 기능은 선택적으로만 작동
- 단점: live 모드 실행 시간은 JSBSim 시뮬레이션 시간과 거의 같아지고, GUI display 환경이 필요
- 검증 결과: CLI 옵션 노출, headless 애니메이터 CSV 로딩, `--realtime` 명령 삽입, 기존 no-live 실행 검증 완료
- 남은 리스크: 실제 GUI 창 확인은 사용자 터미널 환경에서 수동 검증 필요
- 기존 결정과의 관계: QGC 연동 대신 JSBSim CSV 기반 내부 시각화를 우선 제공하는 별도 경량 경로

## [2026-06-23 13:05] DECISION-20260623-1305-001 — 완료

- 문제: CSV 저장 property를 사용자가 빠르게 찾을 수 있도록 유사 역할별로 분류해야 함
- 고려한 대안: 기존 CSV 헤더만 기준으로 분류, XML output property만 기준으로 분류, 공용 runner의 property 상수와 기존 CSV/XML을 함께 대조
- 최종 선택: scripts/run_jsbsim_timestamped.py의 공용 property 상수를 주 기준으로 삼고, 기존 CSV 헤더와 XML output 정의를 cross-check로 포함
- 선택 이유: 현재 workflow에서 새 실행 시 실제 생성되는 raw CSV와 6DOF CSV 목록은 runner 상수가 가장 직접적이며, 기존 CSV/XML 대조를 넣어 과거 산출물과의 차이도 추적 가능
- 영향 범위: 산출물 workbook의 분류·source trace 구성에만 영향, JSBSim 실행 코드와 기존 결과 파일은 변경하지 않음
- 장점: raw CSV, 6DOF 검증 CSV, SI 변환 대상, 기존 header 발견 여부, XML source를 한 파일에서 비교 가능
- 단점: 분류 기준이 prefix·명칭 기반이므로 JSBSim 내부 class/module 기준의 공식 계층과 1:1로 일치한다고 보장하지 않음
- 검증 결과: workbook export 성공, 수식 오류 검색 0건, CSV/XML 대조 수량 확인
- 남은 리스크: 특정 property의 해석이 연구 보고서 수준으로 필요하면 JSBSim catalog 및 source 코드 기준 설명 열을 추가해야 함
- 기존 결정과의 관계: 기존 runner CSV 저장 구조를 변경하지 않고 문서화 산출물만 추가

## [2026-06-30 09:40] DECISION-20260630-0940-001 — 완료

- 문제: `c172x_empty_cg_aligned`는 모든 pointmass가 0이라 탑승자 질량 영향이 제거되어 있고, 75 kg × 4명을 넣으면 기존 5.6 속도 조건에서 안정 순항 완료 여유가 부족할 수 있음
- 고려한 대안: 원본 `c172x` 질량 복원, `c172x_empty_cg_aligned` 직접 수정, 별도 aircraft 변형 생성, runscript의 조종면/고도/추력까지 재튜닝
- 최종 선택: 별도 aircraft `c172x_4x75kg_cg_aligned`를 만들고, 5.6.1에서는 속도 관련 조건만 증가
- 선택 이유: 원본/empty 변형을 보존하고, 사용자 지시대로 동일 init 기반에서 기체만 바꾼 비교와 속도쪽 변경만 분리하기 위함
- 영향 범위: JSBSim aircraft 목록에 `c172x_4x75kg_cg_aligned` 추가, workflow aircraft_variants 보관본 추가, `scripts/c172x/runscript/5.6.1...` 추가
- 장점: 좌우 대칭 pointmass로 `cg-y-in=0` 유지, 기존 5.6과 5.6.1 비교 가능, 조종 로직 변경 없음
- 단점: 5.6.1은 경험적 속도 증분이며 최적화된 C172 POH 절차 검증은 아님
- 검증 결과: 5.6.1에서 STATE 5와 STATE 6 이벤트 확인, 30초 순항 완료
- 남은 리스크: 질량 증가에 따른 실제 활주거리/상승성능 타당성은 별도 POH 또는 FlightGear 조종 모델 비교가 필요
- 기존 결정과의 관계: `c172x_empty_cg_aligned`를 보존하고, 탑승자 질량 비교용 새 변형으로 분리

## [2026-06-30 10:00] DECISION-20260630-1000-001 — 완료

- 문제: FlightGear 시각화는 항상 켜면 실행 시간이 느려지고 Windows FlightGear 수신 준비가 필요함
- 고려한 대안: 항상 FlightGear output directive 연결, 별도 wrapper 유지, runner에 선택형 옵션 추가
- 최종 선택: runner에 `--flightgear` / `--no-flightgear` 선택 옵션과 대화형 질문을 추가
- 선택 이유: 기본 workflow의 CSV/plot 실행을 유지하면서, 사용자가 FlightGear로 보고 싶을 때만 `--realtime`과 `--logdirectivefile`을 붙이기 위함
- 영향 범위: `scripts/run_jsbsim_timestamped.py`, `scripts/README.md`
- 장점: 기존 실행은 기본적으로 미연동, FlightGear 사용 시 명령 반복 입력 감소, live 3D와 독립적으로 선택 가능
- 단점: FlightGear GUI와 UDP 수신 준비는 여전히 사용자가 별도로 수행해야 함
- 검증 결과: 옵션 노출, 명령 구성, no-flightgear 실행 검증 완료
- 남은 리스크: 실제 FlightGear 수신 확인은 수동 검증 필요

## [2026-06-30 10:30] DECISION-20260630-1030-001 — 완료

- 문제: Matplotlib live3d와 FlightGear 시각화가 동시에 존재하면 실행 선택지가 복잡하고, 사용자는 FlightGear를 주 시각화 경로로 사용할 예정
- 고려한 대안: live3d 파일 삭제, runner에서만 제거하고 파일 보존, 둘 다 유지
- 최종 선택: runner에서는 live3d 기능을 제거하고 `scripts/live_trajectory_3d.py` 파일은 보존
- 선택 이유: 사용 경로는 FlightGear로 단순화하되, 이미 작성한 standalone helper는 향후 참고/백업 용도로 남길 수 있기 때문
- 영향 범위: `run_jsbsim_timestamped.py` CLI와 대화형 흐름, `scripts/README.md`
- 장점: 기본 실행 선택지가 단순해지고 FlightGear 중심 시각화 정책이 명확해짐
- 단점: README를 읽지 않으면 `live_trajectory_3d.py`가 왜 남아 있는지 혼동 가능
- 검증 결과: help에서 `--live-3d` 제거 확인, `--flightgear` 유지 확인, no-flightgear 실행 성공
- 남은 리스크: 실제 FlightGear 수신은 별도 수동 검증 필요

## [2026-06-30 11:47] DECISION-20260630-1147-001 — SUPERSEDED

- 대상 기존 결정: interactive runner에서 `--planet` 미지정 시 nonrotating spherical earth를 자동 사용하는 기존 동작
- 교체 이유: 현재 RKSS 14L takeoff/cruise 시나리오와 FlightGear 연동은 JSBSim default Earth 기준이며, interactive 실행에서만 custom planet이 자동 삽입되어 FlightGear output 조합에서 `SIGFPE`가 발생함
- 기존 방식: `args.planet is None`이면 F450을 제외하고 `/home/junyeopkwon/jsbsim_workflow/earth_models/04_nonrotating_spherical_earth.xml` 사용
- 신규 방식: `args.planet is None`이면 `planet_path=None`으로 두어 JSBSim builtin default Earth 사용. custom planet은 `--planet <xml>`을 명시한 경우만 사용
- 고려한 대안: FlightGear 사용 시에만 default Earth 적용, interactive planet 선택 질문 추가, 기존 nonrotating default 유지
- 최종 선택: runner 기본값을 JSBSim default Earth로 통일
- 영향 범위: `scripts/run_jsbsim_timestamped.py`의 interactive 및 `--planet` 미지정 CLI 실행
- 장점: explicit `--planet default` 실행과 interactive 실행이 일관됨, FlightGear output SIGFPE 회피
- 단점: 과거 nonrotating spherical earth를 암묵적으로 기대한 실행은 이제 `--planet earth_models/04_nonrotating_spherical_earth.xml`를 명시해야 함
- 검증 결과: 기본값 `None` 확인, `--planet` 없는 FlightGear output 짧은 실행에서 SIGFPE 미발생
- 남은 리스크: 과거 로그 중 nonrotating earth 기준 결과와 새 default earth 기준 결과를 비교할 때 planet 조건을 명시적으로 구분해야 함

## [2026-06-30 14:25] DECISION-20260630-1425-001 — 적용

- 문제:
  - ADS XML을 jsbsim_workflow에 넣되, JSBSim 실행 위치인 /home/junyeopkwon/jsbsim과 workflow 보관/실행 선택 구조를 구분해야 함
- 고려한 대안:
  - jsbsim_workflow 루트에 ADS 파일을 모두 평면 배치
  - scripts/ADS 아래에 aircraft와 engine까지 모두 배치
  - 기존 workflow 규칙에 맞춰 aircraft_variants, engine_variants, scripts/ADS, logs/results/plots를 분리
- 최종 선택:
  - aircraft XML 복사본은 aircraft_variants/ADS에 둠
  - engine XML 복사본은 engine_variants/ADS에 둠
  - runner 선택용 초기조건과 runscript는 scripts/ADS/initial_condition 및 scripts/ADS/runscript에 둠
  - ADS 전용 산출물 위치로 logs/csv/raw/ADS, logs/csv/si/ADS, logs/console/ADS, logs/generated_runscripts/ADS, plots/ADS, results/ADS를 생성함
- 선택 이유:
  - 기존 scripts/README.md의 aircraft별 폴더 규칙과 맞음
  - JSBSim source tree 설치 파일과 workflow snapshot의 역할을 구분할 수 있음
  - 후속 실행 결과가 다른 기체 결과와 섞이지 않음
- 영향 범위:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS
  - /home/junyeopkwon/jsbsim_workflow/engine_variants/ADS
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS
  - /home/junyeopkwon/jsbsim_workflow/logs 및 results 및 plots 아래 ADS 폴더
- 장점:
  - ADS 모델 진행 위치가 명확함
  - runner interactive 선택 구조에 편입하기 쉬움
  - 실제 실행 전후 산출물 관리가 분리됨
- 단점:
  - source tree 원본과 workflow 복사본이 이중화되어 동기화 관리가 필요함
  - engine_variants는 새 폴더라 기존 문서 사용자가 모를 수 있어 WORKFLOW_INSTALL.md와 scripts/ADS/README.md로 보완함
- 검증 결과:
  - workflow ADS XML 16개 정적 파싱 성공
  - workflow 내부 참조 누락 0개 확인
- 남은 리스크:
  - runner 실제 실행에서 ADS 전용 output property 후처리 보강이 필요할 수 있음
- 기존 결정과의 관계:
  - jsbsim 프로젝트의 ADS XML 초안 결정을 workflow 실행 준비 구조로 반영함


## [2026-06-30 14:34] DECISION-20260630-1434-001 — DONE

- 문제: /home/junyeopkwon/jsbsim_workflow 전체 용량 중 logs/와 plots/ 등 실행 산출물이 대용량이라 그대로 Git에 포함하면 저장소가 불필요하게 커짐
- 고려한 대안: 모든 파일을 추적, 산출물만 제외, 별도 대용량 파일 관리 도구 사용
- 최종 선택: logs/, results/, plots/, outputs/, Python cache류를 .gitignore로 제외하고 소스, 설정, 문서, workflow 파일만 Git에 포함
- 선택 이유: 현재 요청의 목적은 JSBSim workflow 구성 파일을 관리하는 것이며, 실행 산출물은 재생성 가능하고 크기가 큼
- 영향 범위: /home/junyeopkwon/jsbsim_workflow Git 추적 대상
- 장점: 저장소 크기를 줄이고 XML, 스크립트, 문서 중심으로 추적 가능
- 단점: 기존 대용량 실행 결과는 원격 저장소에 포함되지 않음
- 검증 결과: git status --short --ignored에서 산출물 디렉터리가 ignored로 표시됨
- 남은 리스크: 특정 실행 결과를 재현성 자료로 보존해야 하는 경우 별도 아카이브 또는 Git LFS 정책이 필요함
- 기존 결정과의 관계: ADS workflow 구성은 실행 전 XML 산출물 중심으로 관리한다는 기존 범위와 일치함


## [2026-06-30 15:09] DECISION-20260630-1509-001 — DONE

- 문제: 일부 ADS 파일에는 명시적 author 태그가 없고, ADS.xml에는 OpenAI Codex 저자 표기가 남아 있었음
- 고려한 대안: 기존 author 태그만 변경, 모든 ADS 파일에 공통 저자 주석 추가, Git 커밋 작성자만 유지
- 최종 선택: 기존 author 태그는 junyeopkwon으로 변경하고, author 태그가 없는 ADS XML과 Markdown에는 가벼운 저자 표기를 추가
- 선택 이유: 파일 단위로 산출물 저자를 확인할 수 있고, XML 구조 변경 없이 주석 또는 문서 메타데이터만 추가하므로 영향이 작음
- 영향 범위: ADS 관련 XML 및 Markdown 파일
- 장점: GitHub 파일 화면과 로컬 파일에서 작성자 식별이 쉬움
- 단점: XML 파일 상단에 주석 1줄이 추가됨
- 검증 결과: XML 파싱 오류 없음
- 남은 리스크: JSBSim 실행까지는 확인하지 않음
- 기존 결정과의 관계: ADS 모델은 초기 placeholder 산출물이라는 기존 문서화 범위와 일치함


## [2026-06-30 18:26] DECISION-20260630-1826-001 — DONE

- 문제: 20 kg ADS placeholder motor/prop은 추력 부족으로 hover 검증이 막혔고, 기존 DJI_E305 + DJI_9450은 F450급 소형 조합임
- 고려한 대안: 20 kg ADS 추진계 재보정, F450 직접 사용, ADS_mini 1 kg 스케일 모델 생성
- 최종 선택: ADS_mini 1 kg 모델을 별도 aircraft로 만들고 DJI_E305 + DJI_9450을 사용
- 선택 이유: JSBSim 내부에 이미 검증 예제가 있는 전기 motor/prop 조합으로 aircraft 구성, FCS, runscript, logging pipeline을 빠르게 검증할 수 있음
- 영향 범위: ADS_mini 모델 및 테스트 스크립트에 한정, 기존 ADS 20 kg 모델은 유지
- 장점: 10 m hover/landing workflow를 실제 JSBSim 실행으로 확인 가능
- 단점: ADS_mini 결과는 20 kg ADS의 물리적 성능 검증이 아님
- 검증 결과: ADS_mini 10 m hover/landing runscript 정상 종료
- 남은 리스크: hover pitch trim과 착륙 후 contact chatter 개선 필요
- 기존 결정과의 관계: 기존 ADS는 목표 기체 모델로 유지하고, ADS_mini는 테스트 스케일 모델로 병행


## [2026-06-30 18:48] DECISION-20260630-1848-001 — DONE

- 문제: 사용자가 말한 의사코드는 엄격한 문법이 아니라 사람이 이해 가능한 코드형 설명이므로 XML 태그 나열만으로는 목적에 맞지 않음
- 고려한 대안: XML 원문 주석 추가, 표 형식 설명, 파일별 의사코드 Markdown 작성
- 최종 선택: ADS_mini_xml_pseudocode.md에 파일별 의사코드와 핵심 의미를 함께 작성
- 선택 이유: 실제 코드에 가까운 흐름을 유지하면서도 한국어 설명으로 각 XML 역할을 빠르게 이해할 수 있음
- 영향 범위: 문서 파일 추가에 한정
- 장점: XML 구조를 모르는 사람도 JSBSim 모델 흐름을 따라갈 수 있음
- 단점: 실제 XML과 값이 바뀌면 문서도 같이 갱신해야 함
- 검증 결과: 문서 생성 및 일부 내용 확인
- 남은 리스크: ADS_mini가 아닌 ADS 원형 XML 설명은 포함하지 않음
- 기존 결정과의 관계: ADS_mini를 workflow/FCS 검증용 별도 모델로 운용한다는 기존 결정과 일치

## [2026-07-01 00:00] DECISION-20260701-0000-ADS0 — 완료

- 문제: 사용자는 `ADS 0`라는 이름의 값 없는 기체 템플릿을 원했지만, JSBSim/Git 파일 경로에서 공백 이름은 관리와 참조가 불편할 수 있다.
- 고려한 대안: `ADS 0` 공백 포함 폴더명 사용, `ADS_0` 언더스코어 폴더명 사용
- 최종 선택: `ADS_0` 언더스코어 폴더명 및 XML name 사용
- 선택 이유: JSBSim 파일 참조, Git 경로, 스크립트 자동화에서 안전하고 기존 `ADS_mini` 명명 패턴과도 일관된다.
- 영향 범위: `aircraft_variants/ADS_0`, `engine_variants/ADS_0`
- 장점: 파일 참조 오류 가능성 감소, 후속 자동 설치/복사 작업 단순화
- 단점: 사용자 표시명 `ADS 0`와 실제 파일명이 완전히 동일하지 않음
- 검증 결과: `ADS_0.xml` 내부 include 및 engine 파일 참조가 `ADS_0_*`로 연결됨, XML 파싱 성공
- 남은 리스크: 향후 표시명으로 공백 포함 명칭이 필요하면 별도 문서/메타데이터에서 표현해야 함
- 기존 결정과의 관계: ADS/ADS_mini의 분리형 workflow 구조를 유지하는 결정과 일관됨

## [2026-07-19 23:35] DECISION-20260719-2335-001 — DONE

- 문제:
  - C172X 4x75kg 조건을 위해 aircraft XML을 새로 만들지, 기존 variant를 재사용할지 결정 필요
- 고려한 대안:
  - 기존 c172x_4x75kg_cg_aligned 재사용
  - c172x 원본을 복제해 새 4x75kg variant 생성
- 최종 선택:
  - 기존 c172x_4x75kg_cg_aligned 재사용
- 선택 이유:
  - 해당 XML에 PILOT, CO-PILOT, PASSENGER 1, PASSENGER 2가 각각 165.346697 lb로 이미 반영되어 있어 사용자 질량 조건과 일치
  - 새 aircraft variant를 만들면 동일 모델 중복과 설치 tree 동기화 리스크가 증가함
- 영향 범위:
  - 새 initial condition 및 runscript만 추가
  - aircraft_variants/c172x_4x75kg_cg_aligned/c172x_4x75kg_cg_aligned.xml은 수정하지 않음
- 장점:
  - 기존 검증 모델과 runner discovery 구조 유지
  - 변경 범위 최소화
- 단점:
  - 기존 variant의 fuel 260 lb 등 기타 질량 조건은 그대로 유지됨
- 검증 결과:
  - JSBSim Mass Properties Report에서 4명 occupant가 각각 165.3 lb로 출력됨
  - 두 runscript 모두 JSBSim 실행 완료
- 남은 리스크:
  - 사용자가 연료량까지 별도 조건으로 고정하려면 추가 aircraft 또는 runscript property 설정이 필요함
- 기존 결정과의 관계:
  - 기존 c172x_4x75kg_cg_aligned variant 운용 방식을 유지

## [2026-07-19 23:35] DECISION-20260719-2335-002 — DONE

- 문제:
  - 김포공항 조건에서 활주로 heading 대신 동쪽 heading을 어떻게 반영할지 결정 필요
- 고려한 대안:
  - 기존 RKSS 14L heading 135.01 deg 유지
  - lat/lon만 RKSS 값으로 사용하고 psi를 90.0 deg로 강제
- 최종 선택:
  - lat/lon은 기존 RKSS 초기조건의 37.5707083333, 126.7782777778을 사용하고 psi는 90.0 deg로 강제
- 선택 이유:
  - 사용자가 lat, lon만 김포공항을 쓰고 고도 450 m에서 heading이 동쪽이라고 명확히 정정함
- 영향 범위:
  - scripts/c172x_4x75kg_cg_aligned/initial_condition/6.0__gimpo_450m_east_60ms_init.xml
- 장점:
  - 사용자 의도와 일치
  - body u=60 m/s가 local east velocity 60 m/s로 매핑됨
- 단점:
  - 실제 RKSS 활주로 방향과는 일치하지 않음
- 검증 결과:
  - JSBSim console 및 CSV에서 초기 v-east 196.850394 ft/s, yaw 90.0 deg 확인
- 남은 리스크:
  - terrain elevation은 지면 접촉 검출을 위해 기존 38 ft를 유지했으므로 ASL altitude 출력은 450 m + 38 ft로 나타남

## [2026-07-19 23:50] DECISION-20260719-2350-001 — DONE

- 문제:
  - '추력을 아예 없애는' 조건을 runscript 제어만으로 처리할지, 별도 aircraft variant로 처리할지 결정 필요
- 고려한 대안:
  - 기존 c172x_4x75kg_cg_aligned에서 throttle/magneto/starter만 0으로 유지
  - engine/thruster를 제거한 별도 c172x_4x75kg_cg_aligned_zeroprop aircraft 생성
  - zero-thrust dummy engine/thruster 추가
- 최종 선택:
  - engine/thruster를 제거한 별도 c172x_4x75kg_cg_aligned_zeroprop aircraft 생성
- 선택 이유:
  - 기존 aircraft는 engine-off 명령에도 fixed-pitch propeller transient로 초반 propeller rpm 및 thrust가 발생함
  - engine/thruster 제거 방식은 기존 c172x_noengine 패턴과 일치하며 propeller rpm/thrust property 자체를 제거함
  - zero dummy engine/thruster는 thrust table/propeller dynamics에 따라 다시 비의도 출력이 생길 수 있음
- 영향 범위:
  - aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop/
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop/
  - scripts/c172x_4x75kg_cg_aligned_zeroprop/
- 장점:
  - 전 구간 thrust/rpm 0 조건을 명확히 만족
  - 75 kg x 4명 질량 조건과 기존 FCS/autopilot 유지
- 단점:
  - 실제 C172 engine-out 상태의 windmilling prop drag는 제거됨
  - fcs/throttle-cmd-norm 등 propulsion 연동 property가 catalog에서 사라져 runscript와 검증 출력에서 별도 처리가 필요함
- 검증 결과:
  - 6.0.2 및 6.1.1이 JSBSim runner에서 정상 실행
  - SI CSV에서 thrust_lbs, engine_rpm, propeller_rpm 모두 0.0
  - raw CSV에는 propulsion/engine 및 propeller property가 존재하지 않음
- 남은 리스크:
  - 분석 목적이 실제 engine-out windmilling drag라면 기존 propeller-installed 조건도 함께 비교해야 함
- 기존 결정과의 관계:
  - TASK-20260719-2335-001의 기존 4x75kg powered variant 기반 runscript를 보완하는 별도 no-propulsion 조건임


## [2026-07-20 09:20] DECISION-20260720-0920-001 ? DONE

- ??:
  - ?? plots ??? ? ?? plotting ??? ?? ? ?? ?? ?? ??
- ??? ??:
  - ?? plots ??? ??
  - ?? plots ??? ???? ploting ??? ??
  - CSV? plot? ?? logs ??? ?? ??
- ?? ??:
  - ?? plots ??? ????, ? ?? plot? ploting/<aircraft>/<run_id>/ ??? ?? ??
- ?? ??:
  - ?? workflow? ??? ?? ???? ????? ???? ??? aircraft/run? ?? ??? ??? ? ??
  - run_id ???? ??? ??? ?? scenario ?? ?? ??? ???? ??
- ?? ??:
  - scripts/run_jsbsim_timestamped.py
  - ploting/ ??? ??
- ??:
  - ?? ?? plot ???? ? ?? ?? ??? ??? ??
  - ??? ??? ??? ???
- ??:
  - ?? ???? plots? ploting ??? ???? ???? ?? ?? ???
- ?? ??:
  - zero-prop 6.1 run?? ploting/<aircraft>/<run_id>/ ?? 307? PNG ?? ??
- ?? ???:
  - ploting ??? ??? ??? ?? ??? ???? spelling? plotting? ??

## [2026-07-20 09:20] DECISION-20260720-0920-002 ? DONE

- ??:
  - runscript event marker ?? ?? ?? ??
- ??? ??:
  - ?? ???? ?? event ??
  - ?? event?? ??
  - ?? ?? event? 2? ??? ?? ??
- ?? ??:
  - console log?? ?? ??? event? 2? ??? ?? ?? ???? E-label legend? ??
- ?? ??:
  - ???? ?? ???? ?? ???? ??? ??? ??
  - ?? ???? ?? event? template ???? ???? ?? ???? ??
- ?? ??:
  - parse_event_markers
  - add_event_lines
  - events.csv
- ??:
  - ??? clutter ??
  - ?? ?? ?? ???? marker ??
- ??:
  - ???? ?? ?? ???? ???? ???? ??
- ?? ??:
  - 6.1.2 run?? E0 0.008333, E2 137.15? events.csv? ???
- ?? ???:
  - console log ??? ??? event parser? ?? ??

## [2026-07-20 09:30] CORRECTION-20260720-0930-001 — 정정

- 대상 기록:
  - DECISION-20260720-0920-001
  - DECISION-20260720-0920-002
- 정정 이유:
  - 09:20 결정 기록 append 중 PowerShell stdin 인코딩 문제로 한글이 손상될 가능성이 있어 한글 정정본을 재기록함
- 기존 내용:
  - 상세 plotting 폴더 구조 및 이벤트 표시 기준 결정
- 정정 내용:
  - 기존 plots/ 요약 산출물은 유지하고, 새 상세 plot은 ploting/<aircraft>/<run_id>/ 하위에 추가 저장하기로 결정함
  - ploting 철자는 사용자 요청을 그대로 따른 것임
  - 이벤트 표시는 console log에서 실제 실행된 이벤트를 기준으로 하며, 이벤트가 2개 이상일 때만 빨간 세로선과 E0, E1, E2 legend를 표시하기로 결정함
- 영향 범위:
  - scripts/run_jsbsim_timestamped.py
  - ploting/ 산출물 구조
- 검증 결과:
  - zero-prop 6.1.2 run에서 events.csv에 E0,0.008333 및 E2,137.15가 기록됨
  - 상세 PNG 307개 생성 확인
- 다음 작업:
  - console log 형식 변경 시 event parser 조정

## [2026-07-20 10:00] DECISION-20260720-1000-001 — DONE

- 문제: ECI/ECEF 절대 위치 그래프가 수백만 단위 기준값에 작은 변화량을 더한 형태라 Matplotlib이 +3.868e6 같은 y축 offset을 표시해 해석성이 낮아짐
- 고려한 대안: 모든 위치 축을 plain number로 강제 표시, 위치 축을 10^n scale로 나눠 표시, ECI/ECEF 절대 위치만 초기값 기준 delta로 변환
- 최종 선택: ECI/ECEF 절대 위치는 초기값 기준 delta로 표시하고 y축 offset/scientific offset은 비활성화
- 선택 이유: 비행 동역학 해석에서는 절대 지구 중심 좌표값보다 시간에 따른 변화량이 더 직접적이고, 사용자가 지적한 +3.868e6 offset 문제를 원천적으로 제거함
- 영향 범위: ploting 폴더에 생성되는 개별 time series와 6dof 2중 y축 그래프
- 장점: y축 tick이 수십에서 수백 m 또는 ft 변화량으로 직접 표시되어 그래프 판독성이 개선됨
- 단점: 절대 ECI/ECEF 좌표값 자체를 그래프에서 바로 읽을 수는 없고 제목/축 라벨의 delta 표기를 확인해야 함
- 검증 결과: eci_z_m helper 변환과 기존 6.1.2 CSV 기반 ploting 재생성 통과
- 남은 리스크: eci/ecef가 아닌 다른 절대 위치 property는 추후 패턴 확장이 필요할 수 있음

## [2026-07-20 10:57] DECISION-20260720-1057-001 — PROPOSED

- 문제:
  - c1723.xml 기반으로 C172X 4x75kg 4명 탑승 정상 이륙 스크립트를 만들 때 기존 51 kt autopilot rotate 방식을 그대로 쓸지, 문헌 V-speed 기반 상태 기계로 바꿀지 결정 필요
- 고려한 대안:
  - c1723.xml을 거의 그대로 복사하고 aircraft만 c172x_4x75kg_cg_aligned로 교체
  - 기존 workflow 5.6 계열 상태 기계를 유지하면서 Vr/Vy 등 속도 기준을 문헌값으로 정리
  - short-field/soft-field 절차처럼 10 deg flap과 Vx climb을 기본으로 사용
- 최종 선택:
  - 정상 이륙용 기본안은 c172x_4x75kg_cg_aligned, flap 0 deg, Vr 55 KIAS, initial climb Vy 76 KIAS 중심의 상태 기계 runscript로 구성
- 선택 이유:
  - Purdue C172 자료가 Vr 55 KIAS, Vx 60 KIAS, Vy 76 KIAS를 직접 제공함
  - N13701 PDF는 mph IAS 기준으로 normal takeoff 0 deg flaps, Vr 60 MPH, Vy 91 MPH를 제시하며 knots로 환산하면 약 Vr 52 kt, Vy 79 kt라 Purdue 값과 크게 충돌하지 않음
  - JSBSim runscript 조건은 velocities/vc-kts를 쓰므로 KIAS 기준으로 통일하는 것이 실행 및 로그 검증에 명확함
  - c1723.xml의 51 kt altitude-hold activation은 정상 조종 절차라기보다 예제용 autopilot 유도에 가까움
- 영향 범위:
  - 신규 runscript 파일 1개
  - 필요 시 workflow Excel 또는 runner 등록 1건
- 장점:
  - 문헌 V-speed와 JSBSim 조건식이 직접 대응됨
  - 기존 workflow 상태 기계와 출력 검증 관례를 유지할 수 있음
  - normal takeoff와 short-field/soft-field 옵션을 분리할 수 있음
- 단점:
  - elevator command 값은 JSBSim 모델 튜닝값이라 실제 POH 수치가 아님
  - 4x75kg 탑승 조건에서 성능 검증을 위해 시뮬레이션 후 elevator ramp와 target speed 조정이 필요할 수 있음
- 검증 결과:
  - 설계 검토 단계라 실행 검증은 미수행
- 남은 리스크:
  - 실제 c172x_4x75kg_cg_aligned가 연료량까지 포함해 최대 이륙중량 제한 안에 있는지 실행 로그 weight 확인 필요

## [2026-07-20 11:31] DECISION-20260720-1131-001 — DONE

- 문제:
  - 500 m AGL 도달 후 30초 cruise를 정확히 종료하기 위한 이벤트 조건 구성
- 고려한 대안:
  - simulation/cruise-timer-sec를 FG_RAMP로 30초 동안 증가
  - STATE 6 이벤트에 delay 30.0 사용
  - 1000 ft 기존 조건 유지
- 최종 선택:
  - STATE 5에서 cruise-active를 켜고 STATE 6에 delay 30.0을 적용
  - 1000 ft 기준은 제거하고 500 m AGL 기준으로 변경
- 선택 이유:
  - FG_RAMP 방식은 초기 실행에서 cruise 시작 후 약 79초 뒤 STATE 6가 실행되어 30초 cruise 요구와 맞지 않았음
  - JSBSim runscript의 delay가 이벤트 시작 후 고정 시간 대기 조건을 더 직접적으로 표현함
  - 사용자가 500 m까지 상승 후 같은 방향 30초 cruise를 명시함
- 영향 범위:
  - 신규 5.8 runscript 내부 이벤트 조건
- 장점:
  - cruise 지속 시간이 로그에서 30.008334 s로 직접 검증됨
  - 기존 5.6/5.6.1 파일을 건드리지 않음
- 단점:
  - altitude hold capture는 JSBSim autopilot 응답에 의존하므로 정확히 500.000 m에 고정되지는 않음
- 검증 결과:
  - run 5.8.3에서 cruise 구간 고도 496.507421-510.553112 m AGL 확인
  - 최종 고도 502.669138 m AGL 확인
- 남은 리스크:
  - 더 엄격한 altitude tolerance가 필요하면 autopilot gain 또는 throttle/altitude capture 조건 추가 튜닝 필요

## [2026-07-20 11:47] DECISION-20260720-1147-001 — DONE

- 문제:
  - event marker가 legend 안에 E0-E6으로 들어가 그래프 중앙을 가리고, 각 이벤트가 어느 점선인지 직관적으로 보이지 않음
- 고려한 대안:
  - legend를 그래프 밖으로만 이동
  - 점선 옆에 event label만 추가
  - 그래프 상단에 event label, time, 구간 rail을 함께 표시
- 최종 선택:
  - event는 legend에서 제외하고, 각 점선 위에 E label과 time을 표시하며, 이벤트 사이 구간은 상단 rail로 표시
  - dual-axis plot의 데이터 legend는 오른쪽 바깥으로 이동
- 선택 이유:
  - 그래프 내부 데이터 영역을 가리지 않으면서 사용자가 E0/E1 위치를 직접 읽을 수 있음
  - 사용자가 제시한 막대 그래프 형태처럼 상단에 구간 경계가 분리되어 보임
- 영향 범위:
  - scripts/run_jsbsim_timestamped.py로 생성되는 상세 ploting time-series 및 sixdof dual-axis PNG
- 장점:
  - 데이터 선, event 경계, legend가 서로 겹칠 가능성이 줄어듦
  - events.csv와 PNG의 event label이 직접 대응됨
- 단점:
  - 이벤트가 매우 촘촘하면 상단 label lane이 여전히 가까워 보일 수 있음
- 검증 결과:
  - python3 -m py_compile 통과
  - 기존 5.8.3 데이터로 상세 ploting 재생성 완료
  - PIL 기반 PNG 확인에서 상단 red marker 영역과 오른쪽 legend 영역 픽셀 존재 확인
- 남은 리스크:
  - view_image 도구가 WSL/Windows 경로 모두 샌드박스 오류를 내서 사람이 직접 보는 방식의 도구 검증은 수행하지 못함

## [2026-07-20 11:52] DECISION-20260720-1152-001 — DONE

- 문제:
  - event label과 구간 rail을 본 axes transform 위에 그리면 title과 가까운 이벤트 라벨이 겹치거나 시각적으로 복잡해짐
- 고려한 대안:
  - 상단 여백만 더 키우기
  - label fontsize 축소
  - 별도 event strip subplot 도입
- 최종 선택:
  - 별도 event strip subplot을 도입하고, 본 plot에는 점선만 남김
- 선택 이유:
  - title, event label, 구간 rail, 데이터 선이 각자 다른 영역을 사용해 충돌 가능성이 구조적으로 줄어듦
  - 사용자가 제안한 막대 그래프 상단 구간 표시 방식에 더 가까움
- 영향 범위:
  - scripts/run_jsbsim_timestamped.py의 상세 ploting time-series 및 dual-axis 출력
- 장점:
  - E0/E1처럼 가까운 이벤트도 3개 label lane 안에서 분리 표시됨
  - 본 plot 위쪽이 event annotation으로 침범되지 않음
- 단점:
  - 이미지 높이가 기존 642 px에서 약 836 px로 증가함
- 검증 결과:
  - python3 -m py_compile 통과
  - 기존 5.8.3 데이터로 상세 ploting 재생성 완료, layout warning 없음
  - from_start_neu_u_m.png 크기 1451x836, 상단 strip red pixel 6414개, strip/plot 사이 red pixel 1개 확인
- 남은 리스크:
  - 실제 육안 확인은 view_image 샌드박스 오류 때문에 사용자가 생성 PNG를 열어 확인해야 함

## [2026-07-20 12:04] DECISION-20260720-1204-001 — SUPERSEDED

- 대상 기존 결정:
  - DECISION-20260720-1152-001
- 교체 이유:
  - 사용자가 구간 표시가 아니라 이벤트 시작 지점만 표시하길 원한다고 정정함
- 기존 방식:
  - 별도 event strip subplot에 E label/time과 E0-E1 구간 rail 표시
- 신규 방식:
  - 별도 event strip subplot에 이벤트 시작 지점의 vertical marker와 E label만 표시
  - 본 plot에는 동일한 event vertical dashed line만 표시
- 고려한 대안:
  - 기존 구간 rail 유지
  - time text만 제거
  - event strip 전체 제거
- 영향 범위:
  - scripts/run_jsbsim_timestamped.py 상세 ploting 출력
- 검증 결과:
  - python3 -m py_compile 통과
  - 기존 5.8.3 상세 ploting 재생성 완료
  - 코드에서 hlines, start_label, end_label, time_s:.1f 잔여 항목 없음 확인
- 남은 리스크:
  - 가까운 이벤트 E0/E1은 label lane으로 분산되지만, 이벤트가 더 많으면 lane 수 추가가 필요할 수 있음

## [2026-07-20 12:12] DECISION-20260720-1212-001 — SUPERSEDED

- 대상 기존 결정:
  - DECISION-20260720-1204-001
- 교체 이유:
  - event 시작점 label만 남겼지만 label box 때문에 가까운 이벤트가 여전히 겹쳐 보임
- 기존 방식:
  - 별도 event strip에 box가 있는 E label 표시
- 신규 방식:
  - 별도 event strip에 box 없는 E label과 vertical start marker만 표시
  - from_start/distance_from_start 위치 계열은 표시 시 첫 값을 빼서 0 시작으로 보정
  - 양수 time-series 축은 기본 x/y 원점을 0으로 고정
- 고려한 대안:
  - label box 유지 및 lane 수 증가
  - event label 자체 제거
  - 시간 텍스트 재도입
- 영향 범위:
  - scripts/run_jsbsim_timestamped.py 상세 ploting 출력
- 검증 결과:
  - py_compile 통과
  - 기존 5.8.3 ploting 재생성 완료
- 남은 리스크:
  - 시각적 취향에 따라 E label을 더 작게 하거나 marker만 남기는 추가 조정 가능


## [2026-07-20 12:21] DECISION-20260720-1221-001 — SUPERSEDED

- 대상 기존 결정:
  - DECISION-20260720-1212-001
- 교체 이유:
  - box 없는 E label도 가까운 이벤트에서 여전히 겹쳐 보일 수 있음
- 기존 방식:
  - 별도 event strip에 box 없는 E0, E1 label과 vertical start marker 표시
- 신규 방식:
  - event 시작점 label은 0, 1, 2처럼 숫자만 사용하고 빨간 원형 marker 안에 표시
- 고려한 대안:
  - E0, E1 유지 후 lane만 늘리기
  - event time text를 다시 추가하기
  - 숫자만 원형 marker로 표시하기
- 영향 범위:
  - scripts/run_jsbsim_timestamped.py 상세 ploting 출력
  - events.csv label 값
- 장점:
  - label 폭을 최소화하면서 event start 순서를 유지할 수 있음
  - 그래프 본문 영역을 침범하지 않음
- 단점:
  - 숫자만으로는 event 의미를 알 수 없으므로 console log 또는 runscript와 함께 봐야 함
- 검증 결과:
  - Python 문법 검사 통과
  - 기존 5.8.3 events.csv label 0..6 확인
  - sample PNG 상단 red pixel 존재 확인
- 남은 리스크:
  - 매우 가까운 event는 marker 원 자체가 일부 겹칠 수 있음


## [2026-07-20 12:31] DECISION-20260720-1231-001 — SUPERSEDED

- 대상 기존 결정:
  - DECISION-20260720-1221-001
- 교체 이유:
  - 숫자 원형 marker를 lane으로 분산하면 marker 기준 높이가 제각각이라 사용자가 원하는 표현과 다름
- 기존 방식:
  - 숫자 원형 marker를 3개 lane에 분산 배치
- 신규 방식:
  - 모든 숫자 원형 marker를 event strip의 동일 y 위치에 배치
  - marker center y를 vertical dashed line ymax와 동일한 0.96으로 맞춤
- 고려한 대안:
  - lane 분산 유지
  - 겹치는 marker만 선택적으로 offset
  - 모든 marker를 같은 높이로 정렬
- 최종 선택:
  - 모든 marker를 같은 높이로 정렬
- 선택 이유:
  - 사용자가 점선 끝 가운데에 맞춰 모두 올리는 표현을 명시함
  - event start 위치를 한 기준선에서 읽기 쉬움
- 영향 범위:
  - 상세 ploting event strip 표시
- 검증 결과:
  - 코드 파일 diff check 통과
  - py_compile 통과
  - 기존 5.8.3 ploting 재생성 완료
- 남은 리스크:
  - 매우 가까운 event marker는 같은 높이에서 일부 겹칠 수 있음


## [2026-07-20 12:45] DECISION-20260720-1245-001 — 결정

- 문제:
  - dual-axis plot의 legend가 오른쪽 바깥에 있어 오른쪽 y축 label과 함께 보기 불편함
- 고려한 대안:
  - 오른쪽 바깥 legend 유지 후 더 멀리 배치
  - plot 내부 상단/하단에 legend 배치
  - x축 제목 아래 중앙에 legend 배치
- 최종 선택:
  - dual-axis plot legend를 x축 제목 아래 중앙에 세로 1열로 배치
- 선택 이유:
  - 사용자가 x축 제목 아래 배치를 명시함
  - 오른쪽 y축 label과 legend 간 시각 충돌을 제거함
  - 오른쪽 여백을 줄여 plot 본문 폭을 넓힐 수 있음
- 영향 범위:
  - sixdof_dual_axis plot PNG
- 장점:
  - 오른쪽 y축 label 가독성 개선
  - plot 본문 영역 확장
- 단점:
  - 아래쪽 figure 높이 사용량이 증가함
- 검증 결과:
  - py_compile 통과
  - 코드 파일 diff check 통과
  - 기존 5.8.3 상세 ploting 재생성 완료
- 남은 리스크:
  - legend label이 매우 길면 아래쪽에서 좌우 폭에 가까워질 수 있음


## [2026-07-20 21:52] DECISION-20260720-2152-001 — 결정

- 문제:
  - Time Notify 제거 실험을 위해 원본 c1723_run.xml을 직접 수정할지 여부
- 고려한 대안:
  - 원본 c1723_run.xml에서 직접 Time Notify 제거
  - 별도 runscript 복사본 생성 후 Time Notify만 제거
- 최종 선택:
  - c1723_no_time_notify_run.xml 별도 파일 생성
- 선택 이유:
  - 원본 동작을 보존하면서 제거 효과를 비교할 수 있음
  - 사용자가 원하면 원본과 no-time-notify 버전을 병렬 유지 가능
- 영향 범위:
  - scripts/c172x/runscript/c1723_no_time_notify_run.xml 신규 파일
  - c1723_no_time_notify 실행 로그 및 ploting 산출물
- 장점:
  - 원본 회귀 위험 없음
  - 삭제 범위가 Time Notify block으로 한정됨
- 단점:
  - runscript 파일이 하나 추가됨
- 검증 결과:
  - console End 확인
  - Time Notify 없는 event list 확인
- 남은 리스크:
  - wrapper command timeout으로 최종 runner stdout summary는 확보하지 못함


## [2026-07-20 22:10] DECISION-20260720-2210-001 — 결정

- 문제:
  - sixdof_raw에는 total speed vt-fps가 직접 없지만, 고도-총속도 및 총속도-RPM 진단 plot이 필요함
- 고려한 대안:
  - sixdof output property에 velocities/vt-fps를 새로 추가하고 재시뮬레이션
  - 기존 v-north/east/down 또는 u/v/w 성분으로 total speed를 후처리 계산
  - SI CSV의 v_total_mps를 sixdof_dual_axis에 섞어 사용
- 최종 선택:
  - sixdof_raw 내부 성분으로 derived/v-total-fps를 계산
- 선택 이유:
  - 기존 로그만으로 plot을 재생성할 수 있음
  - sixdof_dual_axis가 동일 source인 sixdof_raw 기반으로 유지됨
  - total speed 정의가 속도 벡터 크기라 성분 제곱합으로 계산 가능함
- 영향 범위:
  - sixdof_dual_axis plot 생성 로직
  - 신규 altitude_vs_total_speed.png 및 total_speed_vs_engine_propeller_rpm.png
- 장점:
  - 재시뮬레이션 없이 기존 결과 재처리 가능
  - propulsion RPM과 비행 속도 응답을 한 화면에서 비교 가능
- 단점:
  - derived series가 원본 CSV header에는 없음
- 검증 결과:
  - py_compile 및 diff check 통과
  - 두 기존 케이스에서 신규 PNG 생성 확인
- 남은 리스크:
  - 필요 시 향후 sixdof output property에 velocities/vt-fps를 직접 추가할 수 있음


## [2026-07-21 09:11] DECISION-20260721-0911-001 — 결정

- 문제:
  - 요청된 4개 dual-axis pair 중 일부 property가 기존 sixdof_raw CSV에 없음
- 고려한 대안:
  - sixdof_raw에 있는 property만 사용
  - raw CSV와 sixdof_raw CSV를 병합해 dual plot source로 사용
  - 모든 케이스를 재실행해 sixdof_raw만으로 처리
- 최종 선택:
  - 기존 로그 재활용을 위해 raw CSV와 sixdof_raw CSV를 병합하고, future output property도 보강
- 선택 이유:
  - 기존 5.8.3 결과에서도 가능한 plot을 바로 생성할 수 있음
  - 향후 실행부터 rudder-cmd-norm도 기록되어 4개 pair가 모두 생성됨
- 영향 범위:
  - sixdof_dual_axis plot 생성 로직
  - future raw/sixdof output property set
- 장점:
  - 기존 로그 재처리 가능
  - 표 기반 분석 목적에 맞는 plot 이름으로 산출물 생성
- 단점:
  - 과거 로그에 존재하지 않는 rudder-cmd-norm은 backfill 불가
- 검증 결과:
  - 신규 5.8.4 실행에서 요청 4개 PNG 모두 생성 확인
- 남은 리스크:
  - raw와 sixdof_raw time vector 길이가 다르면 raw 병합은 생략됨

## [2026-07-21 13:18] DECISION-20260721-1318-001 — F450 원본 테스트 스크립트 workflow 편입 방식

- 문제:
  - JSBSim source tree의 /home/junyeopkwon/jsbsim/scripts/Test_F450_Launch.xml를 jsbsim_workflow에서 실행 가능하게 추가해야 함
- 고려한 대안:
  - 원본 XML을 수정해 workflow 전용 간소화 runscript로 재작성
  - 원본 XML을 workflow scripts/F450/runscript 아래에 그대로 복사하고 runner가 use initialize와 output을 생성하도록 둠
  - 기존 scripts/F450/runscript/1.0__ground_launch_scas_run.xml를 덮어씀
- 최종 선택:
  - 원본 Test_F450_Launch.xml를 scripts/F450/runscript/1.1__test_f450_launch_run.xml로 그대로 복사해 별도 케이스로 추가
- 선택 이유:
  - 사용자가 확인한 원본 스크립트와의 대응 관계가 명확함
  - 기존 1.0 ground_launch_scas 및 2.0 nominal_mission_profile 케이스를 보존함
  - run_jsbsim_timestamped.py가 실행 시 use aircraft와 initialize 및 output을 자동으로 workflow 경로에 맞게 재작성하므로 원본 구조를 유지해도 실행 가능함
- 영향 범위:
  - F450 workflow runscript 선택지 및 새 실행 산출물에 한정됨
- 장점:
  - 원본 JSBSim 테스트와 diff 없는 복사본으로 추적 가능
  - 기존 workflow 실행 규칙과 버전 명명 규칙을 따름
- 단점:
  - workflow runner가 output block을 교체하므로 원본 quad_log.csv와 완전히 같은 CSV column은 생성되지 않음
- 검증 결과:
  - 원본과 복사본 diff 없음
  - run_jsbsim_timestamped.py로 1.1.1__test_f450_launch 정상 실행 완료
- 남은 리스크:
  - F450 제어 입력과 로터별 output을 더 세밀하게 분석하려면 runner output property 보강이 필요함
- 기존 결정과의 관계:
  - 기존 scripts/README.md의 aircraft별 initial_condition/runscript 구조와 호환됨


## [2026-07-23 23:30] DECISION-20260723-2330-001 — 결정

- 문제:
  - 제공 full mission bundle을 기존 c172x_4x75kg_cg_aligned에 직접 덮어쓸지, 별도 landing aircraft variant로 분리할지 결정 필요
- 고려한 대안:
  - 기존 c172x_4x75kg_cg_aligned aircraft와 c172ap.xml을 직접 수정
  - 제공 bundle 파일을 원본 그대로 JSBSim에 직접 배치
  - landing 전용 aircraft/scripts 구조를 새로 만들고 workflow runner로 실행
- 최종 선택:
  - c172x_4x75kg_cg_aligned_landing 별도 variant와 scripts 폴더를 생성
- 선택 이유:
  - 기존 5.8 및 c172x_4x75kg_cg_aligned 결과와 동작을 보존
  - landing autopilot gain/gating 변경이 normal takeoff 기존 케이스에 섞이지 않음
  - run_jsbsim_timestamped.py의 aircraft/runscript discovery 구조와 잘 맞음
- 영향 범위:
  - landing variant와 5.9 mission 실행에 한정
  - runner에는 aircraft 이름이 _landing으로 끝날 때만 raw output property를 추가하는 조건부 변경 적용
- 장점:
  - 기존 aircraft 회귀 위험 감소
  - 재실행 경로가 명확함
  - full mission state logging과 기존 plotting pipeline을 함께 활용 가능
- 단점:
  - JSBSim install tree와 workflow aircraft_variants 양쪽에 landing variant를 동기화해야 함
  - 기존 c172x_4x75kg_cg_aligned와 파일 중복이 생김
- 검증 결과:
  - JSBSim catalog load 통과
  - run 5.9.2 mission complete 확인
- 남은 리스크:
  - 향후 landing aircraft XML을 수정할 때 workflow copy와 JSBSim install copy 동기화 절차가 필요


## [2026-07-24 12:55] DECISION-20260724-1255-001 - accepted

- Problem: `5.9` latitude/delay-based recovery completed far from the starting runway axis.
- Decision: Add runway-axis along/cross properties and use them in a new `5.10` runscript.
- Final approach choice: use `180 deg` intercept heading first, then switch to `135.01 deg` runway heading when cross-track approaches centerline.
- Reason: fixed `135.01 deg` final heading alone caused parallel offset flight and late touchdown.
- Validation: `5.10.8` reached `STATE 23`; touchdown cross `-62.4 m`, final cross `-73.6 m`.
- Tradeoff: event tuning is improved but not a robust localizer/PID controller.


## [2026-07-24 15:00] DECISION-20260724-1500-001 - accepted

- Problem: Rectangular loiter used delayed straight legs, producing square-looking turns.
- Considered: direct bank-hold helper vs AP heading-hold continuous heading arc.
- Decision: Keep the bank-hold helper dormant and use AP heading-hold with immediate heading setpoint transitions for `5.11`.
- Reason: direct bank-hold attempt was unstable in `5.11.1`; AP heading-hold preserved stable C172 behavior while removing straight-leg delay.
- Validation: `5.11.2` completed `STATE 23` and produced a continuous left orbit with average bank about `-25.5 deg`.
- Tradeoff: It is a smooth heading-arc orbit, not a mathematically exact radius-hold circle.


## [2026-07-24 20:10] DECISION-20260724-2010-001 - ACCEPTED

- Problem: The provided KSFO `5.13` runscript was nominally using the current landing aircraft but depended on KSFO-specific runway-axis geometry and its traffic-pattern transitions did not land back near the runway start area.
- Considered: Edit the existing RKSS aircraft in place; keep using the same aircraft with KSFO scripts; create a KSFO-specific landing aircraft variant; tune the provided `5.13` procedure directly; rotate the proven RKSS `5.11` procedure to KSFO 28R.
- Decision: Create `c172x_4x75kg_cg_aligned_ksfo28r_landing` and use a rotated/tuned RKSS `5.11` procedure as final `5.16`.
- Reason: Runway-axis monitor coefficients are airport/heading specific, so a separate variant avoids breaking RKSS runs. Direct `5.13` tuning first missed state transitions, then landed too far downrange; rotating the already validated RKSS procedure preserved stable C172 behavior.
- Impact: KSFO missions should use the new aircraft name and script folder; RKSS landing files remain untouched.
- Validation: `5.16.1` reached `STATE 23` with touchdown cross `-33.4 m` and stop cross `-43.5 m`.
- Tradeoff: Procedure is tuned in JSBSim coordinates; FlightGear scenery alignment still needs visual confirmation if FG streaming is required.


## [2026-07-24 21:35] DECISION-20260724-2135-001 - ACCEPTED

- 문제: 기존 no-FG runner는 CSV 생성 후 state/trajectory plot과 detailed `ploting/` 전체를 생성해 테스트 반복 시간이 길다.
- 고려한 대안: 기존 runner에 `--no-plots` 옵션 추가; 기존 runner를 수정; 별도 CSV-only runner 생성.
- 최종 선택: 기존 파일은 보존하고 `run_jsbsim_timestamped_no_fg_prompt_csv_only.py`를 별도 생성.
- 선택 이유: 기존 plotting 포함 workflow와 호환성을 깨지 않고, 필요할 때 빠른 CSV-only 실행 경로를 명확히 분리할 수 있다.
- 영향 범위: 새 runner 파일만 추가. 기존 runner 동작은 변경하지 않음.
- 장점: 테스트 반복 속도 개선, 기존 plotting workflow 보존.
- 단점: 일부 코드 중복과 미사용 plotting 함수 정의가 새 파일에 남음.
- 검증 결과: KSFO 5.16 실행에서 CSV 4종 생성, plot/ploting 결과 미생성 확인.
- 남은 리스크: 장기적으로는 공통 로직을 모듈화하지 않으면 runner 두 개의 유지보수 중복이 생길 수 있음.

## [2026-07-25 14:44] DECISION-20260725-1444-001 — 결정

- 문제:
  - Downloads의 LiftCruise2kg 패키지를 그대로 실행하면 JSBSim root 기준 aircraft/engine lookup 및 Aero.xml tableData 형식 문제로 workflow 실행이 불가능함
- 고려한 대안:
  - 원본 Downloads 폴더를 직접 수정
  - JSBSim source tree에만 aircraft를 직접 설치
  - 원본은 보존하고 workflow aircraft variant와 JSBSim install copy를 따로 생성
- 최종 선택:
  - 원본 Downloads 폴더는 보존하고 jsbsim_workflow/aircraft_variants/LiftCruise2kg, scripts/LiftCruise2kg, /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg에 workflow용 copy를 생성
- 선택 이유:
  - 기존 workflow의 aircraft별 scripts 구조와 맞음
  - 원본 사용자가 구성한 패키지를 비교 기준으로 남길 수 있음
  - JSBSim engine 파일은 /home/junyeopkwon/jsbsim/engine에 있으므로 JSBSim root install 방식이 가장 단순함
- 영향 범위:
  - 새 LiftCruise2kg aircraft와 scripts 추가에 한정
  - 기존 C172/F450/ADS workflow 파일은 수정하지 않음
- 장점:
  - workflow runner에서 비대화식 재실행 가능
  - 원본 대비 수정 차이가 dm_config version과 Aero.xml tableData 형식으로 제한됨
- 단점:
  - workflow copy와 JSBSim install copy를 동기화해야 함
  - 제어 성능 검증 및 튜닝은 별도 작업으로 남음
- 검증 결과:
  - XML, catalog, CSV-only runner 실행 통과
- 남은 리스크:
  - hover mission 궤적 품질과 LiftCruise 전용 output property 보강 필요
- 기존 결정과의 관계:
  - C172 landing variant를 원본 보존 방식으로 workflow/install copy 분리한 기존 결정과 같은 패턴

## [2026-07-25 14:48] CORRECTION-20260725-1448-001 — 정정

- 대상 기록:
  - DECISION-20260725-1444-001
- 정정 이유:
  - PowerShell 백틱 이스케이프 처리로 일부 식별자가 제어문자로 표시될 수 있어, 결정 내용을 plain text로 재기록함
- 정정 내용:
  - 결정은 원본 Downloads 폴더를 수정하지 않고 workflow copy와 JSBSim install copy를 별도로 생성하는 것이다.
  - 최종 경로는 /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg, /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg, /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg 이다.
  - 이 방식은 기존 C172 landing variant처럼 원본 보존과 workflow 재실행성을 동시에 확보한다.
  - 단점은 workflow copy와 JSBSim install copy를 동기화해야 하고, hover 제어 성능 검증은 별도 작업으로 남는다는 점이다.
- 영향 범위:
  - 기록 가독성 정정만 해당하며 실제 코드/XML/실행 결과 변경 없음
- 검증 결과:
  - XML, catalog, CSV-only runner 실행 통과 기록 유지
- 다음 작업:
  - LiftCruise2kg hover 제어 품질 튜닝

## [2026-07-25 15:09] DECISION-20260725-1509-001 — 결정

- 문제:
  - 사용자 지정 10 m 좌표 시퀀스를 기존 1.0 hover mission에 덮어쓸지 별도 runscript로 보존할지 결정 필요
- 고려한 대안:
  - 기존 1.0__hover_mission_run.xml 직접 수정
  - 새 1.1 runscript로 추가
- 최종 선택:
  - 새 1.1__ten_meter_box_hover_land_run.xml 추가
- 선택 이유:
  - 기존 1.0 결과와 비교 가능성을 보존
  - workflow version convention에서 같은 mission family의 변형으로 관리 가능
  - 사용자가 지정한 새 시퀀스를 선택 가능한 독립 케이스로 남길 수 있음
- 영향 범위:
  - LiftCruise2kg scripts 폴더에 한정
- 검증 결과:
  - XML 문법 및 CSV-only runner 실행 통과
- 남은 리스크:
  - 실제 위치 추종은 제어기 튜닝 전까지 요청 좌표를 정확히 따라가지 않음

## [2026-07-25 16:12] DECISION-20260725-1612-001 - ACCEPTED
- 문제: runner가 원본 runscript output을 제거해 XML과 raw CSV가 불일치함
- 선택: LiftCruise2kg에 한해 템플릿 output property와 rate를 raw CSV output에 그대로 사용
- 이유: C172/F450 기존 공용 CSV 동작은 유지하면서 LiftCruise 분석 로그만 원본 XML 기준으로 추적 가능
- 추가 결정: simulation/mission-state는 JSBSim raw CSV 헤더에서 드롭되어 output 목록에서 제외하고 console notify로 확인
- 검증: 1.1.4 실행에서 source XML, generated XML, raw CSV property 수와 순서 일치
- 남은 리스크: mission-state를 CSV 컬럼으로 반드시 쓰려면 모델 카탈로그에 해당 property를 정의하는 별도 작업 필요

## [2026-07-25 17:56] DECISION-20260725-1756-001 - F450 AP 연결 방식

- 문제: LiftCruise2kg AP는 자체 multicopter mixer가 AP command를 직접 소비하지만 F450은 기존 FlightControl.xml rate-SCAS가 fcs command 입력을 받음
- 고려한 대안: F450 mixer를 LiftCruise 방식으로 대체, F450 FlightControl.xml에 AP switch 삽입, F450AP.xml에서 F450 command output bridge 추가
- 최종 선택: F450AP.xml을 새로 두고 AP output을 F450 기존 FCS 입력 property로 내보내는 bridge channel을 추가
- 선택 이유: 기존 F450 mixer/SCAS 변경을 피하면서 AP 기능 시험 범위를 좁힐 수 있음
- 영향 범위: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml, /home/junyeopkwon/jsbsim/aircraft/F450/F450.xml, F450 workflow runscript 및 raw output
- 장점: F450 aircraft catalog와 runner 실행 경로에서 AP/SCAS 연결 상태를 직접 확인 가능
- 단점: F450 기존 SCAS가 rate command 중심이라 LiftCruise AP lateral controller를 그대로 쓰면 10 m box 추종 품질이 낮음
- 검증 결과: catalog load 및 CSV-only run 1.2.9 정상 종료
- 남은 리스크: lateral hold는 별도 제어기 설계와 tuning이 필요

## [2026-07-25 17:56] DECISION-20260725-1756-002 - F450 mission 종료 시점

- 문제: F450 ground reaction은 disarm 이후 gear contact chatter가 커져 긴 post-landing 구간에서 SIGFPE가 발생할 수 있음
- 고려한 대안: 원본 LiftCruise 210 s terminate 유지, disarm 제거, disarm 직후 205.2 s에서 terminate
- 최종 선택: disarm event는 205.0 s에 유지하고 terminate event를 205.2 s로 앞당김
- 선택 이유: landing/disarm 확인은 유지하면서 post-disarm ground chatter 수치 발산을 피함
- 영향 범위: /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml
- 검증 결과: run 1.2.9 정상 종료
- 남은 리스크: ground reaction model 자체 안정화는 별도 과업

## [2026-07-26 14:10] DECISION-20260726-1410-001 — DONE

- 문제: F450 runscript와 runner 로그가 실제 motor/FCS property를 정확히 기록하지 못하고, mission event가 고정 시간만으로 넘어가 제어 성능 문제를 가림
- 고려한 대안: 기존 시간 기반 전환 유지, 완전 동적 dwell timer 기반 state machine, nominal time 하한과 도착 gate를 결합한 state machine
- 최종 선택: nominal time 하한과 위치/속도/고도 도착 gate를 결합한 state machine을 적용하고, 로그 property는 JSBSim catalog 기준 실제 F450 property로 정정
- 선택 이유: 기존 LiftCruise mission schedule과 비교 가능성을 유지하면서도 기체 도착 여부를 전환 조건에 반영할 수 있음
- 영향 범위: /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml 및 F450 runner 출력 property 목록
- 장점: 시간만으로 넘어가는 문제를 제거하고, 첫 hover holding 실패를 즉시 드러냄
- 단점: hover dwell이 완전한 동적 타이머 방식은 아니며, 늦게 도착한 경우 dwell 시간 보장은 추가 state/timer 설계가 필요함
- 검증 결과: run 1.2.12에서 setpoint가 0,0에 머물러 도착 gate가 첫 leg 진입을 차단하는 것을 확인함
- 남은 리스크: gate가 엄격하면 제어기 튜닝 전에는 mission이 진행되지 않을 수 있음. 현재 결과가 그 사례임
- 기존 결정과의 관계: TASK-20260725-1756-001에서 만든 F450 mission을 유지하되, 전환 조건과 로그 property를 보정함


## [2026-07-26 15:33] DECISION-20260726-1533-001 — 채택

- 문제: F450 10 m hover mission이 이론 XY 경로를 따르지 못하고 yaw 회전 및 원점 통과 후 lateral drift가 발생했다.
- 고려한 대안: 센서 stub/노이즈 원인, runscript 시간 조건 문제, roll/east 부호 반전, lateral gain 축소, heading error wrap, JSBSim distance-from-start-* property 사용 중단
- 최종 선택: heading error wrap과 lateral gain 축소를 유지하고, 위치오차는 초기 위경도 기준 signed local north/east 계산값을 사용한다.
- 선택 이유: 센서 파일은 stub이고 F450AP는 실제 JSBSim state property를 직접 사용하므로 센서 노이즈 원인이 아니다. yaw spin은 0 deg와 360 deg가 같은 방향임에도 naive difference가 약 -2*pi로 계산되는 wrap 문제였다. 또한 position/distance-from-start-lat/lon-mt는 원점 반대편에서 부호 정보를 잃어 AP가 실제 위치를 반대로 해석했다.
- 영향 범위: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml의 hover position hold, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml의 게이트 판정 신뢰성
- 장점: 1.3 hover drift가 54.43 m max에서 0.02 m max로 감소하고, 1.2 미션이 목표 setpoint sequence를 통과한다.
- 단점: 현재 signed local 변환은 44.725801, -93.075866 초기 위치에 고정된 small-angle 근사다.
- 검증 결과: 1.2.19 미션에서 최대 XY 거리 약 9.91 m, 마지막 local_N/E = 0.00/0.00 m.
- 남은 리스크: 다른 초기 위치 또는 큰 이동 거리에서는 longitude scale과 home property를 재계산해야 한다.
- 기존 결정과의 관계: 기존 runscript arrival gate 수정은 유지하되, gate가 참조하는 AP error property의 좌표 계산 방식을 교체했다.


## [2026-07-26 16:46] DECISION-20260726-1646-001 — 채택

- 문제: F450에서 검증한 signed local N/E 수정 방식을 LiftCruise2kg에 단순 복사하면 초기 latitude 체계 차이 때문에 AP 위치오차가 21 km 수준으로 포화된다.
- 고려한 대안: position/lat-geod-deg + geodetic home 사용, position/lat-gc-deg + init latitude home 사용, distance-from-start-* 유지, runscript 시간 조건만 유지
- 최종 선택: LiftCruise2kg는 position/lat-gc-deg와 position/long-gc-deg 기준 signed local N/E를 사용하고, runscript는 도착 조건 기반으로 전환한다.
- 선택 이유: /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/initial_condition/1.0__ground_init.xml의 latitude는 type="geodetic"이 없어서 JSBSim에서 geocentric latitude로 해석된다. raw 로그에서도 초기 lat-gc-deg=44.725801, lat-geod-deg=44.918222로 확인되어 lat-geod-deg에 44.725801 home을 빼면 큰 offset이 생긴다.
- 영향 범위: LiftCruise2kg hover AP position feedback 및 1.1 10 m hover-land mission gate
- 장점: 별도 init 변경 없이 현재 LiftCruise2kg 초기조건과 일관된 local N/E control이 가능하다.
- 단점: latitude type을 geodetic으로 바꾸는 경우 AP 기준도 다시 맞춰야 한다.
- 검증 결과: 1.1.9에서 최대 XY 거리 약 9.94 m, 최종 local_N/E 약 0.02/0.00 m로 미션 통과.
- 남은 리스크: 더 먼 거리 미션에서는 단순 degree-to-meter gain 대신 local tangent plane 변환이 필요하다.
- 기존 결정과의 관계: F450의 signed local N/E 원칙은 유지하되, LiftCruise2kg 초기조건의 latitude type 차이에 맞게 lat-gc-deg를 선택했다.

## [2026-07-29 10:54] DECISION-20260729-1054-001 - 채택

- 문제:
  - 사용자는 c172x 4 x 75 kg occupant, 무추력, 프로펠러 정지, 조종면 neutral 0 고정, alpha 제한 제거 조건의 별도 테스트 모델과 RKSS 14L 500 m MSL drop mission을 원함
- 고려한 대안:
  - 원본 c172x.xml 직접 수정
  - 기존 c172x_4x75kg_cg_aligned_zeroprop 모델 직접 수정
  - 기존 zeroprop 모델을 복사한 새 no-alpha-limit variant 생성
- 최종 선택:
  - c172x_4x75kg_cg_aligned_zeroprop_noalphalimit 새 variant를 workflow와 JSBSim install tree 양쪽에 생성
- 선택 이유:
  - 원본과 기존 zeroprop 결과를 비교 기준으로 보존할 수 있음
  - 기존 4 x 75 kg, no engine/propeller, CG-aligned 구성을 재사용해 변경 범위를 aerodynamics alpha limit과 elevator neutral bias로 제한할 수 있음
  - runner의 aircraft discovery와 output/log 디렉터리 구조가 기존 aircraft folder convention을 따른다
- 영향 범위:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit
- 장점:
  - no-alpha-limit 실험과 기존 alpha-limit 실험을 같은 workflow에서 나란히 실행 가능
  - propulsion/engine catalog가 없어 프로펠러 정지 가정을 명확히 만족
  - elevator actuator bias 제거로 neutral command와 surface deflection이 모두 0으로 일치
- 단점:
  - alphalimits 제거가 공력 table 외삽의 물리 타당성을 자동 보장하지 않음
  - support XML을 복사한 variant라 기존 c172ap 지원 파일과 동기화 책임이 생김
- 검증 결과:
  - XML parse, JSBSim catalog load, CSV-only run 7.0.2 통과
  - run 7.0.2에서 조종면 최대 절대값 0.0 rad, engine/propeller column 없음, ground contact terminate 확인
- 남은 리스크:
  - alpha-limit 유지 baseline과 직접 비교하지 않았으므로 제한 제거 효과는 아직 정량 분리되지 않음
- 기존 결정과의 관계:
  - 기존 C172 variant를 원본 보존 방식으로 별도 aircraft folder에 생성하던 프로젝트 패턴을 유지함

## [2026-07-29 11:20] DECISION-20260729-1120-001 - 채택

- 문제:
  - 기존 7.0 theta 2.5 deg 조건은 초기 속도 벡터가 위쪽 성분을 가져 사용자가 기대한 수평 전진 상태와 다를 수 있음
- 고려한 대안:
  - theta 2.5 deg를 유지하고 wbody를 조정해 gamma 0으로 맞춤
  - theta 0 deg, ubody 60 m/s, wbody 0으로 수평 전진 초기조건 생성
  - JSBSim trim을 사용해 no-thrust steady glide 조건 산출
- 최종 선택:
  - 우선 theta 0 deg, ubody 60 m/s, wbody 0인 7.1 비교 케이스를 생성
- 선택 이유:
  - 사용자의 질문이 theta 2.5가 위를 보는지에 대한 후속이므로, 가장 직접적으로 기수 수평/속도 수평 조건을 분리할 수 있음
  - 기존 7.0을 보존해 그래프 비교가 가능함
- 영향 범위:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit
- 장점:
  - 초기 vertical velocity 원인과 aircraft pitch moment 원인을 분리 가능
- 단점:
  - theta 0은 trim된 무추력 활공 평형이 아니므로 phugoid 자체는 제거되지 않음
- 검증 결과:
  - 7.1 초기 v-down 약 0 m/s에도 hmax 637.64 m까지 상승해 nose-up moment 원인이 지배적임을 확인
- 남은 리스크:
  - 실제 순항 또는 안정 활공을 목표로 하면 trim 조건 산출이 필요함
- 기존 결정과의 관계:
  - 7.0 no-alpha-limit variant는 유지하고 초기조건 비교 run만 추가함

## [2026-07-29 11:25] DECISION-20260729-1125-001 - 채택

- 문제:
  - theta 0 deg에서도 neutral zero-prop C172가 강한 pitch-up moment로 상승하므로 nose-down 초기 자세가 효과가 있는지 확인 필요
- 고려한 대안:
  - 기존 7.1을 직접 theta -5로 수정
  - 7.2 별도 케이스로 분리
  - 바로 elevator trim 또는 Cmo 조정 variant 생성
- 최종 선택:
  - 기존 7.0/7.1을 보존하고 theta -5.0 deg인 7.2 케이스를 추가
- 선택 이유:
  - 초기 자세만 바꿨을 때의 효과를 이전 케이스와 직접 비교할 수 있음
  - 모델 공력/조종면 trim 변경 없이 사용자 요청을 최소 변경으로 검증 가능
- 영향 범위:
  - scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit 및 plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit
- 장점:
  - nose-down 초기 자세의 효과를 정량 비교 가능
- 단점:
  - 초기 자세 조정은 pitch moment 원인 제거가 아니라 초기 상태 보정일 뿐임
- 검증 결과:
  - 7.2 hmax 633.31 m로 7.1보다 약 4.33 m 낮아졌지만 여전히 큰 상승이 남음
- 남은 리스크:
  - 실제 원하는 거동은 trim/elevator/Cmo 조정 없이는 얻기 어려울 수 있음
- 기존 결정과의 관계:
  - 7.1 수평 전진 비교 케이스를 유지하면서 7.2 nose-down 비교 케이스를 추가함

## [2026-07-29 11:42] DECISION-20260729-1142-001 - 채택

- 문제:
  - 사용자는 초기 qdot을 0에 가깝게 만들고 재실행하기를 원함. 기존 조건은 조종면 0 고정이므로 elevator trim 사용은 원래 가정을 깨뜨림
- 고려한 대안:
  - elevator deflection 또는 pitch trim을 주어 moment cancel
  - Cmo를 0으로 바꾼 variant 생성
  - 잔여 moment까지 보간한 Cmo_target variant 생성
- 최종 선택:
  - 조종면 0 가정을 유지하기 위해 Cmo 보정 variant를 별도로 생성하고, 최종적으로 Cmo=-0.01523148을 적용
- 선택 이유:
  - 원본 및 기존 no-alpha-limit 모델을 보존하면서 초기 qdot만 분리 검증 가능
  - elevator를 움직이지 않으므로 조종면 0 고정 조건을 계속 만족
  - Cmo=0 중간 run의 잔여 qdot을 이용해 목표값을 수치적으로 보정할 수 있음
- 영향 범위:
  - 새 cmo0/cmotrimq0 aircraft variants와 scripts/output/logs에 한정
- 장점:
  - 8.1에서 초기 qdot을 -1.13e-7 rad/s^2까지 줄임
  - 초기 고도 상승 피크를 637.64 m에서 500.00 m 수준으로 제거
- 단점:
  - Cmo 변경은 공력 모델 자체 수정이므로 실제성 검증 전에는 실험용 variant로만 해석해야 함
- 검증 결과:
  - XML/catalog/CSV-only run 통과
  - 8.1 초기 m-total -0.000165 lb-ft, 조종면 0 rad 유지
- 남은 리스크:
  - 실제 항공기 trim은 Cmo 변경이 아니라 elevator/trim 및 alpha/speed 조합으로 이뤄지므로, 물리적 해석에는 별도 trim run이 필요
- 기존 결정과의 관계:
  - no-alpha-limit 원본 variant는 유지하고 qdot0 검증용 파생 variant만 추가함

## [2026-07-29 12:05] DECISION-20260729-1205-001 - 결정

- 문제: trim 상태 추락 시작을 no-thrust/no-prop/no-control 조건과 동시에 만족해야 함
- 고려한 대안: JSBSim native do_simple_trim=1, Cmo 보정 variant, elevator trim 위치 actuator bias 고정
- 최종 선택: 원래 Cmo=0.1과 no-alpha-limit 모델을 유지하고 elevator bias 0.092863537532 rad를 고정한 별도 variant 사용
- 선택 이유: native trim은 no-thrust 조건에서 udot/qdot trim 실패, Cmo 보정은 공력 모델 자체를 바꾸므로 사용자 요구와 거리가 있음
- 영향 범위: c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_elevtrimq0 및 9.3 run
- 검증 결과: 9.3 초기 qdot=8.55886e-05 rad/s^2, 고도 피크 500.002631 m
- 남은 리스크: steady glide full trim은 alpha/theta/gamma/elevator 동시 최적화 필요


## [2026-07-31 10:56] DECISION-20260731-1056-001 - ACCEPTED

- 문제: `5.16`은 정상 종료하지만 초반 takeoff/climb offset과 final centerline offset이 FlightGear 화면에서 눈에 띌 수 있다.
- 고려한 대안: 기존 `5.16` 직접 덮어쓰기; autopilot XML 수정; nose steering channel 활성화; 새 runscript 후보를 생성해 mission-level tuning 수행.
- 최종 선택: 기존 `5.16`은 보존하고 `5.22__ksfo28r_centerline_balanced_final_landing_run.xml`를 새 개선본으로 추가.
- 선택 이유: 기체/autopilot 모델 변경은 다른 미션에 영향이 크고, mission-level 조정만으로 takeoff 및 landing centerline 오차가 충분히 개선됐다.
- 영향 범위: KSFO 28R landing script folder에 `5.17`~`5.22` 후보 추가. 기존 `5.16`은 변경하지 않음.
- 장점: 기존 검증 baseline 보존, 개선 수치 비교 가능, FlightGear 테스트 시 바로 `5.22` 사용 가능.
- 단점: 후보 파일이 여러 개 남아 runscript 목록이 늘어난다.
- 검증 결과: `5.22.1` reached `STATE 23`; touchdown cross `-1.5 m`, stop cross `-2.3 m`.
- 남은 리스크: FlightGear 시각 검증은 별도로 필요.

## [2026-07-31 13:55] DECISION-20260731-1355-001 — DONE

- 문제: 로테이트 직후 `STATE 3`에서 altitude hold AP를 즉시 켜면 `ap/elevator_cmd`가 큰 목표고도 오차에 반응해 포화/반전되고, plot상 elevator와 theta가 순간적으로 튀어 보임
- 고려한 대안: 즉시 AP 유지 후 altitude setpoint 단계 상승, AP를 500 m 근처까지 지연, AP를 지연하되 로테이트 elevator를 약화하고 수동 pitch 완화 입력을 추가
- 최종 선택: `5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml`을 현재 추천본으로 선정
- 선택 이유: `5.27.1`은 전체 미션을 `STATE 23`까지 완료하면서 20-35초 `fcs/elevator-pos-rad` range를 `0.376 rad`에서 `0.047 rad`로 줄였고, touchdown cross-track도 `-0.1 m`로 가장 양호함
- 영향 범위: KSFO RWY 28R C172 variant runscript 선택지에 새 파일이 추가됨. 기존 `5.22` 및 이전 파일은 보존됨
- 장점: 로테이트 직후 AP elevator 포화가 사라지고 초기 pitch가 14.4도 수준으로 제한됨
- 단점: 46초 부근 altitude hold 재투입 때 AP transient가 남음
- 검증 결과: CSV-only runner 실행, raw CSV 분석, XML parse, `git diff --check` 통과
- 남은 리스크: FlightGear 외부 FDM 화면에서 체감 부드러움은 별도 확인 필요

## [2026-07-31 15:56] DECISION-20260731-1556-001 — combined CSV runner 분리

- 문제: 기존 runner는 raw, si, sixdof_raw, sixdof_si, ploting 산출물을 나누어 생성해 외부 plot 도구 사용 시 불필요한 후처리와 파일 분산이 발생함
- 고려한 대안: 기존 runner 직접 수정, csv_only runner 수정, 새 combined_csv_only runner 추가
- 최종 선택: 기존 파일은 보존하고 scripts/run_jsbsim_timestamped_combined_csv_only.py를 새로 추가
- 선택 이유: 기존 실행 방식과 사용자의 미추적 파일을 건드리지 않으면서 통합 CSV 실험을 독립적으로 검증할 수 있음
- 영향 범위: 새 runner 사용 시에만 logs/csv/combined 아래 단일 CSV 생성
- 장점: ploting/plots 생성 없음, raw와 sixdof 계열 property를 같은 시간축 CSV 하나에 모음, 기존 runner 회귀 위험 낮음
- 단점: SI 변환 컬럼은 만들지 않고 JSBSim raw property 단위와 이름을 유지함
- 검증 결과: F450 12초 ground launch combined CSV 생성 확인
- 남은 리스크: workflow Excel 자동 갱신은 기본 호출하지 않으므로 필요하면 별도 update_workflow_excel.py 실행 필요

## [2026-07-31 17:23] DECISION-20260731-1723-001 — ACCEPTED

- 문제: 기존 `run_jsbsim_csv_plotter_v6.m`를 직접 수정할지, 새 버전 파일로 확장할지 결정 필요
- 고려한 대안: v6 직접 수정, v7 새 파일 생성, 별도 Python/HTML 리포터 생성
- 최종 선택: `logs/csv/run_jsbsim_csv_plotter_v7.m` 새 파일 생성
- 선택 이유: v6는 사용자가 이미 그래프 생성에 쓰는 안정 버전이므로 보존하고, 발표자료용 자동 export와 summary metrics는 새 버전에서 실험적으로 확장하는 편이 회귀 위험이 낮음
- 영향 범위: `logs/csv/run_jsbsim_csv_plotter_v7.m` 사용 시에만 새 기능이 적용됨. v6 기존 동작은 변경하지 않음
- 장점: 기존 작업 흐름 보존, 새 기능 테스트 용이, 실패 시 v6로 즉시 복귀 가능
- 단점: `logs/`가 `.gitignore`에 포함되어 있어 v7 파일은 Git 추적 대상이 아니며 별도 관리가 필요할 수 있음
- 검증 결과: v7 파일 존재와 핵심 함수/컨트롤 정적 확인 완료
- 남은 리스크: MATLAB GUI 런타임에서 실제 export 동작은 아직 미검증

## [2026-08-10 22:35] DECISION-20260810-2235-001 — ACCEPTED

- 문제: 첨부 DATCOM light_control과 erodynamics를 F450에 적용하면서도 멀티콥터 hover/attitude 제어가 살아 있어야 함
- 고려한 대안: 원본 F450 직접 수정, FlightControl.xml 전체 교체, F450 복제 후 flight control 병합, DATCOM 전체 dm_config를 새 항공기로 사용
- 최종 선택: 원본 F450은 보존하고 F450_DATCOM 파생 aircraft를 생성한다. F450의 propulsion/mass/gear/effectors/autopilot/sensors는 유지하고 DATCOM metrics/aerosurface scale/aerodynamics를 병합한다.
- 선택 이유: FlightControl.xml 전체 교체는 F450 motor mixer와 ESC output을 제거해 hover가 불가능해질 위험이 크다. 파생 모델 방식은 원본 baseline과 동일 미션 비교가 쉽고 회귀 위험이 낮다.
- 영향 범위: /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM, ircraft_variants/F450_DATCOM, scripts/F450_DATCOM
- 장점: 원본 F450 보존, 동일 runscript 비교 가능, DATCOM 공력 property 로그 확인 가능
- 단점: DATCOM geometry가 기존 F450 frame/mass와 물리적으로 완전히 맞는지는 별도 검증 필요
- 검증 결과: JSBSim catalog 로딩 및 F450/F450_DATCOM 70초 동일 미션 실행 성공
- 남은 리스크: DATCOM 
ow+table table 구조는 JSBSim 호환을 위해 
ow+column으로 재구성했으며 숫자 데이터는 유지했지만, 원본 생성기의 의도와 완전 동일한 보간 의미인지는 추가 확인 여지가 있음


## [2026-08-10 22:40] CORRECTION-20260810-2240-001 — 정정

- 대상 기록: TASK-20260810-2235-001, PROGRESS-20260810-2235-001, DECISION-20260810-2235-001, TODO-20260810-2235-001, INDEX-20260810-2235-001
- 정정 이유: PowerShell command string에서 Markdown backtick escape가 적용되어 일부 경로와 row/table 표기가 제어문자로 기록됨
- 기존 내용: 일부 backtick-wrapped path 및 row+table, row+column 표기가 깨져 보임
- 정정 내용: 실제 변경 파일은 /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/initial_condition/1.0__ground_park_heading0_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml 이다. JSBSim 호환을 위해 DATCOM base table 6개는 row plus table 구조에서 row plus column 구조로 재구성했으며 숫자 데이터는 변경하지 않았다.
- 영향 범위: 작업 기록 문서 표기 정정만 해당. 모델 파일, runscript, CSV 로그에는 영향 없음
- 검증 결과: INDEX.md 최신 tail에서 정정 항목이 append됨
- 다음 작업: 최종 응답에서는 정정된 경로와 결과만 보고

## [2026-08-11 16:45] DECISION-20260811-1645-001 — 결정

- 문제: AD3000 산출물을 workflow에 원본 실행 모델로 둘지 미러 variant로 둘지 결정 필요
- 고려한 대안: workflow 단독 aircraft 구성, jsbsim root만 구성, jsbsim root 구성 후 workflow variant 미러
- 최종 선택: jsbsim root를 실행 원본으로 두고 workflow에는 aircraft_variants/AD3000 미러와 scripts/AD3000 runscript를 둠
- 선택 이유: JSBSim 실행 root의 aircraft/engine 참조 구조를 유지하면서 workflow에서 산출물과 실행 케이스를 추적할 수 있음
- 영향 범위: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/AD3000 및 scripts/AD3000
- 장점: 기존 workflow 패턴과 jsbsim root 실행 구조를 모두 만족
- 단점: jsbsim root와 workflow mirror 간 동기화 관리 필요
- 검증 결과: 생성 스크립트 실행과 jsbsim root 검증 완료
- 남은 리스크: hover mixer 보정이 generator와 mirror에 동시에 반영되어야 함

## [2026-08-11 00:00] DECISION-20260811-0000-002 — 결정

- 문제: 제품 기반 propulsion XML에 어떤 추력/전력 근거를 적용할지 결정 필요
- 고려한 대안: 전체를 질량 기준 임의값으로 유지, 제품 모터 사양만 반영, 공개 pull test 표에서 static Ct/Cp를 환산해 반영
- 최종 선택: lift는 Hobbywing V6212 180KV와 VSC 22.1x7.4 pull test 표에서 Ct/Cp를 직접 환산함. cruise는 Hobbywing V6215 210KV 모터 사양을 반영하고 Falcon C2E 20x10은 제공 페이지에서 직접 성능표가 없어 같은 C2E 계열 22x12 공개 표를 피치비 10/12로 보정해 임시 Ct/Cp를 구성함
- 선택 이유: lift 조합은 공식 제품 표의 RPM, thrust, power가 직접 제공되어 가장 추적 가능한 근거임. cruise 20x10은 직접 성능표를 확인하지 못했으므로 제품 형상과 같은 계열 공개 표를 이용한 보수적 추정이 현재 가능한 최소 근거임
- 영향 범위: AD3000 engine XML, prop XML, Propulsion.xml 참조, 제품 근거 문서 및 CSV
- 장점: 초기 임의 propulsion보다 제품 데이터와 추정 근거가 명확함. 추후 실제 bench data 확보 시 CSV와 prop XML만 국소 수정 가능함
- 단점: cruise prop은 실제 20x10 직접 계측값이 아니며, 전진비별 공력 성능은 일반 형상으로 근사함
- 검증 결과: XML 검사, JSBSim catalog 로드, 1.5초 smoke run 통과
- 남은 리스크: 실제 장착 조건, 배터리, ESC 제한, prop 간섭 효과가 모델에 반영되지 않음
- 기존 결정과의 관계: 이전 mass 기반 임의 motor/prop 값은 제품 기반 값으로 대체함

## [2026-08-11 17:11] CORRECTION-20260811-1711-001 — 정정

- 대상 기록: TASK-20260811-0000-002, PROGRESS-20260811-0000-002, DECISION-20260811-0000-002, TODO-20260811-0000-002, INDEX-20260811-0000-002
- 정정 이유: 제품 기반 propulsion 반영 기록을 append할 때 기록 시각을 임시값 2026-08-11 00:00으로 남김
- 기존 내용: 기록 시각이 2026-08-11 00:00 또는 ENTRY ID 20260811-0000으로 표기됨
- 정정 내용: 해당 항목의 실제 기록 시각은 2026-08-11 17:11 KST임. 기록 내용과 검증 결과는 그대로 유효함
- 영향 범위: docs/agent-log 아래 Markdown 기록의 메타데이터 시각 표기
- 검증 결과: append-only 방식으로 정정 기록을 추가함
- 다음 작업: 이후 기록에서는 실제 KST 시각을 사용

## [2026-08-12 09:00] DECISION-20260812-0900-001 — 결정

- 문제: AD3000 cruise prop 모델을 Falcon 20x10 추정값으로 유지할지, 공개 데이터가 있는 V6215+VSC22.1x7.4 조합으로 임시 교체할지 결정 필요
- 고려한 대안: Falcon 20x10 추정 유지, V6215+VSC22.1x7.4 공개 pull test 기반으로 임시 교체, cruise prop 모델을 비활성화
- 최종 선택: V6215+VSC22.1x7.4 공개 pull test 기반 임시 모델을 AD3000 기본 cruise prop으로 사용하고, Falcon 20x10은 원래 의도 규격이지만 공개표 부재로 미사용이라고 XML documentation과 Propulsion.xml 주석에 명시함
- 선택 이유: 현재 검증 가능한 thrust/power 근거는 Hobbywing 공식 공개표이며, 추정 Falcon 계수보다 추적성과 재현성이 높음
- 영향 범위: AD3000 Propulsion.xml, cruise prop XML, 제품 근거 문서 및 CSV, workflow 재생성 스크립트
- 장점: 제품 공개표 기반으로 lift와 cruise 모두 근거 체계가 일관됨
- 단점: 실제 cruise prop 형상은 원래 의도한 20x10과 다르므로 전진비별 성능 예측은 임시값임
- 검증 결과: XML 검사, catalog 로드, 1.5초 smoke run 통과
- 남은 리스크: Falcon 20x10 실제 데이터 확보 시 coefficient와 prop inertia를 재산정해야 함
- 기존 결정과의 관계: 2026-08-11의 Falcon 22x12 피치비 보정 추정 결정은 이번 결정으로 대체됨

## [2026-08-12 09:40] DECISION-20260812-0940-001 — 결정

- 문제: 기체 Spec 시트의 공식 pull test 전체 표를 prop XML 계수 산정에 어떻게 반영할지 결정 필요
- 고려한 대안: 전체 throttle 행 평균 사용, 기존 45-84% 대표 구간 유지, throttle별 motor-prop map 별도 구현
- 최종 선택: 전체 throttle 행은 PROPULSION_SOURCE_DATA.csv에 보존하고, prop XML의 J=0 Ct/Cp는 45-84% throttle 구간 평균을 유지하며 used_for_coefficient=Y로 명시함
- 선택 이유: 저 throttle 및 100% endpoint는 prop XML의 단일 대표 Ct/Cp 산정값을 왜곡할 수 있고, 기존 모델과 비교 가능성을 유지할 수 있음. 동시에 원자료 전체는 CSV에 남겨 추후 map 기반 모델로 확장 가능함
- 영향 범위: propulsion source CSV, prop XML documentation, products 문서, validator 계수 산정 방식
- 장점: 원자료 보존과 모델 적용값 추적성을 동시에 확보
- 단점: throttle별 motor-prop coupled map을 직접 재현하지는 않음
- 검증 결과: AD3000_validate_config.py --run-jsbsim PASS 86 FAIL 0
- 남은 리스크: 20*10 직접 성능표가 없으므로 cruise prop은 여전히 VSC22.1x7.4 임시 모델임
- 기존 결정과의 관계: 이전 공식 웹 데이터 직접 반영 결정을 사용자가 제공한 엑셀 시트 기반 source로 구체화함

## [2026-08-12 09:46] DECISION-20260812-0946-001 — SUPERSEDED

- 대상 기존 결정: DECISION-20260812-0940-001
- 교체 이유: 사용자가 시뮬레이션 목적에서는 기체 Spec 시트에 존재하는 33-100% 전체 공식 데이터를 사용해야 한다고 지적함
- 기존 방식: PROPULSION_SOURCE_DATA.csv에는 전체 행을 보존하되 45-84% 행만 used_for_coefficient=Y로 표시하고 prop XML 대표 Ct/Cp 산정에 사용
- 신규 방식: 33-100% 전체 행을 used_for_coefficient=Y로 표시하고 prop XML 대표 Ct/Cp 산정에 사용
- 고려한 대안: throttle별 coupled motor-prop map 구현, 중간 구간 유지
- 영향 범위: PROPULSION_SOURCE_DATA.csv, prop XML C_THRUST/C_POWER, products 문서, generator template
- 검증 결과: AD3000_validate_config.py --run-jsbsim PASS 86 FAIL 0
- 남은 리스크: 전체 행 평균은 공식표 전체를 반영하지만 throttle별 곡선 자체를 JSBSim prop XML에 직접 넣은 것은 아님

## [2026-08-13 13:39] DECISION-20260813-1339-001 — 완료

- 문제: Project AirSim/PX4 연동용 standard_vtol_demo.xml을 JSBSim 단독 실행 모델로 만들면서 DATCOM 공력 DB를 기존 demo 공력과 교체 가능하게 구성해야 했다.
- 고려한 대안: 원본 단일 XML 직접 수정, JSBSim aircraft 폴더에 복사 후 default DATCOM 모델과 demo aero variant 병행, 완전 분리 XML 컴포넌트화.
- 최종 선택: workflow에는 source 복사본과 Aero_Demo/Aero_DATCOM 추출본, DATCOM 기본 standard_vtol_demo.xml, demo aero variant를 함께 둔다. /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo 에도 동일하게 설치한다.
- 선택 이유: JSBSim은 standard_vtol_demo 이름으로 바로 실행할 수 있고, 기존 demo 공력과 DATCOM 공력을 파일 단위로 비교할 수 있다. 원본 Downloads 파일은 보존된다.
- 영향 범위: standard_vtol_demo_jsbsim 신규 aircraft variant, JSBSim aircraft 설치본, 검증 runscript 2개.
- 장점: JSBSim 단독 실행과 PX4 외부 actuator 의존 제거 확인이 가능하다. 공력 교체 구조가 명확하다.
- 단점: DATCOM 3D Mach breakpoint 제어증분은 1차 검증을 위해 Mach 0.1 slice로 단순화했다.
- 검증 결과: JSBSim 실행, DATCOM 공력 출력, 5개 모터 arming gate 동작 확인.
- 남은 리스크: 비행 안정성은 미검증이며, 다음 단계에서 hover/수직이륙 시나리오를 구성하면서 질량, 추력, 공력 스케일을 재점검해야 한다.
- 기존 결정과의 관계: 기존 ADS/F450_DATCOM 계열의 JSBSim aircraft 폴더 패턴을 따랐다.

## [2026-08-13 14:45] DECISION-20260813-1445-001 — DONE

- 문제: standard_vtol_demo 원본은 PX4 연동 전제 모듈이라 JSBSim 단독 runscript에서 ESC ramp만 주면 attitude 불안정과 고도 overshoot가 발생했다.
- 고려한 대안: 원본 모델에 직접 PX4 flightcontrol을 재현, runscript open-loop throttle만 사용, JSBSim 단독 hover controller variant 생성
- 최종 선택: standard_vtol_demo_hover variant에 attitude/altitude controller를 추가하고 mission runscript는 해당 variant를 사용한다.
- 선택 이유: 이번 단계의 목적은 천이 없는 수직 미션을 JSBSim 단독으로 완료하는 것이므로, PX4 전체 제어기를 재현하기보다 JSBSim 내부 property 기반 보조 제어로 폐루프 hover를 구성하는 편이 범위와 검증 가능성이 맞다.
- 영향 범위: /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo
- 장점: JSBSim 단독으로 시동, 10m 수직이륙, 10s hover, 수직착륙, shutdown을 재현 가능하다.
- 단점: PX4 flightcontrol과 동일한 제어 law가 아니며 전방천이/후방천이 제어에는 별도 확장이 필요하다.
- 검증 결과: 최종 JSBSim 실행에서 mission/state=7 종료, motor-armed=0, esc-out[0..4]=0 확인.
- 남은 리스크: 고도 목표 10m는 평균 9.91m, 최대 9.98m 수준으로 맞췄으며 정밀 착륙/접지 모델 튜닝은 추가 필요.

## [2026-08-13 15:04] DECISION-20260813-1504-001 — SUPERSEDED

- 대상 기존 결정: DECISION-20260813-1445-001
- 교체 이유: 이전 hover variant는 JSBSim 단독 제어기를 추가했지만, F450처럼 공력/제어/효과기/외력을 파일 단위로 완전히 분리한 구조는 아니었다.
- 기존 방식: standard_vtol_demo_hover.xml 내부에 metrics, mass, gear, effectors, flight_control, external_reactions, aerodynamics가 함께 존재함.
- 신규 방식: 메인 XML은 include만 담당하고, Metrics.xml, Mass.xml, Gear.xml, Effectors.xml, FlightControl.xml, ExternalReactions.xml, Aero_DATCOM.xml, Aero_Demo.xml을 별도 모듈로 둔다.
- 고려한 대안: hover 모델만 분리, standard_vtol_demo_jsbsim까지 같이 분리, 빈 Propulsion.xml 추가
- 최종 선택: standard_vtol_demo와 standard_vtol_demo_hover 모두 분리하되, 현재 모델에 없는 propulsion은 억지로 만들지 않고 ExternalReactions.xml로 물리 힘 모듈을 분리한다.
- 영향 범위: /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_jsbsim, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover
- 검증 결과: catalog, arming, aero, 수직 미션 회귀 통과.
- 남은 리스크: 향후 천이 단계에서 pusher thrust와 고정익 추진계를 JSBSim propulsion 섹션으로 옮길 필요가 생길 수 있다.

## [2026-08-13 15:10] DECISION-20260813-1510-001 — DONE

- 문제: workflow runner가 aircraft 이름 기준으로 scripts/<aircraft>/initial_condition 및 scripts/<aircraft>/runscript를 찾는데, standard_vtol_demo_hover용 파일 배치가 없었다.
- 고려한 대안: runscript를 standard_vtol_demo 아래에 유지, runner에 aircraft alias 추가, standard_vtol_demo_hover 폴더를 별도 생성
- 최종 선택: standard_vtol_demo_hover 전용 scripts 폴더를 생성하고 runner discovery 버그를 수정한다.
- 선택 이유: 메뉴의 aircraft 78 standard_vtol_demo_hover와 실제 미션 파일 경로가 1:1로 대응되어 사용자가 선택하기 쉽고, 다른 aircraft 선택 흐름을 깨지 않는다.
- 영향 범위: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 검증 결과: 대화형 입력 78 -> 1 -> 1 실행 통과.
- 남은 리스크: 없음. 단, 77 standard_vtol_demo는 hover-controlled 미션용이 아니라 모듈/데이터 검증용으로 구분한다.

## [2026-08-13 15:50] DECISION-20260813-1550-001 — DONE

- 문제: PX4 lift+cruise/standard VTOL 천이 로직을 JSBSim 단독 runscript로 옮겨야 하지만, 현재 standard_vtol_demo_hover DATCOM 공력에는 elevator effectiveness가 없어 FW pitch controller를 정확히 구성할 수 없다.
- 고려한 대안: PX4 strict 방식으로 FW 구간에서 mc-weight 0.0 적용, FW 구간에도 소량 MC stabilization weight 유지, DATCOM에 임의 elevator 항 추가, propulsion/elevator 모델 재작성 후 진행
- 최종 선택: PX4 상태/가중치/추력 ramp 로직을 반영하되, JSBSim standalone 안정성을 위해 FW segment에서 mc-weight 0.22를 유지한다.
- 선택 이유: 이번 단계 목적은 transition 포함 runscript 구성과 실행 검증이며, 검증되지 않은 elevator 공력항을 임의 생성하는 것보다 현재 모델이 가진 lift/pusher force 구조 안에서 상태 머신을 먼저 닫는 것이 안전하다.
- 영향 범위: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/2.0__rkss14_transition_mission_run.xml
- 장점: runner 메뉴에서 transition mission을 즉시 실행할 수 있고, 전방천이/후방천이/착륙/shutdown 상태가 CSV에 명확히 기록된다.
- 단점: PX4의 FW_MODE에서 MC weight 0.0으로 rotor off 하는 동작과는 다르다.
- 검증 결과: 78 -> 1 -> 2 runner 실행 통과, state13 종료 및 최종 motor off 확인.
- 남은 리스크: 다음 단계에서 elevator/TECS/propulsion 모델을 보강하면 mc-weight를 0으로 줄이는 방향으로 재튜닝해야 한다.

## [2026-08-13 17:16] DECISION-20260813-1716-001 — 채택

- 문제: 3.0 멀티콥터 미션을 attitude target만으로 구성하면 수평 속도가 잘 감쇠하지 않아 최종 위치 drift가 약 383 m까지 커졌다.
- 고려한 대안: runscript attitude target만 더 작게 조정, timed brake segment 추가, FlightControl.xml에 기본 off인 speed hold 보조 채널 추가
- 최종 선택: FlightControl.xml에 fcs/hover-speed-enable이 1일 때만 동작하는 body forward/lateral speed hold 채널을 추가하고, 3.0 runscript에서 speed target을 사용한다.
- 선택 이유: 기존 1.0 vertical mission 및 2.0 transition mission은 speed-enable 기본값 0으로 유지되어 영향이 작고, 3.0 멀티콥터 미션은 위치 drift를 줄이면서 시험 유사 기동 sequence를 유지할 수 있기 때문
- 영향 범위: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml
- 장점: 기존 attitude target interface를 유지하면서 3.0에서만 velocity damping을 사용할 수 있다. final drift가 약 383 m에서 max distance 약 22.19 m로 감소했다.
- 단점: GPS/position waypoint controller가 아니므로 실제 시험 코스의 거리와 착륙점 복귀를 엄밀히 보장하지 않는다.
- 검증 결과: 3.0.2 runner 실행 통과, final state32, motor off, mc-weight=1, pusher off 유지. 기존 1.0 vertical mission 회귀 실행 통과.
- 남은 리스크: heading/yaw command와 position loop 부재로 정확한 좌표 기반 코스 재현은 후속 작업 필요
- 기존 결정과의 관계: 이전 FlightControl 모듈 분리 및 JSBSim standalone hover controller 결정을 유지하고, 멀티콥터 mission proof를 위한 보조 채널만 추가한다.
## [2026-08-13 17:41] DECISION-20260813-1741-001 — 채택

- 문제: 3.0 runscript의 기존 전역 시간 조건은 이전 state 완료 여부와 무관하게 다음 state가 진행될 수 있다. FG_DELTA 기반 next-trigger는 altitude capture 지연 시 hover state가 즉시 지나가는 문제가 있었다.
- 고려한 대안: 전역 시간 조건 유지, FG_DELTA next-trigger 유지, state gate + 절대 trigger 시각, FCS integrator 기반 state-age timer
- 최종 선택: 즉시 검증 가능한 방식으로 state gate + 절대 trigger 시각을 사용한다. 모든 주 전이는 mission/state eq 이전상태를 필수 조건으로 둔다.
- 선택 이유: 기존 JSBSim script runner에서 바로 동작하고, 전역 시간만으로 state가 건너뛰는 문제를 제거할 수 있다. FCS integrator 기반 state-age timer는 별도 설계/검증이 필요해 후속으로 미룬다.
- 영향 범위: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml
- 장점: runner 실행 검증 완료, emergency descent 제거, 원주 후 정상 착륙 흐름 명확화
- 단점: trigger 시각보다 이전 state 완료가 늦어지는 경우 hold duration이 줄어들 수 있다.
- 검증 결과: 3.0.5 실행 final state30, motor off, pusher off, state3 hover 5.28 s 유지 확인
- 남은 리스크: 실제 mission-complete 기준은 state-age timer와 waypoint/velocity/yaw tolerance로 고도화 필요
## [2026-08-13 18:07] DECISION-20260813-1807-001 — 채택

- 문제: 사용자는 XML 내부 좌표를 nose 끝점 기준으로 두되, 기존 CG 기준으로 잡힌 좌표를 변경된 CG점 기반으로 변환하라고 요청했다.
- 고려한 대안: CG location만 0.64914 m로 변경하고 다른 좌표 유지, 모든 location x에 0.64914 m를 더해 nose 기준으로 변환, all-in-one/source XML까지 모두 일괄 변경
- 최종 선택: active modular model의 Metrics/Mass/Gear/ExternalReactions location x에 0.64914 m를 더해 nose 기준 구조좌표로 변환한다. source_*.xml과 과거 all-in-one 복사본은 보관 파일로 보고 수정하지 않는다.
- 선택 이유: standard_vtol_demo_hover.xml은 모듈 include 구조이고 실제 실행은 모듈 파일을 사용한다. 기존 relative 배치를 보존하면서 JSBSim structural frame의 nose-origin 좌표로 맞출 수 있다.
- 영향 범위: standard_vtol_demo_hover active module files 및 /home/junyeopkwon/jsbsim mirror
- 장점: 기존 모터/기어의 CG 상대 moment arm을 유지하면서 CG 위치와 XML location 좌표가 nose 기준으로 정리됨
- 단점: 전방 lift motor x=-0.10486 m가 되어 nose tip보다 104.86 mm 앞쪽으로 계산된다. 이는 기존 front motor가 CG보다 0.754 m 앞에 있었다는 모델 가정을 그대로 유지한 결과임.
- 검증 결과: XML 검사 및 3.1.3 실행 통과. CSV에서 mass=20 kg, cg-x=0.64914 m 확인.
- 남은 리스크: 실제 CAD 좌표와 rotor/gear 위치가 다를 경우 nose-origin 좌표 전체를 재측정해야 한다.
## [2026-08-13 18:14] DECISION-20260813-1814-001 — 채택

- 문제: 20 kg으로 변경된 기체에서 기존 hover base 0.578은 과대 thrust이며 4 m target 대비 약 6.25 m까지 overshoot했다.
- 고려한 대안: 기존 0.578 유지, 단순 계산값 0.535 적용, altitude P/D gain까지 동시 수정, thrust table 재식별 후 적용
- 최종 선택: 현재 thrust table 기반 계산값 0.535를 hover base로 적용하고, runscript 버전을 3.2/3.3/3.4로 분리해 단계적으로 착륙 profile을 개선한다.
- 선택 이유: mass 변경에 따른 1차 hover trim은 thrust table에서 직접 계산 가능하며, 기존 controller 구조를 유지한 채 실행 검증으로 확인할 수 있다.
- 영향 범위: Effectors.xml 기본 hover-throttle-base, 3.2/3.3/3.4 runscript
- 장점: hover average collective가 0.5345로 계산값과 일치하고, hmax가 4.065 m로 안정화됨
- 단점: landing gear force는 아직 5W 수준으로 남아 착륙 profile/gnd reaction 추가 튜닝 필요
- 검증 결과: 3.4.1 final state33, motor off, pusher off, mc-weight=1, hmax=4.065 m
- 남은 리스크: 현재 thrust table 자체가 실제 제품/벤치 데이터가 아니면 hover throttle도 재보정 필요
## [2026-08-14 10:01 KST] DECISION-20260814-1001-001 — 결정

- 문제: PX4/QGC 연동 후 생성되는 기본 로그는 .ulg이며 기존 JSBSim standalone workflow의 combined CSV와 형식이 다르다.
- 고려한 대안: ulog2csv topic별 CSV만 사용, ULog를 한 파일로 merge, JSBSim output CSV를 별도 추가
- 최종 선택: 우선 ULog를 원본으로 보존하고 scripts/px4_ulog_to_combined_csv.py로 topic들을 하나의 combined CSV로 병합한다.
- 선택 이유: QGC/PX4 로그 표준을 유지하면서 기존 CSV 분석 흐름에 가장 빨리 연결할 수 있다.
- 영향 범위: jsbsim_workflow 분석 스크립트와 logs/csv/combined 산출물
- 장점: PX4 actuator/status/sensor/GPS topic을 한 파일에서 확인 가능
- 단점: JSBSim 내부 property는 PX4 ULog에 자동 포함되지 않으므로 별도 동기화가 필요하다.
- 검증 결과: 샘플 .ulg에서 combined CSV 생성 확인
- 남은 리스크: topic rate 차이는 forward-fill로 처리하므로 고주파 신호 정밀 분석은 topic별 원본 CSV 또는 ULog를 함께 봐야 한다.

## [2026-08-14 10:08 KST] DECISION-20260814-1008-001 — 결정

- 문제: PX4/QGC/JSBSim 실행 절차가 수동 명령과 GUI 조작으로 나뉘어 재현성이 떨어질 수 있다.
- 고려한 대안: 문서만 작성, shell script 작성, Python 자동화 스크립트 작성
- 최종 선택: Python 자동화 스크립트와 Markdown runbook을 함께 제공한다.
- 선택 이유: 기존 workflow의 Python 실행 방식과 맞고, PX4 실행 후 최신 ULog를 찾아 combined CSV 변환까지 연결하기 쉽다.
- 영향 범위: jsbsim_workflow/scripts, jsbsim_workflow/docs
- 장점: QGC 실행부터 로그 변환까지 한 명령으로 재현 가능
- 단점: QGC GUI 내부 mission upload/arm 조작은 사용자가 직접 수행해야 한다.
- 검증 결과: 스크립트 문법과 help 출력 검증 완료
- 남은 리스크: QGC GUI 실행 환경과 WSL display/FUSE 상태에 따라 QGC 실행 방식이 달라질 수 있다.

## [2026-08-18 11:35] DECISION-20260818-1135-001 — ACCEPTED

- 문제: combined CSV에 선회/제어 분석용 property를 추가할 때 aircraft마다 존재하지 않는 property가 많아 단순 일괄 추가는 로그 경고/빈 컬럼/유지보수 혼선을 만들 수 있음
- 고려한 대안: 모든 후보 property를 무조건 output에 추가, aircraft별 hard-coded 분기 추가, 공통 후보 목록을 만들고 JSBSim aircraft catalog에 존재하는 property만 선택
- 최종 선택: `COMBINED_CONTROL_ANALYSIS_PROPERTIES` 공통 후보 목록을 두고 `aircraft_catalog_properties()`와 `unique_existing_properties()`로 aircraft별 존재 property만 combined output에 추가
- 선택 이유: C172 heading-hold, VTOL hover, F450/LiftCruise AP 계열을 한 runner에서 지원하면서도 없는 property를 무리하게 output하지 않기 위함
- 영향 범위: `scripts/run_jsbsim_timestamped_combined_csv_only.py`로 새로 생성되는 combined CSV
- 장점: C172 선회 분석에서 `heading error -> roll command -> roll error -> aileron` 경로를 추적할 수 있고, 다른 aircraft에는 해당 aircraft에 존재하는 진단 property만 추가됨
- 단점: 과거에 이미 생성된 combined CSV에는 새 컬럼이 자동 반영되지 않음
- 검증 결과: C172 5.16 combined 실행에서 173 columns CSV 생성, 필수 선회 컬럼 존재 및 값 범위 확인
- 남은 리스크: 모든 aircraft/scenario를 실제 실행 검증하지는 않았음
- 기존 결정과의 관계: 기존 sixdof/raw 출력 추가 결정을 combined CSV 전용 제어 분석 컬럼으로 보완

## [2026-08-19 10:21] DECISION-20260819-1021-001 — 채택

- 문제: 첨부 standard_vtol_demo_motor_updated_ko.xml을 바로 PX4 JSBSim SITL에 연결할지, 먼저 JSBSim 단독 호환성을 검증할지 결정 필요
- 고려한 대안: 기존 standard_vtol_demo_hover_px4 모델에 덮어쓰기, PX4 별도 target을 먼저 추가, 임시 JSBSim root에서 단독 로딩 검증 후 수정 범위 결정
- 최종 선택: 프로젝트/PX4 기존 모델은 건드리지 않고 임시 JSBSim root에서 첨부 XML 단독 로딩을 먼저 검증한다.
- 선택 이유: 기존 PX4/JSBSim 작업 트리에 변경 사항이 많고, 첨부 XML이 JSBSim 단독 로딩에서 실패하면 PX4/QGC 실행까지 진행해도 원인 분리가 어렵기 때문
- 영향 범위: 이번 단계는 검토 문서와 agent-log만 변경. PX4 source, JSBSim aircraft source, 첨부 원본 XML은 수정하지 않음
- 장점: 실패 원인을 PX4가 아닌 XML 호환성 문제로 좁힐 수 있고, 기존 정상 target을 손상하지 않는다.
- 단점: 사용자가 원하는 PX4/QGC 실제 실행은 아직 수행하지 못한다.
- 검증 결과: 첨부 XML은 FGTable: missing lookup axis column으로 JSBSim 단독 로딩 실패. 기존 standard_vtol_demo_hover 모델은 같은 초기조건에서 rc=0.
- 남은 리스크: table 형식 보정 후에도 Floating point exception이 발생해 0속도 보호와 공력 rate 항 재검토가 필요하다.
- 기존 결정과의 관계: 기존 PX4/QGC runbook의 standard_vtol_demo_hover_px4 target은 유지하고, 새 XML은 별도 후보 모델로 분리해 검증해야 한다.

## [2026-08-19 10:31] DECISION-20260819-1031-001 — 채택

- 문제: 첨부 XML의 Mach별 2D 공력 table이 JSBSim 1.2.4에서 missing lookup axis column 오류를 발생시킴
- 고려한 대안: 원본 XML 직접 수정, 기존 정상 Aero_DATCOM.xml로 교체, workflow 내부 후보 모델에 원본 보존 복사본과 table 보정본을 분리 생성
- 최종 선택: 원본 첨부 파일은 그대로 두고 workflow 내부 후보 모델에 source copy와 table-fixed main XML을 분리 생성한다.
- 선택 이유: 데이터 원본 추적성을 유지하면서 JSBSim 호환성 수정 내용을 명확히 비교할 수 있기 때문
- 영향 범위: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/ 아래 신규 파일과 검토 문서
- 장점: 기존 PX4/JSBSim 모델을 건드리지 않고 table 오류 제거 여부를 독립 검증할 수 있다.
- 단점: 아직 PX4 target에 연결되지 않았고, Floating point exception은 별도 수정이 필요하다.
- 검증 결과: xmllint 통과, table 구조 row/column 14개 및 row/column/table 2개 확인, JSBSim에서 FGTable missing lookup axis column 메시지 제거 확인
- 남은 리스크: 0속도 divide-by-zero와 PX4 parameter/geometry 정합성은 다음 단계에서 해결해야 한다.
- 기존 결정과의 관계: DECISION-20260819-1021-001의 단계적 검증 방침을 따른다.

## [2026-08-19 10:38] DECISION-20260819-1038-001 — 채택

- 문제: 공력 rate 항에서 1.0 / velocities/vt-fps를 직접 사용하면 지상 정지 초기조건에서 divide-by-zero로 Floating point exception이 발생함
- 고려한 대안: 작은 epsilon denominator 추가, runscript 초기속도 부여, 기존 정상 모델과 같은 aero/ci2vel 및 aero/bi2vel 사용
- 최종 선택: 기존 정상 Aero_DATCOM.xml과 같은 aero/ci2vel 및 aero/bi2vel property를 사용한다.
- 선택 이유: JSBSim 내장 공력 scale property를 사용하면 0속도 보호와 기존 모델 일관성을 동시에 확보할 수 있음
- 영향 범위: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 장점: XML 내 직접 quotient 제거, JSBSim catalog/load/run 정상 종료, 기존 검증 모델과 동일한 표현 방식
- 단점: 원래 생성 XML의 명시적 수식 형태는 사라지고 JSBSim property 의미에 의존함
- 검증 결과: xmllint 통과, JSBSim --catalog rc=0, 지상 정지 --end=0.02 및 --end=1.0 rc=0
- 남은 리스크: PX4 연결 전 CG 좌표와 hover parameter 정합성은 별도 검증 필요
- 기존 결정과의 관계: DECISION-20260819-1031-001의 공력 table 보정 이후 남은 FPE를 해결함

## [2026-08-19 10:52] DECISION-20260819-1052-001 — ACCEPTED

- 문제: 새 XML의 14kg 후보가 PX4 연결 및 JSBSim 단독 실행에서 NaN/FPE를 유발함
- 고려한 대안: 14kg 유지 후 접지 파라미터 재튜닝, 초기조건 변경, 이전 20kg 복귀
- 최종 선택: 좌표계를 기준 모델과 맞춘 뒤, 질량은 이전값 20.0kg으로 복귀
- 선택 이유: 기준 hover 모델은 20kg에서 동일 지상 초기조건 5초 실행을 통과했고, 사용자가 14kg 문제로 보이면 이전 무게로 진행하라고 요청했음
- 영향 범위: 후보 XML 질량, ground_reactions/ExternalReactions x좌표, PX4 airframe hover thrust와 rotor arm
- 장점: PX4/JSBSim 연결에서 NaN/FPE/CRASH가 재발하지 않는 상태까지 빠르게 회복
- 단점: 14kg 모델을 살리기 위한 landing gear/contact 파라미터 튜닝은 보류됨
- 검증 결과: JSBSim direct 5초 rc=0, PX4 SITL 35초 timeout 로그 NaN/FPE/CRASH 0건, CSV NaN 0건
- 남은 리스크: 비행 제어 안정성과 공력 table 물리 타당성은 별도 검증 필요
- 기존 결정과의 관계: 이전 14kg 검토 결과를 대체하지 않고, PX4 연결 검증용 임시 운영 질량을 20kg으로 설정

## [2026-08-19 11:40] DECISION-20260819-1140-001 — ACCEPTED

- 문제: 새 모델이 단일 XML이라 F450처럼 모듈별 관리가 어렵다
- 고려한 대안: 별도 modular variant만 생성, 기존 파일을 직접 분리, PX4 bridge는 단일본 유지
- 최종 선택: workflow 후보와 PX4 bridge 모델 모두 기존 주 파일명은 유지하면서 include main으로 전환하고, 변환 전 단일본은 Monolithic.xml로 보존
- 선택 이유: 기존 실행 target과 문서 경로를 유지하면서 모듈별 편집성을 확보할 수 있음
- 영향 범위: workflow aircraft variant, PX4 jsbsim_bridge model directory, runbook/review 문서
- 장점: Metrics/Mass/Gear/Effectors/FlightControl/ExternalReactions/Aero별 독립 수정 가능
- 단점: 주 XML만 보고는 전체 모델 내용을 한 번에 볼 수 없으며, PX4 direct temp-root 검증에서 output path warning이 보일 수 있음
- 검증 결과: xmllint, JSBSim direct 5초, PX4 DONT_RUN, PX4 short bridge run 통과
- 남은 리스크: QGC 장시간 비행은 분리 후 재수행하지 않음
- 기존 결정과의 관계: 20kg 후보와 PX4 target 명명은 유지

## [2026-08-20 10:00] DECISION-20260820-1000-001 — ACCEPTED

- 문제: 고정익 전환 수정 범위를 어디까지로 잡을지(원인 진단에서는 airframe/bridge/공력 3가지가 모두 지적됨)
- 고려한 대안: (1) airframe/bridge/공력을 한 번에 모두 수정, (2) airframe/bridge만 먼저 수정하고 공력은 별도로 남김
- 최종 선택: (2) 채택. 기체 XML의 Metrics/Mass/Gear/ExternalReactions/Aero는 전혀 수정하지 않고, PX4 airframe 파라미터와 JSBSim bridge actuator/sensor mapping만 수정
- 선택 이유: 사용자가 DATCOM 공력 데이터의 러더 입력 해석 문제를 별도로 검토 중이라고 명시했고, 이번 요청은 "제어부분을 bridge매핑해서 가능하게" 만드는 것으로 범위를 한정함
- 영향 범위: PX4 airframe `3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4`, bridge config `standard_vtol_demo_motor_updated_ko_px4.xml`만 수정. 기체 XML은 무변경
- 장점: 공력 데이터에 대한 사용자의 별도 판단을 침해하지 않음. 제어 배선(플랜트 입력 경로) 문제와 공력 물리 문제를 분리해 원인 추적이 쉬워짐
- 단점: 조종면 명령이 JSBSim까지는 전달되더라도 러더의 실제 요 모멘트가 DATCOM 데이터 한계로 약하거나 없을 수 있어, 이번 수정만으로는 실비행 전환 성공을 보장하지 못함
- 검증 결과: xmllint, bash -n, DONT_RUN 빌드, 30초 headless 실행 모두 통과(NaN/크래시 없음)
- 남은 리스크: 실제 전환 비행에서 요 축 제어권 부족이 나타날 수 있으며, 이는 공력 데이터 보강이 필요한 별도 사안(TODO-20260820-1002-001 참고)
- 기존 결정과의 관계: TASK-20260819-1425-001/1448-001 진단 결과 중 airframe/bridge 항목만 우선 적용, 공력 항목은 사용자 판단 대기

## [2026-08-20 10:00] DECISION-20260820-1000-002 — ACCEPTED

- 문제: 새로 추가하는 pusher 로터(CA_ROTOR4)의 PX4 `CA_ROTOR4_PX` 좌표를 어떤 기준으로 산정할지 (JSBSim 구조좌표와 PX4 FRD body-CG 좌표가 축 방향과 원점이 다름)
- 고려한 대안: (1) JSBSim 좌표값을 그대로 사용, (2) 기존 CA_ROTOR0-3 값에서 변환 공식을 역산해 동일하게 적용
- 최종 선택: (2) 채택. 기존 CA_ROTOR0_PX 0.754/CA_ROTOR1_PX -0.755가 각각 `CG_x(0.649) - motor_x(-0.105)`, `CG_x(0.649) - motor_x(1.404)`와 정확히 일치함을 확인해 `PX4_PX = CG_x(JSBSim) - motor_x(JSBSim)` 공식을 확정하고, pusher(ExternalReactions.xml x=2.249)에 동일 적용: `0.649 - 2.249 = -1.6`
- 선택 이유: 이미 검증되어 정상 hover 중인 4개 로터의 좌표 변환 관례를 그대로 따르는 것이 새 값을 추정하는 것보다 안전함(JSBSim +X=aft, PX4 CA_ROTOR +X=forward-from-CG)
- 영향 범위: airframe `CA_ROTOR4_PX -1.6`, `CA_ROTOR4_AX 1`(추력 방향 +X), `CA_ROTOR4_AZ 0`. Y/Z는 기존 4개 로터도 CG 대비 소각(z=0.05m)을 무시하는 관례를 따라 pusher도 Y=0/Z 미설정으로 둠(pusher는 y=0, z=0으로 원래도 CG와 거의 일치)
- 장점: 좌표계 불일치로 인한 잘못된 모멘트암 설정 위험을 제거
- 단점: 검증은 공식의 내적 일관성(기존 4개 값과의 역산 일치)에 근거한 것이며, 별도의 독립적인 pitch trim 실비행 검증은 하지 않음
- 검증 결과: 기존 4개 로터 값 역산 일치 확인(0.754, -0.755 모두 소수점 3자리까지 일치)
- 남은 리스크: pusher 추력이 커질 경우(전환 후 순항 스로틀) pitch 모멘트가 예상과 다르게 나타날 수 있어 실비행에서 pitch trim 확인 필요
- 기존 결정과의 관계: DECISION-20260819-1052-001에서 확정한 절대좌표 보정(front=1.249 등) 및 그 이전 CA_ROTOR0-3 좌표 산정 관례를 그대로 계승

## [2026-08-20 11:20] DECISION-20260820-1120-001 — ACCEPTED

- 문제: 실비행 검증에서 발견된 고받음각(alpha 불안정) 발산 문제를 이번 세션에서 직접 수정할지 여부
- 고려한 대안: (1) Aero.xml에 즉시 high-alpha 클램핑/제한 로직을 추가해 재시도, (2) 원인만 정확히 규명해 문서화하고 수정은 사용자 판단으로 넘김
- 최종 선택: (2) 채택. Aero.xml은 수정하지 않고 진단 결과만 상세히 기록
- 선택 이유: 이번 세션 초반에 사용자가 "DATCOM이 러더 입력을 해석 못해서 공력 데이터를 이렇게 구성했고 고민 중이니 일단 냅두라"고 이미 명시적으로 지시함(TASK-20260820-1000-001). 이번에 새로 발견한 고받음각 발산 문제도 같은 Aero.xml/DATCOM 영역의 문제이므로, 사용자의 기존 지시 범위를 벗어나지 않으려면 임의로 손대지 않는 것이 맞다고 판단
- 영향 범위: 코드 변경 없음. TODO-20260820-1120-001/1121-001로 사용자 판단 대기 상태를 명시적으로 남김
- 장점: 사용자가 이미 진행 중인 공력 데이터 재검토와 충돌하거나 중복 작업을 만들지 않음
- 단점: 이번 실비행 목표(FW 유지 비행 성공)는 달성하지 못한 채로 세션이 종료됨
- 검증 결과: 해당 없음(의도적 보류)
- 남은 리스크: 사용자가 별도로 공력 데이터를 수정하기 전까지는 이 모델의 실제 전환 비행 성공을 재현할 수 없음
- 기존 결정과의 관계: DECISION-20260820-1000-001(제어 배선만 수정, 공력은 무변경)의 연장선

## [2026-08-20 12:00] DECISION-20260820-1200-001 — ACCEPTED

- 문제: 고받음각 발산을 어떤 방식으로 억제할지(2026-08-19 논의: 풀레인지 -180~180 테이블 vs 속도 기반 게이팅 vs alpha 기반 게이팅)
- 고려한 대안: (1) 레퍼런스 성공 모델처럼 flat-plate 근사로 -180~180도 전체 테이블 재작성, (2) 총속도(Vt) 기준 게이팅, (3) alpha 자체를 기준으로 한 연속 게이팅(모드 스위치 아님)
- 최종 선택: (3) 채택. F450(순정) 모델이 alpha 계수를 상수 0으로 둬서 원천 차단하는 방식을 확인한 뒤, 사용자와 논의를 거쳐 "천이 중에도 lift가 서서히 살아나야 한다"는 물리적 요구를 반영해 alpha 기반 연속 램프(-90/-24/11/90도 4점)로 확정
- 선택 이유: (1)안은 정확하지만 작업량이 크고 새 데이터 합성이 필요함. (2)안(Vt 기준)은 순수 수직상승 중 qbar가 실제로는 작지 않아(상승속도 자체가 크므로) 오판 가능성이 있고, 레퍼런스 모델이 "no lift during transition" 버그를 겪었던 것과 유사한 실수를 반복할 위험이 있음. (3)안은 기존 DATCOM 데이터를 그대로 재사용하면서, 문제의 직접 원인(alpha가 테이블 유효범위 밖)에 정확히 대응하고, 천이 중 alpha가 정상범위로 들어오면 자연스럽게 양력이 살아나 불연속을 피할 수 있음
- 영향 범위: Aero.xml에 게이트 함수 1개 신규 추가, 기존 16개 계수 함수에 곱셈항 1줄씩 삽입(DATCOM 원본 수치는 전혀 변경하지 않음)
- 장점: 기존 DATCOM 값 보존, 코드 변경 최소화, 물리적으로 정확한 근거(alpha가 테이블 밖이면 그 값 자체가 미검증)
- 단점: 재검증 결과 이 게이트만으로는 전환 시퀀스 전체의 안정성을 보장하지 못함(TODO-20260820-1200-001) — 게이트가 닫혀있는 동안의 제어 컨트롤러 거동(적분 와인드업 등)까지는 이 방식으로 해결되지 않음
- 검증 결과: 순수 수직상승 구간의 자세 안정성 개선은 CSV로 확인. 전환 이후 발산은 미해결로 남음
- 남은 리스크: TODO-20260820-1200-001의 새 발산 문제가 이 게이트의 램프 폭 설계(급격한 재개방)에서 비롯된 것인지, 아니면 전적으로 별개(제어 게인/절차)의 문제인지는 추가 실험 없이는 확정할 수 없음
- 기존 결정과의 관계: DECISION-20260820-1120-001에서 사용자 판단 대기로 남겨뒀던 것을 사용자 승인 후 실제로 구현한 후속 결정

## [2026-08-20 12:30] DECISION-20260820-1230-001 — ACCEPTED

- 문제: CG를 원점 기준에서 nose 기준 649mm로 옮길 때, Metrics.xml의 AERORP/VRP/EYEPOINT도 함께 옮겨야 하는가
- 고려한 대안: (1) AERORP는 물리적으로 미미한 영향이라 판단하고 그대로 둔다, (2) CG와 동일하게 0.649로 맞춘다, (3) AERORP를 CG와 별도의 실제 공력중심(다른 값)으로 재산정한다
- 최종 선택: (2) 채택. AERORP/VRP를 CG와 동일한 0.649로, EYEPOINT는 원래 데모의 CG 대비 오프셋(+0.15) 관계를 보존해 0.799로 설정
- 선택 이유: JSBSim 소스(`FGAerodynamics.cpp:247-288`)로 AERORP가 실제 모멘트 계산에 쓰이는 물리량임을 확인했고, 원래 데모 설계 의도가 "AERORP=CG(모멘트암 0)"였음(원본 파일에서 AERORP=CG=(0,0,0) 동일값)이 명백했으므로, 이 설계 의도를 새 프레임에서도 유지하는 것이 가장 안전하고 근거가 명확한 선택. (3)안(별도 실측 공력중심 재산정)은 새로운 CAD/풍동 데이터가 필요해 현재 범위를 벗어남
- 영향 범위: Metrics.xml 3개 location 값만 수정(AERORP, VRP, EYEPOINT). Mass/Gear/ExternalReactions는 이미 정상이라 무변경
- 장점: 소스 코드로 직접 확인된 명확한 물리적 근거. 사용자가 지적한 "모터/기타 부위 좌표 일관성" 우려가 실제로 유효한 버그였음을 확인하고 해결
- 단점: EYEPOINT의 "CG 대비 +0.15" 관계가 원래 데모에서 의도된 것인지(단순 시각화용 placeholder였을 수도 있음) 100% 확정하지 못함 — 다만 EYEPOINT는 물리(EOM) 계산에는 쓰이지 않고 시각화 전용(FGAuxiliary.cpp에서 vLocationVRP류로만 사용)이라 이 불확실성이 발산/크래시에 영향을 주지 않음을 확인
- 검증 결과: 수정 후 동일 arm-takeoff-transition-land 시퀀스 재실행 결과 CSV 전체 NaN 0건, 콘솔 Attitude failure 반복 소멸, Landing detected 확인, 최종 정지상태가 초기 지상정지상태와 일치
- 남은 리스크: 없음(이 결정이 다루는 범위 내에서는). Quad-chute로 인한 MC 강제복귀는 별도 문제(TODO-20260820-1230-001)
- 기존 결정과의 관계: DECISION-20260819-1052-001(모터/기어 절대좌표 보정)이 놓쳤던 부분을 마저 완성. DECISION-20260820-1000-002(CA_ROTOR4_PX 산정)는 이미 올바른 CG=0.649 기준으로 계산했으므로 이번 수정과 무관하게 유효함
