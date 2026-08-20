## [2026-06-15 17:51] TASK-20260615-1751-001 — DONE

- 과업:
  - JSBSim만 사용해 `c172x` 기체의 450 m, 60 m/s, pitch 2.5 deg 조건 추락 궤적 생성 워크플로우 작성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 캡쳐본과 동일한 초기값으로 trim/autopilot 없이 추락 궤적을 생성하는 초기 스크립트와 runscript를 만들고, `jsbsim_workflow` 방식으로 저장
  - 지면 도달 시간, 지면 충돌 좌표, 지면 충돌 속도, 최종 자세각 산출
- 작업 범위:
  - `scripts/c172x/initial_condition/` 초기조건 XML 추가
  - `scripts/c172x/runscript/` runscript XML 추가
  - 실행 및 충돌 지표 요약 Python wrapper 추가
  - c172x README 갱신
  - 실제 JSBSim 실행 및 결과 CSV/JSON/plot 생성 확인
- 제외 범위:
  - `c172x` 항공기 모델 자체 수정
  - trim/autopilot 사용
  - 기존 UAM 모델과 동일 동역학을 강제로 맞추기 위한 계수 튜닝
- 가정:
  - 캡쳐본의 좌표계 `(x, y, z)`는 로컬 좌표계로 보고, JSBSim 결과 보고에서는 `x=local North`, `y=local East`, `z=ground altitude`로 정리
  - 초기 자세각 `(0, 2.5, 0) deg`는 JSBSim Euler angle `(phi, theta, psi)`로 적용
  - 지면 도달은 `c172x` 착륙장치 첫 지면 접촉 `gear/unit[0]/WOW eq 1` 기준으로 판단
- 완료 조건:
  - 초기조건 XML과 runscript XML이 `jsbsim_workflow/scripts/c172x/` 아래에 존재
  - 단일 명령으로 실행 및 요약 산출 가능
  - 실제 실행 결과에서 지면 도달 시간, 충돌 좌표, 충돌 속도, 최종 자세각 확인
- 완료 항목:
  - `4.0__450m_60ms_pitch25_no_trim_init.xml` 추가
  - `4.0__450m_60ms_pitch25_no_trim_drop_run.xml` 추가
  - `run_c172x_450m_drop_no_trim.py` 추가
  - 최종 실행 `4.0.4__450m_60ms_pitch25_no_trim_drop` 성공
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 14:15] TASK-20260617-1415-001 — DONE

- 과업:
  - JSBSim 실행 시 6DOF 검증용 property 묶음을 별도 CSV로 저장
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 사용자가 제시한 상태, 입력, 힘/모멘트, 가속도, 공력, 추력, 접촉/환경 property를 `<output>`에 지정해 CSV로 따로 저장
- 목적:
  - PX4 연동 비교와 6DOF 검증에서 상태값뿐 아니라 원인값까지 같은 timestep에서 추적 가능하게 함
- 작업 범위:
  - 기존 raw/SI CSV 출력 유지
  - 추가 `sixdof_raw` CSV 출력 생성
  - aircraft catalog에 실제 존재하는 property만 `<output>`에 포함
  - pitch +2.5 deg C172X Cm0=0 케이스로 실행 검증
- 제외 범위:
  - SI 단위 변환 컬럼 추가
  - 모든 wrapper의 summary 스키마 일괄 변경
  - Git commit 생성
- 가정:
  - 모델별로 없는 property는 JSBSim output에 넣지 않는 것이 안전함
  - no-engine C172X에서는 VTOL/engine indexed property 일부가 없는 것이 정상
- 완료 조건:
  - generated runscript에 기존 raw output과 별도 6DOF output이 함께 생성
  - 6DOF raw CSV 파일 생성
  - 상태/힘/모멘트/가속도/공력/접촉/환경 대표 컬럼 존재 확인
- 완료 항목:
  - `run_jsbsim_timestamped.py`에 `SIXDOF_VALIDATION_PROPERTIES` 추가
  - aircraft catalog 기반 property 필터링 추가
  - `logs/csv/sixdof_raw/...` 저장 경로 추가
  - pitch +2.5 deg wrapper summary에 `sixdof_raw_csv` 경로 추가
  - 실행 ID `1.1.3__450m_pitchp25_ubody60_cm0zero_drop`로 검증 완료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 12:59] CORRECTION-20260617-1259-001 — 정정

- 대상 기록:
  - `TASK-20260617-1258-001`
- 정정 이유:
  - append 패치 컨텍스트가 흔한 문구와 매칭되어 파일 하단이 아닌 `docs/agent-log/TASK.md:37` 부근에 삽입됨
- 기존 내용:
  - `TASK-20260617-1258-001`의 내용 자체는 유효하나 시간 순서상 위치가 부적절함
- 정정 내용:
  - 기존 중간 삽입 기록은 삭제하지 않고, 아래에 같은 과업의 최신 참조 기록 `TASK-20260617-1259-001`을 append함
- 영향 범위:
  - 작업 기록 조회 시 하단의 `TASK-20260617-1259-001`을 최신 참조로 사용
- 검증 결과:
  - `grep -n 'TASK-20260617-1258-001' docs/agent-log/TASK.md`로 중간 삽입 위치 확인
- 다음 작업:
  - 향후 기록 append 시 더 고유한 EOF 컨텍스트 사용

## [2026-06-17 12:59] TASK-20260617-1259-001 — DONE

- 과업:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체의 pitch +2.5 deg, `ubody=60 m/s` 추락 초기조건 생성 및 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체로 초기 고도 `450 m`, pitch `2.5 deg`, 속도 `ubody=60 m/s` 조건을 만들고 `jsbsim_workflow`에서 추락 실행
- 목적:
  - `Cmo=0`, no-engine/no-propeller, surface-neutral, pointmass-zero 조건에서 pitch-up 초기 자세의 자유 추락/활공 응답 확인
- 작업 범위:
  - 기존 `theta=-20 deg` 케이스 보존
  - `theta=+2.5 deg`, `ubody=60 m/s`, altitude `450 m` initial XML 추가
  - 전용 runscript/wrapper 추가
  - JSBSim 실행 및 summary/plot/CSV 생성
- 제외 범위:
  - 기존 `1.0` 초기조건 수정
  - 추가 공력 계수 변경
  - Git commit 생성
- 가정:
  - `ubody=60`은 JSBSim body x축 속도
  - heading, roll, sideslip, wind는 기존 비교 케이스와 동일하게 `0`으로 유지
- 완료 조건:
  - initial XML에 altitude `450 m`, `theta=2.5 deg`, `ubody=60 m/s` 반영
  - JSBSim 실행 성공
  - 초기 로그에서 pitch와 속도 확인
  - 조종면/추력 0 유지 확인
- 완료 항목:
  - `1.1__450m_pitchp25_ubody60_drop_init.xml` 추가
  - `1.1__450m_pitchp25_ubody60_cm0zero_drop_run.xml` 추가
  - `run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py` 추가
  - 실행 ID `1.1.1__450m_pitchp25_ubody60_cm0zero_drop` 생성
  - 지면 접촉 이벤트로 `73.83333333 s`에 종료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 14:16] CORRECTION-20260617-1416-001 — 정정

- 대상 기록:
  - `TASK-20260617-1415-001`
- 정정 이유:
  - append 패치 컨텍스트 문제로 `TASK-20260617-1415-001`이 파일 하단이 아닌 `docs/agent-log/TASK.md:37` 부근에 삽입됨
- 기존 내용:
  - `TASK-20260617-1415-001`의 작업 내용은 유효하나 시간 순서상 위치가 부적절함
- 정정 내용:
  - 기존 중간 삽입 기록은 삭제하지 않고, 아래 `TASK-20260617-1416-001`을 최신 하단 참조 기록으로 append함
- 영향 범위:
  - 작업 기록 조회 시 `TASK-20260617-1416-001`을 최신 참조로 사용
- 검증 결과:
  - `grep -n 'TASK-20260617-1415-001' docs/agent-log/TASK.md`로 중간 삽입 위치 확인
- 다음 작업:
  - `TASK.md` append 시 더 긴 고유 컨텍스트 사용

## [2026-06-17 14:16] TASK-20260617-1416-001 — DONE

- 과업:
  - JSBSim 실행 시 6DOF 검증용 property 묶음을 별도 CSV로 저장
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 사용자가 제시한 상태, 입력, 힘/모멘트, 가속도, 공력, 추력, 접촉/환경 property를 `<output>`에 지정해 CSV로 따로 저장
- 목적:
  - PX4 연동 비교와 6DOF 검증에서 상태값뿐 아니라 원인값까지 같은 timestep에서 추적 가능하게 함
- 작업 범위:
  - 기존 raw/SI CSV 출력 유지
  - 추가 `sixdof_raw` CSV 출력 생성
  - aircraft catalog에 실제 존재하는 property만 `<output>`에 포함
  - pitch +2.5 deg C172X Cm0=0 케이스로 실행 검증
- 제외 범위:
  - SI 단위 변환 컬럼 추가
  - 모든 wrapper의 summary 스키마 일괄 변경
  - Git commit 생성
- 가정:
  - 모델별로 없는 property는 JSBSim output에 넣지 않는 것이 안전함
  - no-engine C172X에서는 VTOL/engine indexed property 일부가 없는 것이 정상
- 완료 조건:
  - generated runscript에 기존 raw output과 별도 6DOF output이 함께 생성
  - 6DOF raw CSV 파일 생성
  - 상태/힘/모멘트/가속도/공력/접촉/환경 대표 컬럼 존재 확인
- 완료 항목:
  - `run_jsbsim_timestamped.py`에 `SIXDOF_VALIDATION_PROPERTIES` 추가
  - aircraft catalog 기반 property 필터링 추가
  - `logs/csv/sixdof_raw/...` 저장 경로 추가
  - pitch +2.5 deg wrapper summary에 `sixdof_raw_csv` 경로 추가
  - 실행 ID `1.1.3__450m_pitchp25_ubody60_cm0zero_drop`로 검증 완료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 12:58] TASK-20260617-1258-001 — DONE

- 과업:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체의 pitch +2.5 deg, `ubody=60 m/s` 추락 초기조건 생성 및 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체로 초기 고도 `450 m`, pitch `2.5 deg`, 속도 `ubody=60 m/s` 조건을 만들고 `jsbsim_workflow`에서 추락 실행
- 목적:
  - `Cmo=0`, no-engine/no-propeller, surface-neutral, pointmass-zero 조건에서 pitch-up 초기 자세의 자유 추락/활공 응답 확인
- 작업 범위:
  - 기존 `theta=-20 deg` 케이스 보존
  - `theta=+2.5 deg`, `ubody=60 m/s`, altitude `450 m` initial XML 추가
  - 전용 runscript/wrapper 추가
  - JSBSim 실행 및 summary/plot/CSV 생성
- 제외 범위:
  - 기존 `1.0` 초기조건 수정
  - 추가 공력 계수 변경
  - Git commit 생성
- 가정:
  - 사용자의 `속도 ubody 60m/s`는 JSBSim body x축 속도 `ubody`를 의미
  - heading, roll, sideslip, wind는 기존 비교 케이스와 동일하게 `0`으로 유지
- 완료 조건:
  - initial XML에 altitude `450 m`, `theta=2.5 deg`, `ubody=60 m/s` 반영
  - JSBSim 실행 성공
  - 초기 로그에서 pitch와 속도 확인
  - 조종면/추력 0 유지 확인
- 완료 항목:
  - `1.1__450m_pitchp25_ubody60_drop_init.xml` 추가
  - `1.1__450m_pitchp25_ubody60_cm0zero_drop_run.xml` 추가
  - `run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py` 추가
  - 실행 ID `1.1.1__450m_pitchp25_ubody60_cm0zero_drop` 생성
  - 지면 접촉 이벤트로 `73.83333333 s`에 종료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 11:20] TASK-20260617-1120-001 — DONE

- 과업:
  - `c172x_noengine_surface_neutral_empty_cm0`용 30도 간격 자세 격자 drop 초기조건 XML 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `jsbsim_workflow폴더에서 자전없고 구형지구랑 c172x_noengine_surface_neutral_empty_cm0기체로 고도 450m에서 ubody 속력만 60m/s로하고 나머지 속도성분 없는데 자세값(psi, theta, phi)를 30도 간격으로 drop하는 initial xml 만들어줘`
- 목적:
  - Cm0=0 C172X no-engine/no-propeller/surface-neutral/pointmass-zero 모델에서 body x축 속도만 있는 450 m drop 초기 자세 격자 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 작업 범위:
  - `psi`: `0..330 deg`, 30도 간격
  - `theta`: `-90..90 deg`, 30도 간격
  - `phi`: `0..330 deg`, 30도 간격
  - `altitude=450 m`, `ubody=60 m/s`, `vbody=0`, `wbody=0`
  - 재생성용 Python 스크립트 추가
- 제외 범위:
  - runscript 생성
  - JSBSim 시뮬레이션 실행
  - aircraft XML 수정
- 가정:
  - "자전없고 구형지구" 조건은 추후 runscript에서 aircraft/earth model 설정으로 연결하며, initial XML은 위치/고도/자세/속도만 담는 기존 형식을 따른다.
  - Euler 자세 격자는 항공기 관례상 `theta`를 `-90..90 deg` 범위로 제한하고, `psi`와 `phi`는 `0..330 deg`로 순회한다.
- 완료 조건:
  - 30도 간격 자세 격자 초기조건 XML 생성
  - 모든 XML 파싱 성공
- 완료 항목:
  - `1008`개 initial XML 생성
  - 생성 스크립트 추가
  - XML 파싱 검증 완료
- 미완료 항목:
  - runscript/실행 검증은 요청 범위 밖이라 수행하지 않음
- 최종 상태:
  - DONE
- Git commit:
  - 없음

## [2026-06-15 18:20] TASK-20260615-1820-001 — DONE

- 과업:
  - 기존 ballistic 결과와 유사한 방향 고정 + 활공 추락용 `c172x` heading hold/trim glide 별도 케이스 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 제공된 ballistic 결과 이미지를 기준으로, 방향을 고정하고 활공 추락하는 느낌이므로 heading hold/trim glide 버전을 별도 케이스로 분리하는 방향 검토 및 진행
- 작업 범위:
  - `4.3` runscript 추가
  - 무자전 원형지구, t=0 추락 시작, 초기 좌표 `(0,0,450 m)`, 초기 속도 `(60,0,0) m/s` 유지
  - engine-out 상태에서 heading hold와 pitch trim `0.18` 적용
  - 실행/요약 스크립트 추가 및 결과 산출
- 제외 범위:
  - `4.2` AP/trim off 결과 삭제 또는 변경
  - ballistic 질점 모델 신규 생성
- 가정:
  - 기존 ballistic 결과와 “형태상 비교”를 위한 케이스이며, 수평거리까지 일치시키는 보정은 수행하지 않음
- 완료 조건:
  - `4.3` 케이스 실행 성공 및 summary CSV/JSON, CSV log, plot 생성
- 완료 항목:
  - `4.3__450m_60ms_x_engineout_t0_headinghold_trim_spherical_run.xml` 추가
  - `run_c172x_engineout_t0_headinghold_trim_spherical.py` 추가
  - 최종 실행 `4.3.1__450m_60ms_x_engineout_t0_headinghold_trim_spherical` 성공
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
- Git commit:
  - 없음

## [2026-06-15 18:13] TASK-20260615-1813-001 — DONE

- 과업:
  - 추락 시작점을 직접 초기조건으로 둔 `c172x` 무자전 원형지구 추락 케이스 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 추락 시작 좌표를 `(0,0,450 m)`, 속도를 `(60,0,0)`, 시간을 `0 s`로 두고, 추락 시작부터 완료까지의 총 이동거리, 최종 좌표, 자세각, 속도를 확인
  - 지구는 자전하지 않는 원형 지구로 가정
  - 이전처럼 cruise 30초를 포함할 필요 없음
- 작업 범위:
  - `4.2` 초기조건 XML 추가
  - `4.2` runscript XML 추가
  - 무자전 원형지구 planet XML을 명시하는 실행/요약 스크립트 추가
  - 실제 실행 및 결과 요약/그래프 생성
- 제외 범위:
  - 기존 `4.0`, `4.1` 결과 삭제
  - `c172x` 항공기 모델 수정
- 가정:
  - 좌표계는 `x=local North`, `y=local East`, `z=altitude`
  - 초기 속도 `(60,0,0)`은 `psi=0`, `theta=0`, `ubody=60 m/s`로 구현
  - 원래 요청의 trim/autopilot 없이 조건을 반영해 `4.2.2`부터 AP/trim off 기준으로 실행
- 완료 조건:
  - `4.2` 케이스가 `04_nonrotating_spherical_earth.xml`로 실행되고 요약값을 산출
- 완료 항목:
  - `4.2__450m_60ms_x_engineout_t0_spherical_init.xml` 추가
  - `4.2__450m_60ms_x_engineout_t0_spherical_run.xml` 추가
  - `run_c172x_engineout_t0_spherical.py` 추가
  - 최종 실행 `4.2.2__450m_60ms_x_engineout_t0_spherical` 성공
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
- Git commit:
  - 없음

## [2026-06-15 18:05] TASK-20260615-1805-001 — DONE

- 과업:
  - `4.1` 추락 케이스에서 엔진 정지 시점을 `t=0`으로 재기준화한 별도 로그와 그래프 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 방금 요청한 cruise 후 engine-out 케이스만 별도로 추락 시작 시점을 0으로 보고 그래프와 로그를 따로 산출
- 작업 범위:
  - 기존 `4.1.1` SI CSV를 입력으로 사용
  - 엔진 정지 시점 `31.0 s` 이후 행만 추출
  - 시간, x/y 위치, 고도 손실, 수평거리 등을 engine-out 기준으로 재계산
  - 별도 CSV/JSON/PNG 산출
- 제외 범위:
  - 원본 JSBSim 재실행
  - 원본 CSV/JSON/plot 수정
- 가정:
  - 추락 시작 시점은 `engineout_start_time_s = 31.0`으로 정의
  - x 방향은 local North 기준 유지
- 완료 조건:
  - engine-out 기준 CSV, summary JSON, 3D trajectory plot, states plot 생성
- 완료 항목:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/extract_c172x_engineout_t0.py` 추가
  - engine-out t0 산출물 생성 완료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
- Git commit:
  - 없음

## [2026-06-15 18:00] TASK-20260615-1800-001 — DONE

- 과업:
  - c172x 추락 케이스를 “직접 투하”가 아니라 “450 m, 60 m/s x 방향 cruise 이후 engine-out”으로 정정
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 이전 그래프가 말이 안 되며, 참조 runscript `2.2__cruise_30s_engineout_headinghold_legacy_run.xml`처럼 크루즈로 날아가다가 x 방향 60 m/s에서 엔진을 끄고 추락하는 방식으로 해석해야 한다는 정정 요청
- 작업 범위:
  - `4.1` 초기조건 XML 추가
  - `4.1` runscript XML 추가
  - wrapper 기본 실행 대상을 `4.1`로 변경
  - 결과 요약에 엔진 정지 시점 상태 추가
- 제외 범위:
  - 기존 `4.0` 파일 삭제 또는 덮어쓰기
  - `c172x` 항공기 모델 자체 수정
- 가정:
  - x 방향은 기존 결정대로 local North 방향이며, heading `0 deg`로 유지
  - 참조 `2.2`와 유사하게 powered cruise trim 및 altitude/heading hold 후, 엔진 정지 시 altitude hold는 끄고 heading hold는 유지
- 완료 조건:
  - `4.1` 케이스가 실제 JSBSim 실행에 성공하고 지면 접촉 요약을 생성
- 완료 항목:
  - `4.1__450m_60ms_x_cruise_untrimmed_init.xml` 추가
  - `4.1__450m_60ms_x_cruise30_engineout_headinghold_run.xml` 추가
  - `run_c172x_450m_drop_no_trim.py` 기본 실행 대상을 `4.1`로 변경
  - 최종 실행 `4.1.1__450m_60ms_x_cruise30_engineout_headinghold` 성공
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
- Git commit:
  - 없음
## [2026-06-16 11:56] TASK-20260616-1156-001 — DONE

- 과업:
  - `c172x` ground reaction damping/spring/friction 계수 27개 변형 생성 및 기본 계수 이륙 실행 스크립트 추가
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x.xml`의 ground reaction 계수 중 damping, spring, friction을 각각 `0`, `절반값`, `기본값`으로 나눈 총 27개 XML을 별도 폴더에 구성
  - 동일 initial condition과 동일 runscript로 비교할 수 있도록 workflow 내부 로그 저장과 plot 생성을 기존 방식으로 유지
  - 우선 `c172x` 파일을 만들고 기본 계수 파일이 이륙 가능하도록 하는 스크립트 작성
