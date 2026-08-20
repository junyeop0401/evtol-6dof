## [2026-06-15 17:51] INDEX-20260615-1751-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-15 17:51 KST`
- 최근 수행 과업:
  - JSBSim `c172x` 단독 450 m, 60 m/s, pitch 2.5 deg no-trim/no-autopilot 추락 케이스 추가 및 실행
- 현재 상태:
  - 실행 가능한 초기조건 XML, runscript XML, wrapper script가 추가됨
  - 최종 실행 `4.0.4__450m_60ms_pitch25_no_trim_drop` 성공
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.0__450m_60ms_pitch25_no_trim_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.0__450m_60ms_pitch25_no_trim_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.0.4__450m_60ms_pitch25_no_trim_drop_impact_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.0.4__450m_60ms_pitch25_no_trim_drop_impact_summary.json`
- 주요 결정:
  - 캡쳐본 좌표계는 현재 `x=North`, `y=East`, `z=ground altitude`로 해석
  - 지면 도달은 `gear/unit[0]/WOW eq 1` 첫 지면 접촉 기준
- 미완료 TODO:
  - `TODO-20260615-1751-001`: 사용자가 의도한 x축이 North인지 East인지 확인
- 남은 리스크:
  - `c172x`는 고정익 항공기이므로 UAM 캡쳐본과 동역학 결과가 다름
  - `WOW` 기준 접촉이라 접촉 시 CG 고도는 0 m가 아니라 약 `1.595 m`
- 권장 다음 작업:
  - 좌표축 의도 확인
  - 필요 시 `psi=90 deg` 또는 CG 지면 도달 보간 기준의 비교 케이스 추가

## [2026-06-15 18:00] INDEX-20260615-1800-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-15 18:00 KST`
- 최근 수행 과업:
  - `4.0` 직접 투하 해석을 정정하고, `4.1` 450 m / 60 m/s x 방향 cruise 후 engine-out 케이스 추가
- 현재 상태:
  - wrapper `run_c172x_450m_drop_no_trim.py`의 기본 실행 대상은 `4.1__450m_60ms_x_cruise30_engineout_headinghold`
  - 최종 실행 `4.1.1__450m_60ms_x_cruise30_engineout_headinghold` 성공
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.1__450m_60ms_x_cruise_untrimmed_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.1__450m_60ms_x_cruise30_engineout_headinghold_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_impact_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_impact_summary.json`
- 주요 결정:
  - `4.0` 직접 초기상태 추락 해석은 사용자 의도와 달라 `4.1`로 교체
  - `4.1`은 참조 `2.2`처럼 powered cruise trim/hold 후 engine-out
- 미완료 TODO:
  - `TODO-20260615-1751-001`: x축 방향 해석 확인
  - `TODO-20260615-1800-001`: engine-out 이후 heading hold 유지 여부 확인
- 남은 리스크:
  - `4.1`은 heading hold가 켜져 있어 완전 무조종 추락은 아님
  - x 방향이 local East라면 heading `90 deg` 케이스가 별도로 필요
- 권장 다음 작업:
  - 사용자가 원하는 최종 조건에 따라 `4.2` heading hold off 또는 heading 90 deg 변형 추가

## [2026-06-15 18:05] INDEX-20260615-1805-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-15 18:05 KST`
- 최근 수행 과업:
  - `4.1.1` cruise 후 engine-out 결과에서 엔진 정지 시점 `t=0` 별도 로그/그래프 생성
- 현재 상태:
  - engine-out 기준 CSV/JSON/trajectory plot/states plot 생성 완료
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/extract_c172x_engineout_t0.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_si.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_summary.json`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_trajectory_3d.png`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_states_vs_time.png`
- 주요 결정:
  - 추락 시작 시점은 `engineout_start_time_s = 31.0`으로 정의
  - 원본 로그는 유지하고 `results/c172x/engineout_t0/` 아래 별도 산출물로 분리
- 미완료 TODO:
  - 보고서용 2D plot 스타일이 필요하면 추가 생성
- 남은 리스크:
  - 3D plot은 y/east 변위가 작아 축 비율상 직선에 가깝게 보임
- 권장 다음 작업:
  - 보고서 삽입용이면 `time-altitude`, `time-speed`, `x-altitude` 단일 그래프를 추가 생성

## [2026-06-15 18:13] INDEX-20260615-1813-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-15 18:13 KST`
- 최근 수행 과업:
  - 추락 시작점 `t=0`, 좌표 `(0,0,450 m)`, 속도 `(60,0,0) m/s`, 무자전 원형지구 `c172x` 직접 실행 케이스 추가
- 현재 상태:
  - `4.2.2__450m_60ms_x_engineout_t0_spherical` 실행 성공
  - AP/trim off 기준 결과 산출 완료
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.2__450m_60ms_x_engineout_t0_spherical_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.2__450m_60ms_x_engineout_t0_spherical_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_spherical.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.2.2__450m_60ms_x_engineout_t0_spherical_engineout_t0_spherical_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.2.2__450m_60ms_x_engineout_t0_spherical_engineout_t0_spherical_summary.json`
- 주요 결정:
  - `4.2.2`는 AP/trim off 기준으로 확정
  - 지구 모델은 `04_nonrotating_spherical_earth.xml`
- 미완료 TODO:
  - `TODO-20260615-1813-001`: AP/trim off와 heading hold/trim glide 비교 필요 여부 확인
- 남은 리스크:
  - AP/trim off 조건에서 c172x는 실속/회전으로 인해 직진 활공형 그래프가 나오지 않음
- 권장 다음 작업:
  - 보고서용이면 `4.2.2` 결과로 2D 그래프 세트를 추가 생성하거나, 비교용 trimmed glide 케이스를 별도 생성

## [2026-06-15 18:20] INDEX-20260615-1820-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-15 18:20 KST`
- 최근 수행 과업:
  - 기존 ballistic 결과와 유사한 방향 고정 활공 추락 비교용 `4.3` heading hold/trim glide 케이스 추가
- 현재 상태:
  - `4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical` 실행 성공
  - `4.2` AP/trim off 결과와 `4.3` heading hold/trim glide 결과가 모두 존재
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.3__450m_60ms_x_engineout_t0_headinghold_trim_spherical_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_headinghold_trim_spherical.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical_headinghold_trim_spherical_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical_headinghold_trim_spherical_summary.json`
- 주요 결정:
  - ballistic-like 형태 비교용으로 `4.3` heading hold + pitch trim `0.18` 적용
- 미완료 TODO:
  - `TODO-20260615-1820-001`: 기존 ballistic 원본 CSV와 비교표/overlay plot 생성
- 남은 리스크:
  - `c172x` 양력 때문에 기존 ballistic 이미지보다 활공거리와 시간이 훨씬 큼
- 권장 다음 작업:
  - 기존 ballistic 원본 CSV가 있으면 `4.2`/`4.3`/ballistic 3종 비교 그래프 생성

## [2026-06-15 18:24] INDEX-20260615-1824-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-15 18:24 KST`
- 최근 수행 과업:
  - 기존 결과에 사용된 Cessna 172 공력 Excel/XML 파일 확인
- 현재 상태:
  - 기존 결과는 단순 ballistic 질점이 아니라 C172 기본 공력 테이블 기반 6DOF 모델일 가능성이 큼
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 주요 결정:
  - 아직 신규 JSBSim aircraft 생성 전, 기존 6DOF 코드의 공력 부호/축 규약 확인 필요
- 미완료 TODO:
  - 기존 6DOF 코드에서 `CD`, `CL`, `Cm` 적용 식 확인
- 남은 리스크:
  - Excel `CD` 열에 음수 값이 있어 JSBSim drag axis에 그대로 넣으면 물리적으로 잘못될 수 있음
- 권장 다음 작업:
  - `cessna172_config.xml`와 Excel 계수를 기반으로 `c172_basic_6dof` JSBSim aircraft를 별도로 만들고 `4.4` 비교 케이스 실행
## [2026-06-16 11:56] INDEX-20260616-1156-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 11:56 KST`
- 최근 수행 과업:
  - `c172x` ground reaction damping/spring/friction 27개 계수 변형 생성 및 기본 계수 이륙 확인 스크립트 추가
- 현재 상태:
  - `aircraft_variants/c172x_groundreaction/` 아래 27개 `c172x.xml` 생성 완료
  - 기본 계수 변형 `c172x_gr_damp100_spring100_fric100`의 `5.0__takeoff_groundreaction_check` 실행 성공
  - raw CSV, SI CSV, console log, states plot, trajectory plot 생성 완료
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_groundreaction_variants.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_groundreaction_takeoff.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.0__takeoff_groundreaction_check_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_groundreaction/manifest.csv`
- 주요 결정:
  - 변형 원본은 workflow 내부에 `c172x.xml` 파일명으로 보관하고, 실행 시 JSBSim aircraft 폴더로 복사/rename
  - right main gear의 equivalent `strut_force` spring/damping 항도 계수 배율 대상에 포함
- 미완료 TODO:
  - `TODO-20260616-1156-001`: 27개 전체 실행 및 summary 병합 자동화 필요 여부 확인
- 남은 리스크:
  - 기본 계수 변형만 실행 검증했고 나머지 26개 변형은 아직 실행하지 않음
  - `0` 배율 조합은 비물리적 지면 반력 조건으로 수치 불안정 가능성 있음
- 권장 다음 작업:
  - 비교를 자동화하려면 `manifest.csv`를 순회해 `run_c172x_groundreaction_takeoff.py --variant ...`를 실행하고 summary CSV를 병합
## [2026-06-16 12:08] INDEX-20260616-1208-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 12:08 KST`
- 최근 수행 과업:
  - FlightGear C172 매뉴얼 기반 `5.1` takeoff 상태기계 runscript 추가 및 기본 계수 variant 검증
- 현재 상태:
  - `5.1__takeoff_flightgear_state_machine_run.xml` 추가 완료
  - 기본 실행 `python3 scripts/run_c172x_groundreaction_takeoff.py`는 `--procedure flightgear`를 사용
  - 기본 계수 variant `c172x_gr_damp100_spring100_fric100`에서 500 ft AGL 도달 성공
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.1__takeoff_flightgear_state_machine_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_groundreaction_takeoff.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 주요 결정:
  - FlightGear 수동 절차의 40 kt/55 kt/70 kt/500 ft 상태 기준을 사용
  - C172X 안정 상승을 위해 50 ft 이후 AP attitude hold, 250 ft 이후 heading/altitude hold를 적용
- 미완료 TODO:
  - `TODO-20260616-1208-001`: 70 kt initial climb 속도 유지 성능 개선
  - `TODO-20260616-1156-001`: 27개 전체 실행 및 summary 병합 자동화 필요 여부 확인
- 남은 리스크:
  - `5.1`은 완전 수동 이륙이 아니라 AP 안정화가 포함된 하이브리드 절차
  - 27개 전체 variant에서 `5.1` 성공 여부는 아직 검증하지 않음
- 권장 다음 작업:
  - 비교 자동화가 필요하면 `manifest.csv` 전체 variant를 순회 실행하고 `climb_500ft_confirmed`, `liftoff_10ft_time_s`, final speed를 병합
## [2026-06-16 12:16] INDEX-20260616-1216-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 12:16 KST`
- 최근 수행 과업:
  - 원본 `c172x` aircraft 직접 기반 단순 이륙 runscript 추가
- 현재 상태:
  - `5.2__takeoff_simple_c172x_run.xml` 추가 완료
  - `run_jsbsim_timestamped.py --aircraft c172x`로 실행 성공
  - raw CSV, SI CSV, console log, states plot, trajectory plot 생성 완료
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.2__takeoff_simple_c172x_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 주요 결정:
  - ground reaction variant와 별개로 원본 `c172x`를 직접 쓰는 단순 runscript를 추가
  - 사용자가 후속 튜닝을 직접 수행할 수 있도록 AP 안정화 없이 기본 throttle/rotate/climb 이벤트만 구성
- 미완료 TODO:
  - 오른쪽 wing tip 접촉 없이 매끄러운 수동 상승이 되도록 aileron/rudder/elevator 튜닝
- 남은 리스크:
  - 순수 고정 입력만으로는 C172X의 roll/yaw/propeller 효과 때문에 자세가 흐트러질 수 있음
- 권장 다음 작업:
  - `5.2.1` states plot에서 roll/pitch/yaw와 조종면 입력을 보고 수동 제어값 조정
## [2026-06-16 12:25] INDEX-20260616-1225-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 12:25 KST`
- 최근 수행 과업:
  - 원본 `c172x` aircraft로 엔진 켜고 활주 후 500 ft까지 상승하는 runscript 추가
- 현재 상태:
  - `5.3__takeoff_to_500ft_c172x_run.xml` 실행 성공
  - `Aircraft: c172x`
  - 500 ft AGL 도달 및 종료 확인
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.3__takeoff_to_500ft_c172x_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 주요 결정:
  - 사용자가 요청한 기준 스크립트는 variant가 아닌 원본 `c172x` 직접 실행으로 분리
  - 500 ft 안정 상승을 위해 250 ft 이후 heading/altitude hold 사용
- 미완료 TODO:
  - 70 kt 유지가 필요하면 closed-loop elevator 제어 추가
- 남은 리스크:
  - 현재 최종 속도는 약 `56.86 kt`로 70 kt target보다 낮음
- 권장 다음 작업:
  - 비교 기준으로는 `5.3`을 사용하고, 속도 기준이 중요하면 별도 airspeed hold/feedback 제어 추가
## [2026-06-16 12:34] INDEX-20260616-1234-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 12:34 KST`
- 최근 수행 과업:
  - `5.3` 원본 `c172x` 500 ft 이륙 스크립트의 30초 부근 고도 꺾임 원인 수정
- 현재 상태:
  - `5.3__takeoff_to_500ft_c172x_run.xml`에서 20 ft 이후 `ap/attitude_hold` 제거
  - `5.3.6__takeoff_to_500ft_c172x` 실행 성공
  - 원본 `c172x`로 500 ft AGL 도달 확인
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.3__takeoff_to_500ft_c172x_run.xml`
- 주요 결정:
  - 30초 부근 고도 개입 원인인 조기 attitude hold 제거
  - 100 ft 이후 heading hold, 250 ft 이후 altitude hold로 안정화 분리
- 미완료 TODO:
  - 70 kt target 유지가 필요하면 closed-loop airspeed/elevator 제어 추가
- 남은 리스크:
  - 완전 수동 조종만으로 500 ft까지 가는 스크립트는 아직 아님
  - 100 ft 이후 heading hold, 250 ft 이후 altitude hold 개입은 남아 있음
- 권장 다음 작업:
  - `5.3.6` plot으로 30초 부근 altitude 꺾임 개선 여부 확인
## [2026-06-16 18:23] INDEX-20260616-1823-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 18:23 KST`
- 최근 수행 과업:
  - C172X 엔진 없는 상태 추락 runscript 작성
- 현재 상태:
  - `4.4__450m_60ms_x_noengine_drop_init.xml` 추가 완료
  - `4.4__450m_60ms_x_noengine_drop_run.xml` 추가 완료
  - `run_c172x_noengine_drop.py` 실행 성공
  - `4.4.2__450m_60ms_x_noengine_drop` 결과 생성 완료
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.4__450m_60ms_x_noengine_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.4__450m_60ms_x_noengine_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 주요 결정:
  - 기존 `c172x.xml` aircraft를 유지하고 runscript/초기조건 수준에서 engine off를 강제
  - 물리적 propulsion 제거 variant는 후속 TODO로 분리
- 미완료 TODO:
  - `TODO-20260616-1823-001`: 실제 엔진/프로펠러 모델 제거가 필요하면 `c172x_noengine` aircraft variant 생성
  - 기존 `TODO-20260616-1208-001`: 70 kt initial climb 속도 유지 성능 개선
  - 기존 `TODO-20260616-1156-001`: 27개 ground reaction 변형 전체 실행 및 summary 병합 자동화 필요 여부 확인
- 남은 리스크:
  - 현재 `4.4`는 engine off 명령을 적용하지만 기존 propulsion/propeller 모델이 남아 있어 windmilling 관련 로그가 완전 0이 아닐 수 있음
- 권장 다음 작업:
  - 사용자가 실제 "엔진 제거" 모델을 원하면 별도 `c172x_noengine` aircraft variant 생성 후 같은 runscript로 재실행
## [2026-06-16 18:32] INDEX-20260616-1832-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 18:32 KST`
- 최근 수행 과업:
  - C172X 엔진 추력/프로펠러 제거 aircraft variant 및 추락 실행 파일 생성
- 현재 상태:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml` 생성 완료
  - `c172x_noengine`에 `<engine>`과 `<thruster>`가 없고 fuel tank 2개는 유지됨
  - `run_c172x_noengine_noprop_drop.py` 실행 성공
  - engine/thrust/propeller 출력 전 구간 0 확인
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/initial_condition/1.0__450m_60ms_x_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/runscript/1.0__450m_60ms_x_noengine_noprop_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_noprop_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/README.md`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml`
- 주요 결정:
  - `<propulsion>` 전체가 아니라 `<engine>`만 제거해 fuel tank 질량은 유지
  - engine/propeller 질량 보정은 별도 후속 TODO로 분리
- 미완료 TODO:
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
  - 기존 `TODO-20260616-1208-001`: 70 kt initial climb 속도 유지 성능 개선
  - 기존 `TODO-20260616-1156-001`: 27개 ground reaction 변형 전체 실행 및 summary 병합 자동화 필요 여부 확인
- 남은 리스크:
  - 현재 variant는 추력/프로펠러 공력은 제거하지만 원본 `mass_balance`는 유지
- 권장 다음 작업:
  - 질량 제거까지 필요한 연구 조건이면 엔진/프로펠러 질량과 위치를 정해 `mass_balance` 보정
## [2026-06-16 18:39] INDEX-20260616-1839-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 18:39 KST`
- 최근 수행 과업:
  - C172X 추락 케이스 수평/수직속도 및 조종면 상태 비교 plot 생성
- 현재 상태:
  - `plot_c172x_drop_velocity_compare.py` 추가 완료
  - horizontal/vertical speed 비교 plot 생성 완료
  - control surface check plot 생성 완료
  - summary CSV 생성 완료
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/plot_c172x_drop_velocity_compare.py`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_velocity_compare/0616_drop_horizontal_vertical_speed_compare.png`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_velocity_compare/0616_drop_control_surface_check.png`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_velocity_compare/0616_drop_horizontal_vertical_speed_compare_summary.csv`
- 주요 결정:
  - 수직속도는 JSBSim NED 기준 `v_d_mps`를 사람이 보기 쉽게 `vertical speed up + = -v_d_mps`로 변환
  - 조종면 확인 plot은 command와 actual elevator를 분리 표시
- 미완료 TODO:
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
  - 기존 `TODO-20260616-1208-001`: 70 kt initial climb 속도 유지 성능 개선
  - 기존 `TODO-20260616-1156-001`: 27개 ground reaction 변형 전체 실행 및 summary 병합 자동화 필요 여부 확인
- 남은 리스크:
  - 현재 상태는 command neutral이지 trim equilibrium은 아님
  - actual elevator에는 aircraft XML actuator bias 영향이 남음
- 권장 다음 작업:
  - 초반 상승을 제거하려면 초기 수직 하강속도 또는 nose-down pitch를 주는 별도 init 작성
## [2026-06-16 20:42] INDEX-20260616-2042-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 20:42 KST`
- 최근 수행 과업:
  - 실제 조종면 neutral 상태 확인
- 현재 상태:
  - command 입력은 neutral이지만 actual elevator는 완전 0이 아님
  - actual elevator는 `0.11459155902616465 deg`
  - actual aileron/rudder는 `0.0 deg`
- 최근 변경 파일:
  - 없음
- 주요 결정:
  - 조종면 상태 판단은 command가 아니라 SI CSV actual deflection과 aircraft XML actuator 정의 기준으로 수행
- 미완료 TODO:
  - 필요 시 elevator actuator bias 제거 variant 생성
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
- 남은 리스크:
  - elevator actual offset이 초반 pitch-up/상승에 일부 기여할 수 있음
- 권장 다음 작업:
  - 완전한 actual neutral 상태 검증이 필요하면 `c172x_noengine_nobias` variant에서 elevator `<bias>`를 제거하고 동일 케이스 재실행
## [2026-06-16 20:54] INDEX-20260616-2054-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 20:54 KST`
- 최근 수행 과업:
  - pointmass 중량 0 기반 기본 기체 공력 확인용 C172X 추락 케이스 생성 및 실행
- 현재 상태:
  - `c172x_noengine_surface_neutral_empty` aircraft variant 생성 완료
  - engine/propeller 제거, elevator bias 0, 모든 pointmass weight 0 확인
  - 실제 조종면 elevator/aileron/rudder 모두 `0.0 deg`
  - roll/yaw가 수치오차 수준으로 안정화됨
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_surface_neutral_empty_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/initial_condition/1.0__450m_60ms_x_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/runscript/1.0__450m_60ms_x_empty_surface_neutral_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_drop.py`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty/c172x_noengine_surface_neutral_empty.xml`
- 주요 결정:
  - 기본 기체 공력 확인을 위해 `emptywt`와 기본 inertia는 유지하고 모든 pointmass weight만 0으로 설정
- 미완료 TODO:
  - `TODO-20260616-2054-001`: 지면 접촉까지 end time 연장 실행
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
- 남은 리스크:
  - 현재 실행은 180초 종료이며 지면 접촉 전
  - summary의 `ground_reach_time_s` 필드명은 이번 케이스에서 부정확함
- 권장 다음 작업:
  - 지면 접촉 결과까지 필요하면 `end=240` 이상으로 늘려 재실행
## [2026-06-16 21:31] INDEX-20260616-2131-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-16 21:31 KST`
- 최근 수행 과업:
  - pitch -20 deg, `ubody=60 m/s` empty-airframe no-engine/no-propeller 추락 케이스 생성 및 실행
- 현재 상태:
  - `1.1__450m_pitchm20_ubody60_drop_init.xml` 추가 완료
  - `1.1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop` 실행 성공
  - 실제 조종면은 전 구간 0 deg 유지
  - roll/yaw는 수치오차 수준으로 안정
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/initial_condition/1.1__450m_pitchm20_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/runscript/1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_pitchm20_ubody60_drop.py`
- 주요 결정:
  - 기존 baseline은 보존하고 pitch-down/ubody60 케이스를 `1.1`로 분리
- 미완료 TODO:
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
- 남은 리스크:
  - 지면 접촉 종료 시 CG 고도는 약 `1.53 m`
- 권장 다음 작업:
  - heading 방향 변경이 목적이면 다음 케이스에서 `psi` 값을 변경하고 동일 wrapper 패턴으로 실행
## [2026-06-17 10:44] INDEX-20260617-1044-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-17 10:44 KST`
- 최근 수행 과업:
  - C172X pitch-up 원인으로 `Cm0` 영향 여부 확인
- 현재 상태:
  - 현재 `c172x_noengine_surface_neutral_empty` 모델은 `Cmo=0.1`, `Cmalpha=-1.8`
  - 받음각 0도, elevator 0도에서도 nose-up pitch moment가 남는 구조
  - `theta=-20`, `ubody=60` 케이스의 초기 pitch-up 응답과 일치
- 최근 변경 파일:
  - 없음
- 주요 결정:
  - pitch가 -20도에서 위로 올라가는 현상은 `Cm0 != 0` 설명과 부합한다고 판단
- 미완료 TODO:
  - 필요 시 `Cmo=0` 비교 variant 생성
  - 필요 시 alpha trim 약 `3.18 deg` 초기조건 비교 실행
- 남은 리스크:
  - pitch-up 동역학은 `Cm0` 단독이 아니라 전체 longitudinal dynamics의 결과
- 권장 다음 작업:
  - 원인 분리 목적이면 `Cmo=0` variant와 기존 variant를 같은 초기조건으로 비교
## [2026-06-17 10:49] INDEX-20260617-1049-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-17 10:49 KST`
- 최근 수행 과업:
  - `Cmo=0` C172X 비교 모델 생성 및 동일 조건 시뮬레이션
