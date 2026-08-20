## [2026-06-15 17:51] TODO-20260615-1751-001 — OPEN

- 과업:
  - c172x 추락 케이스 좌표축 해석 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 캡쳐본 좌표계와 JSBSim Local NED 좌표계의 대응 확인
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.0__450m_60ms_pitch25_no_trim_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
- 수행 내용:
  - 현재 결과는 `x=North`, `y=East`, `z=ground altitude` 기준으로 산출
- 변경 이유:
  - 캡쳐본 yaw `0 deg`를 JSBSim `psi=0 deg`로 유지하기 위함
- 검증 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
- 검증 결과:
  - 실행 성공
- 검증하지 못한 항목:
  - 사용자가 의도한 x축이 North인지 East인지
- 가정:
  - x축은 JSBSim Local North로 해석
- 남은 리스크:
  - x축을 East로 의도했다면 `psi=90 deg` 케이스를 추가해야 함
- 다음 작업:
  - 사용자 확인 후 필요 시 `4.1` 비교 케이스 추가
- 관련 기록:
  - `DECISION-20260615-1751-001`
- Git commit:
  - 없음

## [2026-06-15 18:20] TODO-20260615-1820-001 — OPEN

- 과업:
  - `4.2`, `4.3`, 기존 ballistic 결과 비교표 및 보고서용 2D 그래프 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 기존 ballistic 결과와 유사한 방향 고정 활공 추락 케이스 검토
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.2.2__450m_60ms_x_engineout_t0_spherical_engineout_t0_spherical_summary.json`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical_headinghold_trim_spherical_summary.json`
- 수행 내용:
  - `4.3` heading hold/trim glide 결과 생성 완료
- 변경 이유:
  - 기존 ballistic 이미지와 비교 가능한 형태의 궤적을 확보하기 위함
- 검증 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_headinghold_trim_spherical.py`
- 검증 결과:
  - 실행 성공
- 검증하지 못한 항목:
  - 기존 ballistic 결과 원본 CSV와의 정량 비교
- 가정:
  - 현재는 이미지 기반 형태 비교만 수행
- 남은 리스크:
  - 기존 ballistic 결과와 수평거리/시간 규모 차이가 큼
- 다음 작업:
  - ballistic 원본 CSV가 있으면 비교표와 overlay plot 생성
- 관련 기록:
  - `DECISION-20260615-1820-001`
- Git commit:
  - 없음

## [2026-06-15 18:13] TODO-20260615-1813-001 — OPEN

- 과업:
  - AP/trim off 추락과 heading hold/trim glide 결과 비교 필요 여부 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 추락 시작 시점 직접 초기조건 기반 결과 산출
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.2__450m_60ms_x_engineout_t0_spherical_run.xml`
- 수행 내용:
  - 현재 최종 결과 `4.2.2`는 AP/trim off 기준
- 변경 이유:
  - 최초 요청의 trim/autopilot 없이 조건과 일치시키기 위함
- 검증 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_spherical.py`
- 검증 결과:
  - 실행 성공
- 검증하지 못한 항목:
  - 사용자가 최종적으로 원하는 궤적이 순수 AP/trim off인지 직진 활공형인지
- 가정:
  - 순수 AP/trim off 결과를 우선
- 남은 리스크:
  - 그래프가 루프 형태로 보일 수 있음
- 다음 작업:
  - 필요 시 heading hold/trim glide 비교 케이스 추가
- 관련 기록:
  - `DECISION-20260615-1813-001`
- Git commit:
  - 없음

## [2026-06-15 18:00] TODO-20260615-1800-001 — OPEN

- 과업:
  - engine-out 이후 heading hold 유지 여부 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 참조 `2.2`와 유사한 cruise 후 engine-out 케이스 구현
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.1__450m_60ms_x_cruise30_engineout_headinghold_run.xml`
- 수행 내용:
  - 현재 `4.1`은 engine-out 이후 altitude hold는 끄고 heading hold는 유지
- 변경 이유:
  - 사용자가 참조한 `2.2__cruise_30s_engineout_headinghold_legacy_run.xml` 동작과 유사하게 만들기 위함
- 검증 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
- 검증 결과:
  - 실행 성공
- 검증하지 못한 항목:
  - 사용자가 engine-out 이후에도 autopilot heading hold를 허용하는지
- 가정:
  - x 방향 유지가 중요하므로 heading hold 유지
- 남은 리스크:
  - 완전한 trim/autopilot 없는 추락 요구와 충돌할 수 있음
- 다음 작업:
  - 필요 시 heading hold off 변형 `4.2` 추가
- 관련 기록:
  - `DECISION-20260615-1800-001`
- Git commit:
  - 없음
## [2026-06-16 11:56] TODO-20260616-1156-001 — OPEN

- 과업:
  - 27개 ground reaction 변형 전체 실행 및 summary 병합 자동화 필요 여부 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 사용자가 결과 비교는 직접 수행한다고 했으므로 이번 작업에서는 기본 계수 변형만 실행
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_groundreaction/manifest.csv`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_groundreaction_takeoff.py`
- 수행 내용:
  - 27개 변형 XML 생성
  - 기본 계수 변형 `c172x_gr_damp100_spring100_fric100` 이륙 실행 확인
- 변경 이유:
  - 전체 조합 비교를 반복 가능하게 만들기 위함
- 검증 명령어:
  - `python3 scripts/run_c172x_groundreaction_takeoff.py`
- 검증 결과:
  - 기본 계수 변형 이륙 확인 성공
- 검증하지 못한 항목:
  - 나머지 26개 변형의 실행 성공 여부와 비교 결과
- 가정:
  - 사용자가 비교 실행을 직접 수행
- 남은 리스크:
  - `spring=0`, `damping=0`, `friction=0` 조합 일부는 비정상 접지/지면 관통/수치 불안정 가능성이 있음
- 다음 작업:
  - 필요 시 `manifest.csv`를 순회하는 일괄 실행 및 summary 병합 스크립트 추가
- 관련 기록:
  - `TASK-20260616-1156-001`
- Git commit:
  - 없음
## [2026-06-16 12:08] TODO-20260616-1208-001 — OPEN

- 과업:
  - `5.1` FlightGear 상태기계에서 70 kt initial climb 속도 유지 성능 개선
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - FlightGear C172 수동 이륙 절차를 JSBSim 스크립트로 반영
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.1__takeoff_flightgear_state_machine_run.xml`
- 수행 내용:
  - 500 ft AGL까지 이륙/상승 성공
- 변경 이유:
  - 현재 최종 속도는 `29.428067169317252 m/s`로 약 57 kt 수준이며, FlightGear 문서의 70 kt target보다 낮음
- 검증 명령어:
  - `python3 scripts/run_c172x_groundreaction_takeoff.py --procedure flightgear`
- 검증 결과:
  - `climb_500ft_confirmed=True`
- 검증하지 못한 항목:
  - 70 kt target을 지속적으로 유지하는 closed-loop 제어
- 가정:
  - 이번 작업의 우선 목표는 기본 계수 variant의 반복 가능한 이륙/500 ft 도달
- 남은 리스크:
  - 계수 비교에서 속도 유지 차이가 ground reaction 영향과 조종 로직 영향을 함께 포함할 수 있음
- 다음 작업:
  - 필요 시 Python runner에서 airspeed feedback 기반 elevator 제어로 전환
- 관련 기록:
  - `TASK-20260616-1208-001`
- Git commit:
  - 없음
## [2026-06-16 18:23] TODO-20260616-1823-001 — OPEN

- 과업:
  - 필요 시 물리적 no-engine `c172x` aircraft variant 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x 엔진 없는상태로 추락하는 runscript 작성`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x/c172x.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.4__450m_60ms_x_noengine_drop_run.xml`
- 수행 내용:
  - 이번 작업에서는 runscript/초기조건 수준의 engine off 구현 완료
- 변경 이유:
  - 기존 aircraft XML의 propulsion/propeller 모델이 남아 있어 windmilling 로그가 남을 수 있음
- 검증 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_drop.py`
- 검증 결과:
  - runscript 실행 성공
  - `magneto_cmd=0`, `starter_cmd=0`, `throttle_cmd_norm=0` 유지
  - `engine_rpm`, `propeller_rpm`, `thrust_lbs`는 windmilling/프로펠러 공력 영향으로 0이 아닌 값 기록
- 검증하지 못한 항목:
  - `<propulsion>` 제거 variant의 동역학 결과
- 가정:
  - 현재 요구는 runscript 수준 구현
- 남은 리스크:
  - 사용자가 "엔진 없음"을 기체 모델에서 엔진/프로펠러 제거로 의미했다면 현재 산출물이 요구보다 약할 수 있음
- 다음 작업:
  - 필요 시 `c172x_noengine` aircraft variant를 만들고 동일 초기조건/runscript를 해당 aircraft로 실행
- 관련 기록:
  - `TASK-20260616-1823-001`
- Git commit:
  - 없음
## [2026-06-16 18:32] TODO-20260616-1832-001 — DONE

- 대상 TODO:
  - `TODO-20260616-1823-001`
- 완료 내용:
  - `c172x_noengine` aircraft variant 생성
  - 원본 `c172x.xml`에서 `<engine>` 및 propeller `<thruster>` 제거
  - no-engine/no-propeller 추락 runscript와 wrapper 생성
- 관련 파일:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_noprop_drop.py`
- 검증 결과:
  - `engine_power_hp`, `thrust_lbs`, `engine_rpm`, `propeller_rpm`, `propeller_power_ftlbps`, `prop_advance_ratio`가 SI CSV 전 구간에서 모두 `0.0`
- 남은 리스크:
  - 엔진/프로펠러 질량 제거까지 반영하지는 않음

## [2026-06-16 18:32] TODO-20260616-1832-002 — OPEN

- 과업:
  - 필요 시 엔진/프로펠러 구조 질량까지 제거한 `c172x_noengine` 질량 모델 보정
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `엔진 추력 프로펠러까지 없이 추락으로 파일 만들어 볼래?`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml`
- 수행 내용:
  - engine/propeller thrust model 제거 완료
- 변경 이유:
  - 현재 variant는 원본 `mass_balance`를 유지하므로 실제 엔진/프로펠러 물리 질량 제거까지는 반영하지 않음
- 검증 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_noprop_drop.py`
- 검증 결과:
  - engine/thrust/propeller 출력 0 확인
- 검증하지 못한 항목:
  - 엔진/프로펠러 질량 제거 후 CG 및 관성 변화
- 가정:
  - 이번 작업의 우선 요구는 추력/프로펠러 공력 제거
- 남은 리스크:
  - 질량까지 제거해야 하는 충돌/낙하 연구에서는 현재 variant가 물리적으로 과대 질량일 수 있음
- 다음 작업:
  - 필요 시 엔진/프로펠러 질량과 위치를 정의해 `mass_balance` 보정 variant 작성
- 관련 기록:
  - `TASK-20260616-1832-001`
- Git commit:
  - 없음
## [2026-06-16 20:54] TODO-20260616-2054-001 — OPEN

- 과업:
  - empty-airframe no-engine/no-propeller surface-neutral 케이스를 지면 접촉까지 연장 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 기본 기체 공력 영향 확인
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/runscript/1.0__450m_60ms_x_empty_surface_neutral_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_drop.py`
- 수행 내용:
  - 180초까지 실행 완료
- 변경 이유:
  - 180초 시점 고도 약 `80.45 m`로 지면 접촉 전