- 작업 범위:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x/c172x.xml` 원본의 `<ground_reactions>` 계수를 기준으로 변형 생성
  - 변형 원본은 `/home/junyeopkwon/jsbsim_workflow/aircraft_variants/c172x_groundreaction/` 아래에 보관
  - 실행 시 선택 변형을 JSBSim aircraft 폴더로 복사/rename 후 기존 `run_jsbsim_timestamped.py`로 실행
  - 기본 계수 변형의 이륙 확인 실행 및 요약 생성
- 제외 범위:
  - 27개 전체 변형 일괄 실행 및 비교 분석
  - 원본 `/home/junyeopkwon/jsbsim/aircraft/c172x/c172x.xml` 직접 수정
- 가정:
  - friction 계수는 `static_friction`, `dynamic_friction`, `rolling_friction`을 같은 배율로 조정
  - damping 계수는 `damping_coeff`, `damping_coeff_rebound`, 그리고 right main gear의 equivalent `strut_force` damping 항을 같은 배율로 조정
  - spring 계수는 `spring_coeff`와 right main gear의 equivalent `strut_force` spring 항을 같은 배율로 조정
- 완료 조건:
  - 27개 `c172x.xml` 변형 생성
  - 기본 계수 변형으로 JSBSim 이륙 확인 runscript 실행 성공
  - raw CSV, SI CSV, console log, states plot, trajectory plot이 기존 workflow 경로에 생성
- 완료 항목:
  - `generate_c172x_groundreaction_variants.py` 추가
  - `5.0__takeoff_groundreaction_check_run.xml` 추가
  - `run_c172x_groundreaction_takeoff.py` 추가
  - 27개 변형 XML과 `manifest.csv` 생성
  - 기본 계수 변형 `c172x_gr_damp100_spring100_fric100` 실행 성공
- 미완료 항목:
  - 나머지 26개 변형은 사용자가 직접 비교한다고 했으므로 실행하지 않음
- 최종 상태:
  - DONE
- Git commit:
  - 없음
## [2026-06-16 12:08] TASK-20260616-1208-001 — DONE

- 과업:
  - FlightGear C172 수동 이륙 절차 기반 `c172x` takeoff 상태기계 runscript 추가
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - FlightGear 매뉴얼의 C172 이륙 방식이 JSBSim 기반이므로, 이를 반영한 스크립트가 필요하지 않은지 확인하고 반영
- 작업 범위:
  - `40 kt` nose-wheel lift, `55 kt` rotation/liftoff, `70 kt` initial climb target, `500 ft AGL` runway heading 유지 절차를 `5.1` runscript로 추가
  - ground reaction variant 실행 wrapper의 기본 procedure를 `flightgear`로 변경
  - 기본 계수 variant로 500 ft AGL 도달 실행 검증
- 제외 범위:
  - 27개 전체 ground reaction variant 실행
  - FlightGear Autostart 자체 호출
- 가정:
  - FlightGear 문서의 Autostart는 엔진 자동 시동이며 자동이륙이 아니므로, JSBSim runscript에서는 수동 이륙 절차를 상태 전이로 구현
  - C172X 모델은 순수 수동 입력만으로 500 ft까지 안정 상승이 어려워 50 ft 이후 attitude hold, 250 ft 이후 heading/altitude hold를 사용하는 하이브리드 안정화 적용
- 완료 조건:
  - 기본 계수 variant에서 `5.1` 절차로 500 ft AGL 도달
  - 기존 workflow 구조로 raw CSV, SI CSV, console log, states plot, trajectory plot 생성
- 완료 항목:
  - `5.1__takeoff_flightgear_state_machine_run.xml` 추가
  - `run_c172x_groundreaction_takeoff.py` 기본 procedure를 `flightgear`로 변경하고 `--procedure basic` 유지
  - README 사용법 갱신
  - 기본 계수 variant `5.1.10__takeoff_flightgear_state_machine` 실행 성공
- 미완료 항목:
  - 27개 전체 variant의 `5.1` 실행 결과 비교
- 최종 상태:
  - DONE
- Git commit:
  - 없음
## [2026-06-16 12:16] TASK-20260616-1216-001 — DONE

- 과업:
  - 원본 `c172x` aircraft 직접 기반 단순 이륙 runscript 추가
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 현재 그래프가 왜 꺾이는지 확인하고, 이륙 스크립트 자체는 `c172x` 기반으로 만들어둘 것
- 작업 범위:
  - ground reaction variant wrapper와 분리된 원본 `c172x` 직접 실행 runscript 추가
  - 기존 `2.0__takeoff_engineout_init.xml` 초기조건 재사용
  - 기존 timestamp runner로 raw CSV, SI CSV, console log, plot 생성 확인
- 제외 범위:
  - 자세/속도/조향 closed-loop 튜닝
  - ground reaction 27개 variant 비교 실행
- 가정:
  - 사용자가 후속 튜닝과 비교는 직접 수행
- 완료 조건:
  - `<use aircraft="c172x">`를 직접 사용하는 단순 이륙 runscript 생성
  - 해당 runscript가 JSBSim에서 실행되어 로그와 plot 생성
- 완료 항목:
  - `5.2__takeoff_simple_c172x_run.xml` 추가
  - README 실행 예시 추가
  - `5.2.1__takeoff_simple_c172x` 실행 성공
- 미완료 항목:
  - 오른쪽 wing tip 접촉 없이 매끄러운 상승 궤적으로 튜닝
- 최종 상태:
  - DONE
- Git commit:
  - 없음
## [2026-06-16 12:25] TASK-20260616-1225-001 — DONE

- 과업:
  - 원본 `c172x`로 엔진 가동, 활주, 이륙, 500 ft 상승 runscript 추가
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 단순 확인용이 아니라 원본 `c172x`로 엔진 켜고 달리다가 500 ft까지 상승하는 스크립트 작성
- 작업 범위:
  - `<use aircraft="c172x">` 직접 사용
  - 엔진 running, 브레이크 해제, full throttle, 40 kt nose lightening, 60 kt rotation, 20 ft initial climb, 250 ft 이후 안정 상승, 500 ft 종료 이벤트 구성
  - 기존 timestamp runner로 실행 및 로그/plot 생성 확인
- 제외 범위:
  - ground reaction variant 실행
  - 27개 계수 조합 비교
- 가정:
  - 500 ft까지 안정 상승을 위해 250 ft 이후 heading/altitude hold를 사용하는 것을 허용
- 완료 조건:
  - 원본 `c172x`로 500 ft AGL 도달
- 완료 항목:
  - `5.3__takeoff_to_500ft_c172x_run.xml` 추가
  - `5.3.1__takeoff_to_500ft_c172x` 실행 성공
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
- Git commit:
  - 없음
## [2026-06-16 12:34] TASK-20260616-1234-001 — DONE

- 과업:
  - `5.3` 원본 `c172x` 500 ft 이륙 스크립트의 30초 부근 고도 개입 제거 및 재검증
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 30초쯤 개입이 들어온 것처럼 보이며 실제 이륙에서 이런 현상은 정상적이지 않으므로 원인 확인 및 수정
- 작업 범위:
  - `5.3__takeoff_to_500ft_c172x_run.xml`에서 20 ft 이후 `ap/attitude_hold` 제거
  - 초기 상승 수동 입력 재튜닝
  - 100 ft 이후 heading hold, 250 ft 이후 altitude hold로 분리
  - 지면 재접촉 abort 조건 추가
- 제외 범위:
  - 완전 closed-loop airspeed controller 작성
  - 27개 variant 전체 재실행
- 가정:
  - 30초 부근의 고도 꺾임은 attitude hold 조기 개입과 elevator 전환 과도응답 때문
- 완료 조건:
  - 원본 `c172x`로 지면 재접촉 없이 500 ft AGL 도달
- 완료 항목:
  - `5.3` 수정
  - `5.3.6__takeoff_to_500ft_c172x` 실행 성공
- 미완료 항목:
  - 70 kt target 유지 튜닝
- 최종 상태:
  - DONE
- Git commit:
  - 없음
## [2026-06-16 18:23] TASK-20260616-1823-001 — DONE

- 과업:
  - C172X 엔진 없는 상태 추락 runscript 작성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `c172x 엔진 없는상태로 추락하는 runscript 작성`
- 목적:
  - `c172x` 기체를 초기 고도 450 m, 초기 속도 60 m/s에서 엔진 off, autopilot off, 조종면 중립 상태로 추락시키는 반복 실행 가능한 JSBSim runscript 제공
- 작업 범위:
  - `scripts/c172x/initial_condition/`에 no-engine 초기조건 추가
  - `scripts/c172x/runscript/`에 no-engine drop runscript 추가
  - 직접 실행용 Python wrapper 및 README 사용법 추가
- 제외 범위:
  - `c172x.xml` aircraft 자체에서 `<propulsion>` 모델을 제거하는 별도 기체 variant 생성
  - 기존 `4.2`, `4.3` engine-out 케이스 변경
- 가정:
  - "엔진 없는상태"는 runscript/초기조건 수준에서 `running=0`, throttle/mixture/magneto/starter/set-running off를 의미한다고 해석
  - 초기 조건은 기존 `4.x` 추락 계열과 맞춰 `(x,y,z)=(0,0,450 m)`, 속도 `(60,0,0) m/s`, 무자전 원형지구를 사용
- 완료 조건:
  - 새 runscript XML이 파싱 가능
  - `run_c172x_noengine_drop.py`가 실행되어 SI CSV, 요약 CSV/JSON, plot을 생성
  - 지면 접촉 시 종료
- 완료 항목:
  - `4.4__450m_60ms_x_noengine_drop_init.xml` 추가
  - `4.4__450m_60ms_x_noengine_drop_run.xml` 추가
  - `run_c172x_noengine_drop.py` 추가
  - `scripts/c172x/README.md`에 실행 명령 추가
  - 실행 검증 완료: `4.4.2__450m_60ms_x_noengine_drop`
- 미완료 항목:
  - 물리적으로 propulsion/engine 요소가 제거된 별도 aircraft variant는 생성하지 않음
- 최종 상태:
  - DONE
## [2026-06-16 18:32] TASK-20260616-1832-001 — DONE

- 과업:
  - C172X 엔진 추력과 프로펠러까지 없는 추락 파일 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `엔진 추력 프로펠러까지 없이 추락으로 파일 만들어 볼래?`
- 목적:
  - 기존 `c172x` aircraft의 propulsion/propeller windmilling 영향을 제거한 별도 aircraft variant와 추락 runscript 제공
- 작업 범위:
  - `c172x_noengine` aircraft variant 생성기 작성
  - `c172x_noengine` 초기조건/runscript 작성
  - 직접 실행 wrapper 작성
  - 실제 실행 및 engine/thrust/propeller 출력 0 확인
- 제외 범위:
  - 원본 `/home/junyeopkwon/jsbsim/aircraft/c172x/c172x.xml` 변경
  - 연료 탱크 제거
- 가정:
  - "엔진 추력 프로펠러까지 없이"는 fuel tank는 유지하되 `<engine>` 및 `<thruster>`만 제거하는 의미로 해석
- 완료 조건:
  - `/home/junyeopkwon/jsbsim/aircraft/c172x_noengine/c172x_noengine.xml` 생성
  - 생성 variant에 `<engine>`과 `<thruster>`가 없음
  - `c172x_noengine` runscript가 실행되고 engine/thrust/propeller 출력이 0
- 완료 항목:
  - `generate_c172x_noengine_variant.py` 추가
  - `scripts/c172x_noengine/` 초기조건, runscript, README 추가
  - `run_c172x_noengine_noprop_drop.py` 추가
  - 실행 ID `1.0.1__450m_60ms_x_noengine_noprop_drop` 검증 완료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-16 18:39] TASK-20260616-1839-001 — DONE

- 과업:
  - C172X 추락 케이스 수평/수직속도 비교 plot 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `지금 조종면 상태가 trim 상태인 뉴트럴 값 맞지? 수평속도랑 수직속도 확인하려고 하니깐 이것들 추가해서 그래프 비교하게 따로 ploting 해줘`
- 목적:
  - 조종면 command/trim 상태를 확인하고 수평속도 및 수직속도를 별도 그래프로 비교
- 작업 범위:
  - 기존 SI CSV에서 최신 `c172x` engine-off prop model 케이스와 `c172x_noengine` no-prop 케이스를 자동 선택
  - horizontal speed, vertical speed up, altitude 비교 plot 생성
  - elevator command, pitch trim command, actual elevator, pitch 확인 plot 생성
- 제외 범위:
  - 시뮬레이션 초기조건 변경
  - runscript 재실행
- 가정:
  - 비교 대상은 최신 `4.4.2__450m_60ms_x_noengine_drop`와 `1.0.1__450m_60ms_x_noengine_noprop_drop`
- 완료 조건:
  - 별도 velocity comparison PNG 생성
  - control surface check PNG 생성
  - summary CSV 생성
- 완료 항목:
  - `plot_c172x_drop_velocity_compare.py` 추가
  - `0616_drop_horizontal_vertical_speed_compare.png` 생성
  - `0616_drop_control_surface_check.png` 생성
  - summary CSV 생성
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-16 20:42] TASK-20260616-2042-001 — DONE

- 과업:
  - C172X no-engine/no-propeller 케이스의 실제 조종면 neutral 상태 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `지금 조종면들 입력값 말고 현재 상태가 뉴트럴 상태인지 확인해봐봐`
- 목적:
  - command 입력값이 아니라 실제 조종면 deflection이 neutral인지 확인
- 작업 범위:
  - 최신 `c172x_noengine` SI CSV 첫 행 확인
  - `c172x_noengine.xml`의 elevator/aileron/rudder actuator 정의 확인
- 제외 범위:
  - aircraft XML 수정
  - 새 시뮬레이션 실행
- 가정:
  - 확인 대상은 최신 `1.0.1__450m_60ms_x_noengine_noprop_drop` 결과
- 완료 조건:
  - 실제 elevator/aileron/rudder 초기 상태 판단
- 완료 항목:
  - elevator 실제 deflection은 `0.11459155902616465 deg`
  - left/right aileron 실제 deflection은 `0.0 deg`
  - rudder 실제 deflection은 `0.0 deg`
  - elevator non-zero 원인은 aircraft XML의 `<bias> 0.002 </bias>`로 확인
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-16 20:54] TASK-20260616-2054-001 — DONE

- 과업:
  - pointmass 중량을 0으로 만든 기본 기체 공력 확인용 C172X 추락 케이스 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `포인트매스로 들어간 것들이 있네 기체 내부 평형 맞추게 기체 중량정보만 냅두고 나머지 중량을 다 0으로 해서 기본 기체 공력 영향만 확인할수 있게 해줘`
- 목적:
  - `emptywt`와 기본 관성/공력은 유지하고 payload/외부 pointmass 영향을 제거해 기본 기체 공력만 확인
- 작업 범위:
  - no-engine/no-propeller 유지
  - elevator actuator bias 0 유지
  - 모든 `<pointmass>` weight를 0으로 설정한 aircraft variant 생성
  - 동일 초기조건으로 실행
- 제외 범위:
  - 원본 `c172x.xml` 수정
  - `emptywt`, 기본 inertia 직접 재계산
- 가정:
  - "기체 중량정보"는 `emptywt` 및 기존 mass_balance 기본 관성값을 의미하고, `<pointmass>` 항목은 payload/추가 질량으로 간주
- 완료 조건:
  - pointmass weight가 모두 0
  - engine/thruster 없음
  - actual elevator/aileron/rudder가 0
  - 실행 결과에서 roll/yaw 확인
- 완료 항목:
  - `c172x_noengine_surface_neutral_empty` variant 생성
  - 실행 ID `1.0.1__450m_60ms_x_empty_surface_neutral_drop` 생성
  - roll/yaw가 수치오차 수준으로 감소함을 확인
- 미완료 항목:
  - 180초 내 지면 접촉 없음
- 최종 상태:
  - DONE
## [2026-06-16 21:31] TASK-20260616-2131-001 — DONE

- 과업:
  - empty-airframe C172X pitch -20 deg, `ubody=60 m/s` 초기조건 케이스 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `ubody를 60으로 해줘`
- 목적:
  - 기본 기체 공력 확인용 no-engine/no-propeller/surface-neutral/pointmass-zero 조건에서 기수가 20도 아래를 바라보고 body x축 속도 `60 m/s`인 케이스 실행
- 작업 범위:
  - 기존 baseline 보존
  - `theta=-20.0`, `ubody=60.0` 초기조건 추가
  - 전용 runscript/wrapper 추가
  - 실행 및 plot/summary 생성
- 제외 범위:
  - 기존 `1.0__450m_60ms_x_drop_init.xml` 수정
- 가정:
  - `ubody=60`은 body x축 기준 속도 60 m/s를 의미
- 완료 조건:
  - 초기 로그에서 `pitch=-20 deg`, total speed `60 m/s` 확인
  - 실제 조종면 0 유지
  - 결과 summary/plot 생성
- 완료 항목:
  - `1.1__450m_pitchm20_ubody60_drop_init.xml` 추가
  - `1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop_run.xml` 추가
  - `run_c172x_empty_surface_neutral_pitchm20_ubody60_drop.py` 추가
  - 실행 ID `1.1.1__450m_pitchm20_ubody60_empty_surface_neutral_drop` 생성
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 10:44] TASK-20260617-1044-001 — DONE

- 과업:
  - C172X 기본 기체 pitch-up 원인으로 `Cm0` 영향 여부 확인
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `우리 지금 사용하는 기체에 받음각 0도일때 Cm0가 0이 아닌것같은 부분이 있어서 pitch가 -20에서 +50정도까지 올라가는것다는 이야기가 있는데 맞을까?`
- 목적:
  - 현재 사용하는 `c172x_noengine_surface_neutral_empty` 모델에서 받음각 0도, 조종면 0 상태에서도 nose-up pitching moment가 발생하는지 확인
- 작업 범위:
  - aircraft XML의 PITCH 축 aerodynamic coefficient 확인
  - 최신 `theta=-20`, `ubody=60` 로그 초기 상태 확인
- 제외 범위:
  - 모델 계수 수정
  - 신규 실행
- 가정:
  - 초기 `ubody=60`, `wbody=0`이므로 body 기준 초기 받음각은 거의 0으로 해석
- 완료 조건:
  - `Cm0` 값과 초기 pitch response를 근거로 판단
- 완료 항목:
  - `Cmo` 값 `0.1` 확인
  - `Cmalpha` 값 `-1.8` 확인
  - 초기 로그에서 `q_radps`가 양수로 증가하며 pitch가 상승 방향으로 반응함을 확인
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 10:49] TASK-20260617-1049-001 — DONE

- 과업:
  - `Cm0=0` C172X 비교 모델 생성 및 동일 조건 시뮬레이션
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - `그러면 Cm0=0으로 구성한 모델 하나 새로 만들어서 동일하게 시뮬레이션 돌려볼래?`
- 목적:
  - 기존 pitch-up 현상에서 `Cmo=0.1`의 영향 분리
- 작업 범위:
  - no-engine/no-propeller
  - surface neutral
  - pointmass weight 0
  - `Cmo=0.0`
  - 동일 초기조건 `theta=-20 deg`, `ubody=60 m/s`
- 제외 범위:
  - 다른 aerodynamic coefficient 수정
  - 기존 모델 덮어쓰기
- 가정:
  - 기존 `c172x_noengine_surface_neutral_empty`와 비교하기 위해 `Cmo` 외 조건은 동일하게 유지
- 완료 조건:
  - `Cmo=0` aircraft variant 생성
  - 같은 초기조건으로 JSBSim 실행
  - 결과 summary/plot 생성
- 완료 항목:
  - `c172x_noengine_surface_neutral_empty_cm0` variant 생성
  - `1.0.1__450m_pitchm20_ubody60_cm0zero_drop` 실행 성공
  - 고도 상승이 0 m로 감소함을 확인
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 13:00] CORRECTION-20260617-1300-001 — 정정

- 대상 기록:
  - `TASK-20260617-1258-001`
  - `TASK-20260617-1259-001`
- 정정 이유:
  - 앞선 두 기록이 append 패치 컨텍스트 문제로 파일 하단이 아닌 중간 위치에 삽입됨
- 기존 내용:
  - 두 기록의 작업 내용은 유효하나 시간 순서상 위치가 부적절함
- 정정 내용:
  - 기존 중간 삽입 기록은 삭제하지 않고, 아래 `TASK-20260617-1300-001`을 최신 하단 참조 기록으로 append함
- 영향 범위:
  - 작업 기록 조회 시 `TASK-20260617-1300-001`을 최신 참조로 사용
- 검증 결과:
  - `grep -n 'TASK-20260617-1259-001' docs/agent-log/TASK.md`로 중간 삽입 위치 확인
- 다음 작업:
  - 이후 `TASK.md` 기록은 마지막 고유 블록을 기준으로 append

## [2026-06-17 13:00] TASK-20260617-1300-001 — DONE

- 과업:
  - `c172x_noengine_surface_neutral_empty_cm0` 기체의 pitch +2.5 deg, `ubody=60 m/s` 추락 초기조건 생성 및 실행
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 초기 고도 `450 m`, pitch `2.5 deg`, 속도 `ubody=60 m/s` 조건을 만들고 추락 실행
- 목적:
  - `Cmo=0`, no-engine/no-propeller, surface-neutral, pointmass-zero 조건에서 pitch-up 초기 자세 응답 확인
- 작업 범위:
  - 기존 `theta=-20 deg` 케이스 보존
  - `theta=+2.5 deg`, `ubody=60 m/s`, altitude `450 m` initial XML 추가
  - 전용 runscript/wrapper 추가
  - JSBSim 실행 및 summary/plot/CSV 생성
- 제외 범위:
  - 기존 `1.0` 초기조건 수정
  - 추가 공력 계수 변경
  - Git commit 생성
- 가정:
  - `ubody=60`은 JSBSim body x축 속도
  - heading, roll, sideslip, wind는 기존 비교 케이스와 동일하게 `0`으로 유지
- 완료 조건:
  - initial XML에 altitude `450 m`, `theta=2.5 deg`, `ubody=60 m/s` 반영
  - JSBSim 실행 성공
  - 초기 로그에서 pitch와 속도 확인
  - 조종면/추력 0 유지 확인
- 완료 항목:
  - `1.1__450m_pitchp25_ubody60_drop_init.xml` 추가
  - `1.1__450m_pitchp25_ubody60_cm0zero_drop_run.xml` 추가
  - `run_c172x_empty_surface_neutral_cm0zero_pitchp25_ubody60_drop.py` 추가
  - 실행 ID `1.1.1__450m_pitchp25_ubody60_cm0zero_drop` 생성
  - 지면 접촉 이벤트로 `73.83333333 s`에 종료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 14:17] CORRECTION-20260617-1417-001 — 정정

- 대상 기록:
  - `TASK-20260617-1415-001`
  - `TASK-20260617-1416-001`
- 정정 이유:
  - 앞선 6DOF 로그 작업 TASK 기록들이 동일 문구 매칭 문제로 파일 하단이 아닌 중간 위치에 삽입됨
- 기존 내용:
  - 두 기록의 작업 내용은 유효하나 시간 순서상 위치가 부적절함
- 정정 내용:
  - 기존 중간 삽입 기록은 삭제하지 않고, 아래 `TASK-20260617-1417-001`을 최신 하단 참조 기록으로 append함
- 영향 범위:
  - 작업 기록 조회 시 `TASK-20260617-1417-001`을 최신 참조로 사용
- 검증 결과:
  - `grep -n`으로 중간 삽입 위치 확인
- 다음 작업:
  - `TASK.md` append에는 EOF 조건을 사용

## [2026-06-17 14:17] TASK-20260617-1417-001 — DONE

- 과업:
  - JSBSim 실행 시 6DOF 검증용 property 묶음을 별도 CSV로 저장
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - 사용자가 제시한 상태, 입력, 힘/모멘트, 가속도, 공력, 추력, 접촉/환경 property를 `<output>`에 지정해 CSV로 따로 저장
- 목적:
  - PX4 연동 비교와 6DOF 검증에서 상태값뿐 아니라 원인값까지 같은 timestep에서 추적 가능하게 함
- 작업 범위:
  - 기존 raw/SI CSV 출력 유지
  - 추가 `sixdof_raw` CSV 출력 생성
  - aircraft catalog에 실제 존재하는 property만 `<output>`에 포함
  - pitch +2.5 deg C172X Cm0=0 케이스로 실행 검증
- 제외 범위:
  - SI 단위 변환 컬럼 추가
  - 모든 wrapper의 summary 스키마 일괄 변경
  - Git commit 생성
- 가정:
  - 모델별로 없는 property는 JSBSim output에 넣지 않는 것이 안전함
  - no-engine C172X에서는 VTOL/engine indexed property 일부가 없는 것이 정상
- 완료 조건:
  - generated runscript에 기존 raw output과 별도 6DOF output이 함께 생성
  - 6DOF raw CSV 파일 생성
  - 상태/힘/모멘트/가속도/공력/접촉/환경 대표 컬럼 존재 확인
- 완료 항목:
  - `run_jsbsim_timestamped.py`에 `SIXDOF_VALIDATION_PROPERTIES` 추가
  - aircraft catalog 기반 property 필터링 추가
  - `logs/csv/sixdof_raw/...` 저장 경로 추가
  - pitch +2.5 deg wrapper summary에 `sixdof_raw_csv` 경로 추가
  - 실행 ID `1.1.3__450m_pitchp25_ubody60_cm0zero_drop`로 검증 완료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 14:33] TASK-20260617-1433-001 — DONE

- 과업:
  - `sixdof_raw` 로그에 JSBSim `position/*` property 전체 추가
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - catalog 이미지에 보이는 position 정보는 어떤 것을 쓸지 나중에 정할 수 있도록 `sixdof_raw`에 모두 추가
- 목적:
  - 별도 동역학 코드의 `(0,0,450)` local position 비교, lat/lon/alt 비교, ECEF/ECI 비교 등 다양한 위치 비교 방식을 후속 선택 가능하게 함
- 작업 범위:
  - `SIXDOF_VALIDATION_PROPERTIES`에 현재 C172X catalog 기준 `position/*` 30개 추가
  - 기존 raw/SI CSV 출력 유지
  - pitch +2.5 deg C172X Cm0=0 케이스로 실행 검증
- 제외 범위:
  - 어떤 position property를 최종 비교 기준으로 쓸지 결정
  - SI 변환 후처리 추가
  - Git commit 생성
- 가정:
  - 모델별 catalog 필터링이 유지되므로 다른 aircraft에서 없는 position property는 자동 제외됨
- 완료 조건:
  - generated runscript의 `sixdof_raw` output에 position property 30개 포함
  - 새 `sixdof_raw` CSV 생성
  - `from-start-neu-*` 등 주요 position 컬럼 존재 확인
- 완료 항목:
  - `position/h-sl-ft`부터 `position/from-start-neu-u-ft`까지 30개 position property 추가
  - 실행 ID `1.1.4__450m_pitchp25_ubody60_cm0zero_drop`로 검증 완료
  - 신규 `sixdof_raw` CSV에 `Time` 포함 103개 컬럼, 8861행 생성 확인
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE
## [2026-06-17 14:45] TASK-20260617-1445-001 — DONE

- 과업:
  - `sixdof_raw` 원본 보존과 별도 `sixdof_si` position 미터 변환 CSV 생성
- 대상 프로젝트:
  - `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용:
  - JSBSim 내부 property를 억지로 늘리지 않고, 별도 SI 변환 CSV에서 meter 단위 position 컬럼을 만들기로 함
- 목적:
  - 직접 코드의 `(0,0,450)` local position 비교에 사용할 수 있는 meter 단위 position CSV 생성
- 작업 범위:
  - `sixdof_raw`는 유지
  - `logs/csv/sixdof_si/`에 position 중심 SI CSV 추가
  - `from_start_neu_n_m`, `from_start_neu_e_m`, `from_start_neu_u_m`, `from_start_ned_d_m` 생성
  - pitch +2.5 deg C172X Cm0=0 케이스로 실행 검증
- 제외 범위:
  - 전체 force/moment/aero SI 변환
  - 최종 position 비교 기준 결정
  - Git commit 생성
- 가정:
  - 현재 단계에서는 position 비교용 SI 변환을 우선 제공
- 완료 조건:
  - `sixdof_si` CSV 생성
  - summary JSON에 `sixdof_si_csv` 경로 저장
  - raw ft 값과 SI m 값 변환 일치 확인
- 완료 항목:
  - `SIXDOF_SI_CSV_DIR` 추가
  - `convert_sixdof_raw_to_si()` 추가
  - wrapper summary에 `sixdof_si_csv` 추가
  - 실행 ID `1.1.5__450m_pitchp25_ubody60_cm0zero_drop` 검증 완료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE

## [2026-06-21 15:54] TASK-20260621-1554-001 — 부분 완료

- 과업: C172X 이륙 시뮬레이션의 3단계·4단계 우선 구축 및 현황 진단
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 전체 이륙·안정고도·30초 순항 제작을 중단하고, 3단계 회전과 4단계 초기상승을 먼저 구성하여 문제를 설명
- 작업 범위: 동력 포함 빈 탑승점질량 C172X 변형, 비자전 구형 지구 초기조건, 3·4단계 전용 runscript, 로그·plot 생성, 결과 분석
- 제외 범위: 안정고도 도달, 30초 순항, 자동조종 튜닝, 확인된 문제 수정
- 가정: 무게중심의 x축 이탈은 좌우 비대칭인 inertia/cg-y-in 문제로 해석
- 완료 조건: 55 kt 회전과 이륙 후 70 kt 가속 구간을 실행하고 실제 자세·상승률 문제를 로그로 확인
- 완료 항목: 3단계 16.508333초 실행, 4단계 19.225000초 실행, 로그·CSV·plot 생성
- 미완료 항목: 안전한 양의 상승률과 수평 자세를 만족하는 4단계 제어, 안정고도·30초 순항
- 최종 상태: PARTIAL — 진단 시나리오는 실행됐으나 4단계 완료 판정이 실제 안전 상승을 보장하지 않음


## [2026-06-21 18:45] TASK-20260621-1845-001 — 완료

- 과업: 첨부된 RKSS 14L 초기조건 설명을 토대로 C172X 이륙·안정고도·30초 순항 시나리오 재구축
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 사용자 정의 지구 모델 대신 JSBSim 기본 지구 사용
- 작업 범위: RKSS 14L 초기조건, 동력 포함 pointmass-zero C172X, 단계별 이륙, heading·altitude hold, 안정화 후 30초 순항, 로그·CSV·plot·문서
- 제외 범위: FlightGear GUI 연동, 외부 AIP 재조회, 공용 runner의 전역 기본 지구 설정 변경
- 가정: 첨부문서의 RKSS 좌표·방향·표고를 입력 근거로 사용
- 완료 조건: 기본 지구에서 정지·엔진 정지 초기상태, 55 kt 회전, 이륙, 1000 ft급 안정고도, 30초 안정 순항, abort 미발생
- 완료 항목: 초기조건과 runscript 생성, JSBSim 내장 지구 실행, 전체 상태 0~6 완료, raw·SI·6DOF CSV와 plot 생성
- 미완료 항목: 없음
- 최종 상태: COMPLETE


## [2026-06-23 08:56] TASK-20260623-0856-001 — 완료

- 과업: RKSS 14L C172X 시나리오에 순항 종료 후 엔진 정지와 지면 충돌까지 추가하고 QGroundControl 직접 연동 가능성 확인
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 시동·출발·이륙·순항 이후 엔진을 끄고 추락까지 실행, JSBSim만으로 QGC 표시 가능 여부 확인
- 작업 범위: 기존 5.6 상태기계 보존, 엔진·AP 정지, 조종면 중립화, 충돌 종료 이벤트, 로그·CSV·plot, 로컬 QGC·PX4 bridge 조사
- 제외 범위: QGC GUI 실행, PX4 SITL 실제 기동, MAVLink 변환기 신규 구현
- 가정: 추락은 엔진 정지 후 autopilot·수동 조종 입력·trim을 모두 중립화한 비제어 비행으로 정의
- 완료 조건: 순항 30초 완료 후 엔진 명령 정지, RPM 0 확인, 지면 접촉 이벤트와 종료 로그 생성, QGC 연동 구조 결론
- 완료 항목: 5.7 runscript 생성·실행, 엔진 정지 253.916667 s, 지면 충돌 277.616667 s, QGC 직접 연동 불가 확인
- 미완료 항목: PX4 SITL+QGC 실제 통합 실행
- 최종 상태: COMPLETE


## [2026-06-23 09:25] TASK-20260623-0925-001 — 완료

- 과업: `c172x_empty_cg_aligned` 전용 시나리오 폴더 분리
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: `c172x_empty_cg_aligned` 선택 시 초기조건이 없어서 대화형 runner가 실패하므로, `c172x` 폴더에서 필요한 시나리오를 분리
- 목적: `python3 run_jsbsim_timestamped.py` 대화형 실행에서 aircraft `c172x_empty_cg_aligned` 선택 후 초기조건과 runscript를 바로 선택 가능하게 함
- 작업 범위: RKSS 14L 기본 지구 이륙·순항 계열 `2.2`, `5.6`, `5.7` XML 전용 폴더 생성, 내부 initialize 경로 정리, 전용 README 추가
- 제외 범위: 원본 `scripts/c172x/` 삭제 또는 전체 과거 실험 XML 대량 이동, runner 선택 로직 변경, 실시간 3D 애니메이션 구현
- 가정: 현재 사용자 의도는 `c172x_empty_cg_aligned` 모델로 RKSS 14L 이륙·순항·엔진정지·추락 시나리오를 대화형으로 선택 가능하게 하는 것
- 완료 조건: `scripts/c172x_empty_cg_aligned/initial_condition/`과 `scripts/c172x_empty_cg_aligned/runscript/`가 존재하고, 새 경로로 5.7 JSBSim 실행이 성공
- 완료 항목: 전용 폴더 생성, `2.2` 초기조건 복사, `5.6`/`5.7` runscript 복사, 복사본 initialize 경로 변경, XML 검증, 5.7 실행 검증
- 미완료 항목: 실제 터미널에서 번호 입력 방식의 대화형 UI 수동 검증은 수행하지 않음
- 최종 상태: 완료
- 관련 기록: `PROGRESS-20260623-0925-001`, `DECISION-20260623-0925-001`, `INDEX-20260623-0925-001`
- Git commit: 없음

## [2026-06-23 09:50] TASK-20260623-0950-001 — 완료

- 과업: JSBSim runner에 선택형 실시간 3D 애니메이션 기능 추가
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: cmd에서 aircraft, 초기조건, 실행 스크립트를 선택한 뒤 실시간 3D 애니메이션을 추가할지 선택할 수 있도록 구성
- 목적: JSBSim 실행 중 생성되는 raw CSV를 실시간으로 읽어 3D 궤적 애니메이션 창을 표시
- 작업 범위: 공용 애니메이션 스크립트 추가, runner CLI 옵션 및 대화형 선택 추가, JSBSim `--realtime` 연결, 문서 갱신, 검증
- 제외 범위: QGroundControl/PX4/MAVLink 연동, FlightGear 3D 외부 시점 연동, 실제 WSLg GUI 창 수동 확인
- 가정: live 모드에서는 시뮬레이션을 빠르게 끝내는 것보다 실제 시간 속도에 맞춘 실시간 표시가 우선
- 완료 조건: `--live-3d`, `--no-live-3d` 옵션이 보이고, 비실시간 기존 실행이 유지되며, 애니메이션 스크립트가 기존 raw CSV를 읽을 수 있음
- 완료 항목: `scripts/live_trajectory_3d.py` 추가, `scripts/run_jsbsim_timestamped.py` live 옵션 추가, `scripts/README.md` 사용법 추가, 검증 수행
- 미완료 항목: 실제 GUI 창에서 live 애니메이션을 눈으로 확인하는 수동 검증
- 최종 상태: 완료
- 관련 기록: `PROGRESS-20260623-0950-001`, `DECISION-20260623-0950-001`, `TODO-20260623-0950-001`, `INDEX-20260623-0950-001`
- Git commit: 없음

## [2026-06-23 13:05] TASK-20260623-1305-001 — 완료

- 과업: jsbsim_workflow에서 CSV로 저장하는 JSBSim property를 유사 역할별로 분류한 Excel 파일 구성
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: jsbsim_workflow의 CSV 저장 property를 역할별로 분류한 엑셀파일 생성
- 목적: raw CSV, 6DOF 검증 CSV, SI 변환 대상 property를 탐색·검토하기 쉬운 카탈로그로 정리
- 작업 범위: scripts/run_jsbsim_timestamped.py의 OUTPUT_PROPERTIES, SIXDOF_VALIDATION_PROPERTIES, RAW_TO_SI_FIELDS, 기존 logs/csv/raw, logs/csv/sixdof_raw, scripts/**/runscript/*.xml, logs/generated_runscripts/**/*.xml 대조
- 제외 범위: JSBSim property 정의 자체 변경, runner 코드 변경, 기존 CSV 재생성, 공식 JSBSim taxonomy 외부 조회
- 가정: csv로 저장하는 property는 현재 workflow의 공용 timestamp runner가 저장하는 raw CSV 및 6DOF 검증 CSV property를 중심으로 하되, 기존 CSV 헤더와 XML output 정의도 cross-check 대상으로 포함
- 완료 조건: 역할별 분류 시트, SI 매핑 시트, CSV 헤더 대조 시트, XML source 시트를 포함한 .xlsx 생성 및 기본 검증 완료
- 완료 항목: /home/junyeopkwon/jsbsim_workflow/outputs/jsbsim_property_classification_20260623/jsbsim_csv_property_classification.xlsx 생성
- 미완료 항목: Codex view_image 도구의 UNC/WSL 경로 오류로 preview PNG를 직접 육안 확인하지는 못했고, PNG 형식·치수·non-white pixel 검사로 대체
- 최종 상태: 완료
- 관련 기록: PROGRESS-20260623-1305-001, DECISION-20260623-1305-001, INDEX-20260623-1305-001
- Git commit: 없음

## [2026-06-29 11:04] TASK-20260629-1104-001 — DONE

- 과업: 5.6 RKSS C172X runscript의 FlightGear 연동 사용 여부 확인
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: scripts/c172x_empty_cg_aligned/runscript/5.6__rkss14l_default_earth_takeoff_cruise30_run.xml 파일을 사용해 FlightGear 연동을 했는지 확인
- 목적: 이전 FlightGear 시각화 연동 명령과 관련 파일 식별
- 작업 범위: runscript, FlightGear output directive, README, bash history, 관련 문서 조사
- 제외 범위: JSBSim/FlightGear 실제 GUI 실행
- 가정: 사용자의 “flightgear 연동”은 JSBSim의 FLIGHTGEAR UDP output을 Windows FlightGear native-fdm 수신으로 연결한 구성을 의미
- 완료 조건: 사용된 runscript, output directive, 실행 명령 확인
- 완료 항목: bash history에서 JSBSim --realtime --logdirectivefile 명령 확인, fg_visual_5500.xml 설정 확인, c172x와 c172x_empty_cg_aligned 5.6 XML 차이 확인
- 미완료 항목: 현재 Windows FlightGear 실행 가능 여부는 확인하지 않음
- 최종 상태: DONE

## [2026-06-30 09:40] TASK-20260630-0940-001 — 완료