- 현재 상태:
  - `c172x_noengine_surface_neutral_empty_cm0` aircraft variant 생성 완료
  - `theta=-20 deg`, `ubody=60 m/s` 동일 조건 실행 완료
  - `Cmo=0`에서 고도 상승량 `0.0 m`, 종료 시각 `66.475 s`
  - 기존 `Cmo=0.1` 대비 pitch-up/고도상승이 크게 감소
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_surface_neutral_empty_cm0_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/1.0__450m_pitchm20_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/runscript/1.0__450m_pitchm20_ubody60_cm0zero_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchm20_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/c172x_noengine_surface_neutral_empty_cm0.xml`
- 주요 결정:
  - 기존 모델은 보존하고 `Cmo=0` 별도 aircraft variant로 비교
- 미완료 TODO:
  - 필요 시 `Cmo` sweep 비교 plot 생성
- 남은 리스크:
  - pitch response에는 `Cmo` 외 pitch damping/alpha/lift coupling도 포함됨
- 권장 다음 작업:
  - 논문/보고용이면 기존 `Cmo=0.1` vs 신규 `Cmo=0` pitch/altitude 비교 plot 생성
## [2026-06-17 11:20] INDEX-20260617-1120-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-17 11:20 KST`
- 최근 수행 과업:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체용 30도 간격 자세 격자 drop initial XML 생성
- 현재 상태:
  - `psi=0..330 deg`, `theta=-90..90 deg`, `phi=0..330 deg` 조건의 initial XML `1008`개 생성 완료
  - 모든 XML 파싱 검증 완료
  - JSBSim 실행용 runscript/batch runner는 아직 생성하지 않음
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_cm0_attitude_grid_initials.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/attitude_grid_30deg/*.xml`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 주요 결정:
  - 대량 initial XML은 기존 단일 파일 폴더에 직접 섞지 않고 `initial_condition/attitude_grid_30deg/` 하위에 분리
  - `theta`는 항공기 Euler pitch 관례에 맞춰 `-90..90 deg` 범위로 생성
- 미완료 TODO:
  - `TODO-20260617-1120-001`: initial XML 격자용 batch runscript/runner 생성 및 실행 검증
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
- 남은 리스크:
  - `theta=±90 deg`는 Euler angle 특이점 가능성이 있어 실제 실행 시 주의 필요
  - 구형지구/자전 없음 조건은 initial XML이 아니라 runscript/JSBSim 설정에서 명시 확인 필요
- 권장 다음 작업:
  - 이 격자를 실제로 돌릴 계획이면 공통 runscript template 또는 Python batch runner를 생성하고 일부 대표 자세부터 smoke test 수행
## [2026-06-17 12:58] INDEX-20260617-1258-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-17 12:58 KST`
- 최근 수행 과업:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체의 `450 m`, pitch `+2.5 deg`, `ubody=60 m/s` drop 초기조건 생성 및 실행
- 현재 상태:
  - 신규 initial XML/runscript/wrapper 생성 완료
  - Run ID `1.1.1__450m_pitchp25_ubody60_cm0zero_drop` 실행 성공
  - 지면 접촉 이벤트로 `73.83333333 s` 종료
  - 최종 고도 `1.6107039963841439 m`, 최종 속도 `50.779647191860775 m/s`
  - 조종면/추력/엔진/프로펠러 출력 전 구간 `0.0` 확인
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/1.1__450m_pitchp25_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/runscript/1.1__450m_pitchp25_ubody60_cm0zero_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_si_06171257.csv`
- 주요 결정:
  - 기존 `theta=-20 deg` 비교 케이스를 보존하고 `theta=+2.5 deg` 케이스를 `1.1`로 분리
- 미완료 TODO:
  - `TODO-20260617-1120-001`: initial XML 격자용 batch runscript/runner 생성 및 실행 검증
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
- 남은 리스크:
  - 현재 SI CSV에는 body-axis 속도 컬럼이 없어서 `ubody`는 initial XML 설정과 total/inertial velocity로 간접 확인
  - `/home/junyeopkwon/jsbsim` 저장소 기준 aircraft variant XML은 untracked 상태
- 권장 다음 작업:
  - pitch +2.5 deg와 pitch -20 deg 케이스를 같은 plot에 겹쳐 pitch/altitude/trajectory 차이를 비교
## [2026-06-17 14:15] INDEX-20260617-1415-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-17 14:15 KST`
- 최근 수행 과업:
  - JSBSim 실행 시 PX4/6DOF 검증용 상태, 입력, 힘/모멘트, 가속도, 공력, 접촉/환경 property를 별도 CSV로 저장
- 현재 상태:
  - `run_jsbsim_timestamped.py`가 기존 raw/SI CSV 외에 `logs/csv/sixdof_raw/` CSV를 추가 생성
  - generated runscript에 기존 raw output과 별도 6DOF output이 함께 삽입됨
  - pitch +2.5 deg C172X Cm0=0 케이스에서 `1.1.3__450m_pitchp25_ubody60_cm0zero_drop_sixdof_raw_06171414.csv` 생성 검증 완료
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.3__450m_pitchp25_ubody60_cm0zero_drop_sixdof_raw_06171414.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.3__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
- 주요 결정:
  - 요청 property를 그대로 모두 넣지 않고 aircraft catalog에 존재하는 property만 필터링해 6DOF output에 삽입
- 미완료 TODO:
  - `TODO-20260617-1120-001`: initial XML 격자용 batch runscript/runner 생성 및 실행 검증
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
- 남은 리스크:
  - `sixdof_raw`는 JSBSim raw 단위이므로 PX4 비교 전 SI 단위 및 frame 변환 필요
  - no-engine C172X에는 indexed propulsion property가 없어 VTOL/multicopter engine/motor 로그는 별도 기체에서 검증 필요
  - `/home/junyeopkwon/jsbsim` 저장소 기준 aircraft variant XML은 untracked 상태
- 권장 다음 작업:
  - PX4 비교용으로 `sixdof_raw`를 SI/NED/FRD 기준 CSV로 변환하는 후처리 스크립트 추가
## [2026-06-17 14:33] INDEX-20260617-1433-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-17 14:33 KST`
- 최근 수행 과업:
  - `sixdof_raw` 로그에 JSBSim `position/*` property 전체 추가
- 현재 상태:
  - `run_jsbsim_timestamped.py`의 6DOF output에 position property 30개 포함
  - pitch +2.5 deg C172X Cm0=0 케이스에서 `1.1.4__450m_pitchp25_ubody60_cm0zero_drop_sixdof_raw_06171432.csv` 생성 검증 완료
  - 신규 6DOF raw CSV는 `Time` 포함 103개 컬럼, 8861행
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.4__450m_pitchp25_ubody60_cm0zero_drop_sixdof_raw_06171432.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.4__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
- 주요 결정:
  - position 비교 기준은 아직 고르지 않고, catalog에 있는 `position/*` 전체를 raw로 저장
- 미완료 TODO:
  - `TODO-20260617-1120-001`: initial XML 격자용 batch runscript/runner 생성 및 실행 검증
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
- 남은 리스크:
  - `position/from-start-neu-u-ft`는 초기값이 0이 아니라 고도에 해당하는 값으로 보이므로 후속 비교 기준 선정 시 의미 확인 필요
  - `sixdof_raw`는 raw 단위이므로 직접 코드와 비교 전 단위 변환 필요
- 권장 다음 작업:
  - 직접 코드의 좌표 정의가 NED인지 NEU인지, z가 altitude인지 down인지 확정한 뒤 position property 선택
## [2026-06-17 14:45] INDEX-20260617-1445-001 — SNAPSHOT

- 프로젝트명:
  - `jsbsim_workflow`
- 기록 시각:
  - `2026-06-17 14:45 KST`
- 최근 수행 과업:
  - `sixdof_raw`를 보존하면서 position 중심 `sixdof_si` 미터 변환 CSV 생성
- 현재 상태:
  - JSBSim 실행 시 기존 `raw`, `si`, `sixdof_raw` 외에 `sixdof_si` CSV도 생성
  - `sixdof_si`에는 `from_start_neu_n_m`, `from_start_neu_e_m`, `from_start_neu_u_m`, `from_start_ned_d_m` 포함
  - pitch +2.5 deg C172X Cm0=0 케이스에서 `1.1.5__450m_pitchp25_ubody60_cm0zero_drop_sixdof_si_06171444.csv` 생성 검증 완료
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_si/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.5__450m_pitchp25_ubody60_cm0zero_drop_sixdof_si_06171444.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.5__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
- 주요 결정:
  - JSBSim 내부 XML property를 늘리지 않고, raw 로그 후처리로 SI meter 컬럼을 생성
- 미완료 TODO:
  - `TODO-20260617-1120-001`: initial XML 격자용 batch runscript/runner 생성 및 실행 검증
  - `TODO-20260616-1832-002`: 필요 시 엔진/프로펠러 구조 질량까지 제거한 질량 모델 보정
- 남은 리스크:
  - `from_start_neu_u_m`는 초기 고도 값을 포함하므로, 직접 코드 좌표 원점에 따라 offset 처리 필요
  - force/moment/aero 전체 SI 변환은 아직 없음
- 권장 다음 작업:
  - 직접 코드의 z 정의가 altitude인지 local displacement인지 확정한 뒤 `from_start_neu_u_m` 또는 offset 제거값으로 비교

## [2026-06-21 15:54] INDEX-20260621-1554-001 — 현재 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: C172X 이륙 3단계 회전·4단계 초기상승 진단
- 현재 상태: 3단계 회전과 실제 이륙은 재현, 4단계는 속도·고도 조건만 만족하고 자세·상승률 안정화 실패
- 최근 변경 파일: scripts/c172x/runscript/5.5__takeoff_stage3_stage4_diagnostic_run.xml, scripts/generate_c172x_empty_cg_aligned_variant.py, scripts/c172x/initial_condition/2.1__takeoff_nonrotating_spherical_init.xml, scripts/run_jsbsim_timestamped.py
- 주요 결정: 동력 계통을 유지한 pointmass-zero C172X 사용, 전체 크루즈 튜닝 중단, 현 상태 수정 없이 보존
- 미완료 TODO: 안전한 4단계 폐루프 제어, 완료 조건 보강, 안정고도·30초 순항
- 남은 리스크: Stage 4 complete 로그가 안전한 상승 완료를 의미하지 않음
- 권장 다음 작업: 롤 안정화와 피치·속도 에너지 관리부터 분리 검증한 뒤 4단계 완료 조건 재정의
- 최신 실행: 5.5.1__takeoff_stage3_stage4_diagnostic, timestamp 06211550
- Git 상태: Git 저장소 아님


## [2026-06-21 18:45] INDEX-20260621-1845-001 — 현재 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: RKSS RWY 14L JSBSim 기본 지구 C172X 이륙·1000 ft급 안정화·30초 순항
- 현재 상태: COMPLETE
- 최근 변경 파일: scripts/c172x/initial_condition/2.2__rkss_14l_default_earth_init.xml, scripts/c172x/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml, scripts/c172x/README.md
- 주요 결정: --planet default 명시, geodetic latitude 사용, elevation 38 ft와 altitude 4.305 ft AGL 분리, t=0.25 s 엔진 가동
- 최종 실행: 5.6.6__rkss14l_default_earth_takeoff_cruise30
- 검증 결과: 55 kt 회전, 약 63.48 KCAS 이륙, 1000 ft급 고도 포착, 30초 안정 순항, abort 없음
- 미완료 TODO: 공용 runner planet 기본값 정책 변경은 DEFERRED
- 남은 리스크: --planet default 옵션을 누락하면 이번 요구와 다른 지구 모델이 선택됨
- 권장 다음 작업: 필요 시 시나리오 전용 wrapper를 추가해 planet 옵션 누락을 구조적으로 방지
- Git 상태: Git 저장소 아님


## [2026-06-23 08:56] INDEX-20260623-0856-001 — 현재 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: RKSS 14L C172X 시동·이륙·30초 순항·엔진 정지·비제어 추락
- 현재 상태: standalone JSBSim 5.7 시나리오 COMPLETE, QGC 통합 OPEN
- 최근 변경 파일: scripts/c172x/runscript/5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml, scripts/c172x/README.md
- 주요 결정: 30초 순항 종료 후 엔진·AP·조종면·trim 중립, 첫 랜딩기어 접촉에서 종료
- 최종 실행: 5.7.1__rkss14l_takeoff_cruise_engineoff_crash
- 검증 결과: 엔진 정지 253.916667 s, 충돌 종료 277.616667 s, 충돌 시 121.24 KCAS·강하율 -27.70 ft/s·RPM 0
- QGC 결론: JSBSim 단독 직접 표시 불가, PX4 jsbsim_bridge 또는 별도 MAVLink adapter 필요
- 미완료 TODO: PX4 SITL+QGC 실시간 통합, 선택적 비상 활공 시나리오
- 남은 리스크: standalone runscript와 PX4 actuator 제어권 충돌 가능
- 권장 다음 작업: QGC가 필요하면 5.7 상태기계를 PX4 명령 기반 시퀀스로 분리하여 jsbsim_bridge에 연결
- Git 상태: Git 저장소 아님


## [2026-06-23 09:25] INDEX-20260623-0925-001 — 현재 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: `2026-06-23 09:25 KST`
- 최근 수행 과업: `c172x_empty_cg_aligned` 전용 시나리오 폴더 생성 및 대화형 runner 초기조건 없음 오류 해결
- 현재 상태: COMPLETE
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_empty_cg_aligned/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_empty_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_empty_cg_aligned/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_empty_cg_aligned/runscript/5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 주요 결정: runner 코드 매핑 대신 `scripts/<aircraft>/` 규칙에 맞춰 필요한 RKSS 14L 시나리오만 `scripts/c172x_empty_cg_aligned/`로 분리
- 검증 결과: XML 문법 검증 성공, `python3 -m py_compile scripts/run_jsbsim_timestamped.py` 성공, 새 경로 기반 5.7 실행 성공
- 최종 실행: `5.7.2__rkss14l_takeoff_cruise_engineoff_crash`, timestamp `06230925`
- 미완료 TODO:
  - `TODO-20260623-0925-001`: 기존 `scripts/c172x/README.md` 경로 예시 정리
  - `TODO-20260623-0925-002`: 원본/복사본 동기화 정책 확정
- 남은 리스크: 기존 `scripts/c172x/`와 새 `scripts/c172x_empty_cg_aligned/`에 RKSS 14L XML 복사본이 공존
- 권장 다음 작업: 사용자는 `cd ~/jsbsim_workflow/scripts && python3 run_jsbsim_timestamped.py` 실행 후 `39 -> 1 -> 2` 선택으로 대화형 경로 확인
- Git 상태: Git 저장소 아님

## [2026-06-23 09:50] INDEX-20260623-0950-001 — 현재 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: `2026-06-23 09:50 KST`
- 최근 수행 과업: JSBSim timestamp runner에 선택형 실시간 3D 애니메이션 기능 추가
- 현재 상태: COMPLETE, GUI 수동 검증은 OPEN
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/live_trajectory_3d.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 주요 결정: runner 내부 GUI 통합 대신 별도 `live_trajectory_3d.py` 프로세스와 JSBSim `--realtime`을 사용
- 검증 결과: Python 문법 검증, help 옵션 확인, headless animator CSV 로딩, 기존 `--no-live-3d` 실행, `--realtime` 명령 삽입 확인
- 최종 실행: `5.7.4__rkss14l_takeoff_cruise_engineoff_crash`, timestamp `06230949`
- 미완료 TODO:
  - `TODO-20260623-0950-001`: WSLg/X11 환경에서 실제 `--live-3d` GUI 창 수동 검증
- 남은 리스크: live 모드는 실제 시간 속도로 실행되므로 5.7은 약 278초 이상 걸리며, GUI display 환경이 없으면 창이 뜨지 않음
- 권장 다음 작업: 사용자 터미널에서 `--live-3d` 명령으로 GUI 창 확인
- Git 상태: Git 저장소 아님

## [2026-06-23 13:05] INDEX-20260623-1305-001 — 현재 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-23 13:05 KST
- 최근 수행 과업: CSV 저장 JSBSim property 역할별 분류 Excel workbook 생성
- 현재 상태: COMPLETE
- 최근 변경 파일:
  - /home/junyeopkwon/jsbsim_workflow/outputs/jsbsim_property_classification_20260623/jsbsim_csv_property_classification.xlsx
  - /home/junyeopkwon/jsbsim_workflow/outputs/jsbsim_property_classification_20260623/build_workbook.cjs
  - /home/junyeopkwon/jsbsim_workflow/outputs/jsbsim_property_classification_20260623/*.png
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정: 공용 runner의 OUTPUT_PROPERTIES, SIXDOF_VALIDATION_PROPERTIES, RAW_TO_SI_FIELDS를 기준으로 하되 기존 CSV 헤더와 XML output 정의를 cross-check로 포함
- 미완료 TODO: 신규 TODO 없음
- 남은 리스크: 역할 분류는 prefix·명칭 기반이며 JSBSim 공식 taxonomy 검증은 별도 작업
- 권장 다음 작업: 필요 시 jsbsim --catalog 출력과 연결해 property별 읽기/쓰기 권한 및 공식 설명 열 추가
- Git 상태: Git 저장소 아님

## [2026-06-29 11:04] TASK-20260629-1104-001 — 완료

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-29 11:04
- 최근 수행 과업: 5.6 RKSS C172X runscript의 FlightGear 연동 사용 여부 확인
- 현재 상태: FlightGear 연동은 runscript 자체가 아니라 scripts/c172x/output/fg_visual_5500.xml log directive를 JSBSim --logdirectivefile로 붙여 수행한 것으로 확인
- 최근 변경 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 주요 결정: 없음
- 미완료 TODO: 현재 FlightGear GUI 실기동 확인은 수행하지 않음
- 남은 리스크: fg_visual_5500.xml의 Windows host IP 172.29.80.1이 현재 환경에서는 바뀌었을 수 있음
- 권장 다음 작업: 현재 host IP에 맞게 output directive를 확인한 뒤 FlightGear native-fdm 수신과 JSBSim realtime 실행

## [2026-06-30 09:40] INDEX-20260630-0940-001 — 현재 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: `2026-06-30 09:40 KST`
- 최근 수행 과업: 75 kg × 4명 탑승자 pointmass C172X 변형 생성 및 5.6.1 higher-speed 이륙·순항 runscript 검증
- 현재 상태: COMPLETE
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_4x75kg_cg_aligned_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned/c172x_4x75kg_cg_aligned.xml`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned/c172x_4x75kg_cg_aligned.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 주요 결정: 4명 탑승자 pointmass는 각 75 kg으로 설정하고, luggage/external pointmass는 0으로 유지; runscript는 속도 관련 조건만 증가
- 검증 결과: 기존 5.6은 75kg×4명 변형에서 300초 종료 시 AGL 1308 ft로 STATE 6 완료 미확인, 5.6.1은 STATE 5/STATE 6 확인 및 최종 AGL 958.47 ft, KCAS 103.63
- 최종 실행: `5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed`, timestamp `06300939`
- 미완료 TODO: 신규 TODO 없음
- 남은 리스크: 5.6.1은 속도 조건 증분 실험 버전이며 실제 C172 탑승중량 절차 최적화는 별도 검토 필요
- 권장 다음 작업: 필요 시 5.6.1과 empty 5.6의 활주거리·이륙속도·고도포착 시간을 표로 비교
- Git 상태: Git 저장소 아님

## [2026-06-30 09:45] INDEX-20260630-0945-001 — 현재 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: `2026-06-30 09:45 KST`
- 최근 수행 과업: 현재 C172X 75kg×4명 5.6.1 실행의 FlightGear 시각화 연동 여부 확인
- 현재 상태: FlightGear 미연동, CSV/plot 생성만 수행
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 주요 결정: 없음
- 검증 결과: 현재 runner 실행에는 `--logdirectivefile scripts/c172x/output/fg_visual_5500.xml` 계열 연결이 없음
- 미완료 TODO: 신규 TODO 없음
- 남은 리스크: FlightGear 연결 시 `fg_visual_5500.xml`의 host IP/port 재확인 필요
- 권장 다음 작업: FlightGear 시각화가 필요하면 runner에 선택형 `--flightgear` 옵션 또는 별도 wrapper 추가
- Git 상태: Git 저장소 아님

## [2026-06-30 10:00] INDEX-20260630-1000-001 — 현재 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: `2026-06-30 10:00 KST`
- 최근 수행 과업: 선택형 FlightGear 시각화 스트림 옵션 추가
- 현재 상태: COMPLETE, 실제 GUI 수신 검증은 OPEN
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 주요 결정: FlightGear 연동은 자동 상시가 아니라 `--flightgear` 선택 시에만 활성화
- 검증 결과: help 옵션 확인, Python 문법 검증, 명령 구성 검증, `--no-flightgear` 회귀 실행 성공
- 최종 회귀 실행: `5.6.2__rkss14l_default_earth_takeoff_cruise30_higher_speed`, timestamp `06300959`
- 미완료 TODO: `TODO-20260630-1000-001` 실제 FlightGear GUI 수신 검증
- 남은 리스크: Windows host IP 변경 시 `fg_visual_5500.xml` 수정 필요
- 권장 다음 작업: FlightGear 창을 먼저 실행한 뒤 `--flightgear`로 실제 수신 확인
- Git 상태: Git 저장소 아님

## [2026-06-30 10:30] INDEX-20260630-1030-001 — 현재 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: `2026-06-30 10:30 KST`
- 최근 수행 과업: live3d runner 기능 제거 및 FlightGear 선택형 시각화 경로 유지
- 현재 상태: COMPLETE
- 최근 변경 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md`
  - `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 보존 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/live_trajectory_3d.py`
- 주요 결정: live3d는 runner에서 사용 중단하되 파일은 reference/backup utility로 보존, 시각화는 `--flightgear` 선택형 경로를 사용
- 검증 결과: `--live-3d` help 미노출, `--flightgear` help 노출, Python 문법 검증, `--no-flightgear` 회귀 실행 성공
- 최종 회귀 실행: `5.6.6__rkss14l_default_earth_takeoff_cruise30_higher_speed`, timestamp `06301029`
- 미완료 TODO: 기존 `TODO-20260630-1000-001` 실제 FlightGear GUI 수신 검증 유지
- 남은 리스크: `fg_visual_5500.xml`의 IP가 현재 Windows host IP와 다르면 FlightGear 수신 실패 가능
- 권장 다음 작업: FlightGear 창을 먼저 실행한 뒤 `--flightgear` 실제 수신 확인
- Git 상태: Git 저장소 아님

## [2026-06-30 11:19] CORRECTION-20260630-1119-001 — 정정

- 대상 기록: `INDEX-20260630-1118-001`
- 정정 이유: Windows PowerShell `Add-Content` 기본 인코딩으로 append되어 한글이 깨져 보이는 기록이 생성됨
- 기존 내용: 직전 `INDEX-20260630-1118-001` 항목은 인코딩 문제로 일부 환경에서 mojibake로 표시될 수 있음
- 정정 내용: 현재 최신 상태는 다음과 같음. `scripts/run_jsbsim_timestamped.py`의 trajectory plot 생성 로직에서 Z축 하한을 0으로 고정했고, 사용자가 첨부한 5.6.8 trajectory PNG를 새 설정으로 재생성함
- 영향 범위: 기록 표시 품질 정정. 실제 코드와 plot 결과는 유지
- 검증 결과: Python 문법 검사 통과, PNG 재생성 성공
- 다음 작업: 사용자 로컬에서 재생성 PNG를 열어 Z축 음수 눈금 제거 상태 확인

## [2026-06-30 11:28] INDEX-20260630-1128-001 — 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: 2026-06-30 11:28 KST
- 최근 수행 과업: 인코딩이 깨진 2026-06-30 11:18 agent-log 기록 블록 삭제
- 현재 상태: 사용자 승인에 따라 `TASK.md`, `PROGRESS.md`, `INDEX.md`의 깨진 11:18 블록을 제거했고, 세 파일 모두 UTF-8로 읽히는 상태를 확인함
- 최근 변경 파일: `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`, `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`, `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 주요 결정: 일반 append-only 원칙보다 사용자의 명시적 삭제 지시와 기록 혼란 방지를 우선하여, 이번 인코딩 사고 블록만 제한적으로 제거
- 미완료 TODO: 없음
- 남은 리스크: 11:19 정정 기록은 남아 있어 해당 인코딩 사고의 경위는 추적 가능
- 권장 다음 작업: 이후 Markdown 기록 append는 UTF-8 명시 방식으로만 수행

## [2026-06-30 11:39] INDEX-20260630-1139-001 — 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: 2026-06-30 11:39 KST
- 최근 수행 과업: `c172x_4x75kg_cg_aligned` interactive 실행용 scripts 폴더 추가
- 현재 상태: aircraft 선택 목록의 `c172x_4x75kg_cg_aligned`에 대응하는 `scripts/c172x_4x75kg_cg_aligned/` 폴더가 생겼고, init `2.2`와 runscript `5.6`, `5.6.1`이 interactive 선택에서 발견됨
- 최근 변경 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml`, `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml`, `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml`
- 주요 결정: runner 로직은 변경하지 않고 aircraft별 scripts 폴더 구조에 맞춰 누락 파일을 추가
- 미완료 TODO: 실제 300초 interactive full run은 사용자 실행으로 확인
- 남은 리스크: `5.6`은 비교용이며 4x75kg 모델에는 `5.6.1` high-speed runscript 사용이 권장됨
- 권장 다음 작업: interactive 실행 시 aircraft 39, init 1, runscript 2를 선택해 5.6.1 시나리오 실행

## [2026-06-30 11:47] INDEX-20260630-1147-001 — 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: 2026-06-30 11:47 KST
- 최근 수행 과업: FlightGear 선택 실행 시 JSBSim `SIGFPE` 원인 조사 및 interactive 기본 planet 수정
- 현재 상태: runner에서 `--planet` 미지정 시 JSBSim default Earth를 사용하도록 수정됨. FlightGear output은 `--planet` 없이 짧은 실행에서 SIGFPE 없이 진행됨
- 최근 변경 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`, `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`, `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`, `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md`, `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 주요 결정: runner 기본 planet을 nonrotating spherical earth에서 JSBSim builtin default Earth로 변경
- 미완료 TODO: 실제 Windows FlightGear GUI 수신 확인
- 남은 리스크: runner의 FlightGear `y`는 FlightGear 자동 실행이 아니라 UDP stream 활성화이므로, Windows FlightGear를 먼저 실행해야 함
- 권장 다음 작업: PowerShell에서 `fgfs.exe --fdm=external --native-fdm=socket,in,60,,5500,udp` 실행 후 runner에서 FlightGear stream `y` 선택

## [2026-06-30 14:25] INDEX-20260630-1425-001 — 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-06-30 14:25 KST
- 최근 수행 과업:
  - ADS Lift+Cruise eVTOL 모델 workflow 폴더 구성
- 현재 상태:
  - ADS aircraft XML snapshot은 aircraft_variants/ADS에 배치됨
  - ADS engine XML snapshot은 engine_variants/ADS에 배치됨
  - runner 선택용 ADS 초기조건과 runscript는 scripts/ADS/initial_condition 및 scripts/ADS/runscript에 배치됨
  - ADS 전용 logs/results/plots 폴더가 생성됨
  - scripts/ADS/README.md와 aircraft_variants/ADS/WORKFLOW_INSTALL.md가 추가됨
  - JSBSim 실행은 수행하지 않음
- 최근 변경 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_aero.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_battery_module.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_effectors.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_flight_control.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_ground_reactions.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_mass.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_metrics.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_model_setup.md
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_propulsion.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/WORKFLOW_INSTALL.md
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/initGimpo.xml
  - /home/junyeopkwon/jsbsim_workflow/engine_variants/ADS/ADS_lift_motor.xml
  - /home/junyeopkwon/jsbsim_workflow/engine_variants/ADS/ADS_lift_prop.xml
  - /home/junyeopkwon/jsbsim_workflow/engine_variants/ADS/ADS_pusher_motor.xml
  - /home/junyeopkwon/jsbsim_workflow/engine_variants/ADS/ADS_pusher_prop.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS/README.md
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS/initial_condition/1.0__gimpo_ground_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS/runscript/1.0__gimpo_30m_hover_run.xml
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정:
  - aircraft snapshot, engine snapshot, runner scripts, output folders를 분리해 구성
  - source tree 원본은 유지하고 workflow에는 진행용 복사본을 둠
- 미완료 TODO:
  - TODO-20260630-1425-001: ADS workflow 실제 실행 검증 및 source/workflow 동기화 정책 확정
  - 기존 TODO-20260630-1000-001: FlightGear GUI 수신 검증
- 남은 리스크:
  - JSBSim 실제 실행은 아직 하지 않았으므로 model load와 hover 결과는 미검증
  - source tree 원본과 workflow snapshot 간 동기화 정책이 필요함
  - ADS 전용 output property 후처리는 첫 실행 후 보강 필요할 수 있음
- 권장 다음 작업:
  - 사용자 승인 후 ADS model load와 짧은 hover run을 실행
  - logs/results/plots/ADS 산출물 생성 여부 확인
  - ADS 편집 기준 위치를 source tree 또는 workflow snapshot 중 하나로 확정
- Git 상태:
  - Git 저장소 아님

## [2026-06-30 14:28] INDEX-20260630-1428-001 — 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-06-30 14:28 KST
- 최근 수행 과업:
  - jsbsim_workflow Git 추가 가능 여부 확인
- 현재 상태:
  - jsbsim_workflow는 현재 Git 저장소가 아님
  - /home/junyeopkwon/.git은 존재하지만 비어 있어 유효한 상위 Git 저장소가 아님
  - 권장 방식은 jsbsim_workflow를 별도 Git 저장소로 초기화하는 것
- 최근 변경 파일:
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정:
  - 실제 git init/add/commit/push는 사용자 확인 전 수행하지 않음
- 미완료 TODO:
  - 원격 저장소 URL 확인
  - .gitignore 정책 확정
- 남은 리스크:
  - 산출물 폴더를 그대로 Git에 포함하면 저장소 크기가 커질 수 있음
- 권장 다음 작업:
  - 별도 저장소로 초기화할지, 원격 저장소를 연결할지 사용자 결정 필요
- Git 상태:
  - Git 저장소 아님


## [2026-06-30 14:34] INDEX-20260630-1434-001 — DONE

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-30 14:34 KST
- 최근 수행 과업: /home/junyeopkwon/jsbsim_workflow를 로컬 Git 저장소로 초기화하고 초기 커밋 생성
- 현재 상태: main 브랜치의 로컬 Git 저장소가 생성되었으며, ADS workflow 구성 파일과 문서가 커밋됨
- 최근 변경 파일: /home/junyeopkwon/jsbsim_workflow/.gitignore, /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md, /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md, /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md, /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md, /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정: 재생성 가능한 logs/, results/, plots/, outputs/와 Python cache는 Git 추적에서 제외
- 미완료 TODO: 원격 저장소 URL 확보 후 remote 등록 및 push
- 남은 리스크: ADS 모델은 아직 JSBSim 실제 실행으로 검증하지 않았고, 원격 저장소 동기화도 수행하지 않음
- 권장 다음 작업: 원격 저장소 URL 제공 후 git remote add origin 및 git push -u origin main 수행


## [2026-06-30 15:09] INDEX-20260630-1509-001 — DONE

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-30 15:09 KST
- 최근 수행 과업: ADS 관련 산출물 저자 표기를 junyeopkwon으로 통일
- 현재 상태: ADS XML 및 Markdown 파일의 저자 표기가 junyeopkwon으로 변경됨
- 최근 변경 파일: ADS 관련 XML 및 Markdown 파일, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/INDEX.md
- 주요 결정: 기존 author 태그는 변경하고, 태그가 없는 XML에는 Author 주석을 추가
- 미완료 TODO: JSBSim 실제 실행 검증, 원격 저장소 publish 확인
- 남은 리스크: workflow_all_cases_initial_settings.xlsx의 별도 변경은 이번 작업 범위에서 제외됨
- 권장 다음 작업: GitHub Desktop에서 Publish repository 실행 후 원격 저장소 파일 확인


## [2026-06-30 15:20] INDEX-20260630-1520-001 — DONE

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-30 15:20 KST
- 최근 수행 과업: ADS 30 m hover 실행 로그 해석
- 현재 상태: runscript 의도와 달리 실제 로그에서는 30 m hover가 발생하지 않은 것으로 확인
- 최근 변경 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/TODO.md, docs/agent-log/INDEX.md
- 주요 결정: 즉시 수정하지 않고 먼저 로그 기반 원인과 수정 필요 항목을 기록
- 미완료 TODO: ADS 초기조건, 추력 스케줄, 출력 property 보강 후 재실행
- 남은 리스크: 현재 ADS 모델은 placeholder 추력으로 20 kg MTOW 수직이륙 추력이 부족할 수 있음
- 권장 다음 작업: ADS hover 미션 수정 후 짧은 실행으로 30 m 도달 여부 재검증


## [2026-06-30 15:27] INDEX-20260630-1527-001 — DONE

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-30 15:27 KST
- 최근 수행 과업: ADS 현재 구현 motor/prop 기준 비행 가능 중량 추정
- 현재 상태: 로그 기반 절대 hover 한계 약 17.6 kgf, 실용 MTOW 권장 범위 약 12~15 kg로 추정
- 최근 변경 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/TODO.md, docs/agent-log/INDEX.md
- 주요 결정: 기존 실행 로그 최대 추력을 기준으로 보수적으로 추정
- 미완료 TODO: full throttle 정적 추력 sweep runscript 작성 및 실행
- 남은 리스크: 실제 ADS 전용 throttle command가 sixdof_raw에 없어 command-추력 매핑이 불완전함
- 권장 다음 작업: thrust sweep 후 20 kg 목표를 유지할지, placeholder prop/motor를 재보정할지 결정


## [2026-06-30 15:36] INDEX-20260630-1536-001 — DONE

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-30 15:36 KST
- 최근 수행 과업: JSBSim engine 디렉터리의 모터/프로펠러 정의 및 ADS/F450 사용 조합 확인
- 현재 상태: ADS는 ADS 전용 placeholder motor/prop을 사용하고, JSBSim 예제 멀티콥터는 DJI_E305 + DJI_9450을 사용함
- 최근 변경 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 주요 결정: 이번 단계에서는 목록 확인만 수행하고 모델 수정은 하지 않음
- 미완료 TODO: 후보별 추력 sweep 비교
- 남은 리스크: 기본 제공 DJI 조합은 F450 1.4 kg급이라 ADS 20 kg급에 직접 사용하기 어려움
- 권장 다음 작업: ADS 목표 MTOW에 맞는 motor/prop placeholder 재보정 또는 정적 추력 sweep 수행


## [2026-06-30 18:26] INDEX-20260630-1826-001 — DONE

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-30 18:26 KST
- 최근 수행 과업: ADS_mini 1 kg DJI_E305 + DJI_9450 기반 10 m hover/landing 테스트 생성 및 실행
- 현재 상태: ADS_mini runscript가 JSBSim에서 정상 종료했고, 15~25 s 구간 9.61~9.78 m hover 및 60 s 이후 throttle 0 착륙 상태 확인
- 최근 변경 파일: ADS_mini aircraft XML, ADS_mini initial condition, ADS_mini runscript, docs/agent-log/*
- 주요 결정: 기존 ADS 20 kg은 유지하고, workflow/FCS 검증용 ADS_mini 1 kg 모델을 별도로 운용
- 미완료 TODO: hover pitch trim 개선, landing gear contact chatter 개선, Git commit 여부 결정
- 남은 리스크: ADS_mini는 20 kg ADS 성능 검증 모델이 아니며, 현재 hover 자세는 수평 hover가 아님
- 권장 다음 작업: ADS_mini 자세/ground reaction 튜닝 후 Git에 커밋


## [2026-06-30 18:36] INDEX-20260630-1836-001 — DONE

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-30 18:36 KST
- 최근 수행 과업: ADS_mini 10 m hover/landing runscript 이벤트 구조 확인
- 현재 상태: 적용 runscript 이벤트 설명 완료
- 최근 변경 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 주요 결정: 파일 수정 없이 현재 적용 상태만 설명
- 미완료 TODO: 없음
- 남은 리스크: runscript 설명은 현재 파일 기준이며 이후 튜닝 시 이벤트 값이 바뀔 수 있음
- 권장 다음 작업: 필요 시 hover 자세와 landing contact chatter 튜닝


## [2026-06-30 18:48] INDEX-20260630-1848-001 — DONE

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-06-30 18:48 KST
- 최근 수행 과업: ADS_mini XML 의사코드 설명 자료 작성
- 현재 상태: ADS_mini 구성 XML과 mission XML을 설명하는 Markdown 문서가 생성됨
- 최근 변경 파일: /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS_mini/ADS_mini_xml_pseudocode.md, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/INDEX.md
- 주요 결정: XML 원문을 단순 번역하지 않고 JSBSim 처리 흐름 중심의 한국어 의사코드로 작성
- 미완료 TODO: ADS 원형 XML 의사코드 문서가 필요하면 별도 작성
- 남은 리스크: 모델 튜닝으로 XML 값이 바뀌면 설명 문서 갱신 필요
- 권장 다음 작업: 문서 검토 후 ADS_mini 변경분 Git commit

## [2026-07-01 00:00] INDEX-20260701-0000-ADS0 — 상태 스냅샷

- 프로젝트명: `jsbsim_workflow`
- 최근 수행 과업: ADS 0 zero-value 기체 템플릿 XML 생성
- 현재 상태: `aircraft_variants/ADS_0` 및 `engine_variants/ADS_0`에 14개 XML 템플릿 생성 완료. JSBSim 실행은 수행하지 않음.
- 최근 변경 파일:
- `aircraft_variants/ADS_0/ADS_0.xml`
- `aircraft_variants/ADS_0/ADS_0_aero.xml`
- `aircraft_variants/ADS_0/ADS_0_battery_module.xml`
- `aircraft_variants/ADS_0/ADS_0_effectors.xml`
- `aircraft_variants/ADS_0/ADS_0_flight_control.xml`
- `aircraft_variants/ADS_0/ADS_0_ground_reactions.xml`
- `aircraft_variants/ADS_0/ADS_0_mass.xml`
- `aircraft_variants/ADS_0/ADS_0_metrics.xml`
- `aircraft_variants/ADS_0/ADS_0_propulsion.xml`
- `aircraft_variants/ADS_0/initGimpo.xml`
- `engine_variants/ADS_0/ADS_0_lift_motor.xml`
- `engine_variants/ADS_0/ADS_0_lift_prop.xml`
- `engine_variants/ADS_0/ADS_0_pusher_motor.xml`
- `engine_variants/ADS_0/ADS_0_pusher_prop.xml`
- 주요 결정: 공백 포함 `ADS 0` 대신 파일/참조 안전성을 위해 `ADS_0` 이름을 사용
- 미완료 TODO: 실제 제원/공력/추력/질량/랜딩기어 데이터 입력 및 실행 검증
- 남은 리스크: 현재 템플릿은 모든 수치가 0이라 실행 가능한 기체 모델이 아님
- 권장 다음 작업: 실제 데이터가 확보되면 `ADS_0`를 복제해 운영 기체명으로 만들고, 항목별 값을 채운 뒤 XML 로딩부터 검증

## [2026-07-19 23:35] INDEX-20260719-2335-001 — DONE

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-19 23:35 KST
- 최근 수행 과업:
  - C172X 4x75kg 김포 lat/lon 450 m east-heading 초기조건 및 무추력 추락/활공 runscript 생성
- 현재 상태:
  - 초기조건 XML과 runscript 2개 생성 완료
  - 6.0.2 중립 무추력 추락 및 6.1.1 heading hold/trim 활공이 JSBSim runner에서 정상 실행되고 nose gear ground contact 시 종료됨
- 최근 변경 파일:
  - scripts/c172x_4x75kg_cg_aligned/initial_condition/6.0__gimpo_450m_east_60ms_init.xml
  - scripts/c172x_4x75kg_cg_aligned/runscript/6.0__gimpo_450m_east_60ms_neutral_noengine_drop_run.xml
  - scripts/c172x_4x75kg_cg_aligned/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_glide_run.xml
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 75 kg x 4명 조건은 기존 c172x_4x75kg_cg_aligned aircraft variant가 만족하므로 새 aircraft XML을 만들지 않고 재사용
  - 김포공항 조건은 lat/lon만 기존 RKSS 값을 사용하고 heading은 동쪽 90.0 deg로 강제
  - 지면 접촉 검출을 위해 terrain elevation은 기존 김포 초기조건의 38 ft 유지
- 미완료 TODO:
  - TODO-20260719-2335-001: 6.1 pitch trim 최적화는 별도 과업으로 DEFERRED
- 남은 리스크:
  - 6.0은 무조종 조건이므로 충돌 시 heading이 113.94 deg까지 변함
  - 6.1의 pitch trim 0.18은 실행 가능한 기준값이며 최적값은 아님
  - workflow_all_cases_initial_settings.xlsx는 runner에 의해 자동 갱신됐고 작업 전부터 modified 상태였음
- 권장 다음 작업:
  - 필요 시 6.1 trim sweep과 trajectory 비교 플롯 검토

## [2026-07-19 23:50] INDEX-20260719-2350-001 — DONE

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-19 23:50 KST
- 최근 수행 과업:
  - C172X 4x75kg zero-propulsion aircraft variant 및 6.0/6.1 no-thrust runscript 생성/검증
- 현재 상태:
  - c172x_4x75kg_cg_aligned_zeroprop aircraft가 workflow와 JSBSim install tree에 생성됨
  - 6.0.2 중립 zero-prop 추락은 205.258333 s에 Nose Gear WOW로 종료
  - 6.1.1 heading hold/trim zero-prop 활공은 137.150000 s에 Nose Gear WOW로 종료하고 yaw 89.872697 deg 유지
- 최근 변경 파일:
  - aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop/c172x_4x75kg_cg_aligned_zeroprop.xml
  - scripts/c172x_4x75kg_cg_aligned_zeroprop/initial_condition/6.0__gimpo_450m_east_60ms_init.xml
  - scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.0__gimpo_450m_east_60ms_neutral_zeroprop_drop_run.xml
  - scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide_run.xml
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop/
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - zero dummy propulsion은 engine/thruster 제거 방식으로 구현
  - fuel tank, 75 kg x 4 pointmass, CG-aligned mass, aerodynamics, FCS, ground reactions는 유지
- 미완료 TODO:
  - TODO-20260719-2350-001: generator script 추가는 DEFERRED
- 남은 리스크:
  - zero-propulsion 조건은 windmilling prop drag도 제거함
  - heading hold는 이번 초기조건에서는 가능했지만 저동압/실속 조건에서는 보장되지 않음
  - workflow_all_cases_initial_settings.xlsx는 runner에 의해 자동 갱신됐고 작업 전부터 modified 상태였음
- 권장 다음 작업:
  - 필요 시 기존 propeller-installed engine-off run과 zero-prop run의 trajectory/impact state 비교


## [2026-07-20 09:20] INDEX-20260720-0920-001 ? DONE

- ?????:
  - jsbsim_workflow
- ?? ??:
  - 2026-07-20 09:20 KST
- ?? ?? ??:
  - JSBSim runner ?? plotting ?? ?? ??
- ?? ??:
  - run_jsbsim_timestamped.py? ?? plots ?? ???? ????? ploting/<aircraft>/<run_id>/ ?? ???? ?? ???
  - zero-prop 6.1.2 ?? ???? ?? PNG 307?, events.csv, 6DOF dual-axis plot 11? ?? ??
  - PROGRESS-20260720-0910-001 append? ???? ?? CORRECTION-20260720-0920-001 ? PROGRESS-20260720-0920-001? ?? ??? ???
- ?? ?? ??:
  - scripts/run_jsbsim_timestamped.py
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- ?? ??:
  - ?? plot ??? ??? ?? spelling? ?? ploting ??
  - ?? event? ???? ???? ??
  - ?? ??? event? console log?? ??? E0/E1/E2 marker? ??
- ??? TODO:
  - ??
- ?? ???:
  - ?? plotting ??? ?? ??? ?? ?? ???
  - dual-axis ?? ??? ?? ?? ???? ??? ?? ?? ??? ??
  - workflow_all_cases_initial_settings.xlsx? runner? ?? ?? ???? ?? ??? modified ????
- ?? ?? ??:
  - ?? ? dual-axis ?? ??? ?? ??? ?? ????? ??

## [2026-07-20 09:30] INDEX-20260720-0930-001 — DONE

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 09:30 KST
- 최근 수행 과업:
  - JSBSim runner 상세 plotting 출력 구조 추가 및 기록 정정
- 현재 상태:
  - un_jsbsim_timestamped.py가 기존 plots/ 요약 산출물을 유지하면서 ploting/<aircraft>/<run_id>/ 상세 산출물을 추가 생성함
  - zero-prop 6.1.2 검증 실행에서 PNG 307개, events.csv, 6DOF dual-axis plot 11개 생성 확인
  - 09:10 및 09:20 기록 중 일부가 here-doc/인코딩 문제로 손상되어 09:30 정정 기록을 append함
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 상세 plot 폴더는 사용자 요청 spelling을 따라 ploting 사용
  - 단일 event는 그래프에 표시하지 않음
  - 실제 실행된 event만 console log에서 파싱해 E0, E1, E2 marker로 표시
- 미완료 TODO:
  - 없음
- 남은 리스크:
  - 상세 plotting 추가로 실행 시간과 파일 수가 증가함
  - dual-axis 기본 조합은 확장 가능 후보이며 완전한 연구 표준 세트는 아님
  - workflow_all_cases_initial_settings.xlsx는 runner에 의해 자동 갱신됐고 작업 전부터 modified 상태였음
- 권장 다음 작업:
  - 필요 시 dual-axis 조합 목록을 연구 목적에 맞게 추가하거나 정리

## [2026-07-20 09:35] CORRECTION-20260720-0935-001 — 정정

- 대상 기록:
  - INDEX-20260720-0930-001
- 정정 이유:
  - PowerShell backtick escape 영향으로 run_jsbsim_timestamped.py 표기가 일부 손상됨
- 기존 내용:
  - un_jsbsim_timestamped.py처럼 보이는 손상된 파일명 표기
- 정정 내용:
  - 정확한 파일명은 scripts/run_jsbsim_timestamped.py임
  - 현재 runner는 기존 plots 요약 산출물을 유지하면서 ploting/<aircraft>/<run_id>/ 상세 산출물을 추가 생성함
- 영향 범위:
  - docs/agent-log/INDEX.md 기록 가독성
- 검증 결과:
  - python3 -m py_compile scripts/run_jsbsim_timestamped.py 통과
  - zero-prop 6.1.2 실행에서 상세 PNG 307개 생성 확인
- 다음 작업:
  - 없음

## [2026-07-20 10:00] INDEX-20260720-1000-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: ploting 위치 계열 y축 offset 제거 및 ECI/ECEF 절대 위치 delta 표시 적용
- 현재 상태: scripts/run_jsbsim_timestamped.py의 상세 ploting 산출물에서 eci_z_m 같은 절대 위치 계열은 초기값 기준 변화량으로 표시됨
- 최근 변경 파일: scripts/run_jsbsim_timestamped.py, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/INDEX.md
- 주요 결정: ECI/ECEF 절대 위치는 큰 기준값 offset 대신 Delta from initial로 표시하고 ScalarFormatter(useOffset=False)를 적용함
- 미완료 TODO: 이번 과업 기준 신규 미완료 TODO 없음
- 남은 리스크: 다른 명명 규칙의 절대 위치 property는 필요 시 위치 token 목록 확장이 필요함
- 권장 다음 작업: 새 ploting 산출물에서 사용자가 원하는 추가 위치 property가 있는지 확인 후 패턴 확장 여부 결정

## [2026-07-20 10:57] INDEX-20260720-1057-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 10:57 KST
- 최근 수행 과업:
  - C172X 4x75kg 4명 탑승 정상 이륙 runscript 생성 전 설계안 제시
- 현재 상태:
  - 새 runscript는 아직 생성하지 않았고, c1723.xml, 기존 5.6/5.6.1 workflow runscript, Purdue C172 자료, N13701 V-speeds 자료를 기준으로 구성 방향을 정리함
- 최근 변경 파일:
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 정상 이륙 기본안은 flap 0 deg, Vr 55 KIAS, Vy 76 KIAS, aircraft c172x_4x75kg_cg_aligned로 구성
  - short-field/soft-field의 10 deg flap과 Vx climb은 별도 옵션으로 분리
- 미완료 TODO:
  - TODO-20260720-1057-001: 사용자 확인 후 신규 runscript 생성 및 JSBSim 실행 검증
- 남은 리스크:
  - PDF mph IAS와 Purdue KIAS 값은 모델/연식 차이가 있어 동일 기준이 아님
  - 실제 4x75kg 중량 조건에서 이륙 성능은 실행 후 elevator/throttle/autopilot 튜닝이 필요할 수 있음
- 권장 다음 작업:
  - 설계안 승인 후 신규 XML runscript 생성, runner 실행, event/속도/고도 로그 검증

## [2026-07-20 11:31] INDEX-20260720-1131-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 11:31 KST
- 최근 수행 과업:
  - C172X 4x75kg RKSS 14L 정상 이륙, 500 m AGL 상승, 동일 방향 30초 cruise runscript 생성 및 검증
- 현재 상태:
  - 신규 5.8 runscript가 생성됐고 JSBSim run 5.8.3에서 정상 종료 확인
  - cruise 구간은 496.507421-510.553112 m AGL, heading 134.640051-134.796973 deg 범위로 유지됨
- 최근 변경 파일:
  - scripts/c172x_4x75kg_cg_aligned/runscript/5.8__rkss14l_normal_takeoff_climb500m_cruise30_run.xml
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - Stage 2 nose-lightening 없이 55 KIAS에서 rotate
  - 30초 cruise 종료는 FG_RAMP timer가 아니라 delay 30.0으로 구현
  - 500 m capture 후 altitude_setpoint 1600 ft, throttle 0.70으로 overshoot를 줄임
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - workflow_all_cases_initial_settings.xlsx는 runner 실행으로 자동 갱신됨
  - 실제 C172 POH 이륙거리/상승률과의 정밀 비교는 별도 검증 필요
- 권장 다음 작업:
  - 필요 시 5.8.3 plot과 CSV를 기준으로 takeoff roll distance, climb rate, cruise speed를 연구 표에 반영

## [2026-07-20 11:47] INDEX-20260720-1147-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 11:47 KST
- 최근 수행 과업:
  - 상세 ploting event marker/legend 가독성 개선
- 현재 상태:
  - event E0-E6는 legend가 아니라 그래프 위쪽 label과 상단 rail로 표시됨
  - dual-axis plot 데이터 legend는 그래프 밖 오른쪽에 배치됨
  - 기존 5.8.3 상세 ploting 산출물은 새 스타일로 재생성됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - event marker는 _nolegend_ 처리
  - E label과 time은 점선 상단에 직접 표시
  - 이벤트 구간은 상단 rail로 표시
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - view_image 도구 오류로 실제 이미지 육안 확인은 못 했고 PIL 기반 렌더링 확인으로 대체함
- 권장 다음 작업:
  - 사용자가 새 PNG를 보고 label lane 높이, rail 색상, 구간 label 표시 기준을 취향에 맞게 미세 조정

## [2026-07-20 11:52] INDEX-20260720-1152-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 11:52 KST
- 최근 수행 과업:
  - 상세 ploting event marker를 별도 상단 strip으로 분리해 title/label/rail 겹침 개선
- 현재 상태:
  - event label/time 및 event 구간 rail은 별도 상단 subplot에 표시됨
  - 본 plot에는 red dashed vertical line만 남음
  - 기존 5.8.3 상세 ploting 산출물은 새 2행 구조로 재생성됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 여백 확대가 아니라 별도 event strip subplot으로 분리
  - 이미지 높이는 약간 키워 이벤트 표시와 데이터 plot을 분리
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - 이벤트 수가 더 많은 run에서는 label lane 수나 strip 높이 추가 조정 가능성 있음
- 권장 다음 작업:
  - 새 PNG를 열어 사용자가 원하는 label 크기, rail 색상, strip 높이를 최종 취향에 맞게 조정

## [2026-07-20 12:04] INDEX-20260720-1204-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 12:04 KST
- 최근 수행 과업:
  - 상세 ploting event 표시를 구간 rail이 아닌 이벤트 시작점 표시로 정정
- 현재 상태:
  - 상단 strip에는 E0, E1 같은 event start label만 표시됨
  - E0-E1 같은 구간 rail과 interval label은 제거됨
  - 기존 5.8.3 상세 ploting 산출물은 새 방식으로 재생성됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 이벤트 구간 표현을 제거하고 이벤트 시작점 marker만 유지
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - view_image 도구 오류로 실제 이미지 육안 확인은 사용자 확인 필요
- 권장 다음 작업:
  - 새 PNG에서 E label 크기와 strip 높이가 적절한지 확인

## [2026-07-20 12:12] INDEX-20260720-1212-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 12:12 KST
- 최근 수행 과업:
  - 상세 ploting event label 겹침 추가 개선 및 기본 0,0 시작 표시 적용
- 현재 상태:
  - event strip은 box 없는 E label과 vertical start marker만 표시함
  - 구간 rail, interval label, event time text는 제거됨
  - from_start/distance_from_start 위치 계열은 표시 시 첫 값을 빼서 0에서 시작함
  - nonnegative time-series 축은 기본 x/y 원점이 0으로 맞춰짐
  - 기존 5.8.3 상세 ploting 산출물은 새 방식으로 재생성됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - label box 제거
  - 시작점 기준 위치 계열은 표시 단계에서 zero-initial 처리
  - 축 원점은 데이터가 양수 범위이면 0으로 고정
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - view_image 도구 오류로 실제 이미지 육안 확인은 사용자 확인 필요
- 권장 다음 작업:
  - 새 PNG를 열어 E label 간격과 0,0 시작 표시가 원하는 수준인지 확인


## [2026-07-20 12:21] INDEX-20260720-1221-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 12:21 KST
- 최근 수행 과업:
  - 상세 ploting event start label을 숫자 원형 marker로 변경 확인
- 현재 상태:
  - event label은 E0 형식이 아니라 0, 1, 2 숫자만 사용함
  - 상단 event strip은 빨간 점선 위에 빨간 원형 marker와 흰 숫자를 표시함
  - 구간 rail, interval label, event time text는 제거된 상태를 유지함
  - 기본 0,0 시작 표시 보정은 유지됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - event marker는 E 접두어 없이 숫자-only circle marker로 표시
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - view_image 도구 오류로 실제 이미지 육안 확인은 사용자 확인 필요
- 권장 다음 작업:
  - 새 PNG에서 숫자 원형 marker 겹침이 충분히 줄었는지 확인


## [2026-07-20 12:22] INDEX-20260720-1222-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 12:22 KST
- 최근 수행 과업:
  - 숫자 원형 event marker 변경 후 코드 diff check 및 py_compile 재검증
- 현재 상태:
  - scripts/run_jsbsim_timestamped.py는 코드 diff check와 py_compile을 통과함
  - events.csv label은 0..6 숫자만 사용함
  - docs/agent-log 전체 diff check에는 append-only 기록의 trailing whitespace가 남아 있음
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - event marker는 숫자-only circle marker로 유지
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - view_image 도구 오류로 PNG 육안 확인은 사용자 확인 필요
  - append-only 기록 원칙상 기존 trailing whitespace는 수정하지 않음
- 권장 다음 작업:
  - 새 PNG를 열어 숫자 원형 marker 배치를 육안 확인


## [2026-07-20 12:31] INDEX-20260720-1231-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 12:31 KST
- 최근 수행 과업:
  - 상세 ploting 숫자 event marker를 점선 상단 끝 중심에 일괄 정렬
- 현재 상태:
  - event marker label은 숫자-only circle marker임
  - 모든 marker는 상단 event strip에서 동일 y 위치 0.96에 배치됨
  - vertical dashed line의 ymax 0.96과 marker center가 맞춰짐
  - 기존 5.8.3 상세 ploting 산출물은 새 배치로 재생성됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - marker lane 분산을 제거하고 같은 높이 정렬을 채택
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - view_image 도구 오류로 실제 이미지 육안 확인은 사용자 확인 필요
  - 0과 1처럼 매우 가까운 event marker는 같은 높이에서 일부 겹칠 수 있음
- 권장 다음 작업:
  - 새 PNG를 열어 같은 높이 marker 배치가 의도와 맞는지 확인


## [2026-07-20 12:45] INDEX-20260720-1245-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 12:45 KST
- 최근 수행 과업:
  - dual-axis 상세 plot legend를 x축 제목 아래로 이동
- 현재 상태:
  - dual-axis plot은 legend_below_x_axis를 사용함
  - dual-axis legend는 x축 아래 중앙에 세로 1열로 표시됨
  - dual-axis plot은 right 0.90, bottom 0.27 여백을 사용함
  - 기존 5.8.3 상세 ploting 산출물은 새 legend 배치로 재생성됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - dual-axis legend는 오른쪽 바깥이 아니라 x축 제목 아래 중앙에 배치
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - view_image 도구 오류로 실제 이미지 육안 확인은 사용자 확인 필요
  - 긴 label 조합에서는 아래 legend가 이미지 좌우 폭에 근접할 수 있음
- 권장 다음 작업:
  - 새 dual-axis PNG를 열어 x축 제목 아래 legend 위치가 의도와 맞는지 확인


## [2026-07-20 12:55] INDEX-20260720-1255-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 12:55 KST
- 최근 수행 과업:
  - 현재 구현 기준 C172 이륙 절차와 runscript event 구성 설명 정리
- 현재 상태:
  - 5.8 normal takeoff runscript는 event 0~6 단계로 구성됨
  - 5.8.3 검증 run은 55.023200 KIAS에서 rotation, 500 m AGL 인근 포착, 30 s cruise 후 종료를 확인함
- 최근 변경 파일:
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 이번 답변은 현재 구현 파일과 기존 검증 로그 기준으로 작성
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - 실제 POH와 절차 세부값의 엄밀한 일치는 별도 외부 자료 재확인 필요
- 권장 다음 작업:
  - 발표 슬라이드에 넣을 경우 Flap 0 구현과 Flap 10 절차의 차이를 명시


## [2026-07-20 13:05] INDEX-20260720-1305-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 13:05 KST
- 최근 수행 과업:
  - c1723_run.xml event 5 필요 여부 분석
- 현재 상태:
  - 원본 c1723_run.xml의 Adjust throttle/flaps event는 flap retract와 heading 변경을 담당함
  - 원본의 Time Notify persistent event는 notify 전용으로 동역학 제어에는 직접 영향 없음
  - 신규 5.8 script의 STATE 5는 30초 cruise timer 시작점으로 의미가 있음
- 최근 변경 파일:
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - event 번호 해석에 따라 삭제 가능 여부가 달라지므로 원본 event와 신규 STATE event를 구분해 설명
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - event 제거 실험은 별도 시뮬레이션 재실행으로 확인 필요
- 권장 다음 작업:
  - 실제 삭제를 원하면 별도 브랜치/복사본에서 제거 후 event log와 climb 결과 비교


## [2026-07-20 21:52] INDEX-20260720-2152-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 21:52 KST
- 최근 수행 과업:
  - c1723_run.xml에서 Time Notify를 제거한 별도 runscript 생성 및 실행
- 현재 상태:
  - scripts/c172x/runscript/c1723_no_time_notify_run.xml 생성됨
  - run 0.0.1__c1723_no_time_notify 실행 산출물 생성됨
  - console End와 CSV final time 1000.008333 s 확인됨
  - events.csv에는 0~4 event만 기록됨
- 최근 변경 파일:
  - scripts/c172x/runscript/c1723_no_time_notify_run.xml
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 원본 c1723_run.xml은 유지하고 별도 no-time-notify runscript를 생성
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - wrapper 명령은 plotting 포함 180초 제한에서 timeout code 124 발생
  - 그러나 console End와 CSV final time 기준으로 JSBSim 실행은 완료됨
- 권장 다음 작업:
  - 필요하면 원본 c1723_run.xml 실행 결과와 no-time-notify 결과를 동일 metric으로 비교


## [2026-07-20 22:10] INDEX-20260720-2210-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-20 22:10 KST
- 최근 수행 과업:
  - sixdof_dual_axis 근거 설명 및 고도-총속도, 총속도-RPM plot 추가
- 현재 상태:
  - sixdof_dual_axis는 6DOF 상태-변화율/원인 진단용 pair 기반 plot임
  - derived/v-total-fps가 v-north/east/down 성분으로 계산됨
  - altitude_vs_total_speed.png 추가됨
  - total_speed_vs_engine_propeller_rpm.png 추가됨
  - 5.8.3 및 c1723_no_time_notify ploting은 sixdof_dual_axis 13개 구성으로 재생성됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - total speed는 sixdof_raw 성분 기반 derived series로 계산
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - 신규 plot의 최종 시각 배치는 사용자 육안 확인 필요
- 권장 다음 작업:
  - 고도-총속도와 총속도-RPM plot이 발표/분석 목적에 맞는지 확인


## [2026-07-20 22:20] INDEX-20260720-2220-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 최근 수행 과업:
  - c1723_no_time_notify plot에서 650초 이후 total speed 급상승 원인 분석
- 현재 상태:
  - 650초 이후 속도 증가는 6000 ft altitude capture 부근 autopilot pitch-down 및 full throttle 유지에 따른 것으로 판단됨
  - 해당 시점에 새 script event는 없음
- 최근 변경 파일:
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 원인 분석은 기존 runscript/log/CSV 기반으로 수행
- 남은 리스크:
  - total speed는 derived ground velocity magnitude이므로 airspeed 해석과 구분 필요
- 권장 다음 작업:
  - 장시간 원본 c1723 plot은 autopilot climb 테스트로 보고, 정상 이륙 절차 검증은 5.8 스크립트 기준 plot을 사용


## [2026-07-21 09:11] INDEX-20260721-0911-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-21 09:11 KST
- 최근 수행 과업:
  - 요청 표의 4개 dual-axis 그래프를 sixdof_dual_axis에 추가
- 현재 상태:
  - altitude_vs_calibrated_airspeed, elevator_command_vs_pitch, rudder_command_vs_heading, altitude_capture_vs_climb_rate pair가 코드에 추가됨
  - 기존 5.8.3/c1723_no_time_notify는 과거 CSV 한계로 rudder_command_vs_heading 제외 3개 추가 생성됨
  - 신규 5.8.4 normal takeoff 실행에서는 4개 모두 생성됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - sixdof_dual_axis 생성 시 raw CSV도 병합해 요청 property를 활용
- 미완료 TODO:
  - 이번 과업 기준 신규 TODO 없음
- 남은 리스크:
  - 과거 로그에는 rudder-cmd-norm이 없어 3번 plot은 새 실행부터 생성 가능
- 권장 다음 작업:
  - 발표/분석에는 4개가 모두 있는 5.8.4 ploting 산출물을 기준으로 사용


## [2026-07-21 09:18] INDEX-20260721-0918-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-21 09:18 KST
- 최근 수행 과업:
  - alt_vs_vc_kts.png 파일명으로 고도-VC dual-axis plot 추가
- 현재 상태:
  - sixdof_dual_axis에 alt_vs_vc_kts pair가 추가됨
  - 5.8.4 ploting은 sixdof_dual_axis 18개 구성으로 재생성됨
  - alt_vs_vc_kts.png가 생성됨
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 기존 altitude_vs_calibrated_airspeed와 동일 데이터지만 찾기 쉬운 파일명 alias로 추가
- 남은 리스크:
  - 중복 plot이므로 분석 시 둘 중 하나만 사용하면 됨
- 권장 다음 작업:
  - 발표 자료에는 alt_vs_vc_kts.png 파일명을 사용

## [2026-07-21 13:18] INDEX-20260721-1318-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-21 13:18 KST
- 최근 수행 과업:
  - JSBSim 내장 F450 Test_F450_Launch.xml를 workflow F450 runscript로 추가하고 실행 검증
- 현재 상태:
  - scripts/F450/runscript/1.1__test_f450_launch_run.xml가 추가됨
  - F450 runscript discovery에서 1.1__test_f450_launch가 선택 가능함
  - run 1.1.1__test_f450_launch가 JSBSim에서 정상 종료됨
  - raw, si, sixdof CSV, console, generated runscript, plots, detailed ploting 산출물이 생성됨
- 최근 변경 파일:
  - scripts/F450/runscript/1.1__test_f450_launch_run.xml
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 원본 Test_F450_Launch.xml를 수정하지 않고 workflow 내부 별도 1.1 runscript로 복사해 추적성을 유지
- 미완료 TODO:
  - TODO-20260721-1318-001: F450 raw output property 보강
- 남은 리스크:
  - workflow runner가 템플릿 output block을 자체 output으로 교체하므로 원본 quad_log.csv와 column 구성은 다름
  - raw CSV에 aileron command와 SCAS engage가 없어 roll doublet 입력값 직접 검증은 제한됨
- 권장 다음 작업:
  - F450 제어 입력 및 로터별 추력 분석이 필요하면 run_jsbsim_timestamped.py에 F450 전용 raw output property를 추가


## [2026-07-23 23:07] INDEX-20260723-2307-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-23 23:07 KST
- 최근 수행 과업:
  - C172 RKSS 14L full normal mission bundle 정적 검토
- 현재 상태:
  - 제공 5.9 runscript, c172ap_landing, c172x_4x75kg_cg_aligned_landing XML은 xmllint 기준 문법 유효
  - 현재 JSBSim aircraft tree에는 c172x_4x75kg_cg_aligned_landing이 없어 바로 workflow 실행 가능한 상태는 아님
  - bundle은 기존 5.8 정상 이륙을 확장해 loiter, recovery, final, flare, rollout, engine shutdown까지 구성한 초기 full mission안으로 판단됨
- 최근 변경 파일:
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 이번 단계에서는 제공 XML을 프로젝트에 설치하거나 수정하지 않고 정적 검토와 후속 TODO 기록만 수행
- 미완료 TODO:
  - TODO-20260723-2307-001: C172X 4x75kg landing full mission workflow 반영 및 실행 검증
  - TODO-20260721-1318-001: F450 raw output property 보강
- 남은 리스크:
  - 5.9의 excessive-bank abort는 현재 조건상 전 구간에서 작동할 수 있어 loiter/복귀 중 조기 종료 가능
  - final 진입 조건이 latitude 중심이라 runway centerline/cross-track 검증이 약함
  - mission-state 연속 CSV logging이 없어 실행 후 상태 전이 분석을 위해 output 보강이 필요
- 권장 다음 작업:
  - landing aircraft variant를 workflow와 JSBSim aircraft tree에 배치한 뒤, bank abort guard 및 full mission 검증용 output property를 보강하고 실제 5.9 실행으로 event sequence와 touchdown 품질을 확인


## [2026-07-23 23:30] INDEX-20260723-2330-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-23 23:30 KST
- 최근 수행 과업:
  - C172X 4x75kg RKSS 14L full normal mission landing variant 생성 및 실행 검증
- 현재 상태:
  - c172x_4x75kg_cg_aligned_landing aircraft가 workflow와 JSBSim install tree에 생성됨
  - scripts/c172x_4x75kg_cg_aligned_landing/runscript/5.9__rkss14l_full_normal_mission_run.xml가 workflow에서 실행 가능함
  - 첫 실행 5.9.1은 downwind base-turn 조건이 늦어 지면 접촉 종료됨
  - base-turn latitude를 37.3670으로 조정한 5.9.2는 684.916667 s에 STATE 23 mission complete 도달
- 최근 변경 파일:
  - aircraft_variants/c172x_4x75kg_cg_aligned_landing/
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_landing/
  - scripts/c172x_4x75kg_cg_aligned_landing/
  - scripts/run_jsbsim_timestamped.py
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 기존 c172x_4x75kg_cg_aligned를 직접 수정하지 않고 landing 전용 variant로 분리
  - landing output property는 aircraft 이름이 _landing일 때만 runner에서 추가
- 미완료 TODO:
  - TODO-20260723-2330-001: C172X 4x75kg full mission 착륙 품질 정량 평가 및 튜닝
  - TODO-20260721-1318-001: F450 raw output property 보강
- 남은 리스크:
  - mission complete는 확인됐지만 touchdown/rollout 품질은 추가 정량 평가 필요
  - gear/unit[0] 계열은 JSBSim catalog에서 unindexed gear/unit으로 노출되어 일부 skipped property가 남음
- 권장 다음 작업:
  - 5.9.2 CSV와 console을 기준으로 runway centerline 편차, touchdown 위치, flare sink-rate, gear contact chatter를 정량화한 뒤 필요 시 STATE 16-20 제어값 튜닝


## [2026-07-23 23:43] INDEX-20260723-2343-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-23 23:43 KST
- 최근 수행 과업:
  - FlightGear y/n 선택 프롬프트 없는 JSBSim runner 별도 생성
- 현재 상태:
  - scripts/run_jsbsim_timestamped_no_fg_prompt.py가 생성됨
  - 기본 실행에서는 FlightGear prompt 없이 FlightGear stream disabled로 진행됨
  - --flightgear 옵션을 명시하면 기존처럼 FlightGear 연동 실행 가능
- 최근 변경 파일:
  - scripts/run_jsbsim_timestamped_no_fg_prompt.py
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 원본 runner는 유지하고 테스트 편의용 별도 runner를 생성
- 미완료 TODO:
  - TODO-20260723-2330-001: C172X 4x75kg full mission 착륙 품질 정량 평가 및 튜닝
  - TODO-20260721-1318-001: F450 raw output property 보강
- 남은 리스크:
  - 새 runner는 FlightGear 선택만 생략하며 aircraft/init/runscript 선택은 그대로 유지
- 권장 다음 작업:
  - 반복 테스트 시 python3 scripts/run_jsbsim_timestamped_no_fg_prompt.py를 사용


## [2026-07-24 11:50] INDEX-20260724-1150-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-24 11:50 KST
- 최근 수행 과업:
  - C172X 4x75kg full mission 최신 로그의 활주로 도착 위치 확인
- 현재 상태:
  - 5.9.3은 STATE 23 mission complete까지 도달했지만 시작 RWY 14L 축 기준 약 -696.6 m cross-track offset에서 정지함
  - touchdown STATE 19 시점도 cross-track 약 -677.3 m로 활주로 축에서 벗어나 있음
  - 사용자가 지적한 것처럼 현재 미션은 시작한 활주로 쪽으로 정확히 복귀하지 않음
- 최근 변경 파일:
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 이번 단계는 로그 검증만 수행하고 runscript 수정은 하지 않음
- 미완료 TODO:
  - TODO-20260724-1150-001: C172X 4x75kg full mission을 RWY 14L 중심선/시작 활주로 쪽으로 복귀하도록 경로 조건 재설계
  - TODO-20260723-2330-001: C172X 4x75kg full mission 착륙 품질 정량 평가 및 튜닝
- 남은 리스크:
  - 현재 final/recovery 조건은 latitude 및 heading 중심이라 runway centerline capture를 보장하지 않음
- 권장 다음 작업:
  - STATE 12-15를 runway-axis along/cross-track 기준으로 재설계하고 touchdown cross-track 기준을 세워 5.9.4로 재검증


## [2026-07-24 12:55] INDEX-20260724-1255-001 - latest snapshot

- Project: `jsbsim_workflow`
- Recent work: created and tuned `5.10__rkss14l_runway_axis_return_landing_run.xml` for RKSS 14L runway-axis return.
- Current state: `5.10.8__rkss14l_runway_axis_return_landing` reached `STATE 23`.
- Key result: touchdown along `1200.9 m`, cross `-62.4 m`; final stop along `1554.1 m`, cross `-73.6 m`.
- Changed files: landing aircraft XML, JSBSim installed landing aircraft XML, `run_jsbsim_timestamped.py`, `run_jsbsim_timestamped_no_fg_prompt.py`, and new `5.10` runscript.
- Main decision: use runway-axis along/cross properties and `180 deg` intercept before `135.01 deg` runway alignment.
- Open risk: not yet precise enough for runway-width-grade centerline landing.
- Recommended next step: add cross-track feedback/localizer-like heading correction and retune to `+/-20 m` touchdown cross-track.


## [2026-07-24 15:00] INDEX-20260724-1500-001 - latest snapshot

- Project: `jsbsim_workflow`
- Recent work: added circular-loiter C172 RKSS 14L mission variant `5.11__rkss14l_circular_loiter_return_landing_run.xml`.
- Current state: `5.11.2__rkss14l_circular_loiter_return_landing` reached `STATE 23`.
- Key result: circular loiter duration `60.5 s`, average bank `-25.5 deg`; touchdown cross `-54.6 m`, final stop cross `-57.8 m`.
- Changed files: landing aircraft XML, installed JSBSim landing aircraft XML, `run_jsbsim_timestamped.py`, `run_jsbsim_timestamped_no_fg_prompt.py`, and new `5.11` runscript.
- Open risk: orbit is smooth AP heading-arc, not exact constant-radius orbit.
- Recommended next step: add stable radius/bank feedback only if exact circular radius is required.


## [2026-07-24 20:10] INDEX-20260724-2010-001 - SNAPSHOT

- Project: `jsbsim_workflow`
- Recent task: Adapt provided KSFO 28R FlightGear-default init/runscript for the current C172 landing workflow aircraft and run validation.
- Current state: Final KSFO scenario `5.16.1__ksfo28r_runway_return_circular_landing` completed `STATE 23` with no-FG runner.
- Recent changed files: `aircraft_variants/c172x_4x75kg_cg_aligned_ksfo28r_landing/`; `/home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_ksfo28r_landing/`; `scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/`.
- Main result: touchdown along `1708.3 m`, cross `-33.4 m`; final stop along `2022.5 m`, cross `-43.5 m`; circular loiter duration `60.6 s`, average bank `-25.4 deg`.
- Main decision: Use a KSFO-specific aircraft variant with 298 deg runway-axis monitor and final `5.16` rotated/tuned from the validated RKSS `5.11` flow.
- Open TODO: FlightGear visual/scenery alignment remains unverified.
- Remaining risk: Exact real-world KSFO runway markings/scenery may differ from the JSBSim start-axis coordinate metric.
- Recommended next step: Use `5.16__ksfo28r_runway_return_circular_landing_run.xml` as the KSFO baseline; run FlightGear visual validation if required.


## [2026-07-24 21:35] INDEX-20260724-2135-001 - SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 최근 수행 과업: plotting 저장을 제거한 CSV-only JSBSim runner 생성.
- 현재 상태: `scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py` 생성 및 KSFO 5.16 실행 검증 완료.
- 최근 변경 파일: `scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py`; `docs/agent-log/TASK.md`; `docs/agent-log/PROGRESS.md`; `docs/agent-log/DECISIONS.md`; `docs/agent-log/TODO.md`; `docs/agent-log/INDEX.md`.
- 주요 결정: 기존 runner를 수정하지 않고 별도 CSV-only runner를 추가.
- 미완료 TODO: CSV-only runner 내부 미사용 plotting 함수 제거는 deferred.
- 남은 리스크: runner 로직 중복으로 장기 유지보수 비용이 생길 수 있음.
- 권장 다음 작업: 빠른 반복 테스트에는 CSV-only runner 사용, 시각 자료가 필요할 때만 기존 plotting runner 사용.

## [2026-07-25 14:44] INDEX-20260725-1444-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-25 14:44 KST
- 최근 수행 과업:
  - Downloads의 LiftCruise2kg_JSBSim 초기 모델을 검토하고 workflow 실행 가능 상태로 반영
- 현재 상태:
  - LiftCruise2kg aircraft가 workflow와 JSBSim install tree에 추가됨
  - 원본 그대로는 aircraft/engine lookup 및 Aero.xml tableData 문제로 실행 불가였으나, workflow copy는 XML/catalog/runner 실행 통과
  - CSV-only runner run 1.0.1__hover_mission 완료 및 CSV 4종 생성
- 최근 변경 파일:
  - ircraft_variants/LiftCruise2kg/
  - scripts/LiftCruise2kg/initial_condition/1.0__ground_init.xml
  - scripts/LiftCruise2kg/runscript/1.0__hover_mission_run.xml
  - /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 원본 Downloads 폴더를 직접 수정하지 않고 workflow copy와 JSBSim install copy를 생성
  - JSBSim 1.2.4 호환을 위해 dm_config version 2.0 및 1D 	ableData 2열 행 형식 적용
- 미완료 TODO:
  - TODO-20260725-1444-001: LiftCruise2kg hover mission 제어 품질 튜닝 및 전용 output 보강
  - 기존 C172/F450 관련 OPEN/DEFERRED TODO 유지
- 남은 리스크:
  - 현재 1.0.1__hover_mission은 실행 완료되지만 최종 원점 오차가 약 38 m로 mission 의도 대비 큼
  - FlightGear visual 확인 및 pusher/fixed-wing transition 검증은 미수행
- 권장 다음 작업:
  - LiftCruise 전용 raw output property를 runner에 조건부 추가한 뒤 LiftCruiseAP.xml gain/sign을 튜닝해 원점 복귀 오차를 먼저 줄일 것

## [2026-07-25 14:48] CORRECTION-20260725-1448-001 — 정정

- 대상 기록:
  - INDEX-20260725-1444-001
- 정정 이유:
  - PowerShell 백틱 이스케이프 처리로 일부 inline-code 표기가 제어문자로 표시될 수 있어, 최신 상태 스냅샷을 plain text로 재기록함
- 정정 내용:
  - 프로젝트명: jsbsim_workflow
  - 최근 수행 과업: Downloads의 LiftCruise2kg_JSBSim 초기 모델 검토 및 workflow 실행 가능 상태 반영
  - 현재 상태: LiftCruise2kg aircraft가 workflow와 JSBSim install tree에 추가됐고, XML/catalog/CSV-only runner 실행을 통과했다.
  - 최근 변경 파일: aircraft_variants/LiftCruise2kg, scripts/LiftCruise2kg, /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/TODO.md, docs/agent-log/INDEX.md
  - 주요 결정: 원본 Downloads 폴더는 보존하고 workflow copy 및 JSBSim install copy를 생성했다. JSBSim 1.2.4 호환을 위해 fdm_config version 2.0 및 Aero.xml 1D tableData 2열 행 형식을 적용했다.
  - 미완료 TODO: TODO-20260725-1444-001 LiftCruise2kg hover mission 제어 품질 튜닝 및 전용 output 보강
  - 남은 리스크: 1.0.1__hover_mission은 실행 완료되지만 최종 원점 오차가 약 38 m로 mission 의도 대비 크다. FlightGear visual 확인 및 pusher/fixed-wing transition 검증은 미수행이다.
  - 권장 다음 작업: LiftCruise 전용 raw output property를 runner에 조건부 추가한 뒤 LiftCruiseAP.xml gain/sign을 튜닝해 원점 복귀 오차를 줄인다.
- 영향 범위:
  - 기록 가독성 정정만 해당하며 실제 코드/XML/실행 결과 변경 없음
- 검증 결과:
  - 정정 기록을 append-only 방식으로 추가함
- 다음 작업:
  - TODO-20260725-1444-001 수행

## [2026-07-25 15:09] INDEX-20260725-1509-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-25 15:09 KST
- 최근 수행 과업:
  - LiftCruise2kg 사용자 지정 10 m 박스 이동 및 수직착륙 runscript 추가
- 현재 상태:
  - scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml 추가됨
  - CSV-only runner run 1.1.1__ten_meter_box_hover_land 실행 완료
  - setpoint 시퀀스와 종료 이벤트는 동작하지만 실제 위치 추종은 크게 드리프트함
- 최근 변경 파일:
  - scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 기존 1.0 runscript를 덮어쓰지 않고 새 1.1 runscript로 추가
- 미완료 TODO:
  - TODO-20260725-1509-001: LiftCruise2kg 1.1 10 m 박스 mission 위치 추종 개선
  - TODO-20260725-1444-001: LiftCruise2kg hover mission 제어 품질 튜닝 및 전용 output 보강
- 남은 리스크:
  - 최종 위치가 local_N/local_E 약 -203.45 m / -177.35 m로 요청 좌표와 크게 다름
  - FlightGear visual 확인은 미수행
- 권장 다음 작업:
  - LiftCruise 전용 output 보강 후 LiftCruiseAP.xml의 좌표계 sign/gain을 먼저 튜닝

## [2026-07-25 15:18] INDEX-20260725-1518-001 — 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-25 15:18 KST
- 최근 수행 과업:
  - 첨부된 LiftCruise2kg 1.1 runscript 및 로그 분석 문서 검토
- 현재 상태:
  - 첨부 문서의 핵심 진단은 대체로 실제 XML/로그와 일치
  - heading wrap 누락과 heading zero assumption 위치 제어가 주요 고장 원인이라는 판단은 타당
  - raw CSV 출력 부족은 workflow runner가 template output block을 교체하기 때문에 발생한 것으로 확인
- 최근 변경 파일:
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/INDEX.md
- 주요 결정:
  - 이번 단계는 검토만 수행하고 코드/XML 수정은 하지 않음
- 미완료 TODO:
  - TODO-20260725-1509-001: LiftCruise2kg 1.1 10 m 박스 mission 위치 추종 개선
- 남은 리스크:
  - fcs/fw-* 및 모터별 indexed output을 기록하지 않으면 다음 튜닝 진단이 제한됨
- 권장 다음 작업:
  - LiftCruise 전용 raw output property를 runner에 조건부 추가한 뒤 heading wrap 및 좌표계 변환 수정

## [2026-07-25 16:12] INDEX-20260725-1612-001 - SNAPSHOT
- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: LiftCruise2kg 1.1 XML output과 raw CSV 헤더 1:1 대응 검증
- 현재 상태: runner 3개는 LiftCruise2kg 템플릿 output을 보존하고, 1.1.4 실행에서 CSV 대응 검증 완료
- 최근 변경 파일: scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py, scripts/run_jsbsim_timestamped_no_fg_prompt.py, scripts/run_jsbsim_timestamped.py, scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
- 주요 결정: mission-state는 CSV output에서 제외하고 console notify로 확인
- 미완료 TODO: mission-state CSV 직접 기록 방법 검토, LiftCruise 위치 추종 drift 튜닝
- 권장 다음 작업: AP position hold sign/gain 튜닝 후 1.1 hover 구간별 위치 오차 분석

## [2026-07-25 17:56] INDEX-20260725-1756-001 - 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-07-25 17:56 KST
- 최근 수행 과업: F450 autopilot bridge 추가 및 LiftCruise2kg 1.1과 유사한 10 m box hover/land mission 실행 검증
- 현재 상태: F450AP.xml 추가, F450.xml autopilot include 추가, F450 heading-zero init 추가, F450 1.2 runscript 추가, runner 3개 F450 전용 raw output 보강, CSV-only run 1.2.9 정상 종료
- 최근 변경 파일: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml, /home/junyeopkwon/jsbsim/aircraft/F450/F450.xml, scripts/F450/initial_condition/1.1__ground_park_heading0_init.xml, scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml, scripts/run_jsbsim_timestamped.py, scripts/run_jsbsim_timestamped_no_fg_prompt.py, scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/TODO.md, docs/agent-log/INDEX.md
- 주요 결정: F450 기존 FlightControl.xml은 유지하고 F450AP.xml에서 FCS 입력으로 command를 bridge함. heading-zero initial condition을 추가함. disarm 후 contact chatter 회피를 위해 terminate를 205.2 s로 앞당김.
- 미완료 TODO: TODO-20260725-1756-001 F450 10 m box hover/land lateral position hold 튜닝, 기존 LiftCruise drift tuning TODO 유지
- 남은 리스크: F450 AP 기능 연결과 altitude hold는 확인됐지만 lateral tracking은 큼. run 1.2.9 종료 직전 horizontal error는 약 59.06 m. FlightGear visual 검증은 미수행.
- 권장 다음 작업: F450AP.xml lateral outer-loop를 F450 rate-SCAS 입력에 맞게 재설계하고 hover segment별 error 자동 평가를 추가

## [2026-07-26 14:10] INDEX-20260726-1410-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-07-26 14:10 KST
- 최근 수행 과업: F450 10 m box hover-land runscript와 로그 property 검토/수정
- 현재 상태: 로그 property 오류와 시간 전환 문제는 보정됨. F450은 첫 hover 위치/속도 gate를 만족하지 못해 10 m leg로 진행하지 않음
- 최근 변경 파일: /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 주요 결정: JSBSim catalog 기준으로 0번 motor/engine 출력은 [0]이 아니라 base property를 사용하고, mission 전환은 nominal time 하한과 도착 gate를 결합함
- 미완료 TODO: TODO-20260726-1410-001 F450AP와 FlightControl 중첩 제어/gain 문제 분리 진단
- 남은 리스크: gate 조건을 만족하지 못하는 원인은 센서 stub보다 F450AP/FlightControl 제어 구조, gain, saturation, 축 부호 문제일 가능성이 큼
- 권장 다음 작업: F450AP lateral position loop, attitude command scaling, FlightControl rate PID, mixer saturation 순서로 로그 기반 튜닝 진행

## [2026-07-26 14:45] INDEX-20260726-1445-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-07-26 14:45 KST
- 최근 수행 과업: 시작점을 (0,0)으로 하는 XY trajectory plot 추가
- 현재 상태: plotting runner는 3D trajectory 외에 고도 제외 XY trajectory PNG를 생성함
- 최근 변경 파일: /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 주요 결정: XY plot은 x=East from start, y=North from start로 표시하고 첫 row를 원점으로 재정렬함
- 미완료 TODO: F450AP와 FlightControl 중첩 제어/gain 문제 분리 진단은 계속 OPEN
- 남은 리스크: view_image 직접 렌더 검증은 WSL sandbox helper 오류로 수행하지 못함
- 권장 다음 작업: F450 제어기 튜닝 후 run별 XY plot을 비교해 수평면 추종 개선 여부 확인

## [2026-07-26 14:59] INDEX-20260726-1459-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-07-26 14:59 KST
- 최근 수행 과업: F450 1.2 runscript 이론 XY setpoint 경로 그래프 생성
- 현재 상태: ideal setpoint XY PNG가 생성되어 실제 trajectory plot과 비교 가능
- 최근 변경 파일: /home/junyeopkwon/jsbsim_workflow/plots/F450/1.2__ten_meter_box_hover_land/ideal_setpoint_xy_1.2__ten_meter_box_hover_land.png
- 주요 결정: xy 축은 runscript 설명에 맞춰 x=North setpoint, y=East setpoint로 표기
- 미완료 TODO: 실제 궤적과 이론 궤적 overlay plot은 후속 개선 가능
- 남은 리스크: 이름은 box mission이지만 실제 setpoint sequence는 십자형 왕복 경로임
- 권장 다음 작업: ideal XY와 실제 XY를 overlay하여 F450 lateral tracking 오차를 정량/시각 비교


## [2026-07-26 15:33] INDEX-20260726-1533-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow / F450 JSBSim autopilot validation
- 기록 시각: 2026-07-26 15:33 KST
- 최근 수행 과업: F450 10 m hover mission 궤적 불량 원인 분석 및 순차 수정
- 현재 상태: heading wrap, lateral gain 축소, signed local N/E 위치오차 적용 후 1.2 10 m 미션이 의도한 XY 경로를 재현함.
- 최근 변경 파일: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.3__hover_origin_diagnostic_run.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.4__attitude_axis_diagnostic_run.xml, /home/junyeopkwon/jsbsim_workflow/plots/F450/1.2__ten_meter_box_hover_land/1.2.19__ten_meter_box_hover_land_actual_vs_ideal_xy_07261531.png
- 주요 결정: JSBSim position/distance-from-start-lat/lon-mt를 AP 위치 feedback으로 쓰지 않고 초기 위경도 기준 signed local north/east를 사용한다.
- 미완료 TODO: home 좌표 자동 주입 일반화, F450 제어기/actuator 동특성 튜닝
- 남은 리스크: 현재 local 변환은 특정 초기 위치와 10 m급 소거리 미션에 맞춘 근사다.
- 권장 다음 작업: F450AP home 좌표를 runscript/init와 동기화하고, 최신 actual-vs-ideal XY 플롯을 기준 산출물로 문서화한다.


## [2026-07-26 16:46] INDEX-20260726-1646-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow / LiftCruise2kg JSBSim autopilot validation
- 기록 시각: 2026-07-26 16:46 KST
- 최근 수행 과업: F450에서 검증한 10 m hover mission 수정 방식을 LiftCruise2kg에 적용하고 CSV-only 실행 검증
- 현재 상태: LiftCruise2kg 1.1 미션은 signed local N/E, yaw wrap, arrival gate 적용 후 정상적으로 10 m cross-shaped XY 경로를 통과한다.
- 최근 변경 파일: /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/LiftCruiseAP.xml, /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml, /home/junyeopkwon/jsbsim_workflow/plots/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.9__ten_meter_box_hover_land_actual_vs_ideal_xy_07261645.png
- 주요 결정: LiftCruise2kg init latitude 체계에 맞춰 AP local north feedback은 position/lat-gc-deg 기준으로 계산한다.
- 미완료 TODO: home 좌표와 latitude type 자동 동기화, 더 긴 거리용 local tangent plane 변환, actuator/motor 동특성 튜닝
- 남은 리스크: 현재 control은 hover mission 기능 검증에는 충분하지만 물리 모델 실제성까지 검증한 것은 아니다.
- 권장 다음 작업: F450/LiftCruise 공통으로 home 좌표 주입 방식을 정리하고, plotting runner에서도 최신 LiftCruise XY 플롯을 자동 생성하게 한다.

## [2026-07-29 10:54] INDEX-20260729-1054-001 - 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-29 10:54 KST
- 최근 수행 과업:
  - c172x 4x75kg zero-propulsion no-alpha-limit RKSS14L 500 m MSL neutral drop mission 생성 및 CSV-only 실행
- 현재 상태:
  - 새 aircraft c172x_4x75kg_cg_aligned_zeroprop_noalphalimit가 workflow와 /home/junyeopkwon/jsbsim/aircraft 양쪽에 생성됨
  - 새 초기조건과 runscript가 scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit 아래에 생성됨
  - run 7.0.2가 219.766667 s에서 nose gear ground contact로 정상 종료됨
- 최근 변경 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.0__rkss14l_500m_ubody60_theta25_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_run.xml
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정:
  - 기존 zeroprop 변형을 직접 수정하지 않고 no-alpha-limit 별도 variant로 분리
  - elevation 38 ft를 유지하면서 h-sl 500 m MSL을 맞추기 위해 초기 altitude는 488.4176 m로 설정
  - elevator actuator bias를 0.0으로 설정해 neutral surface deflection을 0 rad로 맞춤
- 미완료 TODO:
  - TODO-20260729-1054-001 c172x alpha-limit baseline과 no-alpha-limit 결과 비교
- 남은 리스크:
  - FlightGear visual 확인은 미수행
  - alpha-limit 제거 효과는 baseline 비교 전까지 정량 분리되지 않음
  - 공력 table extrapolation 물리 타당성은 별도 검토 필요
- 권장 다음 작업:
  - 같은 초기조건으로 기존 c172x_4x75kg_cg_aligned_zeroprop baseline을 실행하고 7.0.2 결과와 비교

## [2026-07-29 11:08] INDEX-20260729-1108-001 - 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-29 11:08 KST
- 최근 수행 과업:
  - c172x no-alpha-limit drop 고도 상승/출렁임 원인 분석
- 현재 상태:
  - run 7.0.3 고도 상승은 PID 문제가 아니라 AP off, 조종면 0 상태의 자유응답으로 확인됨
  - 초기 theta 2.5 deg + wbody 0이 상승 경로를 만들고, aircraft pitch moment Cmo 0.1이 nose-up을 유발함
- 최근 변경 파일:
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정:
  - 이번 단계는 원인 분석만 수행하고 모델/초기조건은 수정하지 않음
- 미완료 TODO:
  - TODO-20260729-1108-001 c172x no-thrust fixed-control 초기조건 재정의 및 비교 run
  - TODO-20260729-1054-001 c172x alpha-limit baseline과 no-alpha-limit 결과 비교
- 남은 리스크:
  - 사용자가 원하는 조건이 수평 진입인지, 자세 고정 시작인지, trim된 활공인지에 따라 다음 run의 초기조건이 달라짐
- 권장 다음 작업:
  - theta 2.5 deg 유지 상태에서 gamma 0이 되도록 wbody를 약 +2.62 m/s로 설정한 비교 run과 theta 0 deg 비교 run을 생성

## [2026-07-29 11:20] INDEX-20260729-1120-001 - 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-29 11:20 KST
- 최근 수행 과업:
  - c172x no-alpha-limit 7.1 수평 전진 초기조건 생성 및 7.0/7.1 고도 그래프 비교
- 현재 상태:
  - 7.1 theta 0 deg, ubody 60 m/s, wbody 0 run이 생성되고 CSV-only 실행 완료
  - 초기 vertical velocity는 제거됐지만 hmax 637.64 m까지 상승해 neutral pitch moment가 지배 원인임을 확인
- 최근 변경 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.1__rkss14l_500m_ubody60_level_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop_run.xml
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop/altitude_compare_7_0_vs_7_1.png
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop/states_h_vdown_theta_alpha_7_1.png
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정:
  - 수평 전진 비교를 위해 theta 0 deg 케이스를 우선 생성
- 미완료 TODO:
  - TODO-20260729-1120-001 c172x no-thrust neutral 조건의 pitch-up moment 제거 또는 trim 활공 조건 산출
- 남은 리스크:
  - plotting runner가 멈춰 최종 검증은 CSV-only와 별도 matplotlib PNG 생성으로 수행
  - view_image 직접 렌더 확인은 sandbox 오류로 불가
- 권장 다음 작업:
  - Cmo/elevator trim/alpha-theta 조합을 탐색해 no-thrust fixed-control steady glide 초기조건 생성

## [2026-07-29 11:25] INDEX-20260729-1125-001 - 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-29 11:25 KST
- 최근 수행 과업:
  - c172x no-alpha-limit theta -5 deg nose-down run 생성 및 7.0/7.1/7.2 고도 비교
- 현재 상태:
  - 7.2 theta -5 deg run은 실행 완료됐고, hmax 633.31 m로 7.1 대비 상승 피크가 약간 감소함
  - 초기 pitch-up moment와 qdot은 여전히 커서 nose-down만으로 문제를 제거하지 못함
- 최근 변경 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.2__rkss14l_500m_ubody60_thetam5_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.2__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop_run.xml
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.2__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop/altitude_compare_7_0_7_1_7_2.png
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.2__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop/states_h_vdown_theta_alpha_7_2.png
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정:
  - 기존 7.1을 수정하지 않고 7.2를 별도 비교 케이스로 추가
- 미완료 TODO:
  - TODO-20260729-1125-001 c172x no-alpha-limit neutral pitch moment 보정 실험
- 남은 리스크:
  - theta 조정만으로는 neutral pitch moment를 제거하지 못함
- 권장 다음 작업:
  - elevator trim 또는 Cmo 조정 별도 variant로 초기 qdot과 고도 피크를 줄이는 실험 수행

## [2026-07-29 11:42] INDEX-20260729-1142-001 - 최신 상태 스냅샷

- 프로젝트명:
  - jsbsim_workflow
- 기록 시각:
  - 2026-07-29 11:42 KST
- 최근 수행 과업:
  - c172x no-alpha-limit 초기 qdot 0 근접 Cmo 보정 variant 계산 및 실행
- 현재 상태:
  - Cmo=-0.01523148을 적용한 cmotrimq0 variant의 8.1 run에서 초기 qdot이 -1.13e-7 rad/s^2로 사실상 0이 됨
  - 8.1은 조종면 0 rad를 유지하면서 초기 고도 상승 없이 바로 하강함
- 최근 변경 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/8.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmotrimq0_drop
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정:
  - 조종면 0 조건을 유지하기 위해 elevator trim이 아니라 별도 Cmo 보정 variant로 qdot0를 맞춤
- 미완료 TODO:
  - TODO-20260729-1142-001 elevator trim 기반 qdot0 run과 Cmo 보정 run 비교
- 남은 리스크:
  - Cmo 보정은 실험용이며 실제 C172 공력 보정값으로 확정하지 않음
- 권장 다음 작업:
  - 원래 Cmo=0.1 모델에서 elevator trim으로 qdot0를 만드는 run을 추가해 물리적 trim 방식과 비교

## [2026-07-29 12:05] INDEX-20260729-1205-001 - 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: c172x no-thrust/no-alpha-limit trim-fixed 추락 시작 케이스 생성
- 현재 상태: native full trim은 no-thrust 조건에서 실패했고, elevator fixed trim 9.3은 초기 qdot을 8.55886e-05 rad/s^2까지 낮춰 고도 상승 피크를 제거함
- 최근 변경 파일: aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_elevtrimq0; scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_elevtrimq0; plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_elevtrimq0/9.3__rkss14l_500m_ubody60_level_fixed_elevtrimq0_final_noalphalimit_drop
- 주요 결정: Cmo 보정 대신 elevator actuator bias를 trim 고정 조종면으로 사용
- 미완료 TODO: TODO-20260729-1205-001 no-thrust steady glide full trim 산출
- 남은 리스크: 9.3은 full glide equilibrium이 아니라 초기 qdot 제거 중심 trim임
- 권장 다음 작업: 필요 시 alpha/theta/gamma/elevator 동시 최적화로 no-thrust glide trim 조건 산출


## [2026-07-31 10:56] INDEX-20260731-1056-001 - SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 최근 수행 과업: KSFO 28R `5.16`의 runway centerline 이탈 및 조작 튐 현상 분석/개선.
- 현재 상태: 최종 추천 runscript `5.22__ksfo28r_centerline_balanced_final_landing_run.xml` 생성 및 CSV-only JSBSim 검증 완료.
- 최근 변경 파일: `scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.17__ksfo28r_centerline_smoothed_landing_run.xml`; `5.18__ksfo28r_centerline_smoother_takeoff_landing_run.xml`; `5.19__ksfo28r_centerline_smoothest_takeoff_landing_run.xml`; `5.20__ksfo28r_centerline_corrected_takeoff_landing_run.xml`; `5.21__ksfo28r_centerline_balanced_takeoff_landing_run.xml`; `5.22__ksfo28r_centerline_balanced_final_landing_run.xml`.
- 주요 결과: `5.16.5` 대비 `5.22.1`의 초기 150 s 최대 cross `91.2 m -> 44.0 m`, touchdown cross `-33.4 m -> -1.5 m`, stop cross `-43.5 m -> -2.3 m`.
- 주요 결정: 기존 `5.16`은 baseline으로 보존하고 `5.22`를 개선본으로 사용.
- 미완료 TODO: FlightGear visual validation.
- 남은 리스크: JSBSim metric과 FlightGear 시각 체감이 완전히 같지는 않을 수 있음.
- 권장 다음 작업: FlightGear 연동 테스트에는 `5.22`를 우선 사용.

## [2026-07-31 13:55] INDEX-20260731-1355-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 최근 수행 과업: KSFO RWY 28R C172 미션 로테이트 직후 elevator/AP 튐 완화
- 현재 상태: `5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml`을 추천 실행본으로 선정. 기존 `5.22`는 보존됨
- 최근 변경 파일: `5.26__ksfo28r_smooth_manual_pitch_ap_landing_run.xml`, `5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml`, `5.28__ksfo28r_smooth_rotate_late_alt_hold_landing_run.xml`, `5.29__ksfo28r_staged_altitude_ap_landing_run.xml`, `5.30__ksfo28r_manual_climb_damped_landing_run.xml`
- 주요 결정: 즉시 altitude hold 대신 약한 로테이트 입력과 지연 AP handoff를 적용한 `5.27`이 초반 튐/착륙 중심선 균형이 가장 좋음
- 미완료 TODO: `5.27`의 46초 AP 재투입 transient 완화 및 FlightGear 화면 확인
- 남은 리스크: GUI 화면 체감 검증 미실시, `5.28`-`5.30`은 실험 파일로 남아 있으나 추천본은 아님
- 권장 다음 작업: FlightGear에서 `5.27` 실행 후 0-100초 elevator/theta 및 외부 시점 확인

## [2026-07-31 14:05] INDEX-20260731-1405-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 최근 수행 과업: 비교용 `5.26`, `5.28`, `5.29`, `5.30` runscript 및 실행 로그 삭제
- 현재 상태: KSFO RWY 28R 로테이트 튐 완화 추천본은 `5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml` 하나만 유지
- 최근 변경 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml` 보존, 비추천 비교본 삭제
- 남은 리스크: `5.27`의 FlightGear 화면 확인은 아직 필요
- 권장 다음 작업: FlightGear에서 `5.27` 실행 확인

## [2026-07-31 14:18] INDEX-20260731-1418-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: F450 raw CSV distance-from-start property 의미 확인
- 현재 상태: lat-mt와 lon-mt는 시작점 기준 축방향 상대거리 성분이며 전체 스칼라 거리는 mag-mt로 확인됨
- 최근 변경 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 주요 결정: 코드 변경 없음
- 남은 리스크: 부호 있는 North/East 변위가 필요하면 from-start-neu-n-ft 및 from-start-neu-e-ft를 써야 함
- 권장 다음 작업: 이동 궤적 평면 분석에는 mag-mt 또는 NEU 변위를 목적에 맞게 선택

## [2026-07-31 14:24] INDEX-20260731-1424-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: workflow Excel과 F450 CSV에서 from-start-neu-n-ft 존재 여부 확인
- 현재 상태: workflow Excel 및 F450 raw CSV에는 해당 property가 없고, 대응 sixdof_raw/sixdof_si에는 존재함
- 최근 변경 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 주요 결정: 코드 및 Excel 수정 없음
- 남은 리스크: property 단위 분석은 workflow Excel 요약이 아니라 raw 또는 sixdof CSV header를 직접 기준으로 해야 함
- 권장 다음 작업: 시작점 기준 North/East 변위 분석은 sixdof_si의 from_start_neu_n_m, from_start_neu_e_m 사용

## [2026-07-31 15:56] INDEX-20260731-1556-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: plotting 없이 모든 주요 property를 단일 CSV로 출력하는 runner 추가
- 현재 상태: scripts/run_jsbsim_timestamped_combined_csv_only.py 추가 및 F450 1.0 ground launch 검증 완료
- 최근 변경 파일: scripts/run_jsbsim_timestamped_combined_csv_only.py, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/INDEX.md
- 주요 결정: 기존 runner를 수정하지 않고 combined_csv_only runner를 별도 파일로 추가
- 미완료 TODO: 신규 TODO 없음
- 남은 리스크: combined CSV는 raw property 단위이며 SI 변환 컬럼은 포함하지 않음; Excel 자동 갱신은 기본 생략
- 권장 다음 작업: 사용하려는 실제 F450 1.2 ten_meter_box_hover_land runscript를 새 runner로 실행해 external plot 도구 입력 CSV로 사용

## [2026-07-31 16:08] INDEX-20260731-1608-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: MATLAB CSV plotter v6 검토 및 개선 기능 도출
- 현재 상태: plotter는 수동 2D/3D 분석 GUI로 유용하나 발표자료 자동 생산에는 preset, batch export, summary, comparison 기능이 필요함
- 최근 변경 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 주요 결정: 코드 변경 없이 검토 결과만 기록
- 남은 리스크: Min/Max 옵션의 mark2DMinMaxOnly 누락 가능성, MATLAB 직접 실행 미검증
- 권장 다음 작업: 우선 mark2DMinMaxOnly 보완 후 standard plot preset 및 batch export 기능 추가

## [2026-07-31 17:23] INDEX-20260731-1723-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: 2026-07-31 17:23 KST
- 최근 수행 과업: MATLAB CSV plotter v7 구성
- 현재 상태: `run_jsbsim_csv_plotter_v7.m`가 생성되어 표준 분석 PNG 패키지와 summary metrics CSV export 기능을 포함함. v6는 보존됨.
- 최근 변경 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`, `docs/agent-log/TASK.md`, `docs/agent-log/PROGRESS.md`, `docs/agent-log/DECISIONS.md`, `docs/agent-log/TODO.md`, `docs/agent-log/INDEX.md`
- 주요 결정: v6 직접 수정 대신 v7 새 파일로 기능 확장
- 미완료 TODO: MATLAB GUI 환경에서 v7 실기동 및 export 산출물 검증
- 남은 리스크: `logs/`가 `.gitignore`에 포함되어 v7 파일이 Git status에 표시되지 않음. MATLAB 런타임 검증은 미수행.
- 권장 다음 작업: MATLAB에서 F450 CSV를 열고 표준 분석 패키지를 export한 뒤 PNG와 `summary_metrics.csv`를 발표자료용으로 선별
## [2026-07-31 17:47] INDEX-20260731-1747-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: 2026-07-31 17:47 KST
- 최근 수행 과업: MATLAB CSV plotter v7 제목/축/범례 편집 기능 보강
- 현재 상태: `run_jsbsim_csv_plotter_v7.m`에서 제목/축/범례 글씨 크기 조절과 3D 범례 문구 수정이 가능함. 2D 범례 문구는 기존 `범례 이름` 컬럼을 사용함.
- 최근 변경 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`, `docs/agent-log/TASK.md`, `docs/agent-log/PROGRESS.md`, `docs/agent-log/TODO.md`, `docs/agent-log/INDEX.md`
- 주요 결정: 2D는 기존 series table의 `범례 이름` 컬럼을 유지하고, 3D는 별도 `legend3DTable`로 문구를 수정하는 방식 채택
- 미완료 TODO: MATLAB GUI 실사용 검증 및 PNG 시각 확인
- 남은 리스크: `logs/` ignored 파일이므로 v7은 Git status에 표시되지 않음. GUI runtime은 아직 직접 실행하지 않음.
- 권장 다음 작업: MATLAB에서 v7 실행 후 F450 CSV로 글씨 크기/범례 문구 변경과 PNG export를 확인
## [2026-07-31 18:02] INDEX-20260731-1802-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: 2026-07-31 18:02 KST
- 최근 수행 과업: MATLAB CSV plotter v7 2D 범례 직접 입력 기능 수정
- 현재 상태: `title2DTable`에 `범례 이름` 행이 추가되어 사용자가 쉼표 구분으로 입력한 문구가 2D 그래프 범례에 우선 적용됨
- 최근 변경 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`, `docs/agent-log/TASK.md`, `docs/agent-log/PROGRESS.md`, `docs/agent-log/TODO.md`, `docs/agent-log/INDEX.md`
- 주요 결정: 2D 범례 직접 입력은 제목/축 제목 테이블의 추가 행으로 처리하고, 선택된 Y 계열 순서대로 매핑
- 미완료 TODO: MATLAB GUI에서 실제 범례 표시와 PNG 결과 확인
- 남은 리스크: 입력한 범례 개수가 선택된 Y 계열보다 적으면 나머지는 fallback 이름 사용
- 권장 다음 작업: MATLAB에서 v7 실행 후 `범례 이름` 행에 원하는 발표용 이름을 입력하고 2D 그래프/PNG 결과 확인

## [2026-08-03 00:00] INDEX-20260803-0000-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 최근 수행 과업: JSBSim aircraft XML `location` 좌표계 기준 조사
- 현재 상태: 코드 변경 없음. structural frame 기준과 CG 기준 body 변환 관계 확인 완료
- 주요 결정: 모델 XML의 위치 좌표는 원칙적으로 structural frame 좌표로 해석하고, 동역학 계산에서는 CG를 뺀 뒤 body frame으로 변환됨
- 남은 리스크: 각 aircraft 모델의 structural 원점 물리 위치는 모델 파일/제작자 정의에 의존
- 권장 다음 작업: 특정 기체에서 모터/프롭/탑승객을 추가할 때는 기존 `CG`, landing gear, eyepoint 값을 기준으로 같은 structural 좌표계 안에서 상대 위치를 맞춤


## [2026-08-03 00:10] INDEX-20260803-0010-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 최근 수행 과업: C172 XML structural datum 원점 추정
- 현재 상태: 코드 변경 없음. C172 XML의 좌표 원점은 nose tip이 아니라 nose/firewall 근처 aircraft datum으로 추정
- 남은 리스크: Cessna manual의 datum 정의 원문 미확인
- 권장 다음 작업: 정확한 실기 기준점이 필요하면 C172P Information Manual의 weight and balance station datum을 대조

## [2026-08-10 11:20] INDEX-20260810-1120-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: MiniTalon XML 설명 문서를 XML 파일별 Markdown으로 분리
- 현재 상태: docs/minitalon_xml_reference 아래 27개 Markdown 파일 생성 완료. 00_INDEX.md에서 전체 목록을 제공하고, Metrics.xml.md 등 각 문서는 해당 XML 내용만 포함
- 최근 변경 파일: docs/minitalon_xml_reference/*.md, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 주요 결정: 기존 통합 문서 삭제는 승인 없이 수행하지 않고, 새 위치에 XML별 문서만 생성
- 미완료 TODO: 기존 통합 문서 삭제 여부 확인, 문서별 세부 문장 교정
- 남은 리스크: 일부 문서는 기존 통합 문서 섹션을 자동 분리한 것이므로 표현 교정 여지가 있음
- 권장 다음 작업: 사용자가 기존 통합 문서 제거를 명시하면 삭제하고, 필요 시 XML별 문서 문장 스타일을 통일
- 관련 기록: TASK-20260810-1120-001, PROGRESS-20260810-1120-001


## [2026-08-10 22:35] INDEX-20260810-2235-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-10 22:35 KST
- 최근 수행 과업: 첨부 DATCOM 공력/flight control을 적용한 F450_DATCOM 생성 및 원본 F450과 동일 attitude-mode 비교 실행
- 현재 상태: F450_DATCOM aircraft가 JSBSim catalog 로딩과 70초 attitude diagnostic 실행을 통과했다. 원본 F450과 파생 모델 모두 combined CSV 로그가 생성되었고, window별 비교 요약 CSV가 생성되었다.
- 최근 변경 파일: /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/*, ircraft_variants/F450_DATCOM/*, scripts/F450_DATCOM/initial_condition/1.0__ground_park_heading0_init.xml, scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml, docs/agent-log/*.md
- 주요 결정: 원본 F450은 수정하지 않고 파생 모델로 비교한다. F450 multicopter mixer/autopilot은 유지하고 DATCOM aerosurface scale 및 aerodynamic axes를 병합한다.
- 미완료 TODO: F450_DATCOM position-hold hover 전용 장시간 검증과 controller tuning 여부 판단
- 남은 리스크: DATCOM reference geometry와 F450 physical model의 일관성, JSBSim 호환을 위한 
ow+table to 
ow+column 테이블 재구성의 보간 의미
- 권장 다음 작업: 현재 attitude-mode 비교 로그로 공력 차이를 먼저 확인한 뒤, 필요하면 10 m position-hold hover 미션을 별도로 실행해 tuning을 진행
- 관련 기록: TASK-20260810-2235-001, PROGRESS-20260810-2235-001, DECISION-20260810-2235-001, TODO-20260810-2235-001


## [2026-08-10 22:40] CORRECTION-20260810-2240-001 — 정정

- 대상 기록: TASK-20260810-2235-001, PROGRESS-20260810-2235-001, DECISION-20260810-2235-001, TODO-20260810-2235-001, INDEX-20260810-2235-001
- 정정 이유: PowerShell command string에서 Markdown backtick escape가 적용되어 일부 경로와 row/table 표기가 제어문자로 기록됨
- 기존 내용: 일부 backtick-wrapped path 및 row+table, row+column 표기가 깨져 보임
- 정정 내용: 실제 변경 파일은 /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/initial_condition/1.0__ground_park_heading0_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml 이다. JSBSim 호환을 위해 DATCOM base table 6개는 row plus table 구조에서 row plus column 구조로 재구성했으며 숫자 데이터는 변경하지 않았다.
- 영향 범위: 작업 기록 문서 표기 정정만 해당. 모델 파일, runscript, CSV 로그에는 영향 없음
- 검증 결과: INDEX.md 최신 tail에서 정정 항목이 append됨
- 다음 작업: 최종 응답에서는 정정된 경로와 결과만 보고


## [2026-08-10 22:50] INDEX-20260810-2250-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-10 22:50 KST
- 최근 수행 과업: F450 vs F450_DATCOM attitude diagnostic 비교 그래프 생성
- 현재 상태: plots/F450_DATCOM_attitude_compare_08102235 아래 PNG 5개가 생성되어 고도, 자세, 속도, 공력 force/moment, DATCOM coefficient 비교가 가능함
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/plots/F450_DATCOM_attitude_compare_08102235/*.png, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 주요 결정: 직전 08102235 실행 CSV를 비교 기준으로 사용하고, 원본 F450에 없는 DATCOM coefficient는 F450_DATCOM 단독 그래프로 표시
- 미완료 TODO: view_image 도구 렌더 확인 실패로 실제 이미지 미리보기는 사용자 또는 외부 뷰어 확인 필요
- 남은 리스크: 그래프 생성은 정상이나 시각적 미세 조정은 필요 시 추가 가능
- 권장 다음 작업: overview 그래프에서 차이를 확인한 뒤, 필요하면 mode 3 position-hold hover 비교 그래프를 별도로 생성
- 관련 기록: TASK-20260810-2250-001, PROGRESS-20260810-2250-001


## [2026-08-10 23:00] INDEX-20260810-2300-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-10 23:00 KST
- 최근 수행 과업: F450_DATCOM 공력 적용 확인용 1~6번 검증 전체 실행 및 문서화
- 현재 상태: docs/F450_DATCOM_AERO_VALIDATION.md가 생성되었고, aero_validation_checks_08102253.csv의 60개 검증 항목이 모두 PASS임. propulsion-off free-response 비교 로그와 PNG가 추가됨.
- 최근 변경 파일: docs/F450_DATCOM_AERO_VALIDATION.md, scripts/F450_DATCOM/initial_condition/2.0__free_response_10ms_theta5_init.xml, scripts/F450_DATCOM/runscript/2.0__propulsion_off_free_response_run.xml, plots/F450_DATCOM_aero_validation_08102253/*.png, docs/agent-log/*.md
- 주요 결정: 공력 적용 검증은 hover 성공 여부가 아니라 property 존재, table 보존, qbar scaling, control sign, A/B dynamic response, propulsion-off separation의 6개 축으로 판단
- 미완료 TODO: position-hold hover 장시간 검증과 F450_DATCOM controller tuning 여부 판단
- 남은 리스크: DATCOM reference geometry와 F450 physical model의 물리 일관성, table 구조 재구성의 보간 의미
- 권장 다음 작업: docs/F450_DATCOM_AERO_VALIDATION.md를 기준으로 결과 검토 후, mode 3 hover wind/forward-speed 미션을 추가
- 관련 기록: TASK-20260810-2300-001, PROGRESS-20260810-2300-001

## [2026-08-11 16:45] INDEX-20260811-1645-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-11 16:45 KST
- 최근 수행 과업: AD3000 workflow variant 및 smoke runscript 구성
- 현재 상태: aircraft_variants/AD3000과 scripts/AD3000이 생성됨. 실제 JSBSim root에서 XML 검사, catalog load, 1.5초 run은 통과했으나 8초 hover는 FPE로 실패
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_generate_aircraft.py, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/AD3000/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/*.md
- 주요 결정: workflow에는 jsbsim root의 AD3000 aircraft를 미러해 비교/추적용 variant로 보관
- 미완료 TODO: TODO-20260811-1645-001 batch 편입 및 hover split 보정
- 남은 리스크: workflow Excel 미등록, 8초 hover FPE, PDF 상세 제원 미반영
- 권장 다음 작업: AD3000 front/rear collective split 보정 후 scripts/AD3000/runscript/1.0__smoke_hover_run.xml 재실행

## [2026-08-11 17:05] INDEX-20260811-1705-001 — 정정 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-11 17:05 KST
- 최근 수행 과업: AD3000 Markdown 설명 문서 및 생성 스크립트 템플릿 한글화
- 현재 상태: workflow mirror의 README.md와 ASSUMPTIONS_AND_LIMITATIONS.md가 한글로 정정됐고, 생성 스크립트도 한글 Markdown을 재생성하도록 수정됨
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/AD3000/README.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/AD3000/ASSUMPTIONS_AND_LIMITATIONS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_generate_aircraft.py, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/*.md
- 주요 결정: 기술 식별자와 경로는 원문 유지하고 설명 문장은 한글화
- 남은 리스크: XML documentation과 CSV note에는 영어 표현이 일부 남아 있음
- 권장 다음 작업: 필요 시 XML documentation과 CSV note까지 한글화

## [2026-08-11 00:00] INDEX-20260811-0000-002 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-11 00:00 Asia/Seoul
- 최근 수행 과업: AD3000 제품 기반 motor/prop XML 추가 및 Propulsion.xml 참조 갱신
- 현재 상태: AD3000 aircraft는 JSBSim catalog 로드와 1.5초 smoke run 기준 동작 확인됨. 제품 기반 lift와 cruise propulsion 파일이 추가됨
- 최근 변경 파일: AD3000 Propulsion.xml, 제품 기반 engine XML 2개, 제품 기반 prop XML 2개, PROPULSION_PRODUCTS.md, PROPULSION_SOURCE_DATA.csv
- 주요 결정: lift는 V6212 180KV와 VSC 22.1x7.4 공식 pull test 기반, cruise는 V6215 210KV 모터 사양과 Falcon C2E 20x10 형상 및 22x12 공개 표의 피치비 보정 기반으로 구성
- 미완료 TODO: Falcon C2E 20x10 직접 시험표 확보, cruise prop 계수 재보정, 8초 hover run Floating point exception 해결
- 남은 리스크: 실제 전진비별 prop polar와 설치 효과가 반영되지 않아 추력/전력 예측 오차 가능성이 있음
- 권장 다음 작업: 실제 prop bench data 확보 후 Ct/Cp 재산정, 전후 lift rotor 추력 분배 제어 검증, 전체 run 안정화

## [2026-08-11 17:11] CORRECTION-20260811-1711-001 — 정정

- 대상 기록: TASK-20260811-0000-002, PROGRESS-20260811-0000-002, DECISION-20260811-0000-002, TODO-20260811-0000-002, INDEX-20260811-0000-002
- 정정 이유: 제품 기반 propulsion 반영 기록을 append할 때 기록 시각을 임시값 2026-08-11 00:00으로 남김
- 기존 내용: 기록 시각이 2026-08-11 00:00 또는 ENTRY ID 20260811-0000으로 표기됨
- 정정 내용: 해당 항목의 실제 기록 시각은 2026-08-11 17:11 KST임. 기록 내용과 검증 결과는 그대로 유효함
- 영향 범위: docs/agent-log 아래 Markdown 기록의 메타데이터 시각 표기
- 검증 결과: append-only 방식으로 정정 기록을 추가함
- 다음 작업: 이후 기록에서는 실제 KST 시각을 사용

## [2026-08-12 09:00] INDEX-20260812-0900-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-12 09:00 KST
- 최근 수행 과업: AD3000 cruise propulsion을 V6215+VSC22.1x7.4 공개 데이터 기준으로 재구성
- 현재 상태: AD3000 기본 Propulsion.xml은 lift V6212+VSC22.1x7.4, cruise V6215+VSC22.1x7.4 제품 공개표 기반 파일을 참조함
- 최근 변경 파일: Propulsion.xml, AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, PROPULSION_PRODUCTS.md, PROPULSION_SOURCE_DATA.csv, AD3000_generate_aircraft.py
- 주요 결정: Falcon C2E 20x10은 실제 의도 prop이나 공개 thrust/power sheet 부재로 기본 참조에서 제외하고 한글 주석으로 명시함
- 미완료 TODO: Falcon 20x10 직접 데이터 확보, cruise prop 재보정, 8초 hover FPE 해결
- 남은 리스크: 임시 22.1x7.4 cruise prop은 실제 20x10 형상과 다르므로 transition 성능 예측 오차 가능성이 있음
- 권장 다음 작업: Falcon 20x10 벤치 데이터 확보 후 Propulsion.xml 참조를 실제 prop 파일로 전환

## [2026-08-12 09:14] INDEX-20260812-0914-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-12 09:14 KST
- 최근 수행 과업: AD3000 XML 적용값 자동 검증 스크립트 추가 및 실행
- 현재 상태: AD3000 XML 구성값 검증은 PASS 86, FAIL 0이며 JSBSim catalog load도 성공함
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py, docs/agent-log/*.md
- 주요 결정: 비행 안정성 확인 전 XML 적용값 검증을 먼저 수행하는 방식으로 분리
- 미완료 TODO: 8초 hover FPE, Falcon 20x10 직접 성능표 확보, 동적 로그 기반 검증
- 남은 리스크: 현재 검증은 구성값 적용 여부만 확인하며 안정 hover나 전이비행 성능을 보장하지 않음
- 권장 다음 작업: AD3000_validate_config.py를 XML 수정 후 기본 회귀검증으로 실행

## [2026-08-12 09:19] INDEX-20260812-0919-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-12 09:19 KST
- 최근 수행 과업: AD3000 XML table 조건별 보간 확인 도구 추가
- 현재 상태: AD3000_eval_table.py로 prop 1D table과 Aero.xml 2D/3D table 보간값 확인 가능
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_eval_table.py, docs/agent-log/*.md
- 주요 결정: table 자체 검증과 JSBSim 동적 출력 검증을 분리함
- 미완료 TODO: JSBSim output property와 table evaluator 기대값의 자동 비교는 아직 없음
- 남은 리스크: table-only 값은 force/moment 최종값이 아니라 coefficient 또는 table 항목 값임
- 권장 다음 작업: table 값 확인 후 필요 조건에서 runscript output을 추가해 동적 검증 수행

## [2026-08-12 09:40] INDEX-20260812-0940-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-12 09:40 KST
- 최근 수행 과업: DB 정리.xlsx 기체 Spec 시트 기반 AD3000 propulsion 데이터 반영
- 현재 상태: propulsion source CSV는 기체 Spec 시트 전체 44개 pull test 행을 포함하고, prop XML은 used_for_coefficient=Y 행의 평균 Ct/Cp를 사용함
- 최근 변경 파일: PROPULSION_SOURCE_DATA.csv, PROPULSION_PRODUCTS.md, Propulsion.xml, AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, AD3000_validate_config.py, AD3000_generate_aircraft.py
- 주요 결정: 전체 엑셀 원자료는 CSV에 보존하고 45-84% 구간을 계수 산정 대표 구간으로 유지
- 미완료 TODO: 20*10 cruise prop 직접 성능표 확보, 장시간 hover 안정화
- 남은 리스크: cruise prop은 여전히 실제 의도 규격 20*10이 아닌 VSC22.1x7.4 임시 적용
- 권장 다음 작업: 20*10 성능표 확보 시 cruise prop XML 재보정

## [2026-08-12 09:46] INDEX-20260812-0946-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-12 09:46 KST
- 최근 수행 과업: AD3000 propulsion 계수 산정에 기체 Spec 33-100% 전체 데이터 반영
- 현재 상태: PROPULSION_SOURCE_DATA.csv의 44개 공식표 행 전체가 used_for_coefficient=Y이며 prop XML Ct/Cp는 전체 평균 기준으로 갱신됨
- 최근 변경 파일: PROPULSION_SOURCE_DATA.csv, PROPULSION_PRODUCTS.md, AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, AD3000_generate_aircraft.py
- 주요 결정: 45-84% 대표 구간 결정은 폐기하고 33-100% 전체 공식 데이터를 사용
- 미완료 TODO: throttle별 motor-prop map 직접 구현, 8초 hover 안정화
- 남은 리스크: 현재 구조는 전체 데이터 평균 계수이며 공식표 곡선을 throttle별로 직접 재현하지는 않음
- 권장 다음 작업: 실제 throttle별 thrust/power 재현이 필요하면 별도 lookup map 모델 구현

## [2026-08-12 09:55] INDEX-20260812-0955-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-12 09:55 KST
- 최근 수행 과업: AD3000 prop XML에 전진비 table 산정 한계 주석 추가
- 현재 상태: prop XML과 products 문서에 J=0 직접 산정, J>0 임시 advance-ratio shape 적용이 명시됨
- 최근 변경 파일: AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, Propulsion.xml, PROPULSION_PRODUCTS.md, AD3000_generate_aircraft.py
- 주요 결정: 데이터 기반 J=0 계수와 가정 기반 J>0 curve를 문서와 XML 주석에서 분리 명시
- 미완료 TODO: 전진속도 포함 prop map 확보
- 남은 리스크: J>0 table은 실측값이 아니라 임시 형상
- 권장 다음 작업: airspeed/RPM/thrust/power 데이터 확보 시 J별 Ct/Cp table 재구성


## [2026-08-12 00:00] INDEX-20260812-0000-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 최근 수행 과업: `5.16` 원형 선회 시간 구간 확인
- 현재 상태: 코드 변경 없음. 최신 `5.16.6` 로그 기준 원형 선회는 `183.742 - 244.308 s`
- 권장 다음 작업: 그래프에서 `180 - 245 s` 시간축을 적용해 선회 구간만 확인

## [2026-08-13 13:39] INDEX-20260813-1339-001 — 스냅샷

- 프로젝트명: evtol-6dof/jsbsim_workflow
- 최근 수행 과업: standard_vtol_demo JSBSim 단독 모델 구성 및 DATCOM 공력/5모터 arming 1차 확인
- 현재 상태: /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo 에 DATCOM 기본 모델 설치 완료. workflow aircraft_variants/standard_vtol_demo_jsbsim 에 원본, DATCOM, demo aero variant 및 검증 스크립트 보관.
- 최근 변경 파일: aircraft_variants/standard_vtol_demo_jsbsim/*, results/standard_vtol_demo_jsbsim/*.csv, jsbsim_workflow_data/scripts/build_standard_vtol_jsbsim.py, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo/*, /home/junyeopkwon/jsbsim/scripts/standard_vtol_demo_*.xml
- 주요 결정: DATCOM 모델을 기본 standard_vtol_demo.xml로 두고 demo aero variant를 별도 파일로 보존. 모터는 fcs/motor-armed 게이트로 JSBSim 단독 arming 확인.
- 미완료 TODO: 생성기 postprocess 통합, 천이 없는 시나리오 구성, DATCOM 3D Mach breakpoint 제어증분 보간 복원, 정상 비행 튜닝.
- 남은 리스크: 공력 출력값은 qbar-area가 곱해진 함수 출력이며 순수 coefficient가 아니다. 현재 검증은 연결 확인이지 비행성 검증이 아니다.
- 권장 다음 작업: 천이 없는 수직이륙/착륙 시나리오 runscript 구성 전 hover 추력, 지상 접촉, 초기 arming/시동 sequence를 먼저 고정한다.

## [2026-08-13 14:45] INDEX-20260813-1445-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 14:45 KST
- 최근 수행 과업: standard_vtol_demo JSBSim 단독 수직이륙-호버-착륙-shutdown 미션 구성 및 실행
- 현재 상태: 김포공항 RKSS 14L 좌표에서 미션 종료 state7까지 정상 실행됨
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo/initial_condition/1.0__rkss14_runway_ground_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo/runscript/1.0__rkss14_vertical_takeoff_hover_land_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/standard_vtol_demo_hover.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/results/standard_vtol_demo_jsbsim/mission_vertical/standard_vtol_demo_rkss14_vertical_mission.csv, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/results/standard_vtol_demo_jsbsim/mission_vertical/standard_vtol_demo_rkss14_vertical_mission.log
- 주요 결정: JSBSim 단독 실행을 위해 standard_vtol_demo_hover variant에 내부 hover attitude/altitude controller를 추가함
- 미완료 TODO: 천이 없는 다음 시나리오 확장, 전방/후방 천이 미션 설계
- 남은 리스크: PX4 flightcontrol 동일성 미검증, pusher motor는 수직 미션에서 0 명령, 착륙 접지 품질 추가 튜닝 가능
- 권장 다음 작업: 수평 위치 유지가 포함된 takeoff-hover-land 미션 또는 천이 전 단계의 상승/하강 프로파일 정교화

## [2026-08-13 15:04] INDEX-20260813-1504-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 15:04 KST
- 최근 수행 과업: standard_vtol_demo 계열 F450식 모듈 분리 개정
- 현재 상태: standard_vtol_demo와 standard_vtol_demo_hover 모두 메인 XML에서 모듈 파일을 include하는 구조로 정리됨. 기본 공력은 Aero_DATCOM.xml, 교체용 공력은 Aero_Demo.xml.
- 최근 변경 파일: standard_vtol_demo.xml, standard_vtol_demo_hover.xml, Metrics.xml, Mass.xml, Gear.xml, Effectors.xml, FlightControl.xml, ExternalReactions.xml, Aero_DATCOM.xml, Aero_Demo.xml, *_datcom_main.xml, *_demo_main.xml
- 주요 결정: 현재 모델에 없는 JSBSim propulsion 섹션은 억지로 생성하지 않고, rotor/pusher force는 ExternalReactions.xml 모듈로 분리한다.
- 검증 결과: catalog/arming/aero/수직 미션 회귀 통과. 최종 미션 state7 종료, final motor-armed=0, esc-out[0..4]=0.
- 미완료 TODO: 천이 전 propulsion 구조 판단, PX4-like flightcontrol 정리, 천이 없는 다음 미션 확장
- 남은 리스크: 현재 hover controller는 JSBSim 단독 보조 제어기이며 PX4 flightcontrol과 동일하지 않다.
- 권장 다음 작업: 모듈 구조를 기준으로 FlightControl.xml의 hover/transition/fixed-wing 채널 경계를 설계한다.

## [2026-08-13 15:05] INDEX-20260813-1505-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 15:05 KST
- 최근 수행 과업: standard_vtol_demo 모듈 XML BOM 제거 및 catalog 재검증
- 현재 상태: F450식 모듈 구조 유지, standard_vtol_demo/standard_vtol_demo_hover catalog 파싱 통과
- 최근 변경 파일: standard_vtol_demo 계열 XML/Python 파일 일부 인코딩 marker 제거
- 주요 결정: 기능 변경 없이 UTF-8 without BOM으로 정리
- 미완료 TODO: 천이 전 propulsion 구조 판단, PX4-like flightcontrol 정리
- 남은 리스크: 없음
- 권장 다음 작업: 모듈화된 FlightControl.xml 기준으로 다음 미션 단계 설계

## [2026-08-13 15:10] INDEX-20260813-1510-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 15:10 KST
- 최근 수행 과업: standard_vtol_demo_hover runner 메뉴 선택 오류 수정
- 현재 상태: python3 run_jsbsim_timestamped_combined_csv_only.py 실행 후 78 -> 1 -> 1 선택으로 standard_vtol_demo_hover 수직 미션 실행 가능
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.0__rkss14_runway_ground_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/1.0__rkss14_vertical_takeoff_hover_land_run.xml
- 주요 결정: aircraft 78 standard_vtol_demo_hover 전용 scripts 폴더를 만들고, initial_condition 폴더는 runscript discovery에서 제외
- 검증 결과: combined CSV rows=3601, mission/state 최종 7, motor-armed=0, esc-out[0..4]=0
- 미완료 TODO: 천이 전 propulsion 구조 판단, PX4-like flightcontrol 정리
- 남은 리스크: 77 standard_vtol_demo와 78 standard_vtol_demo_hover의 용도를 문서에서 더 명확히 정리할 필요 있음
- 권장 다음 작업: README 또는 모델 설명에 78번 실행 절차와 77/78 용도 차이를 명시

## [2026-08-13 15:50] INDEX-20260813-1550-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 15:50 KST
- 최근 수행 과업: standard_vtol_demo_hover 전방/후방 천이 포함 runscript 구성 및 runner 검증
- 현재 상태: 메뉴 실행 78 -> 1 -> 2로 transition mission 실행 가능. 최종 state13, motor-armed=0, esc-out[0..4]=0 확인.
- 최근 변경 파일: FlightControl.xml, Effectors.xml, 2.0__rkss14_transition_mission_run.xml, 관련 보조 스크립트
- 주요 결정: PX4 standard VTOL 로직을 상태 머신과 pusher/mc-weight ramp로 매핑하되, elevator effectiveness 부재 때문에 FW segment에 mc-weight 0.22를 유지한다.
- 검증 결과: Combined CSV rows=21502, last time=215.01, 최대 속도 22.56 m/s, 최대 고도 50.16 m, 최종 정지 및 모터 off.
- 미완료 TODO: elevator/TECS/propulsion 보강 후 mc-weight 0 strict transition 재튜닝
- 남은 리스크: 현재 결과는 JSBSim standalone transition proof이며 PX4 실제 제어기 동등성 검증은 아님.
- 권장 다음 작업: FW control surface/elevator 공력항 확보 후 pusher/airspeed/altitude 제어를 TECS-like로 분리

## [2026-08-13 17:16] INDEX-20260813-1716-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 17:16 KST
- 최근 수행 과업: standard_vtol_demo_hover 멀티콥터 조종자격증 유사 3.0 runscript 구성 및 1.1 지상 초기조건 추가
- 현재 상태: runner 메뉴에서 78 -> 2 -> 3으로 3.0__rkss14_multicopter_certificate_mission 실행 가능. 최종 state32, motor-armed=0, esc-out[0..4]=0, mc-weight=1, pusher off 확인.
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Effectors.xml
- 주요 결정: attitude target만으로는 drift가 커서, 기본 off인 hover speed hold 보조 채널을 추가하고 3.0에서만 body speed target을 사용한다.
- 미완료 TODO: 실제 시험 코스 geometry를 waypoint/position controller로 엄밀히 추종하도록 고도화, 착륙 gear force 저감 튜닝
- 남은 리스크: 3.0은 JSBSim standalone mission proof이며 실제 한국교통안전공단 시험 코스/채점 기준의 정밀 재현은 아니다. final displacement 약 N/E=10.57/19.07 m, max distance=22.19 m.
- 권장 다음 작업: 3.0 결과를 기준으로 NE waypoint set, yaw/heading profile, 3-5 m altitude tolerance check를 추가해 3.1 정밀 코스 runscript로 확장한다.
## [2026-08-13 17:41] INDEX-20260813-1741-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 17:41 KST
- 최근 수행 과업: 3.0 멀티콥터 mission을 state-gated 전이로 수정하고 긴급강하 제거
- 현재 상태: runner 메뉴 78 -> 2 -> 3으로 3.0.5 실행 통과. state3 hover 유지, 원주비행 이후 circle complete hover -> normal landing -> touchdown idle -> shutdown -> terminate 순서 확인.
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml
- 주요 결정: 모든 주 전이를 mission/state eq 이전상태 조건으로 gate하고, duration 보조 조건은 절대 mission/next-trigger-sec로 둔다.
- 미완료 TODO: 완전한 상대시간 state-age timer, waypoint/position 완료 조건, yaw/heading command 추가
- 남은 리스크: trigger 시각보다 이전 state 완료가 늦어지는 경우 hold duration이 줄어들 수 있다. 현재 final displacement는 N/E=6.217/19.965 m, max distance=20.923 m.
- 권장 다음 작업: 3.1에서 state-age timer와 NE waypoint controller를 추가해 실제 시험 코스 geometry를 명시적으로 추종한다.
## [2026-08-13 17:45] INDEX-20260813-1745-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 17:45 KST
- 최근 수행 과업: 3.0 복구 및 3.1 state-gated runscript 분리
- 현재 상태: 3.0은 이전 시간 기반/긴급강하 포함 버전으로 복구됨. 3.1은 state-gated/긴급강하 제거/원주 후 정상착륙 버전으로 추가됨.
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.1__rkss14_multicopter_certificate_mission_state_gated_run.xml
- 주요 결정: 기존 numbered runscript는 보존하고, 의미 있는 동작 변경은 새 minor version으로 추가한다.
- 검증 결과: 3.0.6 및 3.1.1 모두 final motor off, pusher off, mc-weight=1 유지 확인.
- 미완료 TODO: 3.1의 완전한 relative state-age timer 및 waypoint/position 완료 조건 고도화
- 남은 리스크: 없음. 단, 이전 17:41 기록은 CORRECTION-20260813-1745-001로 정정됨.
- 권장 다음 작업: runner 메뉴에서 3.1 선택 번호를 확인하고, 이후 작업은 3.2 또는 4.0 등 새 번호로 분리한다.
## [2026-08-13 18:07] INDEX-20260813-1807-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 18:07 KST
- 최근 수행 과업: standard_vtol_demo_hover metric/mass/nose-origin coordinate update
- 현재 상태: active module Metrics/Mass/Gear/ExternalReactions와 /home/junyeopkwon/jsbsim mirror에 요청값 반영 완료. 3.1.3 실행 통과, final state30, motor off 확인.
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Metrics.xml, Mass.xml, Gear.xml, ExternalReactions.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Metrics.xml, Mass.xml, Gear.xml, ExternalReactions.xml
- 주요 결정: 기존 CG-relative x 좌표에 0.64914 m를 더해 nose-origin structural coordinate로 변환한다.
- 미완료 TODO: 20 kg 기준 hover throttle/altitude controller 재튜닝, 실제 CAD 좌표 검증, htailarm/vtailarm 실측값 확보
- 남은 리스크: 3.1 미션에서 4 m target 대비 최대 고도 약 6.25 m overshoot가 발생한다. 전방 lift motor 좌표가 nose보다 104.86 mm 앞에 위치하는 계산 결과는 기존 relative 배치 보존에 따른 것이다.
- 권장 다음 작업: 20 kg 기준 hover throttle base를 약 0.535 근처로 낮추고 altitude controller를 재검증한다.
## [2026-08-13 18:14] INDEX-20260813-1814-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-13 18:14 KST
- 최근 수행 과업: 20 kg 기준 hover throttle 산출 및 3.2/3.3/3.4 control mission 구성
- 현재 상태: Effectors.xml hover-throttle-base=0.535 반영. 3.4 state-gated 20kg hover smooth spooldown mission 실행 통과, final state33, motor off, pusher off.
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Effectors.xml, 3.2/3.3/3.4 runscript files
- 주요 결정: 20 kg hover base는 현재 lift thrust table 기반 0.535로 둔다. 기존 runscript는 보존하고 3.2/3.3/3.4로 튜닝 버전을 분리한다.
- 미완료 TODO: 착륙 충격 저감용 h-dot landing controller 또는 gear spring/damping 튜닝
- 남은 리스크: 3.4 max gear force=221.64 lbf=5.02W. thrust table이 실제 벤치 데이터가 아니면 hover base 재보정 필요.
- 권장 다음 작업: 3.5에서 vertical velocity target landing controller를 추가하거나 Gear.xml damping/spring을 재검토한다.
## [2026-08-14 10:01 KST] INDEX-20260814-1001-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: PX4 ULog -> combined CSV 변환 스크립트 추가
- 현재 상태: 샘플 PX4 .ulg를 logs/csv/combined/standard_vtol_demo_hover_px4/00_55_52/ 아래 combined CSV로 변환 완료
- 최근 변경 파일: scripts/px4_ulog_to_combined_csv.py
- 주요 결정: PX4/QGC 로그는 .ulg를 원본으로 두고 필요 시 combined CSV로 변환한다.
- 미완료 TODO: JSBSim 내부 FDM property와 PX4 ULog 동기화 로깅
- 남은 리스크: 실제 비행 미션 로그 변환은 아직 미검증
- 권장 다음 작업: QGC 미션 실행 후 최신 .ulg를 변환하고 주요 topic을 분석한다.

## [2026-08-14 10:08 KST] INDEX-20260814-1008-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: PX4 JSBSim QGC 실행 매뉴얼 및 자동화 스크립트 추가
- 현재 상태: 문서/스크립트 작성 및 정적 검증 완료
- 최근 변경 파일: docs/PX4_JSBSIM_QGC_RUNBOOK.md, scripts/run_px4_jsbsim_qgc_workflow.py, scripts/px4_ulog_to_combined_csv.py
- 주요 결정: WSL QGC AppImage를 우선 실행 대상으로 하고, PX4 종료 후 최신 ULog를 combined CSV로 자동 변환한다.
- 미완료 TODO: 실제 QGC mission 실행 검증
- 남은 리스크: GUI/QGC 연결 환경 차이, 실제 비행 안정성 미검증
- 권장 다음 작업: python3 run_px4_jsbsim_qgc_workflow.py --launch-qgc로 실제 QGC mission을 수행한다.

## [2026-08-14 10:54] INDEX-20260814-1054-002 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: PX4 JSBSim QGC 실행 매뉴얼 RKSS 반영 및 combined CSV 변환 확인
- 현재 상태: 매뉴얼의 수동 실행 명령은 RKSS target 기준이며, 최신 PX4 ULog를 combined CSV로 변환 가능
- 최근 변경 파일: docs/PX4_JSBSIM_QGC_RUNBOOK.md, scripts/run_px4_jsbsim_qgc_workflow.py
- 주요 결정: QGC/PX4 실행은 jsbsim_standard_vtol_demo_hover_px4__RKSS target을 기본 경로로 안내
- 미완료 TODO: QGC UI 기반 실제 미션 로그 생성 및 CSV 분석
- 남은 리스크: 실제 arm/takeoff/land 제어 안정성 미검증
- 권장 다음 작업: QGC에서 Ready 확인 후 저고도 takeoff/land를 수행하고 combined CSV로 상태/actuator/position을 검토

## [2026-08-14 11:12] INDEX-20260814-1112-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: ULog 선택형 combined CSV 변환 기능 추가 및 기록 정정
- 현재 상태: python3 scripts/px4_ulog_to_combined_csv.py를 인자 없이 실행하면 최신 PX4 ULog 목록에서 번호를 선택해 combined CSV를 생성할 수 있음
- 최근 변경 파일: scripts/px4_ulog_to_combined_csv.py, docs/PX4_JSBSIM_QGC_RUNBOOK.md, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 주요 결정: 기존 경로 직접 지정 방식은 유지하고, 인자 생략 시 interactive 선택 모드로 동작
- 미완료 TODO: 없음
- 남은 리스크: 기본 표시 개수는 30개로 제한되며 필요 시 --list-limit로 조정
- 권장 다음 작업: QGC mission 후 생성된 최신 ULog를 선택해 CSV 변환 및 flight 결과 분석

## [2026-08-14 11:36] INDEX-20260814-1136-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 최근 수행 과업: PX4 ULog와 JSBSim property 결합 CSV 및 그래프 생성 기능 추가
- 현재 상태: px4_jsbsim_compare_plot.py를 실행하면 ULog 선택 후 PX4 plus JSBSim merged CSV와 plots PNG를 생성할 수 있음
- 최근 변경 파일: scripts/px4_jsbsim_compare_plot.py, scripts/run_px4_jsbsim_qgc_workflow.py, docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 주요 결정: PX4 ULog는 pyulog로 변환하고, JSBSim 적용값은 모델 native output CSV를 읽어 time_s 기준으로 병합한다.
- 미완료 TODO: 실제 QGC 미션 로그로 actuator 일치성 및 비행상태 그래프 분석
- 남은 리스크: latest_jsbsim_properties.csv overwrite 주의
- 권장 다음 작업: QGC 미션 수행 후 px4_jsbsim_compare_plot.py로 최신 로그를 선택하고 actuator_px4_vs_jsbsim.png부터 확인한다.

## [2026-08-18 11:35] INDEX-20260818-1135-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: `2026-08-18 11:35 KST`
- 최근 수행 과업: `logs/csv/combined` 생성 시 선회/제어 분석용 property 추가
- 현재 상태: 새 combined CSV 생성 시 C172 heading-hold 선회 체인, circular bank 활성/비활성 상태, VTOL hover target/error/mix, F450/LiftCruise AP setpoint/error/mix 계열 property가 aircraft catalog에 존재하는 경우 자동 포함됨
- 최근 변경 파일: `scripts/run_jsbsim_timestamped_combined_csv_only.py`
- 최근 생성 파일: `logs/csv/combined/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.8__ksfo28r_runway_return_circular_landing_combined_08181131.csv`, `logs/generated_runscripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.8__ksfo28r_runway_return_circular_landing_combined_runscript_08181131.xml`, `logs/console/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.8__ksfo28r_runway_return_circular_landing_combined_console_08181131.log`
- 주요 결정: 없는 property를 무조건 추가하지 않고 aircraft catalog에 실제 존재하는 property만 combined output에 추가
- 미완료 TODO: `TODO-20260818-1135-001` 주요 과거/비교 scenario를 새 컬럼 기준으로 재실행할지 결정 필요
- 남은 리스크: `scripts/run_jsbsim_timestamped_combined_csv_only.py`는 Git 기준 untracked 상태이며, 과거 combined CSV에는 새 컬럼이 없음. 새 샘플 CSV는 약 192 MB임.
- 권장 다음 작업: 발표자료/분석에 쓰는 실제 scenario CSV가 무엇인지 확정한 뒤 해당 scenario를 새 combined runner로 재실행

## [2026-08-18 11:47] INDEX-20260818-1147-001 — SNAPSHOT

- 프로젝트명: `jsbsim_workflow`
- 기록 시각: `2026-08-18 11:47 KST`
- 최근 수행 과업: combined CSV 공력계수 전체 포함 구성
- 현재 상태: 새 combined CSV 생성 시 aircraft catalog에 존재하는 모든 `aero/coefficient/*` property가 자동 포함됨
- 최근 변경 파일: `scripts/run_jsbsim_timestamped_combined_csv_only.py`
- 주요 결정: 기존 aircraft catalog 기반 필터링 방식을 유지하고, 공력계수는 prefix `aero/coefficient/` 기준으로 동적 수집
- 미완료 TODO: 기존 combined CSV 재생성은 별도 필요
- 남은 리스크: 기존 combined CSV에는 새 공력계수 컬럼이 없음. 실제 새 CSV 생성은 분석 대상 scenario 재실행 시 확인 필요.
- 권장 다음 작업: 발표자료/분석에 사용할 scenario를 새 combined runner로 재실행

## [2026-08-19 10:21] INDEX-20260819-1021-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 10:21 KST
- 최근 수행 과업: 첨부 standard_vtol_demo_motor_updated_ko.xml의 PX4/JSBSim 실행 가능성 검토
- 현재 상태: 첨부 XML은 XML 문법은 통과하지만 JSBSim 1.2.4 단독 로딩에서 aero/coefficient/CL_base table 형식 오류로 실패하므로 PX4/QGC 실행 전 보정 필요
- 최근 변경 파일: docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/TODO.md, docs/agent-log/INDEX.md
- 주요 결정: 기존 PX4 target에 덮어쓰지 않고, 먼저 별도 후보 모델로 JSBSim 단독 호환성을 통과시킨 뒤 PX4 airframe/bridge config에 등록한다.
- 미완료 TODO: TODO-20260819-1021-001 첨부 XML 호환 보정 및 PX4 별도 target 등록
- 남은 리스크: 공력 table의 lookup table 형식, 1.0 / velocities/vt-fps 직접 분모에 따른 정지 초기조건 FPE, CG 기준 motor/gear/pusher 좌표, 14 kg 질량 대비 PX4 MPC_THR_HOVER=0.535 불일치
- 권장 다음 작업: 새 모델명을 정해 workflow/PX4에 별도 후보 모델을 만들고, JSBSim catalog/load/run 검증을 먼저 완료

## [2026-08-19 10:31] INDEX-20260819-1031-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 10:31 KST
- 최근 수행 과업: standard_vtol_demo_motor_updated_ko.xml 공력 table 형식 보정
- 현재 상태: workflow 내부 후보 모델에서 Mach별 2D 공력 table 14개를 JSBSim 1.2.4 호환 row/column table로 변환 완료. FGTable missing lookup axis column 오류는 제거됨.
- 최근 변경 파일: aircraft_variants/standard_vtol_demo_motor_updated_ko/source_standard_vtol_demo_motor_updated_ko.xml, aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml, docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/TODO.md, docs/agent-log/INDEX.md
- 주요 결정: 원본 첨부 XML은 보존하고, workflow 내부 후보 모델에 table 보정본을 분리 생성한다.
- 미완료 TODO: TODO-20260819-1031-001 Floating point exception 제거, PX4 별도 target 등록
- 남은 리스크: 공력 rate 항의 1.0 / velocities/vt-fps 직접 분모, CG 기준 좌표, 14 kg hover parameter, PX4 airframe/bridge 정합성
- 권장 다음 작업: aero/ci2vel 및 aero/bi2vel 기반으로 공력 rate 항의 0속도 보호를 적용하고 JSBSim --catalog 및 --end=0.02를 정상 종료시킨다.

## [2026-08-19 10:38] INDEX-20260819-1038-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 10:38 KST
- 최근 수행 과업: standard_vtol_demo_motor_updated_ko.xml 0속도 보호 보정
- 현재 상태: 공력 table 보정본에서 velocities/vt-fps 직접 분모 quotient 제거 완료. JSBSim --catalog 및 지상 정지 초기조건 --end=0.02, --end=1.0 모두 rc=0.
- 최근 변경 파일: aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml, docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/TODO.md, docs/agent-log/INDEX.md
- 주요 결정: 직접 1.0 / velocities/vt-fps quotient 대신 기존 정상 모델과 같은 aero/ci2vel 및 aero/bi2vel을 사용한다.
- 미완료 TODO: TODO-20260819-1038-001 PX4 등록 전 geometry 및 hover parameter 정합성 검토
- 남은 리스크: CG 기준 좌표, 14 kg 기준 MPC_THR_HOVER, CA_ROTOR geometry/sign, PX4 bridge model 등록
- 권장 다음 작업: 후보 모델의 좌표계를 기존 PX4 모델과 비교해 정리하고, 14 kg 기준 hover parameter를 산정한 뒤 별도 PX4 target으로 등록

## [2026-08-19 10:52] INDEX-20260819-1052-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 10:52 KST
- 최근 수행 과업: standard_vtol_demo_motor_updated_ko PX4 연결 후보 검증 및 20kg 복귀
- 현재 상태: 공력 table 형식과 0속도 보호는 정리되었고, PX4 연결 후보는 20kg에서 NaN 없이 실행됨
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 주요 결정: 14kg은 접지/FPE 문제가 있어 이전 무게 20kg으로 진행
- 미완료 TODO: arm/hover/takeoff 검증
- 남은 리스크: 실제 비행 제어 안정성, 공력 table 물리 타당성
- 권장 다음 작업: PX4 arm 및 hover 단계 검증 로그 수집

## [2026-08-19 11:02] INDEX-20260819-1102-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 11:02 KST
- 최근 수행 과업: standard_vtol_demo_motor_updated_ko_px4 arm-hover-land 실행
- 현재 상태: arm, takeoff detected, 약 1m 짧은 hover, landing detected, disarmed by landing 확인
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md
- 주요 결정: 추가 파라미터 변경 없이 20kg 후보로 첫 폐루프 실행 결과를 기록
- 미완료 TODO: 목표고도 2.5m hover 추종 개선
- 남은 리스크: altitude setpoint 대비 실제 AGL 부족, 장시간 안정성 미검증
- 권장 다음 작업: 긴 hover run 및 ulog setpoint/position/actuator 비교 분석

## [2026-08-19 11:08] INDEX-20260819-1108-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 11:08 KST
- 최근 수행 과업: 새 PX4 JSBSim 모델 직접 실행 매뉴얼 보강
- 현재 상태: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md 섹션 9에 직접 실행 명령 정리 완료
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 주요 결정: 기존 runbook을 유지하고 새 모델 섹션을 하단 append
- 미완료 TODO: 목표고도 2.5m hover 추종 튜닝
- 남은 리스크: 문서화된 자동 실행은 이전 검증 결과 기반이며 목표고도 도달 튜닝은 별도 필요
- 권장 다음 작업: 사용자가 직접 실행 후 생성 ulog/CSV로 setpoint 대비 AGL 분석

## [2026-08-19 11:13] INDEX-20260819-1113-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 11:13 KST
- 최근 수행 과업: QGC에서 새 JSBSim 모델 arm/takeoff/land 명령 입력 절차 문서화
- 현재 상태: runbook 섹션 9.6에 QGC Fly 버튼 방식과 MAVLink Console 방식 추가 완료
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 주요 결정: PX4/JSBSim은 터미널에서 실행하고 QGC는 vehicle 조작/명령 입력용으로 사용하는 절차를 권장
- 미완료 TODO: QGC GUI 실제 조작으로 목표고도 추종 재검증
- 남은 리스크: QGC 버전별 메뉴명 차이, 현재 모델 목표고도 2.5m 미도달
- 권장 다음 작업: QGC에서 낮은 고도 takeoff 후 land 실행, 생성 ulog/CSV 공유 또는 분석

## [2026-08-19 11:33] INDEX-20260819-1133-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 11:33 KST
- 최근 수행 과업: QGC 20m hover/reposition ULog 분석
- 현재 상태: 20m 고도 유지 및 목표 위치 도달은 확인, 종료 상태는 착륙/Disarm이 아닌 ORBIT 중 비행 상태
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/QGC_20M_HOVER_REPOSITION_LOG_ANALYSIS_20260819.md
- 주요 결정: 최신 rootfs ULog 02_20_29.ulg를 분석 대상으로 사용
- 미완료 TODO: QGC Land/Disarm 완료 로그 재수집
- 남은 리스크: 사용자가 별도 다운로드한 파일 경로가 다르면 재분석 필요
- 권장 다음 작업: Land 명령까지 넣은 QGC 로그로 landing/disarm 검증

## [2026-08-19 11:40] INDEX-20260819-1140-001 — SNAPSHOT

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 11:40 KST
- 최근 수행 과업: standard_vtol_demo_motor_updated_ko XML F450 스타일 분리
- 현재 상태: workflow 및 PX4 bridge 모델이 Metrics/Mass/Gear/Effectors/FlightControl/ExternalReactions/Aero 모듈 구조로 전환됨
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/*.xml
- 최근 변경 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/*.xml
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 주요 결정: 기존 주 파일명 유지, Monolithic.xml 백업 보존
- 미완료 TODO: 분리 후 QGC 20m reposition 재비행은 미수행
- 남은 리스크: 스타일 재직렬화, QGC 장시간 재검증 미수행
- 권장 다음 작업: 모듈별 수정 가이드 또는 QGC 재비행 검증

## [2026-08-19 14:25] INDEX-20260819-1425-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 14:25
- 최근 수행 과업: standard_vtol_demo_motor_updated_ko_px4 고정익 전환 문제 원인 진단
- 현재 상태: 멀티콥터 hover 가능 상태와 별개로, 현재 PX4 airframe이 순수 멀티콥터 구성이라 표준 VTOL 전환 설정이 누락된 상태로 판단
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_TRANSITION_DIAGNOSIS_20260819.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TASK.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/PROGRESS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TODO.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정: 전환 실패 원인 분석은 공력 table보다 PX4 VTOL airframe 설정, pusher/control allocation, JSBSim bridge 조종면/airspeed mapping을 우선 확인하는 순서로 진행
- 미완료 TODO: 3021 airframe 표준 VTOL 전환, bridge 조종면/airspeed mapping 추가, 실제 front transition 로그 검증
- 남은 리스크: fixed-wing trim, 조종면 부호, pusher thrust, FW_AIRSPD_*, VT_F_TRANS_THR 튜닝 미검증
- 권장 다음 작업: 코드 변경 단계에서 3021 airframe을 
c.vtol_defaults 기반 Standard VTOL로 바꾸고 bridge config에 aileron/elevator/rudder/airspeed를 연결

## [2026-08-19 14:31] CORRECTION-20260819-1431-001 — 정정

- 대상 기록: TASK-20260819-1425-001, PROGRESS-20260819-1425-001, TODO-20260819-1425-001, INDEX-20260819-1425-001
- 정정 이유: PowerShell quoting 과정에서 backtick으로 감싼 기술 식별자 일부가 손상되어 표기 정정 필요
- 기존 내용: `rc.mc_defaults`, `rc.vtol_defaults`, `fcs/...`, `barometer`, `rascal.xml`, `vehicle_*`, `airspeed_*` 중 일부가 제어문자 또는 잘린 문자열로 기록됨
- 정정 내용: 올바른 핵심 표기는 `rc.mc_defaults`, `. ${R}etc/init.d/rc.vtol_defaults`, `fcs/esc-cmd-norm[0..4]`, `fcs/aileron-cmd-norm`, `fcs/elevator-cmd-norm`, `fcs/rudder-cmd-norm`, `barometer`, `rascal.xml`, `vehicle_status.nav_state`, `vtol_vehicle_status`, `airspeed_validated`임
- 영향 범위: 진단 결론에는 변화 없음. 손상된 표기는 본 정정 기록과 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_TRANSITION_DIAGNOSIS_20260819.md 재작성본을 기준으로 해석
- 검증 결과: 진단 문서 본문을 literal text로 재작성
- 다음 작업: 3021 airframe 및 bridge config 수정 단계에서 본 정정 표기를 기준으로 적용

## [2026-08-19 14:48] INDEX-20260819-1448-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-19 14:48
- 최근 수행 과업: 전환 성공 `standard_vtol_demo.xml`과 새 PX4-JSBSim 모델 차이 분석
- 현재 상태: 새 모델은 hover는 가능하나 성공 XML에 있던 transition용 full-envelope aero, elevator/rudder derivative, Standard VTOL airframe, bridge surface mapping이 부족한 상태
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_DEMO_COMPARISON_20260819.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TASK.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/PROGRESS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TODO.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/INDEX.md
- 주요 결정: 성공 XML 기준으로는 airframe/bridge 연결과 elevator-rudder aero derivative를 먼저 해결하고, 그 다음 full-envelope/high-alpha 및 전환속도 튜닝을 검증
- 미완료 TODO: 성공 요소 이식 및 transition run 검증
- 남은 리스크: 실제 ProjectAirSim 실행에서 사용된 외부 vehicle 설정이 별도로 존재할 수 있음
- 권장 다음 작업: 3021 airframe/bridge config/Aero.xml을 단계적으로 수정하고 QGC front transition 로그 수집

## [2026-08-20 10:00] INDEX-20260820-1000-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-20 10:00
- 최근 수행 과업: standard_vtol_demo_motor_updated_ko_px4 airframe/bridge를 Standard VTOL로 전환(제어 배선만, 공력/질량/모터 데이터는 무변경)
- 현재 상태: airframe(`CA_AIRFRAME 2`, `CA_ROTOR_COUNT 5`, `CA_SV_CS_COUNT 3`)과 bridge(aileron/elevator/rudder/airspeed 채널 추가)가 구조적으로는 완성되어 DONT_RUN 빌드와 30초 headless 실행을 NaN/크래시 없이 통과함. 다만 `Airspeed selector module down` preflight 경고가 새로 발견됐고, 실제 arm-hover-transition 비행은 아직 미검증. 러더 공력 효과(DATCOM 데이터 한계)는 사용자가 별도 검토 중이라 이번 수정 범위에서 제외됨.
- 최근 변경 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_motor_updated_ko_px4.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/{TASK,PROGRESS,TODO,DECISIONS,INDEX}.md
- 주요 결정: airframe/bridge(제어 배선)만 먼저 수정하고 공력 데이터(elevator/rudder derivative)는 사용자 판단 대기로 분리(DECISION-20260820-1000-001). pusher CA_ROTOR4_PX는 기존 4개 로터 좌표에서 역산한 `PX4_PX = CG_x - motor_x` 공식으로 산정(DECISION-20260820-1000-002)
- 미완료 TODO: airspeed selector 경고 원인 규명(TODO-20260820-1000-001), 실제 MC hover→전방전환→FW 비행 검증(TODO-20260820-1002-001)
- 남은 리스크: FW_AIRSPD_*/VT_F_TRANS_THR가 실측 없는 잠정값, 러더 요 모멘트가 DATCOM 데이터 한계로 약하거나 없을 가능성
- 권장 다음 작업: PX4 shell에서 airspeed_selector 상태 확인 후, arm-hover-transition 실비행으로 실제 전환 성립 여부와 요 축 제어권을 확인

