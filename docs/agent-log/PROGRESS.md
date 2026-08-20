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

## [2026-08-03] PROGRESS-20260803-XXXX-001 — PARTIAL

- 과업: "mini palcon" 모델 검토 + jsbsim_workflow/script 폴더 생성
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof, 검토 대상 실체 /home/junyeopkwon/jsbsim
- 조사한 파일: /home/junyeopkwon/jsbsim/docs/agent-log/PROGRESS.md·TODO.md(2026-08-03 항목), aircraft/MiniTalon/{MiniTalon.xml,Metrics.xml,Mass.xml,Propulsion.xml,Gear.xml,Aero.xml,FlightControl.xml,Effectors.xml,MiniTalonAP.xml,initAir.xml,README.md,ASSUMPTIONS.md}, engine/MiniTalon_Cobra_C2221_16_940KV.xml, engine/MiniTalon_APC_9x7.xml, output/MiniTalon_output.xml, scripts/MiniTalon_smoke_test_run.xml·MiniTalon_trim_test_run.xml, evtol-6dof/reference/docs/lessons_learned.md
- 생성한 파일: jsbsim_workflow/scripts/MiniTalon/initial_condition/README.md, jsbsim_workflow/scripts/MiniTalon/runscript/README.md(둘 다 폴더 자리표시자, 실제 XML 없음)
- 수정한 파일: docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md(이 기록), docs/STATUS.md
- 핵심 발견:
  1. "mini palcon"은 오늘 Codex가 만든 "MiniTalon"(X-UAV Mini Talon) 부트스트랩 모델로 확인(저장소 전체에 palcon/falcon 문자열 없음, 시간 일치)
  2. 문서화 품질 높음(SOURCE/DERIVED/ASSUMPTION/LIMITATION 표, ASSUMPTIONS.md), fdm_config version="2.0" 정상, qbar-area(모멘트는 qbar-area-bw/cbarw) 곱셈 전 축에 정상 적용, airborne init altitude 250M을 AGL로 올바르게 사용
  3. 원 저자가 이미 발견해 TODO로 남긴 것: longitudinal trim(do_simple_trim=0) 미수렴(udot/wdot/qdot), CAD mass/AVL aero 미반영, 추진계 실장 propeller 미확정, 조종면 실물 부호 미검증
  4. 이번 검토에서 새로 발견한 것(원 저자 TODO에 없음): engine/MiniTalon_Cobra_C2221_16_940KV.xml이 `<brushless_dc_motor>` 타입을 사용하는데, 이 프로젝트의 reference/docs/lessons_learned.md 6절이 바로 이 컴포넌트의 "failed to tie property" 버그(JSBSim GitHub Discussion #1183)를 이유로 QuadX_Baseline에서 electric_engine으로 대체하도록 명시함. smoke test는 exit 0에 CSV bad(NaN/Inf) 0건으로 통과했으나, 이 통과 기준은 propeller-rpm/power-hp/thrust-lbs가 "0이 아닌 값"인지까지는 확인하지 못함 — 이 프로젝트에 이미 있었던 F450AP "종료코드는 정상인데 실제로는 한 번도 이륙 안 함" 조용한 실패 사례와 같은 패턴의 위험
- 손계산 대조: Aero.xml 계수로 vt=34.989kt(≈18m/s), 1.7kg/0.3m² 기준 trim CL≈0.288 → 필요 alpha≈0.4deg, 이때 필요 ruddervator-sym≈0.7deg로 기하학적으로는 무리 없어 보임 — trim 미수렴 원인은 계수 자체의 오류라기보다 추력-항력 균형, do_simple_trim의 유한차분 자코비안과 성긴 테이블 구간의 상호작용 등 실행 기반 원인일 가능성이 높다고 판단(실행 불가 환경이라 확정 못함)
- 실행한 명령어: 없음(이번 세션도 bash 도구가 UNC 마운트 버그로 차단됨, Read/Glob/Grep만 사용)
- 테스트 결과: 해당 없음(정적 검토만 수행)
- 검증하지 못한 항목: trim 미수렴의 정확한 원인, brushless_dc_motor property tie 실제 성공 여부(수치 확인 없이 파일 구조만 대조)
- 검증하지 못한 이유: 이번 세션도 JSBSim 실행 불가 환경
- 남은 리스크: 위 "핵심 발견" 3, 4번 그대로
- 후속 작업: (1) engine XML을 electric_engine으로 교체할지 또는 brushless_dc_motor 유지 근거를 명시할지 사용자/Codex 결정, (2) MiniTalon_smoke_test.csv를 열어 propeller-rpm/power-hp/thrust-lbs 실제 수치가 0이 아닌지 직접 확인, (3) trim 재시도 시 CG/Cm0/Cmde/thrust line을 함께 조정(TODO-20260803-1528-003), (4) 위 사항이 정리된 뒤 jsbsim_workflow/scripts/MiniTalon/{initial_condition,runscript}에 실제 XML 작성
- Git commit: 없음

## [2026-08-20 16:10] PROGRESS-20260820-1610-001 — DONE

- 과업: jsbsim_workflow 부모 Git 저장소 편입
- 대상 프로젝트: /home/junyeopkwon/evtol-6dof
- 조사한 파일: .gitignore, jsbsim_workflow/.gitignore, docs/agent-log/INDEX.md, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/TODO.md
- 생성한 파일: 없음
- 수정한 파일: .gitignore, docs/agent-log/INDEX.md, docs/agent-log/TASK.md, docs/agent-log/PROGRESS.md, docs/agent-log/TODO.md
- 추가 예정 파일: jsbsim_workflow 내부 repo가 추적하던 소스/문서 173개
- 핵심 변경점: jsbsim_workflow/.git을 /home/junyeopkwon/jsbsim_workflow_git_backup_20260820_160500으로 이동 백업하고, 부모 repo에서 jsbsim_workflow 파일들을 추적하도록 stage함
- 실행한 명령어: git -C jsbsim_workflow status --short --branch, git -C jsbsim_workflow ls-files, git add -f, git diff --cached --name-only, git diff --cached --stat
- 테스트 결과: 해당 없음
- lint 결과: 해당 없음
- type check 결과: 해당 없음
- build 결과: 해당 없음
- 실행 확인 결과: staged 파일 174개 중 jsbsim_workflow 경로 173개 확인, jsbsim_workflow/logs/ 및 jsbsim_workflow/jsbsim_workflow_data/ staged 항목 없음 확인
- 검증하지 못한 항목: D드라이브 clone 반영 여부
- 검증하지 못한 이유: commit/push 후 Windows clone에서 git pull이 필요
- 남은 리스크: 기존 내부 repo의 commit 이력은 백업에만 남고 부모 repo에는 파일 스냅샷으로 편입됨
- 후속 작업: commit/push 후 D:\\dev\\evtol-6dof에서 git pull 실행
- Git commit: 예정