- 과업: `c172x_empty_cg_aligned` 기반 75 kg × 4명 탑승자 pointmass 변형 생성 및 5.6.1 고속 이륙 runscript 구성
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 기존 `2.2` init과 `5.6` runscript 조합에서 기체만 바꿔 PILOT, CO-PILOT, PASSENGER 1, PASSENGER 2에 각각 성인 남성 평균 75 kg pointmass를 넣고, 질량 증가로 속도 확보가 더 필요하면 5.6.1 버전으로 속도쪽만 증가
- 목적: CG-y 대칭을 유지하면서 4명 탑승 질량을 반영한 C172X 이륙·상승·30초 순항 가능성 확인
- 작업 범위: aircraft 변형 생성 스크립트, JSBSim aircraft 설치본, workflow 보관본, 5.6.1 higher-speed runscript, 실행 검증
- 제외 범위: elevator/aileron/rudder 명령 변경, autopilot/altitude logic 변경, payload 위치 변경, QGC/FlightGear GUI 검증
- 가정: 75 kg은 `165.346697 lb`로 환산하고, 기존 `PILOT`, `CO-PILOT`, `PASSENGER 1`, `PASSENGER 2` pointmass 위치를 유지
- 완료 조건: 새 aircraft가 JSBSim에서 실행되고, `2.2` init과 5.6.1 runscript로 STATE 6 30초 순항 완료
- 완료 항목: `c172x_4x75kg_cg_aligned` 생성·설치, 5.6 기존 실행 비교, 5.6.1 higher-speed runscript 생성, 5.6.1 실행 성공 및 STATE 5/6 확인
- 미완료 항목: 실제 GUI/FlightGear 시각화 검증 없음
- 최종 상태: 완료
- 관련 기록: `PROGRESS-20260630-0940-001`, `DECISION-20260630-0940-001`, `INDEX-20260630-0940-001`
- Git commit: 없음

## [2026-06-30 09:45] TASK-20260630-0945-001 — 완료

- 과업: 현재 75kg×4명 C172X 5.6.1 실행의 FlightGear 시각화 연동 여부 확인
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: "지금 이게 flightgear로 시각화 연동 되어 있나?"
- 목적: 현재 실행 경로가 FlightGear native-fdm/output directive를 사용했는지 확인
- 작업 범위: runner, console log, 기존 agent-log 확인
- 제외 범위: FlightGear GUI 실행, host IP 재탐색, JSBSim `--logdirectivefile` 연동 구현
- 완료 조건: 현재 실행이 FlightGear로 송신했는지 여부를 명확히 판단
- 완료 항목: `run_jsbsim_timestamped.py` 및 `06300939` console에서 FlightGear 관련 실행 흔적 없음 확인, 기존 2026-06-29 기록 재확인
- 최종 상태: 완료
- Git commit: 없음

## [2026-06-30 10:00] TASK-20260630-1000-001 — 완료

- 과업: JSBSim timestamp runner에 선택형 FlightGear 시각화 연동 옵션 추가
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: FlightGear로 보고 싶을 때만 선택할 수 있게 구성
- 목적: 기본 실행은 CSV/plot 생성으로 유지하고, 필요 시에만 JSBSim `--realtime`과 `--logdirectivefile`을 사용해 FlightGear native-fdm UDP 스트림 송신
- 작업 범위: `run_jsbsim_timestamped.py` CLI/대화형 선택 추가, `scripts/README.md` 사용법 append, 정적 검증 및 no-flightgear 회귀 실행
- 제외 범위: FlightGear Windows GUI 자동 실행, 실제 FlightGear 창 수동 확인, 현재 Windows host IP 자동 갱신
- 완료 조건: `--flightgear`, `--no-flightgear`, `--flightgear-logdirective` 옵션이 보이고, `--no-flightgear` 기존 실행이 정상이며, FlightGear 선택 시 JSBSim 명령에 `--realtime`과 `--logdirectivefile`이 들어가도록 구성
- 완료 항목: 선택형 FlightGear 옵션 구현, README 사용법 추가, help/문법/no-flightgear 실행 검증
- 미완료 항목: 실제 FlightGear GUI 연동 수동 검증
- 최종 상태: 완료
- Git commit: 없음

## [2026-06-30 10:30] TASK-20260630-1030-001 — 완료

- 과업: runner에서 live3d 선택 기능 제거 및 FlightGear 시각화 경로 유지
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: live3d 기능은 FlightGear로 시각화를 볼 예정이므로 제거하되, 있었다가 사용 중단했다는 내용은 남기고 Python helper 파일은 삭제하지 않음
- 목적: 시각화 경로를 FlightGear 선택형 스트림으로 단순화하고, 기존 Matplotlib live3d 구현은 보존 자료로 남김
- 작업 범위: `run_jsbsim_timestamped.py`에서 `--live-3d`/`--no-live-3d` 옵션과 live animator 호출 제거, `scripts/README.md`에 deprecated 기록 유지, `scripts/live_trajectory_3d.py` 파일 보존
- 제외 범위: FlightGear GUI 수동 검증, `scripts/live_trajectory_3d.py` 삭제
- 완료 조건: runner help에서 `--live-3d`가 사라지고 `--flightgear`는 유지되며, 기존 `--no-flightgear` 실행이 성공
- 완료 항목: live3d runner 노출 제거, README deprecated 섹션 작성, helper 파일 보존, 회귀 실행 검증
- 미완료 항목: 실제 FlightGear GUI 수신 확인
- 최종 상태: 완료
- Git commit: 없음

## [2026-06-30 11:19] CORRECTION-20260630-1119-001 — 정정

- 대상 기록: `TASK-20260630-1118-001`
- 정정 이유: Windows PowerShell `Add-Content` 기본 인코딩으로 append되어 한글이 깨져 보이는 기록이 생성됨
- 기존 내용: 직전 `TASK-20260630-1118-001` 항목은 인코딩 문제로 일부 환경에서 mojibake로 표시될 수 있음
- 정정 내용: 3D trajectory plot의 Z축 음수 눈금 제거 작업은 완료됨. 작업 범위는 `/home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py`의 `plot_trajectory()` 함수 수정과 기존 `/home/junyeopkwon/jsbsim_workflow/plots/c172x_4x75kg_cg_aligned/5.6.1__rkss14l_default_earth_takeoff_cruise30_higher_speed/5.6.8__rkss14l_default_earth_takeoff_cruise30_higher_speed_trajectory_3d_06301107.png` 재생성임
- 영향 범위: 기록 문서 표시 품질에만 영향. 코드 변경과 PNG 재생성 결과에는 영향 없음
- 검증 결과: Python 문법 검사 통과, 기존 SI CSV 36002행으로 trajectory PNG 재생성 성공
- 다음 작업: 향후 기록 append 시 UTF-8 명시

## [2026-06-30 11:28] TASK-20260630-1128-001 — 완료

- 과업: 인코딩이 깨진 2026-06-30 11:18 작업 기록 제거
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 정정 기록이 있으므로 혼란 방지를 위해 깨진 기록 블록 삭제
- 작업 범위: `docs/agent-log/TASK.md`, `docs/agent-log/PROGRESS.md`, `docs/agent-log/INDEX.md`의 `2026-06-30 11:18` 깨진 블록
- 제외 범위: 기존 정상 기록, 2026-06-30 11:19 정정 기록, 코드 및 plot 파일
- 완료 조건: 깨진 11:18 블록이 제거되고 세 파일이 UTF-8로 읽힘
- 완료 항목: 사용자 승인에 따라 깨진 11:18 블록 삭제
- 미완료 항목: 없음
- 최종 상태: 완료

## [2026-06-30 11:39] TASK-20260630-1139-001 — 완료

- 과업: `c172x_4x75kg_cg_aligned` interactive 실행용 scripts 폴더 추가
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: interactive 실행에서 `c172x_4x75kg_cg_aligned` 선택 시 `No init XML options found`가 발생하는 문제 확인 및 수정
- 작업 범위: `scripts/c172x_4x75kg_cg_aligned/initial_condition`, `scripts/c172x_4x75kg_cg_aligned/runscript` 생성 및 기존 RKSS 14L XML 복사
- 제외 범위: JSBSim aircraft XML 재생성, 시뮬레이션 재실행, runner 로직 변경
- 가정: `c172x_4x75kg_cg_aligned`는 기존 `scripts/c172x`의 `2.2` init과 `5.6`, `5.6.1` runscript를 동일하게 사용하되 interactive 선택 가능성을 위해 전용 폴더에 복사본을 둠
- 완료 조건: runner의 `discover_init_files()`와 `discover_runscripts()`가 `c172x_4x75kg_cg_aligned`용 XML을 반환함
- 완료 항목: 전용 init/runscript 폴더와 XML 3개 생성, discovery 검증 완료
- 미완료 항목: 실제 300초 시뮬레이션 재실행은 생략
- 최종 상태: 완료

## [2026-06-30 11:47] TASK-20260630-1147-001 — 완료

- 과업: FlightGear 선택 실행 시 JSBSim `SIGFPE` 원인 조사 및 interactive 기본 planet 수정
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: interactive 실행에서 FlightGear stream `y` 선택 후 JSBSim이 `SIGFPE`로 종료되고 FlightGear가 보이지 않는 문제 확인
- 작업 범위: 최신 console log 확인, FlightGear output + planet 조합 분리 검증, `scripts/run_jsbsim_timestamped.py`의 interactive 기본 planet 수정
- 제외 범위: Windows FlightGear 자동 실행 기능 추가, 실제 FlightGear GUI 수신 장면 확인, full 300초 시뮬레이션 재실행
- 가정: 최근 시나리오 기준은 JSBSim default Earth이며, custom nonrotating spherical earth는 명시적으로 `--planet <xml>`을 줄 때만 사용함
- 완료 조건: `--planet` 미지정 interactive 실행에서 `planet_path=None`이 되어 JSBSim default Earth가 사용됨
- 완료 항목: `args.planet is None` 기본값을 `None`으로 변경, Python 문법 검사 통과, `resolve_selection()` 기본값 검증, `--planet` 없이 FlightGear output 짧은 실행에서 SIGFPE 미발생 확인
- 미완료 항목: 실제 Windows FlightGear GUI 수신 확인
- 최종 상태: 완료

## [2026-06-30 14:25] TASK-20260630-1425-001 — 완료

- 과업:
  - ADS JSBSim 모델을 jsbsim_workflow에서 진행할 수 있도록 폴더 구성
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - 앞서 만든 ADS Lift+Cruise eVTOL JSBSim XML 초안을 토대로 jsbsim_workflow 폴더에 넣어두고 진행할 수 있도록 구성
- 목적:
  - ADS 기체 XML, engine XML, 초기조건, runscript, 결과 폴더를 workflow 규칙에 맞춰 정리하여 후속 실행/검증을 시작하기 쉽게 함
- 작업 범위:
  - 기존 jsbsim_workflow 구조 및 scripts/README.md 규칙 확인
  - /home/junyeopkwon/jsbsim/aircraft/ADS와 /home/junyeopkwon/jsbsim/engine/ADS_*.xml 복사본을 workflow에 배치
  - scripts/ADS/initial_condition 및 scripts/ADS/runscript 구성
  - ADS 결과/로그/플롯 폴더 생성
  - ADS workflow README와 install note 작성
  - XML 정적 파싱 및 참조 누락 확인
- 제외 범위:
  - JSBSim 실행
  - hover 결과 검증
  - runner 코드 수정
  - 기존 c172x/F450 workflow 변경
- 가정:
  - runnable 원본은 /home/junyeopkwon/jsbsim 아래에 유지하고, jsbsim_workflow에는 추적/실행 선택용 복사본을 둠
  - 기존 runner 구조에 맞춰 aircraft별 scripts 폴더를 사용함
- 완료 조건:
  - ADS aircraft/engine/script/output 폴더가 jsbsim_workflow 내부에 존재
  - workflow runscript가 workflow initial_condition 파일을 참조
  - XML 정적 파싱과 참조 파일 존재 확인 성공
- 완료 항목:
  - aircraft_variants/ADS 구성
  - engine_variants/ADS 구성
  - scripts/ADS/initial_condition/1.0__gimpo_ground_init.xml 구성
  - scripts/ADS/runscript/1.0__gimpo_30m_hover_run.xml 구성
  - logs/csv/raw/ADS, logs/csv/si/ADS, logs/console/ADS, logs/generated_runscripts/ADS, plots/ADS, results/ADS 생성
  - scripts/ADS/README.md 및 aircraft_variants/ADS/WORKFLOW_INSTALL.md 작성
  - workflow ADS XML 16개 정적 파싱 성공
  - workflow 내부 참조 누락 0개 확인
- 미완료 항목:
  - JSBSim 실제 실행은 수행하지 않음
  - hover 성능과 결과 생성은 검증하지 않음
- 최종 상태:
  - 완료
- 관련 기록:
  - PROGRESS-20260630-1425-001
  - DECISION-20260630-1425-001
  - TODO-20260630-1425-001

## [2026-06-30 14:28] TASK-20260630-1428-001 — 완료

- 과업:
  - jsbsim_workflow Git 추가 가능 여부 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - jsbsim_workflow를 사용자 Git에 추가할 수 있는지 확인
- 목적:
  - 현재 Git 저장소 포함 여부와 가능한 Git 관리 방식을 판단
- 작업 범위:
  - /home/junyeopkwon 및 /home/junyeopkwon/jsbsim_workflow의 Git 저장소 여부 확인
  - remote 설정 여부 확인
  - jsbsim_workflow 내부 .git 및 .gitignore 존재 여부 확인
- 제외 범위:
  - git init 실행
  - git add/commit/push 실행
  - 원격 저장소 생성 또는 연결
- 가정:
  - 사용자의 질문은 실제 Git 변경 전 가능 여부 확인으로 해석함
- 완료 조건:
  - 현재 Git 상태와 가능한 다음 선택지 파악
- 완료 항목:
  - /home/junyeopkwon은 Git 저장소로 인식되지 않음 확인
  - /home/junyeopkwon/.git은 존재하지만 비어 있어 유효한 Git 저장소가 아님 확인
  - /home/junyeopkwon/jsbsim_workflow 내부 .git 없음 확인
  - /home/junyeopkwon/jsbsim_workflow 내부 .gitignore 없음 확인
- 미완료 항목:
  - 실제 Git 저장소 초기화 및 원격 연결은 사용자 확인 전 수행하지 않음
- 최종 상태:
  - 가능함. 권장 방식은 jsbsim_workflow를 별도 Git 저장소로 초기화하는 것
- 관련 기록:
  - PROGRESS-20260630-1428-001


## [2026-06-30 14:34] TASK-20260630-1434-001 — DONE

- 과업: jsbsim_workflow 로컬 Git 저장소 추가
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 사용자의 Git에 jsbsim_workflow를 추가
- 관련 파일: /home/junyeopkwon/jsbsim_workflow/.gitignore, /home/junyeopkwon/jsbsim_workflow/docs/agent-log/
- 작업 범위: Git 저장소 초기화, main 브랜치 설정, 추적 대상 선별, 초기 커밋 생성, 작업 기록 커밋
- 제외 범위: 원격 저장소 생성, remote 등록, push 실행, JSBSim 실행 검증
- 가정: 사용자가 말한 내 깃은 현재 로컬 환경의 /home/junyeopkwon/jsbsim_workflow를 독립 Git 저장소로 관리하는 의미로 처리
- 완료 조건: 로컬 Git 저장소가 생성되고, 필요한 소스 및 문서 파일이 커밋되며, 대용량 실행 산출물은 제외됨
- 완료 항목: .gitignore 생성, git init, main 브랜치 설정, 초기 커밋 생성, 로컬 사용자 정보 설정
- 미완료 항목: 원격 저장소 URL이 없어 remote 등록 및 push는 수행하지 않음
- 최종 상태: DONE


## [2026-06-30 15:09] TASK-20260630-1509-001 — DONE

- 과업: ADS 산출물 저자 표기 변경
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: ADS 만든 파일들의 저자를 junyeopkwon으로 변경
- 목적: ADS XML 및 문서의 작성자 메타데이터를 사용자명으로 통일
- 작업 범위: workflow ADS snapshot의 ADS 관련 XML 및 Markdown 파일
- 제외 범위: 대용량 실행 산출물, ADS와 무관한 workflow_all_cases_initial_settings.xlsx 변경, JSBSim 실제 실행 검증
- 가정: 저자 변경은 파일 내부 메타데이터와 Git 커밋 작성자 설정 기준으로 처리
- 완료 조건: ADS 대상 파일에 junyeopkwon 저자 표기가 존재하고 OpenAI Codex 저자 표기가 남지 않음
- 완료 항목: ADS.xml의 author 태그 변경, author 태그가 없는 ADS XML에는 Author 주석 추가, ADS Markdown에는 Author 행 추가
- 미완료 항목: JSBSim 실행 검증은 수행하지 않음
- 최종 상태: DONE


## [2026-06-30 15:20] TASK-20260630-1520-001 — DONE

- 과업: ADS 30 m hover 실행 로그 해석
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 사용자가 제공한 ADS sixdof_raw CSV 로그가 기존 미션 설명과 다르게 보인다는 지적 확인
- 목적: runscript 이벤트 의도와 실제 로그 결과 차이를 식별
- 작업 범위: 1.0.1__gimpo_30m_hover_sixdof_raw_06301505.csv, ADS runscript, ADS initial condition, ADS mass/propulsion 관련 파일
- 제외 범위: ADS XML 수정, JSBSim 재실행, 추력 모델 재보정
- 가정: 제공된 CSV가 현재 ADS 1.0 gimpo 30m hover 실행 결과를 대표함
- 완료 조건: 로그 기준 실제 고도/추력/WOW 상태와 30 m 이벤트 발동 여부를 확인
- 완료 항목: 로그 통계 산출, 시간대별 상태 확인, 원인 후보 식별
- 미완료 항목: 수정안 적용 및 재실행 검증
- 최종 상태: DONE


## [2026-06-30 15:27] TASK-20260630-1527-001 — DONE

- 과업: ADS JSBSim 구현 모터/프로펠러 기준 비행 가능 중량 추정
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: JSBSim에 구현된 모터와 프로펠러를 쓸 경우 기체 무게를 어느 정도까지 날릴 수 있는지 추정
- 목적: 현재 ADS lift motor/prop placeholder와 실행 로그 기준의 중량 한계 산정
- 작업 범위: 제공된 sixdof_raw 로그의 lift thrust, ADS_lift_motor.xml, ADS_lift_prop.xml, ADS_mass.xml
- 제외 범위: 새 시뮬레이션 실행, 모터/프롭 모델 수정, 실제 제조사 데이터 반영
- 가정: 제공 로그에서 관측된 최대 4개 리프트모터 총추력 38.734 lbf를 현재 구현 기준 사용 가능한 추력으로 간주
- 완료 조건: 절대 hover 한계와 권장 MTOW 범위를 kg 단위로 제시
- 완료 항목: 총추력 kgf 환산, T/W margin별 가능 중량 계산
- 미완료 항목: full throttle 별도 sweep 검증
- 최종 상태: DONE


## [2026-06-30 15:36] TASK-20260630-1536-001 — DONE

- 과업: JSBSim 엔진/모터/프로펠러 정의 확인
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: JSBSim에서 사용 중인 모터와 프로펠러가 무엇인지 확인
- 목적: ADS에 적용 가능한 기존 JSBSim motor/prop 후보 파악
- 작업 범위: /home/junyeopkwon/jsbsim/engine, F450, c172p_2kg_vtol, ZLT-NT, ADS propulsion 참조
- 제외 범위: 모델 수정, 추력 sweep 실행, 외부 제조사 데이터 조사
- 가정: 로컬 /home/junyeopkwon/jsbsim 트리의 engine XML을 현재 사용 가능한 JSBSim 정의로 간주
- 완료 조건: 엔진/프로펠러 XML 타입 분류와 ADS/F450 실제 참조 조합 확인
- 완료 항목: brushless_dc_motor, electric_engine, propeller, rotor 등 XML 루트 타입 분류 및 주요 파일 확인
- 미완료 항목: 각 후보의 정적 추력 성능 실행 검증
- 최종 상태: DONE


## [2026-06-30 18:26] TASK-20260630-1826-001 — DONE

- 과업: ADS_mini 10 m hover/landing 테스트 구성 및 실행
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 시동 후 이륙, 10 m에서 10초 호버링, 착륙 후 시동끄기까지 스크립트 생성 및 테스트
- 목적: DJI_E305 + DJI_9450 기반 1 kg ADS_mini 스케일 모델로 JSBSim hover workflow 검증
- 작업 범위: workflow snapshot and scripts, ADS_mini aircraft XML, initial condition, runscript, 실행 로그 분석
- 제외 범위: 20 kg ADS 원형 모델 재보정, 고정익 전환 비행, Git commit, GitHub push
- 가정: ADS_mini는 20 kg ADS의 동역학 상사 모델이 아니라 JSBSim 구성과 hover mission 검증용 1 kg 테스트 모델
- 완료 조건: JSBSim 실행이 정상 종료되고 10 m 부근 10초 호버와 착륙 후 throttle 0 상태가 CSV에서 확인됨
- 완료 항목: ADS_mini 생성, DJI_E305 + DJI_9450 추진계 적용, 10 m hover/landing runscript 생성, JSBSim 실행 검증
- 미완료 항목: Git commit, GitHub publish, 20 kg ADS 재보정
- 최종 상태: DONE


## [2026-06-30 18:36] TASK-20260630-1836-001 — DONE

- 과업: ADS_mini 적용 runscript 이벤트 설명
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 현재 적용한 ADS_mini runscript를 이벤트별로 정리
- 작업 범위: scripts/ADS_mini/runscript/1.0__gimpo_10m_hover_land_run.xml 확인 및 설명
- 제외 범위: 파일 수정, 재실행, 튜닝
- 완료 항목: runscript 이벤트 순서와 설정값 확인
- 최종 상태: DONE


## [2026-06-30 18:48] TASK-20260630-1848-001 — DONE

- 과업: ADS_mini XML 의사코드 설명 자료 작성
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 현재 기체 XML들을 사용자가 제시한 스타일의 의사코드로 각각 설명하는 자료 작성
- 목적: JSBSim ADS_mini XML 구조를 기본 프로그래밍 지식이 있는 사람이 구현 흐름처럼 이해할 수 있게 문서화
- 작업 범위: ADS_mini aircraft XML 9개, initial condition XML, runscript XML 설명
- 제외 범위: 모델 XML 수정, 재실행 테스트, Git commit
- 가정: 현재 기체 XML은 최근 생성 및 테스트한 ADS_mini를 의미함
- 완료 조건: 각 XML별 역할과 처리 흐름을 한국어 의사코드로 정리한 Markdown 문서 생성
- 완료 항목: ADS_mini_xml_pseudocode.md 생성
- 미완료 항목: Git commit 및 GitHub publish
- 최종 상태: DONE

## [2026-07-01 00:00] TASK-20260701-0000-ADS0 — 완료

- 과업: ADS 0 zero-value 기체 템플릿 XML 구성
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 기존 ADS 분리형 XML 구조를 기준으로, 임의 수치 대신 값/테이블 입력 위치를 모두 0으로 둔 `ADS 0` 템플릿을 만든다.
- 목적: 실제 제원과 공력/추력/질량 데이터가 확보되면 바로 채워 넣을 수 있는 JSBSim 기체 XML 골격 확보
- 작업 범위: `aircraft_variants/ADS_0`, `engine_variants/ADS_0` XML 생성
- 제외 범위: JSBSim 실행, runscript 작성, `/home/junyeopkwon/jsbsim` 실행용 트리 복사, commit/push
- 가정: 파일/폴더명은 공백 대신 JSBSim 및 Git에서 안전한 `ADS_0` 형식으로 저장한다. property 이름과 참조 경로는 기능 연결을 위해 변경하지 않는다.
- 완료 조건: XML 파일 생성, 내부 파일 참조 `ADS_0_*` 반영, 수치/테이블 값 0 처리, XML 파싱 성공
- 완료 항목: 14개 XML 생성 및 파싱 검증 완료
- 미완료 항목: 실제 제원 입력, JSBSim 실행 검증, 실행용 JSBSim aircraft/engine 트리 반영
- 최종 상태: 완료

## [2026-07-19 23:35] TASK-20260719-2335-001 — DONE

- 과업:
  - C172X 4x75kg 탑승객 조건에서 김포 lat/lon, 고도 450 m, 동쪽 heading, body u=60 m/s 초기조건 및 무추력 추락/활공 runscript 생성
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - c172x 계열에서 탑승객 75 kg 4명이 반영된 XML을 사용하고, 김포공항 lat/lon에서 고도 450 m, heading 동쪽, u=60 m/s, v/w=0 초기조건을 구성
  - runscript 2개 생성: 조종면 중립 무추력 추락, heading 유지/trim 활공 무추력 추락
- 작업 범위:
  - 기존 c172x_4x75kg_cg_aligned aircraft variant 재사용
  - scripts/c172x_4x75kg_cg_aligned/initial_condition 및 runscript 아래 새 XML 추가
  - JSBSim runner 실행 검증
- 제외 범위:
  - 기존 aircraft mass/CG 재생성
  - FlightGear 실시간 시각화
  - pitch trim 최적화
- 가정:
  - 김포공항 고도 450 m는 김포 lat/lon 위치에서 항공기 초기 altitude를 450 m로 설정한다는 의미로 해석
  - 지면 접촉 검출을 위해 기존 김포 초기조건의 terrain elevation 38 ft를 유지
- 완료 조건:
  - XML well-formed 검증 통과
  - 두 runscript가 JSBSim runner에서 실행되고 landing gear WOW 지면 접촉 시 종료
- 완료 항목:
  - 초기조건 XML 1개 생성
  - 중립 조종면 무추력 추락 runscript 1개 생성
  - heading hold + pitch trim 무추력 활공 runscript 1개 생성
  - 두 runscript 실행 검증 완료
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE

## [2026-07-19 23:50] TASK-20260719-2350-001 — DONE

- 과업:
  - C172X 4x75kg zero-propulsion aircraft variant 생성 및 동일 6.0/6.1 조건 실행 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - 추력을 아예 없앤 상태에서도 조종면으로 heading 유지가 가능한지 판단하고, 가능하면 propulsion을 zero dummy로 구성한 별도 aircraft를 만들어 동일 형태로 진행
- 작업 범위:
  - c172x_4x75kg_cg_aligned 기반 zero-propulsion aircraft variant 생성
  - 새 aircraft용 6.0 중립 무추력 추락 runscript 생성
  - 새 aircraft용 6.1 heading hold + pitch trim 활공 runscript 생성
  - JSBSim runner 실행 검증 및 propeller/thrust 제거 확인
- 제외 범위:
  - heading hold gain 튜닝
  - pitch trim 최적화
  - FlightGear 실시간 시각화
- 가정:
  - zero dummy propulsion은 engine/thruster를 제거하고 fuel tank, mass, aerodynamics, FCS, ground reactions를 유지하는 방식으로 해석
- 완료 조건:
  - 새 aircraft XML이 JSBSim에서 로드됨
  - 6.0/6.1이 지면 접촉 시 종료됨
  - engine/propeller rpm 및 thrust가 전 구간 0 또는 catalog/output에서 제거됨
- 완료 항목:
  - c172x_4x75kg_cg_aligned_zeroprop aircraft variant 생성
  - workflow 및 JSBSim install tree 양쪽에 variant 배치
  - 초기조건 1개와 runscript 2개 생성
  - 6.0/6.1 실행 검증 완료
- 미완료 항목:
  - generator script 추가는 sandbox helper 오류로 완료하지 못함
- 최종 상태:
  - DONE

## [2026-07-20 09:10] TASK-20260720-0910-001 — DONE

- 과업:
  - JSBSim runner 상세 plotting 출력 구조 개편
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - 기존 3D plot 1개와 통합 states plot만 만드는 방식 외에, ploting 폴더 아래 aircraft/run별 폴더를 만들고 JSBSim CSV에 저장된 모든 property를 시간 그래프로 개별 저장
  - ft/rad 단위는 m, m/s, deg 등 변환 그래프도 추가 저장
  - runscript event 시작점은 빨간 세로선으로 표시하되 단일 이벤트면 표시 생략
  - 6DOF 동역학 관점에서 함께 봐야 할 property 조합은 dual-axis plot으로 별도 구성
- 작업 범위:
  - scripts/run_jsbsim_timestamped.py plotting 기능 확장
  - 기존 plots/ 요약 출력 유지
  - 새 ploting/ 상세 출력 추가
  - zero-prop 6.1 run으로 검증
- 제외 범위:
  - 기존 CSV output property 목록 재설계
  - interactive plot UI
  - ploting 폴더명 교정
- 가정:
  - 사용자가 명시한 ploting 철자를 그대로 사용
  - 이벤트 라벨은 E0, E1, E2 형식만 제공하고 의미 설명은 별도 정리하지 않음
- 완료 조건:
  - runner 문법 검사 통과
  - 실제 JSBSim 실행 후 ploting/<aircraft>/<run_id>/ 아래 상세 plot 생성
  - 이벤트가 2개 이상이면 빨간 marker와 events.csv 생성
- 완료 항목:
  - raw/SI/sixdof raw/sixdof SI 개별 time-series plot 생성
  - raw 및 sixdof raw 단위 변환 plot 생성
  - 6DOF dual-axis plot 생성
  - detailed plot count 출력 추가
  - 검증 실행 완료
- 미완료 항목:
  - 이미지 뷰어를 통한 시각 검토는 UNC helper 오류로 수행하지 못함
- 최종 상태:
  - DONE


## [2026-07-20 09:20] CORRECTION-20260720-0920-001 ? ??

- ?? ??:
  - TASK-20260720-0910-001
- ?? ??:
  - ??. ?? TASK ??? ?? append?.
- ?? ??:
  - JSBSim runner ?? plotting ?? ?? ?? ?? ??
- ?? ??:
  - ?? ???
- ?? ??:
  - ??
- ?? ??:
  - TASK.md tail ?? ??
- ?? ??:
  - ??

## [2026-07-20 10:00] TASK-20260720-1000-001 — DONE