## [2026-08-20 11:20] INDEX-20260820-1120-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-20 11:20
- 최근 수행 과업: airspeed selector 경고 원인 규명 + 실제 arm-hover-transition 비행 검증 + 요 축(러더) 제어 경로 확인
- 현재 상태: (1) airspeed selector 경고는 부팅 트랜지언트로 확인, 실제 arming을 막지 않음. (2) bridge actuator mapping(aileron/elevator/rudder/pusher)이 PX4 FW 컨트롤러의 실제 명령을 정확한 스케일로 JSBSim까지 전달함을 CSV로 최종 확인 — **이번 작업의 원래 목표(제어 배선)는 완전히 검증 완료**. (3) 다만 실제 FW 유지 비행에는 실패함: `commander takeoff`로 수직 상승하는 순간(전환 명령 이전)부터 이미 aero/alpha가 ±90도 부근에서 불안정해지고, 전환 명령으로 조종면이 실제로 움직이기 시작하자 자세가 발산해 t≈49.9s에 지면 충돌 후 시뮬레이션이 NaN으로 붕괴함. 근본 원인은 DATCOM Aero.xml에 고받음각 보호가 없는 것으로 판단되며, 이는 사용자가 이미 "별도 검토 중"이라고 밝힌 공력 데이터 영역이라 이번 세션에서는 수정하지 않음
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/{TASK,PROGRESS,TODO,DECISIONS,INDEX}.md (코드 변경 없음, 진단 전용 세션)
- 주요 결정: 고받음각 발산 문제를 발견했지만 사용자의 기존 지시("공력 데이터는 일단 냅두라")를 존중해 Aero.xml을 수정하지 않고 진단 결과만 문서화(DECISION-20260820-1120-001)
- 미완료 TODO: 고받음각 보호 필요성(TODO-20260820-1120-001, 사용자 판단 대기), 러더 실제 공력 요 모멘트 최종 판정(TODO-20260820-1121-001, 위 항목에 의존)
- 남은 리스크: 사용자가 공력 데이터를 수정하기 전까지는 이 모델로 실제 FW 전환 비행 성공을 재현할 수 없음. 상승률이 큰 모든 시나리오(순수 hover 포함)에서 잠재적으로 동일 문제가 재현될 수 있음
- 권장 다음 작업: 사용자가 DATCOM 공력 데이터(러더 포함 고받음각 보호)를 어떻게 처리할지 결정한 뒤, Aero.xml 수정 → 완만한 상승률로 재시도하는 순서를 권장