- 검증 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_drop.py`
- 검증 결과:
  - roll/yaw는 수치오차 수준으로 안정
- 검증하지 못한 항목:
  - 실제 지면 접촉 시각과 충돌 직전 속도
- 가정:
  - 현재 요청의 우선 목적은 roll/yaw 원인 확인
- 남은 리스크:
  - summary 필드 `ground_reach_time_s`가 현재 케이스에서는 runscript 종료 시각을 의미
- 다음 작업:
  - runscript `end`를 240초 이상으로 늘린 변형 추가 또는 현재 파일 수정 후 재실행
- 관련 기록:
  - `TASK-20260616-2054-001`
- Git commit:
  - 없음
## [2026-06-17 11:20] TODO-20260617-1120-001 — OPEN

- 과업:
  - 30도 자세 격자 initial XML용 batch runscript/runner 생성 및 실행 검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 자세값 `psi/theta/phi` 30도 간격 drop initial XML 생성
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/attitude_grid_30deg/`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_cm0_attitude_grid_initials.py`
- 수행 내용:
  - initial XML 생성까지 완료
- 변경 이유:
  - 실제 대량 실행에는 각 initial XML을 참조하는 runscript 또는 공통 runner가 필요
- 검증 명령어:
  - `python3 -m py_compile scripts/generate_c172x_cm0_attitude_grid_initials.py`
  - XML parse 검증
- 검증 결과:
  - 생성된 `1008`개 XML 파싱 성공
- 검증하지 못한 항목:
  - JSBSim 대량 실행
- 가정:
  - 사용자가 요청한 범위는 initial XML 생성까지
- 남은 리스크:
  - `theta=±90 deg` 자세는 Euler singularity 가능성이 있어 실행 결과 해석 시 별도 검토 필요
- 다음 작업:
  - 필요 시 `attitude_grid_30deg` 폴더를 순회하는 batch 실행 스크립트 작성
- 관련 기록:
  - `TASK-20260617-1120-001`
- Git commit:
  - 없음

## [2026-06-21 15:54] TODO-20260621-1554-001 — OPEN

- 과업: 4단계 안전 상승 제어 구성
- 발견된 문제: 고정 elevator 명령을 풀어 속도는 회복했지만 피치 -22.33도, 롤 약 62.78도, 상승률 -47.84 ft/s로 자세가 붕괴
- 필요한 작업: 속도·피치·롤·상승률을 함께 제어하는 폐루프 로직 또는 검증된 FlightGear 조종 입력 적용
- 완료 조건: 70 kt 이상, 양의 상승률, 허용 롤·피치 범위를 일정 시간 유지
- 상태: OPEN
- 관련 파일: scripts/c172x/runscript/5.5__takeoff_stage3_stage4_diagnostic_run.xml

## [2026-06-21 15:54] TODO-20260621-1554-002 — OPEN

- 과업: Stage 4 완료 판정 보강
- 발견된 문제: 현재 조건은 AGL 150 ft와 70 kt만 검사해 급강하·과대 뱅크도 완료로 처리
- 필요한 작업: velocities/h-dot-fps, attitude/phi-deg, attitude/theta-deg, 안정 유지시간 조건 추가
- 상태: OPEN
- 비고: 사용자 지시에 따라 이번 작업에서는 수정하지 않음

## [2026-06-21 15:54] TODO-20260621-1554-003 — DEFERRED

- 과업: 안정고도 도달 후 30초 순항
- 미완료 이유: 3·4단계 진단을 우선하고 전체 제작을 중단하라는 사용자 지시
- 선행 조건: TODO-20260621-1554-001과 TODO-20260621-1554-002 완료
- 상태: DEFERRED


## [2026-06-21 18:45] TODO-20260621-1554-001 — DONE

- 대상 TODO: 4단계 안전 상승 제어 구성
- 완료 내용: heading 135.01 deg와 altitude 1000 ft 폐루프 자동조종을 AGL 20 ft에서 결합
- 관련 파일: scripts/c172x/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml
- 검증 결과: 이륙·상승·고도 포착·30초 순항 완료, 과대 롤과 실속 없음
- 남은 리스크: 안정화 시간 개선 가능

## [2026-06-21 18:45] TODO-20260621-1554-002 — DONE

- 대상 TODO: Stage 4 완료 판정 보강
- 완료 내용: 최종 순항 완료 조건에 고도, 수직속도, 속도, 받음각, 롤, 피치 범위 추가
- 관련 파일: scripts/c172x/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml
- 검증 결과: 최종 30초 구간 전 수치가 허용 범위 유지
- 남은 리스크: 없음

## [2026-06-21 18:45] TODO-20260621-1554-003 — DONE

- 대상 TODO: 안정고도 도달 후 30초 순항
- 완료 내용: AGL 약 953~963 ft에서 30초 안정 순항 완료
- 검증 결과: 속도 103.43~105.79 KCAS, h-dot -0.20~0.46 ft/s, roll 약 -0.07~-0.04 deg
- 남은 리스크: 없음

## [2026-06-21 18:45] TODO-20260621-1845-001 — DEFERRED

- 과업: 공용 runner의 planet 기본값 정책 명확화
- 발견된 문제: C172X에서 --planet을 생략하면 비자전 구형 지구가 선택됨
- 현재 조치: README와 실행 명령에 --planet default 필수 표기
- 보류 이유: 전역 기본값 변경은 기존 시나리오 회귀 가능성이 있어 이번 범위에서 제외
- 상태: DEFERRED


## [2026-06-23 08:56] TODO-20260623-0856-001 — OPEN

- 과업: 5.7 시나리오를 QGroundControl에 실시간 표시
- 필요한 작업: PX4 SITL jsbsim_bridge로 c172x_empty_cg_aligned와 RKSS 초기조건 연결, UDP 14550 telemetry 확인, QGC map·flight instruments 검증
- 선행 조건: runscript가 제어권을 가질지 PX4 actuator가 제어권을 가질지 결정
- 상태: OPEN
- 남은 리스크: 현재 standalone runscript와 PX4 HIL actuator 입력을 동시에 사용하면 제어 명령 충돌 가능

## [2026-06-23 08:56] TODO-20260623-0856-002 — DEFERRED

- 과업: 엔진 정지 후 비상 활공·최적 활공속도·비상착륙 시나리오
- 현재 상태: 이번 5.7은 비제어 추락으로 완료
- 보류 이유: 사용자 요청은 추락 추가이며 조종 가능한 비상절차는 별도 목적
- 상태: DEFERRED


## [2026-06-23 09:25] TODO-20260623-0925-001 — OPEN

- 과업: `scripts/c172x/README.md`의 `c172x_empty_cg_aligned` 실행 예시 경로 정리
- 발견된 문제: 새 전용 폴더가 생성되었지만 기존 `scripts/c172x/README.md`에는 여전히 `scripts/c172x/initial_condition/2.2...`와 `scripts/c172x/runscript/5.6...`, `5.7...` 경로 예시가 남아 있음
- 필요한 작업: 기존 문서의 RKSS 14L `c172x_empty_cg_aligned` 실행 예시를 새 `scripts/c172x_empty_cg_aligned/` 경로로 갱신하거나, 전용 README로 안내
- 상태: OPEN
- 관련 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`

## [2026-06-23 09:25] TODO-20260623-0925-002 — DEFERRED

- 과업: `c172x_empty_cg_aligned` 전용 시나리오의 원본/복사본 동기화 정책 확정
- 발견된 문제: `scripts/c172x/`에 원본 RKSS 14L XML이 남아 있고 `scripts/c172x_empty_cg_aligned/`에 복사본이 생김
- 필요한 작업: 향후 기준 위치를 `scripts/c172x_empty_cg_aligned/`로 확정하고 기존 `scripts/c172x/` 파일을 deprecated 처리할지 결정
- 상태: DEFERRED
- 보류 이유: 기존 로그와 문서가 `scripts/c172x/` 경로를 참조하므로 즉시 삭제나 이동은 회귀·추적성 리스크가 있음
- 관련 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/`, `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_empty_cg_aligned/`

## [2026-06-23 09:50] TODO-20260623-0950-001 — OPEN

- 과업: `--live-3d` 실제 GUI 창 수동 검증
- 발견된 문제: 자동 검증에서는 Matplotlib GUI 창 표시를 확인하지 못함
- 필요한 작업: WSLg/X11 display가 활성화된 터미널에서 `python3 scripts/run_jsbsim_timestamped.py --live-3d`를 실행하고 `c172x_empty_cg_aligned`, `2.2`, `5.7` 조합으로 실시간 궤적 창이 갱신되는지 확인
- 상태: OPEN
- 관련 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`, `/home/junyeopkwon/jsbsim_workflow/scripts/live_trajectory_3d.py`
- 권장 검증 명령어: `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_empty_cg_aligned --init scripts/c172x_empty_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x_empty_cg_aligned/runscript/5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml --planet default --live-3d`
- 남은 리스크: display 환경이 없으면 live 창이 뜨지 않음

## [2026-06-30 10:00] TODO-20260630-1000-001 — OPEN