- 과업: ploting 위치 계열 y축 오프셋 표시 수정
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 위치(ft 또는 m) 그래프에서 Matplotlib의 큰 기준값 오프셋(+3.868e6 등)이 보이지 않도록 y축 표현을 수정
- 관련 파일: scripts/run_jsbsim_timestamped.py
- 작업 범위: 상세 ploting 개별 time series 및 2중 y축 그래프의 y축 포매팅, ECI/ECEF 절대 위치 계열 표시 방식
- 제외 범위: 기존 JSBSim runscript, aircraft XML, CSV 스키마, 기존 통합 plots 출력 구조 변경
- 가정: eci/ecef처럼 지구 중심 절대 좌표는 절대값 자체보다 초기 조건 대비 변화량이 시간 응답 해석에 더 적합함
- 완료 조건: eci_z_m 같은 절대 위치 계열이 초기값 기준 delta로 표시되고 y축 offset/scientific offset이 비활성화될 것
- 완료 항목: ScalarFormatter(useOffset=False) 적용, 절대 위치 계열 delta 변환 helper 추가, 단일/2중 y축 plot에 적용, 기존 CSV 기반 ploting 재생성 검증
- 미완료 항목: 없음
- 최종 상태: 완료

## [2026-07-20 10:57] TASK-20260720-1057-001 — 계획 제시

- 과업:
  - C172X 4x75kg 4명 탑승 정상 이륙 runscript 생성 전 설계안 제시
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - /home/junyeopkwon/jsbsim/scripts/c1723.xml, Purdue Aviation Cessna 172 자료, D:/ADSystem/N13701-V-Speeds.pdf를 기준으로 별도 이륙 스크립트를 만들기 전 구성 방향을 먼저 제시
- 작업 범위:
  - 기존 c1723.xml 이벤트 구조 조사
  - c172x_4x75kg_cg_aligned 변형 기체 확인
  - 기존 jsbsim_workflow takeoff runscript 관례 확인
  - 이륙 속도 기준과 이벤트 상태 설계안 정리
- 제외 범위:
  - 새 XML runscript 생성
  - JSBSim 실행 검증
  - workflow_all_cases_initial_settings.xlsx 갱신
- 가정:
  - 사용자가 말한 c172x_75kg 4명 기체는 aircraft_variants/c172x_4x75kg_cg_aligned를 의미함
  - 정상 이륙 기준이므로 flap 0 deg를 기본안으로 사용하고, short-field/soft-field용 10 deg flap은 별도 옵션으로 둠
- 완료 조건:
  - 파일 생성 전 사용할 aircraft, 초기조건, 이벤트 상태, 속도 기준, 검증 기준을 사용자에게 제시
- 완료 항목:
  - 기존 c1723.xml의 51 kt autopilot rotate 방식과 workflow 5.6 계열 상태 기계 방식 비교
  - Purdue C172 KIAS 값과 N13701 PDF mph 값을 knots 기준으로 정리
  - 새 runscript 설계안 작성
- 미완료 항목:
  - 사용자 승인 후 실제 runscript 생성 필요
- 최종 상태:
  - 계획 제시 완료

## [2026-07-20 11:31] TASK-20260720-1131-001 — DONE

- 과업:
  - C172X 4x75kg 4명 탑승 정상 이륙 후 500 m AGL 상승 및 동일 방향 30초 cruise runscript 생성
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned/initial_condition/2.2__rkss_14l_default_earth_init.xml을 initial로 사용해 새 이륙 스크립트 생성
- 작업 범위:
  - 신규 runscript XML 생성
  - Stage 2 nose-lightening 제거
  - Vr 55 KIAS rotate, 500 m AGL 상승, 동일 heading 30초 cruise 구현
  - XML parse 및 JSBSim 실행 검증
- 제외 범위:
  - 기존 5.6/5.6.1 runscript 수정
  - aircraft model, autopilot model, 초기조건 파일 수정
- 가정:
  - 500 m는 AGL 기준이며 JSBSim 조건식은 ft 단위 position/h-agl-ft로 작성
  - 동일 방향은 initial psi=135.01 deg heading 유지로 해석
- 완료 조건:
  - STATE 6 완료 이벤트가 cruise 시작 후 약 30초 뒤 실행되고 abort 이벤트가 실행되지 않을 것
- 완료 항목:
  - scripts/c172x_4x75kg_cg_aligned/runscript/5.8__rkss14l_normal_takeoff_climb500m_cruise30_run.xml 생성
  - XML parse 검증 통과
  - JSBSim run 5.8.3 실행 완료
  - rotate 55.02 KIAS, 500 m 도달, 30.01초 cruise, abort 미발생 확인
- 미완료 항목:
  - 없음
- 최종 상태:
  - 완료

## [2026-07-20 11:47] TASK-20260720-1147-001 — DONE

- 과업:
  - 상세 ploting 그래프의 event marker 가독성 개선
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - 그래프 안 legend가 보기 어렵고 E0/E1 위치가 불명확하므로 legend를 그래프 밖으로 빼고, 이벤트 위치와 구간을 그래프 위쪽에 표시
- 작업 범위:
  - scripts/run_jsbsim_timestamped.py의 상세 time-series plotting 이벤트 marker 렌더링 개선
  - 기존 5.8.3 run 데이터로 상세 ploting 재생성
- 제외 범위:
  - JSBSim 물리 모델 및 runscript 변경
  - 기존 CSV/console 원본 데이터 변경
- 완료 조건:
  - 이벤트 점선이 legend에 들어가지 않을 것
  - E0 등 event label과 time이 점선 위쪽에 표시될 것
  - 구간이 충분히 넓은 경우 상단 rail에 E0-E1 같은 구간 표시가 나타날 것
  - dual-axis 데이터 legend가 plot 밖 오른쪽에 위치할 것
- 완료 항목:
  - add_event_lines 개선
  - legend_outside helper 추가
  - single/dual time-series save layout 조정
  - 기존 5.8.3 상세 ploting 재생성
- 미완료 항목:
  - 없음
- 최종 상태:
  - 완료

## [2026-07-20 11:52] TASK-20260720-1152-001 — DONE

- 과업:
  - 상세 ploting event marker 상단 겹침 재개선
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - 이전 수정 후에도 E label, rail, title이 겹쳐 보여 추가 개선 필요
- 작업 범위:
  - event marker를 본 그래프 축 밖 annotation이 아니라 별도 event strip subplot으로 분리
  - 기존 5.8.3 상세 ploting 재생성
- 제외 범위:
  - JSBSim 실행 재수행
  - runscript 및 CSV 원본 수정
- 완료 조건:
  - title, event label, 구간 rail, 본 plot 영역이 서로 다른 수직 공간을 사용하도록 분리
  - layout warning 없이 ploting 재생성
- 완료 항목:
  - add_event_strip 추가
  - add_event_lines를 본 plot 점선만 그리도록 단순화
  - single/dual time-series plot을 event strip + data axis 2행 구조로 변경
  - tight_layout 경고를 없애기 위해 subplots_adjust 명시 배치 적용
- 미완료 항목:
  - 없음
- 최종 상태:
  - 완료

## [2026-07-20 12:04] TASK-20260720-1204-001 — DONE

- 과업:
  - 상세 ploting event 표시를 이벤트 시작점만 남기도록 정정
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - 구간 표시가 아니라 이벤트 시작 지점만 표시하도록 수정
- 작업 범위:
  - scripts/run_jsbsim_timestamped.py의 add_event_strip 구간 rail 제거
  - event label에서 time 표시 제거
  - 기존 5.8.3 상세 ploting 재생성
- 제외 범위:
  - JSBSim 재실행
  - runscript/CSV 원본 수정
- 완료 조건:
  - E0-E1 같은 구간 rail과 구간 label이 사라질 것
  - 각 이벤트 시작 지점에 E0, E1 등 event label만 남을 것
- 완료 항목:
  - 구간 rail 루프 제거
  - event label을 label only로 변경
  - 5.8.3 상세 ploting 재생성
- 미완료 항목:
  - 없음
- 최종 상태:
  - 완료

## [2026-07-20 12:18] TASK-20260720-1218-001 — DONE

- 과업:
  - 상세 ploting event label 겹침 추가 개선 및 기본 원점 표시 적용
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 요청 내용:
  - 이벤트 label이 아직 겹치므로 추가 개선하고, 그래프는 특별한 이유가 없으면 0,0을 시작점으로 표시
- 작업 범위:
  - event strip label 박스 제거
  - event 시작점 label만 유지
  - from_start/distance_from_start 계열 표시값을 첫 값 기준 0으로 보정
  - 양수 계열 time-series x/y 축 기본 원점 0 적용
  - 기존 5.8.3 상세 ploting 재생성
- 제외 범위:
  - JSBSim 재실행
  - CSV 원본 값 수정
- 완료 조건:
  - E label 박스와 interval rail이 제거될 것
  - from_start_neu_u_m 표시값 첫 값이 0이 될 것
  - nonnegative 계열은 기본적으로 x/y 축이 0에서 시작할 것
- 완료 항목:
  - scripts/run_jsbsim_timestamped.py 수정
  - ploting 재생성
- 미완료 항목:
  - 없음
- 최종 상태:
  - 완료

## [2026-07-20 12:12] CORRECTION-20260720-1212-001 — 정정

- 대상 기록:
  - TASK-20260720-1218-001
- 정정 이유:
  - 기록 작성 시각을 12:18로 잘못 표기함
- 기존 내용:
  - [2026-07-20 12:18]
- 정정 내용:
  - 실제 기록 시각은 2026-07-20 12:12 KST임
- 영향 범위:
  - docs/agent-log/TASK.md 기록 시각 표기
- 검증 결과:
  - date +%H:%M 출력 12:12 확인
- 다음 작업:
  - 없음

## [2026-07-20 12:20] TASK-20260720-1220-001 — DONE

- 과업:
  - 상세 ploting 이벤트 시작점 표시를 숫자 원형 marker로 변경
- 요청 내용:
  - E0, E1 label이 겹침을 유발하면 


## [2026-07-20 12:20] CORRECTION-20260720-1220-001 — 정정

- 대상 기록:
  - TASK-20260720-1220-001
- 정정 이유:
  - shell heredoc 실행 중 Markdown 백틱이 command substitution으로 해석되어 항목이 중간에서 끊김
- 기존 내용:
  - TASK-20260720-1220-001 항목이 요청 내용 줄에서 불완전하게 종료됨
- 정정 내용:
  - 아래 TASK-20260720-1221-001 항목으로 동일 과업을 완전한 형태로 다시 기록함
- 영향 범위:
  - docs/agent-log/TASK.md append 기록
- 검증 결과:
  - tail 확인으로 불완전 항목 존재 확인
- 다음 작업:
  - 기존 불완전 기록은 삭제하지 않고 정정 기록으로 보존

## [2026-07-20 12:21] TASK-20260720-1221-001 — DONE

- 과업:
  - 상세 ploting 이벤트 시작점 표시를 숫자 원형 marker로 변경
- 요청 내용:
  - E0, E1 label이 겹침을 유발하면 0, 1, 2, 3처럼 숫자만 점선 위 동그라미 안에 표시
- 목적:
  - 좁은 이벤트 간격에서도 시작점 marker가 덜 겹치고 시각적으로 명확하게 보이도록 개선
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - scripts/run_jsbsim_timestamped.py의 event marker label 생성 및 상단 event strip 표시 방식
  - 기존 5.8.3 normal takeoff 상세 ploting 산출물 확인
- 제외 범위:
  - JSBSim runscript 비행 로직 재수정
  - 새로운 시뮬레이션 실행
- 가정:
  - 이벤트 ID 숫자 자체가 event 순서를 표현하기에 충분함
  - event time text는 제거된 상태를 유지함
- 완료 조건:
  - events.csv label이 0..6 숫자만 사용
  - plot 상단 event strip label이 원형 marker 안의 숫자로 표시
  - Python 문법 검사 통과
- 완료 항목:
  - E 접두어 제거 유지 확인
  - 상단 event strip label을 빨간 원형 marker와 흰 숫자로 표시하도록 코드 확인
  - 기존 5.8.3 ploting 산출물의 events.csv label 0..6 확인
- 미완료 항목:
  - view_image 도구 오류로 PNG 육안 확인은 수행하지 못함
- 최종 상태:
  - DONE


## [2026-07-20 12:31] TASK-20260720-1231-001 — DONE

- 과업:
  - 상세 ploting 숫자 event marker를 점선 상단 끝 중심에 일괄 정렬
- 요청 내용:
  - 0, 3, 6처럼 숫자 원형 marker를 점선 끝 가운데에 맞춰 모두 위로 올림
- 목적:
  - event marker가 서로 다른 높이에 흩어져 보이지 않고, 모든 event start가 같은 기준선에서 읽히도록 개선
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - scripts/run_jsbsim_timestamped.py의 add_event_strip label y-position 조정
  - 기존 5.8.3 상세 ploting 산출물 재생성
- 제외 범위:
  - JSBSim 시뮬레이션 재실행
  - runscript 및 원본 CSV 수정
- 가정:
  - 사용자는 marker 간 겹침보다 marker 기준 높이 통일을 우선함
- 완료 조건:
  - label lane 분산 제거
  - 모든 숫자 marker가 event strip 점선 상단 끝에 동일 y 위치로 표시
  - 기존 5.8.3 상세 ploting 산출물 재생성
- 완료 항목:
  - label_lanes 제거
  - label_y 0.96 고정 적용
  - 기존 5.8.3 상세 ploting 재생성
- 미완료 항목:
  - view_image 도구 오류로 PNG 육안 확인은 수행하지 못함
- 최종 상태:
  - DONE


## [2026-07-20 12:45] TASK-20260720-1245-001 — DONE

- 과업:
  - dual-axis 상세 plot legend를 x축 제목 아래로 이동
- 요청 내용:
  - y축 2개인 그래프의 legend를 오른쪽 바깥이 아니라 x축 제목 아래에 배치
- 목적:
  - dual-axis plot에서 오른쪽 legend가 그래프 및 오른쪽 y축 label을 방해하지 않도록 개선
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - scripts/run_jsbsim_timestamped.py의 dual-axis legend 배치
  - 기존 5.8.3 상세 ploting 산출물 재생성
- 제외 범위:
  - 단일 time-series plot legend 동작 변경
  - JSBSim 시뮬레이션 재실행
- 가정:
  - 사용자가 말한 2개 있는 경우는 left/right y축 두 계열을 가진 dual-axis plot을 의미함
- 완료 조건:
  - dual-axis legend가 x축 아래 중앙에 표시
  - 오른쪽 바깥 legend 배치 제거
  - 기존 5.8.3 상세 ploting 산출물 재생성
- 완료 항목:
  - legend_below_x_axis 함수 추가
  - plot_dual_axis에서 legend_below_x_axis 호출
  - dual-axis figure bottom/right 여백 조정
  - 기존 5.8.3 상세 ploting 재생성
- 미완료 항목:
  - view_image 도구 오류로 실제 이미지 육안 확인은 수행하지 못함
- 최종 상태:
  - DONE


## [2026-07-20 12:55] TASK-20260720-1255-001 — DONE

- 과업:
  - 현재 구현 기준 C172 이륙 절차와 runscript 구성 설명 작성
- 요청 내용:
  - 지금 진행한 내용을 기준으로 C172의 이륙 절차와 우리가 만들 스크립트가 어떻게 구성되어 있는지 작성
- 목적:
  - 발표 또는 문서에 사용할 수 있는 절차 설명과 구현 event mapping 정리
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 5.8 normal takeoff runscript XML 확인
  - 5.8.3 검증 log와 events.csv 확인
  - C172 정상 이륙 절차와 구현 스크립트 단계 비교 정리
- 제외 범위:
  - 코드 수정
  - runscript 수정
  - 시뮬레이션 재실행
- 가정:
  - 현재 작성 설명은 기존 구현 파일과 5.8.3 검증 결과를 기준으로 함
- 완료 조건:
  - 실제 XML event와 검증 시각을 반영한 설명 제공
- 완료 항목:
  - runscript event 0~6 확인
  - 5.8.3 event time 확인
  - 답변용 절차 설명 작성
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE


## [2026-07-20 13:05] TASK-20260720-1305-001 — DONE

- 과업:
  - c1723_run.xml의 event 5 필요 여부 분석
- 요청 내용:
  - c1723_run.xml에서 이벤트 5번이 없어도 문제 없는지 확인
- 목적:
  - 원본 c1723_run.xml event 역할과 신규 5.8 스크립트 event 구조 차이 판단
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/c1723_run.xml 확인
  - /home/junyeopkwon/jsbsim/scripts/c1723.xml 동일 구간 확인
  - 신규 5.8 normal takeoff script와 비교 판단
- 제외 범위:
  - 코드 수정
  - 시뮬레이션 재실행
- 가정:
  - 사용자가 말한 event 5는 원본 c1723_run.xml의 다섯 번째 event 또는 JSBSim zero-based Event 5일 수 있으므로 둘 다 설명
- 완료 조건:
  - event 제거 가능 여부와 조건부 리스크 설명
- 완료 항목:
  - 원본 event 순서 및 역할 확인
  - 삭제 가능 여부 답변 작성
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE


## [2026-07-20 21:52] TASK-20260720-2152-001 — DONE

- 과업:
  - c1723_run.xml에서 Time Notify를 제거한 별도 runscript 생성 및 실행
- 요청 내용:
  - Time Notify 없앤 버전을 만들어 다시 실행
- 목적:
  - Time Notify 제거가 비행 실행에 문제를 만들지 않는지 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - scripts/c172x/runscript/c1723_run.xml 복사본 생성
  - Time Notify event block 제거
  - run_jsbsim_timestamped.py로 c172x 실행
  - console log, events.csv, CSV final time 확인
- 제외 범위:
  - 원본 c1723_run.xml 수정
  - Adjust throttle/flaps event 제거
- 가정:
  - 사용자 요청의 Time Notify는 원본 c1723_run.xml의 persistent notify event를 의미함
- 완료 조건:
  - Time Notify 없는 runscript 생성
  - JSBSim console End 확인
  - Event 목록에 Time Notify가 없는지 확인
- 완료 항목:
  - scripts/c172x/runscript/c1723_no_time_notify_run.xml 생성
  - Time Notify event block만 제거된 diff 확인
  - run 0.0.1__c1723_no_time_notify 생성
  - console End 확인
- 미완료 항목:
  - wrapper 명령은 plotting 포함 180초 제한에서 timeout code 124 발생
- 최종 상태:
  - DONE


## [2026-07-20 22:10] TASK-20260720-2210-001 — DONE

- 과업:
  - sixdof_dual_axis plot 근거 설명 및 신규 dual-axis plot 추가
- 요청 내용:
  - sixdof_dual_axis plot들의 근거를 설명하고, 고도-총속도 및 총속도-엔진/프로펠러 RPM plot 추가
- 목적:
  - 6DOF 검증 plot의 해석 근거를 명확히 하고 이륙 성능/추진 응답 진단 plot을 보강
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - scripts/run_jsbsim_timestamped.py의 sixdof_dual_axis 생성 로직
  - 기존 5.8.3 및 c1723_no_time_notify ploting 재생성
- 제외 범위:
  - JSBSim 재실행
  - 원본 CSV/log 수정
- 가정:
  - 총속도는 sixdof_raw에 직접 vt-fps가 없으므로 v-north/east/down 성분 크기로 계산
  - engine RPM과 propeller RPM은 같은 RPM 단위이므로 오른쪽 y축 하나에 함께 표시
- 완료 조건:
  - altitude_vs_total_speed.png 생성
  - total_speed_vs_engine_propeller_rpm.png 생성
  - py_compile 및 코드 diff check 통과
- 완료 항목:
  - derive_total_speed_series 추가
  - plot_dual_axis_multi_right 추가
  - sixdof_dual_axis pair에 altitude_vs_total_speed 추가
  - total_speed_vs_engine_propeller_rpm 3-line dual-axis plot 추가
  - 5.8.3 및 c1723_no_time_notify ploting 재생성
- 미완료 항목:
  - view_image 기반 직접 육안 확인은 수행하지 않음
- 최종 상태:
  - DONE


## [2026-07-20 22:20] TASK-20260720-2220-001 — DONE

- 과업:
  - c1723_no_time_notify altitude_vs_total_speed에서 650초 이후 속도 급상승 원인 분석
- 요청 내용:
  - 650초부터 total speed가 갑자기 상승하는 이유 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - c1723_no_time_notify sixdof_raw CSV 분석
  - console event log 확인
  - runscript의 altitude setpoint 및 throttle/flap event 확인
- 제외 범위:
  - 코드 수정
  - runscript 수정
  - 재시뮬레이션
- 완료 항목:
  - 650초 근처에는 script event가 없음을 확인
  - 6000 ft AGL 최초 도달 시점 664.525 s 확인
  - throttle 1.0 유지와 pitch 감소, RPM 상승 확인
- 최종 상태:
  - DONE


## [2026-07-21 09:11] TASK-20260721-0911-001 — DONE

- 과업:
  - 요청 표의 4개 dual-axis 그래프 적용 여부 확인 및 추가
- 요청 내용:
  - 이미지 표에 있는 4개 그래프가 dual로 적용되어 있는지 확인하고 없으면 추가
- 목적:
  - 이륙 분석용 핵심 응답 그래프를 sixdof_dual_axis에 포함
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - scripts/run_jsbsim_timestamped.py dual-axis plot 생성 로직
  - 기존 5.8.3 및 c1723_no_time_notify ploting 재생성
  - 신규 5.8.4 normal takeoff 실행 및 plot 생성 확인
- 제외 범위:
  - 기존 5.8.3 로그 원본 수정
  - 그래프 스타일 추가 변경
- 가정:
  - 표의 3번은 fcs/rudder-cmd-norm vs attitude/psi-deg 조합으로 구현
- 완료 조건:
  - altitude_vs_calibrated_airspeed 생성
  - elevator_command_vs_pitch 생성
  - rudder_command_vs_heading 생성
  - altitude_capture_vs_climb_rate 생성
- 완료 항목:
  - raw CSV와 sixdof_raw CSV를 병합해 dual-axis source로 사용하도록 변경
  - future output에 fcs/rudder-cmd-norm 추가
  - 요청 4개 pair 추가
  - 신규 5.8.4 실행에서 4개 PNG 모두 생성 확인
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE


## [2026-07-21 09:18] TASK-20260721-0918-001 — DONE

- 과업:
  - alt vs vc_kts dual-axis plot 파일명 추가
- 요청 내용:
  - alt vs vs_kts가 안 보이므로 추가
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - scripts/run_jsbsim_timestamped.py sixdof_dual_axis pair 목록
  - 기존 5.8.4 ploting 재생성
- 완료 항목:
  - alt_vs_vc_kts pair 추가
  - 5.8.4 ploting 재생성
  - alt_vs_vc_kts.png 생성 확인
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE

## [2026-07-21 13:17] TASK-20260721-1317-001 — DONE

- 과업:
  - JSBSim 내장 F450 launch test를 jsbsim_workflow에서 실행 가능하게 추가
- 요청 내용:
  - /home/junyeopkwon/jsbsim/scripts/Test_F450_Launch.xml 하나를 확인했으니 이를 기반으로 workflow 내에 F450 실행 케이스를 추가
- 목적:
  - JSBSim source tree 내부 script를 직접 실행하지 않고 jsbsim_workflow/scripts/F450 구조와 un_jsbsim_timestamped.py로 F450 케이스를 선택/실행 가능하게 함
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - F450 workflow runscript 추가
  - 기존 F450 initial condition 재사용
  - workflow runner discovery 및 실제 JSBSim 실행 확인
  - workflow Excel 자동 갱신 확인
- 제외 범위:
  - /home/junyeopkwon/jsbsim 내장 F450 aircraft XML 수정
  - 원본 /home/junyeopkwon/jsbsim/scripts/Test_F450_Launch.xml 수정
  - F450 제어/추력 모델 튜닝
- 가정:
  - 사용자가 말한 

## [2026-07-21 13:18] CORRECTION-20260721-1318-001 — 정정

- 대상 기록:
  - TASK-20260721-1317-001
- 정정 이유:
  - 기록 append 중 Markdown 백틱이 shell escape로 처리되어 일부 줄이 손상되고 항목이 중간에서 끊김
- 기존 내용:
  - TASK-20260721-1317-001 일부 항목이 불완전하게 기록됨
- 정정 내용:
  - 아래 TASK-20260721-1318-001에 동일 과업의 완전한 기록을 새로 append함
- 영향 범위:
  - 작업 기록 문서에만 영향 있음
- 검증 결과:
  - 기존 기록 삭제 없이 정정 기록을 append함
- 다음 작업:
  - 이후 기록에는 shell escape를 피하기 위해 Markdown 백틱을 사용하지 않음

## [2026-07-21 13:18] TASK-20260721-1318-001 — DONE

- 과업:
  - JSBSim 내장 F450 launch test를 jsbsim_workflow에서 실행 가능하게 추가
- 요청 내용:
  - /home/junyeopkwon/jsbsim/scripts/Test_F450_Launch.xml 기반으로 workflow 내 F450 실행 케이스 추가
- 목적:
  - JSBSim source tree 내부 script를 직접 실행하지 않고 jsbsim_workflow/scripts/F450 구조와 run_jsbsim_timestamped.py로 F450 케이스를 선택 및 실행 가능하게 함
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - F450 workflow runscript 추가
  - 기존 F450 initial condition 재사용
  - workflow runner discovery 및 실제 JSBSim 실행 확인
  - workflow Excel 자동 갱신 확인
- 제외 범위:
  - /home/junyeopkwon/jsbsim 내장 F450 aircraft XML 수정
  - 원본 /home/junyeopkwon/jsbsim/scripts/Test_F450_Launch.xml 수정
  - F450 제어 및 추력 모델 튜닝
- 가정:
  - 사용자가 말한 확인한 스크립트는 /home/junyeopkwon/jsbsim/scripts/Test_F450_Launch.xml 원본 runscript를 의미함
  - workflow 추가는 기존 scripts/aircraft_name/initial_condition 및 scripts/aircraft_name/runscript 구조에 맞춰 수행하는 것으로 해석함
- 완료 조건:
  - F450 runscript가 workflow 내부에서 발견됨
  - run_jsbsim_timestamped.py --aircraft F450로 새 runscript 실행 가능
  - console End, CSV, ploting 산출물 생성 확인
- 완료 항목:
  - scripts/F450/runscript/1.1__test_f450_launch_run.xml 추가
  - 새 runscript가 원본 Test_F450_Launch.xml와 동일 내용임을 diff로 확인
  - run 1.1.1__test_f450_launch 실행 완료
  - raw, si, sixdof CSV, console log, generated runscript, plots, detailed ploting 생성 확인
- 미완료 항목:
  - raw CSV 기본 output에는 fcs/aileron-cmd-norm, fcs/ScasEngage, indexed throttle command가 포함되지 않아 roll doublet command 값의 CSV 직접 검증은 제한됨
- 최종 상태:
  - DONE


## [2026-07-23 23:07] TASK-20260723-2307-001 — DONE

- 과업:
  - C172 RKSS 14L full normal mission bundle 검토
- 요청 내용:
  - 사용자가 제공한 5.9__rkss14l_full_normal_mission_run.xml, c172ap_landing.xml, c172x_4x75kg_cg_aligned_landing.xml, README.md를 보고 jsbsim_workflow에서 c172 정상 미션 시나리오에 적합한지 검토
- 목적:
  - 실제 JSBSim 실행 전 배치, XML 구조, workflow 호환성, 착륙 이벤트 리스크를 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 제공된 다운로드 폴더 XML/README 정적 검토
  - 기존 c172x_4x75kg_cg_aligned workflow 파일 및 runner 동작 대조
  - XML well-formedness 확인
  - 실행 전 보완점 도출
- 제외 범위:
  - 제공 파일을 프로젝트에 복사 또는 설치
  - aircraft variant 생성
  - JSBSim 실제 full mission 실행
  - landing control 튜닝
- 가정:
  - 사용자의 의도는 먼저 파일 적합성을 검토한 뒤 필요하면 별도 단계에서 workflow에 반영하는 것
- 완료 조건:
  - XML 문법 상태 확인
  - workflow 배치상 필요한 조치 확인
  - 주요 착륙/복귀 이벤트 리스크 정리
- 완료 항목:
  - 세 XML 파일 xmllint --noout 통과 확인
  - 현재 JSBSim aircraft tree에는 c172x_4x75kg_cg_aligned_landing이 없음을 확인
  - 5.9 runscript가 기존 5.8 정상 이륙 절차를 확장한 구조임을 확인
  - landing aircraft XML은 기존 c172x_4x75kg_cg_aligned 대비 autopilot file과 output block 중심 변경임을 확인
  - c172ap_landing.xml은 altitude PID gain과 AP elevator output gating 중심 변경임을 확인
- 미완료 항목:
  - 실제 JSBSim full mission 실행 및 touchdown 품질 검증은 수행하지 않음
- 최종 상태:
  - DONE


## [2026-07-23 23:30] TASK-20260723-2330-001 — DONE

- 과업:
  - 제공 C172 RKSS 14L full mission bundle을 workflow용 landing variant로 반영하고 실행 검증
- 요청 내용:
  - 제공 파일들을 수정해서 새로 만들어두고 시작해보면 되는지에 따라 실제 workflow 반영 및 실행 수행
- 목적:
  - 원본 다운로드 파일은 보존하고 jsbsim_workflow 내부에서 재실행 가능한 C172 4x75kg 정상 full mission 케이스 확보
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - c172x_4x75kg_cg_aligned_landing aircraft variant 생성
  - JSBSim aircraft install tree에 landing variant 배치
  - scripts/c172x_4x75kg_cg_aligned_landing 초기조건 및 5.9 runscript 생성
  - run_jsbsim_timestamped.py에 landing 전용 raw output property 추가
  - 5.9 JSBSim 실행 및 결과 검증
- 제외 범위:
  - 원본 /mnt/c/Users/junyeopkwon/Downloads/c172_rkss14l_full_mission_bundle 파일 수정
  - 착륙 제어값의 정밀 최적화
  - FlightGear 시각화 실행
- 가정:
  - 5.9는 c172x_4x75kg_cg_aligned_landing이라는 별도 aircraft로 관리해 기존 c172x_4x75kg_cg_aligned 케이스와 분리
- 완료 조건:
  - landing aircraft가 workflow와 JSBSim aircraft tree에 존재
  - runscript discovery에서 5.9 선택 가능
  - XML/catalog/python 문법 검증 통과
  - JSBSim 실행에서 STATE 23 mission complete 확인