## [2026-08-20 12:00] INDEX-20260820-1200-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-20 12:00
- 최근 수행 과업: Aero.xml에 alpha 기반 연속 게이팅(alpha_validity_gate) 적용 및 재검증
- 현재 상태: 사용자와 논의 끝에(F450 순정 모델의 "alpha 계수 상수 0" 방식 확인 → 레퍼런스 성공 모델의 flat-plate 풀레인지 방식 확인 → 절충안으로 alpha 기반 연속 게이팅 채택) Aero.xml에 게이트를 실제로 적용함. **결과는 부분 개선**: 순수 수직상승 구간의 자세 불안정은 확실히 해결됨(theta 요동폭 대폭 감소, CSV로 확인). 그러나 `commander transition` 명령이 실제 반영되는 시점부터 별개의 발산이 발생해 t≈41.8s에 다시 지면충돌+NaN으로 종료함 — 이번 발산은 alpha 문제가 아니라 조종면이 실제로 움직이며 생기는 것으로, 게이트가 닫혀있던 동안 FW 컨트롤러의 명령이 과도하게 쌓였다가 게이트 재개방 시 한꺼번에 반영되는 것으로 추정(미확정)
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/Aero.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/Aero.xml(동기화), docs/agent-log/{TASK,PROGRESS,TODO,DECISIONS,INDEX}.md
- 주요 결정: alpha 기반 연속 게이팅 방식 채택(모드 스위치가 아닌 물리량 기반 램프) — DECISION-20260820-1200-001. 기존 DATCOM 원본 수치는 전혀 건드리지 않고 곱셈 게이트만 추가하는 최소침습 방식
- 미완료 TODO: 전환 명령 반영 이후의 새 발산 원인 규명(TODO-20260820-1200-001) — pusher 사전가속 절차, FW 자세 게인 재검토, 게이트 램프 폭 조정 등이 후보
- 남은 리스크: 이 문제가 해결되지 않으면 여전히 완전한 전환 비행 성공은 달성 못함. 원인이 공력 데이터가 아니라 제어/절차 영역일 가능성이 있어 사용자 판단 필요
- 권장 다음 작업: pusher로 사전 가속 후 transition을 명령하는 정상 절차로 재시도하는 것을 최우선으로 권장(가장 저비용으로 가설을 검증할 수 있는 방법)