- 과업: 선택형 `--flightgear` 실제 GUI 수신 검증
- 발견된 문제: runner에는 FlightGear 스트림 옵션을 추가했지만 실제 Windows FlightGear 창에서 수신되는지는 아직 확인하지 않음
- 필요한 작업: Windows PowerShell에서 FlightGear를 `--fdm=external --native-fdm=socket,in,60,,5500,udp`로 실행한 뒤 WSL에서 `--flightgear` 옵션으로 JSBSim 실행
- 상태: OPEN
- 관련 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`, `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/output/fg_visual_5500.xml`
- 남은 리스크: `fg_visual_5500.xml`의 IP `172.29.80.1`이 현재 Windows host IP와 다르면 FlightGear가 수신하지 못함

## [2026-06-30 14:25] TODO-20260630-1425-001 — OPEN

- 과업:
  - ADS workflow 실제 실행 검증 및 source/workflow 동기화 정책 확정
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS/runscript/1.0__gimpo_30m_hover_run.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS/initial_condition/1.0__gimpo_ground_init.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS
  - /home/junyeopkwon/jsbsim_workflow/engine_variants/ADS
  - /home/junyeopkwon/jsbsim/aircraft/ADS
  - /home/junyeopkwon/jsbsim/engine/ADS_*.xml
- 내용:
  - 후속 승인 후 runner로 ADS model load 및 hover 실행을 검증해야 함
  - 실행 후 logs/csv/raw/ADS, logs/csv/si/ADS, logs/console/ADS, plots/ADS, results/ADS에 산출물이 정상 생성되는지 확인해야 함
  - ADS source tree 원본과 workflow snapshot 중 어느 쪽을 편집 기준으로 삼을지 정해야 함
  - ADS battery/pusher 전용 output property가 runner 후처리에 충분한지 확인해야 함
- 상태:
  - OPEN
- 권장 후속 작업:
  - python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py --aircraft ADS --init /home/junyeopkwon/jsbsim_workflow/scripts/ADS/initial_condition/1.0__gimpo_ground_init.xml --runscript /home/junyeopkwon/jsbsim_workflow/scripts/ADS/runscript/1.0__gimpo_30m_hover_run.xml --planet default --no-flightgear
  - 첫 실행 전에는 model load와 짧은 run부터 수행
- 남은 리스크:
  - 아직 JSBSim 실제 실행을 하지 않았으므로 runscript/runner 단계 문제는 남아 있음


## [2026-06-30 14:34] TODO-20260630-1434-001 — OPEN

- 과업: jsbsim_workflow 원격 저장소 연결 및 push
- 상태: OPEN
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 발견 내용: 로컬 Git 저장소와 커밋은 생성되었으나 remote URL이 없어 원격 저장소 등록 및 push는 수행하지 않음
- 필요한 작업: 원격 저장소 생성 또는 기존 저장소 URL 제공, git remote add origin 실행, git push -u origin main 실행
- 관련 파일: /home/junyeopkwon/jsbsim_workflow/.gitignore, /home/junyeopkwon/jsbsim_workflow/docs/agent-log/
- 검증 필요 항목: 원격 저장소에서 파일 목록과 ignored 산출물 제외 여부 확인
- 남은 리스크: 원격 저장소 기본 브랜치명, 인증 방식, 대용량 파일 정책에 따라 push 절차가 달라질 수 있음


## [2026-06-30 15:20] TODO-20260630-1520-001 — OPEN

- 과업: ADS 30 m hover 미션 수정 및 재검증
- 상태: OPEN
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 발견 내용: 제공 로그 기준 ADS는 30 m에 도달하지 못하고, 초기 AGL 18 m에서 하강해 지상 접촉 상태로 남음
- 필요한 작업: initial_condition의 altitude/elevation 의미 재정리, lift throttle 스케줄 또는 lift prop/motor 추력 재보정, sixdof_raw 출력에 fcs/ads/lift-throttle-cmd-norm 및 engine[0]~[4] 전체 thrust/RPM 추가
- 관련 파일: scripts/ADS/initial_condition/1.0__gimpo_ground_init.xml, scripts/ADS/runscript/1.0__gimpo_30m_hover_run.xml, aircraft_variants/ADS/ADS_propulsion.xml, engine_variants/ADS/ADS_lift_prop.xml
- 검증 필요 항목: h-agl-ft 0 근처 지상 시작, liftoff, h-agl-ft 98.4 도달, 30 m 주변 hover 유지
- 남은 리스크: 현재 모델 값은 placeholder라 추력/질량/제어기 동시 보정이 필요함


## [2026-06-30 15:27] TODO-20260630-1527-001 — OPEN

- 과업: ADS lift motor/prop 정적 추력 sweep 생성
- 상태: OPEN
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 발견 내용: 현재 로그 기반 최대 추력은 38.73 lbf이나 throttle 1.0에서의 정적 최대 추력은 별도 sweep이 필요함
- 필요한 작업: ADS 전용 runscript에 lift-throttle-cmd-norm 0.0~1.0 단계 입력, engine[0]~[3] thrust/RPM, battery current/power 출력 추가
- 검증 필요 항목: 각 throttle별 총추력, hover 가능 질량, T/W margin
- 남은 리스크: 현재 placeholder motor/prop 계수는 실제 부품 데이터가 아니므로 설계 확정에는 부적합


## [2026-06-30 18:26] TODO-20260630-1826-001 — OPEN

- 과업: ADS_mini hover 자세 및 ground contact 개선
- 상태: OPEN
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 발견 내용: 10 m hover/landing은 성공했지만 hover 중 pitch가 약 28 deg로 남고, 착륙 후 console에 gear contact chatter가 반복됨
- 필요한 작업: ADS_mini CG, rotor 위치/방향, pusher 비활성화 영향, ground_reactions damping/spring 조정, FCS pitch-rate gain 재튜닝
- 관련 파일: ADS_mini_mass.xml, ADS_mini_propulsion.xml, ADS_mini_ground_reactions.xml, ADS_mini_flight_control.xml, 1.0__gimpo_10m_hover_land_run.xml
- 검증 필요 항목: hover pitch 5 deg 이하, touchdown 후 WOW 안정, shutdown 후 contact chatter 감소
- 남은 리스크: 현재 ADS_mini는 10 m 고도 유지 검증은 되지만 자세/착륙 접촉 품질은 초기 튜닝 상태임

## [2026-07-01 00:00] TODO-20260701-0000-ADS0 — OPEN

- 과업: ADS_0 템플릿 실제 데이터 입력 및 실행 검증
- 상태: OPEN
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 관련 파일: `aircraft_variants/ADS_0`, `engine_variants/ADS_0`
- 내용: 실제 ADS 제원, 공력 테이블, 모터/프로펠러/배터리 데이터, 질량/관성/CG, 랜딩기어 값을 확보한 뒤 0 값을 대체해야 한다.
- 발견 배경: `ADS_0`는 실행 목적이 아니라 값 입력용 XML 골격으로 생성됨
- 필요한 작업: 실제 데이터 입력, 실행용 JSBSim 트리 반영, XML 로딩 검증, hover/ground reaction 검증
- 남은 리스크: 현재 상태로는 수치가 모두 0이므로 JSBSim 실행 시 물리적으로 유효하지 않거나 로딩 실패 가능성이 있다.

## [2026-07-19 23:35] TODO-20260719-2335-001 — DEFERRED

- 과업:
  - C172X 4x75kg 450 m east-heading engine-out glide trim 최적화
- 상태:
  - DEFERRED
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - 6.1 runscript는 기존 engine-out glide 사례의 fcs/pitch-trim-cmd-norm 0.18을 재사용해 heading 유지와 지면 접촉 종료를 검증했지만, 활공거리/강하율 최적 trim sweep은 수행하지 않음
- 필요한 작업:
  - pitch trim, optional elevator command, heading hold gain 영향 sweep
  - 활공거리, 강하율, 충돌 시 자세/속도 비교
- 관련 파일:
  - scripts/c172x_4x75kg_cg_aligned/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_glide_run.xml
- 검증 필요 항목:
  - trim별 time-to-impact, downrange, yaw error, impact speed, pitch/roll angle
- 남은 리스크:
  - 현재 0.18 trim은 실행 가능한 기준값이며 최적 활공 설정이라는 의미는 아님

## [2026-07-19 23:45] TODO-20260719-2345-001 — OPEN

- 과업:
  - C172X 4x75kg no-propulsion/noengine variant 생성 검토
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - 6.0 runscript는 throttle/magneto/starter/engine power를 0 또는 engine-off로 두지만, aircraft XML에 eng_io320 + prop_75in2f가 남아 있어 초반 propeller rpm/thrust transient가 발생함
- 필요한 작업:
  - c172x_4x75kg_cg_aligned에서 propulsion 블록을 제거하거나 zero-thrust dummy propulsion으로 대체한 별도 aircraft variant 생성
  - 6.0/6.1 runscript를 새 aircraft로 재실행해 propeller-rpm, thrust-lbs가 전 구간 0인지 확인
- 관련 파일:
  - aircraft_variants/c172x_4x75kg_cg_aligned/c172x_4x75kg_cg_aligned.xml
  - scripts/c172x_4x75kg_cg_aligned/runscript/6.0__gimpo_450m_east_60ms_neutral_noengine_drop_run.xml
  - scripts/c172x_4x75kg_cg_aligned/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_glide_run.xml
- 남은 리스크:
  - propulsion 제거 시 실제 C172 engine-out windmilling drag도 함께 사라지므로, 분석 목적에 따라 '엔진 정지 + 풍차 회전'과 '프로펠러 없음/정지'를 구분해야 함

## [2026-07-19 23:50] TODO-20260719-2345-001 — DONE

- 대상 TODO:
  - TODO-20260719-2345-001
- 완료 내용:
  - c172x_4x75kg_cg_aligned 기반 zero-propulsion/no-engine aircraft variant를 생성하고 6.0/6.1 runscript 실행 검증 완료
- 관련 파일:
  - aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop/c172x_4x75kg_cg_aligned_zeroprop.xml
  - scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.0__gimpo_450m_east_60ms_neutral_zeroprop_drop_run.xml
  - scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide_run.xml
- 검증 결과:
  - 6.0.2 및 6.1.1 실행 완료
  - thrust_lbs, engine_rpm, propeller_rpm 0.0 확인
- 남은 리스크:
  - 실제 windmilling prop drag를 제거한 조건이므로 기존 propeller-installed engine-off 조건과 물리 의미가 다름

## [2026-07-19 23:50] TODO-20260719-2350-001 — DEFERRED

- 과업:
  - c172x_4x75kg_cg_aligned_zeroprop generator script 추가
- 상태:
  - DEFERRED
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - inline XML 변환으로 variant를 생성했으나, generator script 추가 시도 중 Windows sandbox helper 오류가 발생함
- 필요한 작업:
  - scripts/generate_c172x_4x75kg_cg_aligned_zeroprop_variant.py를 저장소 패턴에 맞게 추가
  - 실행 후 workflow variant와 JSBSim install tree가 동일하게 생성되는지 확인
- 남은 리스크:
  - 현재 산출물은 존재하지만 재생성 절차가 별도 script로 고정되어 있지 않음

## [2026-07-20 10:57] TODO-20260720-1057-001 — OPEN

- 과업:
  - C172X 4x75kg 정상 이륙 runscript 생성 및 실행 검증
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - 설계안은 확정했으나 사용자 요청에 따라 아직 새 XML runscript를 생성하지 않음
- 필요한 작업:
  - scripts/c172x_4x75kg_cg_aligned/runscript 아래 신규 normal takeoff runscript 생성
  - aircraft=c172x_4x75kg_cg_aligned 및 RKSS 14L 초기조건 적용
  - Vr 55 KIAS, Vy 76 KIAS 기준 이벤트 구현
  - JSBSim 실행 후 liftoff, 1000 ft capture, 30 s stable climb/cruise 확인
- 검증 필요 항목:
  - XML parsing/load
  - event firing sequence
  - takeoff-state 최종 완료
  - stall/ground-contact abort 미발생
  - inertia/weight-lbs 및 V-speed 도달 시점 로그 확인
- 남은 리스크:
  - elevator command와 throttle reduction 값은 실행 결과에 따라 튜닝 필요

## [2026-07-20 11:31] TODO-20260720-1057-001 — DONE

- 대상 TODO:
  - TODO-20260720-1057-001
- 완료 내용:
  - C172X 4x75kg 정상 이륙 runscript를 생성하고 JSBSim 실행 검증 완료
  - 500 m AGL 상승 후 동일 heading으로 30.008334 s cruise 후 종료 확인
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.8__rkss14l_normal_takeoff_climb500m_cruise30_run.xml
- 검증 결과:
  - XML parse 통과
  - run 5.8.3 정상 종료
  - STATE 6 완료 및 abort 미실행 확인
- 남은 리스크:
  - 실제 항공기 성능값과의 정밀 검증은 별도 POH 성능표 비교 필요

## [2026-07-21 13:18] TODO-20260721-1318-001 — OPEN

- 과업:
  - F450 workflow raw output property 보강
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - F450 Test_F450_Launch workflow 실행은 완료됐지만 raw CSV 기본 output에는 fcs/aileron-cmd-norm, fcs/ScasEngage, fcs/throttle-cmd-norm[1..3]가 포함되지 않음
  - sixdof raw에는 일부 로터별 thrust가 포함되지만 raw CSV의 원본 quad_log.csv와 column 구성이 다름
- 필요한 작업:
  - run_jsbsim_timestamped.py에 F450 또는 multirotor 전용 추가 raw output property 목록을 도입
  - aileron, elevator, rudder, SCAS engage, indexed throttle, indexed rotor RPM, thrust, power를 raw CSV에 포함
  - 기존 C172 계열 실행에서 불필요한 column 영향이 없는지 확인
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.1__test_f450_launch_run.xml
- 검증 필요 항목:
  - F450 roll doublet command 값의 CSV 직접 확인
  - 로터 0부터 3까지 RPM, thrust, power column 존재 확인
  - 기존 c172x 실행의 CSV 변환 회귀 없음
- 남은 리스크:
  - JSBSim aircraft별 property catalog 차이 때문에 공통 output에 무조건 추가하면 일부 기체에서 column 누락 또는 경고가 발생할 수 있음


## [2026-07-23 23:07] TODO-20260723-2307-001 — OPEN

- 과업:
  - C172X 4x75kg landing full mission workflow 반영 및 실행 검증
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - 제공 bundle은 XML 문법은 유효하지만 현재 workflow/JSBSim aircraft tree에 c172x_4x75kg_cg_aligned_landing 변형이 설치되어 있지 않음
  - run_jsbsim_timestamped.py가 use aircraft를 CLI 선택값으로 덮어쓰므로 base aircraft로 5.9를 실행하면 c172ap_landing 변경이 적용되지 않음
  - Abort on excessive bank near the ground 조건에 고도 또는 mission-state 제한이 없어 loiter/복귀 중 bank overshoot로 조기 종료될 수 있음
  - 기본 output에는 simulation/mission-state와 simulation/landing-authorized가 없어 full mission 상태 전이 CSV 검증이 제한됨
- 필요한 작업:
  - aircraft_variants/c172x_4x75kg_cg_aligned_landing 및 /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_landing 배치
  - scripts/c172x_4x75kg_cg_aligned_landing/initial_condition 및 runscript 구조 생성 또는 runner 선택 경로 정책 결정
  - 5.9 runscript의 excessive-bank abort에 landing phase 또는 low-altitude guard 추가 검토
  - mission-state, landing-authorized, ap/aileron_cmd, fcs/flap-pos-deg 등을 full mission 검증용 output에 추가 검토
  - JSBSim 실행 후 event sequence, touchdown vertical speed, gear WOW 순서, runway alignment, rollout, engine shutdown 확인
- 관련 파일:
  - /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/5.9__rkss14l_full_normal_mission_run.xml
  - /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/c172ap_landing.xml
  - /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/c172x_4x75kg_cg_aligned_landing.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
- 검증 필요 항목:
  - XML parse 및 JSBSim catalog load
  - STATE 0-23 event firing sequence
  - stall abort, unintended contact abort, bank abort 미발생
  - final approach speed 58-78 KIAS 유지
  - flare height 35 ft AGL 부근 elevator/throttle command 전이
  - main gear touchdown 후 nose gear touchdown 및 2 KIAS 이하 정지
- 남은 리스크:
  - 위치 조건이 latitude 중심이라 cross-track 오차가 커도 final state가 진행될 수 있음
  - 착륙 직접제어 command 값은 초기 튜닝값이므로 runway/접지 품질은 실행 후 반복 조정 필요


## [2026-07-23 23:30] TODO-20260723-2307-001 — DONE

- 대상 TODO:
  - TODO-20260723-2307-001
- 완료 내용:
  - C172X 4x75kg landing full mission workflow 반영 및 JSBSim 실행 검증 완료
  - run 5.9.2에서 STATE 23 mission complete 확인
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_landing/
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_landing/runscript/5.9__rkss14l_full_normal_mission_run.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
- 검증 결과:
  - XML, catalog, py_compile, JSBSim run 5.9.2 통과
- 남은 리스크:
  - 착륙 품질 정량 튜닝은 별도 TODO로 분리

## [2026-07-23 23:30] TODO-20260723-2330-001 — OPEN

- 과업:
  - C172X 4x75kg full mission 착륙 품질 정량 평가 및 튜닝
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - 5.9.2는 mission complete까지 도달했지만 touchdown 전후 gear contact chatter가 일부 있음
  - Touchdown report상 접지 ground speed가 약 56.8 kt로 기록됨
  - runway centerline cross-track 오차와 touchdown 위치는 아직 정량 계산하지 않음
- 필요한 작업:
  - trajectory/CSV에서 runway centerline 기준 cross-track, touchdown 위치, rollout distance 계산
  - STATE 16-20 elevator/throttle/brake command 튜닝 후보 검토
  - gear contact chatter 감소 여부 확인
  - final approach slope 및 flare sink-rate 추출
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.2__rkss14l_full_normal_mission_raw_07232325.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.2__rkss14l_full_normal_mission_console_07232325.log
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_landing/runscript/5.9__rkss14l_full_normal_mission_run.xml
- 검증 필요 항목:
  - touchdown 지점과 runway 14L 중심선 편차
  - touchdown vertical speed 및 pitch attitude
  - nose gear slap 또는 bounce 여부
  - rollout heading 및 정지 위치
- 남은 리스크:
  - 단순 mission complete는 절차 완료 검증이며, 착륙 품질 최적화 검증은 아님


## [2026-07-24 11:50] TODO-20260724-1150-001 — OPEN

- 과업:
  - C172X 4x75kg full mission을 RWY 14L 중심선/시작 활주로 쪽으로 복귀하도록 경로 조건 재설계
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - 5.9.3은 mission complete까지 도달하지만 RWY 14L heading 135.01 deg 시작점 기준 cross-track 약 -696.6 m 위치에서 정지함
  - STATE 12-15가 latitude와 heading 중심 조건이라 runway centerline alignment를 보장하지 않음
- 필요한 작업:
  - 시작점과 runway heading 기준 along-track/cross-track property 또는 외부 계산 기반 목표점 설정
  - downwind/base/final 전환 조건을 latitude 단독이 아니라 centerline intercept 기준으로 재설계
  - final 진입 시 cross-track 허용치와 along-track distance 조건 추가
  - 재실행 후 touchdown cross-track, stop cross-track, rollout heading 확인
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_landing/runscript/5.9__rkss14l_full_normal_mission_run.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.3__rkss14l_full_normal_mission_si_07232345.csv
- 검증 필요 항목:
  - touchdown cross-track 목표 50 m 이하 또는 사용자 지정 기준
  - final approach heading 135.01 deg 근접
  - runway 시작점 또는 지정 touchdown zone 기준 along-track 범위
- 남은 리스크:
  - JSBSim runscript 내부에서 local runway-axis 계산을 직접 하려면 property/function 추가가 필요할 수 있음


## [2026-07-24 12:55] TODO-20260724-1255-001 - OPEN

- Task: Add cross-track feedback guidance for RKSS 14L landing variant.
- Background: `5.10.8` improves final cross-track from about `-696.6 m` in `5.9.3` to `-73.6 m`, but this is still not runway-width-grade precision.
- Suggested next step: use `mission/runway-cross-ft` and `mission/runway-along-ft` to compute continuous final intercept heading or localizer-like correction.
- Target: tune touchdown cross-track to within `+/-20 m` under the same initial condition before checking other conditions.
- Status: OPEN


## [2026-07-24 15:00] TODO-20260724-1500-001 - OPEN

- Task: If exact radius circular orbit is required, implement a stable bank-angle or radius-hold controller.
- Background: `5.11.2` removes rectangular straight-leg delay and gives smooth continuous turn, but it still uses AP heading setpoints rather than true radius control.
- Suggested next step: expose a bounded bank-angle target or compute heading setpoint continuously from orbit center error.
- Status: OPEN


## [2026-07-24 20:10] TODO-20260724-2010-001 - OPEN

- Task: Verify KSFO 28R `5.16` visually in FlightGear if visual/scenery alignment matters.
- Background: No-FG JSBSim validation reached `STATE 23` and runway-axis metrics are acceptable, but FlightGear live streaming was intentionally not used in this test workflow.
- Suggested next step: Run the original runner with FlightGear enabled or add a no-prompt FG-enabled helper, then inspect runway alignment and touchdown location visually.
- Status: OPEN


## [2026-07-24 21:35] TODO-20260724-2135-001 - DEFERRED

- 과업: CSV-only runner에서 미사용 plotting 함수 정의까지 제거한 slim 구조로 정리.
- 배경: 현재 파일은 기존 runner 복사본에서 실행 경로의 plotting 호출만 제거했기 때문에 동작상 문제는 없지만, 파일 내부에 미사용 plotting 함수가 남아 있다.
- 권장 후속 작업: runner 공통 로직을 모듈화하거나 CSV-only 전용 slim 파일로 정리.
- 상태: DEFERRED

## [2026-07-25 14:44] TODO-20260725-1444-001 — OPEN

- 과업:
  - LiftCruise2kg hover mission 제어 품질 튜닝 및 전용 output 보강
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - 1.0.1__hover_mission은 JSBSim workflow에서 완료됐지만 최종 위치가 시작점 기준 약 38.2 m 떨어져 있음
  - mission 의도는 ±5 m north/east 이동 후 원점 복귀 및 착륙이므로 position hold gain/sign/heading coupling 검토가 필요함
  - CSV-only runner 기본 raw output에는 LiftCruise 전용 p/mode, setpoint, indexed rotor throttle, AP command property가 부족함
- 필요한 작업:
  - LiftCruiseAP.xml position/velocity/attitude gain 및 sign 검토
  - p/heading-setpoint-rad와 north/east position hold의 body/world axis coupling 검토
  - un_jsbsim_timestamped*_*.py에 LiftCruise2kg 전용 raw output property 조건부 보강 검토
  - pusher motor와 fixed-wing surface가 실제 transition mission에서 동작하는 별도 runscript 추가 검토
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg/LiftCruiseAP.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg/FlightControl.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.0__hover_mission_run.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/LiftCruise2kg/1.0__hover_mission/1.0.1__hover_mission_raw_07251442.csv
- 검증 필요 항목:
  - 최종 원점 오차 목표값 설정 및 달성 여부
  - max roll/pitch 제한
  - vertical descent 및 gear contact chatter 여부
  - indexed lift motor command/RPM/thrust 출력 확인
- 남은 리스크:
  - 현재 모델은 preliminary aerodynamic/controller estimate라 실행 가능성과 비행 품질 검증을 분리해서 관리해야 함

## [2026-07-25 14:48] CORRECTION-20260725-1448-001 — 정정

- 대상 기록:
  - TODO-20260725-1444-001
- 정정 이유:
  - PowerShell 백틱 이스케이프 처리로 일부 식별자가 제어문자로 표시될 수 있어, TODO 내용을 plain text로 재기록함
- 정정 내용:
  - TODO는 LiftCruise2kg hover mission 제어 품질 튜닝 및 전용 output 보강이다.
  - 1.0.1__hover_mission은 workflow에서 완료됐지만 최종 위치가 시작점 기준 약 38.2 m 떨어져 있다.
  - 검토 대상은 LiftCruiseAP.xml position/velocity/attitude gain, sign, heading coupling, 그리고 runner의 LiftCruise2kg 전용 raw output property 보강이다.
  - 관련 파일은 aircraft_variants/LiftCruise2kg/LiftCruiseAP.xml, aircraft_variants/LiftCruise2kg/FlightControl.xml, scripts/LiftCruise2kg/runscript/1.0__hover_mission_run.xml, logs/csv/raw/LiftCruise2kg/1.0__hover_mission/1.0.1__hover_mission_raw_07251442.csv 이다.
- 영향 범위:
  - 기록 가독성 정정만 해당하며 실제 코드/XML/실행 결과 변경 없음
- 검증 결과:
  - TODO 상태는 OPEN 유지
- 다음 작업:
  - 전용 output property 추가 후 hover 원점 복귀 오차 튜닝

## [2026-07-25 15:09] TODO-20260725-1509-001 — OPEN

- 과업:
  - LiftCruise2kg 1.1 10 m 박스 mission 위치 추종 개선
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - 1.1__ten_meter_box_hover_land_run.xml은 요청 setpoint 시퀀스를 적용하고 정상 종료됨
  - 그러나 실제 최종 위치가 local_N/local_E 약 -203.45 m / -177.35 m로 크게 드리프트함
  - 고도는 max 10.168 m 및 착륙 후 final 0.158 m로 수직축은 대체로 동작함
- 필요한 작업:
  - LiftCruiseAP.xml의 north/east position error sign 및 velocity-to-attitude mapping 검토
  - heading setpoint와 yaw controller가 position hold 좌표계에 미치는 영향 확인
  - LiftCruise 전용 raw output property를 runner에 조건부 추가해 ap/mode, setpoint, AP command, indexed throttle/RPM/thrust를 CSV에 기록
  - 1.1 runscript 재실행 후 각 5초 hover 구간의 위치 오차를 정량화
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg/LiftCruiseAP.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg/FlightControl.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/si/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.1__ten_meter_box_hover_land_si_07251509.csv
- 검증 필요 항목:
  - 각 target hover 5초 구간의 local_N/local_E/local altitude 오차
  - 최종 수직착륙 위치와 gear contact 안정성
  - roll/pitch 제한 및 horizontal drift 감소
- 남은 리스크:
  - runscript만으로는 현재 제어기 drift를 해결할 수 없음

## [2026-07-25 16:12] TODO-20260725-1612-002 - OPEN
- 과업: simulation/mission-state를 raw CSV 컬럼으로 직접 남길 방법 검토
- 배경: runscript 내부 notify에는 mission-state가 출력되지만 JSBSim raw CSV 헤더에서는 카탈로그 미등록 custom property가 드롭됨
- 권장 후속 작업: aircraft 또는 system XML에서 mission-state를 카탈로그 property로 정의 가능한지 확인
- 상태: OPEN

## [2026-07-25 16:12] TODO-20260725-1612-001 - DONE
- 대상 TODO: TODO-20260725-1509-001 중 LiftCruise 전용 raw output property 보강 항목
- 완료 내용: 1.1 runscript output과 raw CSV 헤더를 381개 property로 1:1 대응시킴
- 관련 파일: scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
- 검증 결과: 1.1.4 raw CSV 헤더가 source XML output과 순서까지 일치
- 남은 리스크: 위치 추종 drift 튜닝 TODO는 계속 OPEN

## [2026-07-25 17:56] TODO-20260721-1318-001 - DONE

- 대상 TODO: TODO-20260721-1318-001 F450 workflow raw output property 보강
- 완료 내용: runner 3개에 F450_OUTPUT_PROPERTIES를 추가하고 F450일 때만 AP/SCAS/ESC/rotor property를 raw CSV output에 확장함
- 관련 파일: /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 검증 결과: run 1.2.9 raw CSV에서 AP/SCAS/ESC/rotor 확인 column 존재
- 남은 리스크: 일부 indexed property는 JSBSim catalog 명칭 차이로 sixdof skipped 목록에 남음

## [2026-07-25 17:56] TODO-20260725-1756-001 - OPEN

- 과업: F450 10 m box hover/land lateral position hold 튜닝
- 상태: OPEN
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 발견 내용: F450 AP bridge와 altitude hold는 동작하고 run 1.2.9는 정상 종료됐지만 205.2 s 종료 직전 local_N/local_E가 -22.40 m / 54.65 m로 10 m box mission 정밀 추종에는 미달함
- 필요한 작업: position/distance-from-start-lat-mt 및 position/distance-from-start-lon-mt와 SI local_N/E 부호 관계 정리, F450 rate-SCAS 입력에 맞는 lateral outer-loop gain/sign 재설계, disarm 이후 ground contact chatter 완화, 각 hover 구간 target error 자동 계산 추가
- 관련 파일: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml, /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/F450/1.2__ten_meter_box_hover_land/1.2.9__ten_meter_box_hover_land_raw_07251756.csv, /home/junyeopkwon/jsbsim_workflow/logs/csv/si/F450/1.2__ten_meter_box_hover_land/1.2.9__ten_meter_box_hover_land_si_07251756.csv
- 검증 필요 항목: 각 5초 hover 구간 target local_N/local_E 오차, final landing horizontal error 목표값, max roll/pitch 제한, FlightGear visual 확인
- 남은 리스크: 현재 결과는 기능 연결 검증이지 mission tracking 완료가 아님

## [2026-07-26 14:10] TODO-20260726-1410-001 — OPEN

- 과업: F450AP와 FlightControl 중첩 제어/gain 문제 분리 진단
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: F450 10 m box mission이 도착 gate를 통과하지 못하는 원인 후속 분석
- 관련 파일: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml, /home/junyeopkwon/jsbsim/aircraft/F450/FlightControl.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml
- 수행 내용: run 1.2.12에서 첫 setpoint 0,0 hover 상태에서 위치오차와 수평속도가 gate를 만족하지 못해 10 m leg로 전환되지 않음을 확인
- 변경 이유: 로그와 runscript 전환 문제를 고친 뒤에도 F450 lateral hold 자체가 불안정하거나 drifting함
- 검증 명령어: CSV-only run 1.2.12__ten_meter_box_hover_land 결과 확인
- 검증 결과: 25 s에 north/east error -10/-10, v-north/v-east 약 -35.49/16.66 fps로 gate 불만족
- 검증하지 못한 항목: 자세 PID와 각속도 PID 계층별 gain/saturation 기여도, 축 부호, position-to-attitude scaling
- 가정: 센서 stub은 현재 궤적 불량의 직접 원인이 아님
- 남은 리스크: 제어기 튜닝 없이 runscript gate만 엄격하게 유지하면 mission 진행이 멈춘 것처럼 보일 수 있음
- 다음 작업: AP lateral loop를 먼저 낮은 gain/제한값으로 안정화한 뒤 rate loop와 mixer saturation을 로그로 확인
- 관련 기록: PROGRESS-20260726-1410-001
- Git commit: 없음


## [2026-07-26 15:33] TODO-20260726-1533-001 — OPEN

- 과업: F450AP home 좌표 일반화
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow, /home/junyeopkwon/jsbsim/aircraft/F450
- 내용: ap/home-lat-deg와 ap/home-lon-deg가 현재 F450AP.xml에 고정되어 있으므로, init XML 또는 runscript에서 초기 위경도를 AP property로 주입하는 방식으로 일반화한다.
- 이유: 초기 위치가 바뀌면 signed local N/E 기준이 틀어져 position hold와 mission gate가 다시 부정확해질 수 있다.
- 상태: OPEN
- 권장 검증: 다른 초기 위경도에서 hover-only와 10 m mission을 재실행해 local_N/E 오차를 비교한다.

## [2026-07-26 15:33] TODO-20260726-1533-002 — OPEN

- 과업: F450 제어기 동특성 튜닝
- 대상 프로젝트: /home/junyeopkwon/jsbsim, /home/junyeopkwon/jsbsim_workflow
- 내용: 현재 미션은 통과하지만 FlightControl rate loop와 F450AP attitude loop가 중첩된 구조이고 actuator lag가 없으므로, 실제성 개선을 위해 rate/attitude/position gain과 ESC/motor lag를 별도 튜닝한다.
- 이유: 현재 수정은 10 m hover mission 재현을 위한 기능 검증 단계이며 실제 기체 응답성까지 보장하지 않는다.
- 상태: OPEN
- 권장 검증: step response, saturation 비율, motor command clipping, attitude/rate tracking error RMS를 로그로 평가한다.


## [2026-07-26 16:46] TODO-20260726-1646-001 — OPEN

- 과업: LiftCruise2kg home 좌표 및 latitude type 동기화
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow, /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg
- 내용: init 파일의 latitude type과 AP local N/E 계산 기준을 명시적으로 연결한다. 현재는 init latitude가 geocentric으로 해석되어 AP가 position/lat-gc-deg를 사용한다.
- 이유: 향후 init에 type="geodetic"이 추가되거나 위치가 변경되면 AP home 기준이 다시 틀어질 수 있다.
- 상태: OPEN
- 권장 검증: init latitude type을 geodetic/geocentric 각각으로 둔 smoke test를 만들고 AP local N/E 초기값이 0 근처인지 확인한다.

## [2026-07-29 10:54] TODO-20260729-1054-001 - OPEN

- 과업:
  - c172x alpha-limit 유지 baseline과 no-alpha-limit 결과 비교
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - no-alpha-limit 변형의 run 7.0.2는 정상 종료했지만, alpha 제한 제거가 궤적과 접지 조건에 미친 효과는 기존 alpha-limit 모델과 같은 초기조건으로 비교해야 분리 가능함
- 필요한 작업:
  - 기존 c172x_4x75kg_cg_aligned_zeroprop 모델에 동일 500 m MSL, RKSS14L, theta 2.5 deg 초기조건을 적용한 baseline run 추가
  - 접지 시각, 접지 속도, 최종 위치, alpha 범위, 자세 범위를 비교
  - 필요하면 plotting runner로 3D/XY/상태 그래프 생성
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.0__rkss14l_500m_ubody60_theta25_init.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop/7.0.2__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_raw_07291053.csv
- 검증 필요 항목:
  - alpha-limit baseline과 no-alpha-limit 결과의 차이
  - FlightGear visual alignment
  - 공력 table 외삽 구간 진입 여부
- 남은 리스크:
  - alpha 제한을 제거해도 table data 범위 밖의 계수 해석은 JSBSim table extrapolation 동작에 의존함

## [2026-07-29 11:08] TODO-20260729-1108-001 - OPEN

- 과업:
  - c172x no-thrust fixed-control 초기조건 재정의 및 비교 run
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - 현재 theta 2.5 deg, wbody 0, alpha 0 조건은 초기 상승 경로와 nose-up 자유응답을 만든다. 사용자가 기대한 것이 수평 시작 또는 안정 활공이라면 초기조건을 다시 정의해야 한다.
- 필요한 작업:
  - theta 2.5 deg 유지 및 gamma 0 deg 조건의 wbody 약 +2.62 m/s 비교 run
  - theta 0 deg, ubody 60 m/s, wbody 0 비교 run
  - no-thrust fixed-control steady glide trim 조건 산출 가능성 검토
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.0__rkss14l_500m_ubody60_theta25_init.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop/7.0.3__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_raw_07291059.csv
- 남은 리스크:
  - trim 없이 초기 속도/자세만 지정하면 C172 longitudinal natural mode가 계속 크게 나타날 수 있음

## [2026-07-29 11:20] TODO-20260729-1120-001 - OPEN

- 과업:
  - c172x no-thrust neutral 조건의 pitch-up moment 제거 또는 trim 활공 조건 산출
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - theta 0, initial vertical velocity 0 조건에서도 7.1은 637.64 m까지 상승했다. 초기 원인은 속도 방향보다 neutral 상태의 positive pitch moment가 더 지배적이다.
- 필요한 작업:
  - Cmo 0.1을 유지한 상태에서 필요한 elevator trim 또는 초기 alpha/theta 조건을 산출
  - 또는 fixed-control 테스트 목적에 맞게 Cmo zero variant를 별도로 만들어 비교
  - no-thrust steady glide 상태를 찾는 trim/탐색 스크립트 작성
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.1__rkss14l_500m_ubody60_level_init.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop/7.1.2__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop_raw_07291115.csv
- 남은 리스크:
  - Cmo를 0으로 바꾸면 원본 C172 공력 모멘트를 바꾸는 것이므로 별도 variant로 분리해야 함

## [2026-07-29 11:25] TODO-20260729-1125-001 - OPEN

- 과업:
  - c172x no-alpha-limit neutral pitch moment 보정 실험
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - theta -5 deg에서도 초기 qdot 약 +2.99 rad/s^2가 유지되어 최고 고도 633.31 m까지 상승함
- 필요한 작업:
  - elevator trim required value 추정
  - Cmo 0 또는 reduced Cmo 별도 variant 생성 여부 검토
  - qdot 초기값이 0에 가까운 fixed-control initial condition 탐색
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.2__rkss14l_500m_ubody60_thetam5_init.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.2__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop/7.2.1__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop_sixdof_raw_07291122.csv
- 남은 리스크:
  - Cmo 조정은 공력 모델 변경이므로 원본 보존 variant로만 수행해야 함

## [2026-07-29 11:42] TODO-20260729-1142-001 - OPEN

- 과업:
  - elevator trim 기반 qdot0 run과 Cmo 보정 run 비교
- 상태:
  - OPEN
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 발견 내용:
  - Cmo=-0.01523148 variant는 초기 qdot을 거의 0으로 만들지만 공력 모델 자체를 변경한다. 실제 비행 trim 관점에서는 elevator trim 또는 alpha/theta/speed 조합을 찾는 편이 더 물리적일 수 있다.
- 필요한 작업:
  - 원래 Cmo=0.1 모델에서 elevator-pos-rad 또는 pitch-trim-cmd-norm으로 초기 moment를 상쇄하는 값 계산
  - Cmo 보정 run 8.1과 elevator trim run의 고도, alpha, theta, 접지 시각 비교
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/8.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmotrimq0_drop/8.1.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmotrimq0_drop_sixdof_raw_07291137.csv
- 남은 리스크:
  - Cmo 보정값은 현재 초기조건에 맞춘 값이며 속도/밀도/다른 alpha 조건에 일반화되지 않을 수 있음

## [2026-07-29 12:05] TODO-20260729-1205-001 - OPEN

- 과업: no-thrust steady glide full trim 산출
- 상태: OPEN
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 발견 내용: JSBSim native do_simple_trim=1은 엔진/프로펠러 제거 조건에서 throttle/udot 축을 trim할 수 없어 실패함; 현재 9.3은 초기 pitch moment/qdot 중심 fixed elevator trim임
- 필요한 작업: alpha, theta/gamma, elevator fixed bias를 동시에 조정하는 no-thrust glide trim 수치 탐색
- 관련 파일: scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/9.2__rkss14l_500m_ubody60_level_native_trim_freeze_noalphalimit_drop_run.xml; aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_elevtrimq0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_elevtrimq0.xml
- 남은 리스크: fixed elevator trim 값은 속도 60 m/s, alpha 0 deg, theta 0 deg 초기조건에 국한됨


## [2026-07-31 10:56] TODO-20260731-1056-001 - OPEN

- 과업: FlightGear에서 `5.22__ksfo28r_centerline_balanced_final_landing_run.xml`를 실제 시각 검증.
- 배경: JSBSim CSV 기준으로 centerline 오차는 크게 개선됐지만, 사용자가 관찰한 문제는 FlightGear 화면에서 발생했다.
- 권장 후속 작업: FlightGear를 `--timeofday=noon`, fuel props, external FDM 옵션으로 실행한 뒤 `5.22`를 `--flightgear`로 재생해 takeoff roll, AP transition, touchdown alignment를 화면에서 확인.
- 상태: OPEN

## [2026-07-31 13:55] TODO-20260731-1355-001 — OPEN

- 과업: `5.27` AP altitude hold 재투입 transient 추가 완화
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 관련 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml`
- 발견 내용: `5.27.1`은 로테이트 직후 20-35초 튐은 해결했지만 `ap/altitude_hold`가 켜지는 46.38초 부근에 `ap/elevator_cmd` range `1.456`, `fcs/elevator-pos-rad` range `0.398` transient가 남음
- 상태: OPEN
- 권장 후속 작업: AP 재투입 조건 또는 altitude setpoint handoff를 별도 이벤트로 미세 조정하고 FlightGear에서 0-100초 시각 확인