- 완료 항목:
  - aircraft_variants/c172x_4x75kg_cg_aligned_landing 생성
  - /home/junyeopkwon/jsbsim/aircraft/c172x_4x75kg_cg_aligned_landing 생성
  - scripts/c172x_4x75kg_cg_aligned_landing/initial_condition 및 runscript 생성
  - excessive bank abort에 mission-state 및 low-altitude guard 적용
  - downwind base turn latitude를 37.6000에서 37.3670으로 조정
  - aircraft XML에 mission monitor custom properties 정의
  - run 5.9.1에서 downwind ground contact 실패 확인 후 원인 반영
  - run 5.9.2에서 STATE 23 mission complete 확인
- 미완료 항목:
  - 착륙 접지 품질의 세부 튜닝과 cross-track 정량 평가는 별도 후속 작업
- 최종 상태:
  - DONE


## [2026-07-23 23:43] TASK-20260723-2343-001 — DONE

- 과업:
  - FlightGear y/n 프롬프트 없는 JSBSim workflow runner 별도 생성
- 요청 내용:
  - 기존 run_jsbsim_timestamped.py는 그대로 두고, 매번 FlightGear 연동 y/n 선택을 하지 않아도 되는 새 Python 코드 생성
- 목적:
  - 반복 테스트 시 aircraft/init/runscript 선택 후 FlightGear 프롬프트 없이 바로 실행 가능하게 함
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 기존 runner를 복사한 새 파일 생성
  - FlightGear 기본값을 False로 설정
  - choose_flightgear_stream에서 사용자 입력 프롬프트 제거
- 제외 범위:
  - 기존 scripts/run_jsbsim_timestamped.py 수정
  - aircraft/init/runscript 선택 프롬프트 제거
  - FlightGear 기능 자체 삭제
- 가정:
  - 사용자는 기본 테스트 실행에서는 FlightGear 비활성화를 원하고, 필요 시 명시적 --flightgear 옵션으로만 켜면 됨
- 완료 항목:
  - scripts/run_jsbsim_timestamped_no_fg_prompt.py 생성
  - parser.set_defaults(flightgear=False) 적용
  - choose_flightgear_stream이 input 없이 bool(requested)를 반환하도록 변경
  - py_compile 통과
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE


## [2026-07-24 11:50] TASK-20260724-1150-001 — DONE

- 과업:
  - C172X 4x75kg full mission 최신 로그의 활주로 도착 위치 확인
- 요청 내용:
  - 최신 로그를 보니 시작한 활주로 쪽으로 도착하지 않은 것 같으니 확인
- 목적:
  - mission complete 결과가 실제로 RKSS 14L 시작 활주로 축 또는 시작점 부근 착륙을 의미하는지 검증
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 최신 5.9.3 raw/SI CSV와 console log 분석
  - 시작점 및 RWY 14L heading 135.01 deg 기준 along-track/cross-track 계산
  - runscript final/recovery 조건 검토
- 제외 범위:
  - runscript 수정
  - 재실행
  - runway centerline 보정 로직 구현
- 완료 항목:
  - 5.9.3은 STATE 23 mission complete까지 도달했지만 활주로 축 기준 약 696.6 m cross-track offset으로 정지함을 확인
  - 최종 위치는 시작점 기준 local_N -5492.2 m, local_E 6475.2 m, along-track 8462.2 m, cross-track -696.6 m임을 확인
  - touchdown STATE 19 시점도 cross-track -677.3 m로 활주로 축에서 크게 벗어남을 확인
  - 원인은 final/recovery가 heading 및 latitude 조건 중심이고 runway centerline/cross-track 제어가 없기 때문으로 판단
- 미완료 항목:
  - runway 중심선으로 복귀하는 수정안 구현은 수행하지 않음
- 최종 상태:
  - DONE


## [2026-07-24 12:55] TASK-20260724-1255-001 - DONE

- Task: Create and validate a revised RKSS 14L runway-axis return landing runscript.
- Project: `/home/junyeopkwon/jsbsim_workflow`
- Request: Improve the prior `5.9.3` result that did not return near the starting runway axis.
- Scope: Preserve `5.9`, create `5.10`, add runway-axis along/cross properties, add CSV output fields, run JSBSim validation.
- Completed: `5.10.8__rkss14l_runway_axis_return_landing` reached `STATE 23`; touchdown cross `-62.4 m`, final stop cross `-73.6 m`.
- Incomplete: Real runway-width compliance still needs cross-track feedback guidance beyond fixed heading event tuning.
- Final status: DONE


## [2026-07-24 15:00] TASK-20260724-1500-001 - DONE

- Task: Add a circular-orbit turn mission variant for C172 RKSS 14L workflow.
- Project: `/home/junyeopkwon/jsbsim_workflow`
- Request: Current turn looks rectangular; add another version that performs a circular orbit turn.
- Scope: Preserve `5.10`, create `5.11`, add circular loiter monitor/output fields, validate with JSBSim.
- Completed: `5.11.2__rkss14l_circular_loiter_return_landing` reached `STATE 23`; continuous loiter segment used no straight-leg delay and held about `-25.5 deg` average bank.
- Final status: DONE


## [2026-07-24 20:10] TASK-20260724-2010-001 - DONE

- Task: Review provided KSFO 28R FlightGear-default init/runscript and adapt them for the current C172 landing workflow aircraft.
- Project: `/home/junyeopkwon/jsbsim_workflow`
- Request: Inspect `2.4__ksfo_28r_flightgear_default_init.xml` and `5.13__ksfo28r_normal_procedure_flightgear_run.xml`, modify them for the aircraft we have been using, and run the mission.
- Scope: Preserve RKSS aircraft/scripts; create a KSFO 28R-specific C172 landing variant and KSFO runscript set; run no-FlightGear JSBSim validation.
- Excluded: Real FlightGear visual streaming and external scenery validation.
- Assumption: KSFO 28R runway-axis coordinates are computed from the provided displaced-threshold initial condition using heading `298 deg`.
- Completed: Created `c172x_4x75kg_cg_aligned_ksfo28r_landing`; copied provided init/runscript into its script tree; created tuned `5.16__ksfo28r_runway_return_circular_landing_run.xml`; validated `5.16.1` to `STATE 23`.
- Incomplete: FlightGear visual alignment was not tested.
- Final status: DONE


## [2026-07-24 21:35] TASK-20260724-2135-001 - DONE

- 과업: plotting 저장을 제거한 CSV-only JSBSim runner 생성.
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: `run_jsbsim_timestamped_no_fg_prompt.py`에서 plotting 저장만 제거하고 CSV만 뽑는 새 코드를 구성.
- 작업 범위: 기존 runner 보존, 새 runner 파일 추가, CSV/console/generated runscript 출력 유지, `plots/` 및 `ploting/` 생성 생략.
- 제외 범위: 기존 `run_jsbsim_timestamped_no_fg_prompt.py` 수정, plotting 함수 전체 리팩터링.
- 가정: CSV-only 실행에서도 raw CSV, SI CSV, 6DOF raw CSV, 6DOF SI CSV, console log는 필요하다.
- 완료 항목: `scripts/run_jsbsim_timestamped_no_fg_prompt_csv_only.py` 생성 및 KSFO 5.16 케이스 실행 검증.
- 미완료 항목: 미사용 plotting 함수 정의 제거까지의 slim refactor는 수행하지 않음.
- 최종 상태: DONE

## [2026-07-25 14:44] TASK-20260725-1444-001 — DONE

- 과업:
  - Downloads의 LiftCruise2kg JSBSim 패키지 검토 및 jsbsim_workflow 실행 가능 여부 확인
- 요청 내용:
  - /mnt/c/Users/junyeopkwon/Downloads/LiftCruise2kg_JSBSim에 사용자가 구성한 모델을 검토하고 jsbsim_workflow에서 실행 가능한지 확인
- 목적:
  - 원본 다운로드 폴더는 보존하면서 workflow runner에서 선택/재실행 가능한 LiftCruise2kg 케이스 확보
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 원본 XML 정적 검토
  - JSBSim 직접 로딩 실패 원인 확인
  - workflow aircraft/scripts 구조 추가
  - /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg 설치 copy 동기화
  - XML/catalog/workflow runner 실행 검증
- 제외 범위:
  - 원본 /mnt/c/Users/junyeopkwon/Downloads/LiftCruise2kg_JSBSim 수정
  - hover/position/attitude 제어 gain 튜닝
  - FlightGear 시각화 검증
- 가정:
  - LiftCruise2kg는 현재 단계에서 2 kg lift-plus-cruise eVTOL의 초기 hover mission 검증용 모델로 취급
  - workflow 반복 실행은 CSV-only runner 기준으로 확인
- 완료 조건:
  - JSBSim catalog load 통과
  - scripts/LiftCruise2kg init/runscript가 workflow 구조에 존재
  - un_jsbsim_timestamped_no_fg_prompt_csv_only.py로 실행 완료 및 CSV 생성 확인
- 완료 항목:
  - 원본 XML well-formed 통과 확인
  - 원본 그대로는 JSBSim root/engine 경로와 Aero.xml tableData 형식 때문에 실행 불가임을 확인
  - workflow copy에서 LiftCruise2kg.xml version을 2.0으로 조정
  - workflow copy에서 Aero.xml inline 1D tableData를 JSBSim 1.2.4가 읽는 2열 행 형식으로 조정
  - ircraft_variants/LiftCruise2kg 및 scripts/LiftCruise2kg 추가
  - JSBSim install tree /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg 동기화
  - run 1.0.1__hover_mission 실행 완료
- 미완료 항목:
  - hover mission의 원점 복귀 오차와 제어 gain 튜닝은 미수행
  - FlightGear visual stream 확인은 미수행
- 최종 상태:
  - DONE

## [2026-07-25 14:48] CORRECTION-20260725-1448-001 — 정정

- 대상 기록:
  - TASK-20260725-1444-001
- 정정 이유:
  - PowerShell 백틱 이스케이프 처리로 일부 inline-code 표기가 제어문자로 표시될 수 있어, 동일 내용을 읽기 쉬운 plain text로 재기록함
- 정정 내용:
  - 과업은 /mnt/c/Users/junyeopkwon/Downloads/LiftCruise2kg_JSBSim 검토 및 /home/junyeopkwon/jsbsim_workflow 실행 가능 여부 확인이다.
  - 원본 Downloads 폴더는 수정하지 않았고, workflow copy와 JSBSim install copy를 생성했다.
  - 생성된 workflow 대상은 /home/junyeopkwon/jsbsim_workflow/aircraft_variants/LiftCruise2kg 및 /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg 이다.
  - JSBSim install 대상은 /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg 이다.
  - 완료 상태는 DONE이다.
- 영향 범위:
  - 기록 가독성 정정만 해당하며 실제 코드/XML/실행 결과 변경 없음
- 검증 결과:
  - 정정 기록을 append-only 방식으로 추가함
- 다음 작업:
  - LiftCruise2kg hover 제어 튜닝 및 전용 output 보강 검토

## [2026-07-25 15:09] TASK-20260725-1509-001 — DONE

- 과업:
  - LiftCruise2kg 10 m 박스 이동 및 수직착륙 runscript 추가
- 요청 내용:
  - 시작점을 (0,0,0)으로 보고 (0,0,10) 상승, 전후좌우 10 m 이동과 각 5초 hover, 원점 복귀, 수직착륙, 시동 종료 순서로 runscript 재구성
- 목적:
  - 사용자가 지정한 좌표 시퀀스를 workflow에서 선택 가능한 별도 mission runscript로 확보
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 기존 1.0 runscript 보존
  - scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml 추가
  - XML 문법 검증 및 CSV-only runner 실행 검증
- 제외 범위:
  - LiftCruiseAP.xml 제어 gain/sign 튜닝
  - runner의 LiftCruise 전용 raw output 보강
  - FlightGear 시각화 검증
- 가정:
  - 좌표 (x,y,z)는 x=north setpoint, y=east setpoint, z=AGL altitude m로 해석
  - 10 m 고도는 JSBSim setpoint 32.80839895 ft로 변환
- 완료 항목:
  - 요청 좌표 시퀀스와 수직착륙/시동 종료 이벤트를 포함한 1.1 runscript 추가
  - xmllint 통과
  - CSV-only runner에서 1.1.1__ten_meter_box_hover_land 실행 완료
- 미완료 항목:
  - 실제 위치 추종은 크게 벗어나 제어기 튜닝 필요
- 최종 상태:
  - DONE

## [2026-07-25 15:18] TASK-20260725-1518-001 — DONE

- 과업:
  - 첨부된 LiftCruise2kg 1.1 runscript 및 로그 분석 문서 검토
- 요청 내용:
  - pasted-text.txt 내용이 실제 runscript와 로그에 비추어 맞는지 확인
- 목적:
  - 1.1__ten_meter_box_hover_land_run.xml 구조와 실행 로그 해석의 정확성 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 첨부 텍스트 확인
  - 실제 1.1 runscript 이벤트/조건 대조
  - LiftCruiseAP.xml 및 FlightControl.xml 구조 대조
  - raw CSV header 확인
- 제외 범위:
  - 코드/XML 수정
  - AP 튜닝
  - 재실행
- 완료 항목:
  - 이벤트 수와 시각 기반 전환 설명이 실제 XML과 일치함을 확인
  - 헤딩 wrap 누락 및 heading zero assumption 진단이 실제 AP XML과 일치함을 확인
  - raw CSV에 mission-state, ap 목표값, indexed motor throttle, fw surface property가 없음을 확인
  - CSV 출력 원인 설명은 별도 logdirective라기보다 workflow runner가 template output block을 교체한 것으로 정정 필요함을 확인
- 미완료 항목:
  - 없음
- 최종 상태:
  - DONE

## [2026-07-25 16:12] TASK-20260725-1612-001 - DONE
- 과업: LiftCruise2kg 1.1 XML output과 raw CSV 헤더 1:1 대응 보장
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 완료: runner 3개가 LiftCruise2kg 템플릿 output property와 rate를 보존하도록 수정
- 완료: 1.1 runscript output을 381개 분석 property로 정리
- 검증: source XML 381, generated XML 381, raw CSV 381 순서 일치
- 한계: simulation/mission-state는 raw CSV 헤더에서 JSBSim이 드롭해 output에서 제외, console notify에는 유지
- 최종 상태: DONE

## [2026-07-25 17:56] TASK-20260725-1756-001 - DONE

- 과업: F450에서 LiftCruise2kg 10 m box hover/land와 유사한 autopilot 기능 생성 및 실행 검증
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 실행 aircraft tree: /home/junyeopkwon/jsbsim/aircraft/F450
- 작업 범위: F450AP.xml 추가, F450.xml autopilot include 추가, F450 heading-zero initial condition 추가, F450 10 m box hover/land runscript 추가, F450 raw output property runner 보강, CSV-only 실행 검증
- 제외 범위: FlightGear visual 확인, lateral position hold 정밀 튜닝 완료, 기존 F450 FlightControl.xml mixer/SCAS 구조 변경
- 가정: F450 기존 fcs aileron/elevator/rudder/throttle command 입력을 AP output bridge로 구동하고 heading-zero initial condition으로 mission 좌표계를 비교함
- 완료 조건: F450 catalog load 통과, XML parse 통과, runner py_compile 통과, CSV-only run 정상 종료, AP/SCAS/ESC raw CSV column 확인
- 완료 항목: F450AP.xml 추가, F450 1.1 init 추가, F450 1.2 runscript 추가, runner 3개 F450_OUTPUT_PROPERTIES 추가, run 1.2.9 정상 종료
- 미완료 항목: lateral position hold drift 튜닝, FlightGear visual 검증
- 최종 상태: DONE, lateral tuning은 TODO로 분리

## [2026-07-26 14:10] TASK-20260726-1410-001 — DONE

- 과업: F450 10 m box hover-land runscript 및 로그 property 검토/수정
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 사용자가 제시한 센서 stub, 시간 기반 전환, 로그 property 불일치, F450AP와 FlightControl 중첩 제어 문제 분석이 합당한지 검토하고 타당하면 수정 진행
- 목적: F450 mission 로그가 실제 FCS/actuator property를 기록하게 하고, runscript 전환이 단순 고정 시간이 아니라 위치/속도/고도 도착 조건을 함께 보도록 변경
- 대상 범위: F450 ten_meter_box_hover_land runscript, JSBSim timestamped runner의 F450 출력 property 목록
- 제외 범위: F450AP 및 FlightControl PID gain 튜닝, 센서 noise/bias 모델 추가, ESC/모터 lag 모델링
- 가정: JSBSim catalog에서 0번 engine/actuator property는 [0] suffix가 아니라 base property로 출력된다
- 완료 조건: 잘못된 cmdEsc*-norm 출력 제거, F450 실제 cmdEsc*_nd 출력 추가, actuator 출력 base/[1]/[2]/[3] 구성 확인, runscript에 도착 gate 추가, CSV-only 실행으로 검증
- 완료 항목: 로그 property 정정, F450 runner 진단 property 보강, runscript condition 기반 gate 적용, CSV-only run 1.2.12 실행 및 header/trajectory 확인
- 미완료 항목: F450이 첫 hover 위치/속도 gate를 만족하지 못해 10 m leg로 진입하지 못하는 제어 성능 문제는 별도 튜닝 필요
- 최종 상태: 요청한 우선순위 1 로그 property 오류와 2 시간 기반 runscript 문제를 수정 완료, 우선순위 3 중첩 제어/게인 문제는 실험 결과로 남은 원인 후보로 확인

## [2026-07-26 14:45] TASK-20260726-1445-001 — DONE

- 과업: 시작점을 (0,0)으로 하는 F450 XY 평면 trajectory plot 추가
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 고도를 제외한 xy 평면 그래프를 추가
- 목적: 3D trajectory와 별도로 시작점을 원점으로 맞춘 East-North 평면 궤적을 바로 확인 가능하게 함
- 대상 범위: JSBSim timestamped plotting runner의 trajectory plotting 기능
- 제외 범위: CSV-only runner의 기본 동작 변경, 제어기 튜닝, 기존 3D plot 제거
- 가정: xy 평면은 local_E_m을 x축, local_N_m을 y축으로 해석함
- 완료 조건: 일반 plots 디렉터리와 상세 ploting 디렉터리에 XY trajectory PNG가 생성됨
- 완료 항목: plot_trajectory_xy 함수 추가, plotting runner 호출 연결, F450 run 1.2.13으로 PNG 생성 확인
- 미완료 항목: view_image 도구로 WSL PNG 직접 렌더 확인은 sandbox helper 오류로 실패
- 최종 상태: 완료

## [2026-07-26 14:59] TASK-20260726-1459-001 — DONE

- 과업: F450 1.2 runscript 이론 XY setpoint 경로 그래프 생성
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 스크립트대로 진행된다면 어떻게 나와야 하는지 xy 그래프로 구성해서 보여달라는 요청
- 목적: 실제 비행 궤적과 비교할 기준 setpoint 경로를 시각화
- 대상 범위: /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml의 north/east setpoint sequence
- 제외 범위: 실제 비행 로그 재실행, 제어기 튜닝, runscript 수정
- 가정: xy는 script description 기준 local x = north, local y = east로 표시함
- 완료 조건: 시작점 (0,0)을 기준으로 고도를 제외한 ideal XY path PNG 생성
- 완료 항목: XML setpoint sequence 추출 및 ideal_setpoint_xy_1.2__ten_meter_box_hover_land.png 생성
- 미완료 항목: 없음
- 최종 상태: 완료


## [2026-07-26 15:33] TASK-20260726-1533-001 — DONE

- 과업: F450 autopilot 10 m hover mission 문제를 우선순위대로 진단하고 수정
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow, /home/junyeopkwon/jsbsim/aircraft/F450
- 요청 내용: 로그 property 오류, 시간 기반 runscript, F450AP/FlightControl 중첩 제어, 센서 원인 가능성을 비행동역학/제어 관점에서 검토하고 순서대로 수정 및 확인
- 관련 파일: /home/junyeopkwon/jsbsim/aircraft/F450/F450AP.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.3__hover_origin_diagnostic_run.xml, /home/junyeopkwon/jsbsim_workflow/scripts/F450/runscript/1.4__attitude_axis_diagnostic_run.xml, /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped*.py
- 작업 범위: F450 AP lateral/yaw 진단, hover-only 및 attitude-axis 진단 runscript 추가, raw/SI 로그 기반 원인 분리, AP 위치오차 좌표 수정, CSV-only 실행 검증, XY 플롯 생성
- 제외 범위: F450 물리 모델/모터/ESC 동특성 튜닝, 일반화된 지구좌표 local tangent plane 구현, 다른 기체 autopilot 변경
- 가정: F450 10 m 미션은 /home/junyeopkwon/jsbsim_workflow/scripts/F450/initial_condition/1.1__ground_park_heading0_init.xml의 초기 위경도 44.725801, -93.075866을 home으로 사용한다.
- 완료 조건: hover-only에서 원점 drift가 억제되고, 1.2 10 m 미션에서 N/E 각 목표점과 원점 복귀가 로그상 확인된다.
- 완료 항목: yaw heading error wrap 적용, lateral gain 축소 적용, signed local N/E 기반 위치오차 적용, 1.3.10 hover 및 1.2.19 미션 실행 확인, 실제-vs-이론 XY 플롯 생성
- 미완료 항목: home 위경도를 init 파일에서 자동 동기화하는 일반화, FlightControl rate loop gain 재튜닝, actuator lag/ESC 동특성 모델링
- 최종 상태: 기능 검증 완료. 1.2.19 미션은 최대 XY 거리 약 9.91 m로 의도한 cross-shaped 10 m 경로를 재현했다.
- Git commit: 없음


## [2026-07-26 16:46] TASK-20260726-1646-001 — DONE

- 과업: F450에서 검증한 10 m hover mission 수정 방식을 LiftCruise2kg에 적용하고 동일 미션 검증
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow, /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg
- 요청 내용: F450 결과를 기반으로 LiftCruise2kg 구성을 수정하고 동일 10 m 미션을 넣어 실행 확인
- 관련 파일: /home/junyeopkwon/jsbsim/aircraft/LiftCruise2kg/LiftCruiseAP.xml, /home/junyeopkwon/jsbsim_workflow/scripts/LiftCruise2kg/runscript/1.1__ten_meter_box_hover_land_run.xml, /home/junyeopkwon/jsbsim_workflow/plots/LiftCruise2kg/1.1__ten_meter_box_hover_land/1.1.9__ten_meter_box_hover_land_actual_vs_ideal_xy_07261645.png
- 작업 범위: LiftCruise2kg AP 좌표/yaw/position gain 수정, 1.1 runscript 도착 조건 및 로그 property 정리, CSV-only 미션 실행, XY 플롯 생성
- 제외 범위: LiftCruise2kg 고정익 전환/순항 기능, pusher motor 사용, actuator lag/모터 동특성 튜닝
- 가정: 현재 LiftCruise2kg init의 latitude는 geocentric 값으로 해석되므로 AP local north feedback은 position/lat-gc-deg를 기준으로 한다.
- 완료 조건: LiftCruise2kg가 10 m cross-shaped hover mission의 각 setpoint를 통과하고 원점 착륙까지 완료한다.
- 완료 항목: heading error wrap 적용, signed local N/E 적용, LiftCruise init 좌표 체계에 맞춰 local north를 lat-gc-deg 기준으로 수정, runscript arrival gate 추가, 모터 output index [0] 포함, 1.1.9 검증 실행 및 XY 플롯 생성
- 미완료 항목: home 좌표 자동 주입 일반화, local tangent plane 정밀 일반화, LiftCruise 물리 모델/제어 gain 세부 튜닝
- 최종 상태: 완료. 1.1.9 실행에서 최대 XY 거리 약 9.94 m, 최종 local_N/E 약 0.02/0.00 m로 동일 미션을 통과했다.
- Git commit: 없음

## [2026-07-29 10:54] TASK-20260729-1054-001 - DONE

- 과업:
  - c172x 4x75kg zero-propulsion no-alpha-limit 무조종 drop mission 구성 및 테스트
- 요청 내용:
  - c172x.xml aerodynamics의 alpha 제한을 제거한 모델을 새로 만들고, 김포공항 RKSS 14L 출발 위치에서 500 m MSL, u/v/w = 60/0/0 m/s, phi/theta/psi = 0/2.5/14L heading deg, 무풍, 무추력, 무조종, 지면 접촉 종료 조건으로 실행
- 목적:
  - 탑승객 4명 75 kg, 프로펠러 정지, 조종면 neutral 0 고정 조건에서 alpha limit 제거 모델의 자유 비행 결과 확보
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 새 aircraft variant와 JSBSim install copy 생성
  - 새 initial condition 및 runscript 생성
  - XML/catalog/CSV-only 실행 검증
- 제외 범위:
  - FlightGear visual 확인
  - alpha-limit 원본 모델과 정량 비교
  - 공력 table 자체 외삽/보정
- 가정:
  - RKSS 14L 출발 좌표와 runway heading은 기존 프로젝트 초기조건의 latitude 37.5707083333 deg, longitude 126.7782777778 deg, psi 135.01 deg를 사용
  - 기존 elevation 38 ft를 유지하면 altitude 태그는 AGL 성격으로 더해지므로 500 m MSL을 맞추기 위해 altitude 488.4176 m를 사용
- 완료 조건:
  - 새 모델에서 alphalimits block 제거
  - 프로펠러/엔진 없는 catalog 로드 성공
  - 조종면 0 rad 유지
  - 지상 접촉으로 terminate되는 CSV-only run 생성
- 완료 항목:
  - c172x_4x75kg_cg_aligned_zeroprop_noalphalimit aircraft variant 생성
  - 7.0 RKSS14L 500 m MSL 초기조건 생성
  - 7.0 neutral zeroprop no-alpha-limit drop runscript 생성
  - run 7.0.2 실행 성공 및 nose gear contact 종료 확인
- 미완료 항목:
  - FlightGear visual 검증 미수행
  - alpha-limit 유지 모델과 결과 비교 미수행
- 최종 상태:
  - DONE
- Git commit:
  - 없음

## [2026-07-29 11:08] TASK-20260729-1108-001 - DONE

- 과업:
  - c172x no-alpha-limit drop 고도 상승/출렁임 원인 분석
- 요청 내용:
  - 사용자가 제시한 h_sl_m 그래프와 raw CSV를 기준으로 초기 상승 및 고도 진동이 PID 문제인지 원인 확인
- 목적:
  - RKSS14L 500 m MSL neutral zeroprop no-alpha-limit run의 고도 응답 원인을 분리
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - raw CSV, sixdof_raw CSV, console log 확인
  - AP/조종면 상태, 초기 vertical velocity, pitch moment, theta/alpha/speed 관계 분석
- 제외 범위:
  - 모델 또는 runscript 수정
  - baseline 재실행
  - FlightGear visual 확인
- 완료 항목:
  - PID 문제가 아니라 AP off 및 조종면 0 상태의 자유응답임을 확인
  - 초기 상승은 theta 2.5 deg와 wbody 0으로 생긴 양의 flight path, 그리고 neutral elevator에서 Cmo 0.1로 발생한 nose-up moment가 결합된 결과로 판단
- 미완료 항목:
  - steady no-thrust glide trim 조건 산출은 후속 작업으로 남김
- 최종 상태:
  - DONE
- Git commit:
  - 없음

## [2026-07-29 11:20] TASK-20260729-1120-001 - DONE

- 과업:
  - c172x no-alpha-limit 수평 전진 초기조건 run 생성 및 고도 그래프 확인
- 요청 내용:
  - theta 2.5 deg로 위를 보는 조건 대신 순항 비행처럼 앞으로 가고 있는 조건으로 변경해 다시 만들고 그래프 확인
- 목적:
  - 초기 pitch-up 자세에 의한 상승 성분을 제거한 뒤 고도 응답이 어떻게 변하는지 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 기존 7.0 케이스 보존
  - theta 0 deg, ubody 60 m/s, wbody 0인 7.1 초기조건 추가
  - 7.1 runscript 추가
  - CSV-only 실행 및 고도 비교 그래프 생성
- 제외 범위:
  - 모델 공력 계수 수정
  - no-thrust trim 산출
  - FlightGear visual 확인
- 완료 항목:
  - scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/initial_condition/7.1__rkss14l_500m_ubody60_level_init.xml 생성
  - scripts/c172x_4x75kg_cg_aligned_zeroprop_noalphalimit/runscript/7.1__rkss14l_500m_ubody60_level_neutral_zeroprop_noalphalimit_drop_run.xml 생성
  - run 7.1.2 CSV-only 실행 완료
  - 7.0 vs 7.1 altitude comparison PNG 생성
- 미완료 항목:
  - plotting runner는 실행 중 멈춰 종료했으며, 최종 검증은 CSV-only run 7.1.2로 수행
  - view_image는 sandbox helper 오류로 직접 렌더 확인 불가
- 최종 상태:
  - DONE
- Git commit:
  - 없음

## [2026-07-29 11:25] TASK-20260729-1125-001 - DONE

- 과업:
  - c172x no-alpha-limit theta -5 deg nose-down 비교 run 생성 및 검증
- 요청 내용:
  - nose down을 보기 위해 theta를 -5.0으로 변경한 run을 만들어 확인
- 목적:
  - 초기 nose-down 자세가 neutral zero-propulsion C172 고도 상승/출렁임을 얼마나 줄이는지 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - 기존 7.0/7.1 보존
  - theta -5.0 deg 7.2 초기조건 및 runscript 추가
  - CSV-only 실행 및 7.0/7.1/7.2 고도 비교 그래프 생성
- 제외 범위:
  - 모델 Cmo/elevator trim 수정
  - no-thrust steady glide trim 산출
  - FlightGear visual 확인
- 완료 항목:
  - 7.2 초기조건 및 runscript 생성
  - run 7.2.1 실행 완료
  - altitude_compare_7_0_7_1_7_2.png 생성
- 미완료 항목:
  - nose-down 자세만으로 pitch-up moment를 제거하지 못함
- 최종 상태:
  - DONE
- Git commit:
  - 없음

## [2026-07-29 11:42] TASK-20260729-1142-001 - DONE