## [2026-08-20 12:30] INDEX-20260820-1230-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-20 12:30
- 최근 수행 과업: 사용자 요청으로 CAD 기반 CG 위치 변경(원점→nose 기준 649mm) 이후 모터/기타 부위 좌표 일관성 전수 점검, 발견된 불일치(AERORP) 수정 및 재검증
- 현재 상태: **크래시/발산 문제가 완전히 해결됨.** Mass.xml(CG)/Gear.xml(착륙기어)/ExternalReactions.xml(모터)은 이미 8/19에 649mm 기준으로 정상 보정돼있었으나, Metrics.xml의 `AERORP`/`VRP`가 옛 값(0,0,0)에 방치돼있던 것을 발견함. JSBSim 소스 확인 결과 AERORP는 실제 모멘트 계산(`M = r×F`, r=AERORP-CG)에 직접 쓰이는 물리량이라, CG만 이동하고 AERORP를 안 옮기면서 매 스텝 0.649m짜리 허위 피칭모멘트가 자동으로 더해지고 있었음 — 이게 alpha 게이트 적용 후에도 남아있던 두 번째 발산의 진짜 원인이었음. AERORP/VRP를 0.649로 수정 후 재검증한 결과, 지금까지 반복되던 지면충돌+NaN이 완전히 사라지고 arm→takeoff→transition→land 전체 시퀀스가 NaN 0건으로 정상 착지까지 완료됨(`Landing detected` 확인, 최종 정지상태가 초기 지상정지상태와 정확히 일치)
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/Metrics.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/Metrics.xml(동기화), docs/agent-log/{TASK,PROGRESS,TODO,DECISIONS,INDEX}.md
- 주요 결정: AERORP/VRP를 CG와 동일한 0.649로, EYEPOINT는 원래 데모의 CG 대비 오프셋 관계를 보존해 0.799로 설정(DECISION-20260820-1230-001) — 원래 데모의 "AERORP=CG" 설계 의도를 새 프레임에서도 유지
- 미완료 TODO: `commander transition` 시 여전히 quad-chute로 MC에 강제복귀되는 문제(TODO-20260820-1230-001) — 좌표 문제는 해결됐으므로 이제 순수 전환 로직/속도 프로파일/제어 게인 영역
- 남은 리스크: 진짜 FW 전환 성공(quad-chute 없이 유지비행)은 아직 미달성. 러더 실제 요 모멘트 최종 판정도 이 항목 해결 후에나 가능
- 권장 다음 작업: quad-chute 발동 조건 확인, 정지 호버에서 바로 transition 명령을 넣는 현재 테스트 절차 대신 pusher 사전가속 절차로 재시도

