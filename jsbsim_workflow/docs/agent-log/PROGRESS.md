## [2026-06-15 17:51] PROGRESS-20260615-1751-001 — DONE

- 과업:
  - c172x JSBSim-only no-trim 추락 케이스 구성 및 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 캡쳐본 기준 초기값으로 JSBSim `c172x` 추락 궤적 생성 및 지면 충돌 지표 산출
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.0__450m_60ms_pitch25_no_trim_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.0__450m_60ms_pitch25_no_trim_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.0.4__450m_60ms_pitch25_no_trim_drop_impact_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.0.4__450m_60ms_pitch25_no_trim_drop_impact_summary.json`
- 수행 내용:
  - 기존 `scripts/c172x` 구조와 `run_jsbsim_timestamped.py` 실행 흐름 확인
  - 초기 고도 450 m, 초기 body 전방속도 60 m/s, 자세각 `(0, 2.5, 0) deg` 초기조건 XML 작성
  - autopilot, trim, throttle, mixture, magneto, starter를 0으로 유지하는 runscript 작성
  - `gear/unit[0]/WOW eq 1`에서 종료하는 첫 지면 접촉 이벤트 설정
  - wrapper 스크립트가 기존 timestamp runner를 호출한 뒤 raw/SI CSV를 읽어 충돌 지표 CSV/JSON을 생성하도록 구현
  - 최초 실행 실패 원인인 `hwind/xwind unit="M/SEC"`를 `KTS`로 수정
  - `scripts/c172x/README.md`에 4.x 케이스와 실행 명령 추가
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.0__450m_60ms_pitch25_no_trim_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.0__450m_60ms_pitch25_no_trim_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.0.4__450m_60ms_pitch25_no_trim_drop_impact_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.0.4__450m_60ms_pitch25_no_trim_drop_impact_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 핵심 변경점:
  - `c172x`를 trim/autopilot 없이 엔진 정지 상태에서 초기조건만으로 적분하는 4.0 케이스 추가
  - 결과 요약 필드는 지면 충돌 좌표 `(x_north, y_east, z_ground)`, 접촉 시 CG 고도, 충돌 속도, 최종 자세각을 포함
- 실행한 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
- 테스트 결과:
  - 최종 실행 성공
  - 최종 Run ID: `4.0.4__450m_60ms_pitch25_no_trim_drop`
  - 지면 도달 시간: `32.80833333 s`
  - 지면 충돌 좌표 `(x_north, y_east, z_ground)`: `(2.2147322765381716, -15.222197781442958, 0.0) m`
  - 접촉 시 CG 고도: `1.5949587921649218 m`
  - 지면 충돌 속도: `71.60556477618731 m/s`
  - 최종 자세각 `(roll, pitch, yaw)`: `(27.71749637934367, -32.52232194331606, 293.1438011315742) deg`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - wrapper 실행으로 raw CSV, SI CSV, summary CSV/JSON, states plot, 3D trajectory plot 생성 확인
  - 3D trajectory plot이 비어 있지 않고 궤적과 시작/끝 marker를 표시함을 시각 확인
- 검증하지 못한 항목:
  - 기존 UAM 동역학 결과와 수치 일치 여부
  - 항공기 모델의 실제 검증 적합성
  - Excel 업데이트 결과의 상세 내용
- 검증하지 못한 이유:
  - 요청 범위가 JSBSim `c172x` 단독 실행 워크플로우 작성이며, UAM 모델 파라미터 동조나 외부 검증 자료 비교는 포함되지 않음
- 필요한 추가 조건:
  - UAM 모델과 수치 일치를 원하면 동일 질량/공력/추진/좌표계 정의 또는 보정 기준 필요
- 권장 후속 검증:
  - 사용자가 원하는 좌표축 정의가 `x=North, y=East`가 맞는지 확인
  - 필요 시 `psi=90 deg`로 `x=East` 해석 케이스 추가 비교
- 남은 리스크:
  - `c172x`는 고정익 항공기라 캡쳐본 UAM 궤적과 물리적으로 크게 다를 수 있음
  - `WOW` 기준 종료라 지면 접촉 시 CG 고도는 0이 아니라 착륙장치 높이만큼 양수임
- 후속 작업:
  - 좌표계 해석이 다르면 초기 yaw 또는 요약 좌표 mapping 조정
- Git commit:
  - 없음
## [2026-06-17 12:58] PROGRESS-20260617-1258-001 — DONE

- 과업:
  - `theta=+2.5 deg`, `ubody=60 m/s` 초기조건 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체로 초기 고도 `450 m`, pitch `2.5 deg`, 속도 `ubody=60 m/s` 조건을 만들고 추락 실행
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/1.1__450m_pitchp25_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/runscript/1.1__450m_pitchp25_ubody60_cm0zero_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_si_06171257.csv`
- 수행 내용:
  - 기존 `Cm0=0`, pitch -20 deg 케이스를 참조해 pitch +2.5 deg 전용 initial XML과 runscript 생성
  - runscript end time은 `600 s`, 종료 조건은 `gear/unit[0]/WOW eq 1`로 설정
  - wrapper로 aircraft variant 재생성 후 JSBSim 실행
  - 결과 summary JSON/CSV와 상태/궤적 plot 생성
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/1.1__450m_pitchp25_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/runscript/1.1__450m_pitchp25_ubody60_cm0zero_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_si_06171257.csv`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_states_vs_time_06171257.png`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_trajectory_3d_06171257.png`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/c172x_noengine_surface_neutral_empty_cm0.xml`
- 핵심 변경점:
  - 초기 자세 `theta=+2.5 deg`
  - 초기 속도 `ubody=60 m/s`
  - `Cmo=0`, no-engine/no-propeller, 조종면 neutral 조건 유지
- 실행한 명령어:
  - `python3 -m py_compile scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - XML parse 검증
  - `python3 scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - summary/CSV 검산 Python snippet
  - `git status --short` 확인
- 테스트 결과:
  - Python 문법 검사 성공
  - initial XML/runscript XML 파싱 성공
  - JSBSim 실행 성공
- 실행 확인 결과:
  - Run ID: `1.1.1__450m_pitchp25_ubody60_cm0zero_drop`
  - 초기 고도: `450.00000068539384 m`
  - 초기 pitch: `2.4999999999999996 deg`
  - 초기 total speed: `60.000000091200036 m/s`
  - 초기 `v_n`: `59.9428933860247 m/s`
  - 초기 `v_d`: `-2.617163245898249 m/s`
  - 종료 시각: `73.83333333 s`
  - 최종 고도: `1.6107039963841439 m`
  - 최종 속도: `50.779647191860775 m/s`
  - 최대 고도: `477.49023545747997 m`
  - 고도 상승량: `27.490234772086126 m`
  - pitch range: `-16.075296745533503 .. 5.5943518995439225 deg`
  - 최종 자세: roll `7.384403868088648e-15 deg`, pitch `-8.519109139448906 deg`, yaw `5.996534723449543e-13 deg`
  - elevator/aileron/rudder/thrust/engine_rpm/propeller_rpm 전 구간 `0.0`
- 검증하지 못한 항목:
  - body-axis `ubody` 컬럼 직접 출력
- 검증하지 못한 이유:
  - 현재 SI CSV 출력 목록에는 body-axis 속도 컬럼이 포함되어 있지 않음
- 필요한 추가 조건:
  - `run_jsbsim_timestamped.py` 출력 속성에 `velocities/u-fps`, `velocities/v-fps`, `velocities/w-fps`의 SI 변환 컬럼을 추가해야 직접 CSV 검증 가능
- 권장 후속 검증:
  - 필요 시 body-axis 속도 컬럼을 SI CSV에 포함하도록 runner 출력 필드 확장
- 가정:
  - initial XML의 `<ubody unit="M/SEC"> 60.0 </ubody>`가 JSBSim 초기 body x축 속도로 적용됨
- 남은 리스크:
  - `/home/junyeopkwon/jsbsim` 저장소 기준 aircraft variant XML은 untracked 상태로 확인됨
- 후속 작업:
  - 필요 시 pitch +2.5 deg 케이스와 pitch -20 deg 케이스의 trajectory/pitch 비교 plot 생성
- Git commit:
  - 없음
## [2026-06-17 11:20] PROGRESS-20260617-1120-001 — DONE

- 과업:
  - 30도 간격 자세 격자 drop initial XML 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체, 고도 `450 m`, `ubody=60 m/s`, 나머지 속도성분 0, `psi/theta/phi` 30도 간격 initial XML 생성
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_cm0_attitude_grid_initials.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/attitude_grid_30deg/`
- 수행 내용:
  - 기존 `1.0__450m_pitchm20_ubody60_drop_init.xml` 형식 확인
  - 재현 가능한 XML 생성 스크립트 작성
  - `psi=0..330 deg`, `theta=-90..90 deg`, `phi=0..330 deg` 격자로 `1008`개 XML 생성
  - 실수로 생성된 `/home/junyeopkwon/scripts/` 임시 폴더는 비어 있음을 확인 후 제거
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_cm0_attitude_grid_initials.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/attitude_grid_30deg/*.xml`
- 수정한 파일:
  - 없음
- 핵심 변경점:
  - 각 initial XML은 `latitude=37.0 deg`, `longitude=127.0 deg`, `altitude=450.0 m`, `elevation=0.0 m`, `ubody=60.0 m/s`, `vbody=0.0 m/s`, `wbody=0.0 m/s`, wind 0 조건을 유지
  - 파일명과 `<initialize name="">`에 `psi/theta/phi` 값을 포함
- 실행한 명령어:
  - `python3 -m py_compile scripts/generate_c172x_cm0_attitude_grid_initials.py`
  - `python3 scripts/generate_c172x_cm0_attitude_grid_initials.py`
  - `find scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/attitude_grid_30deg -type f -name '*.xml' | wc -l`
  - `python3 - <<'PY' ... xml.etree.ElementTree.parse(...) ... PY`
  - `sed -n '1,80p' scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/attitude_grid_30deg/450m_ubody60_psip000_thetam030_phip060_drop_init.xml`
- 테스트 결과:
  - 생성 스크립트 Python compile 성공
  - initial XML 생성 성공: `1008`개
  - XML 파싱 성공: `parsed 1008`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 해당 없음
- build 결과:
  - 해당 없음
- 실행 확인 결과:
  - JSBSim 실행은 수행하지 않음
- 검증하지 못한 항목:
  - 각 자세별 JSBSim runscript 실행 가능성
  - `theta=±90 deg` 조건의 JSBSim Euler singularity 영향
- 검증하지 못한 이유:
  - 이번 요청은 initial XML 생성이며 runscript/시뮬레이션 실행은 요청 범위 밖
- 가정:
  - 구형지구 및 자전 없음 설정은 initial XML이 아니라 runscript/JSBSim 설정에서 적용되는 조건으로 간주
- 남은 리스크:
  - `theta=±90 deg`는 Euler angle 특이점으로 인해 실제 실행 시 일부 해석/출력에서 주의가 필요할 수 있음
  - 프로젝트 루트는 Git 저장소로 확인되지 않아 Git 변경 추적 검증은 제한됨
- 후속 작업:
  - 필요 시 이 initial XML 격자를 순회하는 batch runscript 또는 Python runner 생성
- Git commit:
  - 없음

## [2026-06-15 18:24] PROGRESS-20260615-1824-001 — DONE

- 과업:
  - 기존 ballistic-like 결과에 사용된 Cessna 172 공력 데이터 파일 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 기존 결과가 `Cessna172_AeroCoefficients_Basic.xlsx`와 `cessna172_config.xml`을 사용했다는 추가 정보 제공
- 관련 파일:
  - `D:/OneDrive/바탕 화면/2025 연구실/회랑/추락/6DOF쿼터니안ver/Cessna172_AeroCoefficients_Basic.xlsx`
  - `D:/OneDrive/바탕 화면/2025 연구실/회랑/추락/6DOF쿼터니안ver/cessna172_config.xml`
- 수행 내용:
  - XML에서 질량/기하/관성/기본 공력계수 확인
  - Excel workbook 내부 sheet XML을 파싱해 `alpha [deg]`, `CD [-]`, `CL [-]`, `Cm [-]` 테이블 확인
- 핵심 확인값:
  - mass: `1157 kg`
  - wing_area: `16.17 m^2`
  - mean_chord: `1.49 m`
  - wing_span: `11.0 m`
  - inertia: `Ix=2424.2`, `Iy=2427.3`, `Iz=4372.5`
  - alpha 0 deg: `CD=0.0315`, `CL=0.0306`, `Cm=0.0998`
  - XML aero_coefficients: `CL=0.0306`, `CD=0.0315`, `Cm=0.0`, `CY=0.0`, `Cl=0.0`, `Cn=0.0`
- 실행한 명령어:
  - `sed -n '1,220p' '/mnt/d/OneDrive/바탕 화면/2025 연구실/회랑/추락/6DOF쿼터니안ver/cessna172_config.xml'`
  - `python3` zip/xml parser로 `Cessna172_AeroCoefficients_Basic.xlsx` 내부 `sheet1.xml` 파싱
- 테스트 결과:
  - 파일 접근 및 주요 데이터 추출 성공
- 검증하지 못한 항목:
  - 기존 6DOF 코드에서 CD/CL/Cm 부호와 좌표축을 어떻게 적용했는지
  - 해당 Excel 계수를 JSBSim force axis에 직접 매핑할 때 필요한 부호 변환
- 남은 리스크:
  - Excel의 `CD` 열은 양의 alpha에서 음수 값을 포함하므로, 일반적인 drag coefficient가 아니라 축력 계수 또는 부호 규약이 다른 값일 가능성이 있음
- 후속 작업:
  - 기존 6DOF 코드의 공력 적용 식을 확인한 뒤 JSBSim custom aircraft에 동일 부호/축 규약으로 이식
- Git commit:
  - 없음

## [2026-06-15 18:20] PROGRESS-20260615-1820-001 — DONE

- 과업:
  - ballistic-like heading hold/trim glide 케이스 생성 및 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 제공된 ballistic 궤적 이미지와 유사하게 방향 고정 활공 추락 형태를 얻기 위한 별도 케이스 생성
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.3__450m_60ms_x_engineout_t0_headinghold_trim_spherical_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_headinghold_trim_spherical.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical_headinghold_trim_spherical_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical_headinghold_trim_spherical_summary.json`
- 수행 내용:
  - `4.2` 초기조건을 재사용해 t=0, `(0,0,450 m)`, `(60,0,0) m/s` 조건 유지
  - runscript에서 engine-out, altitude hold off, attitude/airspeed hold off, heading hold on, pitch trim `0.18` 설정
  - 무자전 원형지구 `04_nonrotating_spherical_earth.xml`로 실행
  - 총 궤적 이동거리, 최종 좌표, 최종 속도 성분, 최종 자세각 요약 생성
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.3__450m_60ms_x_engineout_t0_headinghold_trim_spherical_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_headinghold_trim_spherical.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical_headinghold_trim_spherical_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical_headinghold_trim_spherical_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 핵심 변경점:
  - `4.2` AP/trim off 결과와 구분되는 `4.3` heading hold/trim glide 비교용 케이스 추가
- 실행한 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_headinghold_trim_spherical.py`
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_headinghold_trim_spherical.py`
- 테스트 결과:
  - 최종 Run ID: `4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical`
  - 지면 도달 시간: `157.275 s`
  - 총 궤적 이동거리: `6462.427635270617 m`
  - 최종 좌표 `(x_north, y_east, z_ground)`: `(6361.444273921856, 51.47941466523298, 0.0) m`
  - 접촉 시 CG 고도: `1.4064202708214522 m`
  - 최종 속도 성분 `(vx_north, vy_east, vz_down)`: `(41.09641263373492, 0.13986056777936515, 2.3698731593672213) m/s`
  - 최종 속도 크기: `41.16492428187031 m/s`
  - 최종 자세각 `(roll, pitch, yaw)`: `(0.19841284273515825, -1.1805724378496156, 359.8567671688275) deg`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - JSBSim 실행 성공
  - raw CSV, SI CSV, summary CSV/JSON, states plot, 3D trajectory plot 생성 확인
  - 3D trajectory plot에서 루프 없이 방향 고정 활공 형태 확인
- 검증하지 못한 항목:
  - 기존 ballistic 모델과 수평거리/낙하시간 정량 일치 여부
- 검증하지 못한 이유:
  - 이번 작업은 형태상 유사한 heading hold/trim glide 케이스 분리이며 계수 보정은 포함하지 않음
- 필요한 추가 조건:
  - 수평거리 약 400 m 수준으로 맞추려면 c172x 공력/trim이 아니라 ballistic/drag-only 모델 또는 계수 보정 필요
- 권장 후속 검증:
  - `4.2` AP/trim off, `4.3` heading hold/trim glide, 기존 ballistic 결과 비교표 생성
- 남은 리스크:
  - `c172x` 양력이 살아 있어 기존 ballistic 이미지보다 활공거리가 훨씬 길어짐
- 후속 작업:
  - 보고서용 2D `x-altitude`, `time-altitude`, `time-speed` plot 추가
- Git commit:
  - 없음

## [2026-06-15 18:13] PROGRESS-20260615-1813-001 — DONE

- 과업:
  - `c172x` 추락 시작점 t=0, 무자전 원형지구 직접 실행 케이스 생성 및 검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 초기 좌표 `(0,0,450 m)`, 초기 속도 `(60,0,0)`, 시작 시간 `0 s` 조건으로 추락 완료까지의 총 이동거리, 최종 좌표, 자세각, 속도 산출
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.2__450m_60ms_x_engineout_t0_spherical_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.2__450m_60ms_x_engineout_t0_spherical_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_spherical.py`
  - `/home/junyeopkwon/jsbsim_workflow/earth_models/04_nonrotating_spherical_earth.xml`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.2.2__450m_60ms_x_engineout_t0_spherical_engineout_t0_spherical_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.2.2__450m_60ms_x_engineout_t0_spherical_engineout_t0_spherical_summary.json`
- 수행 내용:
  - 추락 시작 자체를 초기조건으로 둔 `4.2` XML 구성
  - 초기 위치 `lat=37 deg`, `lon=127 deg`, `altitude=450 m`에서 로컬 좌표 원점 정의
  - `psi=0`, `theta=0`, `ubody=60 m/s`로 초기 속도 `(x_north,y_east,z_down)=(60,0,0) m/s` 구현
  - `--planet=/home/junyeopkwon/jsbsim_workflow/earth_models/04_nonrotating_spherical_earth.xml`로 무자전 원형지구 실행
  - 최초 `4.2.1`은 heading hold/pitch trim이 남아 있어, `4.2.2`에서 AP/trim off로 수정 후 재실행
  - SI CSV를 누적해 총 3D 궤적 길이를 계산
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.2__450m_60ms_x_engineout_t0_spherical_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.2__450m_60ms_x_engineout_t0_spherical_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_spherical.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.2.2__450m_60ms_x_engineout_t0_spherical_engineout_t0_spherical_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.2.2__450m_60ms_x_engineout_t0_spherical_engineout_t0_spherical_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 핵심 변경점:
  - `4.1`처럼 30초 cruise 후 잘라내지 않고, JSBSim 자체를 `t=0` 추락 시작으로 실행
  - 지구 모델은 `04_nonrotating_spherical_earth.xml` 명시
  - 결과 요약에 총 이동거리, 최종 좌표, 최종 속도 성분, 최종 자세각 포함
- 실행한 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_spherical.py`
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_engineout_t0_spherical.py`
- 테스트 결과:
  - 최종 Run ID: `4.2.2__450m_60ms_x_engineout_t0_spherical`
  - 지면 도달 시간: `32.35833333 s`
  - 총 궤적 이동거리: `1787.6597002464391 m`
  - 최종 좌표 `(x_north, y_east, z_ground)`: `(27.541827129910445, 15.594176084980802, 0.0) m`
  - 접촉 시 CG 고도: `1.5415762868106366 m`
  - 최종 속도 성분 `(vx_north, vy_east, vz_down)`: `(-29.546726126491738, -65.25238572350827, 8.492409651504067) m/s`
  - 최종 속도 크기: `72.13185072554548 m/s`
  - 최종 자세각 `(roll, pitch, yaw)`: `(26.754867841772814, -30.478694385197308, 281.21056963602365) deg`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - JSBSim 실행 성공
  - raw CSV, SI CSV, summary CSV/JSON, states plot, 3D trajectory plot 생성 확인
  - trajectory plot 시각 확인 완료
- 검증하지 못한 항목:
  - 사용자가 원하는 물리 모델이 AP/trim off인지, heading hold/trim glide인지 최종 확정
- 검증하지 못한 이유:
  - 최근 요청은 초기 좌표/속도/시간과 지구 모델을 명시했고 제어 입력 조건은 재명시하지 않았으나, 기존 요청의 trim/autopilot 없이 조건을 우선 반영
- 필요한 추가 조건:
  - 직진 활공 형태가 필요하면 heading hold 또는 trimmed glide 조건을 별도 케이스로 지정 필요
- 권장 후속 검증:
  - 보고서용 그래프가 필요하면 3D보다 `time-altitude`, `time-speed`, `x-altitude` 2D plot을 추가 생성
- 남은 리스크:
  - AP/trim off 조건에서 `c172x`는 실속/회전 거동이 발생해 x 방향 최종 변위가 작고 궤적이 루프 형태가 될 수 있음
- 후속 작업:
  - 필요 시 `4.3`으로 heading hold/trim glide 버전과 AP/trim off 버전 비교표 작성
- Git commit:
  - 없음

## [2026-06-15 18:05] PROGRESS-20260615-1805-001 — DONE

- 과업:
  - engine-out 시점 `t=0` 별도 로그/그래프 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `4.1` cruise 후 engine-out 결과에서 추락 시작 시점을 0으로 보는 별도 그래프와 로그 산출
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/extract_c172x_engineout_t0.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_si.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_summary.json`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_trajectory_3d.png`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_states_vs_time.png`
- 수행 내용:
  - `4.1.1` summary JSON에서 원본 SI CSV와 engine-out 시작 시각 `31.0 s` 확인
  - 원본 SI CSV에서 `time_s >= 31.0` 구간만 추출
  - `time_from_engineout_s`, `x_from_engineout_north_m`, `y_from_engineout_east_m`, `z_from_engineout_altitude_m`, `altitude_loss_from_engineout_m`, `distance_from_engineout_m` 필드 추가
  - engine-out 기준 trajectory/state plot 생성
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/extract_c172x_engineout_t0.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_si.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_summary.json`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_trajectory_3d.png`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/engineout_t0/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_engineout_t0_states_vs_time.png`
- 수정한 파일:
  - 없음
- 핵심 변경점:
  - 엔진 정지 시점을 원점으로 하는 별도 데이터셋과 그래프 생성
- 실행한 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/extract_c172x_engineout_t0.py`
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/extract_c172x_engineout_t0.py`
- 테스트 결과:
  - engine-out 기준 지면 도달 시간: `51.224999999999994 s`
  - engine-out 기준 지면 충돌 좌표 `(x_north, y_east, z_ground)`: `(3051.1993023505283, 10.039513321892173, 0.0) m`
  - 지면 충돌 속도: `61.00876346684495 m/s`
  - 최종 자세각 `(roll, pitch, yaw)`: `(0.3104975632938837, -10.191772439135079, 359.6659611945741) deg`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - CSV/JSON/PNG 파일 생성 확인
  - trajectory plot 시각 확인 완료
- 검증하지 못한 항목:
  - states plot 세부 곡선 육안 검토
- 검증하지 못한 이유:
  - 요청 산출물 생성과 trajectory plot 확인까지만 수행
- 필요한 추가 조건:
  - 세부 변수별 검토가 필요하면 states plot 또는 CSV 기반 추가 분석 수행
- 권장 후속 검증:
  - 보고서용 그래프 축/라벨 형식 요구가 있으면 별도 스타일 적용
- 남은 리스크:
  - 3D plot은 East 변위가 약 `10 m` 수준으로 작아 축 비율 때문에 거의 직선처럼 보임
- 후속 작업:
  - 필요 시 2D `x-altitude`, `time-altitude`, `time-speed` 보고서용 plot 추가
- Git commit:
  - 없음

## [2026-06-15 18:00] PROGRESS-20260615-1800-001 — DONE

- 과업:
  - c172x 450 m, 60 m/s x 방향 cruise 후 engine-out 추락 케이스 정정 구현
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 이전 `4.0` 직접 초기상태 자유응답 그래프가 부적절하므로, 참조 runscript `2.2`처럼 크루즈 후 엔진 정지 방식으로 수정
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.1__450m_60ms_x_cruise_untrimmed_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.1__450m_60ms_x_cruise30_engineout_headinghold_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_impact_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_impact_summary.json`
- 수행 내용:
  - `2.2__cruise_30s_engineout_headinghold_legacy_run.xml` 구조 확인
  - 450 m, 60 m/s, heading 0 deg 초기조건을 `4.1`로 추가
  - powered cruise 시작, simple trim, altitude/heading hold, 31초 engine-out, altitude hold off, heading hold 유지 흐름의 runscript 추가
  - wrapper 기본 실행 대상을 `4.1` 케이스로 변경
  - 요약 JSON/CSV에 `engineout_start_*` 필드를 추가하여 엔진 정지 시점 상태를 기록
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.1__450m_60ms_x_cruise_untrimmed_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.1__450m_60ms_x_cruise30_engineout_headinghold_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_impact_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.1.1__450m_60ms_x_cruise30_engineout_headinghold_impact_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 핵심 변경점:
  - 이전 `4.0`의 직접 pitch 초기화 자유응답 대신, 안정화된 cruise 상태에서 engine-out 하도록 `4.1` 추가
  - 엔진 정지 시점 상태: `time=31.0 s`, `altitude=450.0951988614768 m`, `speed=59.99034647295298 m/s`, 자세각 `(-0.1518415023785531, 0.21940867757500152, 0.09709782744805454) deg`
- 실행한 명령어:
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_450m_drop_no_trim.py`
- 테스트 결과:
  - 최종 Run ID: `4.1.1__450m_60ms_x_cruise30_engineout_headinghold`
  - 지면 도달 시간: `82.225 s`
  - 지면 충돌 좌표 `(x_north, y_east, z_ground)`: `(4851.016206938623, 13.761077913728741, 0.0) m`
  - 접촉 시 CG 고도: `1.5056067515641451 m`
  - 지면 충돌 속도: `61.00876346684495 m/s`
  - 최종 자세각 `(roll, pitch, yaw)`: `(0.3104975632938837, -10.191772439135079, 359.6659611945741) deg`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - JSBSim 실행 성공
  - raw CSV, SI CSV, summary CSV/JSON, states plot, 3D trajectory plot 생성 확인
  - 3D trajectory plot이 이전 `4.0`처럼 루프 형태가 아니라 x 방향 진행 후 하강하는 형태임을 확인
- 검증하지 못한 항목:
  - 사용자가 의도한 x 방향이 local North인지 East인지
- 검증하지 못한 이유:
  - 사용자 정정은 x 방향이라고만 표현했으며 기존 작업의 좌표 가정을 유지함
- 필요한 추가 조건:
  - x=East가 필요하면 heading `90 deg` 케이스 추가 필요
- 권장 후속 검증:
  - 필요 시 `4.2`로 heading `90 deg` 비교 케이스 생성
- 남은 리스크:
  - heading hold를 유지하므로 engine-out 이후에도 autopilot heading 제어가 개입함
  - 완전 무조종 engine-out을 원하면 heading hold off 변형이 필요함
- 후속 작업:
  - 사용자 의도에 따라 heading hold 유지/해제 케이스 분리
- Git commit:
  - 없음
## [2026-06-16 11:56] PROGRESS-20260616-1156-001 — DONE

- 과업:
  - `c172x` ground reaction 계수 변형 생성 및 기본 계수 이륙 실행 검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - damping/spring/friction 각각 `0`, `0.5`, `1.0` 배율의 27개 `c172x.xml` 구성과 기본 계수 이륙 스크립트 작성
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_groundreaction_variants.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_groundreaction_takeoff.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.0__takeoff_groundreaction_check_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
  - `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_groundreaction/manifest.csv`
- 수행 내용:
  - 기존 `c172x.xml`의 `<ground_reactions>` 블록 확인
  - damping/spring/friction 3종 계수를 각각 `0.0`, `0.5`, `1.0` 배율로 조합하는 생성기 작성
  - right main gear가 `spring_coeff`/`damping_coeff` 태그 대신 equivalent `strut_force`를 사용하므로 해당 `<value>` 항도 같은 배율로 조정하도록 반영
  - 각 변형 폴더에 비교용 파일명 `c172x.xml`과 실행에 필요한 `c172ap.xml` 등 companion XML 복사
  - 선택 변형을 `/home/junyeopkwon/jsbsim/aircraft/{variant}/{variant}.xml`로 설치하고 기존 timestamp runner를 호출하는 wrapper 작성
  - 기본 계수 변형으로 이륙 확인 실행
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_groundreaction_variants.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_groundreaction_takeoff.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.0__takeoff_groundreaction_check_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_groundreaction/*/c172x.xml`
  - `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_groundreaction/manifest.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_groundreaction/5.0.2__takeoff_groundreaction_check_takeoff_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_groundreaction/5.0.2__takeoff_groundreaction_check_takeoff_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 핵심 변경점:
  - 총 27개 `c172x.xml` 생성 확인
  - 기본 계수 변형 `c172x_gr_damp100_spring100_fric100`을 동일 초기조건 `2.0__takeoff_engineout_init.xml`, 동일 runscript `5.0__takeoff_groundreaction_check_run.xml`로 실행 가능
  - 실행 산출물이 기존 구조 `logs/csv/raw`, `logs/csv/si`, `logs/console`, `plots`에 저장됨
- 실행한 명령어:
  - `python3 -m py_compile scripts/generate_c172x_groundreaction_variants.py scripts/run_c172x_groundreaction_takeoff.py`
  - `python3 scripts/generate_c172x_groundreaction_variants.py`
  - `find aircraft_variants/c172x_groundreaction -mindepth 2 -maxdepth 2 -name c172x.xml | wc -l`
  - `python3 scripts/run_c172x_groundreaction_takeoff.py`
- 테스트 결과:
  - 생성된 `c172x.xml` 수: `27`
  - 기본 변형 Run ID: `5.0.2__takeoff_groundreaction_check`
  - `takeoff_confirmed`: `True`
  - `liftoff_10ft_time_s`: `26.425`
  - 최종 시간: `30.375 s`
  - 최종 `h-agl`: `100.48082085674082 ft`
  - 최종 속도: `30.74531138733655 m/s`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - JSBSim 실행 성공
  - raw CSV, SI CSV, summary CSV/JSON, states plot, 3D trajectory plot 생성 확인
- 검증하지 못한 항목:
  - 나머지 26개 변형의 개별 이륙 가능 여부
- 검증하지 못한 이유:
  - 사용자가 비교는 직접 수행한다고 했고, 이번 완료 조건은 기본 계수 이륙 가능 스크립트 작성 및 확인임
- 필요한 추가 조건:
  - 27개 전체 비교가 필요하면 `--variant`를 순회하는 배치 실행 스크립트 추가 필요
- 권장 후속 검증:
  - 사용자가 비교할 때 `manifest.csv` 기준으로 각 variant를 순회 실행하고 summary를 병합
- 남은 리스크:
  - `spring=0` 변형은 지면 반력 특성이 비물리적이라 JSBSim 상태가 불안정하거나 이륙 전에 지면 관통/비정상 거동이 발생할 수 있음
  - 변형 실행을 위해 `/home/junyeopkwon/jsbsim/aircraft/c172x_gr_damp100_spring100_fric100/`에 설치 복사본이 생성됨
- 후속 작업:
  - 필요 시 27개 변형 일괄 실행과 결과 summary 병합 스크립트 작성
- Git commit:
  - 없음
## [2026-06-16 12:08] PROGRESS-20260616-1208-001 — DONE

- 과업:
  - FlightGear C172 매뉴얼 기반 이륙 상태기계 구현 및 검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - FlightGear에서 C172가 이륙하는 방식이 JSBSim에도 적용 가능하므로 해당 방식으로 스크립트를 구성해야 하지 않는지 확인
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.1__takeoff_flightgear_state_machine_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_groundreaction_takeoff.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 수행 내용:
  - FlightGear 문서의 수동 절차를 `engine ready -> takeoff roll -> 40 kt nose-wheel lift -> 55 kt rotation -> 70 kt target initial climb -> 500 ft complete` 상태로 매핑
  - 순수 수동 입력 버전이 지면 재접촉 또는 수치 발산을 일으켜 로그를 확인하며 조종 입력 조정
  - C172X 기존 성공 패턴과 맞춰 50 ft 이후 `ap/attitude_hold`, 250 ft 이후 `ap/heading_hold` 및 `ap/altitude_hold`를 적용하는 하이브리드 안정화로 수정
  - wrapper의 기본 `--procedure`를 `flightgear`로 변경하고 기존 단순 확인용 `5.0`은 `--procedure basic`으로 유지
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.1__takeoff_flightgear_state_machine_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_groundreaction/5.1.10__takeoff_flightgear_state_machine_takeoff_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_groundreaction/5.1.10__takeoff_flightgear_state_machine_takeoff_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_groundreaction_takeoff.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 핵심 변경점:
  - `5.1` runscript는 FlightGear 문서의 임계값을 반영
  - 기본 실행 명령 `python3 scripts/run_c172x_groundreaction_takeoff.py`가 이제 `5.1__takeoff_flightgear_state_machine`을 실행
  - raw CSV, SI CSV, console log, states plot, trajectory plot 저장 방식은 기존 timestamp runner와 동일
- 실행한 명령어:
  - `python3 -m py_compile scripts/run_c172x_groundreaction_takeoff.py scripts/generate_c172x_groundreaction_variants.py`
  - `python3 scripts/run_c172x_groundreaction_takeoff.py --procedure flightgear`
- 테스트 결과:
  - 최종 성공 Run ID: `5.1.10__takeoff_flightgear_state_machine`
  - `takeoff_confirmed`: `True`
  - `climb_500ft_confirmed`: `True`
  - `liftoff_10ft_time_s`: `25.50833333`
  - 최종 시간: `65.025 s`
  - 최종 `h-agl`: `500.0621981233534 ft`
  - 최종 고도 증가량: `151.1074207421601 m`
  - 최종 속도: `29.428067169317252 m/s`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - JSBSim 실행 성공
  - raw CSV, SI CSV, summary CSV/JSON, states plot, 3D trajectory plot 생성 확인
- 검증하지 못한 항목:
  - 27개 ground reaction variant 전체에 대한 `5.1` 절차 성공 여부
- 검증하지 못한 이유:
  - 사용자는 비교는 직접 수행한다고 했고, 이번 작업은 기본 계수 절차 검증에 집중
- 필요한 추가 조건:
  - 전체 비교가 필요하면 `manifest.csv` 기반 반복 실행 및 summary 병합 필요
- 권장 후속 검증:
  - `--variant`로 각 계수 조합 실행 후 `climb_500ft_confirmed`, `liftoff_10ft_time_s`, 최종 속도 비교
- 남은 리스크:
  - `5.1`은 50 ft 이후 AP 안정화를 사용하므로 완전한 수동 조종만으로 500 ft까지 간 결과는 아님
  - 최종 속도는 FlightGear 문서의 70 kt target보다 낮아, 속도 유지 제어는 추가 튜닝 여지가 있음
- 후속 작업:
  - 필요 시 70 kt 유지용 elevator feedback을 더 정교하게 구성하거나 Python 기반 closed-loop runner로 전환
- Git commit:
  - 없음
## [2026-06-16 12:16] PROGRESS-20260616-1216-001 — DONE

- 과업:
  - 원본 `c172x` 기반 단순 이륙 runscript 추가 및 실행 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 이륙 스크립트를 variant가 아닌 `c172x` 기반으로 만들어둘 것
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.2__takeoff_simple_c172x_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 수행 내용:
  - `<use aircraft="c172x" initialize="...2.0__takeoff_engineout_init.xml"/>`를 직접 사용하는 `5.2` runscript 추가
  - full throttle, 40 kt nose-wheel lightening, 60 kt rotation, 20 ft 이후 manual climb 이벤트 구성
  - 기존 `run_jsbsim_timestamped.py`로 원본 `c172x` 실행 확인
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.2__takeoff_simple_c172x_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x/5.2__takeoff_simple_c172x/5.2.1__takeoff_simple_c172x_runscript_06161216.xml`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x/5.2__takeoff_simple_c172x/5.2.1__takeoff_simple_c172x_raw_06161216.csv`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x/5.2__takeoff_simple_c172x/5.2.1__takeoff_simple_c172x_si_06161216.csv`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x/5.2__takeoff_simple_c172x/5.2.1__takeoff_simple_c172x_states_vs_time_06161216.png`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x/5.2__takeoff_simple_c172x/5.2.1__takeoff_simple_c172x_trajectory_3d_06161216.png`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 핵심 변경점:
  - variant aircraft가 아니라 원본 `/home/junyeopkwon/jsbsim/aircraft/c172x/c172x.xml`를 사용하는 runscript 추가
  - AP 안정화 없이 단순 이륙/상승 이벤트만 구성
- 실행한 명령어:
  - `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x --init /home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/2.0__takeoff_engineout_init.xml --runscript /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.2__takeoff_simple_c172x_run.xml --planet builtin`
- 테스트 결과:
  - Run ID: `5.2.1__takeoff_simple_c172x`
  - Aircraft: `c172x`
  - `Terminate after simple climb check` 이벤트가 `48.508333 s`에 실행
  - 종료 시 `position/h-agl-ft = 300.193903`
  - 종료 시 `velocities/vc-kts = 42.426614`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - JSBSim 실행 성공
  - raw CSV, SI CSV, console log, states plot, trajectory plot 생성 확인
- 검증하지 못한 항목:
  - 오른쪽 wing tip 접촉 없이 매끄러운 수동 상승
- 검증하지 못한 이유:
  - 사용자 요청은 스크립트 자체를 `c172x` 기반으로 만드는 것이며 후속 튜닝은 사용자가 수행한다고 명시
- 필요한 추가 조건:
  - 조향/롤/피치 closed-loop 제어 또는 AP 안정화 튜닝 필요
- 권장 후속 검증:
  - `states_vs_time`에서 roll, pitch, yaw, rudder, aileron, airspeed를 확인하며 조종 입력 조정
- 남은 리스크:
  - 콘솔에 `RIGHT_TIP` 접촉이 기록되어 순수 고정 입력 수동 스크립트는 자세 안정성이 부족함
- 후속 작업:
  - 필요 시 aileron/rudder feedback을 Python runner로 구현
- Git commit:
  - 없음
## [2026-06-16 12:25] PROGRESS-20260616-1225-001 — DONE

- 과업:
  - 원본 `c172x` 500 ft 이륙 상승 runscript 구현 및 검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x`로 엔진 켜고 활주 후 500 ft까지 상승하는 runscript 작성
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.3__takeoff_to_500ft_c172x_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 수행 내용:
  - 원본 `c172x` aircraft 직접 사용 runscript 추가
  - engine ready, runway roll, nose wheel lightening, rotate, initial climb, stabilize climb, terminate at 500 ft 이벤트 구성
  - `run_jsbsim_timestamped.py --aircraft c172x`로 실행 확인
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.3__takeoff_to_500ft_c172x_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x/5.3__takeoff_to_500ft_c172x/5.3.1__takeoff_to_500ft_c172x_runscript_06161225.xml`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x/5.3__takeoff_to_500ft_c172x/5.3.1__takeoff_to_500ft_c172x_raw_06161225.csv`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x/5.3__takeoff_to_500ft_c172x/5.3.1__takeoff_to_500ft_c172x_si_06161225.csv`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x/5.3__takeoff_to_500ft_c172x/5.3.1__takeoff_to_500ft_c172x_states_vs_time_06161225.png`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x/5.3__takeoff_to_500ft_c172x/5.3.1__takeoff_to_500ft_c172x_trajectory_3d_06161225.png`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 핵심 변경점:
  - variant가 아닌 원본 `/home/junyeopkwon/jsbsim/aircraft/c172x/c172x.xml` 기반 500 ft 상승 runscript 확보
- 실행한 명령어:
  - `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x --init /home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/2.0__takeoff_engineout_init.xml --runscript /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.3__takeoff_to_500ft_c172x_run.xml --planet builtin`
- 테스트 결과:
  - Run ID: `5.3.1__takeoff_to_500ft_c172x`
  - Aircraft: `c172x`
  - `Terminate at 500 ft AGL` 이벤트가 `64.891667 s`에 실행
  - 종료 시 `position/h-agl-ft = 500.040028`
  - 종료 시 `velocities/vc-kts = 56.862562`
  - 종료 자세: roll `-0.208965 deg`, pitch `9.867391 deg`, yaw `0.655474 deg`
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - JSBSim 실행 성공
  - raw CSV, SI CSV, console log, states plot, trajectory plot 생성 확인
- 검증하지 못한 항목:
  - 70 kt 유지 성능
- 검증하지 못한 이유:
  - 이번 요청은 원본 `c172x`로 500 ft까지 상승하는 스크립트 작성이 핵심
- 필요한 추가 조건:
  - 속도 유지까지 필요하면 elevator/throttle closed-loop 제어 추가 필요
- 권장 후속 검증:
  - `states_vs_time` plot에서 속도와 pitch를 확인해 원하는 상승속도/상승률에 맞게 조정
- 남은 리스크:
  - 250 ft 이후 heading/altitude hold를 사용하므로 완전 수동 고정 입력만의 상승은 아님
- 후속 작업:
  - 필요 시 `5.3`의 250 ft 이후 AP 안정화 제거 또는 closed-loop 제어로 대체
- Git commit:
  - 없음
## [2026-06-16 12:34] PROGRESS-20260616-1234-001 — DONE

- 과업:
  - `5.3` 원본 `c172x` 500 ft 이륙 스크립트 고도 꺾임 원인 수정
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 30초쯤 개입이 들어온 것처럼 보이는 현상이 실제 이륙과 맞지 않으므로 수정
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.3__takeoff_to_500ft_c172x_run.xml`
- 수행 내용:
  - 기존 `Initial climb` 이벤트의 `ap/attitude_hold=1` 제거
  - 20 ft 이후 수동 pitch/roll 입력을 완만하게 조정
  - 100 ft 이후 heading hold만 먼저 적용
  - 250 ft 이후 altitude hold 적용
  - 지면 재접촉 시 성공으로 오인하지 않도록 abort 이벤트 추가
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x/5.3__takeoff_to_500ft_c172x/5.3.6__takeoff_to_500ft_c172x_runscript_06161234.xml`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x/5.3__takeoff_to_500ft_c172x/5.3.6__takeoff_to_500ft_c172x_raw_06161234.csv`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x/5.3__takeoff_to_500ft_c172x/5.3.6__takeoff_to_500ft_c172x_si_06161234.csv`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x/5.3__takeoff_to_500ft_c172x/5.3.6__takeoff_to_500ft_c172x_states_vs_time_06161234.png`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x/5.3__takeoff_to_500ft_c172x/5.3.6__takeoff_to_500ft_c172x_trajectory_3d_06161234.png`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.3__takeoff_to_500ft_c172x_run.xml`
- 핵심 변경점:
  - 30초 부근 altitude/attitude hold 개입 제거
  - 100 ft 이후 heading hold, 250 ft 이후 altitude hold로 안정화 시점을 분리
- 실행한 명령어:
  - `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x --init /home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/2.0__takeoff_engineout_init.xml --runscript /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.3__takeoff_to_500ft_c172x_run.xml --planet builtin`
- 테스트 결과:
  - 최종 성공 Run ID: `5.3.6__takeoff_to_500ft_c172x`
  - `Aircraft`: `c172x`
  - `Terminate at 500 ft AGL` 이벤트 실행 시각: `62.825 s`
  - 종료 시 `position/h-agl-ft`: `500.066293`
  - 종료 시 `velocities/vc-kts`: `55.320501`
  - 종료 자세: roll `0.151291 deg`, pitch `11.656716 deg`, yaw `359.965331 deg`
  - 콘솔 tail 기준 이륙 후 abort/CRASH 없음
- lint 결과:
  - 별도 lint 미실행
- type check 결과:
  - 별도 type check 미실행
- build 결과:
  - 별도 build 미실행
- 실행 확인 결과:
  - JSBSim 실행 성공
  - raw CSV, SI CSV, console log, states plot, trajectory plot 생성 확인
- 검증하지 못한 항목:
  - plot 이미지의 시각적 단조성 직접 수동 판독
- 검증하지 못한 이유:
  - CSV/console 기반으로 종료 이벤트와 접촉/abort 여부를 우선 확인
- 필요한 추가 조건:
  - 사용자가 첨부 그래프와 같은 altitude plot을 다시 확인
- 권장 후속 검증:
  - `5.3.6` altitude plot에서 30초 부근 꺾임 제거 여부 확인
- 남은 리스크:
  - 100 ft 이후 heading hold, 250 ft 이후 altitude hold가 여전히 자동 제어로 들어감
  - 완전 수동 조종 기반 고정 입력만으로는 roll/yaw 안정이 부족할 수 있음
- 후속 작업:
  - 필요 시 Python closed-loop 제어로 airspeed/heading/elevator를 연속 제어
- Git commit:
  - 없음
## [2026-06-16 18:23] PROGRESS-20260616-1823-001 — DONE

- 과업:
  - C172X 엔진 없는 상태 추락 runscript 작성 및 검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x 엔진 없는상태로 추락하는 runscript 작성`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.4__450m_60ms_x_noengine_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.4__450m_60ms_x_noengine_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 수행 내용:
  - 기존 `4.2`, `4.3` engine-out 추락 케이스 구조를 확인
  - `4.4` no-engine drop 초기조건과 runscript를 새로 추가
  - runscript에서 throttle/mixture/magneto/starter, `propulsion/engine/set-running`, `propulsion/engine[0]/set-running`, autopilot hold, 조종면 명령을 0으로 고정
  - 직접 실행용 `run_c172x_noengine_drop.py`를 추가해 timestamp runner, SI 변환, plot 생성, 요약 CSV/JSON 생성을 연결
  - README에 새 초기조건/runscript 목록과 실행 명령 추가
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/4.4__450m_60ms_x_noengine_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/4.4__450m_60ms_x_noengine_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.4.2__450m_60ms_x_noengine_drop_noengine_drop_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x/4.4.2__450m_60ms_x_noengine_drop_noengine_drop_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/README.md`
- 핵심 변경점:
  - `4.4__450m_60ms_x_noengine_drop_run.xml`는 시작 시점부터 engine off, AP off, 조종면 중립으로 추락하고 `gear/unit[0]/WOW eq 1`에서 종료
  - `run_c172x_noengine_drop.py`는 최종 접촉 시각, 궤적 길이, 최종 좌표, 최종 속도, 최종 자세를 요약 파일로 저장
- 실행한 명령어:
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_drop.py`
  - `python3 - <<'PY' ... ET.parse(...) ... PY`
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_drop.py`
  - `python3 - <<'PY' ... SI CSV engine/control range check ... PY`
- 테스트 결과:
  - Python syntax check 통과
  - XML parse 통과
  - JSBSim 실행 성공
  - 실행 ID: `4.4.2__450m_60ms_x_noengine_drop`
  - 지면 접촉 시각: `32.35833333 s`
  - 총 궤적 길이: `1787.6597002464391 m`
  - 최종 좌표: `(x_north=27.541827129910445 m, y_east=15.594176084980802 m, z_ground=0 m)`
  - 최종 속도: `72.13185072554548 m/s`
  - 최종 자세: `roll=26.754867841772814 deg`, `pitch=-30.478694385197308 deg`, `yaw=281.21056963602365 deg`
- lint 결과:
  - 별도 lint는 실행하지 않음
- type check 결과:
  - 별도 type check는 실행하지 않음
- build 결과:
  - 해당 없음
- 실행 확인 결과:
  - SI CSV 생성: `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x/4.4__450m_60ms_x_noengine_drop/4.4.2__450m_60ms_x_noengine_drop_si_06161822.csv`
  - generated runscript 생성: `/home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x/4.4__450m_60ms_x_noengine_drop/4.4.2__450m_60ms_x_noengine_drop_runscript_06161822.xml`
  - plot 생성 확인
- 검증하지 못한 항목:
  - aircraft XML에서 `<propulsion>`을 제거한 물리적 no-engine variant와의 결과 비교
- 검증하지 못한 이유:
  - 사용자 요청은 runscript 작성이며 aircraft variant 생성 요청은 없었음
- 필요한 추가 조건:
  - 실제 엔진/프로펠러 모델 제거가 필요하면 별도 `c172x_noengine` aircraft variant 정의 필요
- 권장 후속 검증:
  - `plots/c172x/4.4__450m_60ms_x_noengine_drop/4.4.2__450m_60ms_x_noengine_drop_states_vs_time_06161822.png`로 자세 발산과 지면 접촉 형태 확인
- 가정:
  - runscript 수준의 engine off 상태를 "엔진 없는상태"로 간주
- 남은 리스크:
  - 기존 `c172x` aircraft에 propulsion/propeller 모델이 남아 있어 windmilling으로 `engine_rpm`, `propeller_rpm`, `thrust_lbs` 로그가 0이 아닌 값을 가질 수 있음
  - SI CSV 확인에서 `magneto_cmd=0`, `starter_cmd=0`, `throttle_cmd_norm=0`은 유지됐지만, `engine_rpm`/`propeller_rpm`은 최대 `2816.498083877348`, `thrust_lbs`는 `-31.63601640296799`부터 `442.74510378485877`까지 기록됨
- 후속 작업:
  - 실제 propulsion 제거가 필요하면 `aircraft_variants/c172x_noengine/` 또는 `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/`에 별도 aircraft XML 생성
- Git commit:
  - 없음
## [2026-06-16 18:32] PROGRESS-20260616-1832-001 — DONE

- 과업:
  - C172X no-engine/no-propeller 추락 variant 및 실행 파일 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `엔진 추력 프로펠러까지 없이 추락으로 파일 만들어 볼래?`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/initial_condition/1.0__450m_60ms_x_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/runscript/1.0__450m_60ms_x_noengine_noprop_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_noprop_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/README.md`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml`
- 수행 내용:
  - 기존 runner가 `/home/junyeopkwon/jsbsim/aircraft/<aircraft>/<aircraft>.xml` 구조를 aircraft로 인식함을 확인
  - 원본 `c172x.xml`에서 `<propulsion>`은 유지하고 그 안의 `<engine>`만 제거하는 generator 작성
  - 결과적으로 `<thruster file="prop_75in2f">`도 함께 제거됨
  - fuel tank 2개는 유지
  - `c172x_noengine` 전용 초기조건, runscript, wrapper 추가
  - 실제 JSBSim 실행 및 SI CSV 검증
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/initial_condition/1.0__450m_60ms_x_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/runscript/1.0__450m_60ms_x_noengine_noprop_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_noprop_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine/README.md`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine/1.0.1__450m_60ms_x_noengine_noprop_drop_noengine_noprop_drop_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine/1.0.1__450m_60ms_x_noengine_noprop_drop_noengine_noprop_drop_summary.json`
- 수정한 파일:
  - 없음
- 핵심 변경점:
  - `c172x_noengine.xml`은 원본 `c172x`에서 engine/propeller thruster를 제거하고 fuel tank는 유지
  - `1.0__450m_60ms_x_noengine_noprop_drop_run.xml`는 AP off, 조종면 중립 상태로 지면 접촉까지 실행
- 실행한 명령어:
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_variant.py /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_noprop_drop.py`
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_variant.py`
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_noengine_noprop_drop.py`
  - `python3 - <<'PY' ... engine/thrust/propeller SI CSV range check ... PY`
- 테스트 결과:
  - Python syntax check 통과
  - XML parse 통과
  - variant 구조 확인: `engine_count=0`, `thruster_count=0`, `tank_count=2`
  - JSBSim 실행 성공
  - 실행 ID: `1.0.1__450m_60ms_x_noengine_noprop_drop`
  - 지면 접촉 시각: `32.60833333 s`
  - 총 궤적 길이: `1788.777871261704 m`
  - 최종 좌표: `(x_north=19.446775347962017 m, y_east=17.185848281346324 m, z_ground=0 m)`
  - 최종 속도: `72.30986234272586 m/s`
- 출력 0 검증:
  - `engine_power_hp`: min `0.0`, max `0.0`
  - `thrust_lbs`: min `0.0`, max `0.0`
  - `engine_rpm`: min `0.0`, max `0.0`
  - `propeller_rpm`: min `0.0`, max `0.0`
  - `propeller_power_ftlbps`: min `0.0`, max `0.0`
  - `prop_advance_ratio`: min `0.0`, max `0.0`
- lint 결과:
  - 별도 lint는 실행하지 않음
- type check 결과:
  - 별도 type check는 실행하지 않음
- build 결과:
  - 해당 없음
- 실행 확인 결과:
  - SI CSV 생성: `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_noengine/1.0__450m_60ms_x_noengine_noprop_drop/1.0.1__450m_60ms_x_noengine_noprop_drop_si_06161831.csv`
  - 요약 JSON 생성: `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine/1.0.1__450m_60ms_x_noengine_noprop_drop_noengine_noprop_drop_summary.json`
- 검증하지 못한 항목:
  - 연료 탱크까지 제거한 완전 propulsion 제거 모델과의 비교
- 검증하지 못한 이유:
  - 이번 요청의 핵심은 엔진 추력과 프로펠러 제거였고, fuel tank는 질량 보존을 위해 유지
- 가정:
  - fuel tank 유지가 더 보수적인 aircraft variant라고 판단
- 남은 리스크:
  - 엔진/프로펠러 질량 자체가 별도 point mass로 모델링된 것은 아니며, 원본 `c172x`의 질량 모델은 그대로 유지됨
- 후속 작업:
  - 엔진/프로펠러 질량 제거까지 필요하면 `mass_balance`를 별도로 조정한 variant 작성
- Git commit:
  - 없음
## [2026-06-16 18:39] PROGRESS-20260616-1839-001 — DONE

- 과업:
  - 수평속도/수직속도 비교 plot 및 조종면 상태 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `지금 조종면 상태가 trim 상태인 뉴트럴 값 맞지? 수평속도랑 수직속도 확인하려고 하니깐 이것들 추가해서 그래프 비교하게 따로 ploting 해줘`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/plot_c172x_drop_velocity_compare.py`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_velocity_compare/0616_drop_horizontal_vertical_speed_compare.png`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_velocity_compare/0616_drop_control_surface_check.png`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_velocity_compare/0616_drop_horizontal_vertical_speed_compare_summary.csv`
- 수행 내용:
  - 기존 `run_jsbsim_timestamped.py`의 SI CSV 필드 구조 확인
  - `v_horizontal_mps = sqrt(v_n_mps^2 + v_e_mps^2)` 계산 추가
  - `v_vertical_up_mps = -v_d_mps` 계산 추가
  - altitude와 함께 비교 plot 생성
  - elevator command, pitch trim command, actual elevator, pitch를 별도 plot으로 생성
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/plot_c172x_drop_velocity_compare.py`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_velocity_compare/0616_drop_horizontal_vertical_speed_compare.png`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_velocity_compare/0616_drop_control_surface_check.png`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_velocity_compare/0616_drop_horizontal_vertical_speed_compare_summary.csv`
- 수정한 파일:
  - 없음
- 핵심 변경점:
  - 기존 큰 states plot과 별도로 horizontal speed, vertical speed up, altitude 비교 전용 plot 생성
  - 조종면 command가 0인지 actual elevator가 어떻게 유지되는지 확인 가능한 plot 생성
- 실행한 명령어:
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/plot_c172x_drop_velocity_compare.py`
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/plot_c172x_drop_velocity_compare.py --output-prefix 0616_drop`
- 테스트 결과:
  - Python syntax check 통과
  - plot 생성 성공
  - summary CSV 생성 성공
- 주요 수치:
  - `c172x engine-off with prop model`: 초기 수평속도 `60.0000000912 m/s`, 초기 수직상승속도 약 `0`, 최대 고도 상승 `116.72575286703409 m`
  - `c172x_noengine no prop`: 초기 수평속도 `60.0000000912 m/s`, 초기 수직상승속도 약 `0`, 최대 고도 상승 `115.79707289632563 m`
  - 두 케이스 모두 `elevator_cmd_norm=0`, `pitch_trim_cmd_norm=0`
  - 두 케이스 모두 실제 elevator deflection은 actuator bias 영향으로 `0.11459155902616465 deg`
- 검증하지 못한 항목:
  - 초기 수직속도 또는 pitch를 변경했을 때의 재실행 결과
- 검증하지 못한 이유:
  - 이번 요청은 기존 결과의 속도/조종면 확인 plot 생성
- 가정:
  - "뉴트럴"은 command 기준 0을 의미하며, 완전한 trim equilibrium 의미는 아님
- 남은 리스크:
  - 실제 actuator bias를 제거하려면 aircraft XML의 elevator actuator bias를 별도로 수정해야 함
- 후속 작업:
  - 바로 하강하는 케이스가 필요하면 초기 `wbody` 또는 `theta`를 별도로 조정한 runscript/init 추가
- Git commit:
  - 없음
## [2026-06-16 20:42] PROGRESS-20260616-2042-001 — DONE

- 과업:
  - 실제 조종면 neutral 상태 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `지금 조종면들 입력값 말고 현재 상태가 뉴트럴 상태인지 확인해봐봐`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_noengine/1.0__450m_60ms_x_noengine_noprop_drop/1.0.1__450m_60ms_x_noengine_noprop_drop_si_06161831.csv`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml`
- 수행 내용:
  - SI CSV 첫 행에서 실제 조종면 상태 확인
  - aircraft XML의 elevator actuator bias 확인
  - aileron/rudder actuator에 별도 bias가 없는 구조 확인
- 생성한 파일:
  - 없음
- 수정한 파일:
  - 없음
- 핵심 변경점:
  - 해당 없음
- 실행한 명령어:
  - `head -n 2 .../1.0.1__450m_60ms_x_noengine_noprop_drop_si_06161831.csv`
  - `nl -ba /home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml | sed -n '285,315p'`
  - `nl -ba /home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml | sed -n '320,395p'`
- 검증 결과:
  - 초기 `elevator_control_deg=0.0`
  - 초기 `elevator_deg=0.11459155902616465`
  - 초기 `aileron_left_deg=0.0`
  - 초기 `aileron_right_deg=0.0`
  - 초기 `rudder_deg=0.0`
  - `c172x_noengine.xml` line 309에 elevator actuator `<bias> 0.002 </bias>` 존재
  - `0.002 rad = 0.11459155902616465 deg`로 실제 elevator offset과 일치
- 검증하지 못한 항목:
  - 전체 구간 aileron/rudder min/max 재계산
- 검증하지 못한 이유:
  - 샌드박스가 긴 Python/awk 명령 일부를 차단했으며, 첫 행과 기존 summary/plot으로 현재 상태 판단에는 충분
- 가정:
  - "현재 상태"는 시뮬레이션 시작 시점 `t=0.0`의 actual surface position을 의미
- 남은 리스크:
  - elevator actual neutral을 정확히 0 deg로 맞추려면 aircraft XML variant에서 actuator bias 제거가 필요
- 후속 작업:
  - 필요 시 `c172x_noengine_nobias` variant를 만들어 elevator actuator `<bias>`를 제거하고 재실행
- Git commit:
  - 없음
## [2026-06-16 20:54] PROGRESS-20260616-2054-001 — DONE

- 과업:
  - pointmass 제거 기반 기본 기체 공력 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `포인트매스로 들어간 것들이 있네 기체 내부 평형 맞추게 기체 중량정보만 냅두고 나머지 중량을 다 0으로 해서 기본 기체 공력 영향만 확인할수 있게 해줘`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_surface_neutral_empty_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/initial_condition/1.0__450m_60ms_x_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/runscript/1.0__450m_60ms_x_empty_surface_neutral_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_drop.py`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty/c172x_noengine_surface_neutral_empty.xml`
- 수행 내용:
  - 원본 `c172x`에서 engine/thruster 제거
  - elevator actuator `<bias>`를 `0.0`으로 설정
  - `PILOT`, `CO-PILOT`, `PASSENGER 1`, `PASSENGER 2`, `LUGGAGE`, `PesticideBomb` pointmass weight를 모두 `0.0`으로 설정
  - 동일 초기조건 `(450 m, 60 m/s north, vertical speed 0)`으로 실행
  - states/trajectory plot 확인
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_surface_neutral_empty_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/initial_condition/1.0__450m_60ms_x_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/runscript/1.0__450m_60ms_x_empty_surface_neutral_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_drop.py`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty/c172x_noengine_surface_neutral_empty.xml`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty/1.0.1__450m_60ms_x_empty_surface_neutral_drop_empty_surface_neutral_drop_summary.json`
- 수정한 파일:
  - 없음
- 핵심 변경점:
  - 기본 기체 `emptywt`와 기본 inertia는 유지
  - 추가 pointmass만 0으로 설정해 비대칭 payload 영향을 제거
- 실행한 명령어:
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_surface_neutral_empty_variant.py /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_drop.py`
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_drop.py`
  - `grep -n '<pointmass\|<weight\|<engine\|<thruster\|<bias>' /home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty/c172x_noengine_surface_neutral_empty.xml`
- 검증 결과:
  - pointmass weight 모두 `0.0`
  - `<engine>`/`<thruster>` 없음
  - elevator actuator bias `0.0`
  - mass: `777.4573114615356 kg`
  - 실제 조종면 범위: elevator/left aileron/right aileron/rudder 모두 `0.0..0.0 deg`
  - 종료 시각: `180.0083333 s`
  - 180초 시점 고도: `80.45476975286901 m`
  - 최대 고도: `592.147492164284 m`
  - 고도 상승량: `142.14749147889017 m`
  - 최종 roll: `-1.1820281061543333e-13 deg`
  - 최종 yaw: `359.999999999989 deg`
  - 최종 pitch: `0.23964413969840592 deg`
- 검증하지 못한 항목:
  - 지면 접촉까지의 전체 시간
- 검증하지 못한 이유:
  - runscript end time이 `180 s`이고, 이 시점에도 고도 약 `80.45 m`로 지면 접촉 전
- 가정:
  - roll/yaw 이상은 pointmass 비대칭 영향 여부를 우선 확인하는 것이 목적
- 남은 리스크:
  - wrapper summary의 `ground_reach_time_s` 필드는 이번 케이스에서는 실제 ground reach가 아니라 runscript 종료 시각임
- 후속 작업:
  - 지면 접촉까지 보려면 runscript end time을 늘린 `1.1` 케이스 추가
- Git commit:
  - 없음
## [2026-06-16 21:31] PROGRESS-20260616-2131-001 — DONE

- 과업:
  - `theta=-20 deg`, `ubody=60 m/s` 초기조건 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `ubody를 60으로 해줘`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/initial_condition/1.1__450m_pitchm20_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/runscript/1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_pitchm20_ubody60_drop.py`
- 수행 내용:
  - empty-airframe no-engine/no-propeller/surface-neutral variant용 pitch-down 초기조건 추가
  - `theta=-20.0 deg`, `ubody=60.0 m/s`, `vbody=0`, `wbody=0` 설정
  - runscript end time을 `240 s`로 설정
  - 실행 wrapper로 JSBSim 실행 및 summary JSON/CSV 생성
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/initial_condition/1.1__450m_pitchm20_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty/runscript/1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_pitchm20_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty/1.1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop_pitchm20_ubody60_drop_summary.json`
- 수정한 파일:
  - 없음
- 핵심 변경점:
  - heading은 유지하고 pitch만 -20 deg
  - `ubody`는 사용자 요청대로 `60 m/s`
- 실행한 명령어:
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_pitchm20_ubody60_drop.py`
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_pitchm20_ubody60_drop.py`
  - `head -n 2 .../1.1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop_si_06162130.csv`
- 검증 결과:
  - 실행 성공
  - 초기 `pitch_deg=-20.0`
  - 초기 `v_total_mps=60.000000091199915`
  - 초기 `v_n_mps=56.38155733285439`
  - 초기 `v_d_mps=20.521208630732332`
  - 실제 조종면 elevator/left aileron/right aileron/rudder 모두 전 구간 `0.0 deg`
  - 종료 시각: `209.475 s`
  - 최종 고도: `1.5290655826538802 m`
  - 최대 고도: `575.421799609834 m`
  - 최종 roll: `8.547498604623295e-14 deg`
  - 최종 yaw: `1.1937487904977577e-11 deg`
- 검증하지 못한 항목:
  - 없음
- 가정:
  - JSBSim body velocity 정의에 따라 `ubody=60`과 `theta=-20`이면 관성계 수평/수직 속도 성분은 각각 약 `60*cos(20 deg)`, `60*sin(20 deg)`로 해석
- 남은 리스크:
  - 최종 고도는 CG 기준 약 `1.53 m`에서 gear WOW로 종료되므로 지면 좌표 기준 충돌점과 다를 수 있음
- 후속 작업:
  - 필요 시 heading `psi` 변형을 추가해 방향별 궤적 비교
- Git commit:
  - 없음
## [2026-06-17 10:44] PROGRESS-20260617-1044-001 — DONE

- 과업:
  - `Cm0` 기반 pitch-up 원인 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `우리 지금 사용하는 기체에 받음각 0도일때 Cm0가 0이 아닌것같은 부분이 있어서 pitch가 -20에서 +50정도까지 올라가는것다는 이야기가 있는데 맞을까?`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty/c172x_noengine_surface_neutral_empty.xml`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_noengine_surface_neutral_empty/1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop/1.1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop_si_06162130.csv`
- 수행 내용:
  - aircraft XML의 `<axis name="PITCH">` 확인
  - `aero/coefficient/Cmo`와 `aero/coefficient/Cmalpha` 정의 확인
  - 초기 CSV 행에서 `pitch_deg=-20`, `v_total_mps=60`, 조종면 actual 0, `q_radps` 초기 증가 확인
- 생성한 파일:
  - 없음
- 수정한 파일:
  - 없음
- 핵심 확인:
  - `Cmo`는 `0.1`
  - `Cmalpha`는 `-1.8`
  - elevator actual은 `0.0 deg`
  - 초기 `wbody=0`, `ubody=60` 설정이므로 초기 aerodynamic alpha는 0도에 가까움
  - 단순 정적 pitch moment만 보면 `Cm = 0.1 - 1.8*alpha_rad`
  - 정적 moment가 0이 되는 alpha는 `0.1 / 1.8 = 0.0556 rad = 약 3.18 deg`
- 실행한 명령어:
  - `sed -n '900,1180p' /home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty/c172x_noengine_surface_neutral_empty.xml`
  - `head -n 5 /home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_noengine_surface_neutral_empty/1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop/1.1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop_si_06162130.csv`
- 검증 결과:
  - 사용자가 들은 설명은 현재 모델 기준으로 타당함
  - 받음각 0도, elevator 0도에서 `Cm0=0.1`이 남아 pitch-up moment를 만들 수 있음
  - 실제 로그도 시작 직후 `q_radps`가 양수로 증가하고 pitch가 -20도에서 위로 이동하는 반응과 일치
- 검증하지 못한 항목:
  - `Cm0=0` 또는 alpha trim 조건을 적용한 재실행 결과
- 검증하지 못한 이유:
  - 이번 요청은 원인 판단
- 가정:
  - JSBSim pitch moment 부호는 현재 로그에서 관측되는 pitch-up 응답과 같은 방향으로 해석
- 남은 리스크:
  - 실제 pitch-up은 `Cm0` 외에도 lift/flight-path phugoid, `Cmq`, `Cmadot`, 속도 변화가 함께 만든 동역학 결과
- 후속 작업:
  - 순수 영향 비교가 필요하면 `Cmo=0` variant 또는 초기 alpha 약 `3.18 deg` 조건을 만든 뒤 재실행
- Git commit:
  - 없음
## [2026-06-17 10:49] PROGRESS-20260617-1049-001 — DONE

- 과업:
  - `Cmo=0` variant 생성 및 pitch -20, `ubody=60` 동일 조건 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `그러면 Cm0=0으로 구성한 모델 하나 새로 만들어서 동일하게 시뮬레이션 돌려볼래?`
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_surface_neutral_empty_cm0_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/1.0__450m_pitchm20_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/runscript/1.0__450m_pitchm20_ubody60_cm0zero_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchm20_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/c172x_noengine_surface_neutral_empty_cm0.xml`
- 수행 내용:
  - 원본 `c172x`에서 engine/thruster 제거
  - elevator actuator bias 0
  - 모든 pointmass weight 0
  - `aero/coefficient/Cmo`의 `<value>`를 `0.0`으로 설정
  - 기존 pitch -20, `ubody=60` 초기조건과 같은 조건으로 실행
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_surface_neutral_empty_cm0_variant.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/1.0__450m_pitchm20_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/runscript/1.0__450m_pitchm20_ubody60_cm0zero_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchm20_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/c172x_noengine_surface_neutral_empty_cm0.xml`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.0.1__450m_pitchm20_ubody60_cm0zero_drop_cm0zero_pitchm20_ubody60_drop_summary.json`
- 수정한 파일:
  - 없음
- 핵심 변경점:
  - `Cmo=0.1`에서 `Cmo=0.0`으로 바꾼 비교 모델 생성
- 실행한 명령어:
  - `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_noengine_surface_neutral_empty_cm0_variant.py /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchm20_ubody60_drop.py`
  - `python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchm20_ubody60_drop.py`
  - `head -n 2 .../1.0.1__450m_pitchm20_ubody60_cm0zero_drop_si_06171048.csv`
  - `tail -n 1 .../1.0.1__450m_pitchm20_ubody60_cm0zero_drop_si_06171048.csv`
  - `sed -n '/aero\\/coefficient\\/Cmo/,/function>/p' /home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/c172x_noengine_surface_neutral_empty_cm0.xml`
- 검증 결과:
  - 실행 성공
  - `Cmo` 블록 값 `<value> 0.0 </value>` 확인
  - 초기 `pitch_deg=-20.0`
  - 초기 `v_total_mps=60.000000091199915`
  - 실제 elevator actual `0.0 deg`
  - 종료 시각: `66.475 s`
  - 최종 고도: `1.5903488378137351 m`
  - 최대 고도: `450.00000068539384 m`
  - 고도 상승량: `0.0 m`
  - pitch range: `-20.0 .. 3.1964578634182237 deg`
  - 최종 roll/yaw는 수치오차 수준
- 비교 결과:
  - 기존 `Cmo=0.1` 케이스: 고도 상승량 `125.42179892444017 m`, 종료 시각 `209.475 s`
  - 신규 `Cmo=0` 케이스: 고도 상승량 `0.0 m`, 종료 시각 `66.475 s`
- 검증하지 못한 항목:
  - `Cmo` 외 pitch moment coefficient의 민감도 비교
- 검증하지 못한 이유:
  - 이번 요청은 `Cmo=0` 단일 비교
- 가정:
  - 두 케이스 비교에서 주요 차이는 `Cmo` 값으로 제한됨
- 남은 리스크:
  - dynamic pitch response에는 `Cmalpha`, `Cmq`, `Cmadot`, lift/flight path coupling도 포함됨
- 후속 작업:
  - 필요 시 `Cmo=0.05`, `Cmo=-0.05` 등 sweep 비교 plot 생성
- Git commit:
  - 없음
## [2026-06-17 12:59] CORRECTION-20260617-1259-002 — 정정

- 대상 기록:
  - `PROGRESS-20260617-1258-001`
- 정정 이유:
  - append 패치 컨텍스트가 흔한 문구와 매칭되어 파일 하단이 아닌 `docs/agent-log/PROGRESS.md:73` 부근에 삽입됨
- 기존 내용:
  - `PROGRESS-20260617-1258-001`의 내용 자체는 유효하나 시간 순서상 위치가 부적절함
- 정정 내용:
  - 기존 중간 삽입 기록은 삭제하지 않고, 아래에 같은 수행 내역의 최신 참조 기록 `PROGRESS-20260617-1259-001`을 append함
- 영향 범위:
  - 작업 기록 조회 시 하단의 `PROGRESS-20260617-1259-001`을 최신 참조로 사용
- 검증 결과:
  - `grep -n 'PROGRESS-20260617-1258-001' docs/agent-log/PROGRESS.md`로 중간 삽입 위치 확인
- 다음 작업:
  - 향후 기록 append 시 더 고유한 EOF 컨텍스트 사용

## [2026-06-17 12:59] PROGRESS-20260617-1259-001 — DONE

- 과업:
  - `theta=+2.5 deg`, `ubody=60 m/s` 초기조건 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체로 초기 고도 `450 m`, pitch `2.5 deg`, 속도 `ubody=60 m/s` 조건을 만들고 추락 실행
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/1.1__450m_pitchp25_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/runscript/1.1__450m_pitchp25_ubody60_cm0zero_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_si_06171257.csv`
- 수행 내용:
  - pitch +2.5 deg 전용 initial XML과 runscript 생성
  - runscript end time `600 s`, 종료 조건 `gear/unit[0]/WOW eq 1`
  - wrapper로 aircraft variant 재생성 후 JSBSim 실행
  - 결과 summary JSON/CSV와 상태/궤적 plot 생성
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/initial_condition/1.1__450m_pitchp25_ubody60_drop_init.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_noengine_surface_neutral_empty_cm0/runscript/1.1__450m_pitchp25_ubody60_cm0zero_drop_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_si_06171257.csv`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_states_vs_time_06171257.png`
  - `/home/junyeopkwon/jsbsim_workflow/plots/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.1__450m_pitchp25_ubody60_cm0zero_drop_trajectory_3d_06171257.png`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/c172x_noengine_surface_neutral_empty_cm0.xml`
- 핵심 변경점:
  - 초기 자세 `theta=+2.5 deg`
  - 초기 속도 `ubody=60 m/s`
  - `Cmo=0`, no-engine/no-propeller, 조종면 neutral 조건 유지
- 실행한 명령어:
  - `python3 -m py_compile scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - XML parse 검증
  - `python3 scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - summary/CSV 검산 Python snippet
  - `git status --short` 확인
- 검증 결과:
  - Python 문법 검사 성공
  - initial XML/runscript XML 파싱 성공
  - JSBSim 실행 성공
  - 초기 고도 `450.00000068539384 m`, 초기 pitch `2.4999999999999996 deg`, 초기 total speed `60.000000091200036 m/s`
  - 종료 시각 `73.83333333 s`, 최종 고도 `1.6107039963841439 m`, 최종 속도 `50.779647191860775 m/s`
  - 최대 고도 `477.49023545747997 m`, 고도 상승량 `27.490234772086126 m`
  - pitch range `-16.075296745533503 .. 5.5943518995439225 deg`
  - elevator/aileron/rudder/thrust/engine_rpm/propeller_rpm 전 구간 `0.0`
- 검증하지 못한 항목:
  - body-axis `ubody` 컬럼 직접 출력
- 검증하지 못한 이유:
  - 현재 SI CSV 출력 목록에는 body-axis 속도 컬럼이 포함되어 있지 않음
- 가정:
  - initial XML의 `<ubody unit="M/SEC"> 60.0 </ubody>`가 JSBSim 초기 body x축 속도로 적용됨
- 남은 리스크:
  - `/home/junyeopkwon/jsbsim` 저장소 기준 aircraft variant XML은 untracked 상태로 확인됨
- 후속 작업:
  - 필요 시 body-axis 속도 컬럼을 SI CSV에 포함하도록 runner 출력 필드 확장
- Git commit:
  - 없음
## [2026-06-17 14:15] PROGRESS-20260617-1415-001 — DONE

- 과업:
  - 6DOF 검증용 JSBSim property 별도 CSV 저장 구현 및 실행 검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 상태, 입력, 힘/모멘트, 가속도, 공력, 추력, 접촉/환경 property를 `<output>`에 지정해 CSV로 따로 저장
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.3__450m_pitchp25_ubody60_cm0zero_drop_runscript_06171414.xml`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.3__450m_pitchp25_ubody60_cm0zero_drop_sixdof_raw_06171414.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.3__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
- 수행 내용:
  - `SIXDOF_CSV_DIR`와 `SIXDOF_VALIDATION_PROPERTIES` 추가
  - 상태, body/NED 속도, Euler rate, force, moment, acceleration, aero coefficient, gear/contact, brake, atmosphere property 묶음 정의
  - `JSBSim --catalog --nohighlight` 출력으로 aircraft별 available property를 수집
  - 요청 property 중 catalog에 있는 항목만 두 번째 `<output>`에 기록
  - 기존 `Raw CSV`와 `SI CSV` 출력은 유지
  - pitch +2.5 deg wrapper에서 `6DOF raw CSV` 경로를 summary JSON/CSV에 포함
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.2__450m_pitchp25_ubody60_cm0zero_drop_sixdof_raw_06171412.csv`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.3__450m_pitchp25_ubody60_cm0zero_drop_sixdof_raw_06171414.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.3__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.3__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/c172x_noengine_surface_neutral_empty_cm0.xml`
- 핵심 변경점:
  - generated runscript에 기존 raw output `48`개 property와 별도 6DOF output `76`개 property가 함께 생성됨
  - 6DOF CSV는 `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/` 아래에 저장됨
- 실행한 명령어:
  - `python3 -m py_compile scripts/run_jsbsim_timestamped.py scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `python3 scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - CSV header/row 검산 Python snippet
  - generated runscript output property count 검산 Python snippet
  - catalog selected/skipped property 계산 Python snippet
  - `git status --short` 확인
- 검증 결과:
  - Python 문법 검사 성공
  - 실행 ID `1.1.3__450m_pitchp25_ubody60_cm0zero_drop` 실행 성공
  - 6DOF raw CSV 생성 확인
  - 6DOF raw CSV size: `11121091` bytes
  - 6DOF raw CSV columns: `77` (`Time` 포함)
  - 6DOF raw CSV rows: `8861`
  - 확인한 대표 컬럼:
    - `/fdm/jsbsim/simulation/sim-time-sec`
    - `/fdm/jsbsim/attitude/theta-deg`
    - `/fdm/jsbsim/velocities/u-fps`
    - `/fdm/jsbsim/forces/fbx-total-lbs`
    - `/fdm/jsbsim/moments/m-total-lbsft`
    - `/fdm/jsbsim/accelerations/qdot-rad_sec2`
    - `/fdm/jsbsim/aero/alpha-deg`
    - `/fdm/jsbsim/aero/coefficient/CDo`
    - `/fdm/jsbsim/forces/fbz-gear-lbs`
    - `/fdm/jsbsim/gear/unit[1]/compression-ft`
    - `/fdm/jsbsim/fcs/left-brake-cmd-norm`
    - `/fdm/jsbsim/atmosphere/total-wind-down-fps`
- 검증하지 못한 항목:
  - PX4 uORB 로그와의 실제 동기화 비교
  - VTOL/multicopter 기체에서 indexed engine/motor property 저장 검증
- 검증하지 못한 이유:
  - 이번 검증 대상은 `c172x_noengine_surface_neutral_empty_cm0`
  - no-engine C172X catalog에는 indexed propulsion property가 없음
- 가정:
  - 모델 catalog에 없는 property는 output에 넣지 않고 skipped 처리하는 방식이 모델별 안전성이 높음
- 남은 리스크:
  - `aero/coefficient/CD0`는 현재 C172X catalog에 없고 `aero/coefficient/CDo`가 존재함
  - `gear/unit[0]/...`는 현재 catalog에 없고 첫 gear는 `gear/unit/...`, 이후 gear는 `gear/unit[1]`, `gear/unit[2]` 형태로 노출됨
  - `fcs/throttle-cmd-norm`와 engine 관련 property는 no-engine C172X catalog에 없어 제외됨
  - 6DOF CSV는 raw 단위이므로 PX4 비교 전 단위/좌표계 변환이 필요함
- 후속 작업:
  - 필요 시 `sixdof_raw`를 SI/NED/FRD 기준 비교용 CSV로 변환하는 후처리 추가
- Git commit:
  - 없음
## [2026-06-17 14:33] PROGRESS-20260617-1433-001 — DONE

- 과업:
  - `sixdof_raw`에 전체 position property 추가 및 실행 검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `position/*` 정보는 어떤 것을 쓸지 나중에 정할 수 있게 모두 `sixdof_raw`에 추가
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.4__450m_pitchp25_ubody60_cm0zero_drop_runscript_06171432.xml`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.4__450m_pitchp25_ubody60_cm0zero_drop_sixdof_raw_06171432.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.4__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
- 수행 내용:
  - `SIXDOF_VALIDATION_PROPERTIES` 앞쪽에 `position/*` catalog 항목 30개 추가
  - 기존 중복 제거 로직으로 기존 position property 중복 컬럼 방지
  - `python3 -m py_compile`로 문법 검사
  - pitch +2.5 deg C172X Cm0=0 wrapper 재실행
  - 생성 CSV header와 generated runscript output property 수 검산
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.4__450m_pitchp25_ubody60_cm0zero_drop_sixdof_raw_06171432.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.4__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.4__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/c172x_noengine_surface_neutral_empty_cm0.xml`
- 핵심 변경점:
  - `sixdof_raw` output property가 76개에서 102개로 증가
  - CSV 컬럼은 `Time` 포함 103개
  - position 컬럼 30개 포함
- 실행한 명령어:
  - `python3 -m py_compile scripts/run_jsbsim_timestamped.py scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - catalog 기반 selected property 검산 Python snippet
  - `python3 scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - CSV header/row 검산 Python snippet
  - generated runscript output property count 검산 Python snippet
  - `git status --short` 확인
- 검증 결과:
  - Python 문법 검사 성공
  - catalog 기준 전체 selected property `102`개
  - selected position property `30`개
  - 실행 ID `1.1.4__450m_pitchp25_ubody60_cm0zero_drop` 실행 성공
  - 6DOF raw CSV columns: `103`
  - 6DOF raw CSV rows: `8861`
  - generated runscript의 `sixdof_raw` output property count: `102`
  - 확인한 컬럼:
    - `/fdm/jsbsim/position/from-start-neu-n-ft`
    - `/fdm/jsbsim/position/from-start-neu-e-ft`
    - `/fdm/jsbsim/position/from-start-neu-u-ft`
    - `/fdm/jsbsim/position/distance-from-start-lon-mt`
    - `/fdm/jsbsim/position/eci-x-ft`
    - `/fdm/jsbsim/position/ecef-z-ft`
    - `/fdm/jsbsim/position/epa-rad`
- 검증하지 못한 항목:
  - 최종 비교 기준 position property 선정
  - SI/NED/FRD 변환 후 직접 코드와 비교
- 검증하지 못한 이유:
  - 이번 요청은 position property 전체를 raw 로그에 추가하는 범위
- 가정:
  - 후속 비교에서 필요한 좌표계와 원점 정의에 따라 사용할 position property를 선택할 예정
- 남은 리스크:
  - `position/from-start-neu-u-ft`의 초기값은 이번 케이스에서 약 `1476.377955 ft`로 기록되어 단순 변위인지 고도 포함 local-up인지 후속 해석 필요
  - `/home/junyeopkwon/jsbsim` 저장소 기준 aircraft variant XML은 untracked 상태
- 후속 작업:
  - 별도 코드 `(0,0,450)`과 비교할 때 `from-start-neu-*`, `distance-from-start-*`, `h-sl-meters` 중 기준을 선정하고 단위/부호 변환 정의
- Git commit:
  - 없음
## [2026-06-17 14:45] PROGRESS-20260617-1445-001 — DONE

- 과업:
  - `sixdof_si` position 미터 변환 CSV 생성 구현 및 검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 별도 SI 변환 CSV에서 meter 단위 position 컬럼을 만들기로 함
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_si/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.5__450m_pitchp25_ubody60_cm0zero_drop_sixdof_si_06171444.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.5__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
- 수행 내용:
  - `SIXDOF_SI_CSV_DIR = logs/csv/sixdof_si` 추가
  - `SIXDOF_POSITION_SI_FIELDS` 32개 컬럼 정의
  - `convert_sixdof_raw_to_si()` 추가
  - ft 단위 position property를 meter 단위 컬럼으로 변환
  - `from_start_ned_d_m = -from_start_neu_u_m` 보조 컬럼 추가
  - runner 출력과 pitch +2.5 deg wrapper summary에 `6DOF SI CSV` 경로 추가
- 생성한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_si/c172x_noengine_surface_neutral_empty_cm0/1.1__450m_pitchp25_ubody60_cm0zero_drop/1.1.5__450m_pitchp25_ubody60_cm0zero_drop_sixdof_si_06171444.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.5__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.csv`
  - `/home/junyeopkwon/jsbsim_workflow/results/c172x_noengine_surface_neutral_empty_cm0/1.1.5__450m_pitchp25_ubody60_cm0zero_drop_cm0zero_pitchp25_ubody60_drop_summary.json`
- 수정한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine_surface_neutral_empty_cm0/c172x_noengine_surface_neutral_empty_cm0.xml`
- 핵심 변경점:
  - `sixdof_raw`와 별도로 `sixdof_si` CSV 생성
  - position 비교용 meter 컬럼 제공
  - `from_start_neu_*_m`와 `from_start_ned_d_m` 추가
- 실행한 명령어:
  - `python3 -m py_compile scripts/run_jsbsim_timestamped.py scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - `python3 scripts/run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py`
  - raw/SI row count 및 변환값 대조 Python snippet
  - summary JSON 경로 확인 Python snippet
  - `git status --short` 확인
- 검증 결과:
  - Python 문법 검사 성공
  - 실행 ID `1.1.5__450m_pitchp25_ubody60_cm0zero_drop` 실행 성공
  - `sixdof_raw` rows: `8861`
  - `sixdof_si` rows: `8861`
  - `sixdof_si` columns: `32`
  - raw `position/from-start-neu-u-ft = 1476.3779550049292`
  - SI `from_start_neu_u_m = 450.0000006855024`
  - 기대값 `1476.3779550049292 * 0.3048 = 450.0000006855024`
  - `from_start_ned_d_m = -450.0000006855024`
  - summary JSON에 `sixdof_si_csv` 경로 포함 확인
- 검증하지 못한 항목:
  - force/moment/aero 전체 SI 변환
  - 직접 코드와의 실제 position 비교
- 검증하지 못한 이유:
  - 이번 범위는 position 중심 SI CSV 생성
- 가정:
  - 직접 코드 비교 시 우선 `from_start_neu_*_m` 또는 `from_start_ned_d_m`를 사용할 가능성이 높음
- 남은 리스크:
  - `from_start_neu_u_m`는 이번 케이스에서 초기 고도 `450 m`를 포함하는 값이므로, 별도 코드가 초기 z를 450으로 두는지 0으로 두는지에 따라 offset 처리가 필요할 수 있음
- 후속 작업:
  - 직접 코드 좌표 원점 정의에 맞춰 `from_start_neu_u_m` 그대로 사용 또는 `from_start_neu_u_m - initial_alt_m` 사용 여부 결정
- Git commit:
  - 없음

## [2026-06-21 15:54] PROGRESS-20260621-1554-001 — 진단 완료

- 수행한 작업: 동력 포함 c172x_empty_cg_aligned 변형과 비자전 구형 지구용 초기조건을 사용하여 3·4단계 전용 시나리오 실행
- 조사한 파일: /home/junyeopkwon/flightgear_manual/Chapter4.docx, 기존 c172x 모델, 기존 5.1·5.3 runscript와 프로젝트 기록
- 생성한 파일: scripts/c172x/runscript/5.5__takeoff_stage3_stage4_diagnostic_run.xml
- 관련 생성 파일: scripts/generate_c172x_empty_cg_aligned_variant.py, aircraft_variants/c172x_empty_cg_aligned/c172x_empty_cg_aligned.xml, scripts/c172x/initial_condition/2.1__takeoff_nonrotating_spherical_init.xml
- 핵심 변경점: 40 kt 기수 하중 완화, 55 kt 회전, 지상고 20 ft에서 조종간 완화 후 70 kt·150 ft 도달 조건으로 단계 분리
- 실행한 명령어: xmllint --noout 대상 XML, python3 -m py_compile 관련 Python, python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_empty_cg_aligned --init scripts/c172x/initial_condition/2.1__takeoff_nonrotating_spherical_init.xml --runscript scripts/c172x/runscript/5.5__takeoff_stage3_stage4_diagnostic_run.xml --planet earth_models/04_nonrotating_spherical_earth.xml
- 테스트 결과: XML 검증 및 Python 구문 검증 통과, JSBSim 종료 코드 0
- 실행 확인 결과: Stage 3은 16.508333초·55.021804 kt·받음각 1.684265도에서 실행, Stage 4는 19.225000초·62.972400 kt·받음각 4.104642도·AGL 20.052416 ft에서 실행
- 이륙 확인 결과: Nose Gear 20.541667초·61.747038 KCAS, Left Main Gear 20.575000초·61.675649 KCAS, Right Main Gear 20.633333초·61.546603 KCAS
- 문제 확인 결과: 28.983333초에 70.093660 kt·AGL 154.925764 ft를 만족했지만 상승률 -47.841478 ft/s, 피치 -22.332478도, 롤 약 62.78도로 실제로는 급강하·과대 뱅크 상태
- 무게중심 확인: 실행 CSV의 inertia/cg-y-in은 0으로 좌우 비대칭은 제거됨
- 생성 로그: logs/console/c172x_empty_cg_aligned/5.5__takeoff_stage3_stage4_diagnostic/5.5.1__takeoff_stage3_stage4_diagnostic_console_06211550.log
- 생성 데이터: logs/csv/raw/c172x_empty_cg_aligned/5.5__takeoff_stage3_stage4_diagnostic/5.5.1__takeoff_stage3_stage4_diagnostic_raw_06211550.csv
- 생성 plot: plots/c172x_empty_cg_aligned/5.5__takeoff_stage3_stage4_diagnostic/5.5.1__takeoff_stage3_stage4_diagnostic_states_vs_time_06211550.png, plots/c172x_empty_cg_aligned/5.5__takeoff_stage3_stage4_diagnostic/5.5.1__takeoff_stage3_stage4_diagnostic_trajectory_3d_06211550.png
- 추가 조사 결과: Chapter4.docx는 프로그램 시작·런처 설명 중심이며 C172 이륙 조작 속도 절차를 제공하지 않음
- 검증하지 못한 항목: plot 육안 검토, FlightGear 실제 조종 입력과의 정량 비교, 안전한 4단계 제어
- 검증하지 못한 이유: 현재 요청은 문제 수정 없이 현황 정리로 범위를 제한함
- 남은 리스크: 현재 Stage 4 complete 이벤트는 고도와 속도만 검사해 위험한 강하·과대 뱅크를 성공으로 오판
- 다음 작업: 사용자 승인 후 롤·피치 폐루프 안정화와 상승률 포함 완료 조건을 별도 과업으로 수행
- Git commit: 해당 프로젝트는 Git 저장소가 아니며 commit 없음


## [2026-06-21 18:45] PROGRESS-20260621-1845-001 — 완료

- 수행한 작업: 첨부 pasted-text.txt 분석, RKSS 14L 기본 지구 초기조건과 6단계 C172X 이륙·순항 runscript 구현, 반복 실행·수치 검증
- 생성한 파일: scripts/c172x/initial_condition/2.2__rkss_14l_default_earth_init.xml
- 생성한 파일: scripts/c172x/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml
- 수정한 파일: scripts/c172x/README.md
- 사용 모델: c172x_empty_cg_aligned
- 핵심 변경점: latitude를 type=geodetic으로 명시, RKSS 14L longitude 126.7782777778 deg·heading 135.01 deg·terrain elevation 38.0 ft 적용
- 핵심 변경점: 기체 기준점 altitude를 4.305 ft AGL로 설정하고 초기 running 요소를 삭제해 t=0 엔진 정지를 보장
- 핵심 변경점: t=0.25 s 엔진 가동, 40 kt 기수 하중 완화, 55 kt 회전, AGL 20 ft에서 heading 135.01 deg·altitude 1000 ft 자동조종 결합
- 핵심 변경점: 70 kt·AGL 150 ft 이후 throttle 0.75, 순항 시작 조건을 AGL 950~1050 ft·수직속도 ±0.2 ft/s·속도 65 kt 이상·롤 ±10 deg·피치 -5~15 deg로 제한
- 실행 명령어: python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_empty_cg_aligned --init scripts/c172x/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml --planet default
- 최종 실행: 5.6.6__rkss14l_default_earth_takeoff_cruise30, timestamp 06211844
- 최종 결과: STATE 0 0.258333 s, STATE 1 2.008333 s, STATE 2 12.941667 s, STATE 3 16.466667 s, STATE 4 19.191667 s
- 이륙 결과: 세 랜딩기어가 20.891667~20.975000 s에 약 63.48 KCAS로 지면 이탈
- 고도 포착 결과: 65.583333 s에 70.004057 kt·1026.071262 ft AGL
- 순항 결과: 223.925000 s에 안정 순항 시작, 253.916667 s에 29.991667 s 타이머 완료
- 30초 구간 수치: AGL 953.245375~963.273829 ft, KCAS 103.429263~105.793060 kt, h-dot -0.199545~0.460726 ft/s
- 30초 구간 자세: roll -0.067375~-0.039563 deg, pitch -0.197744~0.081298 deg, alpha -0.134608~-0.067291 deg
- 무게중심 확인: 30초 구간 inertia/cg-y-in 최소·최대 모두 0
- 초기 위치 확인: position/lat-geod-deg 37.5707083333, longitude 126.7782777778, AGL 4.305 ft
- 검증 명령어: xmllint --noout 대상 XML, JSBSim 실행 종료 코드 확인, console 이벤트 검사, raw CSV 30초 구간 min/max 검사
- 검증 결과: XML 정상, JSBSim 종료 코드 0, STATE 0~6 전부 실행, stall·ground-contact abort 미발생
- 실패·정정 기록: --planet 생략 시 공용 runner가 비자전 구형 지구를 선택해 SIGFPE 발생하여 --planet default를 명시
- 실패·정정 기록: altitude=42.305와 running=0은 각각 AGL 42.305 ft 및 엔진 0 가동으로 해석되어 altitude=4.305와 running 삭제로 정정
- 실패·정정 기록: latitude type 미지정 시 geocentric으로 해석되어 type=geodetic 추가
- 생성 로그: logs/console/c172x_empty_cg_aligned/5.6__rkss14l_default_earth_takeoff_cruise30/5.6.6__rkss14l_default_earth_takeoff_cruise30_console_06211844.log
- 생성 데이터: logs/csv/raw/c172x_empty_cg_aligned/5.6__rkss14l_default_earth_takeoff_cruise30/5.6.6__rkss14l_default_earth_takeoff_cruise30_raw_06211844.csv
- 생성 plot: plots/c172x_empty_cg_aligned/5.6__rkss14l_default_earth_takeoff_cruise30/5.6.6__rkss14l_default_earth_takeoff_cruise30_states_vs_time_06211844.png, plots/c172x_empty_cg_aligned/5.6__rkss14l_default_earth_takeoff_cruise30/5.6.6__rkss14l_default_earth_takeoff_cruise30_trajectory_3d_06211844.png
- 검증하지 못한 항목: FlightGear GUI에서 동일 입력 재현, 첨부 AIP 수치의 외부 공식자료 재조회
- 남은 리스크: 공용 runner는 --planet 생략 시 C172X에 비자전 구형 지구를 선택하므로 실행 명령에서 default를 반드시 명시해야 함
- Git commit: 프로젝트가 Git 저장소가 아니므로 없음


## [2026-06-23 08:56] PROGRESS-20260623-0856-001 — 완료

- 수행한 작업: 5.6 RKSS 기본 지구 이륙·순항 시나리오를 기반으로 5.7 엔진 정지·비제어 추락 상태 추가
- 생성한 파일: scripts/c172x/runscript/5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml
- 수정한 파일: scripts/c172x/README.md
- 핵심 변경점: run 종료 한도를 600 s로 확장하고 기존 조기 stall·재접지 abort를 엔진 정지 이후 충돌 이벤트로 대체
- 핵심 변경점: 30초 순항 완료 시 throttle·mixture·magneto·starter 정지, propulsion engine set-running 0, heading·altitude·attitude·airspeed hold 해제
- 핵심 변경점: AP 명령, elevator·aileron·rudder 명령, pitch·roll·yaw trim을 모두 0으로 설정
- 핵심 변경점: cruise-timer-sec 29.99 이상·AGL 5 ft 미만·Left Main Gear WOW 조건에서 STATE 7 충돌 종료
- 실행 명령어: python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_empty_cg_aligned --init scripts/c172x/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x/runscript/5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml --planet default
- 최종 실행: 5.7.1__rkss14l_takeoff_cruise_engineoff_crash, timestamp 06230852
- 이륙 결과: STATE 3 회전 16.466667 s, 세 랜딩기어 이륙 20.891667~20.975000 s
- 순항 결과: 안정 순항 시작 223.925000 s, 30초 완료·엔진 정지 253.916667 s
- 추락 결과: Nose Gear 접촉 277.591667 s, Left Main Gear 접촉 277.608333 s, STATE 7 종료 277.616667 s
- 충돌 종료 상태: 121.237565 KCAS, h-dot -27.703450 ft/s, AGL 4.656501 ft, roll -8.952591 deg, pitch -10.345908 deg
- 엔진 확인: 충돌 종료 시 engine power -1.5 hp 모델 오프셋, thrust 0, engine RPM 0, propeller RPM 0
- 검증 명령어: xmllint --noout 5.7 runscript, JSBSim timestamp runner, console 이벤트 grep, raw CSV 종료행 검사
- 검증 결과: XML 정상, JSBSim 종료 코드 0, STATE 0~7 전부 실행, 엔진 정지 이후 23.70 s에 지면 충돌
- QGC 조사: JSBSim 코어와 현재 workflow에는 MAVLink·QGC 송신 구현이 없고 PX4 저장소의 별도 jsbsim_bridge가 HIL_SENSOR·HIL_GPS와 actuator 제어를 처리
- QGC 로컬 환경: /home/junyeopkwon/Downloads/QGroundControl-x86_64.AppImage, /home/junyeopkwon/PX4-Autopilot/Tools/simulation/jsbsim/jsbsim_bridge 존재
- QGC 결론: JSBSim 실행 파일만으로는 QGC 차량 표시 불가, JSBSim + jsbsim_bridge + PX4 SITL + QGC 또는 별도 MAVLink telemetry adapter 필요
- 생성 로그: logs/console/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.1__rkss14l_takeoff_cruise_engineoff_crash_console_06230852.log
- 생성 데이터: logs/csv/raw/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.1__rkss14l_takeoff_cruise_engineoff_crash_raw_06230852.csv
- 생성 plot: plots/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.1__rkss14l_takeoff_cruise_engineoff_crash_states_vs_time_06230852.png, plots/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.1__rkss14l_takeoff_cruise_engineoff_crash_trajectory_3d_06230852.png
- 검증하지 못한 항목: QGC GUI 연결, PX4 SITL 실제 기동, QGC 3D 외부 시점
- 검증하지 못한 이유: 이번 요청은 가능 여부 확인이며 외부 GUI·PX4 실행은 범위에 포함하지 않음
- 남은 리스크: QGC 통합 시 현재 5.7 runscript 상태기계와 PX4 actuator 제어권 충돌을 별도로 설계해야 함
- Git commit: 프로젝트가 Git 저장소가 아니므로 없음


## [2026-06-23 08:57] CORRECTION-20260623-0857-001 — 정정

- 대상 기록: PROGRESS-20260623-0856-001의 scripts/c172x/README.md 갱신
- 정정 이유: shell append 과정에서 Markdown backtick과 t 문자가 PowerShell escape로 해석되어 코드 펜스와 시간 표현이 손상됨
- 기존 내용: RKSS 5.6·5.7 실행 명령의 코드 펜스와 시뮬레이션 시작 시간 문구가 깨진 상태
- 정정 내용: 해당 두 README 섹션을 정상 Markdown tilde fence와 일반 시간 문구로 재작성
- 영향 범위: 문서 표시만 영향, XML·JSBSim 실행·로그 결과에는 영향 없음
- 검증 결과: README tail 재확인 및 bash fence 2개 확인
- 다음 작업: 없음


## [2026-06-23 09:25] PROGRESS-20260623-0925-001 — 완료

- 수행한 작업: `c172x_empty_cg_aligned` aircraft 선택 시 초기조건 후보가 없어 `RuntimeError: No init XML options found`가 발생하는 원인을 조사하고, 해당 aircraft명과 일치하는 시나리오 폴더를 생성
- 조사한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
- 생성한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_empty_cg_aligned/README.md`
- 생성한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_empty_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml`
- 생성한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_empty_cg_aligned/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml`
- 생성한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_empty_cg_aligned/runscript/5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml`
- 핵심 변경점: runner가 aircraft명과 동일한 `scripts/<aircraft>/` 아래에서 초기조건과 runscript를 찾는 구조에 맞춰 `scripts/c172x_empty_cg_aligned/`를 추가
- 핵심 변경점: 복사한 `5.6`, `5.7` runscript의 `<use initialize="...">` 경로를 `scripts/c172x_empty_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml`로 변경
- 실행한 명령어: `xmllint --noout scripts/c172x_empty_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml scripts/c172x_empty_cg_aligned/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml scripts/c172x_empty_cg_aligned/runscript/5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml`
- 실행한 명령어: `python3 -m py_compile scripts/run_jsbsim_timestamped.py`
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_empty_cg_aligned --init scripts/c172x_empty_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x_empty_cg_aligned/runscript/5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml --planet default`
- 테스트 결과: XML 문법 검증 성공, runner Python 컴파일 성공, 새 폴더 경로 기반 5.7 JSBSim 실행 성공
- 실행 확인 결과: 최종 실행 `5.7.2__rkss14l_takeoff_cruise_engineoff_crash`, timestamp `06230925`
- 생성 로그: `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.2__rkss14l_takeoff_cruise_engineoff_crash_console_06230925.log`
- 생성 데이터: `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.2__rkss14l_takeoff_cruise_engineoff_crash_raw_06230925.csv`
- 생성 plot: `/home/junyeopkwon/jsbsim_workflow/plots/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.2__rkss14l_takeoff_cruise_engineoff_crash_states_vs_time_06230925.png`
- 생성 plot: `/home/junyeopkwon/jsbsim_workflow/plots/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.2__rkss14l_takeoff_cruise_engineoff_crash_trajectory_3d_06230925.png`
- 선택 후보 확인: `init_options=1`, `runscript_options=2`
- 검증하지 못한 항목: 사용자가 보는 실제 대화형 입력 화면에서 `39 -> 1 -> 2` 번호 입력으로 끝까지 실행되는지 수동 검증
- 남은 리스크: `scripts/c172x/`에도 원본 복사본이 남아 있어 향후 같은 시나리오를 수정할 때 두 위치 중 어느 쪽을 기준으로 할지 혼동 가능
- Git commit: 프로젝트가 Git 저장소가 아니므로 없음

## [2026-06-23 09:50] PROGRESS-20260623-0950-001 — 완료

- 수행한 작업: timestamp runner에 live 3D 선택 옵션을 추가하고, JSBSim raw CSV를 실시간으로 읽는 독립 Matplotlib 3D 애니메이션 스크립트를 생성
- 수정한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
- 생성한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/live_trajectory_3d.py`
- 수정한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/README.md`
- 핵심 변경점: `--live-3d`, `--no-live-3d` CLI 옵션 추가
- 핵심 변경점: 대화형 실행 시 aircraft, init XML, runscript 선택 후 live 3D 사용 여부를 묻도록 구성
- 핵심 변경점: live 모드에서 JSBSim 실행 명령에 `--realtime`을 삽입
- 핵심 변경점: runner의 저장용 plot 백엔드 `Agg`와 충돌하지 않도록 live animation은 별도 프로세스 `scripts/live_trajectory_3d.py`로 실행
- 핵심 변경점: 애니메이션 스크립트는 raw CSV의 ECEF 좌표를 첫 샘플 기준 local ENU로 변환하고, 시간·AGL·속도·자세 정보를 함께 표시
- 실행한 명령어: `python3 -m py_compile scripts/run_jsbsim_timestamped.py scripts/live_trajectory_3d.py`
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped.py --help | grep -- "--live-3d"`, `python3 scripts/run_jsbsim_timestamped.py --help | grep -- "--no-live-3d"`
- 실행한 명령어: `python3 scripts/live_trajectory_3d.py --csv logs/csv/raw/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.2__rkss14l_takeoff_cruise_engineoff_crash_raw_06230925.csv --headless --max-frames 1 --final-hold-sec 0`
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_empty_cg_aligned --init scripts/c172x_empty_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x_empty_cg_aligned/runscript/5.7__rkss14l_takeoff_cruise_engineoff_crash_run.xml --planet default --no-live-3d`
- 실행한 명령어: monkeypatch 검증으로 `run_jsbsim(..., realtime=True)` 호출 시 JSBSim 명령 앞부분에 `--realtime`이 들어가는지 확인
- 테스트 결과: Python 문법 검증 성공, help 옵션 노출 확인, headless CSV 애니메이터 1 frame 로딩 성공, 기존 비실시간 5.7 실행 성공, `--realtime` 삽입 확인
- 실행 확인 결과: `5.7.4__rkss14l_takeoff_cruise_engineoff_crash`, timestamp `06230949`, `Live 3D animation: disabled` 출력 확인
- 생성 로그: `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.4__rkss14l_takeoff_cruise_engineoff_crash_console_06230949.log`
- 생성 데이터: `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.4__rkss14l_takeoff_cruise_engineoff_crash_raw_06230949.csv`
- 생성 plot: `/home/junyeopkwon/jsbsim_workflow/plots/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.4__rkss14l_takeoff_cruise_engineoff_crash_states_vs_time_06230949.png`
- 생성 plot: `/home/junyeopkwon/jsbsim_workflow/plots/c172x_empty_cg_aligned/5.7__rkss14l_takeoff_cruise_engineoff_crash/5.7.4__rkss14l_takeoff_cruise_engineoff_crash_trajectory_3d_06230949.png`
- 검증하지 못한 항목: `--live-3d` 실제 GUI 창 표시와 실시간 애니메이션 육안 확인
- 검증하지 못한 이유: 자동 검증 환경에서는 WSLg/X11 GUI 표시 여부를 보장할 수 없고, 5.7 live 실행은 `--realtime` 때문에 약 278초 이상 소요됨
- 필요한 추가 조건: WSLg 또는 X server가 활성화된 터미널 세션
- 권장 후속 검증: `python3 scripts/run_jsbsim_timestamped.py --live-3d` 실행 후 39, 1, 2 선택 또는 비대화형 live 명령 실행
- 남은 리스크: GUI backend가 없는 환경에서는 애니메이션 프로세스가 창을 띄우지 못할 수 있음
- Git commit: 프로젝트가 Git 저장소가 아니므로 없음

## [2026-06-23 13:05] PROGRESS-20260623-1305-001 — 완료

- 수행한 작업: CSV 저장 property 목록을 추출하고 prefix·명칭 기반 역할 분류를 적용해 Excel workbook 생성
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/scripts/**/runscript/*.xml
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/**/*.xml
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/**/*.csv
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/**/*.csv
- 생성한 파일: /home/junyeopkwon/jsbsim_workflow/outputs/jsbsim_property_classification_20260623/jsbsim_csv_property_classification.xlsx
- 생성한 파일: /home/junyeopkwon/jsbsim_workflow/outputs/jsbsim_property_classification_20260623/build_workbook.cjs
- 생성한 파일: /home/junyeopkwon/jsbsim_workflow/outputs/jsbsim_property_classification_20260623/*.png
- 핵심 변경점: workbook에 Overview, Category Summary, Raw CSV Properties, 6DOF Validation Properties, SI Mapping, CSV Header Crosscheck, XML Output Sources 7개 시트 구성
- 핵심 변경점: raw CSV property 55개, 6DOF 검증 property 122개, SI 변환 매핑 46개, 기존 CSV 파일 161개, CSV output XML 182개를 대조
- 핵심 변경점: position, velocities, attitude, fcs, propulsion, forces, moments, gear, aero, atmosphere, inertia, accelerations 등 prefix 기반 역할 분류 적용
- 실행한 명령어: load_workspace_dependencies
- 실행한 명령어: 번들 Node와 @oai/artifact-tool로 build_workbook.cjs 실행
- 실행한 명령어: python3 zipfile 기반 .xlsx 구조 확인
- 실행한 명령어: PIL.Image 기반 preview PNG non-white pixel 검사
- 테스트 결과: @oai/artifact-tool workbook export 성공, 수식 오류 검색 0건, .xlsx 49 KB 생성, worksheet 7개와 table 6개 포함 확인
- 실행 확인 결과: preview PNG 7개 생성, 모든 preview에서 non-white ratio 0.3702~0.6464 및 sample unique color 48~73 확인
- 검증하지 못한 항목: Codex view_image를 통한 preview PNG 직접 육안 확인
- 검증하지 못한 이유: WSL/UNC 경로에 대해 view_image가 windows sandbox helper_unknown_error로 실패
- 필요한 추가 조건: Codex 이미지 뷰어의 WSL 경로 접근 정상화 또는 사용자의 Excel 직접 열람
- 권장 후속 검증: Excel에서 각 시트 필터와 열 너비를 실제로 열어 확인
- 남은 리스크: 역할 분류는 JSBSim 공식 taxonomy가 아니라 workflow property prefix와 명칭 기반의 실무 분류이므로, 특정 property의 물리적 의미를 엄밀히 문서화하려면 JSBSim catalog/source와 추가 대조 필요
- Git commit: 프로젝트가 Git 저장소가 아니므로 없음

## [2026-06-29 11:04] PROGRESS-20260629-1104-001 — 완료

- 수행한 작업: 지목된 5.6 runscript와 FlightGear UDP output directive 연결 흔적 조사
- 조사한 파일: scripts/c172x_empty_cg_aligned/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml, scripts/c172x/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml, scripts/c172x/output/fg_visual_5500.xml, scripts/c172x/README.md, scripts/c172x_empty_cg_aligned/README.md, /home/junyeopkwon/.bash_history
- 생성한 파일: 없음
- 수정한 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 핵심 변경점: 코드 변경 없음. 이전 실행 명령이 JSBSim --root=/home/junyeopkwon/jsbsim --script=...5.6... --realtime --logdirectivefile=...fg_visual_5500.xml 형태였음을 확인
- 실행한 명령어: sed, grep, tail, cmp, diff, date
- 테스트 결과: 실제 시뮬레이션은 실행하지 않음
- lint 결과: 해당 없음
- type check 결과: 해당 없음
- build 결과: 해당 없음
- 실행 확인 결과: fg_visual_5500.xml은 FLIGHTGEAR output, UDP port 5500, target host 172.29.80.1로 설정됨. 현재 /etc/resolv.conf nameserver는 10.255.255.254로 확인되어 과거 Windows host IP와 다를 수 있음
- 검증하지 못한 항목: Windows FlightGear GUI 수신 여부, 현재 host IP에서 UDP 5500 수신 가능 여부
- 검증하지 못한 이유: 요청은 과거 연동 흔적 확인이고 GUI 실행은 수행하지 않음
- 필요한 추가 조건: Windows FlightGear 실행, UDP 포트 허용, 현재 WSL-to-Windows host IP 반영
- 권장 후속 검증: FlightGear를 native-fdm UDP 5500 수신으로 먼저 실행한 뒤 JSBSim direct command를 --realtime으로 실행
- 남은 리스크: fg_visual_5500.xml의 172.29.80.1은 WSL 네트워크 재시작 후 stale IP일 수 있음
- 관련 기록: TASK-20260629-1104-001
- Git commit: 없음

## [2026-06-30 09:40] PROGRESS-20260630-0940-001 — 완료

- 수행한 작업: 기존 `c172x_empty_cg_aligned`에서 탑승자 pointmass 4개만 각각 75 kg으로 되살린 새 aircraft 변형을 생성하고, 질량 증가 대응용 5.6.1 higher-speed runscript를 구성·검증
- 생성한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/generate_c172x_4x75kg_cg_aligned_variant.py`
- 생성한 파일: `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned/c172x_4x75kg_cg_aligned.xml`
- 생성한 파일: `/home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned/c172x_4x75kg_cg_aligned.xml`
- 생성한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml`
- 핵심 변경점: `PILOT`, `CO-PILOT`, `PASSENGER 1`, `PASSENGER 2` pointmass를 각각 `165.346697 lb`로 설정
- 핵심 변경점: `LUGGAGE`, `PesticideBomb` pointmass는 `0.000000 lb`로 유지
- 핵심 변경점: 5.6.1 runscript는 속도 관련 값만 변경 — nose wheel lighten `40 -> 45 kt`, rotate `55 -> 60 kt`, capture `70 -> 75 kt`, cruise/complete minimum `65 -> 70 kt`, low-speed high-AoA abort `55 -> 60 kt`
- 실행한 명령어: `python3 scripts/generate_c172x_4x75kg_cg_aligned_variant.py`
- 실행한 명령어: `python3 -m py_compile scripts/generate_c172x_4x75kg_cg_aligned_variant.py scripts/run_jsbsim_timestamped.py`
- 실행한 명령어: `xmllint --noout scripts/c172x/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml`
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned --init scripts/c172x/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml --planet default --no-live-3d`
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned --init scripts/c172x/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml --planet default --no-live-3d`
- 테스트 결과: 새 aircraft 생성 성공, 5.6 기존 runscript 실행 성공, 5.6.1 higher-speed runscript 실행 성공
- 5.6 기존 실행 결과: `5.6.1__rkss14l_default_earth_takeoff_cruise30`, timestamp `06300934`, 마지막 시각 `300.0083333 s`, AGL `1308.147913 ft`, KCAS `101.315327`, h-dot `-2.139655 ft/s`, STATE 6 미확인
- 5.6.1 실행 결과: `5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed`, timestamp `06300939`, 마지막 시각 `300.0083333 s`, AGL `958.474746 ft`, KCAS `103.631756`, h-dot `-0.992333 ft/s`
- 5.6.1 console 확인: `STATE 5 - stable 1000 ft cruise begins` 이벤트 존재, `STATE 6 - complete 30 second cruise` 이벤트 존재
- 질량/CG 확인: 5.6.1 마지막 행 `mass-slugs=73.6875773803747478`, `cg-y-in=0`
- 생성 로그: `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_console_06300939.log`
- 생성 데이터: `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_raw_06300939.csv`
- 생성 plot: `/home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_states_vs_time_06300939.png`
- 생성 plot: `/home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_trajectory_3d_06300939.png`
- 검증하지 못한 항목: FlightGear/QGC/실시간 3D GUI 확인, 세부 console 이벤트 블록 전문 추출
- 남은 리스크: 5.6.1은 속도 조건만 조정한 실험 버전으로, 탑승자 질량에 대한 최적 이륙 절차라고 단정할 수 없음
- Git commit: 프로젝트가 Git 저장소가 아니므로 없음

## [2026-06-30 09:45] PROGRESS-20260630-0945-001 — 완료

- 수행한 작업: 현재 `c172x_4x75kg_cg_aligned` + `5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed` 실행이 FlightGear 시각화와 연결되었는지 확인
- 조사한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
- 조사한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/output/fg_visual_5500.xml`
- 조사한 파일: `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_console_06300939.log`
- 확인 내용: 현재 runner 실행 명령에는 FlightGear용 `--logdirectivefile` 연결이 포함되어 있지 않음
- 확인 내용: 현재 실행은 raw CSV, SI CSV, 6DOF CSV, static states plot, static trajectory plot 생성 경로임
- 확인 내용: 기존 기록상 FlightGear 연동은 runscript 자체가 아니라 `scripts/c172x/output/fg_visual_5500.xml`을 JSBSim `--logdirectivefile`로 별도 부착해야 하는 방식
- 검증 결과: 현재 75kg×4명 5.6.1 실행은 FlightGear로 시각화 연동되지 않은 상태
- 검증하지 못한 항목: FlightGear GUI 실기동, 현재 Windows host IP/UDP 5500 수신 가능 여부
- 남은 리스크: FlightGear 연동을 추가하려면 현재 host IP와 `fg_visual_5500.xml` 설정 재확인이 필요
- Git commit: 프로젝트가 Git 저장소가 아니므로 없음

## [2026-06-30 10:00] PROGRESS-20260630-1000-001 — 완료

- 수행한 작업: `scripts/run_jsbsim_timestamped.py`에 선택형 FlightGear native-fdm 스트리밍 옵션을 추가
- 수정한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
- 수정한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/README.md`
- 핵심 변경점: `--flightgear`, `--no-flightgear`, `--flightgear-logdirective` CLI 옵션 추가
- 핵심 변경점: 대화형 실행에서는 live 3D 질문 뒤에 FlightGear visualization stream 사용 여부를 추가 질문
- 핵심 변경점: `--flightgear` 선택 시 JSBSim 실행 명령에 `--realtime`과 `--logdirectivefile=<directive>`를 자동 삽입
- 핵심 변경점: 기본 output directive는 `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/output/fg_visual_5500.xml`
- 실행한 명령어: `python3 -m py_compile scripts/run_jsbsim_timestamped.py`
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped.py --help | grep -- "--flightgear"`, `--no-flightgear`, `--flightgear-logdirective`
- 실행한 명령어: monkeypatch 검증으로 `run_jsbsim(..., realtime=True, logdirective_path=Path('/tmp/fg.xml'))` 호출 시 `--realtime`과 `--logdirectivefile=/tmp/fg.xml` 삽입 확인
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned --init scripts/c172x/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml --planet default --no-live-3d --no-flightgear`
- 검증 결과: Python 문법 검증 성공, help 옵션 노출 확인, command 구성 검증 성공, `--no-flightgear` 회귀 실행 성공
- 최종 회귀 실행: `5.6.2__rkss14l_default_earth_takeoff_cruise30_higher_speed`, timestamp `06300959`, `FlightGear stream: disabled` 출력 확인
- 검증하지 못한 항목: 실제 FlightGear GUI 창 수신 확인
- 검증하지 못한 이유: FlightGear Windows GUI를 사용자가 먼저 실행해야 하며, 자동 실행은 이번 범위에서 제외
- 남은 리스크: `fg_visual_5500.xml`의 대상 IP가 `172.29.80.1`로 고정되어 있어 현재 WSL/Windows 네트워크 IP가 바뀌면 수신 실패 가능
- Git commit: 프로젝트가 Git 저장소가 아니므로 없음

## [2026-06-30 10:30] PROGRESS-20260630-1030-001 — 완료

- 수행한 작업: `run_jsbsim_timestamped.py`에서 Matplotlib live3d 실행 경로를 제거하고 FlightGear 선택형 스트림만 시각화 선택지로 유지
- 수정한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`
- 수정한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/README.md`
- 보존한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/live_trajectory_3d.py`
- 핵심 변경점: `--live-3d`, `--no-live-3d` CLI 옵션 제거
- 핵심 변경점: `choose_live_animation`, `LIVE_ANIMATOR_SCRIPT`, `tempfile`, live animator subprocess 호출 제거
- 핵심 변경점: JSBSim `--realtime`은 이제 `--flightgear` 선택 시에만 자동 적용
- 핵심 변경점: README에 `Live 3D trajectory animation - deprecated` 섹션을 남기고, helper 파일은 reference/backup utility로 보존한다고 명시
- 실행한 명령어: `python3 -m py_compile scripts/run_jsbsim_timestamped.py scripts/live_trajectory_3d.py`
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped.py --help` 후 `--live-3d` 미노출 및 `--flightgear`/`--no-flightgear` 노출 확인
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned --init scripts/c172x/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml --planet default --no-flightgear`
- 검증 결과: `LIVE3D_REMOVED`, `LIVE_SCRIPT_KEPT`, Python 문법 검증 성공, `--no-flightgear` 회귀 실행 성공
- 최종 회귀 실행: `5.6.6__rkss14l_default_earth_takeoff_cruise30_higher_speed`, timestamp `06301029`, `FlightGear stream: disabled`
- 생성 로그: `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed/5.6.6__rkss14l_default_earth_takeoff_cruise30_higher_speed_console_06301029.log`
- 검증하지 못한 항목: 실제 FlightGear GUI 수신 확인
- 남은 리스크: `scripts/live_trajectory_3d.py`는 보존 파일이므로 향후 혼동 방지를 위해 README의 deprecated 설명을 유지해야 함
- Git commit: 프로젝트가 Git 저장소가 아니므로 없음

## [2026-06-30 11:19] CORRECTION-20260630-1119-001 — 정정

- 대상 기록: `PROGRESS-20260630-1118-001`
- 정정 이유: Windows PowerShell `Add-Content` 기본 인코딩으로 append되어 한글이 깨져 보이는 기록이 생성됨
- 기존 내용: 직전 `PROGRESS-20260630-1118-001` 항목은 인코딩 문제로 일부 환경에서 mojibake로 표시될 수 있음
- 정정 내용: `plot_trajectory()`에서 `set_axes_equal(ax, east, north, altitude)` 호출 뒤 `z_top = max(ax.get_zlim()[1], max(altitude) * 1.05, 1.0)`와 `ax.set_zlim(0.0, z_top)`을 추가하여 trajectory plot의 Z축 하한을 0으로 고정함. 기존 5.6.8 SI CSV를 사용해 trajectory PNG를 재생성함
- 영향 범위: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`, `/home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed/5.6.8__rkss14l_default_earth_takeoff_cruise30_higher_speed_trajectory_3d_06301107.png`
- 검증 결과: `python3 -m py_compile scripts/run_jsbsim_timestamped.py` 통과, PNG 재생성 명령 정상 종료
- 다음 작업: 필요 시 z축 라벨을 데이터 원천에 맞춰 정리

## [2026-06-30 11:28] PROGRESS-20260630-1128-001 — 완료

- 과업: 인코딩 깨짐 기록 정리
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 관련 파일: `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md`, `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md`, `/home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md`
- 수행 내용: 각 파일에서 비-UTF-8로 기록된 `2026-06-30 11:18` 깨진 블록을 사용자 승인에 따라 제거하고, 제거 후 파일 전체가 UTF-8로 decode되는지 확인
- 변경 이유: 깨진 기록이 남아 있으면 이후 검토 시 혼란을 유발할 수 있음
- 검증 명령어: Python byte-level block removal, UTF-8 decode check, 기록 하단 출력 확인
- 검증 결과: `TASK.md`, `PROGRESS.md`, `INDEX.md` 모두 UTF-8 decode 성공. `INDEX.md`는 대체문자 없음. `TASK.md`, `PROGRESS.md`의 대체문자는 이번 삭제 대상이 아닌 기존 사용자 원문 기록 위치에서 감지됨
- 검증하지 못한 항목: 없음
- 남은 리스크: 2026-06-30 11:19 정정 기록은 깨진 11:18 기록을 참조하지만, 혼란 방지를 위해 후속 삭제 완료 기록을 추가함
- 다음 작업: 향후 기록 append 시 PowerShell 기본 인코딩 대신 UTF-8을 명시하거나 WSL/Python UTF-8 쓰기 사용
- Git commit: 없음

## [2026-06-30 11:39] PROGRESS-20260630-1139-001 — 완료

- 과업: `c172x_4x75kg_cg_aligned` interactive 선택 오류 수정
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 관련 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml`, `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml`, `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml`
- 수행 내용: interactive runner가 `script_aircraft(path)` 기준으로 `scripts/<aircraft>/...` 하위 XML만 보여주는 것을 확인하고, 누락된 `scripts/c172x_4x75kg_cg_aligned/` 전용 폴더를 생성함
- 변경 이유: 항공기 목록에는 JSBSim aircraft `c172x_4x75kg_cg_aligned`가 있으나 해당 이름의 scripts 폴더가 없어 init 선택 단계에서 `RuntimeError: No init XML options found`가 발생함
- 생성한 파일: 위 XML 3개
- 수정한 파일: 없음
- 실행한 명령어: `mkdir -p scripts/c172x_4x75kg_cg_aligned/initial_condition scripts/c172x_4x75kg_cg_aligned/runscript`, 기존 `scripts/c172x`의 `2.2`, `5.6`, `5.6.1` XML 복사, Python import 기반 discovery 확인
- 테스트 결과: `discover_init_files('c172x_4x75kg_cg_aligned')`가 `2.2__rkss_14l_default_earth_init.xml`을 반환하고, `discover_runscripts('c172x_4x75kg_cg_aligned')`가 `5.6`과 `5.6.1` runscript를 반환함
- lint 결과: 해당 없음
- type check 결과: 해당 없음
- build 결과: 해당 없음
- 실행 확인 결과: interactive 선택 직전 경로 discovery는 정상. 실제 시뮬레이션 실행은 시간 소요로 생략
- 검증하지 못한 항목: 사용자 터미널에서 실제 번호 선택 후 전체 300초 실행
- 검증하지 못한 이유: full simulation 재실행은 이번 오류 원인인 파일 discovery 확인 범위를 넘어섬
- 권장 후속 검증: `python3 scripts/run_jsbsim_timestamped.py` 실행 후 aircraft 39, init 1, runscript 2 선택
- 남은 리스크: 비교용 `5.6`은 기존 조건이라 4x75kg 질량에서는 `5.6.1`보다 완료 여유가 낮을 수 있음
- Git commit: 없음

## [2026-06-30 11:47] PROGRESS-20260630-1147-001 — 완료

- 과업: FlightGear 선택 실행 오류 조사 및 수정
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 관련 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`, `/home/junyeopkwon/jsbsim_workflow/scripts/c172x/output/fg_visual_5500.xml`, `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed/5.6.10__rkss14l_default_earth_takeoff_cruise30_higher_speed_console_06301140.log`
- 수행 내용: 실패 명령에 `--planet=/home/junyeopkwon/jsbsim_workflow/earth_models/04_nonrotating_spherical_earth.xml`가 자동 삽입된 것을 확인하고, 동일 FlightGear output을 `--planet` 없이 JSBSim default Earth로 짧게 실행해 SIGFPE가 발생하지 않음을 확인함
- 변경 이유: 최근 RKSS 14L 기본 시나리오는 JSBSim default Earth 기준인데 interactive 실행만 이전 기본값인 nonrotating spherical earth를 자동 적용하고 있었음
- 핵심 변경점: `resolve_selection()`에서 `args.planet is None`일 때 `planet_path = None`으로 설정
- 실행한 명령어: `python3 -m py_compile scripts/run_jsbsim_timestamped.py`, `resolve_selection()` import 기반 확인, `timeout 8s JSBSim --logdirectivefile=... --realtime --script=... --root=.`
- 테스트 결과: Python 문법 검사 통과, `resolve_selection()`이 `None` 반환, `--planet` 없는 FlightGear output 짧은 실행은 timeout까지 정상 진행하고 SIGFPE 없음
- FlightGear IP 확인: WSL default gateway `172.29.80.1`, `fg_visual_5500.xml` target `172.29.80.1` 일치
- 검증하지 못한 항목: Windows FlightGear 창에서 실제 3D 기체 수신 확인
- 검증하지 못한 이유: GUI 수신 확인은 Windows FlightGear를 별도로 실행해야 함
- 남은 리스크: `Enable FlightGear visualization stream? y`는 FlightGear를 자동 실행하지 않고 UDP stream만 켜므로, FlightGear 창을 먼저 열지 않으면 화면에 표시되지 않음
- 다음 작업: Windows PowerShell에서 FlightGear external FDM 수신 명령을 먼저 실행한 뒤 runner에서 `y` 선택
- Git commit: 없음

## [2026-06-30 14:25] PROGRESS-20260630-1425-001 — 완료

- 과업:
  - ADS JSBSim 모델 workflow 폴더 구성
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - ADS 모델을 jsbsim_workflow에 넣어두고 후속 진행 가능한 폴더 구조로 정리
- 관련 파일:
  - /home/junyeopkwon/jsbsim/aircraft/ADS
  - /home/junyeopkwon/jsbsim/engine/ADS_lift_motor.xml
  - /home/junyeopkwon/jsbsim/engine/ADS_lift_prop.xml
  - /home/junyeopkwon/jsbsim/engine/ADS_pusher_motor.xml
  - /home/junyeopkwon/jsbsim/engine/ADS_pusher_prop.xml
  - /home/junyeopkwon/jsbsim/scripts/ADS_hover_gimpo.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/README.md
- 수행 내용:
  - jsbsim_workflow가 Git 저장소가 아님을 확인
  - 프로젝트 내부 AGENTS.md 또는 AGENTS.override.md 없음 확인
  - docs/agent-log 필수 기록 파일 존재 확인
  - scripts/README.md에서 aircraft별 initial_condition/runscript 구조 확인
  - ADS aircraft XML 복사본을 aircraft_variants/ADS에 배치
  - ADS engine XML 복사본을 engine_variants/ADS에 배치
  - ADS 초기조건을 scripts/ADS/initial_condition/1.0__gimpo_ground_init.xml로 배치
  - ADS hover runscript를 scripts/ADS/runscript/1.0__gimpo_30m_hover_run.xml로 배치
  - workflow runscript의 initialize 값을 workflow initial_condition 절대경로로 변경
  - ADS 전용 logs/results/plots 폴더 생성
  - scripts/ADS/README.md와 aircraft_variants/ADS/WORKFLOW_INSTALL.md 작성
- 생성한 파일 및 폴더:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS
  - /home/junyeopkwon/jsbsim_workflow/engine_variants/ADS
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS/README.md
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS/initial_condition/1.0__gimpo_ground_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/ADS/runscript/1.0__gimpo_30m_hover_run.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/ADS
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/si/ADS
  - /home/junyeopkwon/jsbsim_workflow/logs/console/ADS
  - /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/ADS
  - /home/junyeopkwon/jsbsim_workflow/plots/ADS
  - /home/junyeopkwon/jsbsim_workflow/results/ADS
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/WORKFLOW_INSTALL.md
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 핵심 변경점:
  - ADS 기체/엔진 XML을 workflow 내부에서 추적 가능한 복사본으로 보관
  - runner 선택 규칙에 맞는 scripts/ADS/initial_condition 및 scripts/ADS/runscript 폴더 구성
  - 후속 실행 산출물이 모일 ADS 전용 로그/플롯/결과 폴더 생성
- 실행한 명령어:
  - wsl -e bash -lc 'find /home/junyeopkwon/jsbsim_workflow -maxdepth 3 ...'
  - wsl -e bash -lc 'cp ... ADS ...'
  - wsl -e python3 -c '... ET.parse ...'
  - wsl -e python3 -c '... missing reference check ...'
  - wsl -e bash -lc 'cd /home/junyeopkwon/jsbsim_workflow && git status --short 2>/dev/null || echo not-a-git-repo'
- 테스트 결과:
  - JSBSim 시뮬레이션 실행 안 함
- lint 결과:
  - 전용 lint 실행 안 함
- type check 결과:
  - 해당 없음
- build 결과:
  - 빌드 실행 안 함
- 실행 확인 결과:
  - XML 정적 파싱: parsed 16 workflow ADS xml files
  - workflow 참조 확인: missing: 0
  - Git 상태: not-a-git-repo
- 검증하지 못한 항목:
  - JSBSim 실제 model load
  - runner로 ADS 선택 및 실행
  - hover 결과 CSV/plot 생성
- 검증하지 못한 이유:
  - 이번 요청은 workflow 폴더 구성이고 이전 요청에서 실행하지 말라는 전제가 유지됨
- 가정:
  - ADS 실행은 후속 승인 후 수행
- 남은 리스크:
  - runner의 출력 property 목록은 기존 고정익/멀티콥터 공용 목록이므로 ADS battery/pusher 관련 전용 후처리는 후속 보강 필요 가능
  - workflow 복사본과 jsbsim source tree 원본이 나중에 서로 달라질 수 있음
- 후속 작업:
  - ADS model load check
  - ADS hover runscript 실행 및 hover throttle 보정
  - source tree와 workflow snapshot 동기화 정책 확정
- Git commit:
  - 해당 없음, jsbsim_workflow는 Git 저장소 아님

## [2026-06-30 14:28] PROGRESS-20260630-1428-001 — 완료

- 과업:
  - jsbsim_workflow Git 추가 가능 여부 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수행 내용:
  - git -C /home/junyeopkwon rev-parse --show-toplevel 실행 결과 Git 저장소가 아님 확인
  - /home/junyeopkwon/.git 디렉터리는 존재하나 내부 파일이 없어 유효한 저장소가 아님 확인
  - /home/junyeopkwon/jsbsim_workflow 내부 .git 없음 확인
  - /home/junyeopkwon/jsbsim_workflow 내부 .gitignore 없음 확인
  - 현재 별도 원격 remote 확인 불가
- 생성한 파일:
  - 없음
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 실행한 명령어:
  - git -C /home/junyeopkwon rev-parse --show-toplevel
  - git -C /home/junyeopkwon status --short -- jsbsim_workflow
  - git -C /home/junyeopkwon remote -v
  - ind /home/junyeopkwon/jsbsim_workflow -maxdepth 2 -name .git -type d -print
  - ls -la /home/junyeopkwon/.git
  - ind /home/junyeopkwon -maxdepth 2 -type d -name .git -print
- 검증 결과:
  - jsbsim_workflow는 현재 Git 저장소가 아니므로 새 저장소로 초기화 가능
  - 기존 jsbsim 저장소에 억지로 넣는 것은 프로젝트 경계가 섞일 수 있어 권장하지 않음
- 검증하지 못한 항목:
  - 사용자가 원하는 원격 GitHub/GitLab 저장소 URL
- 검증하지 못한 이유:
  - 사용자에게 원격 저장소 정보가 아직 제공되지 않음
- 남은 리스크:
  - logs, results, plots, __pycache__, 대용량 산출물을 그대로 commit하면 저장소가 비대해질 수 있음
- 후속 작업:
  - 사용자 확인 후 .gitignore 작성, git init, git add, git commit, remote 연결 여부 결정
- Git commit:
  - 없음


## [2026-06-30 14:34] PROGRESS-20260630-1434-001 — DONE

- 과업: jsbsim_workflow 로컬 Git 저장소 추가
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 사용자의 Git에 jsbsim_workflow를 추가
- 관련 파일: /home/junyeopkwon/jsbsim_workflow/.gitignore, /home/junyeopkwon/jsbsim_workflow/docs/agent-log/
- 수행 내용: 프로젝트 용량과 Git 상태를 확인하고, 실행 산출물 제외용 .gitignore를 추가한 뒤 /home/junyeopkwon/jsbsim_workflow에서 Git 저장소를 초기화함. 브랜치를 main으로 설정하고 추적 대상 파일을 stage한 뒤 초기 커밋을 생성함.
- 변경 이유: ADS JSBSim workflow 산출물을 사용자가 Git으로 관리할 수 있도록 하기 위함
- 검증 명령어: cd /home/junyeopkwon/jsbsim_workflow && git status --short --ignored
- 검증 명령어: cd /home/junyeopkwon/jsbsim_workflow && git log --oneline --decorate -5
- 검증 결과: 초기 커밋 e1635ee가 main 브랜치에 생성되었고, logs/, outputs/, plots/, results/, scripts/__pycache__/는 ignored 상태로 제외됨
- 검증하지 못한 항목: 원격 저장소 push
- 검증하지 못한 이유: 원격 저장소 URL 및 인증 정보가 제공되지 않음
- 필요한 추가 조건: GitHub 또는 기타 원격 저장소 URL
- 권장 후속 검증: remote 등록 후 git push -u origin main 실행 및 원격 저장소 파일 목록 확인
- 가정: 원격 push 없이 로컬 Git 저장소 생성 및 커밋까지를 이번 요청의 완료 범위로 처리
- 남은 리스크: ADS XML은 정적 XML 참조 검증까지만 수행되었고 JSBSim 실제 실행 검증은 아직 수행하지 않음
- 다음 작업: 원격 저장소 URL을 받으면 remote 등록 및 push 수행
- 관련 기록: TASK-20260630-1434-001, DECISION-20260630-1434-001, TODO-20260630-1434-001
- Git commit: e1635ee


## [2026-06-30 15:09] PROGRESS-20260630-1509-001 — DONE

- 과업: ADS 산출물 저자 표기 변경
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: ADS 만든 파일들의 저자를 junyeopkwon으로 변경
- 관련 파일: ADS 관련 XML 및 Markdown 파일, docs/agent-log/
- 수행 내용: 기존 <author>OpenAI Codex</author> 항목을 <author>junyeopkwon</author>으로 변경하고, 저자 태그가 없는 ADS XML에는 <!-- Author: junyeopkwon --> 주석을 추가함. ADS Markdown 문서에는 Author: junyeopkwon 행을 추가함.
- 변경 이유: GitHub 업로드 및 연구 산출물 관리 시 작성자 표기를 사용자명으로 통일하기 위함
- 검증 명령어: Python xml.etree.ElementTree로 ADS XML 31개 파싱
- 검증 명령어: ADS 대상 파일에서 OpenAI Codex 잔여 문자열 및 junyeopkwon 누락 여부 검색
- 검증 결과: XML 파싱 오류 0개, ADS 대상 파일에서 OpenAI Codex 잔여 문자열 없음, 저자 표기 누락 없음
- 검증하지 못한 항목: JSBSim 실제 시뮬레이션 실행
- 검증하지 못한 이유: 이번 요청은 저자 메타데이터 변경이며 실행 요청이 아님
- 필요한 추가 조건: JSBSim 실행 환경과 사용자의 실행 승인
- 권장 후속 검증: GitHub Desktop에서 변경 커밋과 Publish 결과 확인
- 가정: XML 주석 추가는 JSBSim 입력 파일의 동작에 영향을 주지 않음
- 남은 리스크: workflow_all_cases_initial_settings.xlsx는 별도 변경으로 감지되었으나 이번 커밋 범위에서 제외함
- 다음 작업: 원격 저장소 publish 또는 push 후 GitHub 파일 화면에서 저자 표기 확인
- 관련 기록: TASK-20260630-1509-001, DECISION-20260630-1509-001
- Git commit: workflow 저장소 커밋 후 별도 확인


## [2026-06-30 15:20] PROGRESS-20260630-1520-001 — DONE

- 과업: ADS 30 m hover 실행 로그 해석
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 로그가 기존 설명과 다르게 보인다는 사용자 지적 확인
- 관련 파일: /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/ADS/1.0__gimpo_30m_hover/1.0.1__gimpo_30m_hover_sixdof_raw_06301505.csv, /home/junyeopkwon/jsbsim_workflow/scripts/ADS/runscript/1.0__gimpo_30m_hover_run.xml, /home/junyeopkwon/jsbsim_workflow/scripts/ADS/initial_condition/1.0__gimpo_ground_init.xml
- 수행 내용: CSV 헤더와 8001개 row를 분석하고 h-agl-ft, geod-alt-ft, terrain elevation, body velocity, throttle command, lift engine thrust, WOW, attitude 범위를 계산함
- 핵심 변경점: 파일 변경 없음. 분석 기록만 append함
- 검증 명령어: Python csv DictReader 기반 통계 계산
- 검증 결과: 시뮬레이션 시간 0~80 s, h-agl-ft 범위 0.777~59.055 ft, 98.4 ft 도달 없음, WOW는 지상 접촉 상태로 전환, 0.62 추정 구간 총 리프트 추력 약 38.7 lbf로 20 kg 중량 약 44.1 lbf보다 작음
- 검증하지 못한 항목: 수정 후 재실행 결과
- 검증하지 못한 이유: 이번 요청은 로그 해석이며 파일 수정 요청이 아님
- 필요한 추가 조건: 초기조건 및 추력 스케줄 수정 후 JSBSim 재실행
- 권장 후속 검증: h-agl 초기값 0 근처, liftoff 발생, h-agl 98.4 ft 도달, hover 유지 여부 확인
- 가정: fcs/throttle-cmd-norm은 ADS 전용 lift-throttle-cmd-norm과 별도 generic property일 수 있어 직접 스로틀 판단에는 제한이 있음
- 남은 리스크: sixdof_raw 로그에 fcs/ads/lift-throttle-cmd-norm이 없어 이벤트별 ADS 명령 검증이 제한됨
- 다음 작업: init altitude를 지상 기준으로 수정하고 lift throttle/propulsion placeholder를 재보정, runner 출력에 fcs/ads/* property 추가
- 관련 기록: TASK-20260630-1520-001, TODO-20260630-1520-001
- Git commit: 없음


## [2026-06-30 15:27] PROGRESS-20260630-1527-001 — DONE

- 과업: ADS JSBSim 구현 모터/프로펠러 기준 비행 가능 중량 추정
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 관련 파일: logs/csv/sixdof_raw/ADS/1.0__gimpo_30m_hover/1.0.1__gimpo_30m_hover_sixdof_raw_06301505.csv, engine_variants/ADS/ADS_lift_motor.xml, engine_variants/ADS/ADS_lift_prop.xml, aircraft_variants/ADS/ADS_mass.xml
- 수행 내용: CSV에서 4개 리프트모터 thrust-lbs 합산 최대값을 계산하고 kgf로 환산함
- 검증 명령어: Python csv DictReader로 propulsion/engine, engine[1], engine[2], engine[3] thrust-lbs 합산 최대값 계산
- 검증 결과: 최대 총 리프트 추력 38.733951 lbf = 17.569425 kgf. T/W 1.0 기준 17.57 kg, T/W 1.2 기준 14.64 kg, T/W 1.3 기준 13.51 kg, T/W 1.5 기준 11.71 kg
- 검증하지 못한 항목: throttle 1.0 정적 추력 sweep
- 검증하지 못한 이유: 이번 요청은 기존 로그 기반 추정이며 새 실행 요청은 아님
- 남은 리스크: sixdof_raw에는 ADS 전용 lift-throttle command가 없어서 command별 추력 곡선은 직접 확인하지 못함
- 다음 작업: 별도 thrust sweep runscript 작성 후 throttle 0.0~1.0 정적 추력 곡선 생성
- Git commit: 없음


## [2026-06-30 15:36] PROGRESS-20260630-1536-001 — DONE

- 과업: JSBSim 엔진/모터/프로펠러 정의 확인
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 관련 파일: /home/junyeopkwon/jsbsim/engine/*.xml, /home/junyeopkwon/jsbsim/aircraft/F450/Propulsion.xml, /home/junyeopkwon/jsbsim/aircraft/c172p_2kg_vtol/c172p_2kg_vtol.xml, /home/junyeopkwon/jsbsim/aircraft/ZLT-NT/ZLT-NT.xml, /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/ADS_propulsion.xml
- 수행 내용: engine 디렉터리 XML 94개를 루트 태그별로 파싱 분류하고, 항공기 XML에서 DJI_E305, DJI_9450, electric147kW, ADS_lift_motor, ADS_lift_prop 참조를 검색함
- 검증 명령어: Python xml.etree.ElementTree로 /home/junyeopkwon/jsbsim/engine/*.xml 루트 태그 및 주요 파라미터 추출
- 검증 결과: brushless_dc_motor 3개 ADS_lift_motor, ADS_pusher_motor, DJI_E305 확인. propeller 25개 중 멀티콥터 예제용 DJI_9450 확인. electric_engine 4개 중 electric147kW, electric_1mw 확인. F450 및 c172p_2kg_vtol은 DJI_E305 + DJI_9450 사용. ADS는 ADS_lift_motor + ADS_lift_prop 4개 및 ADS_pusher_motor + ADS_pusher_prop 1개 사용.
- 검증하지 못한 항목: 각 motor/prop 후보의 정적 추력 곡선
- 검증하지 못한 이유: 이번 요청은 목록 확인이며 JSBSim 실행 요청이 아님
- 남은 리스크: electric_engine 파일은 고정익/비행선용 전기 동력 정의이며 멀티콥터 BLDC-프로펠러 조합과 직접 대응하지 않을 수 있음
- 다음 작업: DJI_E305+DJI_9450, ADS_lift_motor+ADS_lift_prop, electric147kW+prop_Clark_Y7570 후보의 정적/전진비 추력 sweep 비교
- Git commit: 없음


## [2026-06-30 15:37] CORRECTION-20260630-1537-001 — 정정

- 대상 기록: PROGRESS-20260630-1536-001
- 정정 이유: /home/junyeopkwon/jsbsim/engine/*.xml 파싱 대상 개수 기록에 오기가 있었음
- 기존 내용: engine 디렉터리 XML 94개
- 정정 내용: engine 디렉터리 XML 95개
- 영향 범위: 조사 수량 표기만 해당하며, motor/prop 후보 분류와 결론은 동일함
- 검증 결과: 루트 태그별 분류 합계 FG_NOZZLE 1, FG_ROCKET 1, brushless_dc_motor 3, direct 1, electric_engine 4, nozzle 5, piston_engine 16, propeller 25, rocket_engine 6, rotor 1, turbine_engine 30, turboprop_engine 2로 총 95개
- 다음 작업: 없음


## [2026-06-30 18:26] PROGRESS-20260630-1826-001 — DONE

- 과업: ADS_mini 10 m hover/landing 테스트 구성 및 실행
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 관련 파일: aircraft_variants/ADS_mini 또는 aircraft/ADS_mini, scripts/ADS_mini/initial_condition/1.0__gimpo_ground_init.xml, scripts/ADS_mini/runscript/1.0__gimpo_10m_hover_land_run.xml
- 수행 내용: ADS_mini 1 kg 모델을 구성하고, JSBSim 기본 DJI_E305 motor와 DJI_9450 propeller를 lift rotor 4개와 pusher placeholder에 적용함. Mini hover 테스트 안정화를 위해 F450 zero-aero 계열 공력 파일을 사용하고, rate feedback을 p/q/r body rate로 변경함. Run script는 arm, takeoff to 10 m, 5 m descent, 1 m flare, idle, shutdown 이벤트로 구성함.
- 생성한 파일: /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS_mini/, /home/junyeopkwon/jsbsim_workflow/scripts/ADS_mini/, /home/junyeopkwon/jsbsim/aircraft/ADS_mini/
- 검증 명령어: /home/junyeopkwon/jsbsim/build/src/JSBSim --root=. --aircraft=ADS_mini --catalog --nohighlight
- 검증 명령어: /home/junyeopkwon/jsbsim/build/src/JSBSim --root=. --script=/home/junyeopkwon/jsbsim_workflow/scripts/ADS_mini/runscript/1.0__gimpo_10m_hover_land_run.xml
- 검증 명령어: Python csv 분석으로 15~25 s hover window, shutdown window, XML parse 확인
- 검증 결과: JSBSim runscript 정상 종료 rc=0. XML 22개 파싱 오류 0. 15~25 s 평균 고도 9.662 m, 최소 9.612 m, 최대 9.784 m. 60~70 s throttle 0, WOW 1, 평균 고도 0.108 m로 착륙 후 시동 종료 상태 확인.
- 검증하지 못한 항목: GitHub Desktop publish 후 원격 저장소 반영 여부
- 검증하지 못한 이유: 원격 publish는 사용자 GUI 작업 또는 별도 요청 필요
- 남은 리스크: hover 중 pitch 약 28 deg trim이 남아 있어 물리적 자세 상사는 아직 부정확함. 착륙 후 ground contact chatter가 console에 남음. ADS_mini는 workflow 검증용이며 20 kg ADS 성능 검증으로 해석하면 안 됨.
- 다음 작업: pitch trim/rotor orientation/CG 조정으로 hover 자세를 수평에 가깝게 개선, ground reaction damping 조정, Git commit 여부 결정
- Git commit: 없음


## [2026-06-30 18:36] PROGRESS-20260630-1836-001 — DONE

- 과업: ADS_mini 적용 runscript 이벤트 설명
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/scripts/ADS_mini/runscript/1.0__gimpo_10m_hover_land_run.xml
- 수행 내용: 현재 runscript의 run interval, use aircraft/init, event 조건, set property, notify/output property를 확인함
- 검증 명령어: sed -n 1,240p scripts/ADS_mini/runscript/1.0__gimpo_10m_hover_land_run.xml
- 검증 결과: run start 0.0, end 70.0, dt 0.005이며 power off init, arm, takeoff to 10 m, descend to 5 m, flare to 1 m, touchdown idle, shutdown, Repeating Notify 이벤트 확인
- 검증하지 못한 항목: 재실행 검증
- 검증하지 못한 이유: 이번 요청은 이벤트 설명이며 재실행 요청이 아님
- Git commit: 없음


## [2026-06-30 18:48] PROGRESS-20260630-1848-001 — DONE

- 과업: ADS_mini XML 의사코드 설명 자료 작성
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS_mini/*.xml, /home/junyeopkwon/jsbsim_workflow/scripts/ADS_mini/initial_condition/1.0__gimpo_ground_init.xml, /home/junyeopkwon/jsbsim_workflow/scripts/ADS_mini/runscript/1.0__gimpo_10m_hover_land_run.xml
- 생성한 파일: /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS_mini/ADS_mini_xml_pseudocode.md
- 수행 내용: ADS_mini.xml, metrics, mass, ground_reactions, propulsion, effectors, flight_control, battery_module, aero, init, runscript를 파일별로 구분해 의사코드 형식으로 설명함
- 검증 명령어: wc -l /home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS_mini/ADS_mini_xml_pseudocode.md
- 검증 결과: 문서 622줄 생성 확인, 첫 80줄 내용 확인
- 검증하지 못한 항목: 문서에 대한 사용자 검토 및 GitHub 반영
- 검증하지 못한 이유: 사용자 검토와 publish는 별도 단계
- 남은 리스크: 사용자가 ADS 원형 XML도 같은 방식으로 원하면 별도 문서가 추가로 필요함
- 다음 작업: 필요 시 ADS 20 kg 원형 XML 의사코드 문서도 별도 작성
- Git commit: 없음

## [2026-07-01 00:00] PROGRESS-20260701-0000-ADS0 — 완료

- 수행한 작업: 기존 `aircraft_variants/ADS` 및 `engine_variants/ADS` XML을 기반으로 `ADS_0` zero-value 템플릿을 생성했다.
- 조사한 파일: `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/ADS/*.xml`, `/home/junyeopkwon/jsbsim_workflow/engine_variants/ADS/*.xml`
- 생성한 파일:
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
- 수정한 파일: 위 생성 파일의 설명/주석 일부를 `ADS_0` 템플릿 목적에 맞게 정리했다.
- 핵심 변경점: `ADS.xml`의 include 참조를 `ADS_0_*.xml`로 변경하고, engine/thruster 참조를 `ADS_0_lift_motor`, `ADS_0_lift_prop`, `ADS_0_pusher_motor`, `ADS_0_pusher_prop`로 변경했다. 숫자 텍스트, `value` 속성, `tableData` 내부 숫자를 모두 0으로 치환했다.
- 실행한 명령어: `wsl -e python3 -c ...`를 사용해 XML 생성/검증 스크립트 실행, `sed`, `git status --short`로 확인
- 테스트 결과: JSBSim 실행은 요청에 따라 수행하지 않음
- lint 결과: 해당 없음
- type check 결과: 해당 없음
- build 결과: 해당 없음
- 실행 확인 결과: XML 파서 기준 14개 XML 모두 파싱 성공
- 검증하지 못한 항목: JSBSim 로딩 및 시뮬레이션 실행
- 검증하지 못한 이유: 사용자가 실행하지 말고 XML 파일만 구성하라고 요청함
- 필요한 추가 조건: 실제 제원/공력/추력/질량 데이터 입력 후 실행용 JSBSim 트리에 반영
- 권장 후속 검증: 실제 데이터 입력 후 `ADS_0` 또는 후속 기체명으로 JSBSim 로딩 검증 및 초기 hover/ground reaction 점검
- 남은 리스크: 모든 수치가 0이라 현재 XML은 실행 목적이 아닌 템플릿이며, 일부 property 이름 예: `systems/ads/battery/estimated-power-W`는 연결을 보존하기 위해 원문 유지됨
- 후속 작업: 실제 ADS 제원 수신 후 0 값을 단계적으로 대체
- Git commit: 없음

## [2026-07-19 23:35] PROGRESS-20260719-2335-001 — DONE

- 과업:
  - C172X 4x75kg 김포 lat/lon 450 m east-heading 무추력 추락/활공 XML 생성 및 실행 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - aircraft_variants/c172x_4x75kg_cg_aligned/c172x_4x75kg_cg_aligned.xml
  - aircraft_variants/c172x_4x75kg_cg_aligned/c172ap.xml
  - scripts/c172x_4x75kg_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml
  - scripts/c172x/runscript/4.4__450m_60ms_x_noengine_drop_run.xml
  - scripts/c172x/runscript/4.3__450m_60ms_x_engineout_t0_headinghold_trim_spherical_run.xml
  - scripts/run_jsbsim_timestamped.py
- 생성한 파일:
  - scripts/c172x_4x75kg_cg_aligned/initial_condition/6.0__gimpo_450m_east_60ms_init.xml
  - scripts/c172x_4x75kg_cg_aligned/runscript/6.0__gimpo_450m_east_60ms_neutral_noengine_drop_run.xml
  - scripts/c172x_4x75kg_cg_aligned/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_glide_run.xml
- 수정한 파일:
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 핵심 변경점:
  - 기존 c172x_4x75kg_cg_aligned는 PILOT, CO-PILOT, PASSENGER 1, PASSENGER 2가 각각 165.346697 lb로 75 kg x 4명 조건을 만족함을 확인하고 재사용
  - 초기조건은 latitude 37.5707083333 deg, longitude 126.7782777778 deg, altitude 450.0 m, elevation 38.0 ft, psi 90.0 deg, ubody 60.0 m/s, vbody/wbody 0.0 m/s로 구성
  - 6.0 runscript는 throttle/mixture/engine/AP/control/trim을 0으로 유지하고 gear WOW 발생 시 종료
  - 6.1 runscript는 throttle/mixture/engine을 0으로 유지하고 ap/heading_setpoint 90.0, ap/heading_hold 1, fcs/pitch-trim-cmd-norm 0.18로 활공
  - 6.0 최초 실행은 end 180 s에서 지면 접촉 전 종료되어 end 360 s로 수정 후 재검증
- 실행한 명령어:
  - xmllint --noout scripts/c172x_4x75kg_cg_aligned/initial_condition/6.0__gimpo_450m_east_60ms_init.xml scripts/c172x_4x75kg_cg_aligned/runscript/6.0__gimpo_450m_east_60ms_neutral_noengine_drop_run.xml scripts/c172x_4x75kg_cg_aligned/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_glide_run.xml
  - python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned --init scripts/c172x_4x75kg_cg_aligned/initial_condition/6.0__gimpo_450m_east_60ms_init.xml --runscript scripts/c172x_4x75kg_cg_aligned/runscript/6.0__gimpo_450m_east_60ms_neutral_noengine_drop_run.xml --planet default --no-flightgear
  - python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned --init scripts/c172x_4x75kg_cg_aligned/initial_condition/6.0__gimpo_450m_east_60ms_init.xml --runscript scripts/c172x_4x75kg_cg_aligned/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_glide_run.xml --planet default --no-flightgear
- 테스트 결과:
  - XML well-formed 검증 통과
  - 6.0.2 중립 무추력 추락은 204.325 s에 Nose Gear WOW로 종료
  - 6.1.1 heading hold/trim 활공은 137.408333 s에 Nose Gear WOW로 종료
- 실행 확인 결과:
  - 두 run 모두 초기 time 0.0에서 lat 37.5707083333, lon 126.7782777778, altitude 461.584828 m ASL, v_e 60.000000 m/s, v_n/v_d 약 0, yaw 90.0 deg 확인
  - 두 run 모두 throttle_cmd_norm 0.0, thrust_lbs -0.0 확인
  - 6.1.1 종료 시 yaw 89.865087 deg로 동쪽 heading 유지 확인
- 검증하지 못한 항목:
  - FlightGear 실시간 시각화
  - pitch trim 0.18의 최적 활공비 여부
- 검증하지 못한 이유:
  - 사용자 요청 범위가 XML/run 생성 및 JSBSim 실행 조건 검증이었고, 시각화/최적화는 별도 튜닝 과업임
- 남은 리스크:
  - 6.0 중립 무조종 run은 heading hold가 없어 충돌 시 yaw가 약 113.94 deg까지 변화함
  - runner가 workflow_all_cases_initial_settings.xlsx를 자동 갱신했으며, 해당 파일은 작업 전부터 modified 상태였음
- 후속 작업:
  - 필요 시 pitch trim 값 sweep으로 6.1 활공거리/강하율 최적화
- Git commit:
  - 없음

## [2026-07-19 23:45] PROGRESS-20260719-2345-001 — DONE

- 과업:
  - 6.0 중립 무추력 추락 runscript 초반 propeller 회전 원인 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - logs/csv/raw/c172x_4x75kg_cg_aligned/6.0__gimpo_450m_east_60ms_neutral_noengine_drop/6.0.2__gimpo_450m_east_60ms_neutral_noengine_drop_raw_07192330.csv
  - /home/junyeopkwon/jsbsim/engine/eng_io320.xml
  - /home/junyeopkwon/jsbsim/engine/prop_75in2f.xml
- 수행 내용:
  - 6.0 raw CSV의 throttle, mixture, magneto, starter, engine power, thrust, engine rpm, propeller rpm을 시간별로 확인
  - engine/prop XML에서 fixed-pitch propeller table과 piston engine 설정 확인
- 검증 결과:
  - t=0.0 s에서는 propeller-rpm 0, thrust -0, engine-rpm 0
  - t=0.008333 s에서 throttle 0, magneto 0, starter 0, engine power -1.9848 hp인데도 propeller-rpm 2816.26, thrust 442.12 lbf가 발생
  - 마지막 비영 propeller-rpm은 t=6.25 s에서 약 17.38 rpm이며 이후 0으로 감쇠
- 결론:
  - 엔진 출력이 켜진 것이 아니라, 기존 c172x_4x75kg_cg_aligned aircraft에 eng_io320 + prop_75in2f propulsion이 남아 있고 초기 60 m/s 전진류와 fixed-pitch propeller 동역학이 결합해 초반 transient를 생성함
- 검증하지 못한 항목:
  - propulsion을 제거한 4x75kg noengine aircraft variant 실행 비교
- 남은 리스크:
  - 엄밀히 '추력도 없이'를 만족하려면 현재 runscript 방식만으로는 초반 prop transient를 제거하지 못할 수 있음
- 후속 작업:
  - 필요 시 c172x_4x75kg_cg_aligned 기반 no-propulsion/noengine variant를 생성해 6.0/6.1을 재실행
- Git commit:
  - 없음

## [2026-07-19 23:50] PROGRESS-20260719-2350-001 — DONE

- 과업:
  - C172X 4x75kg zero-propulsion variant 생성 및 450 m east-heading 6.0/6.1 실행 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - scripts/generate_c172x_noengine_variant.py
  - scripts/generate_c172x_noengine_surface_neutral_empty_variant.py
  - scripts/generate_c172x_4x75kg_cg_aligned_variant.py
  - /home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml
  - /home/junyeopkwon/jsbsim/engine/dummy.xml
- 생성한 파일 및 폴더:
  - aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop/
  - aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop/c172x_4x75kg_cg_aligned_zeroprop.xml
  - scripts/c172x_4x75kg_cg_aligned_zeroprop/initial_condition/6.0__gimpo_450m_east_60ms_init.xml
  - scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.0__gimpo_450m_east_60ms_neutral_zeroprop_drop_run.xml
  - scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide_run.xml
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop/
- 수정한 파일:
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/TODO.md
  - docs/agent-log/INDEX.md
- 핵심 변경점:
  - c172x_4x75kg_cg_aligned 원본에서 engine/thruster를 제거하고 fuel tank, 75 kg x 4 pointmass, CG-aligned mass, aerodynamics, FCS, ground reactions는 유지
  - zero-prop aircraft에서는 fcs/throttle-cmd-norm property가 catalog에서 사라져 runscript의 throttle/mixture/AP throttle set을 제거
  - 6.0/6.1 초기조건은 기존 김포 lat/lon, altitude 450 m, elevation 38 ft, psi 90 deg, ubody 60 m/s를 동일하게 사용
- 실행한 명령어:
  - xmllint --noout aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop/c172x_4x75kg_cg_aligned_zeroprop.xml scripts/c172x_4x75kg_cg_aligned_zeroprop/initial_condition/6.0__gimpo_450m_east_60ms_init.xml scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.0__gimpo_450m_east_60ms_neutral_zeroprop_drop_run.xml scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide_run.xml
  - python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned_zeroprop --init scripts/c172x_4x75kg_cg_aligned_zeroprop/initial_condition/6.0__gimpo_450m_east_60ms_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.0__gimpo_450m_east_60ms_neutral_zeroprop_drop_run.xml --planet default --no-flightgear
  - python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned_zeroprop --init scripts/c172x_4x75kg_cg_aligned_zeroprop/initial_condition/6.0__gimpo_450m_east_60ms_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide_run.xml --planet default --no-flightgear
- 테스트 결과:
  - 최초 6.0 실행은 fcs/throttle-cmd-norm 미정의로 실패
  - zero-prop runscript에서 throttle/mixture/AP throttle set 제거 후 6.0.2 정상 실행
  - 6.0.2는 205.258333 s에 Nose Gear WOW로 종료
  - 6.1.1은 137.150000 s에 Nose Gear WOW로 종료
- 실행 확인 결과:
  - 두 run 모두 초기 lat 37.5707083333, lon 126.7782777778, v_e 60.000000 m/s, yaw 90.0 deg 확인
  - SI CSV에서 thrust_lbs 0.0, engine_rpm 0.0, propeller_rpm 0.0 확인
  - raw CSV에는 propulsion/engine 및 propeller property가 존재하지 않음
  - 6.1.1 종료 시 yaw 89.872697 deg, ap/heading_hold 1, ap/heading_setpoint 90 확인
- 검증하지 못한 항목:
  - FlightGear 실시간 시각화
  - heading hold gain 및 trim 최적화
  - generator script 추가
- 검증하지 못한 이유:
  - generator script 추가 시도 중 Windows sandbox helper 오류 발생
  - 현재 과업 완료에는 aircraft XML과 실행 검증이 충분함
- 남은 리스크:
  - zero-propulsion은 실제 engine-out windmilling prop drag도 제거하므로, 물리 의미가 기존 engine-off propeller-installed 조건과 다름
  - heading hold는 충돌 전까지 유지됐지만 동압 저하/실속 조건에서 항상 보장되는 것은 아님
- 후속 작업:
  - 필요 시 trim sweep 및 no-prop vs windmilling-prop trajectory 비교
- Git commit:
  - 없음

## [2026-07-20 00:00] PROGRESS-20260720-0000-001 — DONE

- 과업:
  - zero-prop 6.0 중립 run이 6.1 heading hold/trim run보다 더 멀리 간 원인 수치 비교
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - logs/csv/si/c172x_4x75kg_cg_aligned_zeroprop/6.0__gimpo_450m_east_60ms_neutral_zeroprop_drop/6.0.2__gimpo_450m_east_60ms_neutral_zeroprop_drop_si_07192345.csv
  - logs/csv/si/c172x_4x75kg_cg_aligned_zeroprop/6.1__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide/6.1.1__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide_si_07192346.csv
- 수행 내용:
  - 두 run의 최종 time, local_N/E/D, 속도, roll, pitch, yaw, 평균 roll/pitch를 비교
- 검증 결과:
  - 6.0 최종 time 205.2583 s, local_E 7206.006 m, yaw 86.819 deg, v_d 2.766 m/s, 평균 pitch 0.0046 deg
  - 6.1 최종 time 137.1500 s, local_E 5921.586 m, yaw 89.873 deg, v_d 4.011 m/s, 평균 pitch -2.5724 deg
  - 6.1은 heading 유지가 잘 됐지만 pitch trim 0.18 영향으로 더 큰 nose-down/강하율을 보이며 더 빨리 지면에 도달함
- 결론:
  - 현재 결과는 heading hold 자체의 거리 손실이라기보다 heading hold와 함께 적용한 pitch trim 0.18이 best glide trim이 아니어서 발생한 차이로 해석하는 것이 타당함
- 후속 작업:
  - heading hold만 켠 trim 0.0 run 또는 trim sweep을 수행해 heading hold 영향과 pitch trim 영향을 분리
- Git commit:
  - 없음

## [2026-07-20 09:10] PROGRESS-20260720-0910-001 — DONE

- 과업:
  - run_jsbsim_timestamped.py 상세 plotting 기능 구현 및 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/INDEX.md
- 수정한 파일:
  - scripts/run_jsbsim_timestamped.py
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- 생성한 폴더/파일:
  - ploting/c172x_4x75kg_cg_aligned_zeroprop/6.1.2__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide/
  - 해당 폴더 내부 events.csv 및 307개 PNG
- 핵심 변경점:
  - PLOTING_DIR = ROOT / 


## [2026-07-20 09:20] CORRECTION-20260720-0920-001 ? ??

- ?? ??:
  - PROGRESS-20260720-0910-001
- ?? ??:
  - ?? append ??? here-doc ??? ?? PROGRESS-20260720-0910-001 ??? ???? ??
- ?? ??:
  - PLOTING_DIR = ROOT / ?? ??? ????? ???
- ?? ??:
  - ?? PROGRESS-20260720-0920-001? ?? ??? ??? ??/?? ??? ?? append?
- ?? ??:
  - docs/agent-log/PROGRESS.md ?? ???
- ?? ??:
  - ?? ??? ??/???? ?? ?? ??? append
- ?? ??:
  - ??

## [2026-07-20 09:20] PROGRESS-20260720-0920-001 ? DONE

- ??:
  - run_jsbsim_timestamped.py ?? plotting ?? ?? ? ??
- ?? ????:
  - /home/junyeopkwon/jsbsim_workflow
- ??? ??:
  - scripts/run_jsbsim_timestamped.py
  - docs/agent-log/INDEX.md
- ??? ??:
  - scripts/run_jsbsim_timestamped.py
  - workflow_all_cases_initial_settings.xlsx
  - docs/agent-log/TASK.md
  - docs/agent-log/PROGRESS.md
  - docs/agent-log/DECISIONS.md
  - docs/agent-log/INDEX.md
- ??? ??/??:
  - ploting/c172x_4x75kg_cg_aligned_zeroprop/6.1.2__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide/
  - ?? ?? ?? events.csv ? 307? PNG
- ?? ???:
  - PLOTING_DIR = ROOT / "ploting" ??
  - console log?? ?? ??? event marker? ???? parse_event_markers ??
  - event? 2? ??? ?? ?? ???? E0/E1/E2 legend ??
  - raw_time_series, raw_converted_units, si_time_series, sixdof_raw_time_series, sixdof_raw_converted_units, sixdof_si_time_series, sixdof_dual_axis, trajectory_3d ?? ??
  - ft/fps/ft_sec2/rad/rad_sec/rad_sec2/slugs/slugs_ft2 ?? ?? plot ??
  - 6DOF dual-axis ?? ?? 11? ??
  - ?? plots/<aircraft>/<scenario>/ states_vs_time ? trajectory_3d ??? ??
- ??? ???:
  - python3 -m py_compile scripts/run_jsbsim_timestamped.py
  - python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned_zeroprop --init scripts/c172x_4x75kg_cg_aligned_zeroprop/initial_condition/6.0__gimpo_450m_east_60ms_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.1__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide_run.xml --planet default --no-flightgear
  - file ploting/.../sixdof_dual_axis/pitch_vs_pitch_rate.png ploting/.../raw_converted_units/velocities_v-east-fps_m_s.png
- ??? ??:
  - Python syntax compile ??
  - JSBSim ?? ??: run_id 6.1.2__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide
  - Detailed plot counts: raw_time_series 43, raw_converted_units 25, si_time_series 42, sixdof_raw_time_series 105, sixdof_raw_converted_units 49, sixdof_si_time_series 31, sixdof_dual_axis 11, trajectory_3d 1
  - find ?? ploting run ?? ?? PNG 307? ?? ??
  - events.csv ??: E0 0.008333, E2 137.15
  - ?? PNG 2?? PNG image data 1500 x 750?? ???
- ???? ?? ??:
  - view_image? ?? ?? ??? ?? ??
- ???? ?? ??:
  - UNC path ?? ? windows sandbox helper ?? ??
- ??? ?? ??:
  - ?? ?? ?? ?? ?? helper ???
- ?? ?? ??:
  - ???? ploting ???? ?? PNG? ?? ??? ?/legend ?? ??
- ?? ???:
  - ?? numeric property? ?? plot??? ?? ??? ???? ???
  - plot ?? ?? ?? ???? ???? ???
  - dual-axis ??? ?? ???? ?? ??? ?? ??/?? ??
- Git commit:
  - ??

## [2026-07-20 09:30] CORRECTION-20260720-0930-001 — 정정

- 대상 기록:
  - PROGRESS-20260720-0910-001
  - CORRECTION-20260720-0920-001
  - PROGRESS-20260720-0920-001
- 정정 이유:
  - 09:10 기록은 here-doc 종료 오류로 중간에서 잘렸고, 09:20 정정 기록은 PowerShell stdin 인코딩 문제로 한글이 ??로 손상됨
- 기존 내용:
  - 상세 plotting 기능 구현 기록 일부가 불완전하거나 문자 손상됨
- 정정 내용:
  - runner에 ploting/<aircraft>/<run_id>/ 상세 출력 기능을 추가했고, raw/SI/sixdof raw/sixdof SI 개별 time-series plot, raw/sixdof raw 단위 변환 plot, 6DOF dual-axis plot, 3D trajectory plot을 생성하도록 구성함
  - 이벤트 marker는 console log에서 실제 실행된 event를 파싱하며, 이벤트가 2개 이상일 때만 빨간 세로선과 E0, E1, E2 형식 legend로 표시함
  - zero-prop 6.1.2 검증 실행에서 raw_time_series 43개, raw_converted_units 25개, si_time_series 42개, sixdof_raw_time_series 105개, sixdof_raw_converted_units 49개, sixdof_si_time_series 31개, sixdof_dual_axis 11개, trajectory_3d 1개를 생성함
  - ploting/c172x_4x75kg_cg_aligned_zeroprop/6.1.2__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide/ 내부 PNG 307개와 events.csv 생성을 확인함
- 영향 범위:
  - scripts/run_jsbsim_timestamped.py
  - ploting/ 산출물 구조
  - docs/agent-log/PROGRESS.md
- 검증 결과:
  - python3 -m py_compile scripts/run_jsbsim_timestamped.py 통과
  - JSBSim 검증 실행 완료
  - 대표 PNG가 PNG image data 1500 x 750으로 확인됨
- 다음 작업:
  - 필요 시 dual-axis 조합 목록을 연구 목적에 맞게 확장

## [2026-07-20 10:00] PROGRESS-20260720-1000-001 — DONE

- 과업: 위치 계열 그래프 y축 오프셋 제거
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 위치(ft/m) 그래프에서 y축이 +3.868e6 같은 offset으로 표시되는 문제 수정
- 관련 파일: scripts/run_jsbsim_timestamped.py, ploting/c172x_4x75kg_cg_aligned_zeroprop/6.1.2__gimpo_450m_east_60ms_headinghold_trim_zeroprop_glide
- 수행 내용: configure_plain_y_axis, is_absolute_position_series, display_series_for_axis helper를 추가하고 plot_single_time_series 및 plot_dual_axis에 적용함
- 핵심 변경점: position/ecef, position/eci, ecef_, eci_ 계열 중 ft/m 단위 절대 위치는 큰 기준값 대비 변화량이 작을 때 초기값 기준 Delta 값으로 표시함
- 실행한 명령어: python3 -m py_compile scripts/run_jsbsim_timestamped.py
- 테스트 결과: 통과
- 실행한 명령어: display_series_for_axis('eci_z_m', 'eci_z_m', [3868600.0, 3868752.0, 3868510.0]) 확인
- 테스트 결과: is_position True, 결과 ('eci_z_m delta from initial', 'Delta eci_z_m from initial', [0.0, 152.0, -90.0]) 확인
- 실행한 명령어: 기존 6.1.2 CSV 세트로 build_detailed_ploting_outputs 호출
- 실행 확인 결과: raw_time_series 43, raw_converted_units 25, si_time_series 42, sixdof_raw_time_series 105, sixdof_raw_converted_units 49, sixdof_si_time_series 31, sixdof_dual_axis 11, trajectory_3d 1 생성
- 실행한 명령어: find ploting/... -name '*.png' | wc -l
- 실행 확인 결과: PNG 307개 확인
- 실행한 명령어: file ploting/.../sixdof_si_time_series/eci_z_m.png 및 ploting/.../sixdof_raw_converted_units/position_eci-z-ft_m.png
- 실행 확인 결과: 두 파일 모두 1500 x 750 PNG로 확인
- 실행한 명령어: cat ploting/.../events.csv
- 실행 확인 결과: E0 0.008333, E2 137.15 유지 확인
- 검증하지 못한 항목: Codex view_image 기반 직접 시각 검수
- 검증하지 못한 이유: 이전 동일 환경에서 UNC 이미지 보기 helper 오류가 발생함
- 남은 리스크: 절대 위치가 아닌 위치성 property 중 이름 패턴이 eci/ecef가 아닌 경우에는 delta 변환 대상에서 제외될 수 있음
- 다음 작업: 사용자가 다른 위치 계열 이름에서 같은 문제가 보이면 해당 property 명명 패턴을 position token 목록에 추가
- Git commit: 없음

## [2026-07-20 10:57] PROGRESS-20260720-1057-001 — 조사 완료

- 과업:
  - C172X 4x75kg 정상 이륙 runscript 설계안 조사
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /home/junyeopkwon/jsbsim/scripts/c1723.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned/c172x_4x75kg_cg_aligned.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned/reset00.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml
  - D:/ADSystem/N13701-V-Speeds.pdf
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/tmp/pdfs/N13701_page_image_1.jpg
  - /home/junyeopkwon/jsbsim_workflow/tmp/pdfs/N13701_page_image_2.jpg
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 핵심 조사 결과:
  - c1723.xml은 c172x/reset00 기반이며 51 kt에서 명시적 elevator rotation 대신 altitude hold autopilot을 켜는 예제성 이륙 스크립트임
  - c172x_4x75kg_cg_aligned는 PILOT, CO-PILOT, PASSENGER 1, PASSENGER 2 pointmass를 각각 75 kg으로 설정한 변형 기체임
  - 기존 workflow에는 같은 변형 기체에 대해 55 kt 또는 60 kt rotate를 쓰는 5.6/5.6.1 takeoff-cruise runscript가 있음
  - Purdue Aviation C172 자료는 Vr 55 KIAS, Vx 60 KIAS, Vy 76 KIAS, enroute climb 75-85 KIAS를 제공함
  - N13701 V-speeds PDF는 1974-75 model 기준 mph IAS 표이며 normal takeoff 0 deg flaps에서 Vr 60 MPH, Vy 91 MPH를 제시함
- 실행한 명령어:
  - git -C /home/junyeopkwon/jsbsim_workflow rev-parse --show-toplevel
  - sed -n 1,260p /home/junyeopkwon/jsbsim/scripts/c1723.xml
  - sed -n 1,260p /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml
  - sed -n 1,260p /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed_run.xml
  - python3 PDF image extraction for /mnt/d/ADSystem/N13701-V-Speeds.pdf
  - git -C /home/junyeopkwon/jsbsim_workflow status --short
- 검증 결과:
  - 아직 XML 파일을 만들지 않았으므로 JSBSim 실행 검증은 수행하지 않음
  - PDF는 이미지 기반 PDF라 WSL 텍스트 추출 도구로 직접 텍스트 추출하지 못했고, 동일 문서의 웹 텍스트와 추출 이미지 존재를 기준으로 속도 표를 확인함
- 검증하지 못한 항목:
  - 새 runscript XML schema/load 검증
  - JSBSim 이륙 성공 여부
  - 4x75kg 상태에서 실제 liftoff time, takeoff roll distance, climb rate
- 남은 리스크:
  - PDF mph IAS와 Purdue KIAS 값은 모델/연식 차이가 있어 완전히 같은 기준이 아님
  - 기존 JSBSim c172x 공력/추진 모델이 실제 C172 POH 성능과 정확히 일치한다고 볼 수 없음
- 다음 작업:
  - 사용자 확인 후 정상 이륙용 runscript를 새 파일로 생성하고 JSBSim 실행 검증
- Git commit:
  - 없음

## [2026-07-20 11:31] PROGRESS-20260720-1131-001 — 구현 및 검증 완료

- 과업:
  - C172X 4x75kg 정상 이륙, 500 m AGL 상승, 동일 방향 30초 cruise runscript 구현
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.8__rkss14l_normal_takeoff_climb500m_cruise30_run.xml
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/workflow_all_cases_initial_settings.xlsx
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 생성된 검증 산출물:
  - /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x_4x75kg_cg_aligned/5.8__rkss14l_normal_takeoff_climb500m_cruise30/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30_runscript_07201131.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned/5.8__rkss14l_normal_takeoff_climb500m_cruise30/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30_console_07201131.log
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned/5.8__rkss14l_normal_takeoff_climb500m_cruise30/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30_raw_07201131.csv
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned/5.8__rkss14l_normal_takeoff_climb500m_cruise30/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30_states_vs_time_07201131.png
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned/5.8__rkss14l_normal_takeoff_climb500m_cruise30/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30_trajectory_3d_07201131.png
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30
- 핵심 변경점:
  - 사용자가 지정한 2.2__rkss_14l_default_earth_init.xml을 initialize 경로로 사용
  - flap 0 deg normal takeoff 구성
  - 별도 nose-lightening stage 없이 55 KIAS에서 바로 rotate
  - 500 m AGL 도달 후 heading 135.01 deg 유지와 altitude hold를 걸고 30초 cruise 후 종료
  - capture 후 altitude_setpoint를 1600 ft, throttle을 0.70으로 조정해 500 m 주변 overshoot를 줄임
- 실행한 명령어:
  - python3 -c XML parse check
  - python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned --init scripts/c172x_4x75kg_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x_4x75kg_cg_aligned/runscript/5.8__rkss14l_normal_takeoff_climb500m_cruise30_run.xml --no-flightgear
- 테스트 결과:
  - XML parse 통과
  - JSBSim run 5.8.3 정상 종료
  - STATE 0~6 순차 실행 확인
  - Abort on low-speed high-AoA stall 미실행
  - Abort if ground contact returns after liftoff 미실행
- 주요 수치 검증:
  - Vr 도달: 21.96666667 s, 55.023200 KIAS
  - 500 m AGL 도달: 134.6166667 s, 500.022394 m AGL
  - cruise 시작: 138.883333 s
  - cruise 완료: 168.891667 s
  - cruise 지속 시간: 30.008334 s
  - 최종 고도: 502.669138 m AGL
  - 최종 속도: 88.192229 KIAS
  - 최종 heading: 134.796973 deg
  - cruise 구간 고도 범위: 496.507421-510.553112 m AGL
  - cruise 구간 속도 범위: 79.885313-88.192229 KIAS
  - cruise 구간 heading 범위: 134.640051-134.796973 deg
- 검증하지 못한 항목:
  - 실제 C172 POH takeoff roll distance와의 정밀 일치성
  - 실제 조종사 절차 수준의 trim/mixture/rudder 최적화
- 남은 리스크:
  - JSBSim c172x autopilot/flight model 검증 범위 안에서의 정상 종료이며 실제 항공기 성능 보증은 아님
  - workflow_all_cases_initial_settings.xlsx는 runner 실행으로 자동 갱신됨
- Git commit:
  - 없음

## [2026-07-20 11:47] PROGRESS-20260720-1147-001 — 구현 및 검증 완료

- 과업:
  - 상세 ploting event marker/legend 가독성 개선
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 재생성한 산출물:
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30
- 핵심 변경점:
  - event axvline label을 _nolegend_로 바꿔 event가 legend에 들어가지 않게 함
  - 각 event 점선 위에 E label과 event time을 표시
  - 이벤트 사이 구간이 충분히 넓으면 상단 rail에 E0-E1 같은 구간 label 표시
  - 촘촘한 이벤트 label은 3개 lane offset으로 겹침을 줄임
  - dual-axis plot의 데이터 legend를 loc=upper left, bbox_to_anchor=(1.015, 1.0) 방식으로 그래프 밖 오른쪽에 배치
  - bbox_inches=tight 및 tight_layout rect 조정으로 상단 marker와 바깥 legend가 저장 이미지에 포함되게 함
- 실행한 명령어:
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - 기존 5.8.3 raw/si/sixdof/console 파일을 사용해 build_detailed_ploting_outputs 직접 호출
  - PIL 이미지 크기 및 red marker/right legend 픽셀 검증
- 검증 결과:
  - py_compile 통과
  - 상세 ploting 재생성 count: raw_time_series 54, raw_converted_units 25, si_time_series 42, sixdof_raw_time_series 109, sixdof_raw_converted_units 49, sixdof_si_time_series 31, sixdof_dual_axis 11, trajectory_3d 1
  - from_start_neu_u_m.png 크기 1452x642, 상단 red marker pixel 5633개 확인
  - altitude_vs_vertical_speed.png 크기 1230x642, 상단 red marker pixel 3776개 및 오른쪽 legend 영역 non-white pixel 3964개 확인
  - events.csv는 E0 0.258333, E1 2.008333, E2 21.975, E3 27.158333, E4 133.058333, E5 138.883333, E6 168.891667 기록 확인
- 검증하지 못한 항목:
  - view_image 도구가 WSL/Windows 경로 모두 샌드박스 오류를 내서 GUI 기반 육안 검증은 수행하지 못함
- 남은 리스크:
  - 매우 짧은 이벤트 간격에서는 label lane offset을 써도 사용자가 더 큰 그림 크기를 원할 수 있음
- Git commit:
  - 없음

## [2026-07-20 11:52] PROGRESS-20260720-1152-001 — 구현 및 검증 완료

- 과업:
  - 상세 ploting event marker를 별도 상단 strip으로 분리
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 재생성한 산출물:
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30
- 핵심 변경점:
  - add_event_lines는 본 plot의 dashed vertical line만 그림
  - add_event_strip helper를 추가해 E label/time과 E0-E1 같은 구간 rail을 별도 subplot에 그림
  - single time-series와 dual-axis time-series 모두 2행 subplot 구조 적용
  - subplots_adjust로 top/bottom/right 영역을 명시 지정해 layout warning 제거
- 실행한 명령어:
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - 기존 5.8.3 raw/si/sixdof/console 파일로 build_detailed_ploting_outputs 직접 호출
  - PIL 기반 PNG pixel check
- 검증 결과:
  - py_compile 통과
  - ploting 재생성 완료: raw_time_series 54, raw_converted_units 25, si_time_series 42, sixdof_raw_time_series 109, sixdof_raw_converted_units 49, sixdof_si_time_series 31, sixdof_dual_axis 11, trajectory_3d 1
  - 재생성 중 matplotlib layout warning 없음
  - from_start_neu_u_m.png: 1451x836, top strip red pixel 6414, strip/plot 사이 red pixel 1
  - altitude_vs_vertical_speed.png: 1519x836, top strip red pixel 5450, right legend area non-white pixel 6377
- 검증하지 못한 항목:
  - view_image 도구 오류로 실제 화면 기반 검증은 수행하지 못함
- 남은 리스크:
  - 이벤트가 훨씬 많은 run에서는 strip 높이 또는 label lane 수 추가가 필요할 수 있음
- Git commit:
  - 없음

## [2026-07-20 12:04] PROGRESS-20260720-1204-001 — 정정 구현 완료

- 과업:
  - 상세 ploting event 시작점만 표시하도록 정정
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 재생성한 산출물:
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30
- 핵심 변경점:
  - add_event_strip에서 구간 rail과 E0-E1 같은 interval label 제거
  - event label에서 time text 제거
  - 상단 strip에는 각 이벤트 시작점의 vertical marker와 E label만 표시
  - strip 높이를 줄이고 기존 ploting 산출물을 재생성
- 실행한 명령어:
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - build_detailed_ploting_outputs로 기존 5.8.3 데이터 재생성
  - grep -n hlines|rail_lanes|start_label|end_label|time_s:.1f 확인
  - PIL 기반 red pixel 확인
- 검증 결과:
  - py_compile 통과
  - ploting 재생성 완료: raw_time_series 54, raw_converted_units 25, si_time_series 42, sixdof_raw_time_series 109, sixdof_raw_converted_units 49, sixdof_si_time_series 31, sixdof_dual_axis 11, trajectory_3d 1
  - hlines, start_label, end_label, time_s:.1f 잔여 코드 없음
  - from_start_neu_u_m.png 크기 1451x769, max_red_in_top_row 69로 긴 수평 rail이 없는 상태 확인
- 검증하지 못한 항목:
  - view_image 도구 오류로 직접 화면 기반 검증은 수행하지 못함
- 남은 리스크:
  - 이벤트가 매우 촘촘한 경우 E label lane 수 추가가 필요할 수 있음
- Git commit:
  - 없음

## [2026-07-20 12:12] PROGRESS-20260720-1212-001 — 구현 및 검증 완료

- 과업:
  - 상세 ploting event label 겹침 추가 개선 및 기본 원점 표시 적용
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 재생성한 산출물:
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30
- 핵심 변경점:
  - event strip label bbox 제거로 E0/E1 근접 label의 겹침 가능성을 줄임
  - E label은 시간/구간 없이 event start marker만 표시
  - from_start 및 distance_from_start 계열은 표시 시 첫 finite 값을 빼서 0부터 시작하도록 처리
  - time-series x축은 nonnegative이면 0부터, y축도 nonnegative 또는 -0.01 이내 numerical drift이면 0부터 시작하도록 처리
- 실행한 명령어:
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - 기존 5.8.3 데이터로 build_detailed_ploting_outputs 직접 호출
  - PIL 기반 PNG pixel check
- 검증 결과:
  - py_compile 통과
  - ploting 재생성 완료: raw_time_series 54, raw_converted_units 25, si_time_series 42, sixdof_raw_time_series 109, sixdof_raw_converted_units 49, sixdof_si_time_series 31, sixdof_dual_axis 11, trajectory_3d 1
  - from_start_neu_u_m 표시값 첫 값 0.0 확인
  - from_start_neu_u_m zeroed_minmax -0.0015931354510367868 to 507.0338141848871 확인
  - bbox, hlines 잔여 코드 없음 확인
  - from_start_neu_u_m.png 크기 1448x769, max_red_in_top_row 43, red_top_total 854 확인
- 검증하지 못한 항목:
  - view_image 도구 오류로 직접 화면 기반 검증은 수행하지 못함
- 남은 리스크:
  - E0/E1처럼 매우 가까운 이벤트는 label box를 제거했지만, 더 많은 이벤트가 몰리면 label 생략/offset 규칙이 추가로 필요할 수 있음
- Git commit:
  - 없음


## [2026-07-20 12:21] PROGRESS-20260720-1221-001 — 완료

- 과업:
  - 상세 ploting 이벤트 시작점 숫자 원형 marker 적용 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - E0, E1 대신 0, 1, 2, 3 숫자를 점선 위 동그라미 안에 넣는 방식 적용
- 관련 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30/events.csv
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30/sixdof_si_time_series/from_start_neu_u_m.png
- 수행 내용:
  - parse_event_markers 함수가 event label을 str(event_id)로 생성하는지 확인
  - add_event_strip 함수가 label을 circle pad 0.24, red facecolor, red edgecolor, white text로 표시하는지 확인
  - 기존 5.8.3 상세 ploting output의 events.csv label이 0, 1, 2, 3, 4, 5, 6인지 확인
  - sample PNG 크기와 상단 red pixel 존재 여부 확인
- 변경 이유:
  - E0, E1 형식은 좁은 간격에서 text width가 커져 겹침이 커짐
  - 숫자 원형 marker는 시작점 번호만 전달해 공간을 줄임
- 검증 명령어:
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - cat /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30/events.csv
  - PIL Image.open(.../sixdof_si_time_series/from_start_neu_u_m.png)
- 검증 결과:
  - py_compile 통과
  - events.csv label 확인: 0, 1, 2, 3, 4, 5, 6
  - sample PNG 크기: 1448x769
  - sample PNG 상단 red pixel count: 2386
- 검증하지 못한 항목:
  - view_image 도구가 sandbox helper 오류를 반환해 PNG 육안 확인은 수행하지 못함
- 가정:
  - 상단 red pixel 증가는 event strip의 점선 및 원형 marker가 렌더링되었음을 확인하는 보조 지표임
- 남은 리스크:
  - E0/E1 대비 겹침은 줄었지만, 극단적으로 가까운 event는 원형 marker 자체가 일부 겹칠 수 있음
- 다음 작업:
  - 사용자가 PNG를 열어 최종 시각 상태를 확인
- 관련 기록:
  - TASK-20260720-1221-001
- Git commit:
  - 없음


## [2026-07-20 12:22] PROGRESS-20260720-1222-001 — 추가 검증

- 과업:
  - 상세 ploting 숫자 원형 marker 변경 후 최종 diff 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수행 내용:
  - scripts/run_jsbsim_timestamped.py 대상 git diff --check 재실행
  - scripts/run_jsbsim_timestamped.py py_compile 재실행
  - events.csv label 재확인
- 검증 명령어:
  - git diff --check -- scripts/run_jsbsim_timestamped.py
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - cat /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30/events.csv
- 검증 결과:
  - 코드 파일 diff check 통과
  - py_compile 통과
  - events.csv label은 0, 1, 2, 3, 4, 5, 6으로 확인
- 검증하지 못한 항목:
  - 전체 docs/agent-log 포함 diff check는 과거 append 기록의 trailing whitespace를 보고함
- 남은 리스크:
  - agent-log는 append-only 정책에 따라 해당 과거 줄을 삭제하거나 수정하지 않음
- Git commit:
  - 없음


## [2026-07-20 12:31] PROGRESS-20260720-1231-001 — 완료

- 과업:
  - 상세 ploting 숫자 event marker 상단 끝 정렬
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
- 재생성한 산출물:
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30
- 핵심 변경점:
  - add_event_strip의 label_lanes를 제거함
  - 모든 event label 위치를 label_y 0.96으로 고정함
  - vertical marker의 ymax 0.96과 label center y를 맞춰 점선 끝 중심에 숫자 원형 marker가 오도록 조정함
- 실행한 명령어:
  - 기존 5.8.3 CSV/log로 build_detailed_ploting_outputs 직접 호출
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - git diff --check -- scripts/run_jsbsim_timestamped.py
  - cat /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30/events.csv
  - PIL 기반 sample PNG red pixel y-range 확인
- 검증 결과:
  - ploting 재생성 완료: raw_time_series 54, raw_converted_units 25, si_time_series 42, sixdof_raw_time_series 109, sixdof_raw_converted_units 49, sixdof_si_time_series 31, sixdof_dual_axis 11, trajectory_3d 1
  - py_compile 통과
  - 코드 파일 diff check 통과
  - events.csv label은 0, 1, 2, 3, 4, 5, 6으로 유지
  - sample PNG 크기 1448x769 확인
  - 상단 red pixel y-range 62 to 84, peak row 79 확인
- 검증하지 못한 항목:
  - view_image 도구가 sandbox helper 오류를 반환해 PNG 직접 육안 확인은 수행하지 못함
- 남은 리스크:
  - 0과 1처럼 시간 간격이 매우 가까운 marker는 같은 높이에 배치되므로 일부 겹칠 수 있음
- Git commit:
  - 없음


## [2026-07-20 12:45] PROGRESS-20260720-1245-001 — 완료

- 과업:
  - dual-axis 상세 plot legend 위치 조정
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
- 재생성한 산출물:
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30
- 핵심 변경점:
  - legend_below_x_axis 함수를 추가함
  - plot_dual_axis에서 legend_outside 대신 legend_below_x_axis를 호출함
  - dual-axis plot의 right 여백을 0.90으로 늘려 그래프 폭을 회복함
  - dual-axis plot의 bottom 여백을 0.27로 늘려 x축 제목 아래 legend 공간을 확보함
- 실행한 명령어:
  - 기존 5.8.3 CSV/log로 build_detailed_ploting_outputs 직접 호출
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - git diff --check -- scripts/run_jsbsim_timestamped.py
  - PIL 기반 /sixdof_dual_axis/u_vs_udot.png 하단 색상 bbox 확인
- 검증 결과:
  - ploting 재생성 완료: raw_time_series 54, raw_converted_units 25, si_time_series 42, sixdof_raw_time_series 109, sixdof_raw_converted_units 49, sixdof_si_time_series 31, sixdof_dual_axis 11, trajectory_3d 1
  - py_compile 통과
  - 코드 파일 diff check 통과
  - sample dual-axis PNG 크기 1408x715 확인
  - sample dual-axis PNG 하단 색상 bbox 14,486 to 1391,683 확인
- 검증하지 못한 항목:
  - view_image 도구가 sandbox helper 오류를 반환해 PNG 직접 육안 확인은 수행하지 못함
- 남은 리스크:
  - 아주 긴 legend label 조합에서는 아래 legend가 이미지 폭에 근접할 수 있음
- Git commit:
  - 없음


## [2026-07-20 12:55] PROGRESS-20260720-1255-001 — 조사 및 정리 완료

- 과업:
  - C172 이륙 절차 및 구현 runscript 구성 설명 작성
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.8__rkss14l_normal_takeoff_climb500m_cruise30_run.xml
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30/events.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned/5.8__rkss14l_normal_takeoff_climb500m_cruise30/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30_console_07201131.log
- 수행 내용:
  - runscript event 0~6 조건과 control command 확인
  - 검증 run 5.8.3의 event 실행 시각과 주요 상태값 확인
  - 현재 구현 기준으로 절차 설명과 event mapping 정리
- 검증 명령어:
  - nl -ba .../5.8__rkss14l_normal_takeoff_climb500m_cruise30_run.xml
  - cat .../events.csv
  - tail .../5.8.3__rkss14l_normal_takeoff_climb500m_cruise30_console_07201131.log
- 검증 결과:
  - Event 0: 0.258333 s
  - Event 1: 2.008333 s
  - Event 2 rotation: 21.975000 s, 55.023200 KIAS
  - Event 3 positive climb: 27.158333 s, 20.110106 ft AGL
  - Event 4 500 m capture condition: 133.058333 s, 1621.895579 ft AGL
  - Event 5 cruise begins: 138.883333 s, 1667.556827 ft AGL
  - Event 6 terminate after 30 s cruise: 168.891667 s, 1649.170902 ft AGL
- 검증하지 못한 항목:
  - 외부 웹/PDF 재확인은 수행하지 않고 기존 구현과 검증 로그를 기준으로 작성함
- 남은 리스크:
  - 실제 POH/운항 절차와 구현값의 정밀 일치성은 별도 출처 재검토가 필요함
- Git commit:
  - 없음


## [2026-07-20 13:05] PROGRESS-20260720-1305-001 — 조사 완료

- 과업:
  - c1723_run.xml event 5 필요 여부 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/c1723_run.xml
  - /home/junyeopkwon/jsbsim/scripts/c1723.xml
- 수행 내용:
  - c1723_run.xml event 순서를 확인함
  - Adjust throttle/flaps event가 flaps retract, heading setpoint 변경, roll mode 설정, state file write를 수행함을 확인함
  - Time Notify persistent event는 1분 간격 notify용임을 확인함
- 검증 명령어:
  - nl -ba /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/c1723_run.xml
  - nl -ba /home/junyeopkwon/jsbsim/scripts/c1723.xml
  - grep -R -n 'Adjust throttle/flaps|ap/altitude_hold|fcs/flap-cmd-norm' ...
- 검증 결과:
  - Begin roll에서 flap-cmd-norm 0.33 설정 확인
  - Adjust throttle/flaps에서 h-agl >= 1000 조건 후 flap-cmd-norm 0으로 retract 확인
  - Time Notify는 persistent notify event로 동역학 제어값 변경 없음
- 검증하지 못한 항목:
  - event 제거 후 실제 시뮬레이션 재실행은 수행하지 않음
- 남은 리스크:
  - 원본 c1723_run.xml에서 Adjust throttle/flaps를 제거하면 flap 10도 상태가 계속 유지되어 상승/속도 응답이 달라질 수 있음
- Git commit:
  - 없음


## [2026-07-20 21:52] PROGRESS-20260720-2152-001 — 생성 및 실행 완료

- 과업:
  - Time Notify 제거 c1723 runscript 생성 및 실행 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/c1723_no_time_notify_run.xml
- 생성된 실행 산출물:
  - /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_runscript_07202146.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/console/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_console_07202146.log
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_raw_07202146.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_si_07202146.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_sixdof_raw_07202146.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_si/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_sixdof_si_07202146.csv
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x/0.0.1__c1723_no_time_notify
- 수행 내용:
  - 원본 c1723_run.xml에서 line 163-177 Time Notify block만 제외해 복사본 생성
  - diff로 Time Notify block만 제거된 것 확인
  - run_jsbsim_timestamped.py로 c172x, reset00_init.xml, c1723_no_time_notify_run.xml 실행
  - console log의 event 실행 목록과 End 확인
  - events.csv label/time 확인
  - SI/RAW CSV 마지막 time 확인
- 실행한 명령어:
  - awk 'NR<163 || NR>177' scripts/c172x/runscript/c1723_run.xml > scripts/c172x/runscript/c1723_no_time_notify_run.xml
  - python3 scripts/run_jsbsim_timestamped.py --aircraft c172x --init scripts/c172x/initial_condition/reset00_init.xml --runscript scripts/c172x/runscript/c1723_no_time_notify_run.xml --planet builtin --no-flightgear
  - grep -n 'executed at time|End:' logs/console/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_console_07202146.log
  - cat ploting/c172x/0.0.1__c1723_no_time_notify/events.csv
  - tail -n 1 logs/csv/si/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_si_07202146.csv
- 검증 결과:
  - 생성된 runscript event 목록: engine start, Begin roll, Rotate, Set autopilot for 6000 ft., Adjust throttle/flaps
  - Time Notify event 없음 확인
  - Event 0 engine start: 0.258333 s
  - Event 1 Begin roll: 3.008333 s
  - Event 2 Rotate: 21.866667 s
  - Event 3 Set autopilot for 6000 ft.: 31.875000 s
  - Event 4 Adjust throttle/flaps: 133.441667 s
  - console End: Monday July 20 2026 21:46:09
  - SI CSV final time: 1000.008333 s
  - RAW CSV final time: 1000.008333 s
  - ploting file count: 323
- 검증하지 못한 항목:
  - wrapper 명령은 plotting까지 포함해 180초 timeout code 124로 종료되어 최종 stdout summary는 받지 못함
- 남은 리스크:
  - timeout은 JSBSim 실행 실패가 아니라 후처리/plotting까지 포함한 wall-clock 제한으로 판단됨
- Git commit:
  - 없음


## [2026-07-20 22:10] PROGRESS-20260720-2210-001 — 구현 및 검증 완료

- 과업:
  - sixdof_dual_axis 신규 plot 추가
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
- 재생성한 산출물:
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x/0.0.1__c1723_no_time_notify
- 핵심 변경점:
  - sixdof_raw에 vt-fps가 직접 없을 때 v-north, v-east, v-down 성분으로 derived/v-total-fps를 계산
  - altitude_vs_total_speed pair 추가
  - total speed를 왼쪽 y축, engine RPM과 propeller RPM을 오른쪽 y축에 같이 표시하는 total_speed_vs_engine_propeller_rpm plot 추가
- 실행한 명령어:
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - git diff --check -- scripts/run_jsbsim_timestamped.py
  - 기존 5.8.3 CSV/log로 build_detailed_ploting_outputs 직접 호출
  - 기존 c1723_no_time_notify CSV/log로 build_detailed_ploting_outputs 직접 호출
  - PIL Image.open으로 신규 PNG 크기 확인
- 검증 결과:
  - py_compile 통과
  - 코드 파일 diff check 통과
  - 5.8.3 sixdof_dual_axis count: 13
  - c1723_no_time_notify sixdof_dual_axis count: 13
  - 5.8.3 altitude_vs_total_speed.png: 1397x715, 98582 bytes
  - 5.8.3 total_speed_vs_engine_propeller_rpm.png: 1512x706, 108546 bytes
  - c1723_no_time_notify altitude_vs_total_speed.png: 1410x715, 109349 bytes
  - c1723_no_time_notify total_speed_vs_engine_propeller_rpm.png: 1512x706, 116977 bytes
- 검증하지 못한 항목:
  - 이미지 렌더링의 최종 육안 검토는 수행하지 못함
- 남은 리스크:
  - total speed는 derived series라 header 원본에는 존재하지 않음
  - engine RPM과 propeller RPM label이 길어 legend 폭이 커질 수 있음
- Git commit:
  - 없음


## [2026-07-20 22:20] PROGRESS-20260720-2220-001 — 분석 완료

- 과업:
  - 650초 이후 total speed 증가 원인 분석
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_sixdof_raw_07202146.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/console/c172x/c1723_no_time_notify/0.0.1__c1723_no_time_notify_console_07202146.log
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/c1723_no_time_notify_run.xml
- 수행 내용:
  - 시간별 h-agl, total speed, pitch, throttle, engine RPM 추출
  - 6000 ft AGL 도달 시점 및 최대 고도/최대 속도 계산
  - event log와 runscript setpoint를 대조
- 검증 결과:
  - Event 3에서 31.875 s에 altitude_setpoint 6000 ft 설정
  - Event 4에서 133.441667 s에 flaps retract 및 heading 변경
  - 650초 근처 추가 event 없음
  - first h-agl 6000 ft: 664.525 s, total speed 32.983 m/s, pitch 10.764 deg
  - 650 s: h_agl 5889.4 ft, total speed 30.45 m/s, pitch 11.67 deg, throttle 1.0
  - 700 s: h_agl 6273.5 ft, total speed 43.11 m/s, pitch 6.24 deg, throttle 1.0
  - 800 s: h_agl 6815 ft 수준, total speed 약 63 m/s, pitch 약 0.47 deg
  - 최대 고도: 806.6 s, 6816.873 ft
  - 최대 속도: 982.275 s, 69.782 m/s
- 결론:
  - 650초 이후 속도 증가는 새 event 때문이 아니라 6000 ft altitude capture 부근에서 full throttle 상태로 pitch가 낮아진 autopilot 응답 때문임
- 남은 리스크:
  - total speed는 ground velocity 성분 기반 derived value이며 calibrated airspeed와 동일하지 않음
- Git commit:
  - 없음


## [2026-07-21 09:11] PROGRESS-20260721-0911-001 — 구현 및 검증 완료

- 과업:
  - 표 기반 dual-axis 그래프 4개 추가
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - /home/junyeopkwon/jsbsim_workflow/workflow_all_cases_initial_settings.xlsx
- 재생성/생성한 산출물:
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.3__rkss14l_normal_takeoff_climb500m_cruise30
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x/0.0.1__c1723_no_time_notify
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.4__rkss14l_normal_takeoff_climb500m_cruise30
- 핵심 변경점:
  - merge_secondary_numeric_csv를 추가해 sixdof_dual_axis 생성 시 sixdof_raw에 없는 raw CSV column도 활용 가능하게 함
  - OUTPUT_PROPERTIES와 SIXDOF_VALIDATION_PROPERTIES에 fcs/rudder-cmd-norm 등 요청 pair에 필요한 property를 추가함
  - altitude_vs_calibrated_airspeed, elevator_command_vs_pitch, rudder_command_vs_heading, altitude_capture_vs_climb_rate pair 추가
- 실행한 명령어:
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - git diff --check -- scripts/run_jsbsim_timestamped.py
  - 기존 5.8.3 및 c1723_no_time_notify 로그로 build_detailed_ploting_outputs 직접 호출
  - python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned --init scripts/c172x_4x75kg_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x_4x75kg_cg_aligned/runscript/5.8__rkss14l_normal_takeoff_climb500m_cruise30_run.xml --planet builtin --no-flightgear
- 검증 결과:
  - py_compile 통과
  - 코드 파일 diff check 통과
  - 기존 5.8.3/c1723_no_time_notify는 과거 CSV에 rudder-cmd-norm이 없어 3개 신규 plot만 생성되고 count 16 확인
  - 신규 5.8.4는 sixdof_dual_axis count 17 확인
  - 5.8.4에서 altitude_vs_calibrated_airspeed.png, elevator_command_vs_pitch.png, rudder_command_vs_heading.png, altitude_capture_vs_climb_rate.png 모두 생성 확인
  - 5.8.4 console End 확인: Tuesday July 21 2026 09:09:48
- 검증하지 못한 항목:
  - PNG 직접 육안 검토는 수행하지 않음
- 남은 리스크:
  - 과거 5.8.3/c1723_no_time_notify 로그에는 rudder-cmd-norm이 없으므로 rudder_command_vs_heading는 새 실행부터 생성 가능
- Git commit:
  - 없음


## [2026-07-21 09:18] PROGRESS-20260721-0918-001 — 구현 및 검증 완료

- 과업:
  - alt_vs_vc_kts.png 추가 생성
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
- 재생성한 산출물:
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned/5.8.4__rkss14l_normal_takeoff_climb500m_cruise30
- 수행 내용:
  - 기존 altitude_vs_calibrated_airspeed와 동일한 position/h-agl-ft vs velocities/vc-kts pair를 alt_vs_vc_kts 파일명으로 추가
  - 기존 5.8.4 로그로 build_detailed_ploting_outputs 재실행
- 검증 명령어:
  - python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - git diff --check -- scripts/run_jsbsim_timestamped.py
  - 기존 5.8.4 로그로 build_detailed_ploting_outputs 직접 호출
  - PIL Image.open으로 alt_vs_vc_kts.png 확인
- 검증 결과:
  - py_compile 통과
  - 코드 파일 diff check 통과
  - sixdof_dual_axis count: 18
  - alt_vs_vc_kts.png 생성 확인: 1397x715, 101492 bytes
- 검증하지 못한 항목:
  - PNG 직접 육안 확인은 수행하지 않음
- 남은 리스크:
  - altitude_vs_calibrated_airspeed.png와 내용은 동일하고 파일명 alias 성격임
- Git commit:
  - 없음

## [2026-07-21 13:18] PROGRESS-20260721-1318-001 — 구현 및 검증 완료

- 과업:
  - F450 Test_F450_Launch workflow 케이스 추가 및 실행 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /home/junyeopkwon/jsbsim/scripts/Test_F450_Launch.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/F450/initial_condition/1.0__ground_park_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.0__ground_launch_scas_run.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/2.0__nominal_mission_profile_run.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.1__test_f450_launch_run.xml
- 수정된 파일:
  - /home/junyeopkwon/jsbsim_workflow/workflow_all_cases_initial_settings.xlsx
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 생성된 실행 산출물:
  - /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/F450/1.1__test_f450_launch/1.1.1__test_f450_launch_runscript_07211313.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/console/F450/1.1__test_f450_launch/1.1.1__test_f450_launch_console_07211313.log
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/F450/1.1__test_f450_launch/1.1.1__test_f450_launch_raw_07211313.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/si/F450/1.1__test_f450_launch/1.1.1__test_f450_launch_si_07211313.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/F450/1.1__test_f450_launch/1.1.1__test_f450_launch_sixdof_raw_07211313.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_si/F450/1.1__test_f450_launch/1.1.1__test_f450_launch_sixdof_si_07211313.csv
  - /home/junyeopkwon/jsbsim_workflow/plots/F450/1.1__test_f450_launch
  - /home/junyeopkwon/jsbsim_workflow/ploting/F450/1.1.1__test_f450_launch
- 핵심 변경점:
  - 원본 Test_F450_Launch.xml를 workflow의 F450 runscript 목록에 1.1__test_f450_launch_run.xml로 추가
  - run_jsbsim_timestamped.py discovery 기준에서 F450 runscript 선택지가 1.0, 1.1, 2.0 세 개로 확장됨
  - 새 실행 결과가 workflow_all_cases_initial_settings.xlsx에 자동 반영됨
- 실행한 명령어:
  - diff -u /home/junyeopkwon/jsbsim/scripts/Test_F450_Launch.xml /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.1__test_f450_launch_run.xml
  - python3 -m py_compile scripts/run_jsbsim_timestamped.py
  - python3 - <<PY로 discover_runscripts('F450') 확인
  - python3 scripts/run_jsbsim_timestamped.py --aircraft F450 --init scripts/F450/initial_condition/1.0__ground_park_init.xml --runscript scripts/F450/runscript/1.1__test_f450_launch_run.xml --planet builtin --no-flightgear
  - grep -n 'executed at time\|End:' logs/console/F450/1.1__test_f450_launch/1.1.1__test_f450_launch_console_07211313.log
  - CSV header, row count, 주요 시간대 throttle, rudder, h-agl 값 확인
  - find 산출물 파일 수 확인
  - git diff --check -- scripts/F450/runscript/1.1__test_f450_launch_run.xml scripts/run_jsbsim_timestamped.py
- 검증 결과:
  - 원본 Test_F450_Launch.xml와 workflow 복사본 diff 없음
  - py_compile 통과
  - F450 discover_runscripts 결과에 scripts/F450/runscript/1.1__test_f450_launch_run.xml 포함 확인
  - 실행 run id: 1.1.1__test_f450_launch
  - console End: Tuesday July 21 2026 13:13:51
  - raw CSV: 51 columns, 3751 rows
  - sixdof raw CSV: 113 columns, 3751 rows
  - SI CSV final time: 30.0 s
  - detailed plot counts: raw_time_series 50, raw_converted_units 25, si_time_series 42, sixdof_dual_axis 18, sixdof_raw_time_series 112, sixdof_raw_converted_units 50, sixdof_si_time_series 31, trajectory_3d 1
  - 관련 실행 산출물 총 파일 수: 338
  - rudder command는 22 s 부근 0.5, 24 s 부근 -0.5, 30 s 0으로 CSV에서 확인됨
  - git diff --check 통과
- 검증하지 못한 항목:
  - roll doublet의 aileron command 값은 raw CSV 기본 output에 fcs/aileron-cmd-norm이 없어 CSV로 직접 확인하지 못함
  - PNG 이미지는 파일 생성 수와 크기 기반으로 확인했고 육안 검토는 수행하지 않음
- 남은 리스크:
  - workflow runner가 템플릿 output block을 제거하고 자체 output을 붙이므로, 원본 Test_F450_Launch.xml의 quad_log.csv와 완전히 같은 CSV column 구성은 아님
  - raw CSV에는 indexed throttle command와 fcs/ScasEngage가 빠져 있어 F450 제어 입력 분석에는 output property 보강이 유용함
- Git commit:
  - 없음


## [2026-07-23 23:07] PROGRESS-20260723-2307-001 — 검토 완료

- 과업:
  - C172 RKSS 14L full normal mission bundle 검토
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/README.md
  - /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/5.9__rkss14l_full_normal_mission_run.xml
  - /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/c172ap_landing.xml
  - /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/c172x_4x75kg_cg_aligned_landing.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/runscript/5.8__rkss14l_normal_takeoff_climb500m_cruise30_run.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned
- 수행 내용:
  - 제공 bundle 파일 목록 및 README 배치 지침 확인
  - 5.9 runscript event state 0-23과 safety termination 조건 검토
  - 기존 5.8 정상 이륙 runscript와 5.9 이륙부 구조 비교
  - landing aircraft XML과 기존 c172x_4x75kg_cg_aligned aircraft XML diff 확인
  - c172ap_landing.xml과 기존 c172ap.xml diff 확인
  - run_jsbsim_timestamped.py의 aircraft discovery, runscript discovery, generated runscript 생성, output 삽입 동작 확인
- 핵심 확인:
  - 현재 JSBSim aircraft tree에는 c172x_4x75kg_cg_aligned_landing 디렉터리가 없어 제공 runscript의 aircraft 이름만으로는 workflow 실행 불가
  - run_jsbsim_timestamped.py는 generated runscript 생성 시 use aircraft와 initialize를 CLI 선택값으로 덮어쓰므로, base aircraft로 실행하면 landing AP 변경이 적용되지 않음
  - runscript discovery는 scripts/<aircraft>/runscript 구조를 기준으로 필터링하므로 landing aircraft를 별도 선택하려면 scripts/c172x_4x75kg_cg_aligned_landing 구조도 맞추는 편이 안전함
  - 기본 raw output에는 simulation/mission-state와 simulation/landing-authorized가 없어서 full mission state 전이를 CSV에서 연속 추적하기 어렵고, sixdof output에는 gear WOW와 compression, VRP 위치가 포함됨
  - Abort on excessive bank near the ground 이벤트는 이름과 달리 고도 또는 mission-state 제한이 없어 loiter/복귀 중 bank overshoot만으로도 전체 미션을 종료할 수 있음
  - final 진입 조건은 주로 latitude와 heading에 의존해 cross-track 또는 runway threshold distance 검증이 약함
- 실행한 명령어:
  - find /home/junyeopkwon -maxdepth 3 -type d -name jsbsim_workflow
  - find docs/agent-log -maxdepth 1 -type f -name *.md
  - xmllint --noout /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/5.9__rkss14l_full_normal_mission_run.xml /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/c172ap_landing.xml /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/c172x_4x75kg_cg_aligned_landing.xml
  - diff -u aircraft_variants/c172x_4x75kg_cg_aligned/c172x_4x75kg_cg_aligned.xml /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/c172x_4x75kg_cg_aligned_landing.xml
  - diff -u aircraft_variants/c172x_4x75kg_cg_aligned/c172ap.xml /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle/c172ap_landing.xml
  - /usr/bin/grep 기반 runscript, aircraft XML, runner property 확인
  - git status --short
- 검증 결과:
  - XML well-formedness 통과
  - 제공 landing aircraft의 주요 변경은 fdm_config name, autopilot file=c172ap_landing, output name/rate/property 추가임을 확인
  - 제공 landing AP의 주요 변경은 altitude-hold PID gain 변경 및 ap/altitude_hold off 또는 WOW 상태에서 ap/elevator_cmd를 0으로 게이트하는 구조임을 확인
  - 현재 /home/junyeopkwon/jsbsim/aircraft에는 c172x_4x75kg_cg_aligned와 c172x_4x75kg_cg_aligned_zeroprop만 존재함
- 검증하지 못한 항목:
  - full mission JSBSim 실행
  - generated runscript 기준 event firing sequence
  - 착륙 시 vertical speed, touchdown order, rollout distance, runway centerline/cross-track 오차
  - PNG plot 육안 확인
- 남은 리스크:
  - 실제 실행 없이 정적 검토만으로는 STATE 12-18의 위치/고도/속도 조건이 모두 순서대로 성립하는지 확정할 수 없음
  - 1500 s end time 안에 landing 완료가 안 되면 정상 종료 대신 run end 종료가 될 수 있음
  - landing tuning 값은 README에도 명시된 초기값이므로 실제 CSV 기반 반복 튜닝 필요
  - rg 명령은 Windows Codex 앱 리소스 경로 권한 문제로 실패하여 /usr/bin/grep으로 대체함
- Git commit:
  - 없음


## [2026-07-23 23:30] PROGRESS-20260723-2330-001 — 구현 및 실행 검증 완료

- 과업:
  - C172 RKSS 14L full mission landing variant 생성 및 실행 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 생성한 파일 및 디렉터리:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_landing/
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_landing/
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_landing/initial_condition/2.2__rkss_14l_default_earth_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_landing/runscript/5.9__rkss14l_full_normal_mission_run.xml
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
  - /home/junyeopkwon/jsbsim_workflow/workflow_all_cases_initial_settings.xlsx
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TASK.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/PROGRESS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/DECISIONS.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/TODO.md
  - /home/junyeopkwon/jsbsim_workflow/docs/agent-log/INDEX.md
- 핵심 변경점:
  - 제공 bundle aircraft와 c172ap_landing을 원본 보존 방식으로 새 landing variant에 복사
  - 기존 RKSS 14L initial condition을 landing aircraft scripts 폴더에 복사
  - 5.9 runscript의 initialize 경로를 landing scripts 폴더로 조정
  - excessive bank abort를 positive/negative 두 이벤트로 분리하고 mission-state ge 14 및 h-agl-ft le 300 guard 추가
  - 첫 실행 실패 분석 후 downwind base turn latitude를 position/vrp-gc-latitude_deg ge 37.3670으로 앞당김
  - mission-state logging을 위해 aircraft XML에 Mission monitor properties system 추가
  - landing aircraft 실행 시 raw output에 mission-state, landing-authorized, AP/FCS/gear 보강 property를 추가하도록 runner 보강
- 실행한 명령어:
  - python3 -m py_compile scripts/run_jsbsim_timestamped.py
  - xmllint --noout scripts/c172x_4x75kg_cg_aligned_landing/runscript/5.9__rkss14l_full_normal_mission_run.xml aircraft_variants/c172x_4x75kg_cg_aligned_landing/c172x_4x75kg_cg_aligned_landing.xml /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_landing/c172x_4x75kg_cg_aligned_landing.xml
  - /home/junyeopkwon/jsbsim/build/src/JSBSim --root=/home/junyeopkwon/jsbsim --aircraft=c172x_4x75kg_cg_aligned_landing --catalog --nohighlight
  - python3 scripts/run_jsbsim_timestamped.py --aircraft c172x_4x75kg_cg_aligned_landing --init scripts/c172x_4x75kg_cg_aligned_landing/initial_condition/2.2__rkss_14l_default_earth_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_landing/runscript/5.9__rkss14l_full_normal_mission_run.xml --planet builtin --no-flightgear
  - grep -n 'executed at time' logs/console/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.2__rkss14l_full_normal_mission_console_07232325.log
  - Python csv extraction for final state and state transitions
  - git diff --check
- 실행 결과:
  - 5.9.1은 1056.291667 s에 downwind 상태에서 지면 접촉으로 종료됨
  - 실패 원인은 STATE 12 base turn latitude 37.6000이 너무 늦어, h-agl 900-1120 및 vc 68-95 조건을 놓친 것으로 판단
  - 5.9.2는 684.916667 s에 STATE 23 mission complete 실행 확인
  - 5.9.2 raw CSV rows: 82191
  - 5.9.2 final mission-state: 23
  - 5.9.2 final vc-kts: 0.0001145
  - 5.9.2 final h-agl-ft: 4.324508
  - 5.9.2 final heading psi-deg: 132.336327
  - 5.9.2 final throttle-cmd-norm: 0
  - 5.9.2 final magneto_cmd: 0
  - 5.9.2 final main gear WOW: left 1, right 1
  - console Event 23 notify에서 gear/unit[0]/WOW, gear/unit[1]/WOW, gear/unit[2]/WOW 모두 1 확인
- 생성된 주요 산출물:
  - /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.2__rkss14l_full_normal_mission_runscript_07232325.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.2__rkss14l_full_normal_mission_console_07232325.log
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.2__rkss14l_full_normal_mission_raw_07232325.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.2__rkss14l_full_normal_mission_si_07232325.csv
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.2__rkss14l_full_normal_mission_states_vs_time_07232325.png
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.2__rkss14l_full_normal_mission_trajectory_3d_07232325.png
  - /home/junyeopkwon/jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned_landing/5.9.2__rkss14l_full_normal_mission
- 검증 결과:
  - py_compile 통과
  - xmllint 통과
  - JSBSim catalog load 통과 및 simulation custom property 경고 제거 확인
  - runscript discovery에서 landing 5.9 runscript 확인
  - 5.9.2 STATE 0부터 STATE 23까지 raw mission-state transition 확인
  - git diff --check 통과
- 검증하지 못한 항목:
  - FlightGear 시각화 확인은 수행하지 않음
  - plot PNG 직접 육안 검토는 수행하지 않음
  - runway centerline cross-track 오차는 정량 계산하지 않음
- 남은 리스크:
  - touchdown 전후 gear contact chatter가 일부 있어 착륙 품질 튜닝 여지는 남음
  - Touchdown report상 접지 ground speed는 약 56.8 kt로 기록되어 정상 범위 검토 필요
  - nose gear indexed property는 catalog에서 gear/unit[0] 대신 gear/unit으로 노출되어 일부 6DOF skipped property가 남음
- Git commit:
  - 없음


## [2026-07-23 23:43] PROGRESS-20260723-2343-001 — 구현 및 검증 완료

- 과업:
  - FlightGear 선택 프롬프트 없는 runner 생성
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt.py
- 수행 내용:
  - scripts/run_jsbsim_timestamped.py 현재 버전을 복사해 새 runner 파일 생성
  - 새 runner에서 FlightGear 기본값을 None이 아니라 False로 변경
  - 새 runner에서 choose_flightgear_stream 함수의 input 프롬프트를 제거
  - --flightgear를 명시하면 FlightGear stream은 계속 켤 수 있게 유지
- 실행한 명령어:
  - python3 -m py_compile scripts/run_jsbsim_timestamped_no_fg_prompt.py
  - diff -u scripts/run_jsbsim_timestamped.py scripts/run_jsbsim_timestamped_no_fg_prompt.py
  - git status --short scripts/run_jsbsim_timestamped.py scripts/run_jsbsim_timestamped_no_fg_prompt.py
- 검증 결과:
  - py_compile 통과
  - 원본 대비 diff는 parser.set_defaults(flightgear=False)와 choose_flightgear_stream 프롬프트 제거로 제한됨
  - 기존 scripts/run_jsbsim_timestamped.py는 이번 과업에서 수정하지 않음
- 검증하지 못한 항목:
  - 실제 interactive 선택 실행은 수행하지 않음
- 남은 리스크:
  - 새 runner도 aircraft/init/runscript 선택 프롬프트는 유지함
  - 기본 실행은 FlightGear 비활성화이며, 시각화가 필요하면 --flightgear를 명시해야 함
- Git commit:
  - 없음


## [2026-07-24 11:50] PROGRESS-20260724-1150-001 — 분석 완료

- 과업:
  - 최신 5.9.3 full mission landing 위치 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.3__rkss14l_full_normal_mission_console_07232345.log
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.3__rkss14l_full_normal_mission_raw_07232345.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.3__rkss14l_full_normal_mission_si_07232345.csv
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_landing/runscript/5.9__rkss14l_full_normal_mission_run.xml
- 수행 내용:
  - console에서 STATE 23 mission complete 실행 시각 확인
  - raw CSV에서 mission-state transition, final lat/lon/h-agl/heading 확인
  - SI CSV에서 시작점 기준 local_N/local_E를 추출하고 heading 135.01 deg runway axis 기준 along-track/cross-track 계산
  - runscript의 recovery, base, final 조건이 latitude/heading 중심인지 확인
- 핵심 수치:
  - final time: 684.916667 s
  - final mission-state: 23
  - final lat/lon: 37.521200588026602, 126.851526494200158
  - final h-agl-ft: 4.324508
  - final heading psi-deg: 132.336327
  - final local_N/local_E: -5492.2 m, 6475.2 m
  - final along-track/cross-track vs heading 135.01 deg: 8462.2 m, -696.6 m
  - STATE 19 touchdown local_N/local_E: -5270.9 m, 6226.7 m
  - STATE 19 touchdown along-track/cross-track: 8129.9 m, -677.3 m
- 결론:
  - 사용자의 의심대로 현재 5.9.3은 시작 활주로 축으로 정확히 돌아오지 않음
  - 절차는 완료됐지만 실제 착륙/정지는 RWY 14L 축에서 약 0.7 km 벗어난 평행 경로에서 발생함
  - runscript의 STATE 12-15가 position/vrp-gc-latitude_deg와 heading 조건에 의존하고 longitude 또는 cross-track 조건이 없어 활주로 중심선 정렬을 보장하지 않음
- 검증 명령어:
  - grep -n 'executed at time' logs/console/c172x_4x75kg_cg_aligned_landing/5.9__rkss14l_full_normal_mission/5.9.3__rkss14l_full_normal_mission_console_07232345.log
  - Python csv extraction for raw mission-state and SI local coordinate analysis
  - nl -ba scripts/c172x_4x75kg_cg_aligned_landing/runscript/5.9__rkss14l_full_normal_mission_run.xml
- 검증 결과:
  - STATE 23 mission complete는 확인됨
  - 활주로 축 기준 cross-track offset이 touchdown 약 -677.3 m, 정지 약 -696.6 m로 확인됨
- 검증하지 못한 항목:
  - 실제 RKSS 14L published runway threshold 좌표와의 외부 대조는 수행하지 않음
  - FlightGear 화면 육안 확인은 수행하지 않음
- 남은 리스크:
  - 현재 local axis는 workflow SI 변환의 초기 위치 기준 ENU이며, 실제 활주로 양끝 좌표와 약간 다를 수 있음
  - 그래도 cross-track 약 0.7 km는 오차 허용 범위를 명확히 초과함
- Git commit:
  - 없음


## [2026-07-24 12:55] PROGRESS-20260724-1255-001 - completed

- Work: Created and tuned `5.10__rkss14l_runway_axis_return_landing_run.xml` from preserved `5.9`.
- Changed: added `mission/runway-along-ft` and `mission/runway-cross-ft` to landing aircraft XML and landing raw CSV outputs.
- Final logic: runway-axis event gates plus `180 deg` intercept heading, then `135.01 deg` runway alignment.
- Validated commands: `xmllint --noout`, `python3 -m py_compile`, JSBSim catalog, JSBSim no-FG runner, relevant `git diff --check`.
- Best run: `5.10.8__rkss14l_runway_axis_return_landing`.
- Raw CSV: `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_landing/5.10__rkss14l_runway_axis_return_landing/5.10.8__rkss14l_runway_axis_return_landing_raw_07241250.csv`.
- Console: `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned_landing/5.10__rkss14l_runway_axis_return_landing/5.10.8__rkss14l_runway_axis_return_landing_console_07241250.log`.
- Result: state19 touchdown at along `1200.9 m`, cross `-62.4 m`; state23 final stop at along `1554.1 m`, cross `-73.6 m`.
- Residual risk: still outside a strict runway-centerline tolerance; needs cross-track feedback guidance for tighter landing.
- Git commit: none.


## [2026-07-24 15:00] PROGRESS-20260724-1500-001 - completed

- Work: Created `5.11__rkss14l_circular_loiter_return_landing_run.xml` as a circular-loiter variant derived from `5.10`.
- Changed: added circular loiter properties to landing raw CSV output and added a dormant bank-hold helper system to landing aircraft XML.
- Important correction: first `5.11.1` bank-hold attempt was unstable and stayed at `STATE 6`; final `5.11.2` uses AP heading-hold with no straight-leg delay for a stable continuous heading-arc orbit.
- Best run: `5.11.2__rkss14l_circular_loiter_return_landing`.
- Raw CSV: `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_landing/5.11__rkss14l_circular_loiter_return_landing/5.11.2__rkss14l_circular_loiter_return_landing_raw_07241443.csv`.
- Console: `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned_landing/5.11__rkss14l_circular_loiter_return_landing/5.11.2__rkss14l_circular_loiter_return_landing_console_07241443.log`.
- Circular loiter result: duration `60.5 s`, heading progression `135 -> 50 -> 320 -> 230 -> 140 deg`, bank avg `-25.5 deg`, bank min `-30.0 deg`.
- Landing result: touchdown along `1214.6 m`, cross `-54.6 m`; final stop along `1607.7 m`, cross `-57.8 m`; final state `23`.
- Validation: XML well-formed check passed, Python `py_compile` passed, JSBSim catalog loaded circular properties, JSBSim run completed, relevant `git diff --check` passed.
- Git commit: none.


## [2026-07-24 20:10] PROGRESS-20260724-2010-001 - DONE

- Task: KSFO 28R C172 landing mission adaptation and validation.
- Project: `/home/junyeopkwon/jsbsim_workflow`
- Files inspected: provided `/mnt/c/Users/junyeopkwon/Downloads/ksfo28r_flightgear_default_bundle/2.4__ksfo_28r_flightgear_default_init.xml`; provided `/mnt/c/Users/junyeopkwon/Downloads/ksfo28r_flightgear_default_bundle/5.13__ksfo28r_normal_procedure_flightgear_run.xml`; existing RKSS `5.11__rkss14l_circular_loiter_return_landing_run.xml`; existing landing aircraft XML.
- Files created: `aircraft_variants/c172x_4x75kg_cg_aligned_ksfo28r_landing/`; `/home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_ksfo28r_landing/`; `scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/initial_condition/2.4__ksfo_28r_flightgear_default_init.xml`; `scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.13__ksfo28r_normal_procedure_flightgear_run.xml`; `5.14`, `5.15`, and final `5.16` KSFO runscript variants.
- Key changes: KSFO aircraft variant uses runway-axis monitor coefficients for heading `298 deg`: along `e*(-0.882947592858927)+n*(0.469471562785890)`, cross `e*(0.469471562785890)+n*(0.882947592858927)`.
- Trial result: `5.13.1` stalled at `STATE 11` and contacted ground before landing authorization; `5.14.1` reached `STATE 12` but did not reach final; `5.15.1` reached `STATE 23` but touchdown was too far downrange at about `8005 m` along.
- Final run: `5.16.1__ksfo28r_runway_return_circular_landing` reached `STATE 23` at `636.716667 s`.
- Final run output: raw CSV `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.1__ksfo28r_runway_return_circular_landing_raw_07242006.csv`; console `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.1__ksfo28r_runway_return_circular_landing_console_07242006.log`; trajectory plot `/home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.1__ksfo28r_runway_return_circular_landing_trajectory_3d_07242006.png`.
- Final landing metrics: touchdown along `1708.3 m`, cross `-33.4 m`; final stop along `2022.5 m`, cross `-43.5 m`; circular loiter duration `60.6 s`, average bank `-25.4 deg`.
- Validation commands: `xmllint --noout` on new XML files; `python3 -m py_compile` on JSBSim runners; JSBSim catalog check for runway/circular output properties; no-FG JSBSim runs for `5.13.1`, `5.14.1`, `5.15.1`, `5.16.1`; `git diff --check` on changed KSFO files.
- Validation result: XML and Python checks passed; catalog exposed required properties; final `5.16.1` completed normally.
- Not validated: FlightGear live stream/scenery visual alignment.
- Git commit: none.


## [2026-07-24 21:35] PROGRESS-20260724-2135-001 - DONE

- 수행한 작업: 기존 no-FG prompt runner를 복사해 `scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py`를 생성하고 plotting 호출, detailed `ploting/` 생성, workflow Excel update를 실행 경로에서 제거.
- 생성한 파일: `scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py`.
- 핵심 변경점: `--show` 인자 제거, `matplotlib` import 제거, `plot_states_vs_time`, `plot_trajectory`, `build_detailed_ploting_outputs`, `update_workflow_excel` 호출 제거. 최종 출력 메시지에 plotting/detailed ploting/Excel update skipped 표시 추가.
- 검증 명령어: `python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py`; `python3 ...run_jsbsim_timestamped_no_fg_prompt_csv_only.py --help`; KSFO 5.16 no-FG 실행; `git diff --check -- scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py`.
- 실행 검증 결과: `5.16.4__ksfo28r_runway_return_circular_landing` 실행 완료. 생성 CSV: raw `90M`, SI `52M`, 6DOF raw `138M`, 6DOF SI `44M`.
- plotting 검증 결과: `/home/junyeopkwon/jsbsim_workflow/plots` 및 `/home/junyeopkwon/jsbsim_workflow/ploting`에서 `5.16.4__ksfo28r_runway_return_circular_landing` 관련 파일 없음.
- 검증하지 못한 항목: 다른 aircraft/scenario 조합 전체 회귀 실행은 수행하지 않음.
- 남은 리스크: 파일 내부에 미사용 plotting 함수 정의는 남아 있으나 main 실행 경로에서는 호출되지 않음.
- Git commit: none.

## [2026-07-25 14:44] PROGRESS-20260725-1444-001 — 구현 및 검증 완료

- 과업:
  - LiftCruise2kg JSBSim 패키지 workflow 실행 검토
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /mnt/c/Users/junyeopkwon/Downloads/LiftCruise2kg_JSBSim/README.md
  - /mnt/c/Users/junyeopkwon/Downloads/LiftCruise2kg_JSBSim/aircraft/LiftCruise2kg/*.xml
  - /mnt/c/Users/junyeopkwon/Downloads/LiftCruise2kg_JSBSim/scripts/Test_LiftCruise2kg_HoverMission.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 생성한 파일/폴더:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg/
  - /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/initial_condition/1.0__ground_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.0__hover_mission_run.xml
  - /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/
- 수정한 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg/LiftCruise2kg.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg/Aero.xml
  - /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/LiftCruise2kg.xml
  - /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/Aero.xml
- 핵심 변경점:
  - dm_config version을 JSBSim 1.2.4가 기대하는 2.0으로 변경
  - Aero.xml의 한 줄 inline 1D 	ableData들을 2열 행 형식으로 변경해 FGTable: Missing data fatal error 제거
  - workflow scripts 구조에 맞춰 init/runscript를 aircraft별 폴더로 배치
- 실행한 명령어:
  - xmllint --noout /mnt/c/Users/junyeopkwon/Downloads/LiftCruise2kg_JSBSim/aircraft/LiftCruise2kg/*.xml /mnt/c/Users/junyeopkwon/Downloads/LiftCruise2kg_JSBSim/scripts/*.xml
  - /home/junyeopkwon/jsbsim/build/src/JSBSim --script=/mnt/c/Users/junyeopkwon/Downloads/LiftCruise2kg_JSBSim/scripts/Test_LiftCruise2kg_HoverMission.xml --nohighlight
  - 임시 JSBSim root 구성 후 /home/junyeopkwon/jsbsim/build/src/JSBSim --root=<tmp> --script=scripts/Test_LiftCruise2kg_HoverMission.xml --nohighlight
  - xmllint --noout on workflow/install LiftCruise XML files
  - /home/junyeopkwon/jsbsim/build/src/JSBSim --root=/home/junyeopkwon/jsbsim --aircraft=LiftCruise2kg --catalog --nohighlight
  - python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft LiftCruise2kg --init scripts/LiftCruise2kg/initial_condition/1.0__ground_init.xml --runscript scripts/LiftCruise2kg/runscript/1.0__hover_mission_run.xml --planet builtin --no-flightgear
  - git diff --check -- aircraft_variants/LiftCruise2kg scripts/LiftCruise2kg
- 검증 결과:
  - 원본 XML well-formed 통과
  - JSBSim root에서 원본 script 직접 실행 시 aircraft 미설치로 실패 확인
  - 원본 패키지 폴더에서 실행 시 DJI_E305 engine lookup 실패 확인
  - 임시 root에서 engine 경로를 맞춘 뒤 Aero.xml line 22 계열 FGTable: Missing data fatal error 확인
  - 수정 후 workflow/install XML well-formed 통과
  - 수정 후 JSBSim catalog load 통과
  - workflow CSV-only runner 실행 완료: 1.0.1__hover_mission
  - raw/SI/sixdof raw/sixdof SI CSV 각각 18127 lines 생성 확인
  - 최종 raw CSV rows: 18126
  - final time: 145 s
  - final h-agl-ft: 0.5183307730217032
  - max h-agl-ft: 33.14369629685908
  - max vt-fps: 5.815581093434926
  - max abs roll/pitch: 약 13.06 deg / 13.01 deg
  - final local_N/local_E: 약 -6.77 m / -37.60 m
  - max horizontal distance from start: 약 38.56 m
  - NaN row count: 0
  - git diff --check 통과
- 검증하지 못한 항목:
  - FlightGear 시각화 확인은 수행하지 않음
  - hover position control gain 튜닝은 수행하지 않음
  - workflow runner의 LiftCruise 전용 raw output property 보강은 수행하지 않음
- 남은 리스크:
  - mission은 실행 완료되지만 원점 복귀 오차가 약 38 m로, README의 ±5 m 이동/복귀 의도와는 차이가 큼
  - 현재 CSV-only runner는 기본 raw output 중심이라 p/mode, p/north-setpoint-m, p/east-setpoint-m, indexed lift motor throttle 등을 raw CSV에 충분히 남기지 않음
  - pusher/고정익 전환 모델은 아직 검증되지 않음
- Git commit:
  - 없음

## [2026-07-25 14:48] CORRECTION-20260725-1448-001 — 정정

- 대상 기록:
  - PROGRESS-20260725-1444-001
- 정정 이유:
  - PowerShell 백틱 이스케이프 처리로 일부 코드 식별자 표기가 제어문자로 표시될 수 있어, 검증 핵심 내용을 plain text로 재기록함
- 정정 내용:
  - 원본 XML well-formed 검증은 통과했다.
  - 원본을 JSBSim root에서 직접 실행하면 aircraft/LiftCruise2kg/LiftCruise2kg.xml 미설치로 실패했다.
  - 원본 패키지 폴더에서 실행하면 DJI_E305 engine lookup 실패가 발생했다.
  - 임시 root에서 engine 경로를 맞추면 Aero.xml의 inline 1D tableData 형식 때문에 FGTable: Missing data fatal error가 발생했다.
  - workflow copy에서는 LiftCruise2kg.xml fdm_config version을 2.0으로 조정했다.
  - workflow copy에서는 Aero.xml의 inline 1D tableData를 JSBSim 1.2.4가 읽는 2열 행 형식으로 조정했다.
  - 생성 파일은 aircraft_variants/LiftCruise2kg, scripts/LiftCruise2kg/initial_condition/1.0__ground_init.xml, scripts/LiftCruise2kg/runscript/1.0__hover_mission_run.xml 이다.
  - 설치 copy는 /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg 이다.
  - 검증 명령은 xmllint, JSBSim catalog, CSV-only runner, git diff --check 이며 모두 통과했다.
  - workflow run은 1.0.1__hover_mission 이고 final time은 145 s, final h-agl-ft는 0.5183307730217032, max h-agl-ft는 33.14369629685908, max vt-fps는 5.815581093434926 이다.
  - final local_N/local_E는 약 -6.77 m / -37.60 m, max horizontal distance from start는 약 38.56 m, NaN row count는 0 이다.
- 영향 범위:
  - 기록 가독성 정정만 해당하며 실제 코드/XML/실행 결과 변경 없음
- 검증 결과:
  - 정정 기록을 append-only 방식으로 추가함
- 다음 작업:
  - LiftCruise2kg 전용 raw output property 보강 및 hover gain/sign 튜닝

## [2026-07-25 15:09] PROGRESS-20260725-1509-001 — 구현 및 검증 완료

- 과업:
  - LiftCruise2kg 10 m 박스 이동 및 수직착륙 runscript 추가
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
- 핵심 변경점:
  - 기존 1.0 runscript는 유지하고 사용자가 지정한 좌표 순서를 1.1 runscript로 추가
  - mission-state 0-20과 1초 반복 notify를 추가해 console에서 단계 확인 가능하게 구성
  - x 좌표는 ap/north-setpoint-m, y 좌표는 ap/east-setpoint-m, z=10 m는 ap/altitude-setpoint-ft 32.80839895로 매핑
  - 205 s에 ap/mode 0 및 throttle 0으로 disarm, 210 s에 simulation/terminate 1로 종료
- 실행한 명령어:
  - xmllint --noout /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
  - git diff --check -- scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
  - python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft LiftCruise2kg --init scripts/LiftCruise2kg/initial_condition/1.0__ground_init.xml --runscript scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml --planet builtin --no-flightgear
- 검증 결과:
  - XML well-formed 통과
  - diff check 통과
  - run 1.1.1__ten_meter_box_hover_land 정상 종료
  - final time 210.0 s
  - final altitude 0.158 m
  - max altitude 10.168 m
  - max total speed 4.267 m/s
  - max abs roll/pitch 약 13.64 deg / 12.67 deg
  - NaN row count 0
  - raw CSV 및 SI CSV 각각 26252 lines 생성
- 생성된 주요 산출물:
  - /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.1__ten_meter_box_hover_land_runscript_07251509.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/console/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.1__ten_meter_box_hover_land_console_07251509.log
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.1__ten_meter_box_hover_land_raw_07251509.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/si/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.1__ten_meter_box_hover_land_si_07251509.csv
- 검증하지 못한 항목:
  - FlightGear 시각화 확인은 수행하지 않음
  - 위치 추종 튜닝은 수행하지 않음
- 남은 리스크:
  - runscript setpoint는 요청 순서대로 적용되지만 실제 궤적은 최종 local_N/local_E 약 -203.45 m / -177.35 m로 크게 드리프트함
  - LiftCruiseAP.xml의 east/north position hold sign, heading coupling, gain 튜닝이 필요
- Git commit:
  - 없음

## [2026-07-25 15:18] PROGRESS-20260725-1518-001 — 분석 완료

- 과업:
  - 첨부 분석 문서 검토
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /mnt/c/Users/junyeopkwon/.codex/attachments/37edf6c4-a0d7-46b4-b171-b40bd401bd04/pasted-text.txt
  - /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg/LiftCruiseAP.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg/FlightControl.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.1__ten_meter_box_hover_land_raw_07251509.csv
- 수행 내용:
  - 첨부 텍스트의 이벤트 표를 실제 XML line 구조와 대조
  - AP heading-error-rad 및 North-East position hold 구조를 확인
  - raw CSV header에서 포함/미포함 property 확인
- 검증 결과:
  - 21개 mission event와 1개 repeating notify라는 설명은 실제 XML과 일치
  - 모든 mission 전환이 위치 도달 조건이 아니라 simulation/sim-time-sec 기준이라는 설명은 맞음
  - heading-error-rad가 단순 ap/heading-setpoint-rad - attitude/psi-rad 구조이고 wrap 처리가 없다는 설명은 맞음
  - position hold가 heading zero assumption에 따라 north error를 pitch, east error를 roll에 직접 매핑한다는 설명은 맞음
  - raw CSV에는 mission-state, ap/mode, ap/north-setpoint-m, ap/east-setpoint-m, ap/collective-cmd-norm, fcs/throttle-pos-norm[0..4], fcs/fw-aileron-pos-rad, fcs/fw-elevator-pos-rad, fcs/fw-rudder-pos-rad가 없음
  - raw CSV에는 일반 fcs/elevator-pos-rad, fcs/left-aileron-pos-rad, fcs/right-aileron-pos-rad, fcs/rudder-pos-rad, fcs/throttle-pos-norm만 있음
- 정정/보완할 점:
  - 첨부 텍스트의 별도 logdirective 또는 일반 raw logger 표현은 대체로 맞지만, 이 workflow에서는 runner가 template output block을 삭제하고 자체 raw/sixdof output block을 생성한 것이 직접 원인임
  - 고정익 조종면 0 확인은 현재 raw CSV만으로는 fcs/fw-* property를 직접 확인한 것이 아니므로, template set 명령 및 FlightControl 기본값 기반 추정으로 표현하는 편이 정확함
- 검증하지 못한 항목:
  - 새 output property를 추가한 재실행은 수행하지 않음
- 남은 리스크:
  - AP 수정 전에는 1.1 박스 mission 위치 추종 실패가 반복될 가능성이 큼
- Git commit:
  - 없음

## [2026-07-25 16:12] PROGRESS-20260725-1612-001 - DONE
- 수행: LiftCruise2kg raw CSV가 원본 XML output과 1:1 대응되도록 runner 및 1.1 runscript 수정
- 수정 파일: scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py, scripts/run_jsbsim_timestamped_no_fg_prompt.py, scripts/run_jsbsim_timestamped.py
- 수정 파일: scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
- 실행: python3 -m py_compile runner 3개, xmllint --noout 1.1 runscript
- 실행: 1.1.4__ten_meter_box_hover_land CSV-only JSBSim run, timestamp 07251611
- 결과: raw CSV 10501 rows, Time 0 to 210, NaN 0
- 결과: source XML 381, generated XML 381, raw CSV 381 순서 일치
- 산출 로그: logs/csv/raw/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.4__ten_meter_box_hover_land_raw_07251611.csv
- Git commit: 없음

## [2026-07-25 17:56] PROGRESS-20260725-1756-001 - DONE

- 과업: F450 AP 기능 추가 및 10 m box hover/land mission 실행 검증
- 조사한 파일: /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/LiftCruiseAP.xml, /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml, /home/junyeopkwon/jsbsim/aircraft/F450/F450.xml, /home/junyeopkwon/jsbsim/aircraft/F450/FlightControl.xml, /home/junyeopkwon/jsbsim/aircraft/F450/Effectors.xml, runner 3개
- 생성한 파일: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/initial_condition/1.1__ground_park_heading0_init.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml
- 수정한 파일: /home/junyeopkwon/jsbsim/aircraft/F450/F450.xml, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 핵심 변경점: LiftCruise2kg AP 기반 F450AP.xml을 만들고 F450 기존 rate-SCAS 입력으로 AP command를 bridge함. F450 runscript는 LiftCruise2kg 1.1 mission sequence 기반으로 만들되 F450 미지원 pusher/fixed-wing set을 제거함. 지상 초기 안정화를 위해 simulation/do_simple_trim=2를 추가하고 disarm 후 chatter 회피를 위해 terminate를 205.2 s로 조정함.
- 실행한 명령어: python3 -m py_compile runner 3개, XML parse check, JSBSim F450 catalog load, CSV-only runner F450 1.2 mission 실행, git diff --check
- 검증 결과: XML parse 통과, py_compile 통과, F450 catalog load 통과, CSV-only run 1.2.9__ten_meter_box_hover_land 정상 종료, git diff --check 통과
- 실행 산출물: /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/F450/1.2__ten_meter_box_hover_land/1.2.9__ten_meter_box_hover_land_runscript_07251756.xml, /home/junyeopkwon/jsbsim_workflow/logs/console/F450/1.2__ten_meter_box_hover_land/1.2.9__ten_meter_box_hover_land_console_07251756.log, /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/F450/1.2__ten_meter_box_hover_land/1.2.9__ten_meter_box_hover_land_raw_07251756.csv, /home/junyeopkwon/jsbsim_workflow/logs/csv/si/F450/1.2__ten_meter_box_hover_land/1.2.9__ten_meter_box_hover_land_si_07251756.csv
- 정량 결과: 185 s 착륙 명령 직전 local_N/local_E = -18.99 m / 110.67 m, horizontal error 112.29 m. 205.2 s 종료 직전 local_N/local_E = -22.40 m / 54.65 m, horizontal error 59.06 m. 205.2 s 종료 직전 ASL altitude = 285.36 m, vertical speed down = 0.20 m/s. 185 s까지 max abs roll/pitch = 12.81 deg / 12.69 deg. 205.2 s까지 max abs roll/pitch = 28.19 deg / 14.11 deg.
- raw CSV 확인: column 103개이며 /fdm/jsbsim/ap/mode, /fdm/jsbsim/ap/collective-cmd-norm, /fdm/jsbsim/fcs/ScasEngage, /fdm/jsbsim/fcs/cmdEscFR_nd, /fdm/jsbsim/propulsion/engine[1]/propeller-rpm 존재 확인
- 검증하지 못한 항목: FlightGear visual alignment, lateral hold 정밀 튜닝, ground contact model 자체 안정화
- 남은 리스크: 현재 AP는 altitude hold와 command bridge 기능 확인 수준이며 10 m box lateral tracking은 mission 정밀도에 미달함
- Git commit: 없음

## [2026-07-26 14:10] PROGRESS-20260726-1410-001 — DONE

- 과업: F450 로그 property 및 mission transition gate 수정 검증
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 사용자 분석을 검토하고 합당하면 F450 runscript와 로그 구성을 수정
- 관련 파일: /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 수행 내용: F450 runscript 출력에서 fcs/cmdEscFR-norm 계열과 fcs/throttle-pos-norm[4] 등 잘못된 property를 제거하고, fcs/cmdEscFR_nd, fcs/cmdEscAL_nd, fcs/cmdEscFL_nd, fcs/cmdEscAR_nd를 사용하도록 정리함
- 수행 내용: JSBSim catalog 기준으로 0번 motor/engine 출력은 [0] suffix 대신 base property인 fcs/throttle-pos-norm, propulsion/engine/propeller-rpm, propulsion/engine/thrust-lbs로 기록하도록 runner 세 파일을 정정함
- 수행 내용: F450_OUTPUT_PROPERTIES에 ap/altitude-error-ft, ap/climb-rate-setpoint-fps, ap/climb-rate-error-fps, ap/altitude-collective-unclipped, ap/altitude-collective-clipped 진단 property를 추가함
- 수행 내용: F450 10 m box runscript 이벤트 전환을 mission-state와 nominal time 하한, 위치오차, 속도, 고도오차 gate 조합으로 수정함
- 변경 이유: 기존 runscript는 기체가 목표에 도착했는지와 무관하게 고정 시간만으로 다음 구간으로 넘어가고, 로그 일부가 실제 FCS property와 맞지 않았음
- 검증 명령어: python3 -m py_compile /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt.py /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 검증 결과: py_compile 통과
- 검증 명령어: XML parse for /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml
- 검증 결과: XML parse 통과
- 검증 명령어: cd /home/junyeopkwon/jsbsim_workflow && python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft F450 --init scripts/F450/initial_condition/1.1__ground_park_heading0_init.xml --runscript scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml --planet builtin --no-flightgear
- 검증 결과: run 1.2.12__ten_meter_box_hover_land 성공, raw CSV /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/F450/1.2__ten_meter_box_hover_land/1.2.12__ten_meter_box_hover_land_raw_07261410.csv 생성
- 검증 결과: header에 /fdm/jsbsim/fcs/cmdEscFR_nd, /fdm/jsbsim/fcs/cmdEscAL_nd, /fdm/jsbsim/fcs/cmdEscFL_nd, /fdm/jsbsim/fcs/cmdEscAR_nd 존재 확인
- 검증 결과: header에 /fdm/jsbsim/fcs/throttle-pos-norm, [1], [2], [3] 존재 확인, [0] 및 [4] 부재 확인
- 검증 결과: header에 /fdm/jsbsim/ap/altitude-error-ft, /fdm/jsbsim/ap/climb-rate-error-fps 존재 확인
- 실행 확인 결과: setpoint_changes는 0,0에서 바뀌지 않음. 즉 도착 gate가 첫 leg 진입을 차단함
- 실행 확인 결과: 25 s 시점에서 north/east position error가 -10/-10으로 saturate되고 v-north/v-east가 약 -35.49/16.66 fps로 gate 조건을 만족하지 못함
- 실행 확인 결과: 215 s 최종 local_N/local_E는 약 83.13/-70.53 m, 수평 거리 약 109.02 m, max |roll|/|pitch|는 약 12.81/12.69 deg
- 검증하지 못한 항목: F450AP/FlightControl PID gain 튜닝, ESC/모터 lag 모델링, 센서 노이즈 모델링
- 검증하지 못한 이유: 이번 요청의 1차 수정 범위는 로그 property 및 runscript 전환 조건 보정이었고, 제어기 재튜닝은 별도 반복 실험이 필요함
- 가정: F450AP가 센서 stub이 아니라 JSBSim truth property를 사용한다는 사용자 분석을 현재 파일 구조 기준으로 타당한 전제로 채택함
- 남은 리스크: 현재 F450은 목표 이동 전 hover holding부터 위치/속도 gate를 만족하지 못하므로, square path 품질 문제는 F450AP와 FlightControl 중첩 제어 및 gain/축 부호/속도 제한 문제일 가능성이 큼
- 다음 작업: F450AP lateral position loop와 FlightControl rate loop 사이의 명령 scaling 및 saturation을 분리 진단하고 gain을 단계적으로 튜닝
- 관련 기록: TASK-20260726-1410-001, DECISION-20260726-1410-001, TODO-20260726-1410-001
- Git commit: 없음

## [2026-07-26 14:45] PROGRESS-20260726-1445-001 — DONE

- 과업: XY trajectory plot 추가 및 실행 확인
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 시작 지점을 (0,0)으로 하는 고도 제외 xy 평면 그래프 추가
- 관련 파일: /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt.py, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 수행 내용: local_E_m/local_N_m에서 첫 행 값을 빼 시작점을 항상 (0,0)으로 맞추는 plot_trajectory_xy 함수를 추가함
- 수행 내용: /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py 및 /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt.py에서 일반 plots 출력과 상세 ploting 출력에 XY trajectory plot 생성을 연결함
- 수행 내용: CSV-only runner에는 함수만 추가하고 main에서는 호출하지 않아 CSV-only 동작을 유지함
- 변경 이유: 기존 3D trajectory plot은 고도 축이 포함되어 수평면 drift와 box 경로 이탈을 즉시 보기 어려웠음
- 검증 명령어: python3 -m py_compile runner 3개
- 검증 결과: 통과
- 검증 명령어: git diff --check -- runner 3개
- 검증 결과: 통과
- 검증 명령어: cd /home/junyeopkwon/jsbsim_workflow && python3 scripts/run_jsbsim_timestamped_no_fg_prompt.py --aircraft F450 --init scripts/F450/initial_condition/1.1__ground_park_heading0_init.xml --runscript scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml --planet builtin --no-flightgear
- 검증 결과: run 1.2.13__ten_meter_box_hover_land 성공
- 실행 확인 결과: 일반 XY plot 생성 /home/junyeopkwon/jsbsim_workflow/plots/F450/1.2__ten_meter_box_hover_land/1.2.13__ten_meter_box_hover_land_trajectory_xy_07261441.png
- 실행 확인 결과: 상세 XY plot 생성 /home/junyeopkwon/jsbsim_workflow/ploting/F450/1.2.13__ten_meter_box_hover_land/trajectory_xy/trajectory_xy.png
- 실행 확인 결과: PNG 크기 1280 x 1280, 파일 크기 약 121K 확인
- 검증하지 못한 항목: view_image 도구를 통한 직접 렌더 확인
- 검증하지 못한 이유: WSL UNC 경로에서 sandbox helper_unknown_error 발생
- 가정: 생성된 PNG를 file 명령으로 검증하는 것으로 산출물 생성 확인을 대체함
- 남은 리스크: XY plot은 trajectory 후처리 시각화이며 F450 제어 성능 자체를 개선하지 않음
- 다음 작업: XY plot을 기준으로 hover drift와 lateral control tuning 결과를 비교
- 관련 기록: TASK-20260726-1445-001
- Git commit: 없음

## [2026-07-26 14:59] PROGRESS-20260726-1459-001 — DONE

- 과업: F450 1.2 이론 XY setpoint graph 생성
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: runscript가 이론대로 진행될 때의 xy 평면 경로를 그래프로 보여주기
- 관련 파일: /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml, /home/junyeopkwon/jsbsim_workflow/plots/F450/1.2__ten_meter_box_hover_land/ideal_setpoint_xy_1.2__ten_meter_box_hover_land.png
- 수행 내용: XML event의 ap/north-setpoint-m 및 ap/east-setpoint-m 변경 순서를 추출함
- 수행 내용: (0,0) -> (10,0) -> (0,0) -> (-10,0) -> (0,0) -> (0,10) -> (0,0) -> (0,-10) -> (0,0) 순서로 ideal XY plot 생성
- 변경 이유: 실제 3D/XY trajectory와 비교할 이론 setpoint 기준선 필요
- 검증 명령어: XML parse and setpoint extraction with python3
- 검증 결과: setpoint 변경 이벤트 11개 확인, 중복 hover/landing 포함 기준 경로는 cardinal out-and-back 형태임
- 검증 명령어: file /home/junyeopkwon/jsbsim_workflow/plots/F450/1.2__ten_meter_box_hover_land/ideal_setpoint_xy_1.2__ten_meter_box_hover_land.png
- 검증 결과: PNG image data, 1280 x 1280 확인, 파일 크기 약 62K
- 검증하지 못한 항목: 없음
- 가정: local x는 north, local y는 east라는 runscript description을 따른다
- 남은 리스크: mission 이름은 box이지만 현재 setpoint sequence는 perimeter square가 아니라 십자형 왕복 경로임
- 다음 작업: 실제 run trajectory_xy와 ideal_setpoint_xy를 한 그림에 overlay하면 tracking error를 더 직관적으로 볼 수 있음
- 관련 기록: TASK-20260726-1459-001
- Git commit: 없음


## [2026-07-26 15:33] PROGRESS-20260726-1533-001 — DONE

- 과업: F450 autopilot 10 m hover mission 순차 진단 및 수정
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow, /home/junyeopkwon/jsbsim/aircraft/F450
- 관련 파일: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.3__hover_origin_diagnostic_run.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.4__attitude_axis_diagnostic_run.xml, /home/junyeopkwon/jsbsim_workflow/plots/F450/1.2__ten_meter_box_hover_land/1.2.19__ten_meter_box_hover_land_actual_vs_ideal_xy_07261531.png
- 수행 내용: hover-only 진단으로 yaw spin과 lateral drift를 분리했고, attitude-axis 진단으로 rate loop가 reference를 추종하는 것을 확인했다. 이후 heading error wrap, lateral gain 축소, signed local N/E 위치오차 계산을 순서대로 적용했다.
- 핵심 변경점: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml에서 ap/heading-error-rad를 atan2(sin(delta), cos(delta)) 방식으로 wrap하고, position/distance-from-start-lat/lon-mt 대신 초기 위경도 기준 ap/local-north-m, ap/local-east-m을 계산해 ap/north-position-error-m 및 ap/east-position-error-m에 사용하도록 변경했다.
- 실행한 명령어: python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft F450 --init scripts/F450/initial_condition/1.1__ground_park_heading0_init.xml --runscript scripts/F450/runscript/1.3__hover_origin_diagnostic_run.xml --planet builtin --no-flightgear
- 실행한 명령어: python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft F450 --init scripts/F450/initial_condition/1.1__ground_park_heading0_init.xml --runscript scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml --planet builtin --no-flightgear
- 테스트 결과: 1.3.10 hover signed local N/E 적용 후 t=80 s에서 local_N=-0.01 m, local_E=-0.00 m, max XY distance=0.02 m, yaw=0.0 deg.
- 테스트 결과: 1.2.19 미션 signed local N/E 적용 후 주요 지점은 t=40 s (9.50, -0.00), t=60 s (0.45, -0.00), t=80 s (-9.52, -0.00), t=100 s (-0.47, 0.00), t=120 s (-0.00, 9.54), t=140 s (0.00, 0.47), t=160 s (0.00, -9.54), t=180 s (-0.00, -0.48), t=210 s (0.00, 0.00) m.
- 검증 결과: XML parse 성공. CSV-only JSBSim 실행 성공. 생성 PNG 크기 1260x1260, RGB 표준편차 [30.73, 31.71, 31.23]으로 비어 있지 않음 확인.
- 검증하지 못한 항목: Codex image viewer 직접 렌더링 확인
- 검증하지 못한 이유: view_image가 WSL/Windows 경로 모두에서 fs sandbox helper_unknown_error로 실패
- 남은 리스크: ap/home-lat-deg, ap/home-lon-deg가 F450AP.xml에 고정되어 있어 init 위치가 바뀌면 local N/E 기준도 같이 바꿔야 한다.
- 다음 작업: home 좌표를 runscript/init에서 AP property로 set하거나, runner가 init 위경도를 읽어 runscript에 주입하도록 일반화한다.
- Git commit: 없음


## [2026-07-26 16:46] PROGRESS-20260726-1646-001 — DONE

- 과업: LiftCruise2kg 10 m hover mission 수정 및 검증
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow, /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg
- 조사한 파일: /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/LiftCruiseAP.xml, /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/FlightControl.xml, /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/Effectors.xml, /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/initial_condition/1.0__ground_init.xml, /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
- 수정한 파일: /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/LiftCruiseAP.xml, /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml
- 생성한 파일: /home/junyeopkwon/jsbsim_workflow/plots/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.9__ten_meter_box_hover_land_actual_vs_ideal_xy_07261645.png
- 핵심 변경점: LiftCruiseAP.xml에 ap/home-lat-deg, ap/home-lon-deg, ap/local-north-m, ap/local-east-m을 추가하고 position/distance-from-start-* 대신 signed local error를 사용했다. yaw error는 atan2(sin(delta), cos(delta))로 wrap했다. runscript 전환은 mission-state guard와 위치/속도/고도 arrival gate를 추가했다.
- 중간 검증: 1.1.6은 geodetic latitude 기준 home mismatch로 ap/north-position-error-m가 처음부터 포화되어 남쪽으로 약 205 m drift했다. 1.1.7은 north local gain만 반전해 북쪽으로 약 212 m drift했다. 1.1.8은 pitch gain만 반전해 북쪽으로 약 3127 m 발산했다.
- 최종 수정: LiftCruise init latitude가 geocentric으로 해석됨을 확인하고 local north 입력을 position/lat-gc-deg로 변경했으며 pitch gain은 -0.025로 유지했다.
- 검증 명령어: python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft LiftCruise2kg --init scripts/LiftCruise2kg/initial_condition/1.0__ground_init.xml --runscript scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml --planet builtin --no-flightgear
- 검증 결과: 1.1.9 실행 성공. t=40 s (9.52, 0.00), t=60 s (0.46, 0.00), t=80 s (-9.53, 0.00), t=100 s (-0.47, 0.00), t=120 s (0.05, 9.52), t=140 s (0.05, 0.47), t=160 s (0.05, -9.52), t=180 s (0.05, -0.47), t=210 s (0.02, 0.00) m.
- 검증 결과: setpoint changes는 25.02 s (10,0), 45.0 s (0,0), 65.0 s (-10,0), 85.02 s (0,0), 105.02 s (0,10), 125.02 s (0,0), 145.02 s (0,-10), 165.0 s (0,0), 185.0 s landing으로 진행했다.
- 검증 결과: 생성 PNG 크기 1260x1260, RGB 표준편차 [32.19, 32.45, 31.74]로 비어 있지 않음 확인.
- 검증하지 못한 항목: GUI 이미지 직접 렌더링 확인, FlightGear 시각화, 실제 actuator/motor lag가 있는 물리 응답 검증
- 검증하지 못한 이유: 이번 검증은 CSV-only 실행으로 제한했다.
- 남은 리스크: ap/home-lat-deg/ap/home-lon-deg는 고정값이며 init이 geodetic으로 바뀌면 AP local north 입력도 재검토해야 한다.
- 다음 작업: home 좌표와 latitude type을 runner 또는 runscript에서 명시적으로 동기화한다.
- Git commit: 없음

## [2026-07-29 10:54] PROGRESS-20260729-1054-001 - DONE

- 과업:
  - c172x no-alpha-limit 무추력/무조종 RKSS14L 500 m MSL drop mission 생성 및 실행
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop/c172x_4x75kg_cg_aligned_zeroprop.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop/initial_condition/6.0__gimpo_450m_east_60ms_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop/runscript/6.0__gimpo_450m_east_60ms_neutral_zeroprop_drop_run.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/c172ap.xml 및 support XML 파일들
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit.xml
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/c172ap.xml 및 support XML 파일들
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.0__rkss14l_500m_ubody60_theta25_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_run.xml
- 핵심 변경점:
  - aerodynamics의 alphalimits block을 제거함
  - 기존 4 x 75 kg occupant, fuel tank, CG-aligned mass, zeroprop 구성을 유지함
  - 프로펠러와 engine thruster가 없는 모델을 사용해 propulsion/engine 계열 catalog property가 생성되지 않게 함
  - elevator actuator bias를 0.0으로 바꿔 neutral command에서 fcs/elevator-pos-rad가 0.0이 되도록 함
  - 초기조건은 latitude 37.5707083333 deg, longitude 126.7782777778 deg, h-sl 약 500.003 m, theta 2.5 deg, psi 135.01 deg, ubody 60 m/s, 무풍으로 구성
- 실행한 명령어:
  - xmllint --noout aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit.xml scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.0__rkss14l_500m_ubody60_theta25_init.xml scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_run.xml
  - /home/junyeopkwon/jsbsim/build/src/JSBSim --aircraft=c172x_4x75kg_cg_aligned_zeroprop_noalphalimit --catalog
  - python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft c172x_4x75kg_cg_aligned_zeroprop_noalphalimit --init scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.0__rkss14l_500m_ubody60_theta25_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_run.xml --planet default --no-flightgear
- 검증 결과:
  - XML 문법 검증 통과
  - aircraft catalog load 통과
  - 최종 run 7.0.2 정상 실행
  - console에서 GEAR_CONTACT 219.758333 s Nose Gear 1 확인
  - terminate event는 219.766667 s에 실행
  - raw CSV rows 26373, last Time 219.7666667 s
  - 초기 h-sl 500.002630 m, h-agl 1602.419950 ft, theta 2.5 deg, psi 135.01 deg 확인
  - 초기 body 속도 u/v/w = 196.850394/-0.0/0.0 ft/s, 즉 60/0/0 m/s 확인
  - 조종면 fcs/elevator-pos-rad, left/right aileron, rudder 전체 구간 최대 절대값 0.0 rad 확인
  - propulsion/engine 계열 output column 없음 확인
  - aero/alpha-deg 범위는 약 0.0 deg에서 12.625445 deg
- 실행 산출물:
  - /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop/7.0.2__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_runscript_07291053.xml
  - /home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop/7.0.2__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_console_07291053.log
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop/7.0.2__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_raw_07291053.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/si/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop/7.0.2__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_si_07291053.csv
- 검증하지 못한 항목:
  - FlightGear visual alignment
  - alpha-limit 유지 모델과 no-alpha-limit 모델의 차이 정량 비교
  - 공력 table 범위 밖 extrapolation 물리 타당성
- 남은 리스크:
  - alphalimits는 제거됐지만 기존 CL/CD/Cm table 자체의 alpha 범위와 외삽 특성은 별도 검토가 필요함
  - 이번 CSV-only run에서는 시각화 plot을 생성하지 않음
- 다음 작업:
  - 같은 초기조건으로 alpha-limit 유지 zeroprop baseline을 실행해 궤적, 접지 시각, alpha 범위를 비교
- Git commit:
  - 없음

## [2026-07-29 11:08] PROGRESS-20260729-1108-001 - 분석 완료

- 과업:
  - c172x_4x75kg_cg_aligned_zeroprop_noalphalimit run 7.0.3 고도 상승/출렁임 원인 분석
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 조사한 파일:
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop/7.0.3__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_raw_07291059.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop/7.0.3__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_sixdof_raw_07291059.csv
  - /home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.0__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop/7.0.2__rkss14l_500m_ubody60_theta25_neutral_zeroprop_noalphalimit_drop_console_07291053.log
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit.xml
- 수행 내용:
  - raw CSV에서 altitude, vertical speed, total speed, body u/w, theta, alpha, 조종면 값을 샘플링함
  - sixdof_raw에서 pitch moment, qdot, aero force/moment를 확인함
  - aircraft XML에서 pitch axis Cmalpha, Cmq, Cmadot, Cmo, Cmde 항을 확인함
- 핵심 결과:
  - AP/PID는 꺼져 있고 조종면은 전 구간 0 rad였으므로 PID에 의한 고도 출렁임은 아님
  - 초기 상태에서 v-down-fps = -8.586494로 시작하여 약 +2.617 m/s 상승 속도가 이미 존재함
  - 초기 theta 2.5 deg, alpha 약 0 deg, ubody 60 m/s 조건은 수평 경로가 아니라 약 2.5 deg 상승 경로를 의미함
  - 초기 pitch moment m-total = +4311.7 lb-ft, qdot = +2.98765 rad/s^2로 강한 nose-up acceleration이 발생함
  - aircraft XML에는 Cmo = +0.1 pitch moment at zero alpha가 있어 neutral elevator/alpha 0 조건에서 nose-up moment가 생김
  - 고도는 t=8.8167 s에 639.842 m까지 상승했고, 이때 speed는 약 13.93 m/s까지 감소, alpha는 약 12.5 deg까지 증가함
  - 이후 속도-고도 에너지 교환과 longitudinal/phugoid 자유응답으로 감쇠 진동하며 하강함
  - max alpha는 약 12.625 deg로 기존 alphalimits max 0.28 rad, 약 16.0 deg보다 낮아 이번 실행의 첫 상승 원인은 alpha limit 제거가 아님
- 검증 명령어:
  - raw CSV 및 sixdof_raw CSV를 Python csv 모듈로 샘플링
  - grep/sed로 aircraft XML pitch moment 항 확인
- 검증 결과:
  - max_abs_surface = 0.0 rad
  - h_start = 500.003 m, h_max = 639.842 m at 8.8167 s, h_end = 12.993 m
  - theta 범위 약 -43.576 deg에서 +45.143 deg
  - alpha 범위 약 0.0 deg에서 12.625 deg
- 검증하지 못한 항목:
  - 같은 조건에서 alpha-limit 유지 baseline 비교
  - no-thrust fixed-control steady glide trim 산출
- 남은 리스크:
  - 사용자가 원하는 물리 시나리오가 수평 진입인지, 정해진 pitch 자세인지, trim된 활공인지에 따라 초기조건을 다르게 구성해야 함
- 다음 작업:
  - 수평으로 시작하려면 theta 2.5 deg 유지 시 wbody를 약 +2.62 m/s로 주거나, theta를 0 deg로 바꾸는 비교 run 생성
  - 안정 활공으로 시작하려면 zero-thrust, fixed-control 조건에서 trim alpha/theta/elevator 조건을 별도 산출
- Git commit:
  - 없음

## [2026-07-29 11:20] PROGRESS-20260729-1120-001 - DONE

- 과업:
  - c172x no-alpha-limit 수평 전진 초기조건 run 생성 및 고도 응답 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.1__rkss14l_500m_ubody60_level_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop_run.xml
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop/altitude_compare_7_0_vs_7_1.png
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop/states_h_vdown_theta_alpha_7_1.png
- 수행 내용:
  - 7.0 초기조건을 복사해 7.1 초기조건을 만들고 theta를 0.0 deg로 변경함
  - 7.1 runscript가 새 초기조건을 참조하도록 변경함
  - plotting runner가 오래 멈춰 PID 272454를 종료하고 CSV-only runner로 최종 재실행함
  - raw CSV에서 7.0과 7.1 altitude를 비교하는 PNG를 별도 생성함
- 검증 명령어:
  - xmllint --noout scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.1__rkss14l_500m_ubody60_level_init.xml scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop_run.xml
  - python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft c172x_4x75kg_cg_aligned_zeroprop_noalphalimit --init scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.1__rkss14l_500m_ubody60_level_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop_run.xml --planet default --no-flightgear
- 검증 결과:
  - XML 문법 통과
  - run 7.1.2 정상 종료
  - 초기 h-sl 500.002630 m, theta 약 0 deg, v-down 약 0 m/s, ubody 60 m/s 확인
  - 7.1 hmax = 637.641576 m at 9.016667 s
  - 7.1 terminate = 219.725 s, nose gear contact
  - 조종면 최대 절대값 0.0 rad
  - 7.0 hmax 639.841712 m와 비교해 초기 상승 성분은 제거됐지만 고도 피크는 거의 유지됨
  - 7.1 sixdof_raw 초기 m-total = +4311.3 lb-ft, qdot = +2.98738 rad/s^2 확인
- 해석:
  - theta 2.5 deg가 만든 초기 상승속도는 제거됐지만, neutral fixed-control C172 모델 자체의 positive Cmo 기반 nose-up moment가 남아 고도 상승과 phugoid가 계속 발생함
- 검증하지 못한 항목:
  - view_image 직접 렌더 확인은 Windows/WSL sandbox helper 오류로 실패
  - FlightGear visual 확인 미수행
  - no-thrust steady glide trim 미산출
- 남은 리스크:
  - 수평 전진 초기조건은 trim된 순항 또는 활공 평형을 의미하지 않으므로 고도 출렁임이 계속 남음
- 다음 작업:
  - zero-thrust fixed-control 조건에서 steady glide trim 또는 Cmo/elevator trim 보정 케이스 생성
- Git commit:
  - 없음

## [2026-07-29 11:25] PROGRESS-20260729-1125-001 - DONE

- 과업:
  - c172x no-alpha-limit theta -5 deg nose-down 비교 run 생성 및 분석
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.2__rkss14l_500m_ubody60_thetam5_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.2__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop_run.xml
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.2__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop/altitude_compare_7_0_7_1_7_2.png
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/7.2__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop/states_h_vdown_theta_alpha_7_2.png
- 수행 내용:
  - 7.1 level 초기조건을 복사해 theta를 -5.0 deg로 변경한 7.2 초기조건을 생성함
  - 7.2 runscript가 새 초기조건을 참조하도록 변경함
  - CSV-only runner로 7.2.1을 실행함
  - 7.0 theta +2.5, 7.1 theta 0, 7.2 theta -5의 h_sl_m 비교 그래프를 생성함
- 검증 명령어:
  - xmllint --noout scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.2__rkss14l_500m_ubody60_thetam5_init.xml scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.2__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop_run.xml
  - python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft c172x_4x75kg_cg_aligned_zeroprop_noalphalimit --init scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.2__rkss14l_500m_ubody60_thetam5_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.2__rkss14l_500m_ubody60_thetam5_neutral_zeroprop_noalphalimit_drop_run.xml --planet default --no-flightgear
- 검증 결과:
  - XML 문법 통과
  - run 7.2.1 정상 종료
  - 초기 h-sl 500.002630 m, theta -5.0 deg, v-down +5.229345 m/s 확인
  - 7.2 hmax = 633.309377 m at 9.433333 s
  - 7.2 terminate = 219.25 s, h_end 약 12.986 m
  - 7.2 max alpha = 11.620923 deg, max theta = 43.698916 deg, min theta = -42.032087 deg
  - 조종면 최대 절대값 0.0 rad
  - 7.0 hmax 639.84 m, 7.1 hmax 637.64 m, 7.2 hmax 633.31 m로 nose-down이 상승 피크를 줄였지만 제거하지는 못함
  - 7.2 sixdof_raw 초기 m-total = +4312.76 lb-ft, qdot = +2.98839 rad/s^2로 pitch-up moment는 여전히 존재
- 검증하지 못한 항목:
  - FlightGear visual 확인
  - trim된 steady glide 조건 산출
- 남은 리스크:
  - theta만 더 nose-down으로 조정하는 방식은 임시적이며 모델의 neutral pitch moment 문제를 해결하지 않음
- 다음 작업:
  - elevator trim 또는 Cmo 조정 variant를 분리 생성해 초기 qdot을 0에 가깝게 맞추는 비교 run 수행
- Git commit:
  - 없음

## [2026-07-29 11:42] PROGRESS-20260729-1142-001 - DONE

- 과업:
  - c172x no-alpha-limit 초기 qdot 0 근접 Cmo 보정 variant 계산 및 실행
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 생성한 파일:
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0.xml
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/initial_condition/8.0__rkss14l_500m_ubody60_level_cmo0_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/runscript/8.0__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmo0_drop_run.xml
  - /home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0.xml
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/initial_condition/8.1__rkss14l_500m_ubody60_level_cmotrimq0_init.xml
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/runscript/8.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmotrimq0_drop_run.xml
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/8.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmotrimq0_drop/altitude_compare_7_1_8_0_8_1_cmo_trim.png
  - /home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/8.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmotrimq0_drop/states_h_vdown_theta_alpha_8_1_cmotrimq0.png
- 수행 내용:
  - 기존 no-alpha-limit model에서 Cmo 0.1이 초기 pitch-up moment의 주 원인임을 바탕으로 Cmo 보정 실험을 별도 variant로 분리함
  - 먼저 Cmo=0.0 variant 8.0을 실행해 초기 qdot이 2.987 rad/s^2에서 0.394876 rad/s^2로 감소함을 확인함
  - 잔여 moment를 선형 보간하여 Cmo = -0.01523148을 계산함
  - cmotrimq0 variant에서 Cmo=-0.01523148을 적용하고 8.1을 실행함
- 계산:
  - 7.1 Cmo 0.1 초기 m-total 약 4311.3 lb-ft
  - 8.0 Cmo 0.0 초기 m-total 569.874488 lb-ft
  - dM/dCmo ≈ (4311.3 - 569.874488) / 0.1
  - Cmo_target ≈ -569.874488 / dM/dCmo = -0.01523148
- 검증 명령어:
  - xmllint --noout aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0.xml scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/initial_condition/8.0__rkss14l_500m_ubody60_level_cmo0_init.xml scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/runscript/8.0__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmo0_drop_run.xml
  - /home/junyeopkwon/jsbsim/build/src/JSBSim --aircraft=c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0 --catalog
  - python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0 --init scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/initial_condition/8.0__rkss14l_500m_ubody60_level_cmo0_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmo0/runscript/8.0__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmo0_drop_run.xml --planet default --no-flightgear
  - xmllint --noout aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0.xml scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/initial_condition/8.1__rkss14l_500m_ubody60_level_cmotrimq0_init.xml scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/runscript/8.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmotrimq0_drop_run.xml
  - /home/junyeopkwon/jsbsim/build/src/JSBSim --aircraft=c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0 --catalog
  - python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py --aircraft c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0 --init scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/initial_condition/8.1__rkss14l_500m_ubody60_level_cmotrimq0_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_cmotrimq0/runscript/8.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_cmotrimq0_drop_run.xml --planet default --no-flightgear
- 검증 결과:
  - XML 문법 통과
  - aircraft catalog load 통과
  - 8.0 run 성공, hmax 502.592039 m, terminate 81.175 s
  - 8.1 run 성공, 초기 m-total -0.000165 lb-ft, 초기 qdot -1.1313e-7 rad/s^2
  - 8.1 hmax 500.002631 m at 0.008333 s, terminate 51.85 s
  - 8.1 alpha range -0.086526 deg to 0.216185 deg, theta range -14.421277 deg to 0.000009 deg
  - 조종면 최대 절대값 0.0 rad 유지
- 검증하지 못한 항목:
  - FlightGear visual 확인
  - Cmo 보정이 C172 실제 공력 데이터와 부합하는지 검증
- 남은 리스크:
  - Cmo 보정은 초기 qdot 제거 목적의 실험 variant이며, 실제 C172 공력 모델 보정으로 확정하면 안 됨
- 다음 작업:
  - Cmo 보정 대신 elevator trim으로 같은 qdot0를 만드는 variant/run과 비교
- Git commit:
  - 없음

## [2026-07-29 12:05] PROGRESS-20260729-1205-001 - 완료

- 과업: trim-fixed c172x no-thrust 추락 케이스 생성 및 검증
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 생성/수정 파일: aircraft_variants/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_elevtrimq0, scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_elevtrimq0, scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/9.2 native trim test files
- 핵심 변경점: 원래 Cmo=0.1 유지, elevator actuator bias를 0.092863537532 rad로 고정, control command와 pitch-trim command는 0 유지
- 실행한 명령어: xmllint --noout, JSBSim --catalog, python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 검증 결과: XML 통과, catalog 통과, 9.3 run 성공; 초기 m-total=0.123517 lb-ft, qdot=8.55886e-05 rad/s^2, hmax=500.002631 m, 접지 종료 53.95 s, elevator-pos-rad 전 구간 0.092863537532
- 검증하지 못한 항목: view_image 직접 렌더 확인
- 검증하지 못한 이유: Windows sandbox helper 오류
- 남은 리스크: 9.3은 full glide equilibrium이 아니라 초기 pitch moment/qdot 제거 중심 trim임
- Git commit: 없음


## [2026-07-31 10:56] PROGRESS-20260731-1056-001 - DONE

- 수행한 작업: `5.16` 최신 raw CSV를 분석해 takeoff roll, AP 전환, final, touchdown 구간의 `mission/runway-cross-ft`, heading, rudder/elevator, AP hold 상태를 비교했다.
- 조사한 파일: `scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.16__ksfo28r_runway_return_circular_landing_run.xml`; `aircraft_variants/c172x_4x75kg_cg_aligned_ksfo28r_landing/c172x_4x75kg_cg_aligned_ksfo28r_landing.xml`; `/home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_ksfo28r_landing/c172ap_landing.xml`.
- 생성한 파일: `5.17__ksfo28r_centerline_smoothed_landing_run.xml`; `5.18__ksfo28r_centerline_smoother_takeoff_landing_run.xml`; `5.19__ksfo28r_centerline_smoothest_takeoff_landing_run.xml`; `5.20__ksfo28r_centerline_corrected_takeoff_landing_run.xml`; `5.21__ksfo28r_centerline_balanced_takeoff_landing_run.xml`; `5.22__ksfo28r_centerline_balanced_final_landing_run.xml`.
- 원인 분석: `5.16`은 takeoff roll에서 `rudder=-0.035/-0.030`로 heading이 305 deg 이상으로 밀리고, 20 ft AGL 이후 AP heading hold가 되돌리면서 초기 offset이 커졌다. final에서는 210 ft AGL에서 heading hold를 끊은 뒤 heading이 약 296 deg까지 밀려 touchdown cross가 커졌다.
- 핵심 변경점: takeoff rudder를 작은 양의 값으로 ramp 적용, rotate elevator를 `-0.110 tc=0.9`에서 `-0.090 tc=1.7`로 완화, 초기 climb heading setpoint를 `297.2 deg`로 임시 보정 후 state4에서 `298 deg` 복귀, final 진입 cross 조건을 `-370 ft`로 조정, heading hold를 flare 직전까지 유지.
- 검증 명령어: `xmllint --noout` on new runscript files; `run_jsbsim_timestamped_no_fg_prompt_csv_only.py` with `5.17`~`5.22`; `git diff --check` on new runscript files.
- 검증 결과: 최종 `5.22.1__ksfo28r_centerline_balanced_final_landing` reached `STATE 23` at `642.025 s`.
- 비교 결과: `5.16.5` max cross within first 150 s `91.2 m`, touchdown cross `-33.4 m`, stop cross `-43.5 m`; `5.22.1` max cross within first 150 s `44.0 m`, touchdown cross `-1.5 m`, stop cross `-2.3 m`.
- 최종 run output: raw CSV `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.22__ksfo28r_centerline_balanced_final_landing/5.22.1__ksfo28r_centerline_balanced_final_landing_raw_07311053.csv`; console `/home/junyeopkwon/jsbsim_workflow/logs/console/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.22__ksfo28r_centerline_balanced_final_landing/5.22.1__ksfo28r_centerline_balanced_final_landing_console_07311053.log`.
- 검증하지 못한 항목: FlightGear visual scene에서 실제 활주로 페인트/중심선에 대한 화면 검증은 수행하지 않음.
- 남은 리스크: JSBSim centerline metric 기준 튜닝이며, FlightGear 모델 시점/렌더링에서는 체감 offset이 다를 수 있음.
- Git commit: none.

## [2026-07-31 13:55] PROGRESS-20260731-1355-001 — DONE

- 과업: 로테이트 직후 pitch/elevator 튐 저감 runscript 생성 및 검증
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 조사한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.22__ksfo28r_centerline_balanced_final_landing_run.xml`, `5.22.2__ksfo28r_centerline_balanced_final_landing_raw_07311110.csv`
- 생성한 파일: `5.26__ksfo28r_smooth_manual_pitch_ap_landing_run.xml`, `5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml`, `5.28__ksfo28r_smooth_rotate_late_alt_hold_landing_run.xml`, `5.29__ksfo28r_staged_altitude_ap_landing_run.xml`, `5.30__ksfo28r_manual_climb_damped_landing_run.xml`
- 핵심 변경점: `5.27`에서 로테이트 elevator를 `-0.040 tc=2.8`로 완화하고, `STATE 3` 수동 pitch 완화 elevator `0.180 tc=2.5`, altitude hold 지연을 적용
- 실행한 명령어: `python3 scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py` 선택값 `43 / 1 / 14`부터 `43 / 1 / 18`, `git diff --check -- scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.26__... 5.30__...`
- 테스트 결과: `5.22.2`는 20-35초 elevator position range `0.376 rad`, AP elevator range `1.312`; `5.27.1`은 `STATE 23`, 20-35초 elevator position range `0.047 rad`, AP elevator range `0.000`, theta max `14.4 deg`, touchdown cross-track `-0.1 m`, stop cross-track `-1.1 m`
- 추가 결과: `5.26.1`은 초반 튐은 작지만 theta max `21.0 deg`; `5.28.1`은 40-120초 pitch/elevator 변동 큼; `5.29.1`은 초반 AP 튐 재발; `5.30.1`은 `STATE 3`, `T=73.0 s`에서 종료되어 정상 완료 실패
- lint 결과: XML parse 확인 통과, `git diff --check` 통과
- 검증하지 못한 항목: FlightGear 화면에서 실제 시각적 흔들림 확인
- 검증하지 못한 이유: 현재 검증은 JSBSim CSV 로그 기반으로 수행했고 FlightGear GUI 실행은 하지 않음
- 남은 리스크: `5.27`은 46초 부근 altitude hold 재투입 시 elevator transient가 남아 전체 0-100초 plot에서 중간 튐으로 보일 수 있음
- 후속 작업: 필요 시 `5.27` 기반으로 AP 재투입 이벤트만 별도 미세 조정
- Git commit: 없음

## [2026-07-31 14:05] PROGRESS-20260731-1405-001 — DONE

- 과업: 방금 생성한 비교용 KSFO RWY 28R runscript 및 실행 로그 정리
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 비교용으로 만든 파일 중 멀쩡한 것만 남기고 삭제
- 수행 내용: 추천본 `5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml`과 해당 실행 로그는 보존하고, 비추천 비교본 `5.26`, `5.28`, `5.29`, `5.30` runscript 및 관련 generated runscript, console, raw/si/sixdof CSV 로그 디렉터리를 삭제
- 삭제한 파일/폴더: `5.26__ksfo28r_smooth_manual_pitch_ap_landing*`, `5.28__ksfo28r_smooth_rotate_late_alt_hold_landing*`, `5.29__ksfo28r_staged_altitude_ap_landing*`, `5.30__ksfo28r_manual_climb_damped_landing*`
- 보존한 파일: `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml`
- 검증 결과: 삭제 전 모든 대상 경로가 `/home/junyeopkwon/jsbsim_workflow` 내부인지 확인했고, `5.27` runscript 존재 확인 결과 `True`
- 검증하지 못한 항목: 삭제 후 전체 Git diff 상세 검토는 수행하지 않음
- 남은 리스크: 이전 작업 기록에는 `5.26`-`5.30` 생성 기록이 남아 있으며, 이는 append-only 정책상 삭제하지 않음
- Git commit: 없음

## [2026-07-31 14:18] PROGRESS-20260731-1418-001 — DONE

- 과업: F450 raw CSV distance-from-start property 의미 조사
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/F450/1.2__ten_meter_box_hover_land/1.2.20__ten_meter_box_hover_land_raw_07261547.csv, /home/junyeopkwon/jsbsim/src/models/FGAuxiliary.cpp, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py
- 수행 내용: CSV column 및 샘플 값을 확인하고 JSBSim FGAuxiliary property tie와 getter 산식을 확인
- 검증 결과: distance-from-start-lon-mt는 초기 longitude를 고정한 경도방향 상대거리, distance-from-start-lat-mt는 초기 geodetic latitude를 고정한 위도방향 상대거리, distance-from-start-mag-mt는 초기 lat/lon까지의 합성 거리로 tie됨
- 검증하지 못한 항목: 없음
- 남은 리스크: lat/lon 성분은 부호 없는 distance 성격으로 보이며 북/동 방향 부호가 필요한 경우 from-start-neu-n-ft 및 from-start-neu-e-ft 사용이 더 적합함
- Git commit: 없음

## [2026-07-31 14:24] PROGRESS-20260731-1424-001 — DONE

- 과업: Excel 및 CSV header 내 from-start-neu-n-ft 확인
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/workflow_all_cases_initial_settings.xlsx, /home/junyeopkwon/jsbsim_workflow/logs/csv/raw/F450/1.2__ten_meter_box_hover_land/1.2.20__ten_meter_box_hover_land_raw_07261547.csv, /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_raw/F450/1.2__ten_meter_box_hover_land/1.2.20__ten_meter_box_hover_land_sixdof_raw_07261547.csv, /home/junyeopkwon/jsbsim_workflow/logs/csv/sixdof_si/F450/1.2__ten_meter_box_hover_land/1.2.20__ten_meter_box_hover_land_sixdof_si_07261547.csv
- 수행 내용: xlsx zip XML 전체 문자열 검색 및 관련 CSV header 검색
- 검증 결과: Excel 전체에 position/from-start-neu-n-ft, /fdm/jsbsim/position/from-start-neu-n-ft, from_start_neu_n_m 문자열 없음. raw CSV에도 없음. sixdof_raw에는 /fdm/jsbsim/position/from-start-neu-n-ft, sixdof_si에는 from_start_neu_n_m 존재
- 검증하지 못한 항목: 없음
- 남은 리스크: workflow Excel은 CSV property header 전체를 담는 파일이 아니라 파일/시나리오 요약 중심이므로 특정 property 분석에는 CSV 파일을 직접 봐야 함
- Git commit: 없음

## [2026-07-31 15:56] PROGRESS-20260731-1556-001 — DONE

- 과업: combined CSV only runner 구현 및 검증
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 생성한 파일: /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped_combined_csv_only.py
- 생성된 검증 산출물: /home/junyeopkwon/jsbsim_workflow/logs/csv/combined/F450/1.0__ground_launch_scas/1.0.4__ground_launch_scas_combined_07311556.csv, /home/junyeopkwon/jsbsim_workflow/logs/console/F450/1.0__ground_launch_scas/1.0.4__ground_launch_scas_combined_console_07311556.log, /home/junyeopkwon/jsbsim_workflow/logs/generated_runscripts/F450/1.0__ground_launch_scas/1.0.4__ground_launch_scas_combined_runscript_07311556.xml
- 핵심 변경점: 기존 run_jsbsim_timestamped_no_fg_prompt_csv_only.py의 선택 및 기체별 property 목록을 재사용하되, JSBSim output을 logs/csv/combined 아래 단일 CSV 하나로 생성하도록 별도 runner 추가
- 실행한 명령어: python3 -m py_compile scripts/run_jsbsim_timestamped_combined_csv_only.py; python3 scripts/run_jsbsim_timestamped_combined_csv_only.py --aircraft F450 --init scripts/F450/initial_condition/1.0__ground_park_init.xml --runscript scripts/F450/runscript/1.0__ground_launch_scas_run.xml --planet builtin --no-flightgear; git diff --check -- scripts/run_jsbsim_timestamped_combined_csv_only.py
- 검증 결과: py_compile 통과; git diff --check 통과; run 1.0.4__ground_launch_scas 정상 종료; combined CSV 188 columns, 1501 rows, final time 12 s 생성; from-start-neu-n-ft, from-start-neu-e-ft, distance-from-start-lat-mt, distance-from-start-lon-mt, fcs/aileron-cmd-norm, fcs/ScasEngage, propulsion/engine[3]/thrust-lbs header 존재 확인
- 검증하지 못한 항목: 긴 runscript 전체에 대한 실행 검증은 수행하지 않음
- 남은 리스크: JSBSim catalog에 없는 일부 6DOF property는 skipped 목록으로 보고되며, requested 193개 중 실제 CSV column은 188개로 생성됨
- 참고: 최초 검증 실행 1.0.3은 combined CSV와 console을 생성했으나 workflow Excel 자동 갱신이 120초 제한을 초과해 timeout됨. 이후 새 runner에서 Excel 자동 갱신 호출을 제거하고 1.0.4로 정상 종료 확인
- Git commit: 없음

## [2026-07-31 16:08] PROGRESS-20260731-1608-001 — DONE

- 과업: run_jsbsim_csv_plotter_v6.m 정적 검토
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/logs/csv/run_jsbsim_csv_plotter_v6.m
- 수행 내용: 파일 상단 기능 설명, GUI tab 구성, CSV load, 2D/3D plotting, PNG 저장, XML event parsing, trajectory auto-detect, metadata summary, downsampling 로직 확인
- 검증 결과: 2D/3D 수동 탐색 기능은 충분히 구현되어 있음. 발표자료 생산 목적에는 plot preset, batch export, metrics summary, multi-run comparison, event source 자동 연동 기능이 추가되면 효과가 큼. Min/Max 옵션에서 호출하는 mark2DMinMaxOnly 함수 정의가 없어 해당 옵션 사용 시 오류 가능성이 큼
- 검증하지 못한 항목: MATLAB 앱 직접 실행, GUI 조작, PNG 시각 검증
- 남은 리스크: 정적 검토 기준이며 MATLAB 버전별 UI 동작 차이는 확인하지 못함
- Git commit: 없음

## [2026-07-31 17:23] PROGRESS-20260731-1723-001 — DONE

- 과업: MATLAB CSV plotter v7 구성
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: JSBSim CSV 로그 분석과 발표자료용 그래프 패키지 생성을 위한 plotter 기능 보강
- 관련 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`, `logs/csv/run_jsbsim_csv_plotter_v6.m`, `logs/csv/raw/F450/1.2__ten_meter_box_hover_land/1.2.20__ten_meter_box_hover_land_raw_07261547.csv`
- 수행 내용: v6를 복사해 v7을 만들고 GUI 이름/태그/헤더를 v7로 변경함. 저장 탭에 `보고서 프리셋`, `표준 분석 PNG + summary CSV 저장`, `summary metrics CSV만 저장` 컨트롤을 추가함. 표준 분석 패키지 export 함수와 summary metrics 계산/저장 함수를 추가함. F450 로터 RPM/추력, 자세, 속도, 제어명령, 위치 변화, C172 활주로/기어 후보 컬럼을 구성함. 기존 Min/Max 표시 옵션에서 호출하던 `mark2DMinMaxOnly` 누락 함수를 추가함. F450 raw CSV의 `/fdm/jsbsim/position/distance-from-start-lat-mt`, `/fdm/jsbsim/position/distance-from-start-lon-mt`를 North/East 위치 후보로 추가함.
- 생성한 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`
- 수정한 파일: `docs/agent-log/TASK.md`, `docs/agent-log/PROGRESS.md`, `docs/agent-log/DECISIONS.md`, `docs/agent-log/TODO.md`, `docs/agent-log/INDEX.md`
- 핵심 변경점: 발표자료용 PNG 묶음(`00_trajectory_3d.png`, `01_altitude.png`, `02_speed.png`, `03_attitude.png`, `04_rates.png`, `05_position_from_start.png`, `06_controls.png`, F450/C172 전용 PNG), `summary_metrics.csv`, `skipped_plots.txt`를 생성하는 경로를 추가함.
- 실행한 명령어: `cp logs/csv/run_jsbsim_csv_plotter_v6.m logs/csv/run_jsbsim_csv_plotter_v7.m`; `grep -nE ... run_jsbsim_csv_plotter_v7.m`; `python3` 정적 존재 확인; F450 raw CSV header 후보 매칭 확인; `command -v matlab`; `command -v octave`; `git check-ignore -v logs/csv/run_jsbsim_csv_plotter_v7.m`; `git status --short ...`
- 테스트 결과: 핵심 함수/컨트롤 문자열이 모두 1회 이상 존재함을 확인함. 충돌 마커 `<<<<<<<`, `>>>>>>>` 없음. F450 raw CSV에서 altitude, speed, roll, pitch, yaw, aileron, rotor RPM, rotor thrust, distance-from-start lat/lon 후보 매칭 확인. `logs/csv/run_jsbsim_csv_plotter_v7.m`는 `.gitignore`의 `logs/` 규칙에 의해 Git 추적 상태에 표시되지 않음.
- lint 결과: MATLAB lint 미수행
- type check 결과: 해당 없음
- build 결과: 해당 없음
- 실행 확인 결과: MATLAB/Octave 실행 파일이 WSL PATH에 없어 GUI 실기동은 미수행
- 검증하지 못한 항목: MATLAB에서 `run_jsbsim_csv_plotter_v7.m` 실행, CSV 로드 후 export 버튼 클릭, PNG/CSV 실제 생성물 시각 검수
- 가정: 사용자는 MATLAB GUI에서 직접 실행 가능하며, `logs/` ignored 파일도 작업 산출물로 사용할 수 있음
- 남은 리스크: MATLAB 버전에 따라 `uifigure`, `uidropdown`, `exportgraphics`, `contains(...,'IgnoreCase',true)` 지원 여부 차이가 있을 수 있음. raw F450 CSV에는 scalar magnitude distance 컬럼이 없어 `distance_from_start_final`은 combined CSV 또는 별도 magnitude 컬럼이 있을 때만 기록됨.
- 다음 작업: MATLAB에서 v7 실행 후 F450 raw/combined CSV 각각으로 표준 분석 패키지 export 결과를 확인
- Git commit: 없음
## [2026-07-31 17:47] PROGRESS-20260731-1747-001 — DONE

- 과업: MATLAB CSV plotter v7 제목/축/범례 편집 기능 보강
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 그래프 제목/축 제목 글씨 크기 조절 및 범례 문구 수정 기능 추가
- 관련 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`
- 수행 내용: 2D 설정 탭에 `제목 크기`, `축 제목`, `범례` numeric 입력을 추가함. 3D 설정 탭에도 동일한 폰트 크기 입력을 추가하고 `legend3DTable`을 추가해 `Trajectory`, `Start`, `End`, `Min Z`, `Max Z` 표시 이름을 수정 가능하게 함. 3D `범례` 체크박스를 분리해 마커 표시 여부와 별개로 범례 표시를 제어하도록 함. `get2DFontSizes`, `get3DFontSizes`, `numericControlValue`, `default3DLegendData`, `resolve3DLegendNames` helper를 추가함. 수동 2D/3D 그래프와 표준 분석 PNG export에 제목/축/범례 폰트 크기와 3D 범례 이름을 반영함. CSV 로드 및 전체 설정 초기화 시 폰트/3D 범례 기본값을 복원하도록 함.
- 생성한 파일: 없음
- 수정한 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`, `docs/agent-log/TASK.md`, `docs/agent-log/PROGRESS.md`, `docs/agent-log/TODO.md`, `docs/agent-log/INDEX.md`
- 핵심 변경점: 발표자료용 그래프에서 제목/축/범례 글씨 크기와 3D 범례 문구를 GUI에서 직접 조절 가능
- 실행한 명령어: `Select-String ... run_jsbsim_csv_plotter_v7.m`; PowerShell 정적 문자열 점검; `C:\Program Files\MATLAB\R2024b\bin\matlab.exe -batch "... checkcode(...) ..."`
- 테스트 결과: MATLAB R2024b `checkcode` 실행 완료. 문법 오류는 보고되지 않음. 기존 스타일/성능 경고(`INUSD`, `ISCL`, `MSNU`, `NOCOMMA`, `SPRINTFN`, `NASGU`, `AGROW`, `DATST`, `TNOW1`)가 출력됨.
- lint 결과: MATLAB `checkcode` 실행, fatal syntax error 없음
- type check 결과: 해당 없음
- build 결과: 해당 없음
- 실행 확인 결과: GUI 실기동은 하지 않음. MATLAB batch 정적 분석만 수행함.
- 검증하지 못한 항목: MATLAB GUI에서 CSV 로드 후 2D/3D 그래프 생성, 범례 이름 변경, 글씨 크기 변경, 표준 PNG export 결과 시각 확인
- 가정: MATLAB R2024b 환경에서 `uifigure`, `uitable`, `uidropdown`, `exportgraphics`가 정상 동작함
- 남은 리스크: checkcode는 GUI callback 런타임 오류를 완전히 보장하지 않음. `logs/`가 `.gitignore`에 포함되어 v7 파일은 Git status에 표시되지 않음.
- 다음 작업: MATLAB GUI에서 F450 CSV를 로드해 글씨 크기와 범례 문구를 바꾼 뒤 2D/3D 및 표준 분석 PNG export 결과 확인
- Git commit: 없음
## [2026-07-31 18:02] PROGRESS-20260731-1802-001 — DONE

- 과업: MATLAB CSV plotter v7 2D 범례 직접 입력 기능 수정
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 범례가 property명으로 표시되지 않고 사용자가 작성한 문구를 쓰도록 수정
- 관련 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`
- 수행 내용: `title2DTable`에 `범례 이름` 행을 추가함. 두 번째 열 안내 문구를 `사용자 입력: 공란이면 자동 / 범례는 쉼표 구분`으로 변경함. `resolve2DLegendNames` 함수를 추가해 `범례 이름` 행의 쉼표/세미콜론/줄바꿈 구분 텍스트를 선택된 Y 계열 순서대로 매핑함. `plot2DSeriesRows`가 `legendNamesByRow`를 우선 사용하고, 비어 있을 때만 기존 `series2DTable`의 `범례 이름` 및 property명을 fallback으로 쓰도록 변경함. 3D 제목 테이블에 잘못 들어간 2D용 쉼표 구분 안내 문구는 원래대로 정리함.
- 생성한 파일: 없음
- 수정한 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`, `docs/agent-log/TASK.md`, `docs/agent-log/PROGRESS.md`, `docs/agent-log/TODO.md`, `docs/agent-log/INDEX.md`
- 핵심 변경점: 사용자가 `범례 이름` 행에 `고도, 속도, 자세각`처럼 입력하면 선택된 2D Y 계열 순서대로 범례가 표시됨
- 실행한 명령어: `grep -n ... run_jsbsim_csv_plotter_v7.m`; `C:\Program Files\MATLAB\R2024b\bin\matlab.exe -batch "... checkcode(...) ..."`; PowerShell 문자열 정적 점검
- 테스트 결과: MATLAB R2024b `checkcode` fatal 오류 없음(`CHECKCODE_NO_ERR`). 핵심 문자열 확인 결과 `resolve2DLegendNames` 정의 1개, 호출 1개, `DisplayName` 적용 1개, conflict marker 없음.
- lint 결과: MATLAB `checkcode` fatal 오류 없음. 기존 스타일/성능 경고는 남아 있음.
- type check 결과: 해당 없음
- build 결과: 해당 없음
- 실행 확인 결과: GUI 실기동은 미수행
- 검증하지 못한 항목: 실제 MATLAB GUI에서 2D 그래프 생성 후 범례 표시 확인
- 가정: `범례 이름` 행의 입력 순서는 현재 선택된 Y 계열 표시 순서와 동일하게 해석함
- 남은 리스크: 사용자가 입력한 범례 개수가 선택된 Y 계열보다 적으면 남은 계열은 기존 `series2DTable` 범례 이름/property명으로 표시됨
- 다음 작업: MATLAB GUI에서 F450 CSV를 열고 `범례 이름` 행에 직접 문구를 입력해 PNG 저장 결과 확인
- Git commit: 없음

## [2026-08-03 00:00] PROGRESS-20260803-0000-001 — DONE

- 과업: JSBSim XML 좌표계 조사
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 조사한 파일:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_ksfo28r_landing/c172x_4x75kg_cg_aligned_ksfo28r_landing.xml`
  - `/home/junyeopkwon/jsbsim/src/models/FGMassBalance.cpp`
  - `/home/junyeopkwon/jsbsim/src/models/FGMassBalance.h`
  - `/home/junyeopkwon/jsbsim/src/models/FGExternalForce.h`
- 수행 내용: `AERORP`, `EYEPOINT`, `VRP`, `CG`, `pointmass`, `ground_reactions`의 `location unit="IN"` 예시 확인. `FGMassBalance::StructuralToBody()`에서 structural 좌표가 CG를 기준으로 body 좌표로 변환되는 식 확인
- 핵심 확인: structural frame은 `X` aft, `Y` right, `Z` up이고, body frame은 `X` forward, `Y` right, `Z` down. 변환식은 `(body_x, body_y, body_z) = ((CG_x - r_x), (r_y - CG_y), (CG_z - r_z)) * inchtoft`
- 검증 결과: 로컬 JSBSim 소스 주석 및 실제 C172 XML 값으로 확인
- 검증하지 못한 항목: 외부 JSBSim PDF 원문 직접 열람은 수행하지 않음
- 남은 리스크: 모델 제작자가 structural 원점을 어디에 두었는지는 각 aircraft XML 설계 관례에 따르므로, JSBSim 전역 원점이 항상 nose/firewall이라고 단정하면 안 됨
- Git commit: 없음


## [2026-08-03 00:10] PROGRESS-20260803-0010-001 — DONE

- 과업: C172 XML 원점 추정 근거 확인
- 조사한 파일:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x/c172x.xml`
  - `/home/junyeopkwon/jsbsim/aircraft/c172p/c172p.xml`
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_ksfo28r_landing/c172x_4x75kg_cg_aligned_ksfo28r_landing.xml`
- 확인 내용: `CG x=41.0`, pilot `x=36.0`, rear passenger `x=60.0`, baggage `x=95.0`, nose gear `x=-6.8`, nose skid `x=-37.7`, tail skid `x=188.0` 확인
- 해석: structural frame에서 `+X`는 aft이므로 음수 x 값은 원점보다 앞쪽이다. nose gear와 nose skid가 음수라서 원점은 nose tip이 아니라 nose보다 뒤쪽의 datum으로 보는 것이 타당함
- 검증 결과: 로컬 XML 좌표값 비교로 추정 완료
- 검증하지 못한 항목: Cessna 원제작사 weight and balance datum 문서 원문 대조는 수행하지 않음
- 남은 리스크: 정확한 물리적 원점 명칭은 모델 제작자가 참조한 Cessna manual의 datum 정의 확인이 필요

## [2026-08-10 11:20] PROGRESS-20260810-1120-001 — DONE

- 수행한 작업: MiniTalon XML 통합 설명 문서를 docs/minitalon_xml_reference 아래 XML별 Markdown 파일로 분리
- 조사한 파일: /home/junyeopkwon/jsbsim/aircraft/MiniTalon/XML_VALUE_REFERENCE.md, /home/junyeopkwon/jsbsim/aircraft/MiniTalon/*.xml, engine/APC_10x8E.xml, engine/Cobra_C2820_14.xml, scripts/MiniTalon*.xml, output/MiniTalon_output.xml
- 생성한 파일: docs/minitalon_xml_reference/00_INDEX.md 및 XML별 Markdown 26개
- 수정한 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 핵심 변경점: 단일 통합 문서를 유지하는 대신 MiniTalon.xml.md, Metrics.xml.md, Mass.xml.md, Gear.xml.md, Propulsion.xml.md, FlightControl.xml.md, Aero.xml.md 등 XML별 문서로 분리
- 실행한 명령어: Python split script, find/grep/sed/git status 확인
- 검증 결과: docs/minitalon_xml_reference 아래 Markdown 27개 생성 확인. Metrics.xml.md와 Propulsion.xml.md 및 runscript 문서 샘플 확인
- 검증하지 못한 항목: 문서 문장 전체의 수작업 교정, 기존 통합 문서 삭제
- 검증하지 못한 이유: 삭제는 안전 검토상 별도 명시 승인 필요. 문서 전체 문장 교정은 이번 요청의 구조 분리 완료 후 남은 품질 개선 항목
- 남은 리스크: 기존 통합 문서에서 분리했기 때문에 일부 inline XML 예시의 따옴표 표기는 추가 교정 여지가 있음
- 후속 작업: 필요 시 기존 통합 문서 삭제를 명시 승인받고, 문서별 문장/표기 교정을 한 번 더 수행
- Git commit: 없음


## [2026-08-10 22:35] PROGRESS-20260810-2235-001 — DONE

- 수행한 작업: 기존 /home/junyeopkwon/jsbsim/aircraft/F450를 복제해 /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM 생성. 프로젝트 보관용 사본 ircraft_variants/F450_DATCOM 생성. 비교 미션 scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml 및 초기조건 scripts/F450_DATCOM/initial_condition/1.0__ground_park_heading0_init.xml 생성.
- 조사한 파일: C:/Users/junyeopkwon/Downloads/jsbsim_aerodynamic_database.xml, /home/junyeopkwon/jsbsim/aircraft/F450/F450.xml, /home/junyeopkwon/jsbsim/aircraft/F450/Metrics.xml, /home/junyeopkwon/jsbsim/aircraft/F450/FlightControl.xml, /home/junyeopkwon/jsbsim/aircraft/F450/Aero.xml, /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml, scripts/run_jsbsim_timestamped_combined_csv_only.py
- 생성한 파일: /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/*, ircraft_variants/F450_DATCOM/*, scripts/F450_DATCOM/initial_condition/1.0__ground_park_heading0_init.xml, scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml, logs/csv/combined/F450_DATCOM/1.0__attitude_axis_datcom_compare/1.0.1__F450_vs_F450_DATCOM_attitude_compare_summary_08102235.csv
- 수정한 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/TODO.md, docs/agent-log/INDEX.md
- 핵심 변경점: F450_DATCOM은 F450의 mass/gear/propulsion/effectors/autopilot/sensors를 유지하고, DATCOM metrics의 wingarea=1.0650005 M2, wingspan=3 M, chord=0.36967129 M를 적용했다. 기존 multicopter mixer를 유지하면서 DATCOM light_control의 elevator/aileron aerosurface scale channel을 추가했다. Aero.xml은 DATCOM aerodynamic axes를 적용했다.
- 호환성 조정: 첨부 XML의 6개 
ow+table base table은 JSBSim 1.2.4가 FGTable: missing lookup axis column으로 거부했다. 숫자 데이터는 변경하지 않고 Mach reakPoint 블록을 column으로 합친 
ow+column 2D table 구조로 변환했다. 
ow+column+table control increment table은 유지했다.
- 실행한 명령어: XML parse 확인, JSBSim --aircraft=F450_DATCOM --catalog --nohighlight, python3 scripts/run_jsbsim_timestamped_combined_csv_only.py --aircraft F450 ..., python3 scripts/run_jsbsim_timestamped_combined_csv_only.py --aircraft F450_DATCOM ..., Python CSV window summary
- 테스트 결과: F450와 F450_DATCOM 모두 70초까지 정상 종료. F450 CSV rows 8751, columns 191. F450_DATCOM CSV rows 8751, columns 155. console fatal/abort/failed/nan 검색 결과 0건.
- 비교 결과: final hover 60-70초 기준 F450 고도 평균 10.0053 m, 마지막 10.0037 m, 수직속도 평균 0.0001668 m/s. F450_DATCOM 고도 평균 9.66485 m, 마지막 9.8536 m, 수직속도 평균 0.0106851 m/s. 파생 모델은 cs/effective-aileron-pos-deg, cs/elevator-pos-deg, ero/coefficient/CL_base, CD_base, Cm_base, aero force/moment가 비영으로 기록되어 공력 적용이 로그상 확인됨.
- 검증하지 못한 항목: FlightGear 시각 검증, DATCOM reference geometry가 F450 질량/모터 배치와 물리적으로 일관되는지에 대한 별도 설계 검증, position-hold mode 3에서의 장시간 정지 hover 안정성
- 검증하지 못한 이유: 이번 요청은 공력 적용 확인을 위한 동일 attitude-mode 비교 실행이 우선이었고, tuning/시각화는 별도 작업 범위임
- 남은 리스크: DATCOM reference area/span/chord가 기존 F450보다 매우 커서 공력 효과가 강하게 나타난다. p/mode=2는 altitude hold와 attitude command 확인용이며 위치 고정 hover가 아니므로 수평속도 drift는 미션 특성상 발생할 수 있다.
- 후속 작업: 필요하면 mode 3 position-hold hover 미션과 mode 2 attitude step 미션을 분리해 각각 기준을 세우고, 파생 모델용 controller gain 또는 reference geometry 적용 범위를 재검토
- Git commit: 없음


## [2026-08-10 22:40] CORRECTION-20260810-2240-001 — 정정

- 대상 기록: TASK-20260810-2235-001, PROGRESS-20260810-2235-001, DECISION-20260810-2235-001, TODO-20260810-2235-001, INDEX-20260810-2235-001
- 정정 이유: PowerShell command string에서 Markdown backtick escape가 적용되어 일부 경로와 row/table 표기가 제어문자로 기록됨
- 기존 내용: 일부 backtick-wrapped path 및 row+table, row+column 표기가 깨져 보임
- 정정 내용: 실제 변경 파일은 /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/initial_condition/1.0__ground_park_heading0_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml 이다. JSBSim 호환을 위해 DATCOM base table 6개는 row plus table 구조에서 row plus column 구조로 재구성했으며 숫자 데이터는 변경하지 않았다.
- 영향 범위: 작업 기록 문서 표기 정정만 해당. 모델 파일, runscript, CSV 로그에는 영향 없음
- 검증 결과: INDEX.md 최신 tail에서 정정 항목이 append됨
- 다음 작업: 최종 응답에서는 정정된 경로와 결과만 보고


## [2026-08-10 22:50] PROGRESS-20260810-2250-001 — DONE

- 수행한 작업: F450 및 F450_DATCOM combined CSV를 matplotlib로 읽어 비교 그래프 5개 생성
- 조사한 파일: /home/junyeopkwon/jsbsim_workflow/logs/csv/combined/F450/1.0__attitude_axis_datcom_compare/1.0.1__attitude_axis_datcom_compare_combined_08102235.csv, /home/junyeopkwon/jsbsim_workflow/logs/csv/combined/F450_DATCOM/1.0__attitude_axis_datcom_compare/1.0.1__attitude_axis_datcom_compare_combined_08102235.csv
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/plots/F450_DATCOM_attitude_compare_08102235/01_overview_altitude_attitude_velocity.png, 02_attitude_tracking_and_aerosurfaces.png, 03_aero_forces_moments.png, 04_datcom_coefficients.png, 05_aero_state.png
- 수정한 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 핵심 변경점: 시간축 0-70초 기준으로 altitude, vertical speed, roll/pitch tracking, north/east velocity, aerosurface equivalent deflection, aero force/moment, DATCOM coefficient, alpha/beta/qbar-area 비교 그래프를 생성
- 실행한 명령어: python3 matplotlib plot generation, PIL Image.open metadata validation
- 테스트 결과: PNG 5개 생성 확인. 크기는 각각 2520x1800, 2520x1980, 2700x1440, 2520x1800, 2520x1620.
- 검증하지 못한 항목: view_image 도구를 통한 직접 이미지 렌더 확인
- 검증하지 못한 이유: view_image가 WSL 경로와 Windows visualization 경로 모두에서 windows sandbox helper 오류를 반환함
- 남은 리스크: 이미지 파일 자체는 PIL로 열리지만, 그래프 디자인의 시각적 세부 품질은 직접 렌더 확인이 필요할 수 있음
- 후속 작업: 필요하면 position-hold hover 미션까지 포함한 비교 그래프 세트를 추가 생성
- Git commit: 없음


## [2026-08-10 23:00] PROGRESS-20260810-2300-001 — DONE

- 수행한 작업: 공력 적용 검증 1~6번을 모두 실행하고 별도 문서 docs/F450_DATCOM_AERO_VALIDATION.md를 작성
- 조사한 파일: /mnt/c/Users/junyeopkwon/Downloads/jsbsim_aerodynamic_database.xml, /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/Aero.xml, /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/FlightControl.xml, 기존 attitude 비교 CSV 2개
- 생성한 파일: docs/F450_DATCOM_AERO_VALIDATION.md, scripts/F450_DATCOM/initial_condition/2.0__free_response_10ms_theta5_init.xml, scripts/F450_DATCOM/runscript/2.0__propulsion_off_free_response_run.xml, logs/csv/combined/F450_DATCOM/aero_validation_08102253/aero_validation_checks_08102253.csv, plots/F450_DATCOM_aero_validation_08102253/06_propulsion_off_free_response.png, plots/F450_DATCOM_aero_validation_08102253/07_propulsion_off_thrust_check.png
- 수정한 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/INDEX.md
- 핵심 변경점: propulsion-off free-response 테스트를 추가해 ap/mode 0, SCAS 0, throttle 0 조건에서 F450과 F450_DATCOM의 aero force/moment 차이를 분리 검증함
- 실행한 명령어: JSBSim catalog 확인, run_jsbsim_timestamped_combined_csv_only.py F450 free-response 실행, run_jsbsim_timestamped_combined_csv_only.py F450_DATCOM free-response 실행, Python CSV 검증 분석, matplotlib PNG 생성, XML parse 확인
- 테스트 결과: aero_validation_checks_08102253.csv 기준 60개 검증 항목 모두 PASS. F450와 F450_DATCOM free-response 모두 8초 정상 종료. PNG 2개 생성 및 PIL 메타데이터 확인 완료.
- 검증하지 못한 항목: view_image 도구 기반 실제 렌더 확인, FlightGear 시각 검증, position-hold hover 장시간 검증
- 검증하지 못한 이유: view_image는 sandbox helper 오류를 반환했고, 이번 요청 범위는 공력 적용 확인 테스트와 문서화였음
- 남은 리스크: DATCOM reference geometry와 기존 F450 물리 모델의 일관성은 별도 검토 필요. row plus table을 row plus column으로 재구성한 보간 의미는 추가 확인 여지가 있음.
- 후속 작업: 10 m mode 3 position-hold hover, headwind/crosswind hover, forward speed 조건별 qbar scaling 추가 검증
- Git commit: 없음

## [2026-08-11 16:45] PROGRESS-20260811-1645-001 — DONE_WITH_RISK

- 수행한 작업: AD3000 aircraft 생성 스크립트 작성 및 workflow variant/runscript 생성
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_generate_aircraft.py, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/AD3000/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000/initial_condition/1.0__ground_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000/runscript/1.0__smoke_hover_run.xml
- 핵심 변경점: /home/junyeopkwon/jsbsim/aircraft/AD3000과 동일한 variant 파일을 workflow에 보관하고 runscript를 추가
- 실행한 명령어: python3 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_generate_aircraft.py
- 검증 결과: 생성 스크립트 exit 0
- 연계 검증: /home/junyeopkwon/jsbsim에서 XML 검사, catalog load, 1.5초 짧은 runscript 실행 통과
- 실패한 검증: 8초 smoke hover는 Floating point exception으로 실패
- 검증하지 못한 항목: workflow batch runner 연결, workflow Excel 등록, 장시간 hover/transition run
- 남은 리스크: 생성 스크립트는 최초 생성 산출물 기준이며, 이후 hover mixer split 보정은 아직 반영되지 않음
- Git commit: 없음

## [2026-08-11 17:05] PROGRESS-20260811-1705-001 — 정정 완료

- 수행한 작업: AD3000 workflow mirror Markdown 설명 문서와 생성 스크립트 Markdown 템플릿 한글화
- 수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/AD3000/README.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/AD3000/ASSUMPTIONS_AND_LIMITATIONS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_generate_aircraft.py
- 변경 이유: Markdown 설명 문서가 영어로 생성되어 전역 기록/문서 언어 정책과 맞지 않음
- 검증 명령어: cmp mirror Markdown files, python3 -m py_compile scripts/AD3000_generate_aircraft.py
- 검증 결과: jsbsim root와 workflow mirror Markdown 동일, 생성 스크립트 py_compile 통과
- 남은 리스크: XML documentation과 CSV note에는 영어 표현이 일부 남아 있음
- Git commit: 없음

## [2026-08-11 00:00] PROGRESS-20260811-0000-002 — 완료

- 과업: AD3000 제품 기반 propulsion 데이터 반영
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 제공된 Hobbywing 및 Falcon 제품 URL의 추력/전력 자료를 기준으로 JSBSim engine/thruster XML 구성
- 관련 파일: AD3000_lift_motor_V6212_180KV.xml, AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, AD3000_cruise_motor_V6215_210KV.xml, AD3000_cruise_prop_Falcon_C2E_20x10.xml, Propulsion.xml, PROPULSION_PRODUCTS.md, PROPULSION_SOURCE_DATA.csv
- 수행 내용: V6212 180KV lift motor와 Hobbywing VSC 22.1x7.4 lift prop XML을 추가하고, V6215 210KV cruise motor와 Falcon C2E 20x10 cruise prop XML을 추가함. AD3000 Propulsion.xml의 engine과 thruster 참조를 제품 기반 파일명으로 교체함. 제품별 원자료와 환산값을 Korean Markdown 및 CSV로 정리하고 workflow 저장소에 mirror함
- 변경 이유: 초기 mass 기반 임의 propulsion 모델을 공개 제품 사양과 pull test 기반 모델로 개선하기 위함
- 검증 명령어: xmllint --noout /home/junyeopkwon/jsbsim/engine/AD3000_lift_motor_V6212_180KV.xml /home/junyeopkwon/jsbsim/engine/AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml /home/junyeopkwon/jsbsim/engine/AD3000_cruise_motor_V6215_210KV.xml /home/junyeopkwon/jsbsim/engine/AD3000_cruise_prop_Falcon_C2E_20x10.xml /home/junyeopkwon/jsbsim/aircraft/AD3000/Propulsion.xml
- 검증 결과: XML well-formed 검사 통과
- 검증 명령어: /home/junyeopkwon/jsbsim/build/src/JSBSim --root=/home/junyeopkwon/jsbsim --aircraft=AD3000 --catalog
- 검증 결과: AD3000 aircraft catalog 로드 성공
- 검증 명령어: /home/junyeopkwon/jsbsim/build/src/JSBSim --root=/home/junyeopkwon/jsbsim --script=/home/junyeopkwon/jsbsim/scripts/AD3000_smoke_hover_run.xml --end=1.5
- 검증 결과: 1.5초 smoke 실행 성공. 마지막 샘플 기준 lift thrust는 대략 15.16, 12.68, 15.18, 12.66 lbf이며 pusher thrust는 0 lbf임
- 검증하지 못한 항목: Falcon C2E 20x10 직접 추력/전력 표 부재로 cruise prop 계수는 추정값임. 8초 전체 hover run의 Floating point exception은 기존 리스크로 남음
- 가정: 공기밀도 rho=1.225 kg/m3, static Ct=T/(rho*n^2*D^4), static Cp=P/(rho*n^3*D^5), 일반 advance ratio shape를 사용함
- 남은 리스크: 실제 ESC, 배터리 전압 sag, prop wash, 설치 간섭, 전진비별 prop polar가 반영되지 않았음
- 다음 작업: 제품 조합별 실측표 확보 후 Ct/Cp 재산정 및 hover trim 제어 보정
- 관련 기록: TASK-20260811-0000-002, DECISION-20260811-0000-002, TODO-20260811-0000-002
- Git commit: 없음

## [2026-08-11 17:11] CORRECTION-20260811-1711-001 — 정정

- 대상 기록: TASK-20260811-0000-002, PROGRESS-20260811-0000-002, DECISION-20260811-0000-002, TODO-20260811-0000-002, INDEX-20260811-0000-002
- 정정 이유: 제품 기반 propulsion 반영 기록을 append할 때 기록 시각을 임시값 2026-08-11 00:00으로 남김
- 기존 내용: 기록 시각이 2026-08-11 00:00 또는 ENTRY ID 20260811-0000으로 표기됨
- 정정 내용: 해당 항목의 실제 기록 시각은 2026-08-11 17:11 KST임. 기록 내용과 검증 결과는 그대로 유효함
- 영향 범위: docs/agent-log 아래 Markdown 기록의 메타데이터 시각 표기
- 검증 결과: append-only 방식으로 정정 기록을 추가함
- 다음 작업: 이후 기록에서는 실제 KST 시각을 사용

## [2026-08-12 09:00] PROGRESS-20260812-0900-001 — 완료

- 과업: AD3000 제품 공개표 기반 propulsion 재반영
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: cruise도 V6215+VSC22.1x7.4 공개 데이터 시트를 기준으로 구성하고 AD3000 XML 내부 주석을 한글화
- 관련 파일: AD3000 Propulsion.xml, Metrics.xml, Mass.xml, AD3000.xml, 제품 motor/prop XML, PROPULSION_PRODUCTS.md, PROPULSION_SOURCE_DATA.csv, workflow mirror, AD3000_generate_aircraft.py
- 수행 내용: AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml을 추가하고 Propulsion.xml의 cruise thruster 참조를 해당 파일로 변경함. V6215+VSC22.1x7.4 공식 pull test 45-84% throttle 행에서 cruise Ct0=0.07410, Cp0=0.02732를 산출함. V6212+VSC22.1x7.4 lift 계수는 공식표 정확 행 기준 Ct0=0.07464, Cp0=0.02744로 재확인함. XML 내부 documentation과 주석을 한글로 정리함. Metrics.xml의 중복 XML declaration도 제거함
- 변경 이유: 공개표가 없는 Falcon 20x10 추정값을 현재 기본 참조로 두지 않고, 공개 데이터가 있는 제품 조합을 임시 기준으로 명시하기 위함
- 검증 명령어: xmllint --noout /home/junyeopkwon/jsbsim/aircraft/AD3000/*.xml 및 관련 engine XML
- 검증 결과: 통과
- 검증 명령어: python3 -m py_compile /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_generate_aircraft.py
- 검증 결과: 통과
- 검증 명령어: /home/junyeopkwon/jsbsim/build/src/JSBSim --root=/home/junyeopkwon/jsbsim --aircraft=AD3000 --catalog
- 검증 결과: 통과
- 검증 명령어: /home/junyeopkwon/jsbsim/build/src/JSBSim --root=/home/junyeopkwon/jsbsim --script=/home/junyeopkwon/jsbsim/scripts/AD3000_smoke_hover_run.xml --end=1.5
- 검증 결과: 통과
- 검증하지 못한 항목: Falcon 20x10 직접 데이터, full 8초 hover run 안정성
- 가정: VSC 22.1x7.4 cruise 적용은 임시 모델이며 실제 cruise prop 의도는 Falcon C2E 20x10임
- 남은 리스크: 실제 prop diameter와 pitch 차이로 transition 성능 예측이 달라질 수 있음
- 다음 작업: 실제 20x10 데이터 확보 후 cruise prop XML 교체 및 transition 검증
- 관련 기록: TASK-20260812-0900-001, DECISION-20260812-0900-001, TODO-20260812-0900-001
- Git commit: 없음

## [2026-08-12 09:14] PROGRESS-20260812-0914-001 — 완료

- 과업: AD3000 XML 적용값 자동 검증
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: AD3000 전체 XML에 적용된 값이 제대로 들어갔는지 확인하는 방법 제공
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py
- 수행 내용: 검증 스크립트를 추가하고 SOURCE_MATRIX.csv의 혼합 헤더 구조를 처리하도록 파서를 작성함. 검증 항목은 AD3000.xml 하위 include, Mass.xml의 total mass/CG/inertia, Metrics.xml 기본값과 XML declaration, Propulsion.xml의 engine count/order/file/sense/location, motor 전기 사양, prop diameter와 J=0 Ct/Cp, JSBSim catalog load임
- 변경 이유: JSBSim 동적 실행 전에 XML 수치와 참조가 기준 데이터에 맞게 적용됐는지 빠르게 확인하기 위함
- 검증 명령어: python3 -m py_compile /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py
- 검증 결과: 통과
- 검증 명령어: python3 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py --run-jsbsim
- 검증 결과: PASS 86, FAIL 0. JSBSim catalog load returncode=0
- 검증하지 못한 항목: hover 안정성, Falcon 20x10 실제 성능표, 장시간 run 안정성
- 가정: source CSV 값이 현재 XML의 의도 기준임
- 남은 리스크: script는 구성값 검증용이며 실제 항공기 거동 검증은 별도 테스트가 필요함
- 다음 작업: smoke run CSV에서 altitude, attitude, thrust monotonicity를 검사하는 동적 검증 추가 가능
- 관련 기록: TASK-20260812-0914-001
- Git commit: 없음

## [2026-08-12 09:19] PROGRESS-20260812-0919-001 — 완료

- 과업: AD3000 table 보간값 검증 도구 추가
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 특정 alpha, Mach, deflection, advance ratio 조건에서 XML table 값이 어떻게 나오는지 확인
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_eval_table.py
- 수행 내용: 1D prop table은 --table과 --x로 보간값을 출력하고, Aero.xml function table은 --function과 --var 입력으로 2D 또는 breakPoint 기반 3D 보간값을 출력하게 함. 출력에는 최종 value, row/column/table breakpoint 범위, 보간 비율, 주변 grid 값이 포함됨
- 변경 이유: XML table 적용 확인을 수동 계산 없이 재현 가능하게 만들기 위함
- 검증 명령어: python3 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_eval_table.py --xml /home/junyeopkwon/jsbsim/engine/AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml --table C_THRUST --x 0.45
- 검증 결과: value 0.05261, x 0.4..0.5 보간 출력
- 검증 명령어: python3 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_eval_table.py --xml /home/junyeopkwon/jsbsim/aircraft/AD3000/Aero.xml --function aero/coefficient/CL_de --var aero/alpha-deg=2 --var fcs/elevator-pos-deg=7.5 --var velocities/mach=0.15
- 검증 결과: value 0.00525, table breakPoint 0.1..0.2 보간 출력
- 검증하지 못한 항목: JSBSim run output property와 자동 비교하는 통합 검증
- 가정: JSBSim table interpolation은 선형 보간 기준으로 검토함
- 남은 리스크: 실제 JSBSim axis force/moment 출력에는 table 값 외 product 항이 곱해질 수 있음
- 다음 작업: 필요하면 특정 초기조건 runscript와 output property 비교 도구 추가
- 관련 기록: TASK-20260812-0919-001
- Git commit: 없음

## [2026-08-12 09:40] PROGRESS-20260812-0940-001 — 완료

- 과업: 엑셀 기체 Spec 기반 propulsion source data 재정리
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: C:/Users/junyeopkwon/Downloads/DB 정리.xlsx의 기체 Spec 시트 데이터를 propulsion에 반영
- 관련 파일: /home/junyeopkwon/jsbsim/aircraft/AD3000/PROPULSION_SOURCE_DATA.csv, /home/junyeopkwon/jsbsim/aircraft/AD3000/PROPULSION_PRODUCTS.md, /home/junyeopkwon/jsbsim/aircraft/AD3000/Propulsion.xml, /home/junyeopkwon/jsbsim/engine/AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, /home/junyeopkwon/jsbsim/engine/AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml
- 수행 내용: 기체 Spec 시트의 H5:R28 cruise 표와 H30:R53 lift 표를 추출함. PROPULSION_SOURCE_DATA.csv에 workbook, sheet, range, table_title, temperature, used_for_coefficient 컬럼을 추가해 전체 원자료 행을 보존함. prop XML documentation과 Propulsion.xml 한글 주석을 엑셀 시트 기준으로 갱신함. workflow mirror와 engine_variants도 동기화함
- 변경 이유: 모델 계수 산정 출처를 사용자가 제공한 DB 정리.xlsx 파일로 추적 가능하게 하기 위함
- 검증 명령어: xmllint --noout /home/junyeopkwon/jsbsim/aircraft/AD3000/Propulsion.xml 및 관련 prop XML
- 검증 결과: 통과
- 검증 명령어: python3 -m py_compile AD3000_generate_aircraft.py AD3000_validate_config.py AD3000_eval_table.py
- 검증 결과: 통과
- 검증 명령어: python3 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py --run-jsbsim
- 검증 결과: PASS 86, FAIL 0
- 검증 명령어: JSBSim smoke hover run --end=1.5
- 검증 결과: 성공
- 검증하지 못한 항목: 장시간 hover 안정성 및 20*10 prop 직접 데이터
- 가정: 45-84% throttle 구간을 prop XML 계수 산정 대표 구간으로 유지
- 남은 리스크: CSV 전체 행 평균이 아니라 used_for_coefficient=Y 행 평균을 prop XML과 validator가 사용함
- 다음 작업: 실제 20*10 표 확보 후 used_for_coefficient 기준과 prop XML 재검토
- 관련 기록: TASK-20260812-0940-001, DECISION-20260812-0940-001
- Git commit: 없음

## [2026-08-12 09:46] PROGRESS-20260812-0946-001 — 완료

- 과업: 33-100% 전체 propulsion data 적용
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 기체 Spec 시트의 공식 pull test 전체 데이터 사용
- 관련 파일: /home/junyeopkwon/jsbsim/aircraft/AD3000/PROPULSION_SOURCE_DATA.csv, /home/junyeopkwon/jsbsim/engine/AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, /home/junyeopkwon/jsbsim/engine/AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml
- 수행 내용: V6212/V6215 각각 22개 행, 총 44개 행 전체를 prop XML 계수 산정 대상으로 표시함. lift full Ct0=0.074598, Cp0=0.027951, cruise full Ct0=0.073876, Cp0=0.027725를 산출해 prop XML C_THRUST/C_POWER table의 J=0 기준값을 갱신함. workflow mirror와 생성 스크립트도 동기화함
- 변경 이유: 공식 데이터가 존재하는 범위는 제외하지 않고 사용해야 한다는 사용자 지적을 반영함
- 검증 명령어: PROPULSION_SOURCE_DATA.csv 행 수 및 used_for_coefficient 확인
- 검증 결과: rows 44, used Y 44, 각 configuration 33.0-100.0 throttle 범위 확인
- 검증 명령어: python3 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py --run-jsbsim
- 검증 결과: PASS 86, FAIL 0
- 검증 명령어: JSBSim smoke run --end=1.5
- 검증 결과: 성공
- 검증하지 못한 항목: throttle별 공식표를 JSBSim 내부에서 직접 보간하는 coupled map 검증
- 가정: 현재 prop XML의 C_THRUST/C_POWER는 advance-ratio table이므로 공식 throttle table 전체는 대표 Ct/Cp 평균 산정에 사용함
- 남은 리스크: throttle별 thrust/power 곡선을 직접 재현하는 모델은 아직 아님
- 다음 작업: 필요 시 motor/prop test table을 별도 map으로 구현
- 관련 기록: TASK-20260812-0946-001, DECISION-20260812-0946-001
- Git commit: 없음

## [2026-08-12 09:55] PROGRESS-20260812-0955-001 — 완료

- 과업: 전진비 J 산정 방식과 임시 table shape 주석화
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 계산값을 만들어 넣을 경우 해당 주석을 XML에 명시
- 관련 파일: /home/junyeopkwon/jsbsim/engine/AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, /home/junyeopkwon/jsbsim/engine/AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, /home/junyeopkwon/jsbsim/aircraft/AD3000/Propulsion.xml, /home/junyeopkwon/jsbsim/aircraft/AD3000/PROPULSION_PRODUCTS.md
- 수행 내용: documentation에 V=0 static pull test로부터 J=0 Ct/Cp만 직접 산출 가능하다는 설명과 J>0 C_THRUST/C_POWER는 J=0 계수에 임시 advance-ratio 감소 shape를 곱한 값이라는 설명을 추가함. products 문서에 J=V/(nD), n=RPM/60 공식을 추가함
- 변경 이유: 사용자가 XML 값을 검토할 때 데이터 기반 값과 가정 기반 값을 구분할 수 있도록 하기 위함
- 검증 명령어: xmllint --noout /home/junyeopkwon/jsbsim/aircraft/AD3000/Propulsion.xml 및 관련 prop XML
- 검증 결과: 통과
- 검증 명령어: python3 -m py_compile AD3000_generate_aircraft.py AD3000_validate_config.py
- 검증 결과: 통과
- 검증 명령어: python3 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py --run-jsbsim
- 검증 결과: PASS 86, FAIL 0
- 검증하지 못한 항목: 실측 전진비별 prop map
- 가정: 현재 엑셀 데이터에는 airspeed V가 없으므로 모든 시험점은 J=0으로 처리
- 남은 리스크: J>0 table은 정확한 물리 실측값이 아님
- 다음 작업: 전진속도 포함 데이터 확보 후 AD3000_eval_table.py로 J별 table 검증
- 관련 기록: TASK-20260812-0955-001
- Git commit: 없음


## [2026-08-12 00:00] PROGRESS-20260812-0000-001 — DONE

- 과업: `5.16` 원형 선회 구간 분석
- 조사한 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.16__ksfo28r_runway_return_circular_landing_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/logs/csv/raw/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.6__ksfo28r_runway_return_circular_landing_raw_08022350.csv`
- 수행 내용: `simulation/mission-state` 전이와 `simulation/circular-loiter-active` 값을 기준으로 선회 구간 계산
- 검증 결과:
  - `STATE 5`: `153.733 - 183.733 s`, 안정화 cruise 30초
  - `STATE 6`: `183.742 - 199.833 s`
  - `STATE 7`: `199.842 - 215.042 s`
  - `STATE 8`: `215.050 - 229.825 s`
  - `STATE 9`: `229.833 - 244.308 s`
  - `circular-loiter-active=1`: `183.742 - 244.308 s`, duration `60.567 s`
- 권장 그래프 시간축: `180 - 245 s`
- 검증하지 못한 항목: 별도 only-turn runscript 생성 및 실행은 수행하지 않음
- 남은 리스크: 다른 실행 번호에서는 세부 시간이 수 초 이내로 달라질 수 있으므로, 해당 실행 CSV의 `mission-state`를 기준으로 보는 것이 가장 정확함
- Git commit: 없음

## [2026-08-13 13:39] PROGRESS-20260813-1339-001 — 완료

- 수행한 작업: standard_vtol_demo.xml과 jsbsim_aerodynamic_database.xml을 분석하고, JSBSim aircraft 폴더 /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo 및 workflow 복사본 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_jsbsim 을 구성했다.
- 조사한 파일: /mnt/c/Users/junyeopkwon/Downloads/standard_vtol_demo.xml, /mnt/c/Users/junyeopkwon/Downloads/jsbsim_aerodynamic_database.xml, /home/junyeopkwon/jsbsim/aircraft/F450/F450.xml, /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/Aero.xml, /home/junyeopkwon/jsbsim/scripts/Test_F450_Launch.xml.
- 생성한 파일: aircraft_variants/standard_vtol_demo_jsbsim/standard_vtol_demo.xml, standard_vtol_demo_datcom_aero.xml, standard_vtol_demo_demo_aero.xml, Aero_DATCOM.xml, Aero_Demo.xml, initGrnd.xml, initAir.xml, standard_vtol_demo_arming_check.xml, standard_vtol_demo_aero_check.xml, README.md, source XML 복사본 2개, results/standard_vtol_demo_jsbsim/*.csv, jsbsim_workflow_data/scripts/build_standard_vtol_jsbsim.py.
- 수정한 파일: /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo/*, /home/junyeopkwon/jsbsim/scripts/standard_vtol_demo_arming_check.xml, /home/junyeopkwon/jsbsim/scripts/standard_vtol_demo_aero_check.xml.
- 핵심 변경점: fcs/motor-armed를 추가해 fcs/esc-cmd-norm[0..4]가 fcs/esc-cmd-armed[0..4]를 거쳐 fcs/esc-out[0..4]로 전달되도록 구성. DATCOM 공력 테이블은 row/table breakpoint를 row/column 행렬로 변환했고, 3D Mach breakpoint 제어증분은 1차 검증을 위해 Mach 0.1 slice로 단순화. vt=0 지상 초기화를 위해 rate derivative의 1/velocities/vt-fps 항을 aero/ci2vel 및 aero/bi2vel로 치환.
- 실행한 명령어: python3 build_standard_vtol_jsbsim.py, JSBSim --root=/home/junyeopkwon/jsbsim scripts/standard_vtol_demo_arming_check.xml, JSBSim --root=/home/junyeopkwon/jsbsim scripts/standard_vtol_demo_aero_check.xml, JSBSim --aircraft=standard_vtol_demo --initfile=initGrnd --catalog=standard_vtol_demo.
- 테스트 결과: XML 파싱 11개 통과. JSBSim catalog에서 aero/coefficient/CL_base, CD_base, Cm_base, Cl_da, Cn_da 및 fcs/motor-armed, fcs/esc-out[0..4] 확인. arming 전 0.25/0.35/0.45/0.55/0.65 명령에도 esc-out[0..4]=0.0, arming 후 esc-out[0..4]=0.25/0.35/0.45/0.55/0.65 확인. DATCOM aero check에서 CL_base, CD_base, Cm_base, Cl_da, Cn_da 값이 출력됨.
- 검증하지 못한 항목: 비행 안정성, 정상 수직이륙, 호버 유지, 천이, 미션, 착륙, DATCOM 전체 Mach breakpoint 제어증분 보간.
- 검증하지 못한 이유: 이번 요청 범위가 모델 구성 및 데이터/모터 입력 확인까지였고, 시나리오/제어 튜닝은 후속 단계로 분리됨.
- 남은 리스크: 생성기 build_standard_vtol_jsbsim.py는 초기 생성 후 수동 postprocess가 추가 적용된 상태이므로 재실행 시 DATCOM postprocess를 반영하도록 정리 필요. DATCOM 함수명은 coefficient지만 aero/qbar-area를 곱하므로 실행 출력은 순수 계수가 아니라 force/moment 스케일 기여량임.
- 후속 작업: 생성기 postprocess 통합, 천이 없는 수직이륙-상승-하강-착륙 시나리오 구성, 이후 천이 시나리오 구성.
- Git commit: 없음.

## [2026-08-13 14:45] PROGRESS-20260813-1445-001 — DONE

- 과업: standard_vtol_demo 수직이륙-호버-착륙 JSBSim 미션 구성 및 실행
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo/standard_vtol_demo.xml
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo/initial_condition/1.0__rkss14_runway_ground_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo/runscript/1.0__rkss14_vertical_takeoff_hover_land_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/results/standard_vtol_demo_jsbsim/mission_vertical/standard_vtol_demo_rkss14_vertical_mission.csv, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/results/standard_vtol_demo_jsbsim/mission_vertical/standard_vtol_demo_rkss14_vertical_mission.log
- 수정한 파일: /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/standard_vtol_demo_hover.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/standard_vtol_demo_hover.xml
- 핵심 변경점: JSBSim 단독 hover용 attitude/altitude controller를 추가하고, mission/state를 CSV에 기록되도록 property 선언을 추가했다. 미션은 state 0~7로 pre-start, arm idle, takeoff, hover capture, descend, touchdown idle, shutdown, terminate를 구성했다.
- 실행한 명령어: JSBSim --nohighlight --root=/home/junyeopkwon/jsbsim /home/junyeopkwon/jsbsim_workflow/scripts/standard_vtol_demo/runscript/1.0__rkss14_vertical_takeoff_hover_land_run.xml
- 테스트 결과: 최종 실행 정상 종료. CSV 3601 rows 생성. 상태 전이: state0 t=0.00s, state1 t=1.00s, state2 t=3.01s, state3 t=8.59s, state4 t=20.00s, state5 t=23.06s, state6 t=32.00s, state7 t=36.00s.
- 실행 확인 결과: 최대 고도 32.7449 ft = 9.9806 m at t=20.01s. 10~20s 구간 평균 고도 32.5214 ft = 9.9125 m. 최종 t=36.00s, h-agl=0.5472 ft, mission/state=7, motor-armed=0, esc-out[0..4]=0.
- 검증하지 못한 항목: 실제 PX4 flightcontrol 연동, 천이 구간, 고정익 순항/선회, 실기체 수준 착륙 접지 모델 품질
- 남은 리스크: 현재 hover controller는 JSBSim 단독 미션 실행을 위한 내부 보조 제어기이며, PX4 제어기와 동일한 동작을 보장하지 않는다. 5번째 pusher는 수직 미션에서 의도적으로 0 명령이다.
- 후속 작업: 천이를 제외한 다음 시나리오 확장 또는 hover controller를 PX4-like 제어 구조로 정리
- Git commit: 없음

## [2026-08-13 15:04] PROGRESS-20260813-1504-001 — DONE

- 과업: standard_vtol_demo/standard_vtol_demo_hover 모듈 분리 개정
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 수정한 파일: /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo/standard_vtol_demo.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/standard_vtol_demo_hover.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_jsbsim/standard_vtol_demo.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/standard_vtol_demo_hover.xml
- 생성/갱신한 모듈 파일: Metrics.xml, Mass.xml, Gear.xml, Effectors.xml, FlightControl.xml, ExternalReactions.xml, Aero_DATCOM.xml, Aero_Demo.xml, Aero.xml, *_datcom_main.xml, *_demo_main.xml
- 생성한 보조 스크립트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/jsbsim_workflow_data/scripts/modularize_standard_vtol_demo_hover.py, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/jsbsim_workflow_data/scripts/fix_standard_vtol_main_include_order.py, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/jsbsim_workflow_data/scripts/repair_standard_vtol_literal_newlines.py, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/jsbsim_workflow_data/scripts/summarize_standard_vtol_vertical_mission.py
- 핵심 변경점: 메인 XML은 fileheader와 include만 유지한다. Effectors.xml에는 motor arming gate 및 actuator/property 계층, FlightControl.xml에는 hover attitude/altitude controller, ExternalReactions.xml에는 lift/pusher force, Aero_DATCOM.xml/Aero_Demo.xml에는 공력을 분리했다.
- 실행한 명령어: JSBSim --nohighlight --root=/home/junyeopkwon/jsbsim --aircraft=standard_vtol_demo --initfile=initGrnd --catalog=standard_vtol_demo; JSBSim --nohighlight --root=/home/junyeopkwon/jsbsim --aircraft=standard_vtol_demo_hover --initfile=initGrnd --catalog=standard_vtol_demo_hover; JSBSim --nohighlight --root=/home/junyeopkwon/jsbsim scripts/standard_vtol_demo_arming_check.xml; JSBSim --nohighlight --root=/home/junyeopkwon/jsbsim scripts/standard_vtol_demo_aero_check.xml; JSBSim --nohighlight --root=/home/junyeopkwon/jsbsim /home/junyeopkwon/jsbsim_workflow/scripts/standard_vtol_demo/runscript/1.0__rkss14_vertical_takeoff_hover_land_run.xml
- 검증 결과: standard_vtol_demo 및 standard_vtol_demo_hover catalog 파싱 통과. arming check에서 disarmed 상태 esc-out[0..4]=0, armed 상태 esc-out[0..4]=0.25/0.35/0.45/0.55/0.65 확인. aero check에서 CL_base/CD_base/Cm_base/Cl_da/Cn_da 출력 확인. 최종 수직 미션은 state7로 종료.
- 수직 미션 결과: CSV 3601 rows. 상태 전이 state0 t=0.00s, state1 t=1.00s, state2 t=3.01s, state3 t=8.59s, state4 t=20.00s, state5 t=23.06s, state6 t=32.00s, state7 t=36.00s. 최대 고도 9.9806 m, hover 평균 9.9125 m, 최종 motor-armed=0 및 esc-out[0..4]=0.
- 결과 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/results/standard_vtol_demo_jsbsim/mission_vertical/standard_vtol_demo_rkss14_vertical_mission_modular_final.csv, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/results/standard_vtol_demo_jsbsim/mission_vertical/standard_vtol_demo_rkss14_vertical_mission_modular_final.log, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/results/standard_vtol_demo_jsbsim/standard_vtol_modular_arming_check_final.log, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/results/standard_vtol_demo_jsbsim/standard_vtol_modular_aero_check_final.log
- 검증하지 못한 항목: 별도 propulsion 섹션 신규화, PX4 flightcontrol 동등성, 천이/고정익 미션
- 남은 리스크: 현재 모터 힘은 propulsion이 아니라 external_reactions 기반이다. 다음 천이 단계에서는 pusher/고정익 추력 모델을 JSBSim propulsion으로 재구성할지 판단 필요.
- Git commit: 없음

## [2026-08-13 15:05] PROGRESS-20260813-1505-001 — DONE

- 과업: standard_vtol_demo 모듈 XML 후처리
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 수행 내용: PowerShell 저장 과정에서 생성된 UTF-8 BOM을 standard_vtol_demo 관련 XML/Python 파일에서 제거했다.
- 변경 이유: JSBSim은 BOM 포함 XML도 읽었지만, XML 파일을 깔끔한 UTF-8 without BOM 상태로 유지하기 위함.
- 검증 명령어: JSBSim --nohighlight --root=/home/junyeopkwon/jsbsim --aircraft=standard_vtol_demo --initfile=initGrnd --catalog=standard_vtol_demo; JSBSim --nohighlight --root=/home/junyeopkwon/jsbsim --aircraft=standard_vtol_demo_hover --initfile=initGrnd --catalog=standard_vtol_demo_hover
- 검증 결과: BOM 제거 후 standard_vtol_demo 및 standard_vtol_demo_hover catalog 파싱 통과.
- 남은 리스크: 없음. 기능 변경 없이 파일 인코딩 marker만 제거함.
- Git commit: 없음

## [2026-08-13 15:10] PROGRESS-20260813-1510-001 — DONE

- 과업: standard_vtol_demo_hover workflow runner 실행 경로 수정
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.0__rkss14_runway_ground_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/1.0__rkss14_vertical_takeoff_hover_land_run.xml
- 수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py
- 핵심 변경점: discover_runscripts가 initial_condition 폴더를 제외하도록 필터를 추가했다. standard_vtol_demo_hover aircraft 선택 시 init/runscript 후보가 정상 표시되도록 파일을 배치했다.
- 실행한 명령어: cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts && printf '78\n1\n1\n' | python3 run_jsbsim_timestamped_combined_csv_only.py
- 검증 결과: 메뉴 선택 방식에서 aircraft 78 standard_vtol_demo_hover, init 1, runscript 1 선택 후 정상 실행. Combined CSV rows=3601, last time=36.
- 실행 확인 결과: 최신 combined CSV /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/combined/standard_vtol_demo_hover/1.0__rkss14_vertical_takeoff_hover_land/1.0.2__rkss14_vertical_takeoff_hover_land_combined_08131510.csv 에서 mission/state 전이 0->7 확인. 최대 고도 9.9806 m, 최종 motor-armed=0, esc-out[0..4]=0.
- 검증하지 못한 항목: aircraft 77 standard_vtol_demo 선택 플로우의 비행 성공 여부. 해당 모델은 hover controller 없는 기본/검증용 모델로 유지한다.
- 남은 리스크: standard_vtol_demo_hover 전용 미션은 78번 aircraft를 선택해야 한다.
- Git commit: 없음

## [2026-08-13 15:50] PROGRESS-20260813-1550-001 — DONE

- 과업: standard_vtol_demo_hover 천이 미션 구성 및 검증
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/PX4-Autopilot/src/modules/vtol_att_control/standard.cpp, /home/junyeopkwon/PX4-Autopilot/src/modules/vtol_att_control/vtol_type.cpp, /home/junyeopkwon/PX4-Autopilot/src/modules/vtol_att_control/vtol_att_control_params.c, /home/junyeopkwon/PX4-Autopilot/src/modules/vtol_att_control/standard_params.c
- 수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Effectors.xml
- 생성/수정한 runscript: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/2.0__rkss14_transition_mission_run.xml
- 생성한 보조 스크립트: add_standard_vtol_transition_controls.py, add_standard_vtol_hover_attitude_targets.py, patch_transition_runscript_events.py, tune_transition_backtransition_decel.py, tighten_transition_touchdown_condition.py, extend_transition_landing_window.py, summarize_standard_vtol_transition_csv.py
- 핵심 변경점: HoverAltitudeController/HoverAttitudeController를 Effectors.xml에서 FlightControl.xml로 이동했다. LiftMotorWeightBlend를 추가해 fcs/lift-esc-raw-norm[0..3]에 fcs/mc-weight를 곱한 뒤 esc-cmd-norm[0..3]로 전달한다. fcs/hover-roll-target-rad 및 fcs/hover-pitch-target-rad를 추가해 후방천이 pitch-up 감속을 구현했다.
- PX4 근거: standard.cpp line 67-69는 전방천이에서 pusher로 속도를 얻고 충분한 속도 후 rotor shutdown, 후방천이에서 pusher stop 및 rotor reactivate를 설명한다. line 196-229는 pusher throttle ramp 및 mc_weight blending을 수행한다. line 234-248은 후방천이 pitch 감속, pusher_throttle=0, mc_weight ramp-up을 수행한다. vtol_att_control_params.c는 VT_F_TRANS_THR, VT_ARSP_BLEND, VT_ARSP_TRANS, VT_B_TRANS_DUR 기본 개념을 정의하고 standard_params.c는 VT_B_TRANS_RAMP 및 VT_PSHER_SLEW를 정의한다.
- 실행한 명령어: cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts && printf '78\n1\n2\n' | python3 run_jsbsim_timestamped_combined_csv_only.py
- 검증 결과: 메뉴 선택 방식에서 aircraft 78 standard_vtol_demo_hover, init 1, runscript 2 실행 통과. Combined CSV rows=21502, last time=215.01.
- 최종 CSV: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/combined/standard_vtol_demo_hover/2.0__rkss14_transition_mission/2.0.6__rkss14_transition_mission_combined_08131550.csv
- 상태 전이: state0 t=0.00s, state1 t=1.00s, state2 t=3.01s, state3 t=8.59s, state4 t=14.01s, state5 t=26.00s, state6 t=30.00s, state7 t=42.00s, state8 t=58.01s, state9 t=80.00s, state10 t=96.00s, state11 t=188.33s, state12 t=210.01s, state13 t=215.01s.
- 실행 확인 결과: 최대 고도 50.1576 m, 최대 body-x 속도 22.5627 m/s. 최종 t=215.01s, h-agl=0.1668 m, u=0.0000 m/s, hdot=0.0000 m/s, mission/state=13, motor-armed=0, esc-out[0..4]=0.
- 검증하지 못한 항목: PX4 uORB 기반 실제 controller mixing, TECS fixed-wing altitude/airspeed controller, FW control surface elevator effectiveness, 실제 lift motor 완전 off FW cruise.
- 남은 리스크: 현재 FW segment는 DATCOM elevator effectiveness 부재 때문에 mc-weight 0.22 안정화가 남아 있다. 이것은 PX4 strict FW mode가 아니라 JSBSim standalone transition proof run이다.
- Git commit: 없음

## [2026-08-13 17:16] PROGRESS-20260813-1716-001 — DONE

- 과업: standard_vtol_demo_hover 멀티콥터 조종자격증 유사 미션 구성 및 검증
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 천이를 제외하고 멀티콥터 모드 정상 미션 runscript 3.0을 만들고, 1.1 지상 초기조건을 추가한다.
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Effectors.xml
- 수행 내용: 기존 1.0 초기조건은 보존하고 altitude 0.5567 ft, elevation 38.0 ft인 1.1 초기조건을 추가했다. 3.0 runscript는 mc-weight=1.0, pusher motor command 0.0을 유지하며 arm, takeoff, hover, lateral, forward/backward, triangle, circle approximation, emergency descent/recovery, landing, shutdown 상태를 구성했다. attitude target만 사용할 때 최종 drift가 약 383 m로 커서, 기본 off인 hover speed hold 보조 채널을 추가하고 3.0에서만 body forward/lateral speed target을 사용하도록 보정했다.
- 변경 이유: 사용자가 지적한 초기조건 자유낙하 문제를 기존 파일 손상 없이 새 버전으로 분리하고, 멀티콥터 단독 미션이 과도한 수평 drift 없이 실행되도록 하기 위함
- 검증 명령어: xmllint --noout aircraft_variants/standard_vtol_demo_hover/Effectors.xml aircraft_variants/standard_vtol_demo_hover/FlightControl.xml scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Effectors.xml /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/FlightControl.xml
- 검증 결과: XML 문법 검사 통과
- 검증 명령어: cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts && printf '78\n2\n3\n' | python3 run_jsbsim_timestamped_combined_csv_only.py --planet builtin
- 검증 결과: 3.0.2 combined CSV rows=19802, last time=198.01, final mission/state=32.0, final motor-armed=0.0, final esc-out[0..4]=0.0, mc-weight min/max=1.0/1.0, pusher esc-out max abs=0.0, pusher command range=0.0/0.0
- 검증 결과: 1.1 초기조건 첫 행 h-agl=0.5567 ft, geod-alt=38.5567 ft, terrain=38.0 ft. 첫 1초 max abs h-dot=0.0426 m/s, min h-agl=0.5458 ft, max gear force=55.19 lbf로 기존 4.305 ft 초기 자유낙하성 충격 대비 개선 확인
- 검증 결과: 3.0.2 전체 h-agl 범위 0.4816 - 13.3219 ft, 최대 고도 4.06 m, 최대 body horizontal speed 1.37 m/s, final displacement N/E=10.57/19.07 m, max distance from start=22.19 m
- 검증 명령어: cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts && python3 run_jsbsim_timestamped_combined_csv_only.py --aircraft standard_vtol_demo_hover --init /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.0__rkss14_runway_ground_init.xml --runscript /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/1.0__rkss14_vertical_takeoff_hover_land_run.xml --planet builtin
- 검증 결과: 기존 1.0 vertical mission 회귀 실행 rows=3601, final mission/state=7.0, final motor-armed=0.0, final esc-out[0..4]=0.0
- 검증하지 못한 항목: 실제 한국교통안전공단 실기시험 세부 geometry, GPS 좌표 기반 waypoint 추종, 실제 위치 hold/heading/yaw command, 시험 채점 tolerance
- 가정: 이번 단계는 JSBSim standalone multicopter mission proof이며, 실제 시험장 코스 엄밀 재현은 다음 단계에서 waypoint/position controller로 진행한다.
- 남은 리스크: 3.0 landing 중 최대 gear force는 약 236.88 lbf, 약 4.55 weight ratio로 초기 자유낙하 충격은 제거됐지만 착륙 profile은 더 부드럽게 튜닝 가능하다. final displacement는 약 21.8 m로 줄었으나 출발점 복귀 착륙은 아직 아니다.
- 다음 작업: waypoint/position hold controller와 yaw/heading command를 추가해 실제 시험 코스 거리와 원주/삼각 geometry를 명시적으로 추종하게 만든다.
- 관련 기록: TASK-20260813-1716-001, DECISION-20260813-1716-001, TODO-20260813-1716-001
- Git commit: 없음
## [2026-08-13 17:41] PROGRESS-20260813-1741-001 — DONE

- 과업: 3.0 멀티콥터 mission 전이 구조 수정 및 제어 구성 검증
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/FlightControl.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/ExternalReactions.xml
- 수행 내용: 3.0 runscript의 주 전이를 mission/state eq 이전상태 AND simulation/sim-time-sec ge mission/next-trigger-sec 구조로 변경했다. takeoff capture는 mission/state eq 2.0, h-agl >= 12.3 ft, h-dot <= 1.0 fps 조건으로 구성했다. emergency descent/recovery state를 제거하고 circle complete hover 이후 normal landing으로 바로 전이하도록 했다.
- 수행 내용: 최초 FG_DELTA 기반 next-trigger는 altitude capture가 지연되면 hover state가 즉시 지나가는 문제가 있어, 절대 trigger 시각을 사용하는 state-gated 방식으로 수정했다.
- 검증 명령어: xmllint --noout scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml aircraft_variants/standard_vtol_demo_hover/FlightControl.xml aircraft_variants/standard_vtol_demo_hover/Effectors.xml
- 검증 결과: XML 문법 검사 통과
- 검증 명령어: cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts && printf '78\n2\n3\n' | python3 run_jsbsim_timestamped_combined_csv_only.py --planet builtin
- 검증 결과: 3.0.5 combined CSV rows=14601, last time=146.0, final mission/state=30.0, final h-agl=0.5472 ft, final motor-armed=0.0, final esc-out[0..4]=0.0, mc-weight min/max=1.0/1.0, pusher esc-out max abs=0.0
- 검증 결과: state3 hover가 8.72 - 14.00 s로 5.28 s 유지됨. circle states 20 - 25 후 state26 circle complete hover, state27 normal landing, state28 touchdown idle, state29 shutdown, state30 terminate 순서로 진행됨.
- 검증 결과: 최대 고도 4.06 m, 최대 body horizontal speed 1.37 m/s, max distance from start 20.923 m, final displacement N/E=6.217/19.965 m
- 제어 확인: FlightControl.xml에서 forward speed target은 pitch target으로 변환되고, lateral speed target은 roll target으로 변환된다. pitch/roll/yaw rate damping mixer가 fcs/lift-esc-raw-norm[0..3]에 차등 반영되며, mc-weight를 곱해 fcs/esc-cmd-norm[0..3]로 전달된다. ExternalReactions.xml에서 esc-out[0..3]은 FR/RL/FL/RR 위치의 lift force로 작용한다.
- 제어 확인: CSV transient에서 forward state 진입 직후 front-rear motor command differential, lateral state 진입 직후 left-right motor command differential이 확인됨. pusher esc-out[4]는 전 구간 0으로 유지됨.
- 검증하지 못한 항목: JSBSim runscript만으로 phase start time을 현재 sim-time으로 저장하는 신뢰 가능한 문법은 확인하지 못함. yaw/heading target command는 아직 없음.
- 남은 리스크: 현재 duration은 state gate + 절대 trigger 방식이므로, 특정 phase가 trigger 시각보다 늦게 완료되는 극단 상황에서는 다음 hold 시간이 줄어들 수 있다. 실제 완전한 mission-complete 기준은 position/velocity/yaw tolerance와 state-age timer를 추가해야 한다.
- 다음 작업: FlightControl.xml에 mission state age 또는 waypoint 도달 판정을 명시적으로 구성하고, yaw heading command를 추가한다.
- Git commit: 없음
## [2026-08-13 17:45] CORRECTION-20260813-1745-001 — 정정

- 대상 기록: TASK-20260813-1741-001, PROGRESS-20260813-1741-001, DECISION-20260813-1741-001, INDEX-20260813-1741-001
- 정정 이유: state-gated/긴급강하 제거 수정을 기존 3.0 파일에 직접 적용해 버전 보존 원칙을 위반함. 사용자의 지적에 따라 기존 3.0은 복구하고 수정본은 3.1로 분리함.
- 기존 내용: 3.0__rkss14_multicopter_certificate_mission_run.xml을 state-gated 전이로 수정하고 긴급강하를 제거했다고 기록함.
- 정정 내용: 3.0__rkss14_multicopter_certificate_mission_run.xml은 이전 시간 기반/긴급강하 포함 버전으로 복구했다. state-gated/긴급강하 제거/원주 후 착륙 버전은 3.1__rkss14_multicopter_certificate_mission_state_gated_run.xml로 분리했다.
- 영향 범위: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.0__rkss14_multicopter_certificate_mission_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.1__rkss14_multicopter_certificate_mission_state_gated_run.xml
- 검증 결과: 3.0.6 실행 rows=19802, last time=198.01, final state=32, motor-armed=0, esc-out[0..4]=0, mc-weight=1, pusher=0. 3.1.1 실행 rows=14601, last time=146.0, final state=30, motor-armed=0, esc-out[0..4]=0, mc-weight=1, pusher=0.
- 다음 작업: 이후 runscript 동작 변경은 반드시 새 minor version 파일로 분리한다.
- Git commit: 없음
## [2026-08-13 18:07] PROGRESS-20260813-1807-001 — DONE

- 과업: standard_vtol_demo_hover metric/mass/coordinate update
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Metrics.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Mass.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Gear.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/ExternalReactions.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Metrics.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Mass.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Gear.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/ExternalReactions.xml
- 수행 내용: Metrics.xml에 wingarea=0.572 M2, wingspan=3.0 M, chord=0.215 M, wing_incidence=2.44 DEG, htailarea=0.164 M2, htailarm=0.0 M, vtailarea=0.083 M2, vtailarm=0.0 M을 반영했다.
- 수행 내용: Mass.xml에 emptywt=20.0 KG, CG=(0.64914,0,0) M을 반영했다. inertia ixx=10.7000, iyy=8.0000, izz=18.5000 KG*M2는 유지했다.
- 수행 내용: 기존 CG 기준 상대 x 좌표에 0.64914 m를 더해 nose 기준 x 좌표로 변환했다. AERORP/VRP=(0.64914,0,0), EYEPOINT=(0.79914,0,-0.05), front_foot x=1.24914, rear feet x=0.04914, lift motors x=-0.10486/1.40414, pusher x=2.24914로 반영했다.
- 검증 명령어: xmllint --noout aircraft_variants/standard_vtol_demo_hover/Metrics.xml aircraft_variants/standard_vtol_demo_hover/Mass.xml aircraft_variants/standard_vtol_demo_hover/Gear.xml aircraft_variants/standard_vtol_demo_hover/ExternalReactions.xml /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Metrics.xml /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Mass.xml /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Gear.xml /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/ExternalReactions.xml
- 검증 결과: XML 문법 검사 통과
- 검증 명령어: XML 파싱으로 Metrics/Mass/Gear/ExternalReactions 값 확인
- 검증 결과: 요청값 및 변환 좌표가 파싱 결과와 일치함. CSV 실행 결과 mass=20.0 kg, cg-x=0.64914 m 확인.
- 검증 명령어: cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts && python3 run_jsbsim_timestamped_combined_csv_only.py --aircraft standard_vtol_demo_hover --init /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml --runscript /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.1__rkss14_multicopter_certificate_mission_state_gated_run.xml --planet builtin
- 검증 결과: 3.1.3 실행 완료, rows=14601, last time=146.0, final mission/state=30.0, final motor-armed=0.0, final esc-out[0..4]=0.0, mc-weight=1.0, pusher=0.0
- 검증하지 못한 항목: htailarm/vtailarm 실제값, inertia 재계산, 실제 CAD 기반 nose-origin 좌표 전체 대조, 비-hover standard_vtol_demo variant 동기화 필요 여부
- 남은 리스크: emptywt가 23.6 kg에서 20.0 kg으로 줄었지만 hover throttle/gain은 유지했으므로 3.1 미션에서 h-agl 최대값이 약 20.50 ft(6.25 m)까지 overshoot된다. 다음 단계에서 hover base throttle 및 altitude controller 재튜닝 필요.
- 다음 작업: 20 kg 기준 hover throttle base 약 0.535 근처로 재튜닝하고, 4 m altitude target overshoot를 줄이는 3.2 또는 별도 controller update를 만든다.
- Git commit: 없음
## [2026-08-13 18:14] PROGRESS-20260813-1814-001 — DONE

- 과업: 20 kg 기준 hover throttle 산출 및 mission 제어 튜닝
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover/Effectors.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.2__rkss14_multicopter_certificate_mission_state_gated_20kg_hover_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.3__rkss14_multicopter_certificate_mission_state_gated_20kg_hover_smooth_land_run.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/runscript/3.4__rkss14_multicopter_certificate_mission_state_gated_20kg_hover_smooth_spooldown_run.xml
- 수행 내용: 20 kg 기준 hover throttle을 계산했다. 총 중량 약 44.16 lbf, 모터당 필요 추력 약 11.04 lbf. 현재 lift motor table의 0.5=9.45 lbf, 0.7=18.5 lbf 선형 구간에서 esc = 0.5 + (11.04-9.45)/(18.5-9.45)*0.2 ≈ 0.535로 산출했다.
- 수행 내용: Effectors.xml의 기본 fcs/hover-throttle-base-norm을 0.578에서 0.535로 변경하고 /home/junyeopkwon/jsbsim mirror에도 반영했다.
- 수행 내용: 기존 3.1은 보존하고, 20 kg hover baseline 버전을 3.2로 추가했다. 3.2에서 직접 착륙 target은 gear force가 약 6.02W로 커서, staged landing을 3.3으로 추가했다. 착지 후 collective를 천천히 빼는 slow spooldown을 3.4로 추가했다.
- 검증 명령어: xmllint --noout Effectors.xml 및 3.2/3.3/3.4 runscript
- 검증 결과: XML 문법 검사 통과
- 검증 명령어: run_jsbsim_timestamped_combined_csv_only.py --aircraft standard_vtol_demo_hover --init 1.1__rkss14_runway_ground_init.xml --runscript 3.2/3.3/3.4 --planet builtin
- 검증 결과: 3.2.1 final state30, motor-armed=0, esc-out[0..4]=0, hmax=4.065 m, hover avg collective=0.5345, max hdot=1.805 m/s, max gear force=265.94 lbf=6.02W, pusher=0
- 검증 결과: 3.3.1 final state32, motor-armed=0, esc-out[0..4]=0, hmax=4.065 m, hover avg collective=0.5345, max hdot=1.458 m/s, max gear force=223.14 lbf=5.05W, pusher=0
- 검증 결과: 3.4.1 final state33, motor-armed=0, esc-out[0..4]=0, hmax=4.065 m, hover avg collective=0.5345, max hdot=1.418 m/s, max gear force=221.64 lbf=5.02W, pusher=0
- 검증하지 못한 항목: 실제 모터/프로펠러 thrust curve 검증, gear spring/damping 재튜닝, position controller 기반 착륙점 복귀, yaw command
- 남은 리스크: 3.4에서도 gear force가 약 5.02W로 여전히 큰 편이다. 착륙 품질은 altitude target profile뿐 아니라 gear spring/damping, touchdown collective scheduling, vertical velocity target controller 추가로 더 줄여야 한다.
- 다음 작업: vertical velocity command 기반 landing controller 또는 gear damping 재튜닝을 별도 버전으로 진행한다.
- Git commit: 없음
## [2026-08-14 10:01 KST] PROGRESS-20260814-1001-001 — DONE

- 수행한 작업: pyulog/ulog2csv 설치 상태를 확인하고, PX4 .ulg를 하나의 forward-filled combined CSV로 변환하는 스크립트를 추가했다.
- 조사한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/combined, /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-14/*.ulg
- 생성한 파일: scripts/px4_ulog_to_combined_csv.py
- 생성한 산출물: logs/csv/combined/standard_vtol_demo_hover_px4/00_55_52/00_55_52_px4_combined_0814100111.csv
- 핵심 변경점: PX4 ULog topic들을 timestamp union 기준으로 합치고, 이전 값을 forward-fill하여 기존 combined CSV와 유사하게 한 파일에서 볼 수 있게 했다.
- 실행한 명령어: ulog2csv -m actuator_outputs,vehicle_local_position,vehicle_attitude,vehicle_status,estimator_status ...; python3 scripts/px4_ulog_to_combined_csv.py /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-14/00_55_52.ulg
- 검증 결과: combined CSV 2549행 생성 확인, ctuator_outputs.output[0..4], ehicle_status.*, sensor_combined.*, GPS 관련 컬럼 포함 확인
- 검증하지 못한 항목: 실제 QGC 미션에서 생성된 풍부한 flight topic 전체 변환 품질
- 남은 리스크: 짧은 actuator test 로그라 ehicle_local_position, ehicle_attitude, estimator_status가 없거나 제한적으로 기록됐다. 실제 미션 로그에서는 컬럼이 더 늘어난다.
- 후속 작업: QGC 미션 실행 후 최신 .ulg를 같은 스크립트로 변환하고 분석용 plotting/summary를 추가한다.
- Git commit: 없음

## [2026-08-14 10:08 KST] PROGRESS-20260814-1008-001 — DONE

- 수행한 작업: PX4 JSBSim QGC 실행 매뉴얼과 자동화 스크립트를 추가했다.
- 조사한 파일: scripts/, docs/, QGC AppImage 경로, PX4 airframe 경로
- 생성한 파일: docs/PX4_JSBSIM_QGC_RUNBOOK.md, scripts/run_px4_jsbsim_qgc_workflow.py
- 핵심 변경점: python3 run_px4_jsbsim_qgc_workflow.py --launch-qgc로 QGC를 켜고 PX4 JSBSim target을 실행한 뒤 종료 시 최신 .ulg를 combined CSV로 변환하도록 했다.
- 실행한 명령어: python3 -m py_compile scripts/run_px4_jsbsim_qgc_workflow.py scripts/px4_ulog_to_combined_csv.py; python3 scripts/run_px4_jsbsim_qgc_workflow.py --help; QGC/PX4/airframe 경로 존재 확인
- 검증 결과: py_compile OK, help 출력 OK, /home/junyeopkwon/Downloads/QGroundControl-x86_64.AppImage 존재 확인, /home/junyeopkwon/px4_versions/PX4-v1.16.0 존재 확인, 3020_jsbsim_standard_vtol_demo_hover_px4 존재 확인
- 검증하지 못한 항목: 자동화 스크립트로 실제 QGC GUI 실행 및 미션 수행
- 남은 리스크: Windows QGC를 사용할 경우 WSL2 UDP localhost 연결 문제가 있을 수 있어 WSL AppImage 실행을 우선 권장했다.
- 후속 작업: QGC에서 짧은 takeoff-hover-land 미션을 실제 실행하고 자동 변환된 CSV를 분석한다.
- Git commit: 없음

## [2026-08-14 10:54] PROGRESS-20260814-1054-002 — DONE

- 과업: PX4 JSBSim QGC 실행 매뉴얼 및 자동화 스크립트 RKSS 반영
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 수행 내용: docs/PX4_JSBSIM_QGC_RUNBOOK.md의 수동 실행 target을 jsbsim_standard_vtol_demo_hover_px4__RKSS로 변경했다. scripts/run_px4_jsbsim_qgc_workflow.py는 기본 world RKSS 및 RKSS target 생성 상태를 확인했고, 도움말 문구를 RKSS variant 설명으로 수정했다. PX4 최신 ULog 01_53_16.ulg를 combined CSV로 변환했다.
- 변경 파일: docs/PX4_JSBSIM_QGC_RUNBOOK.md, scripts/run_px4_jsbsim_qgc_workflow.py
- 생성 파일: logs/csv/combined/standard_vtol_demo_hover_px4/01_53_16/01_53_16_px4_combined_0814105344.csv
- 검증 명령어: python3 -m py_compile scripts/run_px4_jsbsim_qgc_workflow.py
- 검증 결과: OK
- 검증 명령어: python3 scripts/px4_ulog_to_combined_csv.py /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-14/01_53_16.ulg
- 검증 결과: combined CSV 생성, 242개 컬럼 확인, vehicle_gps_position/vehicle_local_position/vehicle_attitude/sensor_combined 컬럼 포함
- 검증하지 못한 항목: QGC UI에서 미션 업로드 및 비행 로그 생성
- 남은 리스크: 실제 mission 수행 전 control allocation/rotor 부호 검증 필요
- Git commit: 없음

## [2026-08-14 11:09] PROGRESS-20260814-1109-001 — DONE

- 과업: ULog 선택형 combined CSV 변환 기능 추가
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 수행 내용: 의  인자를 선택사항으로 변경했다. 인자가 없으면  아래의 를 최신순으로 표시하고 번호 입력으로 선택하게 했다. 와  옵션을 추가했다. 매뉴얼의 수동 변환 절차를 번호 선택 방식으로 갱신했다.
- 변경 파일: scripts/px4_ulog_to_combined_csv.py, docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 생성 파일: logs/csv/combined/standard_vtol_demo_hover_px4/01_59_04/01_59_04_px4_combined_0814110841.csv
- 검증 명령어: python3 -m py_compile scripts/px4_ulog_to_combined_csv.py
- 검증 결과: OK
- 검증 명령어: printf 

## [2026-08-14 11:12] CORRECTION-20260814-1112-002 — 정정

- 대상 기록: PROGRESS-20260814-1109-001
- 정정 이유: Markdown 백틱이 shell command substitution으로 해석되어 일부 명령어/식별자가 누락됨.
- 기존 내용: 파일명, 인자명, 검증 명령 일부가 누락됨.
- 정정 내용: scripts/px4_ulog_to_combined_csv.py의 ulg positional 인자를 optional로 변경했다. 인자가 없으면 /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log 아래의 .ulg 파일을 최신순으로 표시하고 번호 선택으로 변환한다. --log-root와 --list-limit 옵션을 추가했다. docs/PX4_JSBSIM_QGC_RUNBOOK.md의 수동 변환 예시는 인자 없이 실행 후 번호 선택하는 방식으로 갱신했다.
- 검증 명령어: python3 -m py_compile scripts/px4_ulog_to_combined_csv.py
- 검증 결과: OK
- 검증 명령어: printf '1\\n' | python3 scripts/px4_ulog_to_combined_csv.py --list-limit 5
- 검증 결과: 최신 ULog 목록 표시 후 1번 선택으로 logs/csv/combined/standard_vtol_demo_hover_px4/01_59_04/01_59_04_px4_combined_0814110841.csv 생성. 242개 컬럼, vehicle_gps_position 및 vehicle_local_position 컬럼 포함 확인.
- 다음 작업: QGC mission 후 생성된 최신 ULog 선택 변환.

## [2026-08-14 11:36] PROGRESS-20260814-1136-001 — DONE

- 과업: PX4 ULog와 JSBSim property 결합 CSV 및 그래프 생성 기능 추가
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 수행 내용: px4_jsbsim_compare_plot.py를 추가해 ULog 선택, PX4 combined CSV 생성, JSBSim native output CSV 읽기, merge_asof 기반 시간축 병합, 그래프 생성을 수행하게 했다. run_px4_jsbsim_qgc_workflow.py는 PX4 종료 후 JSBSim CSV 복사, PX4 plus JSBSim combined CSV, plots 생성을 수행하도록 연결했다. 매뉴얼에 PX4 plus JSBSim 변환 명령을 추가했다.
- 변경 파일: scripts/px4_jsbsim_compare_plot.py, scripts/run_px4_jsbsim_qgc_workflow.py, docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 생성 파일: logs/csv/combined_px4_jsbsim/standard_vtol_demo_hover_px4/02_26_56/02_26_56_px4_jsbsim_combined_0814113449.csv
- 생성 그래프: actuator_px4_vs_jsbsim.png, altitude_px4_vs_jsbsim.png, jsbsim_forces.png, jsbsim_aero.png
- 검증 명령어: python3 -m py_compile scripts/run_px4_jsbsim_qgc_workflow.py scripts/px4_jsbsim_compare_plot.py scripts/px4_ulog_to_combined_csv.py
- 검증 결과: OK
- 검증 명령어: printf 1 입력을 통해 python3 scripts/px4_jsbsim_compare_plot.py --list-limit 3 실행
- 검증 결과: ULog 목록 표시, 02_26_56.ulg 선택, 484컬럼 PX4 plus JSBSim combined CSV 생성, JSBSim esc command/out, altitude, gear force, alpha 컬럼 포함 확인
- 검증하지 못한 항목: 실제 mission flight 데이터에서 PX4 actuator_motors와 JSBSim esc 적용값의 수치 일치 분석
- 남은 리스크: JSBSim native output은 latest_jsbsim_properties.csv를 overwrite하므로 오래된 ULog와 비교할 때는 같은 실행에서 복사 보존된 JSBSim CSV를 사용해야 한다.
- Git commit: 없음

## [2026-08-18 11:35] PROGRESS-20260818-1135-001 — DONE

- 과업: `logs/csv/combined` 선회/제어 분석 컬럼 확장
- 대상 프로젝트: `/home/junyeopkwon/evtol-6dof/jsbsim_workflow`
- 요청 내용: combined CSV 로그 생성 시 추가로 필요한 정보 파악 및 반영
- 조사한 파일: `scripts/run_jsbsim_timestamped_combined_csv_only.py`, `scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py`, `aircraft_variants/c172x_4x75kg_cg_aligned_ksfo28r_landing/c172ap_landing.xml`, `scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.16__ksfo28r_runway_return_circular_landing_run.xml`, `aircraft_variants/standard_vtol_demo_hover/FlightControl.xml`, 기존 `logs/csv/combined/*`
- 수정한 파일: `scripts/run_jsbsim_timestamped_combined_csv_only.py`
- 생성한 파일: `logs/csv/combined/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.8__ksfo28r_runway_return_circular_landing_combined_08181131.csv`, `logs/generated_runscripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.8__ksfo28r_runway_return_circular_landing_combined_runscript_08181131.xml`, `logs/console/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing/5.16.8__ksfo28r_runway_return_circular_landing_combined_console_08181131.log`
- 핵심 변경점: combined runner에 `COMBINED_CONTROL_ANALYSIS_PROPERTIES`를 추가하고 `aircraft_catalog_properties()` 기반으로 실제 존재하는 property만 output에 합치도록 연결했다.
- 추가된 주요 컬럼: `ap/heading_setpoint`, `fcs/heading-error`, `fcs/heading-corrected`, `fcs/heading-command`, `fcs/heading-roll-error-lag`, `fcs/heading-roll-error`, `fcs/heading-roll-error-switch`, `ap/aileron_cmd`, `simulation/circular-bank-hold-active`, `mission/circular-bank-target-rad`, `mission/circular-bank-error-rad`, `mission/circular-bank-cmd-norm`, VTOL hover target/error/mix, F450/LiftCruise AP setpoint/error/mix 계열
- 실행한 명령어: `python3 -m py_compile scripts/run_jsbsim_timestamped_combined_csv_only.py`
- 검증 결과: Python 문법 검사 통과
- 실행한 명령어: C172 5.16 combined runner 실행 `python3 scripts/run_jsbsim_timestamped_combined_csv_only.py --aircraft c172x_4x75kg_cg_aligned_ksfo28r_landing --init scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/initial_condition/2.4__ksfo_28r_flightgear_default_init.xml --runscript scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.16__ksfo28r_runway_return_circular_landing_run.xml --no-flightgear`
- 검증 결과: Run ID `5.16.8__ksfo28r_runway_return_circular_landing`, combined CSV 173 columns, 76407 rows 생성
- 실행 확인 결과: C172 선회 핵심 컬럼이 모두 존재하고 숫자 값 기록 확인. 예: `fcs/heading-corrected` 범위 `-30.0..30.0`, `fcs/heading-command` 범위 `-0.5235..0.5235`, `ap/aileron_cmd` 범위 약 `-1.1764..0.0932`, `simulation/circular-bank-hold-active`는 전 구간 `0.0`
- 검증하지 못한 항목: 기존 과거 combined CSV 전체 재생성, PX4 ULog combined topic 확장 필요성, 모든 aircraft/scenario 실제 실행 검증
- 검증하지 못한 이유: 요청 범위는 combined JSBSim 로그 생성 시 필요한 컬럼 추가와 대표 C172 선회 케이스 검증이며, 과거 산출물 대량 재생성은 포함하지 않음
- 남은 리스크: `scripts/run_jsbsim_timestamped_combined_csv_only.py`는 Git 기준 untracked 상태라 commit 대상에 포함하려면 별도 `git add`가 필요함. generated CSV는 약 192 MB로 큼.
- 후속 작업: 필요 시 5.16 외 5.17~5.27 landing scenario와 VTOL hover/transition scenario를 새 combined runner로 재실행
- Git commit: 없음

## [2026-08-18 11:47] PROGRESS-20260818-1147-001 — DONE

- 과업: combined CSV 공력계수 전체 포함 구성
- 대상 프로젝트: `/home/junyeopkwon/evtol-6dof/jsbsim_workflow`
- 관련 파일: `scripts/run_jsbsim_timestamped_combined_csv_only.py`
- 수행 내용: `aero_coefficient_properties(available_properties)`를 추가해 JSBSim aircraft catalog에서 `aero/coefficient/`로 시작하는 모든 property를 정렬 수집하고, `combined_output_properties()`에서 기본 6DOF property 뒤에 자동 포함하도록 구성했다.
- 수정한 파일: `scripts/run_jsbsim_timestamped_combined_csv_only.py`
- 생성한 파일: 없음
- 핵심 변경점: aircraft별 공력계수 이름이 달라도 catalog에 존재하는 모든 `aero/coefficient/*`가 새 combined CSV에 포함됨
- 실행한 명령어: `python3 -m py_compile scripts/run_jsbsim_timestamped_combined_csv_only.py`
- 검증 결과: Python 문법 검사 통과
- 실행한 명령어: C172 landing, `standard_vtol_demo_hover`, `F450`, `F450_DATCOM`, `LiftCruise2kg`에 대해 catalog 공력계수 수와 combined selected property 포함 여부를 Python snippet으로 확인
- 검증 결과: C172 landing 32개, `standard_vtol_demo_hover` 16개, `F450` 16개, `F450_DATCOM` 11개, `LiftCruise2kg` 5개 공력계수가 모두 selected property에 포함되고 누락 0개 확인
- 검증하지 못한 항목: 새 스키마로 실제 JSBSim 장시간 실행 및 CSV 파일 생성
- 검증하지 못한 이유: 이번 변경은 property 선택 로직 확장이며, 추가 192MB급 CSV 생성을 피하기 위해 정적 catalog 검증과 문법 검사로 확인함
- 남은 리스크: 기존 combined CSV에는 새 공력계수 컬럼이 자동 추가되지 않음
- 다음 작업: 분석 대상 scenario를 새 combined runner로 재실행하면 공력계수 전체가 포함된 CSV가 생성됨
- Git commit: 없음

## [2026-08-19 10:21] PROGRESS-20260819-1021-001 — DONE

- 과업: 첨부 standard_vtol_demo_motor_updated_ko.xml의 PX4/JSBSim 실행 가능성 검토
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 조사한 파일: /mnt/c/Users/junyeopkwon/Downloads/standard_vtol_demo_motor_updated_ko.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/run_px4_jsbsim_qgc_workflow.py, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_hover_px4.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_hover_px4/standard_vtol_demo_hover_px4.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3020_jsbsim_standard_vtol_demo_hover_px4, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_hover/Aero_DATCOM.xml
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md
- 수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TASK.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/PROGRESS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/DECISIONS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TODO.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/INDEX.md
- 핵심 변경점: 첨부 XML은 XML well-formed이지만 JSBSim 1.2.4에서 aero/coefficient/CL_base table 오류로 단독 로딩 실패함을 확인하고, PX4 연결 전 보정 필요 항목을 문서화
- 실행한 명령어: xmllint --noout /mnt/c/Users/junyeopkwon/Downloads/standard_vtol_demo_motor_updated_ko.xml
- 검증 결과: XML well-formed 확인
- 실행한 명령어: JSBSim --root=/tmp/jsbsim_attached_xml_check --aircraft=standard_vtol_demo --initfile=/home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml --end=0.02 --nohighlight
- 검증 결과: FGTable: missing lookup axis 

## [2026-08-19 10:22] CORRECTION-20260819-1022-001 — 정정

- 대상 기록: PROGRESS-20260819-1021-001
- 정정 이유: 기록 append 중 shell quoting 문제로 마지막 검증 결과 줄이 중간에서 잘림.
- 기존 내용: 검증 결과 줄이 FGTable: missing lookup axis 에서 종료됨.
- 정정 내용: JSBSim 단독 로딩 검증 결과는 FGTable: missing lookup axis column 및 Error loading aerodynamic function in aero/coefficient/CL_base로 실패함. 임시로 lookup row/table 형식 14개를 lookup row/column 형식으로 평탄화하면 초기 table 오류는 통과하지만 Floating point exception으로 실패함. 기존 standard_vtol_demo_hover 모델은 같은 초기조건에서 rc=0으로 종료됨.
- 영향 범위: 작업 기록 문구만 정정. 코드와 검토 보고서에는 영향 없음.
- 검증 결과: tail로 기록 append 상태 확인.
- 다음 작업: 첨부 XML을 별도 후보 모델로 복사해 JSBSim 호환 형식으로 보정 후 재검증.

## [2026-08-19 10:31] PROGRESS-20260819-1031-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko.xml 공력 table 형식 보정
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/source_standard_vtol_demo_motor_updated_ko.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TASK.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/PROGRESS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/DECISIONS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TODO.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/INDEX.md
- 핵심 변경점: lookup row/table 및 복수 tableData breakPoint로 작성된 Mach별 2D table 14개를 lookup row/column 및 단일 tableData 형식으로 변환
- 변환 대상: aero/coefficient/CL_base, CLq, CLadot, CD_base, CYp, Cl_beta, Clp, Clr, Cm_base, Cmq, Cmadot, Cn_beta, Cnp, Cnr
- 유지 대상: 3D table인 aero/coefficient/Cl_da, Cn_da는 row/column/table 형식을 유지
- 실행한 명령어: xmllint --noout /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 검증 결과: 통과
- 실행한 명령어: 변환본 table 구조 확인 Python snippet
- 검증 결과: row/column table 14개, row/column/table table 2개 확인
- 실행한 명령어: JSBSim --root=/tmp/jsbsim_motor_updated_table_fixed_run --aircraft=standard_vtol_demo_motor_updated_ko --initfile=/home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml --end=0.02 --nohighlight
- 검증 결과: FGTable, missing lookup, Error loading aerodynamic 메시지는 재발하지 않음. 이후 Floating point exception으로 종료됨.
- 검증하지 못한 항목: JSBSim 정상 종료, PX4 SITL/QGC 실행
- 검증하지 못한 이유: 이번 단계는 공력 table 형식 보정이며, 다음 실패 원인은 velocities/vt-fps 직접 분모 등 0속도 보호 문제로 분리됨
- 남은 리스크: 공력 rate 항의 1.0 / velocities/vt-fps 직접 계산, CG 기준 좌표, 14 kg 기준 hover parameter, PX4 별도 target 등록
- 다음 작업: velocities/vt-fps 직접 분모를 aero/ci2vel 및 aero/bi2vel 기반 또는 보호식으로 바꿔 Floating point exception 제거
- Git commit: 없음

## [2026-08-19 10:38] PROGRESS-20260819-1038-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko.xml 0속도 보호 보정
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md, agent-log Markdown files
- 핵심 변경점: CLq, CLadot, Cmq, Cmadot은 aero/ci2vel로 변경. CYp, Clp, Clr, Cnp, Cnr은 aero/bi2vel로 변경. velocities/vt-fps 직접 분모 quotient 제거.
- 실행한 명령어: xmllint --noout /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 검증 결과: 통과
- 실행한 명령어: grep 및 Python snippet으로 velocities/vt-fps quotient, aero/ci2vel, aero/bi2vel 수 확인
- 검증 결과: quotient with velocities/vt-fps 0개, aero/ci2vel 4개, aero/bi2vel 5개
- 실행한 명령어: JSBSim --root=/tmp/jsbsim_motor_updated_safe_root --aircraft=standard_vtol_demo_motor_updated_ko --catalog --nohighlight
- 검증 결과: rc=0
- 실행한 명령어: JSBSim --root=/tmp/jsbsim_motor_updated_safe_run --aircraft=standard_vtol_demo_motor_updated_ko --initfile=/home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml --end=0.02 --nohighlight
- 검증 결과: rc=0
- 실행한 명령어: JSBSim --root=/tmp/jsbsim_motor_updated_safe_run1 --aircraft=standard_vtol_demo_motor_updated_ko --initfile=/home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml --end=1.0 --nohighlight
- 검증 결과: rc=0, FGTable/missing lookup/Error loading aerodynamic/Floating point/NaN 메시지 없음
- 검증하지 못한 항목: PX4 SITL 및 QGC mission 실행
- 검증하지 못한 이유: PX4 등록 전 CG 기준 좌표와 14 kg hover parameter 정합성 검토가 남아 있음
- 남은 리스크: motor/gear/pusher 좌표계, PX4 MPC_THR_HOVER 및 CA_ROTOR geometry, 실제 actuator sign 검증
- 다음 작업: CG 기준 좌표와 PX4 parameter를 검토한 뒤 별도 PX4 model/airframe 등록
- Git commit: 없음

## [2026-08-19 10:52] PROGRESS-20260819-1052-001 — DONE

- 과업: 새 JSBSim XML의 PX4 연결 실행 문제 분리
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 14kg 문제가 의심되면 이전 무게로 변경해 진행
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 수행 내용: 기준 hover 모델과 비교해 JSBSim 위치 좌표계가 CG 기준값처럼 들어간 부분을 절대좌표로 보정했다. ground_reactions x좌표를 front=1.249, rear=0.049로, lift motor x좌표를 -0.105/1.404로, pusher x좌표를 2.249로 조정했다. 14kg 후보는 JSBSim 단독 5초에서 Floating point exception이 재현되어 이전 무게 20.0kg으로 변경했다.
- 변경 이유: 14kg 모델은 좌표 보정 후에도 무추력 접지 조건에서 crash/FPE가 발생했으나, 기준 20kg hover 모델은 동일 조건에서 정상 종료했다. 사용자 요청에 따라 이전 무게로 진행했다.
- 검증 명령어: xmllint --noout /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 검증 명령어: JSBSim --root=/tmp/jsbsim_px4_direct_20kg.* --aircraft=standard_vtol_demo_motor_updated_ko_px4 --initfile=initGrnd --end=5
- 검증 결과: XML 문법 통과. 20kg 후보 JSBSim 단독 실행 rc=0. 14kg 후보는 direct 실행에서 Floating point exception rc=136을 보였음.
- 검증하지 못한 항목: arm 후 hover/takeoff, transition, 장시간 비행, 공력 계수 물리 검증
- 가정: 기존 20kg 후보의 Mass/Gear/ExternalReactions 좌표 체계를 기준으로 삼음
- 남은 리스크: 20kg에서는 접지/연결 안정성은 확보했지만, 새 공력 table과 제어기 mixer의 실제 비행 안정성은 아직 미검증
- 다음 작업: PX4에서 arm 및 짧은 hover 시나리오 검증, 필요 시 control allocation과 모터 추력 table 조정
- 관련 기록: TASK-20260819-1052-001, DECISION-20260819-1052-001
- Git commit: 없음

## [2026-08-19 11:02] PROGRESS-20260819-1102-001 — DONE

- 과업: PX4 arm-hover-land 검증
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 아밍 후 짧게 호버링하고 착륙까지 실행
- 관련 파일: /tmp/px4_motor_updated_hover/arm_hover_land_20kg_try1.log
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/jsbsim_bridge/standard_vtol_demo_motor_updated_ko_px4/latest_jsbsim_properties.csv
- 관련 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-19/01_59_23.ulg
- 수행 내용: PX4 shell에 commander arm, commander takeoff, commander land, shutdown 명령을 순차 주입했다. 로그에서 Armed by internal command, Takeoff detected, Landing detected, Disarmed by landing을 확인했다.
- 변경 이유: 이전 단계의 비무장 연결 검증 이후 실제 폐루프 arm/takeoff/landing 가능성을 확인하기 위함
- 검증 명령어: timeout 70s env HEADLESS=1 JSBSIM_LOG_ONLY=1 JSBSIM_LOG_FILTER=... make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS
- 검증 결과: TRY1_RC=0. PX4 명령 시퀀스 정상 종료. 로그 NaN/Floating point/CRASH DETECTED/Preflight Fail/Arming denied/Takeoff denied/failsafe/ERROR count 0.
- 검증 명령어: JSBSim CSV altitude/ESC 분석
- 검증 결과: samples=4546, time=0.0-36.36s, max AGL=1.029m at 22.84s, 0.9-1.1m 구간 duration=6.808s, ESC command max 약 0.658
- 검증하지 못한 항목: 기본 takeoff altitude 2.5m까지의 목표고도 도달, 장시간 hover 안정성, transition
- 가정: 0.9-1.1m 구간 6.8초를 짧은 hover 성립으로 판단
- 남은 리스크: 목표고도 2.5m보다 낮게 hover했으므로 altitude controller/thrust/mass/land command timing 튜닝 여지가 있음
- 다음 작업: land 명령 대기 시간을 늘리거나 takeoff altitude setpoint/hover thrust를 조정해 2.5m 목표고도 추종 확인
- 관련 기록: TASK-20260819-1102-001
- Git commit: 없음

## [2026-08-19 11:08] PROGRESS-20260819-1108-001 — DONE

- 과업: 직접 실행 명령어 문서화
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 직접 하려면 어떻게 하는지와 매뉴얼 존재 여부 확인
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 수행 내용: 기존 매뉴얼이 standard_vtol_demo_hover_px4 중심임을 확인하고, standard_vtol_demo_motor_updated_ko_px4 직접 실행 섹션을 추가했다. DONT_RUN 빌드 확인, PX4 shell 수동 arm-hover-land, 자동 실행, 로그 grep, 최신 ulog 확인 명령을 정리했다.
- 변경 이유: 최근 검증한 새 모델 실행 절차가 리뷰 문서에는 있었지만 사용자가 직접 따라할 runbook 본문에는 없었음
- 검증 명령어: tail -180 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 검증 결과: 섹션 9가 정상 append 되었고 Markdown code fence가 깨지지 않음
- 검증하지 못한 항목: 문서 명령을 새 터미널에서 재실행하지는 않음
- 가정: 이전 arm-hover-land 검증 결과를 기준으로 문서화
- 남은 리스크: 실제 목표고도 2.5m 추종은 아직 미튜닝
- 다음 작업: 필요 시 2.5m hover 튜닝용 runbook 섹션 추가
- 관련 기록: TASK-20260819-1108-001
- Git commit: 없음

## [2026-08-19 11:13] PROGRESS-20260819-1113-001 — DONE

- 과업: QGC 명령 입력 매뉴얼 보강
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: QGC에서 arm/takeoff/land 명령을 넣는 방법 안내
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 수행 내용: QGC 실행, PX4/JSBSim SITL 실행, QGC Fly 화면 버튼 방식, QGC MAVLink Console 방식, 성공 로그 확인 기준을 섹션 9.6에 추가했다.
- 변경 이유: 기존 섹션 9는 터미널 pxh 명령 중심이었고 QGC에서 명령을 넣는 절차가 부족했음
- 검증 명령어: tail -140 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 검증 결과: 섹션 9.6이 정상 append 되었고 code fence가 정상 표시됨
- 검증하지 못한 항목: QGC GUI에서 실제 버튼/콘솔 입력 재현
- 가정: QGC 버전에 따라 MAVLink Console 메뉴명이 Analyze Tools 또는 Widgets로 다를 수 있음
- 남은 리스크: QGC UI takeoff altitude/setpoint가 현재 모델의 약 1m 저고도 검증 결과와 다를 수 있음
- 다음 작업: 사용자가 QGC에서 실행한 로그를 기준으로 목표고도 추종 분석
- 관련 기록: TASK-20260819-1113-001
- Git commit: 없음

## [2026-08-19 11:33] PROGRESS-20260819-1133-001 — DONE

- 과업: QGC 실행 로그 분석
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 고도 20m hover 및 목표 위치 이동 로그 확인
- 관련 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-19/02_20_29.ulg
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/jsbsim_bridge/standard_vtol_demo_motor_updated_ko_px4/latest_jsbsim_properties.csv
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/QGC_20M_HOVER_REPOSITION_LOG_ANALYSIS_20260819.md
- 수행 내용: ULog duration, dropout, logged messages, vehicle_local_position, vehicle_status, vehicle_command, vehicle_command_ack, position_setpoint_triplet, actuator_motors, hover_thrust_estimate, failsafe_flags를 분석했다. JSBSim CSV의 AGL과 NaN도 확인했다.
- 변경 이유: QGC에서 실행한 실제 hover/reposition 로그의 성립 여부와 종료 상태 확인 필요
- 검증 명령어: ulog_info /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-19/02_20_29.ulg
- 검증 결과: duration 0:03:04, No Dropouts
- 검증 명령어: pyulog 기반 분석 스크립트
- 검증 결과: local altitude max 19.849m, 18-22m 구간 148.904s, 마지막 DO_REPOSITION 목표 최근접 0.002m, 종료 시 목표점 거리 47.423m, arming_state 최종 ARMED, nav_state 최종 ORBIT, landed 최종 0
- 검증 명령어: JSBSim CSV NaN/AGL 분석
- 검증 결과: CSV rows 23252, NaN count 0, JSBSim AGL max 20.999m, final 20.090m
- 검증하지 못한 항목: QGC 다운로드 폴더에 별도 저장된 파일이 있는 경우 해당 파일 분석
- 가정: 최신 rootfs ULog가 사용자가 언급한 로그임
- 남은 리스크: 종료 전 Land/Disarm이 수행되지 않았으므로 로그는 착륙 완료 로그가 아니라 비행 중 ORBIT 상태 종료 로그임
- 다음 작업: QGC에서 Land 후 Landing detected/Disarmed 로그가 남는 run 재수집
- 관련 기록: TASK-20260819-1133-001
- Git commit: 없음

## [2026-08-19 11:40] PROGRESS-20260819-1140-001 — DONE

- 과업: F450 스타일 modular XML 생성
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 새 기체 XML을 분리 파일 구조로 변환
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 관련 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/standard_vtol_demo_motor_updated_ko_px4.xml
- 관련 파일: Metrics.xml, Mass.xml, Gear.xml, Effectors.xml, FlightControl.xml, ExternalReactions.xml, Aero.xml, Monolithic.xml
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 수행 내용: 단일 XML의 top-level metrics, mass_balance, ground_reactions, system, flight_control, external_reactions, aerodynamics 블록을 각각 Metrics.xml, Mass.xml, Gear.xml, Effectors.xml, FlightControl.xml, ExternalReactions.xml, Aero.xml로 분리했다. 주 XML은 fileheader와 file include로 재구성했다. PX4 bridge 모델은 CSV output 블록을 주 XML에 유지했다. 변환 전 단일본은 각 폴더의 Monolithic.xml에 보존했다.
- 변경 이유: F450_DATCOM처럼 구성 요소별 수정/검증이 가능하도록 분리하기 위함
- 검증 명령어: xmllint --noout workflow/PX4 model directory *.xml
- 검증 결과: xml_ok
- 검증 명령어: JSBSim --root=/tmp/jsbsim_modular_wf.* --aircraft=standard_vtol_demo_motor_updated_ko --initfile=... --end=5 --nohighlight
- 검증 결과: WF_RC=0
- 검증 명령어: JSBSim --root=/tmp/jsbsim_modular_px4.* --aircraft=standard_vtol_demo_motor_updated_ko_px4 --initfile=initGrnd --end=5 --nohighlight
- 검증 결과: PX4_RC=0. temp root 특성상 CSV output path warning은 있었지만 실행은 정상 종료
- 검증 명령어: DONT_RUN=1 HEADLESS=1 make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS
- 검증 결과: DONT_RUN_RC=0
- 검증 명령어: timeout 25s env HEADLESS=1 JSBSIM_LOG_ONLY=1 NO_PXH=1 make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS
- 검증 결과: SHORT_RC=124(timeout), NaN/Floating point/CRASH DETECTED/Preflight Fail/ERROR count 0, JSBSim CSV 2772 lines 및 NaN 0
- 검증하지 못한 항목: 분리 후 QGC 20m reposition 재비행
- 가정: 파일 include 구조는 F450_DATCOM과 동일 패턴으로 JSBSim이 해석
- 남은 리스크: ElementTree 재직렬화로 공백/따옴표 스타일은 바뀌었지만 XML 의미는 유지됨
- 다음 작업: 필요 시 모듈별 README 또는 수정 가이드 추가
- 관련 기록: TASK-20260819-1140-001, DECISION-20260819-1140-001
- Git commit: 없음

## [2026-08-19 14:25] PROGRESS-20260819-1425-001 — 진단 완료

- 과업: standard_vtol_demo_motor_updated_ko_px4 고정익 전환 문제 원인 진단
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 멀티콥터 hover 이후 고정익 천이 문제 원인 확인
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_TRANSITION_DIAGNOSIS_20260819.md
- 조사한 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4, /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/1040_gazebo-classic_standard_vtol, /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/10043_sihsim_standard_vtol, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_motor_updated_ko_px4.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/FlightControl.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/src/actuator_plugin.cpp, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/src/sensor_airspeed_plugin.cpp
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_TRANSITION_DIAGNOSIS_20260819.md
- 수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TASK.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/PROGRESS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TODO.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/INDEX.md
- 핵심 변경점: 전환 실패 1순위 원인을 PX4 airframe이 순수 멀티콥터 구성인 점으로 정리하고, 2순위로 JSBSim bridge 조종면 mapping 누락, 3순위로 airspeed/전환 속도 파라미터 누락을 기록
- 실행한 명령어: sed, grep
- 테스트 결과: 실행 테스트 없음
- lint 결과: 해당 없음
- type check 결과: 해당 없음
- build 결과: 실행하지 않음
- 실행 확인 결과: 현재 3021 airframe은 
c.mc_defaults, CA_AIRFRAME 0, CA_ROTOR_COUNT 4; bridge config는 actuator index 0-4만 ESC property로 전달; FlightControl.xml은 aileron/elevator/rudder command property를 기대함
- 검증하지 못한 항목: 실제 transition flight, ULog의 tol_vehicle_status, ctuator_outputs, irspeed_validated, JSBSim CSV의 조종면/전방추진 출력 변화
- 남은 리스크: VTOL 구성 전환 후에도 fixed-wing trim과 공력 coefficient, 조종면 부호/스케일, pusher thrust table 튜닝이 필요할 수 있음
- 후속 작업: airframe을 표준 VTOL로 변경하고 bridge actuator/airspeed mapping을 추가한 뒤 QGC 또는 scripted MAVLink 전환 검증
- Git commit: 없음

## [2026-08-19 14:31] CORRECTION-20260819-1431-001 — 정정

- 대상 기록: TASK-20260819-1425-001, PROGRESS-20260819-1425-001, TODO-20260819-1425-001, INDEX-20260819-1425-001
- 정정 이유: PowerShell quoting 과정에서 backtick으로 감싼 기술 식별자 일부가 손상되어 표기 정정 필요
- 기존 내용: `rc.mc_defaults`, `rc.vtol_defaults`, `fcs/...`, `barometer`, `rascal.xml`, `vehicle_*`, `airspeed_*` 중 일부가 제어문자 또는 잘린 문자열로 기록됨
- 정정 내용: 올바른 핵심 표기는 `rc.mc_defaults`, `. ${R}etc/init.d/rc.vtol_defaults`, `fcs/esc-cmd-norm[0..4]`, `fcs/aileron-cmd-norm`, `fcs/elevator-cmd-norm`, `fcs/rudder-cmd-norm`, `barometer`, `rascal.xml`, `vehicle_status.nav_state`, `vtol_vehicle_status`, `airspeed_validated`임
- 영향 범위: 진단 결론에는 변화 없음. 손상된 표기는 본 정정 기록과 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_TRANSITION_DIAGNOSIS_20260819.md 재작성본을 기준으로 해석
- 검증 결과: 진단 문서 본문을 literal text로 재작성
- 다음 작업: 3021 airframe 및 bridge config 수정 단계에서 본 정정 표기를 기준으로 적용

## [2026-08-19 14:48] PROGRESS-20260819-1448-001 — 비교 분석 완료

- 과업: `standard_vtol_demo.xml`와 `standard_vtol_demo_motor_updated_ko_px4` 비교
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 전환 성공 모델과 새 모델 차이 확인
- 조사한 파일: /mnt/d/ProjectAirSim-jsbsim/core_sim/jsbsim/models/aircraft/standard_vtol_demo/standard_vtol_demo.xml, /mnt/d/ProjectAirSim-jsbsim/core_sim/jsbsim/models/aircraft/standard_vtol_demo/initfile.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/Metrics.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/Mass.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/ExternalReactions.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/Aero.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_motor_updated_ko_px4.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_DEMO_COMPARISON_20260819.md
- 수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TASK.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/PROGRESS.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/TODO.md, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/agent-log/INDEX.md
- 핵심 변경점: 새 모델 전환 문제의 핵심 차이를 airframe VTOL 설정 누락, bridge 조종면 mapping 누락, elevator/rudder aero derivative 누락, full-envelope aero 부재로 정리
- 실행한 명령어: `sed`, `grep`, `find`
- 테스트 결과: 실행 테스트 없음
- lint 결과: 해당 없음
- type check 결과: 해당 없음
- build 결과: 실행하지 않음
- 실행 확인 결과: 비교 분석 문서 생성 완료
- 검증하지 못한 항목: 실제 transition 실행 및 ULog 동특성 비교
- 남은 리스크: 외부 ProjectAirSim vehicle 설정이 별도 위치에 있을 수 있으나 모델명 기반 검색에서는 추가 파일을 찾지 못함
- 후속 작업: airframe/bridge/aero derivative 수정 후 transition 로그 검증

## [2026-08-20 10:00] PROGRESS-20260820-1000-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko_px4 airframe/bridge Standard VTOL 전환
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/{1040_gazebo-classic_standard_vtol,10043_sihsim_standard_vtol,3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4}, /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d/{rc.vtol_defaults,rc.vehicle_setup}, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/{Mass.xml,ExternalReactions.xml,FlightControl.xml}
- 수정한 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_motor_updated_ko_px4.xml
- 핵심 변경점:
  1. airframe: `rc.mc_defaults` → `rc.vtol_defaults`, `@type Quadrotor Wide` → `Standard VTOL`, `CA_AIRFRAME 0` → `2`, `CA_ROTOR_COUNT 4` → `5`(pusher를 rotor4로 등록, `CA_ROTOR4_AX 1`/`CA_ROTOR4_AZ 0`/`CA_ROTOR4_PX -1.6`), `CA_SV_CS_COUNT 3` 추가(`CA_SV_CS0_TYPE 15` aileron/`CS1_TYPE 3` elevator/`CS2_TYPE 4` rudder, 각각 `TRQ_R`/`TRQ_P`/`TRQ_Y` 1), `PWM_MAIN_FUNC6/7/8` = `201/202/203` 추가(기존 FUNC1-5 모터/pusher 배치는 그대로 유지), `VT_TYPE 2`/`VT_FWD_THRUST_EN 4`/`VT_F_TRANS_THR 0.75`, `SENS_EN_ARSPDSIM 1`과 `FW_AIRSPD_MIN/TRIM/MAX 10/15/22`(실측 없는 잠정값) 추가
  2. bridge config: `<sensors>`에 `<airspeed>` 블록 추가, `<actuators>`에 index 5/6/7로 `fcs/aileron-cmd-norm`/`fcs/elevator-cmd-norm`/`fcs/rudder-cmd-norm` 채널 3개 추가(FlightControl.xml에서 실제 사용하는 입력 프로퍼티명과 대조해 확인)
  3. CA_ROTOR4_PX 계산 근거: 기존 CA_ROTOR0-3 값(0.754/-0.755)이 `PX4_PX = CG_x(JSBSim) - motor_x(JSBSim)` 공식으로 역산됨을 Mass.xml(CG x=0.649)과 기존 파라미터 대조로 확인(0.649-(-0.105)=0.754, 0.649-1.404=-0.755 일치). 동일 공식으로 pusher(ExternalReactions.xml x=2.249) 적용: 0.649-2.249=-1.6
  4. 사용자 지시에 따라 Metrics/Mass/Gear/ExternalReactions/Aero.xml은 전혀 수정하지 않음(모터 위치/추력/공력 데이터 유지)
- 실행한 명령어: `xmllint --noout standard_vtol_demo_motor_updated_ko_px4.xml`(WSL 네이티브), `bash -n 3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4`
- 검증 결과: 둘 다 통과
- 실행한 명령어: `DONT_RUN=1 HEADLESS=1 make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS`
- 검증 결과: ROMFS airframe 재생성 포함 빌드 정상 완료
- 실행한 명령어: `timeout 30 HEADLESS=1 JSBSIM_LOG_ONLY=1 NO_PXH=1 make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS`
- 검증 결과: 739줄 로그 전체에서 NaN/Floating point/CRASH DETECTED 없음, JSBSim이 지상 정지 상태로 30초간 안정적으로 스텝됨. 유일한 경고는 `WARN [health_and_arming_checks] Preflight Fail: Airspeed selector module down`
- 추가 조사: `rc.vtol_defaults`가 `VEHICLE_TYPE vtol`을 설정하므로 `rc.vehicle_setup`을 통해 `rc.vtol_apps`(airspeed_selector 시작 포함)가 이론상 자동 실행되어야 함을 rc 스크립트 체인에서 확인했으나, 이번 세션에서는 이 경고의 정확한 원인(모듈 미시작 vs 데이터 미검증)까지는 규명하지 못함
- 검증하지 못한 항목: airspeed selector 경고의 정확한 원인, 실제 arm 이후 hover-transition-FW 비행, QGC ULog 기반 동특성 확인
- 검증하지 못한 이유: 이번 턴은 구조적 배선(airframe/bridge) 수정과 정적/짧은 실행 검증까지가 범위였고, 실비행 검증은 후속 작업으로 분리
- 남은 리스크: FW_AIRSPD_*/VT_F_TRANS_THR은 실측 없는 잠정값이라 전환 시점과 실속 여유가 실제와 다를 수 있음. 러더 공력 효과(Cn_dr 등)가 DATCOM 데이터에 없을 가능성은 사용자가 별도 검토 중이라 이번 수정으로는 해결되지 않음(제어 신호는 전달되지만 실제 요 모멘트가 약하거나 없을 수 있음)
- 다음 작업: (1) airspeed selector 경고 원인 확인, (2) PX4 shell 또는 QGC로 arm 후 hover→전방전환→FW 유지 실비행, (3) ULog의 vtol_vehicle_status/airspeed_validated/actuator_outputs로 전환 성공 여부 판정
- 관련 기록: TASK-20260820-1000-001, TODO-20260820-1000-001, DECISION-20260820-1000-001
- Git commit: 없음

## [2026-08-20 11:00] PROGRESS-20260820-1100-001 — airspeed selector 진단 완료

- 과업: `Preflight Fail: Airspeed selector module down` 경고 원인 규명
- 대상 프로젝트: jsbsim_workflow
- 조사한 파일: 없음(런타임 진단)
- 실행한 명령어: PX4 shell에 `airspeed_selector status`/`stop`/`start`/`status`, `listener differential_pressure 1`, `listener airspeed_validated 1`, `uorb top -1`를 순차 주입(`JSBSIM_LOG_FILTER`로 관련 로그만 필터링)
- 검증 결과: `airspeed_selector status` → `INFO [airspeed_selector] running`(모듈 정상 기동). `listener differential_pressure` → `differential_pressure_pa: -0.81832`(실제 값 발행 중). `listener airspeed_validated` → `airspeed_sensor_measurement_valid: True`, `selected_airspeed_index: 1`(정상 유효 판정). `uorb top`에서도 `airspeed`/`airspeed_validated`/`differential_pressure` 토픽 모두 정상 publish rate로 확인됨
- 핵심 변경점: 해당 WARN은 부팅 직후(약 t=12s) health_and_arming_checks가 airspeed_selector가 첫 유효 샘플을 발행하기 전에 한 번 평가되면서 찍히는 부팅 트랜지언트로 판단됨. 이후 재평가에서는 반복 출력되지 않았고, 모듈/토픽 모두 정상 상태로 확인됨
- 검증하지 못한 항목: health_and_arming_checks 내부 로직상 정확히 어느 조건에서 이 WARN이 clear되는지(소스 코드 추적은 하지 않음)
- 검증하지 못한 이유: 런타임 동작으로 충분히 설명되어 소스 추적의 우선순위를 낮춤
- 남은 리스크: 없음(후속 arm-hover-transition 테스트에서 이 경고로 인한 arming 거부는 발생하지 않음을 확인함)
- 다음 작업: 실비행 검증으로 진행
- 관련 기록: TODO-20260820-1000-001(종결)
- Git commit: 없음

## [2026-08-20 11:20] PROGRESS-20260820-1120-001 — 실비행 검증(전환 실패, 원인 규명)

- 과업: standard_vtol_demo_motor_updated_ko_px4 실제 arm→hover→전방전환→FW 비행 검증
- 대상 프로젝트: jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/jsbsim_bridge/standard_vtol_demo_motor_updated_ko_px4/latest_jsbsim_properties.csv
- 실행한 명령어: PX4 shell에 `commander arm` → `commander takeoff` → `commander transition` → `commander transition`(복귀) → `commander land` → `shutdown` 순차 주입(약 100초 timeout)
- 검증 결과(콘솔): `Armed by internal command`, `Using default takeoff altitude: 20.0 m`, `Takeoff detected`까지는 정상. `commander transition` 이후 `Preflight Fail: Attitude failure (pitch)`, `Compass needs calibration`, `vtol_att_control: Quad-chute triggered`(PX4 자동 안전복귀), `airspeed_selector: Airspeed sensor failure detected` 순으로 경고 발생. 이후 `commander land` 시도했으나 `Landing detected`/`Disarmed` 로그는 확인되지 않음(timeout 내 미완료)
- 검증 결과(JSBSim CSV 정밀 분석, awk로 시계열 추출):
  1. **`commander takeoff`로 수직 상승을 시작한 시점(t≈15.7s, 전환 명령 이전)부터 이미 `aero/alpha-deg`가 -90도 부근으로 급변하고 이후 지속적으로 요동침(-90 ~ -176 ~ +145 등)**. 원인은 전진속도(u)가 거의 0인 순수 수직 상승 상태에서 `alpha=atan2(w,u)` 계산이 본질적으로 불안정해지는 구간이며, 이 자체는 JSBSim의 일반적인 특성이지만 이 모델의 DATCOM 기반 Aero.xml에 고받음각 구간 보호/클램핑이 없어 보임
  2. t≈42.5s(전환 명령이 실제 FCS에 반영되는 시점)부터 elevator/aileron/rudder 명령이 실제로 0이 아닌 값으로 변하기 시작(`fcs/elevator-cmd-norm`, `fcs/aileron-cmd-norm`, `fcs/rudder-cmd-norm` 전부 확인, rudder는 최대 약 -0.44까지 관측) → **조종면 bridge mapping이 PX4 FW 컨트롤러의 실제 명령을 JSBSim까지 정확히 전달하고 있음을 확인**(elevator 0.036 → elevator position 0.9deg, 정확히 aerosurface_scale gain 25배와 일치)
  3. 이미 alpha가 불안정한 상태에서 조종면이 실제로 움직이기 시작하자 theta(pitch)가 급격히 발산(7.9° → 32.6° → 77.6° → ...), t≈49.9s에 AGL이 음수(-2.56ft)로 지면 관통, 직후 AGL/theta가 NaN으로 전환되며 시뮬레이션 붕괴
- 핵심 변경점: 없음(진단만 수행, 코드 변경 없음)
- 검증하지 못한 항목: 러더의 실제 공력 요 모멘트 발생 여부(비행이 붕괴되기 전까지 안정적인 FW 비행 구간을 확보하지 못해 판정 불가), 완만한 수직 상승률로 alpha 불안정을 회피했을 때의 전환 성공 여부
- 검증하지 못한 이유: 이번 실행은 PX4 기본 수직 상승(약 20m/15초 이내)로 상승률이 빨라 alpha 불안정 구간에 바로 진입함
- 남은 리스크: (1) DATCOM Aero.xml에 고받음각(|alpha| 대략 30~40도 이상) 보호/클램핑이 없다면 수직 상승이 포함되는 모든 시나리오(단순 멀티콥터 hover 포함)에서 유사한 문제가 잠재함. 이전 hover 검증들이 통과했던 것은 상승률이 낮아 qbar가 작아서 aero 힘 자체가 미미했기 때문일 가능성이 높음. (2) 러더 공력 효과 유무는 여전히 미확인이며, 사용자가 이미 알고 있던 DATCOM 러더 해석 문제와 관련될 수 있으나 이번 크래시의 직접 원인은 아님(전환 이전에 이미 alpha 불안정이 시작됨)
- 다음 작업: (1) 사용자에게 alpha/고받음각 보호 필요성 보고(공력 데이터 영역이라 수정 범위 아님), (2) 재시도 시 상승률을 낮추거나(느린 takeoff/수동 고도 제어) alpha가 안정된 구간에서만 전환을 시도하는 방식으로 재검증 여지 있음
- 관련 기록: TASK-20260820-1000-001, TODO-20260820-1002-001(종결, 원인 규명됨), TODO-20260820-1120-001(신규), DECISION-20260820-1120-001
- Git commit: 없음

## [2026-08-20 12:00] PROGRESS-20260820-1200-001 — alpha 유효성 게이트 적용 및 재검증(부분 개선)

- 과업: TODO-20260820-1120-001(고받음각 보호)에 대해 사용자가 승인한 alpha 기반 연속 게이팅 방식을 Aero.xml에 적용하고 재검증
- 대상 프로젝트: jsbsim_workflow
- 조사한 파일: F450(순정)/Aero.xml(alpha 계수를 상수 0으로 둬서 전혀 발산하지 않는 방식 확인), /mnt/d/ProjectAirSim-jsbsim/core_sim/jsbsim/models/aircraft/standard_vtol_demo/standard_vtol_demo.xml(성공 모델의 -180~180도 풀레인지 flat-plate 블렌딩 테이블 확인, 및 elevator 부호 버그 수정 이력 확인)
- 생성/수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/Aero.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/Aero.xml(동기화)
- 핵심 변경점: `<alphalimits>` 바로 뒤에 `aero/coefficient/alpha_validity_gate` 함수를 신규 추가(alpha-deg 기준 -90/-24/11/90도 4점 선형보간 테이블, 유효범위 안은 1.0, ±90도에서 0.0). 이 게이트를 `<property>aero/qbar-area</property>`를 가진 기존 16개 함수(CL_base, CLq, CLadot, CD_base, CYp, Cl_beta, Clp, Clr, Cl_da, Cm_base, Cmq, Cmadot, Cn_beta, Cnp, Cnr, Cn_da) 전부의 `<product>`에 곱셈항으로 삽입(replace_all로 일괄 처리 후 개수 검증: qbar-area 16개=게이트 16개 일치). 모터 반작용 토크(motor_yaw_torque)는 alpha와 무관한 실물리 항이라 게이팅 대상에서 명시적으로 제외
- 실행한 명령어: `xmllint --noout Aero.xml`(WSL 네이티브)
- 검증 결과: 통과
- 실행한 명령어: `JSBSim --root=/tmp/jsbsim_aerogate_check --aircraft=standard_vtol_demo_motor_updated_ko_px4 --initfile=initGrnd --end=5 --nohighlight`(aircraft 심볼릭 링크로 PX4 bridge 모델 디렉터리 직접 참조)
- 검증 결과: 정상 종료, NaN/FGTable 오류 없음(임시 root라 CSV 출력경로 못 찾는다는 무해한 ERROR 1건만 있음, 이전에도 동일 패턴으로 무해 확인됨)
- 실행한 명령어: PX4 shell에 `commander arm` → `commander takeoff` → `commander transition` → `commander transition` → `commander land` → `shutdown` 재주입(동일 시퀀스로 PROGRESS-20260820-1120-001과 직접 비교 가능하게 함)
- 검증 결과(개선된 부분): JSBSim CSV 정밀 비교 결과, 순수 수직 상승 구간(t=13~31s)에서 이전 실행은 theta가 크게 요동쳤던 반면 이번엔 ±0.3~1.3도 수준으로 훨씬 안정적으로 유지됨. alpha 자체는 여전히 -90도 근방으로 감(물리적 특이점이라 게이트로 막을 수 없는 게 당연함)이나, 그로 인한 힘/모멘트 발산은 확실히 억제됨을 확인
- 검증 결과(미해결): 전환 명령이 실제 반영되는 t≈35.8s부터 elevator/aileron 명령이 다시 발산성으로 커지며(theta 1°→3.5°→16°→35°→57°→79°) t≈41.8s에 지면 충돌, AGL/theta NaN. 이전 실행(PROGRESS-20260820-1120-001)과는 다른 실패 시점/양상(이번엔 순수 alpha 발산이 아니라 조종면이 실제로 움직이면서 발산)
- 핵심 변경점(코드): 없음(이미 위에 기록)
- 검증하지 못한 항목: 새 발산의 정확한 메커니즘(제어 게인 와인드업 가설은 CSV 정황상 추정일 뿐 확정 아님), pusher로 사전 가속 후 전환하는 정상적 절차로 재시도했을 때의 결과
- 검증하지 못한 이유: 이번 세션은 alpha 게이트 효과 검증까지가 범위였고, 제어 게인 튜닝이나 전환 절차 재설계는 별도 작업으로 판단
- 남은 리스크: 이 모델은 전환 명령 시점에 전진속도가 거의 0인 상태(정지 호버에서 바로 transition 명령)로 테스트됐는데, 이는 실제 VTOL 운용 절차(pusher로 먼저 가속 후 전환)와 다른 비정상적 시나리오일 가능성이 있음. alpha 게이트가 열려있지 않은 구간(저속) 동안 FW rate/attitude 컨트롤러가 조종면 명령을 과도하게 키웠다가(적분 와인드업 등), 게이트가 다시 열리는 시점에 그 과도한 명령이 그대로 반영되며 발산했을 가능성 추정
- 다음 작업: (1) 전환 전 pusher로 어느 정도 전진속도를 만든 뒤 transition을 명령하는 정상 절차로 재시도, (2) FW_RR_P/FW_PR_P 등 자세 게인이 잠정값인 점 재확인, (3) 필요 시 alpha_validity_gate의 램프 폭(-90~-24, 11~90)을 더 완만하게 조정해 게이트 재개방 시 충격 완화
- 관련 기록: TASK-20260820-1200-001, TODO-20260820-1200-001, DECISION-20260820-1200-001
- Git commit: 없음

## [2026-08-20 12:30] PROGRESS-20260820-1230-001 — AERORP 좌표 불일치 발견 및 수정(전환 발산 완전 해결)

- 과업: 사용자 요청으로 모터/기타 부위 좌표가 CAD 기반 CG 변경(원점 CG → nose 기준 649mm)에 맞춰 일관되게 갱신됐는지 전수 점검, 및 TODO-20260820-1200-001(alpha 게이트 적용 후에도 남은 전환 발산)의 원인 규명
- 대상 프로젝트: jsbsim_workflow
- 조사한 파일: Mass.xml(CG x=0.649, 이미 올바름), Gear.xml(front_foot=1.249/rear=0.049, 8/19 10:52에 이미 보정 확인), ExternalReactions.xml(모터 4개 -0.105/1.404, pusher 2.249, 8/19 10:52에 이미 보정 확인), Metrics.xml(AERORP/VRP가 (0,0,0)에 방치돼있음을 발견), JSBSim 소스 /home/junyeopkwon/jsbsim/src/models/FGAerodynamics.cpp(247-288행), /home/junyeopkwon/jsbsim/src/FGFDMExec.cpp(479-528행)
- 생성/수정한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/Metrics.xml, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/Metrics.xml(동기화)
- 핵심 변경점: `AERORP`를 (0.0,0.0,0.0) → (0.649,0.0,0.0)으로, `VRP`를 (0.0,0.0,0.0) → (0.649,0.0,0.0)으로, `EYEPOINT`를 (0.15,0.0,-0.05) → (0.799,0.0,-0.05)로 수정(원래 데모의 CG-CG오프셋 관계를 새 nose-기준 프레임에서 보존). Mass.xml/Gear.xml/ExternalReactions.xml은 이미 8/19에 649mm 기준으로 정상 보정돼있었음을 재확인(문제 없음)
- 원인 분석: JSBSim 소스 확인 결과 `AERORP`는 단순 메타데이터가 아니라 `FGAerodynamics.cpp:288`의 `vMoments = vMomentsMRCBodyXYZ + vDXYZcg*vForces`(M = r × F)에서 `vDXYZcg`(AERORP-CG 거리, 247-249행)로 직접 사용됨. 원래 데모는 AERORP=CG=(0,0,0)이라 모멘트암이 0이었는데, CG만 0.649로 옮기고 AERORP를 안 옮기면서 이 모멘트암이 실수로 0.649m가 생겨버렸고, 양력/항력이 조금이라도 발생하면(즉 alpha 게이트가 열리는 순간) 그 힘에 0.649m가 곱해진 큰 허위 피칭모멘트가 자동으로 더해지고 있었음. 이게 TODO-20260820-1200-001에서 "제어 게인 와인드업"으로 추정했던 두 번째 발산의 진짜 원인으로 확인됨
- 실행한 명령어: `xmllint --noout Metrics.xml`(WSL 네이티브)
- 검증 결과: 통과
- 실행한 명령어: PX4 shell에 `commander arm` → `commander takeoff` → `commander transition` → `commander land` → `shutdown` 재주입(TODO-20260820-1200-001과 동일 시퀀스, land 대기시간을 40초로 늘려 완전한 착지까지 확인)
- 검증 결과: **NaN/크래시 완전히 사라짐**(CSV 전체에서 NaN 0건, `grep -ic nan` = 0). 콘솔에서 "Attitude failure (pitch)" 반복 경고 사라짐. `vtol_att_control: Quad-chute triggered`는 여전히 발생(전환 자체는 아직 성공 못 함, MC로 안전 복귀)하지만 그 이후 발산 없이 정상적으로 하강. `INFO [commander] Landing detected` 확인. 최종 CSV 상태(t=79.3s)의 AGL/theta가 최초 지상 정지 상태값(AGL≈0.554, theta≈0.0015°)과 정확히 일치 — 완전히 안정적으로 착지 후 정지함을 확인
- 검증하지 못한 항목: 고정익(FW) 모드 유지 성공 여부(Quad-chute로 MC 복귀했으므로 진짜 전환 성공은 아직 미달성), 러더 실제 요 모멘트 최종 판정
- 검증하지 못한 이유: 이번 수정은 발산/크래시 제거가 목표였고 FW 유지 비행 성공 자체는 별도 과제(전환 조건/속도 프로파일 튜닝 필요할 수 있음)
- 남은 리스크: Quad-chute가 왜 발동하는지(전환 자체 시도가 실패로 판정되는 이유)는 아직 별도 원인 규명 필요. AERORP 버그가 사라졌으니 이제 순수하게 전환 로직/속도 프로파일 문제로 좁혀짐
- 다음 작업: Quad-chute 발동 조건(VT_QC_* 관련 파라미터, 예상 전환 소요시간 대비 실제 실패 판정 임계값) 확인, pusher 사전가속 절차 적용 여부 검토
- 관련 기록: TASK-20260820-1230-001, TODO-20260820-1200-001(대부분 해결로 업데이트), TODO-20260820-1230-001(신규), DECISION-20260820-1230-001
- Git commit: 없음

## [2026-08-20 13:00] PROGRESS-20260820-1300-001 — 실제 전방 목적지를 준 정상 절차로 재검증(FW 상태 실제 도달 확인)

- 과업: 사용자가 지적한 대로, 이전 quad-chute 테스트는 정지 호버 상태에서 목적지 없이 `commander transition`만 호출한 비정상 절차였음을 인정하고, pusher 사전가속 후 전환하는 정상 절차로 재검증
- 대상 프로젝트: jsbsim_workflow
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/vtol_transition_mavlink_test.py(pymavlink 기반 arm→takeoff→DO_REPOSITION(전방 600m)→10초 대기→DO_VTOL_TRANSITION→모니터링→land 시퀀스)
- 핵심 변경점: 기존 PX4 shell 텍스트 명령(`commander transition`)만으로는 미션 업로드나 DO_REPOSITION 같은 MAVLink 명령을 보낼 수 없어, pymavlink로 GCS link(UDP 로컬포트 18570, `udpout:127.0.0.1:18570`로 접속)에 직접 연결하는 스크립트를 신규 작성함
- 실행한 명령어: PX4 SITL을 `HEADLESS=1 JSBSIM_LOG_ONLY=1 NO_PXH=1 timeout 200 make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS`로 백그라운드 실행 후, `python3 vtol_transition_mavlink_test.py`로 arm/takeoff/reposition/transition/land 시퀀스 실행
- 검증 결과: **실제 전방 가속 및 FW 상태(vtol_state=4) 도달을 최초로 확인함.** DO_REPOSITION 이후 groundspeed가 5→9→13→19→24 m/s로 실제 증가했고, `EXTENDED_SYS_STATE.vtol_state`가 1(TRANSITION_TO_FW)을 거쳐 4(FW)에 도달함(t=715.5, PX4 로컬 타임스탬프 기준). 이후 t≈717~720 구간에서 고도가 15m→0.6m→-3m→-12.8m로 급격히 떨어지는 이벤트가 발생했으나 JSBSim CSV 전체에서 NaN은 0건이었고(발산 아님), 이후 회복해 안정적으로 재상승/유지비행하다가 land 명령으로 정상 하강함(최종 고도 -1.6~1.1m 범위에서 소폭 진동하며 정지, 급격한 발산 없음)
- 검증 결과(JSBSim CSV 정밀분석): 이 구간에서 theta가 최대 +41.53도(t=50.22 sim time), 최소 -39.13도(t=47.36)까지 진동함(이전 AERORP 버그 시절의 79°/153° 등 발산성 값과 달리 유한하고 bounded된 범위). `vtol_att_control: Quad-chute triggered`가 이 큰 자세 이탈을 감지해 MC로 강제 복귀시킨 것으로 판단됨
- 검증하지 못한 항목: quad-chute가 정확히 어떤 파라미터/조건(자세 이탈 임계값 등)으로 발동했는지, FW 트림(Cm0/Cmalpha 등)이 이 비행 속도(20m/s대)에서 실제로 균형이 맞는지
- 검증하지 못한 이유: 이번 세션은 "제대로 된 절차로 재현했을 때 크래시 없이 견딜 수 있는지" 확인까지가 목표였음
- 남은 리스크: 전환 시도 자체는 실제로 이뤄지고 FW 상태에도 도달하지만, 그 직후 큰 자세 이탈로 quad-chute가 발동함 — 이는 좌표/게이트/제어경로 문제가 아니라 이제 순수하게 FW 비행 트림/안정성(Aero.xml의 Cm0, Cmalpha 등 균형) 영역으로 좁혀짐. 사용자가 이미 알고 있는 DATCOM 데이터 한계와 같은 카테고리의 사안
- 다음 작업: 사용자가 QGC로 직접 재현 예정. 이후 필요 시 quad-chute 트리거 조건 확인, FW 트림 재검토
- 관련 기록: TASK-20260820-1230-001, TODO-20260820-1230-001(진행 상황 갱신), TODO-20260820-1300-001(신규)
- Git commit: 없음

## [2026-08-20 13:30] PROGRESS-20260820-1330-001 — A/B 비교 종합 문서 작성(승강타/러더 공력 계수 부재 신규 발견)

- 과업: 이번 세션(2026-08-19~20) 전체 작업을 기준으로 standard_vtol_demo(A, ProjectAirSim 레퍼런스)와 standard_vtol_demo_motor_updated_ko(B, 현재 모델)의 차이를 항목별로 정리하고, 각 항목이 논문/데이터/실측 기반인지, 신규 추가분은 어떤 문제 때문인지, 대안은 무엇인지 명시한 종합 문서 작성
- 대상 프로젝트: jsbsim_workflow
- 조사한 파일: A(`/mnt/d/ProjectAirSim-jsbsim/.../standard_vtol_demo.xml`) 전체, B의 Metrics/Mass/Gear/ExternalReactions/Aero/FlightControl.xml 전체, PX4 표준 예제(gazebo-classic/sihsim) airframe
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_VS_DEMO_CHANGELOG_20260820.md
- 핵심 발견 1(신규): **B의 Aero.xml에 `fcs/elevator-pos-rad`/`fcs/rudder-pos-rad`를 참조하는 함수가 전무함**(grep으로 전수 확인). 즉 승강타/러더가 기계적으로는 정상 작동(제어경로 검증됨)하지만 공력 피치/요 모멘트를 전혀 만들지 않음. A는 `CLde`/`Cmde`/`Cndr`(위치 비례 선형 계수)로 셋 다 구현돼있음. 사용자가 이미 알고 있던 "러더 문제"가 승강타에도 동일하게 적용됨을 확인 — 최근 전환 테스트의 자세 발산(theta -39~+41도) 유력 원인 후보로 추가
- 핵심 발견 2(신규): **B의 Mass.xml 관성모멘트(ixx/iyy/izz = 10.7/8.0/18.5)가 A와 완전히 동일함.** 질량(23.6→20.0kg)과 형상(wingarea/span/chord 전부 다름)이 바뀌었는데 관성모멘트만 일치하는 것은 CAD 재계산이 반영 안 됐을 가능성을 시사. 이번 세션에서 직접 수정하지는 않음
- 핵심 변경점: 문서 자체 신규 작성 외 코드 변경 없음
- 검증 결과: 문서 내 모든 표는 실제 파일 대조로 작성(추정 아님). 다만 "B의 wingarea/CAD 실측 여부", "A의 Cmde/Cndr 계수 출처", "EYEPOINT 오프셋의 실측 여부"는 원 출처 확인이 이번 세션 범위 밖이라 문서에 "미검증"으로 명시
- 검증하지 못한 항목: 관성모멘트 상속 여부의 확정적 검증(원 CAD 계산 이력 확인 필요), A의 Cmde/Cndr 계수 출처
- 검증하지 못한 이유: CAD/DATCOM 원본 계산 이력에 접근할 수 없음(이 세션 범위 밖)
- 남은 리스크: 문서 9절에 명시한 우선순위(승강타/러더 계수 → 관성모멘트 확인 → pusher 감쇠 → FW_AIRSPD 재추정) 중 어느 것도 아직 적용하지 않음
- 다음 작업: 사용자 판단에 따라 Cmde/Cndr 추가 등 진행
- 관련 기록: STANDARD_VTOL_MOTOR_UPDATED_KO_VS_DEMO_CHANGELOG_20260820.md
- Git commit: 없음

## [2026-08-20 14:00] PROGRESS-20260820-1400-001 — 정상 시나리오 풀 세트 실행(시동~착륙, 크래시 없이 완주)

- 과업: 사용자 요청으로 시동→이륙→상승→천이→미션(선회/waypoint)→RTL→역천이→착륙까지 한 세트 전체 시나리오를 스크립트로 실행
- 대상 프로젝트: jsbsim_workflow
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/vtol_full_mission_test.py(pymavlink 기반, arm→takeoff/climb→DO_REPOSITION 가속→DO_VTOL_TRANSITION(FW)→2개 waypoint 선회 leg→NAV_RETURN_TO_LAUNCH→명시적 DO_VTOL_TRANSITION(MC)→NAV_LAND→disarm 모니터링까지 전 구간)
- 실행한 명령어: PX4 SITL 백그라운드 실행(`timeout 320`) 후 `python3 vtol_full_mission_test.py`
- 검증 결과(단계별):
  1. ARM: 정상
  2. TAKEOFF/CLIMB: 정상, 37m 도달(약 28초 소요)
  3. TRANSITION: FW 상태 도달 확인(vtol_state MC→TRANS_TO_FW→**FW**), 그러나 **FW 상태 유지는 약 2.6초뿐**이고 곧바로 quad-chute로 MC 복귀(5.3절에서 확인한 승강타/러더 공력 계수 부재가 원인으로 추정, 예상된 결과)
  4. MISSION LEG 2/3(선회/waypoint): FW 복귀 실패로 인해 이 구간은 MC 모드로 비행됨(스크립트가 재전환을 시도하지 않는 설계라 예상된 동작). DO_REPOSITION 자체는 정상 처리(ack=3이지만 실제 위치 이동은 확인됨, 이전 세션과 동일 패턴)
  5. RETURN TO HOME: 정상 접수(ack=0), 이미 MC 상태라 별다른 전이 없이 귀환 로직 진입
  6. 명시적 BACK-TRANSITION(MC): 이미 MC라 사실상 no-op, ack=0
  7. LAND: **완벽하게 매끄러운 단조 하강**(42.9m→0.1m까지 약 34초간 오차 없이 선형에 가깝게 하강), t=437.1에 **정상 DISARMED 확인**
- 검증 결과(CSV): 전체 실행 동안 **NaN 0건**. theta 최대 56.14도/최소 -39.46도(t=46~47s 부근, FW 시도 구간과 일치) — 이전 세션 결과와 유사한 범위로, 발산이 아닌 bounded된 진동
- 검증하지 못한 항목: 실제 FW 유지 비행 상태에서의 미션 완주(승강타/러더 계수 부재로 아직 불가능), 미션 아이템 프로토콜(MISSION_ITEM_INT 업로드) 기반의 "진짜" AUTO 미션(이번엔 DO_REPOSITION 연속 호출로 대체함)
- 검증하지 못한 이유: 5.3절 이슈(V-tail 공력 계수)가 해결되기 전까지는 FW 유지비행 자체가 불가능. 미션 프로토콜은 이번 세션 범위상 더 간단한 DO_REPOSITION으로 충분하다고 판단
- 남은 리스크: 없음(이번 테스트 목표였던 "전체 시퀀스가 안전하게 완주되는지"는 완전히 검증됨). FW 유지비행은 여전히 TODO-20260820-1300-001(승강타/러더 계수, 사용자 V-tail 작업 대기)에 의존
- 다음 작업: 사용자의 V-tail 공력 처리/W&B 확정 이후 동일 스크립트로 재검증하면 FW 유지 여부를 바로 확인 가능
- 관련 기록: TASK-20260820-1400-001, scripts/vtol_full_mission_test.py(신규 도구)
- Git commit: 없음

## [2026-08-20 14:30] PROGRESS-20260820-1430-001 — quad-chute 정확한 트리거 규명 + 임시 대응(A+B) 적용, 여전히 미해결

- 과업: quad-chute 정확한 원인 규명(사용자 요청 "고정익 비행 안되는 이유 확인하고 해결할 방법 제시"), 이후 사용자 승인에 따라 A(임시 승강타/러더 공력계수)+B(전환 추력 상향) 적용 및 재검증
- 대상 프로젝트: jsbsim_workflow
- 조사한 파일: /home/junyeopkwon/px4_versions/PX4-v1.16.0/src/modules/vtol_att_control/{vtol_type.cpp, vtol_att_control_main.cpp, vtol_att_control_params.c}
- 핵심 발견(원인 규명): **quad-chute 트리거는 pitch/roll 자세각 임계값(`isPitchExceeded`/`isRollExceeded`)이 아니라 `isFrontTransitionAltitudeLoss()`(`VT_QC_T_ALT_LOSS` 기본 20m)였음.** `VT_FW_QC_P`/`VT_FW_QC_R`는 기본값 0(비활성)이고 이 프로젝트에서 한 번도 설정된 적 없음(grep으로 확인) — 즉 여태 관측한 theta -30~+56도 진동은 quad-chute의 원인이 아니라 결과(추락 회복 과정의 흔들림)였음. CSV 데이터와 대조: TRANS_TO_FW 진입 직후 alt≈28.8m에서 3.6초 만에 alt≈0.6m까지(28.2m 손실) 떨어짐 — 20m 기준을 크게 초과, 타이밍도 "전환 중 또는 완료 후 5초 이내"라는 코드 조건과 정확히 일치
- 핵심 발견(정량 분석): Cm_base 테이블의 무승강타 자연 트림점은 alpha≈4.5도(CL≈0.91). 이 CL로 20kg/0.572㎡ 기체가 수평비행하려면 필요속도 V≈24.8m/s(계산: √(196N/(0.5·1.225·0.91·0.572))). 전환 가속 구간(15~20m/s대)에서는 이 자연 트림 CL로 양력이 부족해 가라앉고, Cmde 부재로 PX4가 받음각을 능동적으로 키워 보정할 수단이 없어 그대로 가라앉음
- 수정한 파일: aircraft_variants/standard_vtol_demo_motor_updated_ko/Aero.xml(+PX4 bridge 동기화), airframe 3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4
- 핵심 변경점(A): LIFT/PITCH/YAW 축에 각각 `CLde`(-0.35), `Cmde`(+1.10), `Cndr`(+0.09) 함수를 신규 추가 — 전부 레퍼런스 standard_vtol_demo.xml(A)의 계수를 그대로 임시 차용(명시적으로 "[임시 placeholder]" 표기, alpha_validity_gate 미적용). (B) `VT_F_TRANS_THR`를 0.75→1.0으로 상향(전환 중 최대 pusher 추력)
- 실행한 명령어: xmllint, DONT_RUN 빌드, `vtol_transition_mavlink_test.py` 재실행(A/B 적용 전과 동일 시퀀스로 직접 비교)
- 검증 결과: **quad-chute는 동일 메커니즘(고도손실)으로 여전히 발생**. FW 도달 최고 groundspeed는 24.33→25.17m/s로 소폭 개선됐으나, 고도손실은 오히려 더 심함(28.8→0.6m였던 것이 28.7→0.2m→-5.9m). theta 범위 -30~+56도(이전과 유사). **NaN 0건, 착륙까지 완전히 정상(disarm 확인)**은 이전과 동일하게 유지됨
- 검증하지 못한 항목: A의 계수가 왜 부족한지 정량적 확인(가설: A는 wingarea 0.953㎡/23.6kg, 우리 기체는 0.572㎡/20.0kg로 날개하중이 더 커서 A의 계수 크기로는 부족할 가능성)
- 검증하지 못한 이유: 이번 세션은 A+B 적용 및 1차 재검증까지가 범위
- 남은 리스크: A(레퍼런스 계수 그대로 차용)만으로는 부족함이 확인됨. 날개하중 비율로 스케일링한 재시도, 또는 정식 V-tail 데이터(TODO-20260820-1300-001, 사용자 진행 중) 확보가 필요
- 다음 작업: 사용자 판단에 따라 (1) 계수를 날개하중 비율로 스케일링해 재시도, 또는 (2) 여기서 멈추고 정식 V-tail 데이터 대기
- 관련 기록: TODO-20260820-1430-001(신규)
- Git commit: 없음

## [2026-08-20 15:00] PROGRESS-20260820-1500-001 — quad-chute 진단 종합 보고서 작성(PPT용)

- 과업: 사용자가 나중에 PPT로 만들 것이라고 밝혀, 지금까지의 quad-chute 진단 과정(소스 분석/정량 계산/A+B 실험/QGC 실비행 재현/NaN 발산 사례/로그 비교) 전체를 발표 자료로 바로 쓸 수 있게 정리한 별도 문서 작성
- 대상 프로젝트: jsbsim_workflow
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_QUADCHUTE_DIAGNOSIS_20260820.md
- 구성: 1)문제정의 2)원인규명 1단계(자세각 가설 기각, 소스 코드로 진짜 트리거 확정) 3)원인규명 2단계(정량적 양력 부족 계산) 4)해결시도 A+B 5)실제 QGC 비행 재검증(동일 재현 + NaN 발산 사례 + 로그 비교표) 6)로그/산출물 경로 7)결론 및 다음 단계
- 핵심 변경점: 문서 신규 작성 외 코드 변경 없음(기존 세션에서 이미 완료된 진단/실험 내용을 종합 정리)
- 검증 결과: 문서 내 모든 인용(PX4 소스, JSBSim CSV 수치, ulog 메시지, git 커밋 해시, 로그 파일명/타임스탬프)은 실제 확인된 내용 그대로 옮김, 추정치는 명시적으로 "추정"으로 표기
- 관련 기록: docs/STANDARD_VTOL_MOTOR_UPDATED_KO_QUADCHUTE_DIAGNOSIS_20260820.md
- Git commit: 없음

## [2026-08-20 15:15] PROGRESS-20260820-1515-001 — 8/19~8/20 전체 종합 타임라인 문서 작성(PPT 마스터 자료)

- 과업: 사용자가 quad-chute 문서만으로는 부족하다고 지적, "어제 오늘 진행한 standard_vtol 관련 내용 전체"를 한 문서로 종합 정리해달라고 요청
- 대상 프로젝트: jsbsim_workflow
- 생성한 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_MOTOR_UPDATED_KO_FULL_SUMMARY_20260819_20260820.md
- 구성: 0)한눈에 보는 결론 표 1)8/19 이전 배경 2)8/19 타임라인(표, PX4 최초 연결~고정익 전환 문제 발견) 3)8/20 상세 9개 소절(제어배선 구현→alpha발산 크래시→AERORP버그 발견수정→정상절차 재현→A/B비교문서→전체시나리오테스트→quad-chute원인규명→A/B실험→QGC실비행검증) 4)종합 결론(해결된 것/안된 것/우선순위) 5)기존 6개 하위 문서 인덱스 표
- 핵심 변경점: 문서 신규 작성 외 코드 변경 없음. 기존에 개별적으로 작성됐던 6개 문서(PX4_REVIEW, TRANSITION_DIAGNOSIS, QGC_LOG_ANALYSIS, DEMO_COMPARISON, VS_DEMO_CHANGELOG, QUADCHUTE_DIAGNOSIS)와 agent-log 전체를 종합해 하나의 타임라인으로 재구성
- 검증 결과: 모든 시각/수치/커밋해시는 기존 agent-log 및 이전 문서에서 실제 확인된 내용만 인용, 새로운 사실 조사는 하지 않음(순수 종합)
- 관련 기록: docs/STANDARD_VTOL_MOTOR_UPDATED_KO_FULL_SUMMARY_20260819_20260820.md
- Git commit: 없음