- 과업:
  - c172x no-alpha-limit 초기 qdot 0 근접 Cmo 보정 variant 계산 및 실행
- 요청 내용:
  - 초기 qdot을 0에 가깝게 만드는 값을 계산해 다시 실행
- 목적:
  - 무추력, 조종면 0, theta 0 deg, ubody 60 m/s 조건에서 초기 pitch acceleration을 제거하고 고도 상승/출렁임 감소 확인
- 대상 프로젝트:
  - /home/junyeopkwon/jsbsim_workflow
- 작업 범위:
  - Cmo 보정값 계산
  - Cmo0 중간 variant와 Cmo trim qdot0 최종 variant 생성
  - 8.0 및 8.1 runscript/초기조건 생성
  - CSV-only 실행 및 비교 그래프 생성
- 제외 범위:
  - elevator trim 조종면 deflection 사용
  - 원본 c172x 또는 기존 no-alpha-limit variant 직접 수정
  - FlightGear visual 확인
- 완료 항목:
  - Cmo=0.0 variant 8.0 실행
  - 잔여 초기 qdot을 보고 Cmo=-0.01523148 계산
  - Cmo=-0.01523148 cmotrimq0 variant 8.1 실행
  - 8.1 초기 qdot = -1.1313e-7 rad/s^2 확인
- 미완료 항목:
  - Cmo 보정의 물리 타당성/원본 모델 대비 검증은 별도 필요
- 최종 상태:
  - DONE
- Git commit:
  - 없음

## [2026-07-29 12:05] TASK-20260729-1205-001 - 완료

- 과업: c172x no-thrust/no-alpha-limit 조건을 trim 상태에서 추락 시작하도록 변경
- 요청 내용: neutral fixed-control 시작 대신 trim 적용 후 조종면 위치 고정 방식으로 진행
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 작업 범위: elevator trim 고정 aircraft variant, 9.3 init/runscript, CSV-only 실행, native trim 실패 확인
- 제외 범위: Cmo 보정 확정, 추력/프로펠러 재도입, autopilot/PID 제어 사용
- 가정: no-thrust 조건에서는 JSBSim full trim이 수렴하지 않아 elevator actuator bias로 trim 위치를 고정
- 완료 항목: c172x_4x75kg_cg_aligned_zeroprop_noalphalimit_elevtrimq0 생성, elevator bias 0.092863537532 rad 적용, 9.3 run 성공
- 미완료 항목: no-thrust steady glide full equilibrium trim은 별도 수치 최적화 필요
- 최종 상태: 완료


## [2026-07-31 10:56] TASK-20260731-1056-001 - DONE

- 과업: KSFO 28R `5.16` 미션의 초반 활주로 중심 이탈, 초기 직접 조종 명령에 의한 튐, 최종 착륙 중심선 오차 검토 및 개선.
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: `5.16__ksfo28r_runway_return_circular_landing_run.xml` 실행 시 초반 중심선 이탈과 조작 튐, 마지막 착륙 중심선 불일치 현상을 검토.
- 작업 범위: raw CSV 기반 정량 분석, runscript 후보 생성, CSV-only runner 실행 검증, 최종 개선본 선정.
- 제외 범위: FlightGear 화면 직접 캡처 검증, 기체 XML/autopilot XML 구조 변경.
- 가정: JSBSim `mission/runway-cross-ft`를 활주로 중심선 오차 판단 기준으로 사용.
- 완료 항목: `5.17`~`5.22` 후보 생성 및 검증, 최종 추천본 `5.22__ksfo28r_centerline_balanced_final_landing_run.xml` 선정.
- 미완료 항목: FlightGear 시각 검증은 별도 수행 필요.
- 최종 상태: DONE

## [2026-07-31 13:55] TASK-20260731-1355-001 — DONE

- 과업: KSFO RWY 28R 정상 미션의 로테이트 직후 제어 입력 튐 완화
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 사용자가 제공한 theta/elevator plot에서 로테이트 직후 값이 튀는 것으로 보이며, 해당 현상을 줄이도록 수정 실행 요청
- 관련 파일:
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.26__ksfo28r_smooth_manual_pitch_ap_landing_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.28__ksfo28r_smooth_rotate_late_alt_hold_landing_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.29__ksfo28r_staged_altitude_ap_landing_run.xml`
  - `/home/junyeopkwon/jsbsim_workflow/scripts/c172x_4x75kg_cg_aligned_ksfo28r_landing/runscript/5.30__ksfo28r_manual_climb_damped_landing_run.xml`
- 작업 범위: 기존 `5.22` runscript는 보존하고 파생 runscript `5.26`부터 `5.30`까지 생성, CSV-only runner로 실행, raw CSV 기반 비교 분석
- 제외 범위: 기존 원본 runscript 삭제 또는 덮어쓰기, FlightGear 실시간 화면 검증, 플롯 자동 생성
- 가정: 사용자가 지적한 튐은 `STATE 3` 진입 직후 `ap/altitude_hold`가 켜지며 `ap/elevator_cmd`가 포화/반전되는 현상으로 판단
- 완료 조건: 새 runscript 중 최소 하나가 로테이트 직후 `fcs/elevator-pos-rad` 급변을 줄이고 전체 미션을 `STATE 23`까지 완료
- 완료 항목: `5.27.1` 기준 20-35초 elevator position range `0.047 rad`, AP elevator range `0.000`, final `STATE 23`, touchdown cross-track `-0.1 m`, stop cross-track `-1.1 m`
- 미완료 항목: `5.27`은 46초 AP altitude hold 재투입 시점에 elevator transient가 남음
- 최종 상태: `5.27__ksfo28r_smoother_rotate_manual_pitch_landing_run.xml`을 현재 추천 실행본으로 선정

## [2026-07-31 14:05] TASK-20260731-1405-001 — DONE

- 과업: 비교용 runscript 정리
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 방금 비교용으로 만든 것 중 멀쩡한 것만 남기고 삭제
- 완료 항목: `5.27` 추천본만 보존하고 `5.26`, `5.28`, `5.29`, `5.30` 관련 runscript 및 실행 로그 삭제
- 최종 상태: DONE

## [2026-07-31 14:18] TASK-20260731-1418-001 — DONE

- 과업: F450 CSV distance-from-start-lat-mt 및 distance-from-start-lon-mt 의미 확인
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: F450 raw CSV의 distance-from-start-lat-mt, distance-from-start-lon-mt가 시작지점을 원점으로 한 이동거리 스칼라인지 확인
- 작업 범위: 지정 CSV header 및 값 확인, JSBSim source property tie 및 getter 산식 확인
- 제외 범위: 코드 수정, CSV 재생성, plot 재생성
- 완료 항목: lat-mt와 lon-mt는 각각 시작점 기준 위도방향 및 경도방향 이동 성분이고, 전체 평면 스칼라 거리는 distance-from-start-mag-mt임을 확인
- 미완료 항목: 없음
- 최종 상태: DONE

## [2026-07-31 14:24] TASK-20260731-1424-001 — DONE

- 과업: workflow Excel 및 F450 CSV의 from-start-neu-n-ft 존재 여부 확인
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: workflow Excel에 position/from-start-neu-n-ft가 없는지 확인
- 작업 범위: workflow_all_cases_initial_settings.xlsx 내부 XML 문자열 검색, CSV Results 및 AC F450 sheet 구조 확인, F450 raw/sixdof_raw/sixdof_si header 확인
- 제외 범위: Excel 수정, CSV 재생성, 코드 수정
- 완료 항목: workflow_all_cases_initial_settings.xlsx에는 position/from-start-neu-n-ft 문자열 없음, 지정 raw CSV에도 없음, 대응 sixdof_raw와 sixdof_si에는 각각 /fdm/jsbsim/position/from-start-neu-n-ft 및 from_start_neu_n_m 존재 확인
- 미완료 항목: 없음
- 최종 상태: DONE

## [2026-07-31 15:56] TASK-20260731-1556-001 — DONE

- 과업: plotting 없이 통합 CSV 하나만 생성하는 JSBSim runner 추가
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: 기존 run_jsbsim_timestamped 계열로 실행하되 ploting은 만들지 않고 raw, sixdof_raw, sixdof_si처럼 나뉘는 CSV를 하나의 모든 property 통합 CSV로 생성하는 새 Python 파일 작성
- 작업 범위: 새 runner 파일 추가, combined CSV output 구성, F450 짧은 케이스 실행 검증
- 제외 범위: 기존 runner 파일 수정, 기존 CSV/plot 구조 삭제, 사용자의 기존 미추적 runner 파일 덮어쓰기
- 가정: 통합 CSV는 JSBSim raw property 이름을 보존한 단일 CSV를 의미하며 SI 변환 CSV는 별도 생성하지 않음
- 완료 조건: 새 Python runner가 문법 검증을 통과하고, F450 실행에서 logs/csv/combined 아래 단일 CSV를 생성하며 plotting 및 split CSV 생성을 수행하지 않음
- 완료 항목: scripts/run_jsbsim_timestamped_combined_csv_only.py 추가, combined output property union 구성, F450 1.0 ground launch 실행 검증 완료
- 미완료 항목: 없음
- 최종 상태: DONE

## [2026-07-31 16:08] TASK-20260731-1608-001 — DONE

- 과업: MATLAB JSBSim CSV plotter v6 기능 검토 및 개선 제안
- 대상 프로젝트: /home/junyeopkwon/jsbsim_workflow
- 요청 내용: logs/csv/run_jsbsim_csv_plotter_v6.m로 그래프를 만들고 있는데 분석 및 발표자료 구성 목적에 적합한지 검토하고 추가하면 좋은 기능 탐색
- 작업 범위: MATLAB 파일의 GUI 구성, 2D/3D plot 기능, 이벤트 표시, 저장 기능, 궤적 자동 탐지, CSV metadata 처리, 잠재 오류 확인
- 제외 범위: 코드 수정, MATLAB GUI 직접 실행, PNG 생성 검증
- 완료 항목: 현재 기능 요약, 버그성 항목, 발표자료 목적의 우선 개선 기능 도출
- 미완료 항목: MATLAB 런타임에서 직접 실행 검증은 수행하지 않음
- 최종 상태: DONE

## [2026-07-31 17:23] TASK-20260731-1723-001 — DONE

- 과업: MATLAB CSV plotter v7 구성
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: `run_jsbsim_csv_plotter_v6.m` 검토 결과를 바탕으로 JSBSim 로그 분석과 발표자료 구성에 유용한 기능을 실제로 구성
- 관련 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`, `logs/csv/run_jsbsim_csv_plotter_v6.m`
- 작업 범위: 기존 v6 보존, v7 새 파일 생성, 표준 분석 패키지 export, summary metrics CSV export, F450/C172/General 프리셋, Min/Max 표시 helper 누락 보완, F450 distance-from-start lat/lon 컬럼 후보 보강
- 제외 범위: MATLAB 앱 실기동 검증, PPT 자동 생성, 다중 CSV 비교 오버레이 구현
- 가정: 발표자료에는 반복적으로 동일한 항목의 PNG와 요약 지표 CSV가 우선 필요하며, v6는 비교/롤백용으로 유지하는 것이 안전함
- 완료 조건: v7 파일이 존재하고 핵심 버튼/함수/후보 컬럼이 정적으로 확인되며 F450 raw CSV 헤더와 주요 후보가 매칭됨
- 완료 항목: `run_jsbsim_csv_plotter_v7.m` 생성 및 기능 추가 완료
- 미완료 항목: MATLAB GUI에서 실제 버튼 클릭 실행 검증은 로컬 MATLAB 실행 파일이 PATH에 없어 미수행
- 최종 상태: 코드 구성 완료, MATLAB 환경에서 수동 실행 확인 필요
## [2026-07-31 17:47] TASK-20260731-1747-001 — DONE