## [2026-08-20 13:00] INDEX-20260820-1300-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-20 13:00
- 최근 수행 과업: DO_REPOSITION으로 실제 전방 목적지를 주는 정상 절차(pymavlink 스크립트)로 전환 재검증
- 현재 상태: **최초로 실제 FW 상태(vtol_state=4) 도달을 확인함.** 사용자가 "정지 호버에서 바로 transition은 절차가 잘못됐다"고 지적한 것을 반영해 `scripts/vtol_transition_mavlink_test.py`를 신규 작성(arm→takeoff→DO_REPOSITION(전방 600m)→10초 대기→DO_VTOL_TRANSITION→모니터링→land). 결과: groundspeed 5→24m/s로 실제 가속하며 vtol_state가 1(TRANSITION_TO_FW)→4(FW)로 정상 전이됨. 직후 theta가 -39~+41도까지 진동하는 자세 이탈이 발생해 quad-chute로 MC 강제복귀됐으나, JSBSim CSV 전체 NaN 0건으로 발산은 아니었고 이후 정상적으로 회복/착지함
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/vtol_transition_mavlink_test.py(신규), docs/agent-log/{TASK,PROGRESS,TODO,INDEX}.md
- 주요 결정: 없음(검증 세션). 원인 후보가 좌표/게이트/제어경로에서 FW 비행 트림(Aero.xml의 Cm0/Cmalpha 등)으로 확정적으로 좁혀짐
- 미완료 TODO: FW 상태 도달 직후 자세 이탈의 정확한 원인 규명 및 트림 보정(TODO-20260820-1300-001) — 사용자가 QGC로 직접 재현 예정
- 남은 리스크: 이 시점부터는 좌표/제어경로 버그가 아니라 공력 트림 튜닝 영역이라, 사용자가 진행 중인 DATCOM 데이터 재검토와 함께 다뤄야 함
- 권장 다음 작업: 사용자의 QGC 재현 결과 확인 후, 필요 시 quad-chute 트리거 파라미터 및 Cm0/Cmalpha 트림 재검토

