# TODO Log


## [2026-08-01 18:30] TODO-20260801-1830-001 — OPEN

- 항목: scripts/QuadX_nominal_mission.xml 고도/착지 프로파일 재설계
- 배경: 현재 실행은 종료코드 0이나 최대 고도 약 243.8 ft, 최종 고도 약 30.5 ft로 10m급 호버/안정 착지 기대값을 만족하지 못함
- 권장 작업: 단순 open-loop 스로틀 이벤트를 더 세밀하게 조정하거나, 최소 고도 유지 제어를 FCS에 추가
- 관련 파일: scripts/QuadX_nominal_mission.xml, models/systems/QuadX_FCS.xml, docs/QuadX_Baseline_model.md
- 상태: OPEN

## [2026-08-01 18:30] TODO-20260801-1830-002 — OPEN

- 항목: JSBSim 1.2.4 실행 루트 구성 방식 고정
- 배경: JSBSim 1.2.4는 --aircraft-path, --engine-path, --systems-path 옵션을 지원하지 않고, 현재 저장소 구조는 표준 aircraft/engine/systems 루트와 다름
- 권장 작업: scripts/run_quadx_jsbsim.sh 같은 실행 헬퍼를 추가하거나 저장소 구조/문서 명령을 표준 루트 기준으로 정리
- 관련 파일: docs/QuadX_Baseline_model.md, scripts/QuadX_nominal_mission.xml, scripts/QuadX_control_response_test.xml
- 상태: OPEN

## [2026-08-20 16:10] TODO-20260820-1610-001 — OPEN

- 항목: D드라이브 clone에서 jsbsim_workflow 반영 확인
- 배경: jsbsim_workflow를 부모 repo에 편입한 뒤 Windows 로컬 경로 D:\\dev\\evtol-6dof에서 작업하려면 push 이후 pull이 필요
- 권장 작업: git push 성공 후 PowerShell에서 cd D:\\dev\\evtol-6dof; git pull; Test-Path .\jsbsim_workflow 실행
- 관련 파일: jsbsim_workflow/*, .gitignore
- 상태: OPEN