- 과업: MATLAB CSV plotter v7 제목/축/범례 편집 기능 보강
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 그래프 제목과 축 제목을 쓸 수 있는 기존 기능에 글씨 크기 조절 기능을 추가하고, 범례에 표시할 문구도 수정 가능하게 구성
- 관련 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`
- 작업 범위: 2D/3D 제목 크기, 축 제목 크기, 범례 크기 입력 UI 추가. 3D 범례 표시 이름 테이블 추가. 2D는 기존 `범례 이름` 컬럼을 유지하고 범례 크기만 추가. 수동 그래프와 표준 PNG export에 폰트 크기 반영.
- 제외 범위: v6 수정, MATLAB GUI 실제 클릭 테스트, PPT 자동 생성 기능
- 가정: 2D 범례 이름은 기존 `series2DTable`의 `범례 이름` 컬럼으로 충분하며, 3D는 궤적/시작점/종료점/Min Z/Max Z 이름을 별도 테이블에서 바꾸는 방식이 가장 직접적임
- 완료 조건: `run_jsbsim_csv_plotter_v7.m`에 관련 UI와 callback 반영, MATLAB `checkcode`에서 문법 오류 없음
- 완료 항목: 제목/축/범례 글씨 크기 조절, 3D 범례 문구 수정, 3D 범례 표시 on/off, 초기화 시 기본값 복원
- 미완료 항목: MATLAB GUI를 실제로 열어 버튼 클릭 및 PNG 시각 결과 확인은 미수행
- 최종 상태: 코드 수정 및 MATLAB 정적 분석 완료
## [2026-07-31 18:02] TASK-20260731-1802-001 — DONE

- 과업: MATLAB CSV plotter v7 2D 범례 직접 입력 기능 수정
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 2D 그래프 범례가 property명으로 표시되는 문제를 고치고, 사용자가 제목/축 제목 입력 영역에서 작성한 범례 문구를 그대로 쓰게 변경
- 관련 파일: `logs/csv/run_jsbsim_csv_plotter_v7.m`
- 작업 범위: 2D 제목/축 제목 테이블에 `범례 이름` 행 추가, 쉼표/세미콜론/줄바꿈 구분 입력을 선택된 Y 계열 순서대로 `DisplayName`에 적용, 기존 property명은 fallback으로만 사용
- 제외 범위: v6 수정, GUI 클릭 테스트, 3D 범례 구조 변경
- 가정: 여러 2D 계열은 사용자가 선택한 Y 계열 순서대로 `범례 이름`에 쉼표로 입력하는 방식이 가장 직관적임
- 완료 조건: MATLAB `checkcode` fatal 오류 없음, resolver 함수와 plot 호출 연결 확인
- 완료 항목: 2D 직접 범례 입력 구현 완료
- 미완료 항목: MATLAB GUI에서 실제 CSV 로드 후 범례 표시 시각 확인은 미수행
- 최종 상태: 코드 수정 및 MATLAB 정적 분석 완료

## [2026-08-03 00:00] TASK-20260803-0000-001 — DONE

- 과업: JSBSim aircraft XML location 좌표계 기준 설명
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: 기체 XML의 모터 위치, 프롭 위치, CG, 시점, 탑승객 위치 좌표의 기준점과 원점 문의
- 작업 범위: 로컬 JSBSim 소스와 C172 XML의 `location` 정의 확인
- 제외 범위: 코드 수정, 기체 XML 수정, 시뮬레이션 실행
- 완료 항목: JSBSim structural frame의 축 방향과 CG 기준 body frame 변환식을 확인해 설명
- 최종 상태: DONE


## [2026-08-03 00:10] TASK-20260803-0010-001 — DONE

- 과업: C172 XML structural datum 원점 추정
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: `CG = (41.0, 0.0, 36.5)`이면 원점 위치를 찾을 수 있는지, nose 기준인지 문의
- 작업 범위: C172 XML의 CG, pointmass, nose gear, nose skid, tail skid 좌표 비교
- 완료 항목: CG 하나만으로 원점을 특정할 수는 없지만, C172 XML 좌표 분포상 원점은 nose tip이 아니라 nose/firewall 근처의 aircraft datum으로 추정된다고 설명
- 최종 상태: DONE

## [2026-08-10 11:20] TASK-20260810-1120-001 — DONE

- 과업: MiniTalon XML 설명 문서를 jsbsim_workflow로 이동 및 XML별 분리
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 기존 단일 문서가 아니라 Metrics.xml이면 Metrics.xml 내용만 담는 식으로 XML 파일별 문서를 만들고 jsbsim_workflow 아래에 폴더로 보관
- 작업 범위: /home/junyeopkwon/jsbsim/aircraft/MiniTalon/XML_VALUE_REFERENCE.md 내용을 기준으로 docs/minitalon_xml_reference 아래 XML별 Markdown 생성
- 제외 범위: MiniTalon XML 파라미터 변경, 기존 통합 문서 삭제
- 완료 조건: XML별 Markdown 문서가 별도 파일로 생성되고 index가 제공됨
- 완료 항목: docs/minitalon_xml_reference 폴더 생성 및 27개 Markdown 생성
- 미완료 항목: 기존 /home/junyeopkwon/jsbsim/aircraft/MiniTalon/XML_VALUE_REFERENCE.md 삭제는 안전 검토상 별도 명시 승인 전에는 수행하지 않음
- 최종 상태: DONE_WITH_NOTE


## [2026-08-10 22:35] TASK-20260810-2235-001 — DONE

- 과업: 첨부 DATCOM flight control/aerodynamics를 F450 파생 모델에 적용하고 원본 F450과 동일 자세진단 미션 비교
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 첨부 jsbsim_aerodynamic_database.xml 내부 데이터는 변경하지 않고 F450 파생 모델에 적용한 뒤, 멀티콥터 자세 적용 확인 미션을 원본 F450과 파생 F450에 동일하게 실행해 결과 비교
- 작업 범위: F450_DATCOM aircraft 생성, DATCOM metrics/flight_control/aerodynamics 병합, 자세 step 비교 runscript 생성, 원본/파생 모델 JSBSim 실행, combined CSV 로그 비교
- 제외 범위: autopilot gain tuning, DATCOM 원본 XML 수정, FlightGear 시각 검증, MATLAB plotter 실행
- 가정: 공력 확인을 위해 p/mode=2 altitude-hold attitude mode에서 roll/pitch setpoint step을 주는 미션을 사용한다. mode 3 position hold는 roll/pitch setpoint를 내부 위치제어 reference로 대체하므로 자세 적용 확인에는 부적합하다고 판단했다.
- 완료 조건: 원본 F450과 F450_DATCOM이 같은 미션으로 정상 종료되고, CSV 로그에서 고도/자세/공력 property 비교가 가능함
- 완료 항목: 새 aircraft 및 프로젝트 사본 생성, 비교 runscript 생성, F450 및 F450_DATCOM 실행, 요약 CSV 생성
- 미완료 항목: FlightGear 화면 확인, 공력 적용 후 안정성 튜닝, DATCOM table 변환 방식에 대한 별도 물리 검증
- 최종 상태: DONE_WITH_RISK


## [2026-08-10 22:40] CORRECTION-20260810-2240-001 — 정정

- 대상 기록: TASK-20260810-2235-001, PROGRESS-20260810-2235-001, DECISION-20260810-2235-001, TODO-20260810-2235-001, INDEX-20260810-2235-001
- 정정 이유: PowerShell command string에서 Markdown backtick escape가 적용되어 일부 경로와 row/table 표기가 제어문자로 기록됨
- 기존 내용: 일부 backtick-wrapped path 및 row+table, row+column 표기가 깨져 보임
- 정정 내용: 실제 변경 파일은 /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/F450_DATCOM/*, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/initial_condition/1.0__ground_park_heading0_init.xml, /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml 이다. JSBSim 호환을 위해 DATCOM base table 6개는 row plus table 구조에서 row plus column 구조로 재구성했으며 숫자 데이터는 변경하지 않았다.
- 영향 범위: 작업 기록 문서 표기 정정만 해당. 모델 파일, runscript, CSV 로그에는 영향 없음
- 검증 결과: INDEX.md 최신 tail에서 정정 항목이 append됨
- 다음 작업: 최종 응답에서는 정정된 경로와 결과만 보고


## [2026-08-10 22:50] TASK-20260810-2250-001 — DONE

- 과업: F450 원본과 F450_DATCOM attitude diagnostic 결과 그래프 비교 산출
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 표보다 그래프로 원본 F450과 공력 적용 파생 F450 결과를 비교
- 작업 범위: 기존 combined CSV 두 개를 읽어 시간축 비교 PNG 생성, 이미지 파일 메타데이터 검증, 작업 기록 append
- 제외 범위: JSBSim 재실행, controller tuning, 그래프 수동 시각 검수
- 가정: 직전 실행 산출물 08102235 timestamp CSV를 기준 비교 데이터로 사용
- 완료 조건: 고도/자세/속도/공력 force/moment/DATCOM coefficient 그래프가 PNG로 생성됨
- 완료 항목: plots/F450_DATCOM_attitude_compare_08102235 아래 PNG 5개 생성 및 Codex visualization 폴더 복사본 생성
- 미완료 항목: view_image 도구가 sandbox helper 오류로 직접 렌더 확인을 수행하지 못함
- 최종 상태: DONE_WITH_NOTE


## [2026-08-10 23:00] TASK-20260810-2300-001 — DONE

- 과업: F450_DATCOM 공력 적용 확인용 1~6번 검증 전체 실행 및 별도 문서화
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 공력 적용 확인을 위한 1~6번 테스트를 모두 수행하고 별도 문서로 정리
- 작업 범위: catalog/property 확인, DATCOM table 보존 확인, qbar force/moment 응답 분석, control sign 확인, attitude-mode A/B 비교, propulsion-off free-response 비교, Markdown 문서 작성
- 제외 범위: FlightGear 시각 검증, controller gain tuning, DATCOM reference geometry 재설계
- 가정: 직전 attitude 비교 실행 08102235와 신규 propulsion-off free-response 실행 08102253을 검증 데이터로 사용
- 완료 조건: 6개 검증 항목이 정량 산출물과 문서로 남음
- 완료 항목: aero_validation_checks_08102253.csv 생성, propulsion-off 미션 추가 및 F450/F450_DATCOM 실행, free-response PNG 2개 생성, docs/F450_DATCOM_AERO_VALIDATION.md 작성
- 미완료 항목: position-hold hover 장시간 검증과 tuning은 후속 작업으로 남김
- 최종 상태: DONE

## [2026-08-11 16:45] TASK-20260811-1645-001 — DONE_WITH_RISK

- 과업: AD3000 JSBSim workflow variant 및 실행 스크립트 구성
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: AD3000 aircraft 구성을 workflow에서도 사용할 수 있도록 구성 파일과 runscript를 배치
- 작업 범위: 생성 스크립트 추가, aircraft_variants/AD3000 미러 생성, scripts/AD3000 초기조건 및 smoke runscript 생성
- 제외 범위: 기존 workflow Excel 반영, batch runner 연결, hover 튜닝 완료
- 가정: 실제 실행 root는 /home/junyeopkwon/jsbsim이며 workflow variant는 추적/비교용 복사본
- 완료 항목: AD3000 workflow variant와 1.0 smoke runscript 생성
- 미완료 항목: 8초 hover run FPE로 안정 hover 검증 미완료
- 최종 상태: 구성 완료, 장시간 동특성 검증은 후속 필요

## [2026-08-11 00:00] TASK-20260811-0000-002 — 완료

- 과업: AD3000 제품 기반 모터/프롭 파일 추가 구성
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: Hobbywing V6215 210KV, Hobbywing V6212 180KV, Falcon C2E 20x10, Hobbywing VSC 22.1x7.4 제품 자료의 추력/전력 데이터를 확인하여 JSBSim 모터/프롭 파일과 AD3000 propulsion 구성을 갱신
- 관련 파일: AD3000 Propulsion.xml, AD3000 제품 모터/프롭 XML, PROPULSION_PRODUCTS.md, PROPULSION_SOURCE_DATA.csv
- 수행 내용: lift는 V6212 180KV와 VSC 22.1x7.4 공개 pull test 표를 기준으로, cruise는 V6215 210KV 모터 사양과 Falcon C2E 20x10 형상 및 공개 22x12 표의 피치 비례 추정을 기준으로 구성함
- 변경 이유: 초기 임의 모터/프롭 값을 실제 제품 사양과 공개 추력/전력 근거가 있는 값으로 교체하기 위함
- 검증 명령어: xmllint --noout, JSBSim --catalog, JSBSim smoke hover run --end=1.5
- 검증 결과: XML well-formed 확인, AD3000 catalog 로드 성공, 1.5초 smoke 실행 성공
- 검증하지 못한 항목: Falcon C2E 20x10 직접 추력/전력 시험표는 제공 페이지에서 확인하지 못함. 8초 전체 hover run의 Floating point exception은 이번 제품 데이터 반영 범위에서 해결하지 않음
- 가정: JSBSim propeller 계수는 정지 추력 기반 Ct/Cp와 일반 advance ratio 형상을 결합해 구성함. Cruise 20x10은 Falcon C2E 22x12 공개 표에서 피치비 10/12로 추정함
- 남은 리스크: Cruise prop 성능은 실제 20x10 벤치 데이터 확보 시 재보정 필요. Lift hover 안정성은 전후 로터 추력 분배 제어가 필요
- 다음 작업: 실제 Falcon 20x10 시험표 또는 모터-프롭 벤치 데이터를 확보해 cruise prop 계수를 재계산하고, 전후 collective split 제어를 추가 검증
- 관련 기록: PROGRESS-20260811-0000-002, DECISION-20260811-0000-002, TODO-20260811-0000-002
- Git commit: 없음

## [2026-08-11 17:11] CORRECTION-20260811-1711-001 — 정정

- 대상 기록: TASK-20260811-0000-002, PROGRESS-20260811-0000-002, DECISION-20260811-0000-002, TODO-20260811-0000-002, INDEX-20260811-0000-002
- 정정 이유: 제품 기반 propulsion 반영 기록을 append할 때 기록 시각을 임시값 2026-08-11 00:00으로 남김
- 기존 내용: 기록 시각이 2026-08-11 00:00 또는 ENTRY ID 20260811-0000으로 표기됨
- 정정 내용: 해당 항목의 실제 기록 시각은 2026-08-11 17:11 KST임. 기록 내용과 검증 결과는 그대로 유효함
- 영향 범위: docs/agent-log 아래 Markdown 기록의 메타데이터 시각 표기
- 검증 결과: append-only 방식으로 정정 기록을 추가함
- 다음 작업: 이후 기록에서는 실제 KST 시각을 사용

## [2026-08-12 09:00] TASK-20260812-0900-001 — 완료

- 과업: AD3000 cruise propulsion을 공개 데이터 시트 기준으로 재정리
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: V6215와 V6212 모두 공개된 22.1x7.4 데이터 시트를 기준으로 motor/prop 파일을 구성하고, 원래 cruise prop은 20x10이나 공개 스펙이 없어 22.1x7.4를 임시 적용한다는 주석을 AD3000 XML 내부에 한글로 남김
- 관련 파일: Propulsion.xml, AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, PROPULSION_PRODUCTS.md, PROPULSION_SOURCE_DATA.csv, AD3000_generate_aircraft.py
- 수행 내용: cruise thruster 참조를 Falcon 20x10 추정 파일에서 Hobbywing VSC 22.1x7.4 공개표 기반 파일로 교체하고, XML documentation 및 주석을 한글로 정리함
- 변경 이유: Falcon 20x10 직접 thrust/power sheet가 없는 상태에서 추정값을 쓰는 것보다, 공개 pull test가 있는 V6215+VSC22.1x7.4 조합을 임시 기준으로 삼는 편이 근거 추적성이 높음
- 검증 명령어: xmllint --noout, python3 -m py_compile, JSBSim --catalog, JSBSim smoke run --end=1.5
- 검증 결과: XML well-formed 통과, 생성 스크립트 문법 통과, AD3000 catalog 로드 성공, 1.5초 smoke run 성공
- 검증하지 못한 항목: Falcon C2E 20x10 직접 thrust/power sheet와 8초 전체 hover 안정성
- 가정: cruise prop은 실제 의도 규격과 다르며, 공개 데이터 확보 전까지 임시 VSC 22.1x7.4 모델을 사용함
- 남은 리스크: 실제 Falcon 20x10 적용 시 cruise 추력과 전력 계수는 달라질 수 있음
- 다음 작업: Falcon 20x10 실측 또는 제조사 성능표 확보 후 cruise prop XML 재보정
- 관련 기록: PROGRESS-20260812-0900-001, DECISION-20260812-0900-001, TODO-20260812-0900-001
- Git commit: 없음

## [2026-08-12 09:14] TASK-20260812-0914-001 — 완료

- 과업: AD3000 XML 적용값 검증 방법 구체화 및 자동 검증 스크립트 추가
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: JSBSim 실행 시 비행 결과가 아니라 AD3000 XML 전체에 적용된 값이 제대로 들어갔는지 확인하는 방법 제시
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py, AD3000 XML 패키지, SOURCE_MATRIX.csv, PROPULSION_SOURCE_DATA.csv
- 수행 내용: AD3000.xml include, Mass.xml, Metrics.xml, Propulsion.xml, motor XML, prop XML, source CSV 계수 비교, JSBSim catalog load를 자동 확인하는 검증 스크립트를 추가하고 실행함
- 변경 이유: 단순 hover 실행 결과는 자세 안정성 문제와 XML 적용값 문제를 분리하기 어려우므로, 정적 구성값 검증과 catalog load를 먼저 수행하기 위함
- 검증 명령어: python3 -m py_compile /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py
- 검증 결과: 통과
- 검증 명령어: python3 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_validate_config.py --run-jsbsim
- 검증 결과: PASS 86, FAIL 0
- 검증하지 못한 항목: 실제 동특성 안정성, 8초 hover FPE, 전이비행 성능
- 가정: SOURCE_MATRIX.csv와 PROPULSION_SOURCE_DATA.csv가 현재 AD3000 XML의 기준 데이터임
- 남은 리스크: 검증 스크립트는 XML 적용값 검증용이며 비행 품질 검증은 별도 runscript와 로그 분석이 필요함
- 다음 작업: 필요 시 output CSV 기반 동특성 검증 스크립트를 별도로 추가
- 관련 기록: PROGRESS-20260812-0914-001
- Git commit: 없음

## [2026-08-12 09:19] TASK-20260812-0919-001 — 완료

- 과업: AD3000 XML table 조건별 보간값 확인 도구 추가
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: JSBSim table이 특정 조건에서 해당 값을 제대로 표현하는지 확인하는 방법 제공
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_eval_table.py
- 수행 내용: propeller 1D table과 Aero.xml 2D/3D table을 입력 조건별로 보간 계산하는 도구를 추가하고 예시 실행을 확인함
- 변경 이유: JSBSim 전체 동적 실행에서는 table 값, qbar 곱, 자세/속도 변화가 섞이므로 XML table 자체의 기대 보간값을 분리해 확인하기 위함
- 검증 명령어: python3 -m py_compile /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/AD3000_eval_table.py
- 검증 결과: 통과
- 검증 명령어: AD3000_eval_table.py로 C_THRUST, C_POWER, CL_base, CL_de 예시 실행
- 검증 결과: 각 조건에서 보간값과 사용된 breakpoint/grid 정보를 출력함
- 검증하지 못한 항목: JSBSim 내부 force/moment output과 table-only 값의 동시 비교 runscript는 아직 추가하지 않음
- 가정: table-only 검증은 XML table interpolation 기대값 확인용이며, JSBSim 전체 함수 출력은 추가 곱셈 항과 동역학 상태를 포함할 수 있음
- 남은 리스크: Aero.xml function은 qbar-area 등 product 항을 포함하므로 JSBSim output property와 table-only 값은 직접 같지 않을 수 있음
- 다음 작업: 필요 시 runscript output property와 table evaluator 결과를 비교하는 동적 검증을 추가
- 관련 기록: PROGRESS-20260812-0919-001
- Git commit: 없음

## [2026-08-12 09:40] TASK-20260812-0940-001 — 완료

- 과업: C:/Users/junyeopkwon/Downloads/DB 정리.xlsx의 기체 Spec 시트 기반 AD3000 propulsion 데이터 반영
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 엑셀 기체 Spec 시트에 정리된 공식 홈페이지 데이터를 기준으로 propulsion 쪽 값을 변경
- 관련 파일: Propulsion.xml, PROPULSION_PRODUCTS.md, PROPULSION_SOURCE_DATA.csv, AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, AD3000_generate_aircraft.py, AD3000_validate_config.py
- 수행 내용: 기체 Spec 시트의 V6215+VSC22.1x7.4 및 V6212+VSC22.1x7.4 전체 throttle 표 44행을 PROPULSION_SOURCE_DATA.csv에 반영하고, 45-84% 구간을 used_for_coefficient=Y로 표시해 prop XML Ct/Cp 산정 기준으로 사용함
- 변경 이유: propulsion 원자료 기준을 외부 웹 직접 입력값이 아니라 사용자가 제공한 엑셀의 기체 Spec 시트로 맞추기 위함
- 검증 명령어: xmllint --noout, python3 -m py_compile, AD3000_validate_config.py --run-jsbsim, JSBSim smoke run --end=1.5
- 검증 결과: XML 검사 통과, Python 문법 통과, 적용값 검증 PASS 86 FAIL 0, 1.5초 smoke run 성공
- 검증하지 못한 항목: 8초 hover 안정성, 실제 20*10 cruise prop 성능표
- 가정: prop XML 계수는 기체 Spec 시트의 공식표 중 45-84% throttle 구간 평균 Ct/Cp를 사용함
- 남은 리스크: cruise 실기 의도 prop 20*10의 직접 성능표가 없어 VSC22.1x7.4 임시 적용 상태임
- 다음 작업: 20*10 직접 thrust/power sheet 확보 시 cruise prop XML 재보정
- 관련 기록: PROGRESS-20260812-0940-001, DECISION-20260812-0940-001
- Git commit: 없음

## [2026-08-12 09:46] TASK-20260812-0946-001 — 완료

- 과업: AD3000 propulsion 계수 산정에 기체 Spec 시트 33-100% 전체 데이터 반영
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 공식 데이터가 33-100% 전체 구간으로 있는데 일부 45-84%만 사용하는 것은 부적절하므로 전체 데이터를 사용하도록 변경
- 관련 파일: PROPULSION_SOURCE_DATA.csv, PROPULSION_PRODUCTS.md, AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, AD3000_generate_aircraft.py
- 수행 내용: PROPULSION_SOURCE_DATA.csv의 44개 행 전체를 used_for_coefficient=Y로 변경하고, lift/cruise prop XML의 Ct0/Cp0를 전체 33-100% 평균으로 재계산함
- 변경 이유: 시뮬레이션 목적에서는 제공된 공식 데이터 전체를 기본 반영하는 것이 타당하기 때문
- 검증 명령어: xmllint --noout, python3 -m py_compile, AD3000_validate_config.py --run-jsbsim, JSBSim smoke run --end=1.5
- 검증 결과: XML 검사 통과, Python 문법 통과, 적용값 검증 PASS 86 FAIL 0, 1.5초 smoke run 성공
- 검증하지 못한 항목: 실제 throttle별 coupled motor-prop map 구현, 8초 hover 안정성
- 가정: 현재 JSBSim prop XML 구조에서는 throttle별 표 전체를 직접 map으로 넣는 대신 전체 행 평균 Ct/Cp를 대표 계수로 사용함
- 남은 리스크: 진짜 전체 데이터를 동적으로 쓰려면 throttle/RPM/thrust/power map 기반 모델링이 별도로 필요함
- 다음 작업: 필요 시 throttle별 static thrust/power table을 JSBSim system/function으로 별도 구현
- 관련 기록: PROGRESS-20260812-0946-001, DECISION-20260812-0946-001
- Git commit: 없음

## [2026-08-12 09:55] TASK-20260812-0955-001 — 완료

- 과업: AD3000 prop XML 전진비 table 산정 한계 주석 추가
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 엑셀 static pull test 데이터로 J=0만 직접 계산 가능하고 J>0 table은 임시 shape라는 점을 XML과 문서에 주석으로 명확히 남김
- 관련 파일: AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml, AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml, Propulsion.xml, PROPULSION_PRODUCTS.md, AD3000_generate_aircraft.py
- 수행 내용: prop XML documentation, Propulsion.xml 한글 주석, products 문서에 전진비 J 공식과 static test 한계, J>0 값의 임시 advance-ratio shape 적용 사실을 추가함
- 변경 이유: 모델에 임시 생성값이 들어간 경우 산정 근거와 한계를 XML 내부에서 바로 확인할 수 있어야 하기 때문
- 검증 명령어: xmllint --noout, python3 -m py_compile, AD3000_validate_config.py --run-jsbsim
- 검증 결과: XML 검사 통과, Python 문법 통과, 적용값 검증 PASS 86 FAIL 0
- 검증하지 못한 항목: 실제 전진비별 prop performance map
- 가정: 기체 Spec 시트의 pull test는 V=0 static data로 해석함
- 남은 리스크: J>0 table은 실측값이 아닌 초기 가정
- 다음 작업: airspeed/RPM/thrust/power가 포함된 prop map 확보 시 J별 Ct/Cp table 재작성
- 관련 기록: PROGRESS-20260812-0955-001
- Git commit: 없음


## [2026-08-12 00:00] TASK-20260812-0000-001 — DONE

- 과업: `5.16` runscript의 원형 선회 시간 구간 확인
- 대상 프로젝트: `/home/junyeopkwon/jsbsim_workflow`
- 요청 내용: `5.16` runscript에서 선회 부분만 별도 runscript로 만들거나, 그래프 시간축 적용을 위한 선회 시간 확인
- 작업 범위: `5.16__ksfo28r_runway_return_circular_landing_run.xml`의 선회 이벤트와 최신 `5.16.6` raw CSV 상태 전이 시간 확인
- 완료 항목: 원형 선회 구간이 `STATE 6`부터 `STATE 10` 진입 직전이며, 최신 로그 기준 `183.742 s`부터 `244.308 s`까지임을 확인
- 최종 상태: 별도 runscript 생성 없이 그래프 시간축 구간 안내로 완료

## [2026-08-13 13:39] TASK-20260813-1339-001 — 완료

- 과업: standard_vtol_demo JSBSim 단독 모델 구성 및 DATCOM 공력 연결 1차 검증
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow, /home/junyeopkwon/jsbsim
- 요청 내용: Downloads의 standard_vtol_demo.xml을 JSBSim 단독 시뮬레이션 가능한 모델로 구성하고 jsbsim_aerodynamic_database.xml을 공력 데이터로 사용하게 구성. 기존 demo 공력과 교체 가능하게 두고, 데이터 연결 및 5개 모터 아밍 확인.
- 작업 범위: 항공기 XML 구성, DATCOM 공력 테이블 JSBSim 호환 변환, 모터 arming gate 추가, JSBSim aircraft 설치, 단기 실행 검증 스크립트 작성 및 실행.
- 제외 범위: 정상 비행 시나리오, 수직이륙-착륙 자동 시나리오, 천이 제어, 비행 안정성 튜닝.
- 가정: 원본 Downloads 파일은 덮어쓰지 않고 workflow 및 JSBSim aircraft 폴더에 작업 복사본을 둔다.
- 완료 조건: JSBSim이 모델을 로딩/실행하고, DATCOM 공력 함수가 catalog 및 실행 출력에 나타나며, 5개 모터가 arming 전 0 출력 및 arming 후 명령값 전달을 보일 것.
- 완료 항목: standard_vtol_demo_jsbsim 항공기 폴더 생성, DATCOM 기본 모델 및 demo aero variant 생성, 5개 모터 arming gate 추가, 검증 CSV 생성.
- 미완료 항목: DATCOM 3D Mach breakpoint 제어증분 전체 보간 복원, 비행 가능성 검증, 시나리오 구성.
- 최종 상태: 1차 모델 구성 및 데이터/모터 arming 확인 완료.

## [2026-08-13 14:45] TASK-20260813-1445-001 — DONE

- 과업: standard_vtol_demo JSBSim 단독 수직 미션 구성 및 실행
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 김포공항 14번 활주로 위 초기 위치에서 시동 -> 수직이륙(10m) -> 호버링(10s) -> 수직착륙 -> 시동종료 미션을 구성하고 JSBSim으로 실행한다.
- 작업 범위: JSBSim runscript, 초기조건, hover 제어 variant, 실행 결과 CSV/log 생성 및 검증
- 제외 범위: 전방/후방 천이, 고정익 미션, 실제 PX4 오토파일럿 연동 검증, 비행 품질 최종 튜닝
- 가정: 김포공항 14번 활주로 좌표는 기존 RKSS 14L 초기조건의 lat 37.5707083333, lon 126.7782777778, heading 135.01 deg를 재사용한다.
- 완료 조건: 미션 상태가 종료 상태까지 진행되고, 10m 근처 호버 구간과 착륙 후 motor-armed=0 및 esc-out[0..4]=0을 확인한다.
- 완료 항목: 초기조건 작성, 수직 미션 runscript 작성, JSBSim hover attitude/altitude controller variant 구성, CSV에 mission/state 포함, 최종 JSBSim 실행 완료
- 미완료 항목: pusher 모터는 수직 미션에서 명령 0으로 유지됨. 천이/고정익 구간은 다음 단계에서 별도 구성 필요.
- 최종 상태: DONE

## [2026-08-13 15:04] TASK-20260813-1504-001 — DONE

- 과업: standard_vtol_demo 계열 XML을 F450식 모듈 분리 구조로 개정
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 공력/제어를 포함한 각 모듈을 F450처럼 별도 XML 파일로 분리하고, 메인 XML에서 선택해 불러오도록 구성한다.
- 작업 범위: standard_vtol_demo, standard_vtol_demo_hover의 JSBSim aircraft 디렉터리와 workflow mirror 디렉터리 모듈화
- 제외 범위: JSBSim propulsion 섹션 신규 설계, PX4 flightcontrol 동일 재현, 천이 미션
- 가정: 현재 모델은 top-level propulsion 섹션이 없고 rotor/pusher force가 external_reactions로 구현되어 있으므로 propulsion-equivalent 물리 힘 모듈은 ExternalReactions.xml로 분리한다.
- 완료 조건: 메인 XML은 F450처럼 file attribute include만 갖고, 공력은 Aero_DATCOM.xml/Aero_Demo.xml로 교체 가능하며, JSBSim catalog/arming/aero/vertical mission 검증이 통과한다.
- 완료 항목: Metrics.xml, Mass.xml, Gear.xml, Effectors.xml, FlightControl.xml, ExternalReactions.xml, Aero_DATCOM.xml, Aero_Demo.xml 분리. default main은 Aero_DATCOM.xml을 로드. demo/datcom main variant 파일 생성.
- 미완료 항목: 별도 JSBSim propulsion 엔진/스러스터 모델로 재구성은 하지 않음.
- 최종 상태: DONE

## [2026-08-13 15:10] TASK-20260813-1510-001 — DONE

- 과업: standard_vtol_demo_hover runner 선택 오류 수정
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: run_jsbsim_timestamped_combined_csv_only.py에서 standard_vtol_demo_hover 선택 시 No init XML options found 오류가 발생하는 문제를 수정한다.
- 원인: 이전 작업은 JSBSim runscript를 직접 실행했으며, workflow runner가 요구하는 scripts/standard_vtol_demo_hover/initial_condition 및 scripts/standard_vtol_demo_hover/runscript 배치를 만들지 않았다. 또한 init 파일명에 runway가 포함되어 discover_runscripts의 *run*.xml 검색에 init XML이 섞였다.
- 완료 항목: standard_vtol_demo_hover용 init/runscript 추가, discover_runscripts에서 initial_condition 폴더 제외, 메뉴 선택 78 -> 1 -> 1 실행 검증
- 최종 상태: DONE

## [2026-08-13 15:50] TASK-20260813-1550-001 — DONE

- 과업: standard_vtol_demo_hover 천이 포함 JSBSim runscript 구성
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: PX4 VTOL lift+cruise/standard VTOL 천이 로직을 확인하고, 전방천이와 후방천이를 포함한 runscript를 구성한다.
- 작업 범위: PX4 로컬 소스 확인, standard_vtol_demo_hover FlightControl/Effectors 보정, transition mission runscript 생성, workflow runner 메뉴 실행 검증
- 제외 범위: PX4 controller 완전 복제, TECS/FW position controller 구현, DATCOM elevator control effectiveness 신규 생성, propulsion 섹션 재구성
- 가정: standard_vtol_demo_hover는 lift+cruise/standard VTOL 구조로 보고, PX4 standard.cpp의 pusher ramp, mc_weight blending, backtransition pusher cut 및 MC ramp-up 로직을 JSBSim runscript 상태 머신으로 근사한다.
- 완료 조건: runner 메뉴에서 78 -> 1 -> 2 선택으로 천이 미션이 실행되고, mission/state가 종료 상태까지 진행되며 최종 motor-armed=0 및 esc-out[0..4]=0을 확인한다.
- 완료 항목: 2.0__rkss14_transition_mission_run.xml 생성, fcs/mc-weight 블렌딩 추가, hover attitude target 추가, 제어 채널을 FlightControl.xml로 이동, runner 메뉴 방식 실행 검증
- 미완료 항목: FW 모드에서 MC weight를 완전 0으로 끄는 PX4 strict 구현은 보류. 현재 DATCOM 공력에 elevator effectiveness가 없어 JSBSim standalone 안정성 확보를 위해 FW 구간에 mc-weight 0.22를 남김.
- 최종 상태: DONE

## [2026-08-13 17:16] TASK-20260813-1716-001 — DONE

- 과업: standard_vtol_demo_hover 멀티콥터 조종자격증 유사 미션 runscript 구성
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 고정익/천이를 제외하고 멀티콥터 모드로 정상 미션을 새로 구성한다. 기존 4.305 ft AGL 초기조건은 유지하되, 지상 안정 CG 높이에 맞춘 1.1_rkss14_runway_ground_init.xml 버전을 만들고 새 3.0 runscript를 구성한다.
- 작업 범위: standard_vtol_demo_hover 초기조건 추가, 멀티콥터 전용 runscript 추가, JSBSim 단독 hover speed hold 보조 채널 추가, workflow 및 /home/junyeopkwon/jsbsim aircraft mirror 동기화, runner 메뉴 실행 검증
- 제외 범위: PX4 연동, 고정익 모드, 전방/후방 천이, 실제 시험장 geometry 및 채점 기준 정밀 재현, GPS waypoint controller 구현
- 가정: 김포공항 RKSS 14번 활주로 좌표는 기존 lat 37.5707083333, lon 126.7782777778, heading 135.01 deg를 유지한다. 실기시험 유사 sequence는 이륙, 4 m hover, 좌우/전후진, 삼각, 원주 근사, 비상 하강/복구, 정상 착륙, shutdown 순서로 근사한다.
- 완료 조건: runner 메뉴에서 78 -> 2 -> 3 선택으로 3.0 runscript가 실행되고, mission/state가 종료 상태까지 진행되며, mc-weight=1 및 pusher motor=0을 유지하고 최종 motor-armed=0 및 esc-out[0..4]=0을 확인한다. 1.1 초기조건에서 초기 자유낙하성 충격이 사라졌는지 첫 1초 수직속도와 gear force로 확인한다.
- 완료 항목: 1.1__rkss14_runway_ground_init.xml 생성, 3.0__rkss14_multicopter_certificate_mission_run.xml 생성, FlightControl.xml에 기본 off인 hover speed hold target 채널 추가, Effectors.xml에 speed hold property 추가, workflow 및 /home/junyeopkwon/jsbsim mirror 반영, JSBSim runner 실행 검증 완료
- 미완료 항목: 실제 자격시험 코스 거리/콘 위치/원주 geometry를 좌표 기반으로 엄밀히 추종하는 controller는 아직 없음. 현재는 body speed target 기반의 JSBSim standalone mission proof임.
- 최종 상태: DONE
## [2026-08-13 17:41] TASK-20260813-1741-001 — DONE

- 과업: standard_vtol_demo_hover 3.0 runscript 상태 완료 기반 전이로 수정 및 제어 구성 확인
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 3.0 runscript가 전역 시간 조건만으로 진행되지 않게 이전 미션이 끝나야 다음 미션이 진행되도록 구성하고, 원주비행 이후 긴급강하 없이 착륙하게 변경한다. 현재 제어가 멀티콥터 명령처럼 앞/뒤/좌/우 모터 추력 차이로 동작하는지 확인한다.
- 작업 범위: 3.0__rkss14_multicopter_certificate_mission_run.xml 상태 전이 조건 개정, 긴급강하/recovery state 제거, runner 실행 검증, FlightControl.xml/ExternalReactions.xml mixer 구조 확인
- 제외 범위: 실제 waypoint position controller 구현, yaw heading command 추가, 실제 시험장 geometry 정밀 추종
- 가정: hover/leg duration을 위한 절대 trigger 시각은 보조 조건으로 유지하되, 모든 주 미션 전이는 mission/state eq 이전상태 조건을 필수로 한다.
- 완료 조건: 3.0 runner 실행이 최종 shutdown/terminate까지 진행되고, 원주비행 이후 normal landing으로 바로 전이되며, mc-weight=1 및 pusher=0을 유지한다. 제어 mixer의 motor differential 구조를 XML과 CSV로 확인한다.
- 완료 항목: 3.0 runscript 상태 게이트 적용, emergency descent/recovery 제거, 원주 완료 hover 후 정상 착륙 구성, 3.0.5 실행 검증, 제어 mixer 확인
- 미완료 항목: hover duration timer가 완전한 상대 시간 타이머가 아니라 절대 trigger + state gate 방식이다. 현재 JSBSim script 내에서 phase start time을 직접 저장하는 패턴은 확인하지 못했다.
- 최종 상태: DONE
## [2026-08-13 17:45] TASK-20260813-1745-001 — DONE

- 과업: 3.0 runscript 버전 오염 정정 및 3.1 분리
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 기존 3.0은 보존하고, 수정한 state-gated/긴급강하 제거 버전은 3.1로 분리한다.
- 작업 범위: 3.0__rkss14_multicopter_certificate_mission_run.xml 이전 버전 복구, 3.1__rkss14_multicopter_certificate_mission_state_gated_run.xml 신규 분리, 두 버전 실행 검증, 이전 기록 정정
- 완료 항목: 3.0은 3.0.2 generated runscript 기준 이전 동작으로 복구. 3.1은 state-gated 및 원주 후 착륙 버전으로 생성. 3.0.6 및 3.1.1 실행 검증 완료.
- 최종 상태: DONE
## [2026-08-13 18:07] TASK-20260813-1807-001 — DONE

- 과업: standard_vtol_demo_hover metric, mass_balance, nose 기준 좌표 갱신
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: wingarea, wingspan, chord, wing_incidence, htail/vtail area/arm을 새 값으로 바꾸고, CG=(649.14 mm,0,0), emptywt=20 kg로 설정한다. 기존 CG 기준으로 잡힌 좌표를 새 CG점 기반으로 변환하되 XML 내부 좌표는 nose 끝점 기준으로 둔다.
- 작업 범위: standard_vtol_demo_hover 활성 모듈 Metrics.xml, Mass.xml, Gear.xml, ExternalReactions.xml 및 /home/junyeopkwon/jsbsim/aircraft/standard_vtol_demo_hover mirror 동기화
- 제외 범위: source_*.xml 원본 보관 파일, 과거 all-in-one 복사본, inertia 재산정, hover controller gain/throttle 재튜닝, standard_vtol_demo 비-hover variant
- 가정: 기존 active module 좌표는 CG=0 기준 상대좌표로 해석하고, JSBSim 구조좌표는 nose에서 aft 방향 +x로 둔다. 따라서 x_nose = x_old_relative_to_CG + 0.64914 m로 변환한다.
- 완료 조건: 요청 metric/mass 값이 XML에 들어가고, active location 좌표가 nose 기준으로 변환되며, XML 검사 및 3.1 미션 로딩/실행이 통과한다.
- 완료 항목: Metrics.xml 값 갱신, wing_incidence 추가, Mass.xml emptywt/CG 갱신, Gear/ExternalReactions x 좌표 nose 기준 변환, workflow와 /home/junyeopkwon/jsbsim mirror 반영, XML 검사 및 3.1 미션 실행 검증 완료
- 미완료 항목: inertia는 요청대로 기존값 유지. htailarm/vtailarm은 확인 불가값으로 0.0 m 반영. 제어 gain과 hover throttle base는 기존값 유지.
- 최종 상태: DONE
## [2026-08-13 18:14] TASK-20260813-1814-001 — DONE

- 과업: 20 kg 변경 기체용 hover throttle 및 멀티콥터 제어 구성
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 변경된 기체 질량/좌표에 맞는 hover throttle을 구하고, 제어 방식을 구성한다.
- 작업 범위: 20 kg 기준 lift motor hover ESC 산출, Effectors.xml 기본 hover-throttle-base 갱신, 3.2/3.3/3.4 runscript 버전 분리, 3.2/3.3/3.4 실행 비교 검증
- 제외 범위: thrust table 재식별, full PID 재설계, waypoint position controller, yaw controller, gear spring/damping 튜닝
- 가정: lift motor thrust table은 현재 ExternalReactions.xml의 0.5=9.45 lbf, 0.7=18.5 lbf 선형 구간을 사용한다. 20 kg 중량은 약 44.16 lbf이며 hover는 모터당 약 11.04 lbf가 필요하다.
- 완료 조건: hover collective가 약 0.535 근처에서 4 m hover를 유지하고, 최종 mission 종료 및 motor off를 확인한다.
- 완료 항목: hover throttle base 0.535 반영, 3.2 20kg hover baseline mission 생성/검증, 3.3 staged landing mission 생성/검증, 3.4 staged landing + slow spooldown mission 생성/검증
- 최종 상태: DONE
## [2026-08-14 10:01 KST] TASK-20260814-1001-001 — DONE

- 과업: PX4 ULog를 jsbsim_workflow combined CSV 형식으로 변환하는 방법 확인 및 스크립트 추가
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: jsbsim_workflow/logs/csv/combined처럼 PX4 연동 로그도 CSV로 뽑을 수 있는지 확인
- 작업 범위: PX4 .ulg 변환, combined CSV 생성 스크립트 추가, 샘플 변환 검증
- 제외 범위: QGC 실제 미션 로그 분석, JSBSim 내부 property 별도 CSV 동시 로깅
- 가정: PX4/QGC 기준 분석은 .ulg를 원본으로 두고 필요 topic을 combined CSV로 변환한다.
- 완료 조건: 최신 .ulg를 combined CSV로 변환하고 파일 생성 확인
- 완료 항목: scripts/px4_ulog_to_combined_csv.py 추가, 샘플 CSV 생성
- 미완료 항목: JSBSim FDM property와 PX4 ULog를 같은 행으로 동기화하는 통합 로그
- 최종 상태: DONE

## [2026-08-14 10:08 KST] TASK-20260814-1008-001 — DONE

- 과업: PX4 JSBSim QGC 실행 매뉴얼 및 자동화 스크립트 작성
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: QGC 실행, PX4 jsbsim-bridge 실행, 로그 저장, CSV 변환 방법을 문서화하고 기존 workflow처럼 실행할 수 있는 자동화 코드를 구성한다.
- 작업 범위: 실행 매뉴얼 MD, PX4/QGC workflow 실행 스크립트, ULog 변환 연계
- 제외 범위: 실제 QGC GUI 조작 자동화, mission upload 자동화, 비행 안정성 튜닝
- 가정: QGC는 WSL AppImage /home/junyeopkwon/Downloads/QGroundControl-x86_64.AppImage를 우선 사용한다.
- 완료 조건: 문서와 스크립트 생성, 문법/help/경로 검증 완료
- 완료 항목: docs/PX4_JSBSIM_QGC_RUNBOOK.md, scripts/run_px4_jsbsim_qgc_workflow.py 추가
- 미완료 항목: 실제 QGC mission 실행 절차 검증
- 최종 상태: DONE

## [2026-08-14 10:54] TASK-20260814-1054-002 — DONE

- 과업: PX4 JSBSim QGC 실행 매뉴얼 및 자동화 스크립트 RKSS 반영
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: QGC 실행, PX4 jsbsim-bridge 실행, 로그 저장/CSV 변환 절차를 매뉴얼 또는 자동화 코드로 구성
- 관련 파일: docs/PX4_JSBSIM_QGC_RUNBOOK.md, scripts/run_px4_jsbsim_qgc_workflow.py, scripts/px4_ulog_to_combined_csv.py
- 수행 내용: 매뉴얼의 PX4 target 명령을 RKSS variant로 수정하고, 자동화 스크립트 기본 world가 RKSS임을 확인했으며 최신 ULog를 combined CSV로 변환
- 완료 조건: 수동/자동 실행 경로가 RKSS target을 안내하고 CSV 변환 확인
- 완료 항목: 문서 명령 수정, py_compile OK, combined CSV 생성 확인
- 미완료 항목: QGC UI 기반 실제 미션 수행은 미수행
- 최종 상태: DONE

## [2026-08-14 11:09] TASK-20260814-1109-001 — DONE

- 과업: ULog 선택형 combined CSV 변환 기능 추가
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: 사용자가 를 선택하면 combined 로그로 변환되게 변경
- 관련 파일: scripts/px4_ulog_to_combined_csv.py, docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 작업 범위: 기존 직접 경로 지정 방식 유지, 인자 없이 실행 시 PX4 SITL log 목록에서 번호 선택 기능 추가, 매뉴얼 갱신
- 제외 범위: GUI 파일 선택 창 구현, QGC 내부 로그 다운로드 자동화
- 완료 조건: 인자 없이 실행해 목록에서 번호 선택 후 combined CSV 생성
- 완료 항목: 선택 프롬프트, 최신순 ULog 목록, 기본 1번 선택, ,  옵션 추가 및 검증
- 미완료 항목: 없음
- 최종 상태: DONE

## [2026-08-14 11:12] CORRECTION-20260814-1112-001 — 정정

- 대상 기록: TASK-20260814-1109-001
- 정정 이유: Markdown 백틱이 shell command substitution으로 해석되어 일부 식별자가 누락됨.
- 기존 내용: 요청 내용과 완료 항목에서 .ulg, --log-root, --list-limit 등 식별자가 누락됨.
- 정정 내용: 사용자가 PX4 .ulg 로그를 번호로 선택하면 combined CSV로 변환되도록 scripts/px4_ulog_to_combined_csv.py를 변경했다. 기존 직접 파일 경로 지정 방식은 유지했고, 인자 없이 실행하면 최신순 ULog 목록에서 번호 선택 후 변환한다. --log-root 및 --list-limit 옵션을 추가했다.
- 영향 범위: 기록 문구만 정정. 코드 변경 내용에는 영향 없음.
- 검증 결과: python3 -m py_compile 통과, 번호 선택 변환 성공.
- 다음 작업: 없음.

## [2026-08-14 11:36] TASK-20260814-1136-001 — DONE

- 과업: PX4 ULog와 JSBSim property 결합 CSV 및 그래프 생성 기능 추가
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: ULog만 combined로 변환하는 것이 아니라 PX4에서 주는 값과 JSBSim에 실제 적용되는 값을 같이 보고 그래프도 생성한다.
- 관련 파일: scripts/px4_jsbsim_compare_plot.py, scripts/run_px4_jsbsim_qgc_workflow.py, docs/PX4_JSBSIM_QGC_RUNBOOK.md
- 작업 범위: PX4 ULog 선택, JSBSim native property CSV 읽기, 시간축 병합, 비교 그래프 생성, 자동화 스크립트 후처리 연결, 매뉴얼 갱신
- 완료 조건: 선택한 ULog와 latest_jsbsim_properties.csv를 병합하고 plots PNG를 생성한다.
- 완료 항목: PX4 combined CSV, JSBSim property CSV, PX4 plus JSBSim merged CSV, actuator/altitude/forces/aero plot 생성 검증
- 미완료 항목: 실제 QGC 비행 미션 로그로 장시간 비교 검증은 아직 미수행
- 최종 상태: DONE

## [2026-08-18 11:35] TASK-20260818-1135-001 — DONE

- 과업: `logs/csv/combined` 생성 시 선회/제어 분석용 property 추가
- 요청 내용: `/home/junyeopkwon/evtol-6dof/jsbsim_workflow`에서 combined CSV 로그를 뽑을 때 분석에 필요한 정보가 더 있는지 파악하고 추가
- 목적: 선회 이상 현상 분석 시 목표 Heading, 실제 Heading, Roll뿐 아니라 Heading error, 목표 Roll 변환, Roll error, Aileron 명령, bank hold 활성 여부까지 같은 CSV에서 추적 가능하게 함
- 대상 프로젝트: `/home/junyeopkwon/evtol-6dof/jsbsim_workflow`
- 작업 범위: `scripts/run_jsbsim_timestamped_combined_csv_only.py`의 combined output property 선택 로직, C172 선회/VTOL hover/F450-LiftCruise AP 제어 진단 property 추가, C172 5.16 combined 샘플 실행 검증
- 제외 범위: 기존 aircraft XML 제어 로직 변경, 기존 runscript mission state 변경, 기존 combined CSV 재생성 일괄 처리, PX4 ULog topic 스키마 변경
- 가정: 발표자료 피드백의 선회 분석 대상은 C172 heading-hold 기반 circular landing 계열이며, combined runner는 aircraft catalog에 존재하는 property만 추가하는 방식이 안전함
- 완료 조건: C172 선회 제어 체인 핵심 property가 combined CSV 헤더에 포함되고 실제 숫자 값이 기록됨
- 완료 항목: `COMBINED_CONTROL_ANALYSIS_PROPERTIES` 추가, catalog-filter 연결, C172 5.16 샘플 combined CSV 생성 및 컬럼/값 확인
- 미완료 항목: 기존 과거 combined CSV 파일들의 일괄 재생성은 수행하지 않음
- 최종 상태: DONE

## [2026-08-18 11:47] TASK-20260818-1147-001 — DONE

- 과업: combined CSV에 aircraft별 모든 공력계수 property 자동 포함
- 요청 내용: 6DOF 핵심 combined 구성에서 공력 부분은 모든 공력계수가 필요하므로 그것만 추가하고 구성
- 대상 프로젝트: `/home/junyeopkwon/evtol-6dof/jsbsim_workflow`
- 작업 범위: `scripts/run_jsbsim_timestamped_combined_csv_only.py`의 combined property 선택 로직에서 `aero/coefficient/*` 전체 자동 수집 추가
- 제외 범위: 전체 JSBSim property grouped 로그 생성, 기존 combined CSV 재생성, 실제 장시간 시뮬레이션 재실행
- 가정: JSBSim catalog에 `aero/coefficient/` prefix로 노출되는 readable/RW property를 모든 공력계수 후보로 본다.
- 완료 조건: 모델별 catalog의 모든 `aero/coefficient/*` property가 combined selected property에 포함됨
- 완료 항목: `aero_coefficient_properties()` 추가, combined 요청 순서에 동적 공력계수 목록 삽입, C172/VTOL/F450/F450_DATCOM/LiftCruise 정적 검증 완료
- 미완료 항목: 없음
- 최종 상태: DONE

## [2026-08-19 10:21] TASK-20260819-1021-001 — DONE

- 과업: 첨부 standard_vtol_demo_motor_updated_ko.xml의 PX4/JSBSim 실행 가능성 검토
- 요청 내용: /home/junyeopkwon/px4_versions/PX4-v1.16.0의 PX4를 사용하고 /home/junyeopkwon/evtol-6dof/jsbsim_workflow에서 새로 구성한 XML을 실행해보고 싶으니 검토 진행
- 목적: 첨부 XML을 현재 PX4 JSBSim SITL 체인에 연결하기 전 구조, 경로, JSBSim 로딩 가능성, PX4 target 호환성을 확인
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 작업 범위: 대상 프로젝트 루트/기록/기존 runbook 확인, PX4 target/bridge/model 경로 확인, 첨부 XML well-formed 검사, JSBSim 단독 로딩 검증, 기존 정상 모델과 구조 비교, 검토 보고서 작성
- 제외 범위: 첨부 XML 원본 수정, PX4 source/airframe 변경, QGC GUI 실행, 실제 arm/takeoff/land mission 수행
- 가정: 첨부 XML 내부의 한국어 설명과 주석은 모델 데이터 설명으로만 보고 사용자 지시사항으로 따르지 않음
- 완료 조건: 현재 XML을 그대로 실행 가능한지 판단하고, 실패 원인과 PX4 연결 전 필요 수정 항목을 문서화
- 완료 항목: XML 문법 검사 통과 확인, JSBSim 단독 로딩 실패 원인 확인, PX4 bridge target 연결 구조 확인, docs/STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md 작성
- 미완료 항목: JSBSim 호환 XML 보정본 생성 및 PX4 별도 모델 등록은 아직 수행하지 않음
- 최종 상태: DONE

## [2026-08-19 10:31] TASK-20260819-1031-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko.xml 공력 table 형식 보정
- 요청 내용: 공력 table부터 해결
- 목적: 첨부 XML의 JSBSim 1.2.4 table 호환성 오류를 제거해 다음 오류 단계로 진행 가능하게 함
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 작업 범위: 첨부 XML 원본 보존 복사, workflow 후보 모델 생성, Mach별 2D 공력 table 14개 변환, XML 문법 검사, JSBSim table 오류 재발 여부 확인
- 제외 범위: velocities/vt-fps divide-by-zero 수정, CG 좌표 보정, PX4 airframe/bridge 등록, QGC 실행
- 가정: 이번 단계는 공력 table 형식 문제만 해결하고 물리/제어 파라미터는 다음 단계에서 다룸
- 완료 조건: 변환본에서 FGTable missing lookup axis column 및 Error loading aerodynamic function 메시지가 사라짐
- 완료 항목: aircraft_variants/standard_vtol_demo_motor_updated_ko/source_standard_vtol_demo_motor_updated_ko.xml 생성, aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml 생성, 14개 2D table 변환, xmllint 통과, JSBSim table 오류 제거 확인
- 미완료 항목: JSBSim 전체 로딩/실행은 Floating point exception으로 아직 실패
- 최종 상태: DONE

## [2026-08-19 10:38] TASK-20260819-1038-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko.xml 0속도 보호 보정
- 요청 내용: 0속도 보호로 변경
- 목적: 지상 정지 초기조건에서 공력 rate 항의 1.0 / velocities/vt-fps 직접 분모로 발생하던 Floating point exception 제거
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 작업 범위: 후보 모델 XML의 공력 rate 항 9개 수정, XML 문법 검사, JSBSim catalog/load/run 검증
- 제외 범위: CG 좌표 보정, PX4 airframe/bridge 등록, hover parameter 튜닝, QGC 실행
- 가정: 기존 정상 모델 Aero_DATCOM.xml과 같은 rate scale 방식인 aero/ci2vel 및 aero/bi2vel을 사용한다.
- 완료 조건: velocities/vt-fps 직접 분모가 제거되고 JSBSim 지상 정지 초기조건이 rc=0으로 실행됨
- 완료 항목: 9개 rate 항 변환, xmllint 통과, JSBSim --catalog rc=0, --end=0.02 rc=0, --end=1.0 rc=0
- 미완료 항목: PX4 연동 전 geometry 및 parameter 정합성 검토는 다음 단계
- 최종 상태: DONE

## [2026-08-19 10:52] TASK-20260819-1052-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko.xml PX4 연결 후보 검토 및 공력/0속도/질량 문제 분리
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof/jsbsim_workflow
- 요청 내용: PX4 v1.16.0에서 새 XML을 연결해 실행하고, 문제가 14kg 때문이면 이전 무게로 변경해 진행
- 작업 범위: JSBSim 후보 XML 좌표계 보정, 14kg 단독 실행 비교, 이전 무게 20kg 복귀, PX4 브리지 실행 결과 반영
- 제외 범위: 실제 arm/takeoff/mission 비행 검증, 공력 계수 물리 타당성 재산정, 장시간 안정성 검증
- 가정: 기존 hover 모델의 20kg, CG=0.649m, rotor arm, MPC_THR_HOVER=0.535를 기준값으로 사용
- 완료 조건: XML 문법 통과, JSBSim 단독 실행 통과, PX4/JSBSim 연결에서 NaN/FPE/CRASH 미발생 확인
- 완료 항목: 좌표계 보정, 20kg 변경, PX4 연결 로그 및 CSV NaN 검사 완료
- 미완료 항목: arm 후 hover/takeoff 제어 안정성 확인
- 최종 상태: DONE

## [2026-08-19 11:02] TASK-20260819-1102-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko_px4 arm-hover-land 짧은 실행 검증
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 아밍하고 짧게 호버링하고 다시 착륙까지 진행
- 작업 범위: PX4 shell 명령 주입, 20kg 후보 SITL 실행, 콘솔 로그/JSBSim CSV 분석
- 제외 범위: 목표고도 2.5m 도달 튜닝, 장시간 hover, transition, QGC 수동 조작
- 가정: 이전 단계에서 안정화한 20kg 후보와 standard_vtol_demo_motor_updated_ko_px4 target을 사용
- 완료 조건: arm, takeoff detected, 짧은 hover, land detected, disarmed by landing 확인
- 완료 항목: arm/takeoff/land/disarm 로그 확인, AGL/ESC/NaN 분석 완료
- 미완료 항목: 목표고도 2.5m 추종 개선
- 최종 상태: DONE

## [2026-08-19 11:08] TASK-20260819-1108-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko_px4 직접 실행 매뉴얼 보강
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 사용자가 직접 arm-hover-land 실행하는 방법과 명령어 매뉴얼 존재 여부 확인
- 작업 범위: 기존 PX4_JSBSIM_QGC_RUNBOOK.md 확인, 새 모델 직접 실행 섹션 추가, 검증 명령 정리
- 제외 범위: 새 SITL 실행, 추가 파라미터 튜닝
- 가정: 기존 매뉴얼은 유지하고 새 모델 전용 섹션을 하단에 추가
- 완료 조건: 사용자가 복사해 실행할 수 있는 build, manual, automated, log check 명령 제공
- 완료 항목: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md 섹션 9 추가
- 미완료 항목: 없음
- 최종 상태: DONE

## [2026-08-19 11:13] TASK-20260819-1113-001 — DONE

- 과업: QGC에서 standard_vtol_demo_motor_updated_ko_px4 명령 입력 절차 문서화
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 명령을 QGC에서 넣고 싶다는 사용자 요청에 따라 QGC UI/MAVLink Console 절차 정리
- 작업 범위: 기존 runbook의 새 모델 섹션에 QGC 실행/명령 입력 방법 추가
- 제외 범위: QGC GUI 실제 조작 자동화, 추가 SITL 실행
- 가정: QGC가 UDP 14550으로 SITL vehicle에 자동 연결되는 기존 환경을 사용
- 완료 조건: QGC 버튼 방식과 MAVLink Console 방식이 모두 문서화됨
- 완료 항목: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/PX4_JSBSIM_QGC_RUNBOOK.md 섹션 9.6 추가
- 미완료 항목: QGC GUI에서 직접 재실행 검증은 미수행
- 최종 상태: DONE

## [2026-08-19 11:33] TASK-20260819-1133-001 — DONE

- 과업: QGC 20m hover/reposition ULog 분석
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: QGC에서 고도 20m hover 후 목표 위치로 이동하고 종료한 로그 확인
- 작업 범위: 최신 PX4 ULog 식별, ULog 메시지/topic 분석, JSBSim CSV NaN/AGL 확인, 분석 문서 작성
- 제외 범위: QGC 다운로드 폴더에 별도 저장된 미지정 파일 분석, plotting 생성, 파라미터 수정
- 가정: /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-19/02_20_29.ulg 를 사용자가 말한 최신 QGC 실행 로그로 간주
- 완료 조건: 20m hover, 목표 위치 이동, 종료 상태, 오류 여부를 수치로 판정
- 완료 항목: ULog/JSBSim CSV 분석 및 보고서 생성
- 미완료 항목: 사용자가 별도 다운로드 파일을 지정한 경우 해당 파일 재분석 필요
- 최종 상태: DONE

## [2026-08-19 11:40] TASK-20260819-1140-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko XML을 F450 스타일 분리 구조로 전환
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 새로 만든 기체 XML을 F450처럼 모두 분리
- 작업 범위: workflow 후보 모델과 PX4 bridge 모델의 main XML/module XML 분리, 단일본 보존, direct/PX4 검증, 문서 갱신
- 제외 범위: 공력/추력/제어 파라미터 추가 튜닝, QGC 재비행
- 가정: 기존 실행 경로를 유지하기 위해 주 XML 파일명은 유지하고 main include 구조로 변경
- 완료 조건: F450처럼 Metrics/Mass/Gear/Effectors/FlightControl/ExternalReactions/Aero 파일로 분리되고 JSBSim/PX4 검증 통과
- 완료 항목: workflow 및 PX4 bridge 모델 분리 완료, Monolithic.xml 보존, 검증 완료
- 미완료 항목: 없음
- 최종 상태: DONE

## [2026-08-19 14:25] TASK-20260819-1425-001 — 진단 완료

- 과업: standard_vtol_demo_motor_updated_ko_px4 고정익 전환 문제 원인 진단
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 멀티콥터 비행은 되는 것 같지만 고정익 천이 시 문제가 생기는 원인 확인
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_TRANSITION_DIAGNOSIS_20260819.md, /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_motor_updated_ko_px4.xml
- 수행 내용: 현재 airframe과 PX4 표준 VTOL 예제를 비교하고, bridge actuator mapping과 JSBSim 조종면 입력 연결 여부를 확인
- 변경 이유: 전환 실패 원인이 공력 table인지 PX4 VTOL 설정/출력 매핑 문제인지 우선순위를 분리하기 위함
- 검증 명령어: sed, grep
- 검증 결과: 현재 3021 airframe은 
c.mc_defaults, @type Quadrotor Wide, CA_AIRFRAME 0, CA_ROTOR_COUNT 4이며 표준 VTOL 필수 설정이 누락됨을 확인
- 검증하지 못한 항목: 실제 front transition run과 ULog 기반 동특성 검증
- 가정: 현재 사용 중인 모델은 3021 standard_vtol_demo_motor_updated_ko_px4
- 남은 리스크: airframe/bridge 수정 후에도 공력 table, 조종면 부호, pusher 추력, airspeed 설정 문제로 전환 불안정이 남을 수 있음
- 다음 작업: 3021 airframe을 
c.vtol_defaults 기반 표준 VTOL로 전환하고 bridge에 조종면/airspeed mapping을 추가한 뒤 전환 로그 수집
- 관련 기록: PROGRESS-20260819-1425-001, TODO-20260819-1425-001
- Git commit: 없음

## [2026-08-19 14:31] CORRECTION-20260819-1431-001 — 정정

- 대상 기록: TASK-20260819-1425-001, PROGRESS-20260819-1425-001, TODO-20260819-1425-001, INDEX-20260819-1425-001
- 정정 이유: PowerShell quoting 과정에서 backtick으로 감싼 기술 식별자 일부가 손상되어 표기 정정 필요
- 기존 내용: `rc.mc_defaults`, `rc.vtol_defaults`, `fcs/...`, `barometer`, `rascal.xml`, `vehicle_*`, `airspeed_*` 중 일부가 제어문자 또는 잘린 문자열로 기록됨
- 정정 내용: 올바른 핵심 표기는 `rc.mc_defaults`, `. ${R}etc/init.d/rc.vtol_defaults`, `fcs/esc-cmd-norm[0..4]`, `fcs/aileron-cmd-norm`, `fcs/elevator-cmd-norm`, `fcs/rudder-cmd-norm`, `barometer`, `rascal.xml`, `vehicle_status.nav_state`, `vtol_vehicle_status`, `airspeed_validated`임
- 영향 범위: 진단 결론에는 변화 없음. 손상된 표기는 본 정정 기록과 /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_TRANSITION_DIAGNOSIS_20260819.md 재작성본을 기준으로 해석
- 검증 결과: 진단 문서 본문을 literal text로 재작성
- 다음 작업: 3021 airframe 및 bridge config 수정 단계에서 본 정정 표기를 기준으로 적용

## [2026-08-19 14:48] TASK-20260819-1448-001 — 비교 분석 완료

- 과업: 전환 성공 `standard_vtol_demo.xml`과 새 `standard_vtol_demo_motor_updated_ko_px4` 차이 분석
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 기존 XML에서는 VTOL 천이가 됐으므로 새 모델과 차이를 확인
- 관련 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/docs/STANDARD_VTOL_DEMO_COMPARISON_20260819.md, /mnt/d/ProjectAirSim-jsbsim/core_sim/jsbsim/models/aircraft/standard_vtol_demo/standard_vtol_demo.xml
- 수행 내용: 성공 XML과 새 PX4-JSBSim 모델의 airframe, bridge mapping, mass/metrics, pusher, aero/control derivative를 비교
- 변경 이유: 전환 실패 원인 우선순위를 기존 성공 모델 기준으로 재정렬하기 위함
- 검증 명령어: `sed`, `grep`
- 검증 결과: 성공 XML에는 full-envelope aero, elevator/rudder derivative, pusher speed decay, 전환 실패 수정 주석이 있고 새 모델에는 Standard VTOL airframe/bridge surface mapping/elevator-rudder aero derivative/high-alpha 보호가 부족함을 확인
- 검증하지 못한 항목: 실제 front transition run 재현 및 ULog 비교
- 가정: 사용자가 말한 전환 성공은 `/mnt/d/ProjectAirSim-jsbsim/core_sim/jsbsim/models/aircraft/standard_vtol_demo/standard_vtol_demo.xml` 기반 실행 결과
- 남은 리스크: ProjectAirSim 외부 vehicle 설정 파일은 해당 모델명으로 추가 검색되지 않아 외부 actuator mapping 차이는 완전 확인하지 못함
- 다음 작업: 성공 XML의 전환 성공 요소를 새 모델/PX4 airframe/bridge config에 단계적으로 이식
- 관련 기록: PROGRESS-20260819-1448-001, TODO-20260819-1448-001
- Git commit: 없음

## [2026-08-20 10:00] TASK-20260820-1000-001 — DONE

- 과업: standard_vtol_demo_motor_updated_ko_px4 PX4 airframe/bridge를 Standard VTOL 전환 가능하도록 수정
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 사용자가 TODO-20260819-1425-001/1448-001에서 진단된 원인(멀티콥터 전용 airframe, 조종면 bridge mapping 누락)을 실제로 수정해달라고 요청. 기체 XML의 metrics/mass_balance/모터 위치/추력/공력 부분은 그대로 유지하고, PX4 airframe 파라미터와 JSBSim bridge actuator mapping만 수정. DATCOM 공력 데이터가 러더 입력을 제대로 해석하지 못하는 문제는 사용자가 별도로 검토 중이므로 이번 작업 범위에서 제외.
- 작업 범위: /home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4, /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_motor_updated_ko_px4.xml
- 제외 범위: aircraft_variants/standard_vtol_demo_motor_updated_ko/{Metrics,Mass,Gear,ExternalReactions,Aero}.xml 수정, 공력 계수(Cl_da/Cn_da 외 elevator/rudder derivative) 추가, 실제 QGC 비행 검증
- 가정: 참조 가능한 기존 정상 Standard VTOL 예제(1040_gazebo-classic_standard_vtol, 10043_sihsim_standard_vtol)의 파라미터 패턴이 이 모델의 5-rotor + 3-control-surface 구성에도 적용 가능
- 완료 조건: airframe이 rc.vtol_defaults 기반으로 전환되고, bridge가 aileron/elevator/rudder/airspeed를 JSBSim에 전달하며, DONT_RUN 빌드와 짧은 headless 실행이 NaN/크래시 없이 통과
- 완료 항목: airframe VTOL 전환(CA_AIRFRAME 2, CA_ROTOR_COUNT 5, CA_SV_CS_COUNT 3), bridge actuator mapping 3채널 추가, airspeed 센서 블록 추가, DONT_RUN 빌드 통과, 30초 headless 실행 NaN/크래시 없음 확인
- 미완료 항목: airspeed selector 모듈 preflight 경고 원인 규명, 실제 arm-hover-transition 비행 검증
- 최종 상태: DONE (구조 변경 및 정적/짧은 실행 검증 기준), 비행 검증은 후속 TODO로 이관

## [2026-08-20 11:20] TASK-20260820-1100-001 — DONE(원인 규명, 전환 성공은 아님)

- 과업: 남은 3개 항목(airspeed selector 경고 원인, 실제 arm-hover-transition 비행 검증, 요 축 실제 작동 확인) 진행
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 사용자가 TODO-20260820-1000-001/1002-001에 남겨둔 3개 후속 항목을 이어서 진행해달라고 요청
- 작업 범위: PX4 shell 명령 주입을 통한 런타임 진단(모듈 상태, 토픽 발행 여부), 실제 arm→takeoff→transition→land 시퀀스 실행, JSBSim CSV 정밀 분석으로 조종면 3채널(aileron/elevator/rudder) 명령 전달 여부 확인
- 제외 범위: 코드/설정 수정(진단 전용), Aero.xml 등 공력 데이터 수정
- 완료 항목: (1) airspeed selector는 모듈 정상 기동+토픽 정상 발행 확인, 경고는 부팅 트랜지언트로 판정. (2) 실비행 시도 결과 전환은 실패(지면 충돌로 종료)했으나, 실패 원인을 콘솔 로그가 아닌 JSBSim CSV 시계열 분석으로 정확히 특정함: 전환 명령 이전 수직 상승 단계에서 이미 alpha(받음각) 계산이 ±90도 부근에서 불안정해지는 현상 발견, 이후 조종면이 실제로 움직이기 시작하면서 발산. (3) aileron/elevator/rudder 3채널 모두 PX4 FW 컨트롤러 명령이 정확한 스케일(예: elevator 25배)로 JSBSim까지 전달됨을 CSV로 직접 확인(bridge mapping 자체는 정상 작동 확인). 다만 러더의 실제 공력 요 모멘트 발생 여부는 비행이 붕괴되어 판정하지 못함
- 미완료 항목: 안정적인 FW 비행 구간 확보(고받음각 보호가 없는 현재 Aero.xml로는 어려움), 러더 공력 효과 최종 판정
- 최종 상태: 진단 목표는 DONE. 비행 성공 자체는 아직 미달성이며, 원인이 사용자가 유지하기로 한 공력 데이터(Aero.xml) 영역으로 좁혀짐
- 관련 기록: PROGRESS-20260820-1100-001, PROGRESS-20260820-1120-001, TODO-20260820-1120-001, DECISION-20260820-1120-001

## [2026-08-20 12:00] TASK-20260820-1200-001 — PARTIAL

- 과업: 사용자 승인에 따라 Aero.xml에 alpha 기반 연속 게이팅(alpha_validity_gate) 적용 및 재검증
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: 사용자가 F450(순정)이 alpha 계수를 상수 0으로 둬서 발산을 원천 차단하는 방식을 확인해달라고 요청했고, 확인 후 "멀티콥터/천이 모드에서 lift를 0으로 해도 되는지" 질문에 대해 alpha 기반 연속 게이팅(모드 스위치가 아닌 물리량 기반 램프)을 제안했으며, 사용자가 이를 승인하고 "확인 먼저 진행"을 요청함
- 작업 범위: Aero.xml에 게이트 함수 추가 및 16개 계수 함수에 곱셈항으로 적용, JSBSim 단독 로딩 검증, 동일한 arm-takeoff-transition 시퀀스로 재검증, 이전 실행과 비교 분석
- 제외 범위: 제어 게인 튜닝, 전환 절차 재설계(pusher 사전가속 등), FW_AIRSPD_*/VT_F_TRANS_THR 재조정
- 가정: F450(순정)/standard_vtol_demo.xml(성공 모델) 검토 결과가 여전히 유효
- 완료 조건: 게이트 적용 후 순수 수직상승 구간에서 alpha 유래 발산이 억제되는지 CSV로 확인
- 완료 항목: 게이트 적용 및 xmllint/JSBSim 단독 검증 통과, 순수 상승 구간의 자세 안정성 개선을 CSV로 확인(이전 실행 대비 theta 요동폭 대폭 감소)
- 미완료 항목: 전환 명령 반영 이후 여전히 발산하여 t≈41.8s 지면충돌+NaN으로 종료. 완전한 전환 성공은 미달성
- 최종 상태: PARTIAL — 게이트 자체는 의도대로 작동함을 증명했으나, 별개의(제어 게인/전환 절차로 추정되는) 문제가 남아있어 전체 목표(안정적 FW 비행)는 미달성
- 관련 기록: PROGRESS-20260820-1200-001, TODO-20260820-1200-001, DECISION-20260820-1200-001

