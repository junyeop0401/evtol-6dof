# Progress Log


## [2026-08-01 18:30] PROGRESS-20260801-1830-001 — PARTIAL

- 과업: QuadX_Baseline JSBSim 실행 검증
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof
- 조사한 파일: README.md, docs/STATUS.md, docs/coordinate_frame_checklist.md, docs/QuadX_Baseline_model.md, models/aircraft/QuadX_Baseline.xml, models/systems/QuadX_FCS.xml, models/engine/QuadX_Motor.xml, models/engine/QuadX_Prop.xml, init/QuadX_ground.xml, init/QuadX_hover.xml, scripts/QuadX_nominal_mission.xml, scripts/QuadX_control_response_test.xml
- 생성한 파일: docs/agent-log/INDEX.md, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/DECISIONS.md, docs/agent-log/TODO.md
- 수정한 파일: init/QuadX_ground.xml, init/QuadX_hover.xml, scripts/QuadX_nominal_mission.xml, docs/STATUS.md, docs/QuadX_Baseline_model.md, docs/coordinate_frame_checklist.md
- 핵심 변경점: 초기조건 속도 단위를 JSBSim 1.2.4 호환 단위로 변경, altitude를 AGL 기준으로 정정, 정상 미션 이벤트에 시간 게이트 추가, 정상 미션 스로틀/플레어 1차 튜닝
- 실행한 명령어: JSBSim --version, JSBSim --help, JSBSim --root=/tmp/evtol-jsbsim-run-codex --script=/home/junyeopkwon/evtol-6dof/scripts/QuadX_nominal_mission.xml --nohighlight, JSBSim --root=/tmp/evtol-jsbsim-run-codex --script=/home/junyeopkwon/evtol-6dof/scripts/QuadX_control_response_test.xml --nohighlight
- 테스트 결과: control_response_test 종료코드 0, CSV 2001행 생성, 양의 roll/pitch/yaw 입력에 양의 p/q/r 응답 확인
- build 결과: 해당 없음
- 실행 확인 결과: nominal_mission 종료코드 0, CSV 1801행 생성, propeller-rpm 및 power-hp 기록 확인
- 검증하지 못한 항목: nominal_mission 10m급 호버/착지 체크리스트 통과
- 검증하지 못한 이유: 현재 open-loop 스로틀 프로파일이 최대 고도 약 243.8 ft, 최종 고도 약 30.5 ft로 기대값을 만족하지 못함
- 남은 리스크: JSBSim 1.2.4 표준 루트 구조와 현재 저장소 models/ 구조 불일치, 정상 미션 고도 제어 부재, 착지 이벤트 튜닝 미완료
- 후속 작업: 실행 스크립트 또는 표준 루트 배치 결정, nominal_mission에 고도 제어 또는 더 정교한 스로틀 프로파일 추가
- Git commit: 없음