## [2026-07-31 17:23] TODO-20260731-1723-001 — OPEN

- 과업: MATLAB v7 plotter 실기동 검증
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 관련 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`
- 상태: OPEN
- 내용: MATLAB에서 `run_jsbsim_csv_plotter_v7.m`를 실행하고 F450 raw CSV 및 combined CSV를 각각 로드한 뒤 `표준 분석 PNG + summary CSV 저장` 버튼으로 PNG/CSV 생성 여부를 확인해야 함
- 필요한 추가 조건: MATLAB GUI 실행 환경
- 남은 리스크: MATLAB 버전 호환성 및 실제 GUI callback 런타임 오류 가능성
## [2026-07-31 17:47] TODO-20260731-1747-001 — OPEN

- 과업: MATLAB v7 plotter GUI 실사용 검증
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 관련 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`
- 상태: OPEN
- 내용: MATLAB GUI에서 F450 CSV를 로드하고 2D `범례 이름`, 2D/3D 글씨 크기, 3D 범례 문구 테이블, 표준 분석 PNG export 결과를 실제로 확인해야 함
- 필요한 추가 조건: MATLAB GUI 실행 및 사용자가 생성된 PNG 시각 검수
- 남은 리스크: batch `checkcode`는 통과했지만 GUI callback 런타임 문제는 별도 확인 필요
## [2026-07-31 18:02] TODO-20260731-1802-001 — OPEN