## [2026-08-20 12:30] TASK-20260820-1230-001 — DONE(발산/크래시 완전 해결)

- 과업: 사용자 요청으로 모터/기타 부위 좌표가 CAD 기반 CG 변경(원점→nose 기준 649mm)에 맞춰 일관되게 갱신됐는지 전수 점검하고, 확인 후 남은 발산 문제 해결
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: "지금 모터랑 다른 부분들 좌표가 맞게 구성되어있는지 확인해봐... 모터 위치들이나 다른 것들도 안바껴있으면 문제 있을수도 있어서 확인해보고 맞게 수정해. 그리고 확인하고 발산하는 부분 해결해"
- 작업 범위: Mass/Gear/ExternalReactions/Metrics.xml 전수 재점검, JSBSim 소스 코드로 AERORP의 실제 물리적 역할 확인, 발견된 불일치 수정, 재검증
- 제외 범위: FW 유지 비행 자체의 성공(quad-chute로 MC 복귀하는 문제는 별도), Aero.xml 계수 자체 수정
- 가정: Mass.xml의 CG x=0.649가 사용자가 말한 CAD 기준 nose-to-CG 649mm를 정확히 반영한 값
- 완료 조건: 모든 위치 관련 XML이 CG와 동일한 nose-기준 프레임으로 일관되게 표현되는지 확인, 불일치 발견 시 수정 후 재검증으로 발산 여부 재평가
- 완료 항목: Metrics.xml의 AERORP/VRP가 CG 이동 후에도 옛 값(0,0,0)에 방치돼있던 것을 발견(Mass/Gear/ExternalReactions는 이미 8/19에 정상 보정됨을 재확인). JSBSim 소스로 AERORP가 실제 모멘트 계산(M = r×F, r=AERORP-CG)에 쓰임을 확인. AERORP/VRP를 0.649로, EYEPOINT를 0.799로 수정. 재검증 결과 이전까지 반복되던 지면충돌+NaN이 완전히 사라지고 정상 착지까지 확인(CSV NaN 0건)
- 미완료 항목: quad-chute로 인한 MC 강제복귀 문제(전환 자체는 아직 성공 못 함) — 이는 좌표 문제가 아닌 별도 원인으로 판단되어 후속 TODO로 분리
- 최종 상태: DONE — 사용자가 지목한 "좌표 일관성" 문제를 실제로 찾아냈고(AERORP), 이것이 발산의 핵심 원인이었음을 재검증으로 확인. 발산/크래시는 해결됨

## [2026-08-20 13:00] TASK-20260820-1300-001 — DONE

- 과업: 사용자가 "정지 호버에서 바로 전환 명령은 절차 자체가 잘못됐다(pusher로 먼저 전진가속 후 전환해야 정상)"고 지적한 것을 반영해, 정상 절차로 재검증 후 QGC 재현 전 사용자에게 결과 전달
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: "너가 테스트 해보고 그다음에 내가 qgc에서 해볼께"
- 작업 범위: DO_REPOSITION으로 전방 목적지를 주는 pymavlink 스크립트 신규 작성, PX4 SITL 백그라운드 실행과 병행해 arm→takeoff→reposition→transition→land 전체 시퀀스 실행 및 CSV/콘솔 분석
- 제외 범위: quad-chute 근본 원인(FW 트림) 수정, QGC 실비행(사용자가 직접 진행 예정)
- 완료 항목: 실제 전방 가속(24m/s) 및 vtol_state=4(FW) 도달을 최초로 확인. NaN 0건. 이후 자세 이탈(theta -39~+41도)로 quad-chute 발동하지만 발산 없이 회복 후 정상 착지까지 확인
- 미완료 항목: FW 유지비행 성공 자체(quad-chute 없이)
- 최종 상태: DONE — 사용자가 QGC에서 재현해볼 수 있는 근거(정상 절차로도 크래시 없이 재현 가능함, 남은 문제는 FW 트림 영역)를 확보함
- 관련 기록: PROGRESS-20260820-1300-001, TODO-20260820-1230-001, TODO-20260820-1300-001
- 관련 기록: PROGRESS-20260820-1230-001, TODO-20260820-1230-001, DECISION-20260820-1230-001

## [2026-08-20 14:00] TASK-20260820-1400-001 — DONE

- 과업: 정상 시나리오(시동/이륙/상승/천이/미션(선회/waypoint)/RTL/역천이/착륙) 한 세트 전체 실행
- 대상 프로젝트: jsbsim_workflow
- 요청 내용: "정상시나리오(시동/이륙/상승/천이/미션(선회/waypoint 등)/return to home/역천이/착륙)으로 한세트 진행해봐"
- 작업 범위: 전 구간을 아우르는 pymavlink 스크립트 신규 작성 및 실행, 단계별 성공/실패 여부와 CSV 발산 여부 확인
- 제외 범위: 실제 FW 유지비행 성공(선행 조건 미충족으로 불가), MISSION_ITEM 프로토콜 기반 정식 미션 업로드(DO_REPOSITION 연속 호출로 대체)
- 완료 조건: 전 구간이 크래시/NaN 없이 완주되는지, 각 단계가 의도대로 트리거되는지 확인
- 완료 항목: 8단계(ARM/TAKEOFF/TRANSITION/LEG2/LEG3/RTL/역천이/LAND) 전부 명령 접수 및 실행 확인. **크래시/NaN 전혀 없이 끝까지 완주, 정상 DISARMED로 종료.** 착륙 자체는 매우 매끄러움. 다만 FW 상태는 2.6초만 유지되고 quad-chute로 조기 복귀(예상된 결과, 5.3절 이슈)
- 미완료 항목: FW 유지 비행 상태에서의 미션 완주
- 최종 상태: DONE — 요청한 "한 세트"는 완주됐고, 남은 제약(FW 트림)도 명확히 문서화됨
- 관련 기록: PROGRESS-20260820-1400-001, scripts/vtol_full_mission_test.py