## [2026-08-20 13:30] INDEX-20260820-1330-001 — 최신 상태 스냅샷

- 프로젝트명: jsbsim_workflow
- 기록 시각: 2026-08-20 13:30
- 최근 수행 과업: standard_vtol_demo(A, 레퍼런스) vs standard_vtol_demo_motor_updated_ko(B, 현재 모델) 전 항목 비교 종합 문서 작성
- 현재 상태: `docs/STANDARD_VTOL_MOTOR_UPDATED_KO_VS_DEMO_CHANGELOG_20260820.md` 신규 작성. **가장 중요한 신규 발견은 B의 Aero.xml에 승강타/러더 공력 모멘트 계수(Cmde/Cndr에 해당하는 항)가 전혀 없다는 것**(elevator-pos-rad/rudder-pos-rad를 참조하는 함수 0개, grep으로 전수 확인) — 조종면은 기계적으로 정상 작동하지만 공력 응답이 없는 상태였음. 최근 전환 테스트의 자세 발산(theta -39~+41도) 유력 원인으로 확정. 부차적으로 Mass.xml 관성모멘트(ixx/iyy/izz)가 A와 완전히 동일해 CAD 재계산 여부가 의심스러움도 발견
- 최근 변경 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_VS_DEMO_CHANGELOG_20260820.md(신규), docs/agent-log/{TASK,PROGRESS,TODO,INDEX}.md
- 주요 결정: 없음(문서화 세션, 코드 변경 없음)
- 미완료 TODO: Cmde/Cndr 추가(TODO-20260820-1300-001 갱신), 관성모멘트 CAD 재계산 여부 확인(TODO-20260820-1330-001, 신규)
- 남은 리스크: 문서 9절 우선순위(승강타/러더 계수 > 관성모멘트 확인 > pusher 감쇠 > FW_AIRSPD 재추정) 중 아직 아무것도 적용 안 됨
- 권장 다음 작업: 사용자 판단에 따라 Cmde/Cndr을 A의 선형 계수 방식으로 우선 임시 적용해 검증하는 것을 최우선 권장