- 과업: 2D 직접 범례 입력 GUI 검증
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 관련 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`
- 상태: OPEN
- 내용: MATLAB GUI에서 2D Y 계열 여러 개를 선택하고 `범례 이름` 행에 쉼표 구분 문구를 입력한 뒤, 범례와 PNG 저장 결과가 사용자 입력대로 나오는지 확인해야 함
- 필요한 추가 조건: MATLAB GUI 실행 및 시각 확인
- 남은 리스크: 정적 분석은 통과했지만 GUI 표시 결과는 실제 실행으로 확인 필요

## [2026-08-10 22:35] TODO-20260810-2235-001 — OPEN

- 과업: F450_DATCOM 공력 적용 후 position-hold hover 및 gain tuning 추가 검증
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 관련 파일: /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/*, ircraft_variants/F450_DATCOM/*, scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml
- 상태: OPEN
- 내용: 이번 미션은 attitude-mode step 비교용이라 위치 고정 hover 안정성까지 검증하지 않았다. 10 m position-hold hover 전용 미션을 별도로 만들어 30-60초 이상 고도/수평위치/자세 안정성을 확인하고, 필요하면 F450AP.xml gain과 hover throttle base를 조정해야 한다.
- 필요한 추가 조건: position-hold 기준 오차 허용범위 정의, 필요 시 FlightGear 시각 검증
- 남은 리스크: DATCOM reference geometry가 기존 F450 질량/추진 모델 대비 커서 공력 모멘트/힘이 controller tuning에 큰 영향을 줄 수 있음


## [2026-08-10 22:40] CORRECTION-20260810-2240-001 — 정정

- 대상 기록: TASK-20260810-2235-001, PROGRESS-20260810-2235-001, DECISION-20260810-2235-001, TODO-20260810-2235-001, INDEX-20260810-2235-001
- 정정 이유: PowerShell command string에서 Markdown backtick escape가 적용되어 일부 경로와 row/table 표기가 제어문자로 기록됨
- 기존 내용: 일부 backtick-wrapped path 및 row+table, row+column 표기가 깨져 보임
- 정정 내용: 실제 변경 파일은 /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/initial_condition/1.0__ground_park_heading0_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml 이다. JSBSim 호환을 위해 DATCOM base table 6개는 row plus table 구조에서 row plus column 구조로 재구성했으며 숫자 데이터는 변경하지 않았다.
- 영향 범위: 작업 기록 문서 표기 정정만 해당. 모델 파일, runscript, CSV 로그에는 영향 없음
- 검증 결과: INDEX.md 최신 tail에서 정정 항목이 append됨
- 다음 작업: 최종 응답에서는 정정된 경로와 결과만 보고

## [2026-08-11 16:45] TODO-20260811-1645-001 — OPEN

- 과업: AD3000 workflow run을 batch 체계에 편입하고 hover split 보정
- 상태: OPEN
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 발견 내용: AD3000 smoke runscript는 생성되었지만 workflow_all_cases_initial_settings.xlsx와 batch runner에는 아직 등록하지 않았다. 8초 hover run은 FPE로 실패했다.
- 필요한 작업: front/rear collective split 보정 후 8초 smoke run 재검증, 결과 CSV를 workflow 로그 구조에 맞게 저장, 필요 시 workflow Excel에 case 등록
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_generate_aircraft.py, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000/runscript/1.0__smoke_hover_run.xml
- 남은 리스크: batch 연결 전에는 workflow 자동 실행 대상이 아님

## [2026-08-11 00:00] TODO-20260811-0000-002 — OPEN

- 과업: AD3000 cruise prop 및 hover trim 재검증
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 제품 기반 propulsion 구성 후 남은 미검증 항목 추적
- 관련 파일: AD3000_cruise_prop_Falcon_C2E_20x10.xml, Propulsion.xml, AD3000_smoke_hover_run.xml
- 수행 내용: Falcon C2E 20x10 직접 성능표 미확보와 8초 hover run Floating point exception 리스크를 TODO로 기록함
- 변경 이유: 현재 cruise prop 계수와 hover 안정성은 추정 또는 미해결 상태이므로 후속 검증이 필요함
- 검증 명령어: JSBSim smoke hover run --end=1.5
- 검증 결과: 단기 실행은 성공했으나 장기 hover 안정성은 미해결
- 검증하지 못한 항목: Falcon 20x10 직접 thrust/power table, full duration hover run, 실측 전진비별 prop polar
- 가정: 공개 Falcon 22x12 표를 20x10 추정에 임시 사용함
- 남은 리스크: cruise 추력 과대 또는 과소 추정 가능성, hover pitch divergence 가능성
- 다음 작업: 실제 20x10 bench data 확보, cruise prop XML 재보정, front/rear collective split 또는 trim 로직 반영
- 관련 기록: DECISION-20260811-0000-002
- Git commit: 없음

## [2026-08-11 17:11] CORRECTION-20260811-1711-001 — 정정

- 대상 기록: TASK-20260811-0000-002, PROGRESS-20260811-0000-002, DECISION-20260811-0000-002, TODO-20260811-0000-002, INDEX-20260811-0000-002
- 정정 이유: 제품 기반 propulsion 반영 기록을 append할 때 기록 시각을 임시값 2026-08-11 00:00으로 남김
- 기존 내용: 기록 시각이 2026-08-11 00:00 또는 ENTRY ID 20260811-0000으로 표기됨
- 정정 내용: 해당 항목의 실제 기록 시각은 2026-08-11 17:11 KST임. 기록 내용과 검증 결과는 그대로 유효함
- 영향 범위: docs/agent-log 아래 Markdown 기록의 메타데이터 시각 표기
- 검증 결과: append-only 방식으로 정정 기록을 추가함
- 다음 작업: 이후 기록에서는 실제 KST 시각을 사용

## [2026-08-12 09:00] TODO-20260812-0900-001 — OPEN

- 과업: AD3000 Falcon C2E 20x10 cruise prop 실제 데이터 확보 및 재보정
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 현재 VSC22.1x7.4 임시 cruise 모델의 남은 리스크 추적
- 관련 파일: AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, AD3000_cruise_prop_Falcon_C2E_20x10.xml, Propulsion.xml
- 수행 내용: 공개표 부재 때문에 Falcon 20x10을 기본 참조에서 제외하고 VSC 22.1x7.4 공개표를 임시 적용함
- 변경 이유: 실제 의도 prop과 임시 모델의 차이를 추적하기 위함
- 검증 명령어: xmllint, JSBSim catalog, JSBSim smoke run --end=1.5
- 검증 결과: 단기 로딩 및 실행 통과
- 검증하지 못한 항목: Falcon C2E 20x10 직접 thrust/power table, full transition 성능, 8초 hover 안정성
- 가정: 임시 VSC 22.1x7.4 cruise prop은 데이터 근거 확보용이며 설계 최종값이 아님
- 남은 리스크: 실제 20x10 적용 시 cruise thrust, power, RPM 한계가 바뀜
- 다음 작업: Falcon 20x10 성능표 또는 bench test 데이터 확보, AD3000_cruise_prop_Falcon_C2E_20x10.xml 재보정 후 Propulsion.xml 참조 전환
- 관련 기록: DECISION-20260812-0900-001
- Git commit: 없음

## [2026-08-13 13:39] TODO-20260813-1339-001 — OPEN

- 대상 TODO: standard_vtol_demo_jsbsim 후속 검증 및 시나리오 확장
- 상태: OPEN
- 내용: build_standard_vtol_jsbsim.py에 DATCOM postprocess를 통합해 재실행 가능하게 정리하고, 천이 없는 시나리오 시동-수직이륙-상승-하강-호버링-수직착륙-시동종료를 구성한다. 이후 DATCOM 3D Mach breakpoint 제어증분 보간 복원과 전방/후방 천이 시나리오를 진행한다.
- 관련 파일: aircraft_variants/standard_vtol_demo_jsbsim/*, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo/*, /home/junyeopkwon/jsbsim/scripts/standard_vtol_demo_*.xml
- 검증 필요 항목: hover throttle, 지상 접촉 안정성, 외력 방향, pusher 방향, control surface sign, 공력 스케일.
- 남은 리스크: 현재 검증은 단기 property 연결 확인이며 정상 비행 가능성을 의미하지 않는다.

## [2026-08-13 14:45] TODO-20260813-1445-001 — OPEN

- 과업: standard_vtol_demo 다음 단계 미션 확장
- 상태: OPEN
- 내용: 천이를 제외한 정상 비행 시나리오 또는 hover 기반 위치 제어 미션을 구성한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo/runscript/1.0__rkss14_vertical_takeoff_hover_land_run.xml
- 남은 리스크: 현재 미션은 수직축 중심이며 수평 위치 유지/항법 제어는 아직 구성하지 않았다.

## [2026-08-13 14:45] TODO-20260813-1445-002 — DEFERRED

- 과업: standard_vtol_demo 천이 미션 구성
- 상태: DEFERRED
- 내용: 전방천이(멀티콥터 -> 고정익), 미션, 후방천이(고정익 -> 멀티콥터)는 다음 단계에서 별도 설계한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/standard_vtol_demo_hover.xml
- 남은 리스크: 천이 단계에서는 pusher motor, 고정익 공력, pitch/airspeed 제어 및 flightcontrol 구조 재검토가 필요하다.

## [2026-08-13 15:04] TODO-20260813-1504-001 — OPEN

- 과업: 천이 단계 전 propulsion 구조 판단
- 상태: OPEN
- 내용: 현재 standard_vtol_demo 계열은 pusher/lift force가 ExternalReactions.xml에 있고 JSBSim propulsion 섹션은 없다. 전방천이/고정익 미션 전에 propulsion 섹션으로 재구성할지, external_reactions를 유지할지 결정한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/ExternalReactions.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml
- 남은 리스크: pusher thrust와 고정익 공력/속도 제어가 결합되는 천이 구간에서 현재 force-only 구조의 한계가 드러날 수 있다.

## [2026-08-13 15:50] TODO-20260813-1550-001 — OPEN

- 과업: standard_vtol_demo_hover FW/transition 모델 고도화
- 상태: OPEN
- 내용: DATCOM elevator effectiveness 또는 별도 pitch control surface 모델을 확보하고, FW segment에서 mc-weight를 PX4처럼 0.0까지 낮출 수 있도록 fixed-wing attitude/TECS 제어를 구성한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Aero_DATCOM.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml
- 남은 리스크: 현재 천이 runscript는 JSBSim standalone proof이며 PX4 strict transition equivalence는 아니다.

## [2026-08-13 17:16] TODO-20260813-1445-001 — DONE

- 대상 TODO: standard_vtol_demo 다음 단계 미션 확장
- 완료 내용: standard_vtol_demo_hover 기준 천이 없는 멀티콥터 조종자격증 유사 3.0 mission runscript를 추가하고 runner 메뉴 78 -> 2 -> 3으로 실행 검증했다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml
- 검증 결과: final mission/state=32, motor-armed=0, esc-out[0..4]=0, mc-weight=1, pusher esc-out=0
- 남은 리스크: 실제 시험 코스 geometry와 waypoint/position 추종은 별도 TODO로 남김

## [2026-08-13 17:16] TODO-20260813-1716-001 — OPEN

- 과업: standard_vtol_demo_hover 자격시험 유사 미션의 waypoint/position controller 고도화
- 상태: OPEN
- 내용: 현재 3.0은 body speed target 기반 sequence라서 실제 시험 코스의 40-50 m 전후진, 삼각/원주 형상, 착륙점 복귀를 엄밀히 보장하지 않는다. 다음 단계에서 NE 좌표 기준 waypoint/position hold, yaw/heading command, 원주 궤적 generator를 구성한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml
- 검증 필요 항목: 출발점 복귀 오차, 각 코스 거리, 고도 3-5 m 유지, hover 5 s 정지 조건, 착륙 gear force 저감, yaw/heading 추종
- 남은 리스크: 현재 final displacement는 약 N/E=10.57/19.07 m이고 max distance=22.19 m로, mission proof에는 충분하지만 시험장 geometry 재현에는 부족하다.
## [2026-08-13 17:41] TODO-20260813-1741-001 — OPEN

- 과업: 3.0 mission의 완전한 상대시간 state-age timer 및 waypoint 완료 조건 추가
- 상태: OPEN
- 내용: 현재 3.0은 state gate + 절대 trigger 시각으로 이전 state 완료 전 다음 state 진행은 막았지만, trigger 시각보다 이전 state 완료가 늦어지는 경우 hold duration이 줄어들 수 있다. 다음 단계에서 mission/state-age-sec 또는 phase-start-sec를 신뢰성 있게 구성하고, position/velocity/yaw tolerance 기반 완료 조건을 추가한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml
- 검증 필요 항목: 각 hover 5 s 보장, 각 leg 도달 판정, 원주/삼각 waypoint geometry, 착륙점 복귀, yaw/heading command
- 남은 리스크: 현재 mission proof는 통과했지만 실제 시험 코스의 엄밀한 완료 조건은 아직 부족하다.
## [2026-08-13 17:45] TODO-20260813-1741-001 — SUPERSEDED

- 대상 TODO: 3.0 mission의 완전한 상대시간 state-age timer 및 waypoint 완료 조건 추가
- 교체 이유: state-gated 수정본을 3.0이 아니라 3.1로 분리했으므로 TODO 대상 파일명을 정정한다.
- 기존 대상: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml
- 신규 대상: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.1__rkss14_multicopter_certificate_mission_state_gated_run.xml
- 남은 리스크: 3.1은 state gate + 절대 trigger 시각 방식이며 완전한 relative state-age timer는 아직 없음.
## [2026-08-13 18:07] TODO-20260813-1807-001 — OPEN

- 과업: 20 kg metric/mass 반영 후 hover controller 재튜닝
- 상태: OPEN
- 내용: emptywt를 20 kg으로 낮춘 뒤 기존 hover throttle base/gain을 그대로 사용하자 3.1 미션에서 4 m target 대비 최대 h-agl 약 6.25 m overshoot가 발생했다. 다음 단계에서 fcs/hover-throttle-base-norm, altitude P/D, runscript climb/landing base 값을 20 kg 기준으로 재조정한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.1__rkss14_multicopter_certificate_mission_state_gated_run.xml
- 검증 필요 항목: 4 m target overshoot, hover steady-state collective, landing gear force, final touchdown 안정성
- 남은 리스크: 현재 비행 미션은 실행 완료되지만 고도 품질은 mass 변경 전 controller 기준임.
## [2026-08-13 18:14] TODO-20260813-1807-001 — DONE

- 대상 TODO: 20 kg metric/mass 반영 후 hover controller 재튜닝
- 완료 내용: hover throttle base를 0.535로 산출/반영하고 3.2/3.3/3.4 runscript로 검증했다. 3.4 기준 hover avg collective=0.5345, hmax=4.065 m.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.4__rkss14_multicopter_certificate_mission_state_gated_20kg_hover_smooth_spooldown_run.xml
- 검증 결과: 3.4.1 final state33, motor-armed=0, esc-out[0..4]=0, pusher=0
- 남은 리스크: landing gear force는 5.02W로 여전히 높아 추가 착륙 제어/gear 튜닝 필요

## [2026-08-13 18:14] TODO-20260813-1814-001 — OPEN

- 과업: 착륙 충격 저감을 위한 vertical velocity landing controller 또는 gear damping 튜닝
- 상태: OPEN
- 내용: 3.4에서 staged landing과 slow spooldown을 적용했지만 max gear force가 221.64 lbf, 약 5.02W로 남았다. 다음 단계에서 h-dot target 기반 descent controller, landing flare, ground reaction spring/damping을 재설계한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Gear.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.4__rkss14_multicopter_certificate_mission_state_gated_20kg_hover_smooth_spooldown_run.xml
- 검증 필요 항목: touchdown h-dot, max gear force, bounce 여부, motor spooldown 후 안정 정지
- 남은 리스크: gear force가 높으면 이후 정상 착륙 시나리오의 물리 품질이 낮아진다.
## [2026-08-14 10:54] TODO-20260814-1054-002 — OPEN

- 과업: QGC 저고도 시험 미션 후 combined CSV 검토
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 상태: OPEN
- 이유: 현재 CSV 변환은 preflight/sensor 확인 로그 기준이며 실제 arm/takeoff/land mission 데이터는 아직 없음
- 권장 검증: QGC에서 Arm -> Takeoff 5 m -> Land -> Disarm 후 생성된 ULog를 px4_ulog_to_combined_csv.py로 변환

## [2026-08-18 11:35] TODO-20260818-1135-001 — OPEN

- 과업: 새 combined 제어 분석 컬럼 기준으로 주요 과거/비교 scenario 재실행 여부 결정
- 대상 프로젝트: `/home/junyeopkwon/evtol-6dof/jsbsim_workflow`
- 요청 내용: combined CSV 로그 분석 컬럼 확장
- 관련 파일: `scripts/run_jsbsim_timestamped_combined_csv_only.py`, `logs/csv/combined/`
- 수행 내용: C172 5.16 대표 케이스는 새 컬럼으로 재실행 검증 완료
- 변경 이유: 기존 `logs/csv/combined` 아래 과거 CSV에는 새 heading/roll/control-chain 컬럼이 자동 추가되지 않음
- 검증 명령어: C172 5.16 combined runner 실행 및 헤더/값 범위 확인
- 검증 결과: `5.16.8__ksfo28r_runway_return_circular_landing_combined_08181131.csv` 생성 확인
- 검증하지 못한 항목: 5.17~5.27 landing 계열, `standard_vtol_demo_hover` transition/mission 계열, F450/LiftCruise 계열 전체 재실행
- 가정: 과거 CSV 보존이 우선이므로 기존 파일을 덮어쓰지 않고 필요한 scenario만 새 Run ID로 재실행해야 함
- 남은 리스크: 발표자료나 분석 스크립트가 과거 CSV를 계속 참조하면 새 컬럼을 볼 수 없음
- 다음 작업: 사용자가 분석 대상 scenario를 지정하면 새 combined runner로 재실행하고 PPT/plot 스크립트 입력 파일을 새 CSV로 교체
- 관련 기록: `TASK-20260818-1135-001`, `PROGRESS-20260818-1135-001`, `DECISION-20260818-1135-001`
- Git commit: 없음

## [2026-08-19 10:21] TODO-20260819-1021-001 — OPEN

- 과업: standard_vtol_demo_motor_updated_ko.xml JSBSim 1.2.4 호환 보정 및 PX4 별도 target 등록
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 상태: OPEN
- 내용: 첨부 XML을 그대로 PX4 SITL에 연결하지 말고, 별도 후보 모델명으로 복사해 공력 table 형식, 0속도 divide-by-zero, CG 기준 좌표, 14 kg hover throttle, PX4 airframe/bridge config를 순서대로 보정해야 한다.
- 관련 파일: /mnt/c/Users/junyeopkwon/Downloads/standard_vtol_demo_motor_updated_ko.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_hover_px4/, /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3020_jsbsim_standard_vtol_demo_hover_px4
- 검증 필요 항목: xmllint, JSBSim --catalog, JSBSim --end=0.02 단독 로딩, 짧은 standalone hover run, DONT_RUN=1 HEADLESS=1 make px4_sitl jsbsim_<new_model>__RKSS, PX4 bridge actuator mapping, QGC 저고도 arm/takeoff/land ULog
- 남은 리스크: table 변환만으로는 충분하지 않으며, velocities/vt-fps 직접 분모와 PX4 hover parameter 불일치를 함께 해결해야 한다.

## [2026-08-19 10:31] TODO-20260819-1021-001 — PARTIAL

- 대상 TODO: standard_vtol_demo_motor_updated_ko.xml JSBSim 1.2.4 호환 보정 및 PX4 별도 target 등록
- 완료 내용: 공력 table 형식 보정 단계 완료. Mach별 2D table 14개를 JSBSim 1.2.4 호환 row/column table로 변환했다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 검증 결과: xmllint 통과, FGTable missing lookup axis column 및 Error loading aerodynamic function 메시지 제거 확인
- 남은 리스크: Floating point exception, CG 좌표, hover parameter, PX4 target 등록은 아직 OPEN

## [2026-08-19 10:31] TODO-20260819-1031-001 — OPEN

- 과업: standard_vtol_demo_motor_updated_ko.xml의 Floating point exception 제거
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 상태: OPEN
- 내용: table 보정 후 JSBSim은 공력 table 오류 없이 진행하지만 지상 정지 초기조건에서 Floating point exception으로 종료된다. 공력 rate 항의 1.0 / velocities/vt-fps 직접 분모 사용을 기존 정상 모델처럼 aero/ci2vel, aero/bi2vel 또는 0속도 보호식으로 바꿔야 한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 검증 필요 항목: JSBSim --catalog 정상 종료, JSBSim --end=0.02 정상 종료, 지상 정지 초기조건에서 NaN/FPE 없음
- 남은 리스크: FPE 제거 후에도 CG 기준 좌표와 PX4 hover parameter 정합성 검증이 필요하다.

## [2026-08-19 10:38] TODO-20260819-1031-001 — DONE

- 대상 TODO: standard_vtol_demo_motor_updated_ko.xml의 Floating point exception 제거
- 완료 내용: 공력 rate 항의 velocities/vt-fps 직접 분모 quotient 9개를 제거하고 aero/ci2vel 또는 aero/bi2vel로 교체했다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 검증 결과: JSBSim --catalog rc=0, 지상 정지 초기조건 --end=0.02 rc=0, --end=1.0 rc=0
- 남은 리스크: CG 기준 좌표, 14 kg hover parameter, PX4 target 등록은 아직 OPEN

## [2026-08-19 10:38] TODO-20260819-1038-001 — OPEN

- 과업: standard_vtol_demo_motor_updated_ko_px4 등록 전 geometry 및 PX4 hover parameter 정합성 검토
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 상태: OPEN
- 내용: 후보 XML은 JSBSim 단독 load/run은 통과하지만 PX4 연결 전 motor/gear/pusher 좌표 기준과 14 kg 기준 MPC_THR_HOVER, CA_ROTOR 위치/부호를 재검토해야 한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3020_jsbsim_standard_vtol_demo_hover_px4
- 검증 필요 항목: CG 기준 좌표 변환, hover throttle 재산정, actuator sign 및 rotor geometry 확인, PX4 별도 model/airframe 등록 후 DONT_RUN build 검증
- 남은 리스크: geometry/parameter가 어긋나면 PX4 attitude/position control이 반대로 작동할 수 있음

## [2026-08-19 10:52] TODO-20260819-1052-001 — OPEN

- 과업: 20kg 후보의 PX4 arm/hover/takeoff 검증
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: PX4 연결 후 실제 제어 안정성 확인
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 수행 내용: 현재는 비무장 연결 안정성까지만 확인됨
- 변경 이유: arm 이후 control allocation, 모터 추력 table, 공력 table 상호작용은 아직 검증되지 않음
- 검증 명령어: 없음
- 검증 결과: 미검증
- 검증하지 못한 항목: arm, hover, takeoff, transition
- 가정: 20kg 후보를 다음 검증 기준으로 사용
- 남은 리스크: arm 이후 자세 제어 불안정 또는 추력 부족/과다 가능성
- 다음 작업: PX4 shell 또는 scripted MAVLink로 arm 후 짧은 hover 로그 수집
- 관련 기록: PROGRESS-20260819-1052-001
- Git commit: 없음

## [2026-08-19 11:02] TODO-20260819-1102-001 — OPEN

- 과업: 목표고도 2.5m hover 추종 개선
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: arm-hover-land 이후 hover 품질 개선
- 관련 파일: /tmp/px4_motor_updated_hover/arm_hover_land_20kg_try1.log
- 수행 내용: 현재 run은 약 1.03m 최대 AGL 및 0.9-1.1m 약 6.8초 hover로 종료
- 변경 이유: PX4 기본 takeoff altitude 2.5m 로그가 있었으나 실제 JSBSim AGL은 2.5m까지 도달하지 않음
- 검증 명령어: 없음
- 검증 결과: 미검증
- 검증하지 못한 항목: 목표고도 2.5m 도달 및 유지
- 가정: 다음 단계는 20kg 후보 유지
- 남은 리스크: 추력 table, MPC_THR_HOVER, land timing, 고도 추정 offset 중 하나 이상이 목표고도 추종에 영향 가능
- 다음 작업: 더 긴 takeoff 대기 run과 ulog local_position/setpoint 비교
- 관련 기록: PROGRESS-20260819-1102-001
- Git commit: 없음

## [2026-08-19 11:33] TODO-20260819-1133-001 — OPEN

- 과업: QGC Land/Disarm 완료 로그 재검증
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 20m hover/reposition 이후 착륙까지 완결된 로그 확보
- 관련 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-19/02_20_29.ulg
- 수행 내용: 현재 로그는 takeoff/reposition/orbit는 확인됐으나 land/disarm은 없음
- 변경 이유: 종료 시점이 ARMED + landed=0 + ORBIT라서 착륙 완료 판정 불가
- 검증 명령어: 없음
- 검증 결과: 미검증
- 검증하지 못한 항목: Landing detected, Disarmed by landing
- 가정: 다음 run에서는 QGC Land 버튼 또는 commander land를 명시적으로 실행
- 남은 리스크: 종료 전 강제 shutdown/프로세스 종료 시 비행 중 로그로 남을 수 있음
- 다음 작업: Land 후 지면 접촉 및 disarm 이벤트 확인
- 관련 기록: PROGRESS-20260819-1133-001
- Git commit: 없음

## [2026-08-19 14:25] TODO-20260819-1425-001 — OPEN

- 과업: standard_vtol_demo_motor_updated_ko_px4 표준 VTOL 전환 구성 적용
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 고정익 천이 문제 해결
- 관련 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_motor_updated_ko_px4.xml
- 수행 내용: 원인 진단 결과, 현재 airframe이 순수 멀티콥터 설정이고 조종면/airspeed bridge mapping이 누락되어 있음을 확인
- 변경 이유: PX4가 기체를 Standard VTOL로 초기화하고 fixed-wing 조종면과 pusher를 JSBSim에 전달하도록 구성 필요
- 검증 명령어: 없음
- 검증 결과: 미검증
- 검증하지 못한 항목: 실제 front transition 및 fixed-wing hold
- 가정: 20kg 안정 후보를 유지한 상태에서 먼저 제어/매핑 문제를 수정
- 남은 리스크: 수정 후 공력 table, 조종면 부호, pusher 추력, FW_AIRSPD_*, VT_F_TRANS_THR 튜닝 필요 가능성
- 다음 작업: 3021 airframe 
c.vtol_defaults 전환, VT_TYPE 2, CA_AIRFRAME 2, CA_ROTOR_COUNT 5, CA_SV_CS_COUNT 3, surface PWM function 및 bridge mapping 추가
- 관련 기록: TASK-20260819-1425-001, PROGRESS-20260819-1425-001
- Git commit: 없음

## [2026-08-19 14:31] CORRECTION-20260819-1431-001 — 정정

- 대상 기록: TASK-20260819-1425-001, PROGRESS-20260819-1425-001, TODO-20260819-1425-001, INDEX-20260819-1425-001
- 정정 이유: PowerShell quoting 과정에서 backtick으로 감싼 기술 식별자 일부가 손상되어 표기 정정 필요
- 기존 내용: `rc.mc_defaults`, `rc.vtol_defaults`, `fcs/...`, `barometer`, `rascal.xml`, `vehicle_*`, `airspeed_*` 중 일부가 제어문자 또는 잘린 문자열로 기록됨
- 정정 내용: 올바른 핵심 표기는 `rc.mc_defaults`, `. ${R}etc/init.d/rc.vtol_defaults`, `fcs/esc-cmd-norm[0..4]`, `fcs/aileron-cmd-norm`, `fcs/elevator-cmd-norm`, `fcs/rudder-cmd-norm`, `barometer`, `rascal.xml`, `vehicle_status.nav_state`, `vtol_vehicle_status`, `airspeed_validated`임
- 영향 범위: 진단 결론에는 변화 없음. 손상된 표기는 본 정정 기록과 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_TRANSITION_DIAGNOSIS_20260819.md 재작성본을 기준으로 해석
- 검증 결과: 진단 문서 본문을 literal text로 재작성
- 다음 작업: 3021 airframe 및 bridge config 수정 단계에서 본 정정 표기를 기준으로 적용

## [2026-08-19 14:48] TODO-20260819-1448-001 — OPEN

- 과업: 성공 `standard_vtol_demo.xml`의 전환 성공 요소 이식
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 새 모델 fixed-wing transition 문제 해결
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_DEMO_COMPARISON_20260819.md
- 수행 내용: 성공 모델 대비 누락된 요소를 정리
- 변경 이유: 전환 실패를 공력 table 단독 문제가 아니라 PX4/bridge/aero derivative 통합 문제로 해결하기 위함
- 검증 명령어: 없음
- 검증 결과: 미검증
- 검증하지 못한 항목: 실제 front transition 및 fixed-wing hold
- 가정: 20kg 새 모델을 기준으로 먼저 제어 연결 문제를 해결
- 남은 리스크: 성공 XML의 단순 full-envelope aero를 그대로 이식하면 실제 DATCOM 기반 모델의 물리성과 충돌할 수 있음
- 다음 작업: `rc.vtol_defaults`, `VT_TYPE 2`, surface bridge mapping, `CLde`, `Cmde`, `Cndr`, high-alpha 보호 순서로 적용
- 관련 기록: TASK-20260819-1448-001, PROGRESS-20260819-1448-001
- Git commit: 없음

## [2026-08-20 10:00] TODO-20260819-1425-001 — PARTIAL

- 대상 TODO: standard_vtol_demo_motor_updated_ko_px4 표준 VTOL 전환 구성 적용
- 완료 내용: airframe을 `rc.vtol_defaults` 기반 Standard VTOL로 전환(`CA_AIRFRAME 2`, `CA_ROTOR_COUNT 5`, `CA_SV_CS_COUNT 3`), bridge에 aileron/elevator/rudder/airspeed 매핑 추가. DONT_RUN 빌드 및 30초 headless 실행 통과.
- 관련 파일: airframe `3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4`, bridge config `standard_vtol_demo_motor_updated_ko_px4.xml`
- 남은 리스크: 공력 elevator/rudder derivative(`CLde`/`Cmde`/`Cndr`)는 사용자 지시로 이번 범위에서 제외(DATCOM 러더 해석 문제를 사용자가 별도 검토 중). 제어 신호는 JSBSim까지 전달되지만 실제 요 모멘트 발생 여부는 미검증. airspeed selector preflight 경고 원인 미규명. 실제 arm-hover-transition 비행 미검증.

## [2026-08-20 10:00] TODO-20260819-1448-001 — PARTIAL

- 대상 TODO: 성공 `standard_vtol_demo.xml`의 전환 성공 요소 이식
- 완료 내용: `rc.vtol_defaults`, `VT_TYPE 2`, surface bridge mapping 3항목 적용 완료
- 미완료 내용: `CLde`, `Cmde`, `Cndr`, high-alpha 보호는 사용자 지시로 보류(공력 데이터는 현재 구조 유지, 별도 검토 중)
- 관련 기록: TASK-20260820-1000-001, PROGRESS-20260820-1000-001

## [2026-08-20 10:00] TODO-20260820-1000-001 — OPEN

- 과업: airspeed selector preflight 경고 원인 규명
- 대상 프로젝트: jsbsim_workflow
- 상태: OPEN
- 내용: `SENS_EN_ARSPDSIM 1` 및 bridge `<airspeed>` 센서를 추가했지만, 30초 headless 실행에서 `WARN [health_and_arming_checks] Preflight Fail: Airspeed selector module down`이 발생함. `rc.vtol_defaults`가 `VEHICLE_TYPE vtol`을 설정해 `rc.vehicle_setup` → `rc.vtol_apps`에서 `airspeed_selector` 모듈이 자동 시작되어야 하는 것으로 rc 스크립트 체인상 확인되나, 실제로 모듈이 기동했는지 또는 기동 후 유효 데이터 미검증 상태인지는 확인하지 못함.
- 검증 필요 항목: PX4 shell에서 `airspeed_selector status`, `listener airspeed_validated` 확인, 필요 시 정지 상태(u=0)에서의 차압 센서 유효성 판정 기준 확인
- 남은 리스크: 이 경고가 해소되지 않으면 실제 arm이 막힐 수 있음

## [2026-08-20 10:00] TODO-20260820-1002-001 — OPEN

- 과업: standard_vtol_demo_motor_updated_ko_px4 실제 MC 호버 → 전방 전환 → FW 유지 비행 검증
- 대상 프로젝트: jsbsim_workflow
- 상태: OPEN
- 내용: airframe/bridge 구조 수정은 완료됐으나 실제 비행으로 전환이 성립하는지는 아직 확인 전. PX4 shell 또는 QGC로 arm 후 hover, 전방 전환 명령(`VT_F_TRANS_THR`/DO_VTOL_TRANSITION), FW 유지 비행까지 실행하고 ULog로 판정 필요.
- 검증 필요 항목: `vtol_vehicle_status.vtol_type`/`vehicle_status.nav_state` 전환 여부, `airspeed_validated`, `actuator_outputs`의 조종면/pusher 채널 실제 변화, JSBSim CSV의 `fcs/aileron-pos-rad` 등 실제 반영 여부, 요 모멘트 발생 여부(러더 공력 효과 유무 확인)
- 남은 리스크: `FW_AIRSPD_*`/`VT_F_TRANS_THR`가 잠정값이라 전환 실속/타이밍이 부적절할 수 있음. 러더 요 모멘트가 DATCOM 데이터 한계로 약하거나 없을 수 있음(사용자가 별도 검토 중인 사안)

## [2026-08-20 11:00] TODO-20260820-1000-001 — DONE

- 대상 TODO: airspeed selector preflight 경고 원인 규명
- 완료 내용: `airspeed_selector status`=running, `differential_pressure`/`airspeed_validated` 토픽 모두 정상 발행+`measurement_valid: True` 확인. 경고는 부팅 직후(t≈12s) health_and_arming_checks가 모듈의 첫 유효 샘플 발행 이전에 한 번 평가되며 찍히는 부팅 트랜지언트로 판정. 이후 arm/takeoff는 이 경고로 막히지 않고 정상 진행됨을 확인
- 관련 기록: PROGRESS-20260820-1100-001
- 남은 리스크: 없음

## [2026-08-20 11:20] TODO-20260820-1002-001 — PARTIAL(원인 규명, 전환 미성공)

- 대상 TODO: standard_vtol_demo_motor_updated_ko_px4 실제 MC 호버 → 전방 전환 → FW 유지 비행 검증
- 완료 내용: arm/takeoff 정상 진행 확인. `commander transition` 명령이 실제로 FCS의 aileron/elevator/rudder 3채널 명령을 정확한 스케일로 변화시킴을 CSV로 확인(bridge mapping 정상 작동 최종 확인). `vtol_att_control`의 Quad-chute(자동 안전복귀) 발동 확인(PX4 안전장치 정상 동작)
- 미완료 내용: FW 유지 비행 성공은 달성하지 못함. t≈49.9s에 지면 충돌 및 시뮬레이션 NaN 발산으로 종료
- 근본 원인(신규 발견): 전환 명령 이전, PX4 기본 수직 상승(takeoff) 단계에서 이미 `aero/alpha-deg`가 ±90도 근방에서 불안정해짐(전진속도≈0인 순수 수직 상승 시 alpha=atan2(w,u) 특이점). Aero.xml에 고받음각 보호가 없어 이 상태에서 조종면이 움직이기 시작하자 자세가 발산함
- 관련 기록: PROGRESS-20260820-1120-001, TODO-20260820-1120-001(신규), DECISION-20260820-1120-001
- 남은 리스크: 아래 TODO-20260820-1120-001 참고

## [2026-08-20 11:20] TODO-20260820-1120-001 — OPEN

- 과업: DATCOM 기반 Aero.xml의 고받음각(|alpha| 큰 구간) 보호/클램핑 필요성 검토
- 대상 프로젝트: jsbsim_workflow
- 상태: OPEN(사용자 판단 대기 — 이번 세션 범위에서는 Aero.xml 수정하지 않음)
- 내용: 순수 수직 상승(전진속도≈0) 시 alpha 계산이 ±90도 부근에서 불안정해지는 것은 JSBSim 자체의 일반적 특성이지만, 이 모델의 DATCOM 테이블은 고받음각 구간에 대한 보호/클램핑이 없어 그 상태에서 qbar가 커지면(빠른 상승률) 실제 발산으로 이어짐. 이전 hover 검증들이 통과한 것은 상승률이 낮아 문제가 가려졌을 가능성이 있음
- 검증 필요 항목: Aero.xml의 CL/CD/Cm 등 table이 alpha 전 구간(-180~180도)에서 어떤 값을 반환하는지, high-alpha 시 강제로 힘을 감쇠/제한하는 로직 추가 여부
- 남은 리스크: 이 문제를 해결하지 않으면 상승률이 큰 모든 시나리오(순수 멀티콥터 hover 포함)에서 잠재적으로 동일한 발산이 재현될 수 있음
- 다음 작업: 사용자가 공력 데이터(러더 문제 포함) 재검토 시 이 발견도 함께 반영 필요. 임시 우회책으로는 상승률을 낮추거나(느린 takeoff), MIS_TAKEOFF_ALT를 낮춰 alpha 불안정 구간 노출 시간을 줄이는 방법이 있음(근본 해결은 아님)

## [2026-08-20 11:20] TODO-20260820-1121-001 — OPEN

- 과업: 러더 실제 공력 요 모멘트 발생 여부 최종 판정
- 대상 프로젝트: jsbsim_workflow
- 상태: OPEN(TODO-20260820-1120-001에 의존)
- 내용: rudder-cmd-norm이 최대 약 -0.44까지 PX4 FW 컨트롤러에 의해 실제로 생성되고 JSBSim까지 전달됨은 확인했으나(제어 경로 정상), 비행이 alpha 불안정으로 붕괴되어 실제 요 모멘트 발생 여부(Cn_dr 등 공력 계수 유효성)는 판정하지 못함
- 검증 필요 항목: TODO-20260820-1120-001 해결 후 안정적인 FW 비행 구간을 확보한 다음, 러더 스텝 입력에 대한 yaw rate 응답 확인
- 남은 리스크: 사용자가 이미 우려한 대로 DATCOM 데이터에 러더 효과가 없거나 미약할 가능성이 여전히 남아있음

## [2026-08-20 12:00] TODO-20260820-1120-001 — DONE(게이트 적용 완료, 후속 이슈는 신규 TODO로 분리)

- 대상 TODO: DATCOM 기반 Aero.xml의 고받음각(|alpha| 큰 구간) 보호/클램핑 필요성 검토
- 완료 내용: alpha 기반 연속 게이팅 함수(`aero/coefficient/alpha_validity_gate`) 추가 및 16개 계수 함수에 적용. 순수 수직상승 구간에서 발산이 억제됨을 CSV로 확인(사용자 승인 후 실제 적용까지 완료)
- 관련 기록: PROGRESS-20260820-1200-001, TASK-20260820-1200-001
- 남은 리스크: 아래 TODO-20260820-1200-001 참고(별개의 전환 발산 문제 발견)

## [2026-08-20 12:00] TODO-20260820-1200-001 — OPEN

- 과업: alpha 게이트 적용 후에도 남은 전환 발산 문제(제어 게인/전환 절차 추정) 원인 규명 및 해결
- 대상 프로젝트: jsbsim_workflow
- 상태: OPEN
- 내용: alpha 게이트로 순수 수직상승 구간의 발산은 해결됐으나, `commander transition` 명령이 실제 반영되는 시점(t≈35.8s)부터 elevator/aileron 명령이 다시 발산성으로 커지며 t≈41.8s 지면충돌+NaN. 콘솔 로그의 "Attitude failure (pitch)"/Quad-chute 발생 양상은 이전과 유사하나, CSV 상 발산 메커니즘은 다름(이번엔 순수 alpha 문제가 아니라 조종면이 실제로 움직이며 발산)
- 가설(미검증): 이 모델은 정지 호버 상태에서 바로 transition을 명령하는 비정상적 절차로 테스트됐음(실제로는 pusher로 먼저 가속 후 전환하는 게 정석). alpha 게이트가 닫혀있는(저속) 동안 FW rate/attitude 컨트롤러가 무반응한 플랜트에 대해 조종면 명령을 계속 키우다가(적분 와인드업 등), 게이트가 다시 열리는 시점에 그 과도한 명령이 그대로 반영되며 발산했을 가능성
- 검증 필요 항목: (1) pusher로 사전 가속 후 transition을 명령하는 정상 절차로 재시도, (2) FW_RR_P/FW_PR_P 등 자세 게인이 잠정값(untuned)인 점 재확인 및 조정, (3) alpha_validity_gate의 램프 폭(-90~-24, 11~90도)을 더 완만하게 만들어 게이트 재개방 충격 완화 실험
- 남은 리스크: 이 문제가 해결되지 않으면 alpha 게이트만으로는 완전한 전환 비행 성공을 달성할 수 없음. 원인이 공력 데이터가 아니라 제어/절차 영역일 가능성이 있어 사용자 판단이 추가로 필요함

## [2026-08-20 12:30] TODO-20260820-1200-001 — 원인 재규명(가설 기각, 진짜 원인은 AERORP)

- 대상 TODO: alpha 게이트 적용 후에도 남은 전환 발산 문제
- 갱신 내용: 위에서 세운 "제어 게인 와인드업" 가설은 틀린 것으로 판명됨. 진짜 원인은 Metrics.xml의 `AERORP`가 CG 이동(원점→0.649) 후에도 옛 값(0,0,0)에 방치되어 JSBSim이 매 스텝 0.649m 모멘트암을 곱한 허위 피칭모멘트를 추가하고 있었던 것. AERORP/VRP를 0.649로 수정 후 동일 시퀀스 재검증 결과 NaN/크래시 완전히 사라지고 정상 착지까지 확인됨
- 관련 기록: PROGRESS-20260820-1230-001, TASK-20260820-1230-001, DECISION-20260820-1230-001
- 남은 리스크: 없음(이 TODO가 다루던 발산 문제 자체는 해결). 단, quad-chute로 인한 MC 강제복귀 문제는 별도 TODO-20260820-1230-001로 분리

## [2026-08-20 12:30] TODO-20260820-1230-001 — OPEN

- 과업: `commander transition` 시 `vtol_att_control: Quad-chute triggered`로 MC 모드 강제복귀되는 원인 규명(진짜 FW 전환 성공까지 도달)
- 대상 프로젝트: jsbsim_workflow
- 상태: OPEN
- 내용: AERORP 수정으로 발산/크래시는 완전히 사라졌으나, 전환 자체는 여전히 quad-chute(PX4의 전환 실패 자동 감지 안전장치)로 중단되고 MC로 복귀함. 이후 착지까지는 안정적으로 진행됨(NaN 없음, "Landing detected" 확인)
- 검증 필요 항목: quad-chute 발동 조건(관련 파라미터, 예: 전환 중 고도/자세/시간 임계값 초과 판정 로직) 확인, 정지 호버 상태에서 바로 transition 명령을 넣는 현재 테스트 절차가 정상적인지(실제로는 pusher로 먼저 전진가속 후 전환하는 것이 정석일 수 있음) 점검, FW_AIRSPD_MIN/TRIM/MAX 및 VT_F_TRANS_THR가 여전히 잠정값인 점 재검토
- 남은 리스크: 좌표 문제는 해결됐으므로 이제 순수하게 전환 로직/속도 프로파일/제어 게인 튜닝 영역으로 좁혀짐. 러더 실제 요 모멘트 판정(TODO-20260820-1121-001)도 이 항목 해결 후에나 가능

## [2026-08-20 13:00] TODO-20260820-1230-001 — 진행 상황 업데이트(원인 후보 좁혀짐)

- 대상 TODO: quad-chute로 MC 강제복귀되는 원인 규명
- 갱신 내용: 정지 호버에서 바로 transition을 명령한 것이 문제였다는 사용자 지적에 따라 DO_REPOSITION으로 실제 전방 목적지를 준 정상 절차로 재검증함(PROGRESS-20260820-1300-001). 결과: 실제로 groundspeed 24m/s까지 가속하고 vtol_state=4(FW)까지 도달함 — 전환 시도 자체는 정상 작동. 그 직후 theta가 -39~+41도까지 진동하는 큰 자세 이탈이 발생해 quad-chute가 발동한 것으로 확인됨(NaN은 없음, bounded된 진동)
- 관련 기록: PROGRESS-20260820-1300-001, scripts/vtol_transition_mavlink_test.py(신규 테스트 도구)
- 남은 리스크: 원인이 좌표/게이트/제어경로가 아니라 FW 비행 트림/안정성(Aero.xml의 Cm0, Cmalpha 등)으로 좁혀짐. 사용자가 QGC로 직접 재현 예정

## [2026-08-20 13:00] TODO-20260820-1300-001 — OPEN

- 과업: FW 상태 도달 직후 발생하는 큰 자세 이탈(theta -39~+41도)의 정확한 원인 규명 및 트림 보정
- 대상 프로젝트: jsbsim_workflow
- 상태: OPEN
- 내용: 20m/s대 실비행 속도에서 자세가 크게 진동하는 것은 좌표/제어경로 문제가 아니라 이 속도 영역에서의 공력 트림(Cm0, Cmalpha, 승강타 효과 등)이 맞지 않을 가능성이 높음. 사용자가 이미 별도로 검토 중인 DATCOM 데이터 한계와 같은 카테고리
- 검증 필요 항목: 해당 비행 속도 대역에서 Cm_base 테이블 값과 실제 트림 받음각의 정합성, VT_QC_* 계열 quad-chute 트리거 파라미터 확인
- 남은 리스크: 사용자의 QGC 재현 결과에 따라 우선순위/접근 방식이 달라질 수 있음

## [2026-08-20 13:30] TODO-20260820-1300-001 — 원인 후보 확정(승강타/러더 공력 계수 부재)

- 대상 TODO: FW 상태 도달 직후 자세 이탈 원인 규명
- 갱신 내용: A/B 비교 문서 작성 과정에서 Aero.xml 전수 grep 결과, `fcs/elevator-pos-rad`/`fcs/rudder-pos-rad`를 참조하는 함수가 전무함을 확인(PROGRESS-20260820-1330-001). 승강타/러더는 기계적으로 움직이지만 공력 피치/요 모멘트를 전혀 만들지 않음 — 자세 이탈의 유력한 근본 원인으로 확정
- 관련 기록: PROGRESS-20260820-1330-001, docs/STANDARD_VTOL_MOTOR_UPDATED_KO_VS_DEMO_CHANGELOG_20260820.md
- 다음 작업: Cmde/Cndr 계수 추가(A의 선형 계수 방식 우선 적용 또는 DATCOM 재계산) — 사용자 판단 대기

## [2026-08-20 13:30] TODO-20260820-1330-001 — OPEN(원인 확인됨, 사용자 W&B 작업 대기)

- 과업: Mass.xml 관성모멘트(ixx/iyy/izz)가 CAD 재계산 없이 A(레퍼런스)에서 그대로 상속된 것인지 확인
- 대상 프로젝트: jsbsim_workflow
- 상태: OPEN(외부 대기 — 이번 세션에서 규명할 사안 아니었음)
- 내용: B의 ixx=10.7/iyy=8.0/izz=18.5가 A와 완전히 동일함을 발견했으나, **사용자가 2026-08-20에 직접 확인**: Weight & Balance 확인 작업이 진행 중이며 현재 CG x좌표(0.649m)만 확정값이고 관성모멘트를 포함한 나머지는 전부 임의값(placeholder)임. 버그가 아니라 W&B 확정 전 정상적인 중간 상태
- 검증 필요 항목: 없음(원인 확인 완료). W&B 확정되면 Mass.xml 갱신만 남음
- 남은 리스크: W&B 확정 전까지는 이 모델의 피치/롤/요 각가속도 응답(quad-chute 발동 시점의 자세 발산 등)을 정량적으로 신뢰하지 말 것 — 정성적 검증(발산/NaN 여부)까지만 유효
- 관련 기록: docs/STANDARD_VTOL_MOTOR_UPDATED_KO_VS_DEMO_CHANGELOG_20260820.md(2절 갱신)

## [2026-08-20 13:45] TODO-20260820-1300-001 — 원인 확인됨(V-tail 러더베이터, 사용자 별도 검토 중)

- 대상 TODO: 승강타/러더 공력 모멘트 계수 부재
- 갱신 내용: **사용자가 2026-08-20에 직접 확인**: 이 기체는 V-tail(러더베이터) 기체이며, AVL/DATCOM 계열 프로그램이 V-tail 러더베이터 혼합 효과를 직접 산출하지 못하는 한계 때문에 사용자가 별도로 대응 방안을 검토 중임. 미발견 버그가 아니라 이미 인지하고 있는 사안
- 관련 기록: docs/STANDARD_VTOL_MOTOR_UPDATED_KO_VS_DEMO_CHANGELOG_20260820.md(5.3절 갱신)
- 다음 작업: 사용자가 V-tail 공력 처리 방안을 결정하면 그에 맞춰 Aero.xml 갱신(이번 세션에서는 적용하지 않음, 대기)

## [2026-08-20 14:30] TODO-20260820-1430-001 — OPEN

- 과업: A(레퍼런스 계수 임시 차용)+B(VT_F_TRANS_THR 상향) 적용에도 quad-chute(고도손실 20m 초과)가 해결되지 않는 문제
- 대상 프로젝트: jsbsim_workflow
- 상태: OPEN
- 내용: PROGRESS-20260820-1430-001에서 정확한 quad-chute 트리거(`VT_QC_T_ALT_LOSS`, 자세각 아님)를 규명하고 A/B를 적용해 재검증했으나, 여전히 동일 메커니즘으로 실패함. 레퍼런스(A) 기체는 wingarea 0.953㎡/23.6kg, 우리 기체는 0.572㎡/20.0kg로 날개하중이 더 큰데 A의 계수 크기를 그대로 썼기 때문일 가능성이 높음
- 검증 필요 항목: CLde/Cmde/Cndr을 날개하중 또는 익현 비율로 스케일링한 재시도, FW_AIRSPD_MIN(현재 10m/s, 자연 트림 균형속도 24.8m/s보다 훨씬 낮음)을 올려 PX4가 전환 완료를 너무 이르게 판정하지 않도록 조정하는 방안
- 남은 리스크: 근본적으로는 TODO-20260820-1300-001(V-tail 정식 공력데이터)이 해결돼야 완전히 풀릴 문제일 가능성. 스케일링 등 임시 조치는 진단/완화 목적으로만 유효
- 관련 기록: PROGRESS-20260820-1430-001
