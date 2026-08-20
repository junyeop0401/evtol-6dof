# Agent Log Index


## [2026-08-01 18:30] INDEX-20260801-1830-001 — PARTIAL

- 프로젝트명: evtol-6dof
- 기록 시각: 2026-08-01 18:30 KST
- 최근 수행 과업: Codex 배정 작업 확인 후 QuadX_Baseline JSBSim 1.2.4 실행 검증
- 현재 상태: control_response_test는 축별 부호 검증 통과, nominal_mission은 실행되지만 고도/착지 체크리스트 미통과
- 최근 변경 파일: init/QuadX_ground.xml, init/QuadX_hover.xml, scripts/QuadX_nominal_mission.xml, docs/STATUS.md, docs/QuadX_Baseline_model.md, docs/coordinate_frame_checklist.md, docs/agent-log/*
- 주요 결정: 저장소 구조를 이동하지 않고 /tmp/evtol-jsbsim-run-codex 심볼릭 링크 루트로 JSBSim 1.2.4 검증 수행
- 미완료 TODO: nominal_mission 고도/착지 프로파일 재설계, JSBSim 실행 루트 구성 방식 고정
- 남은 리스크: open-loop 정상 미션은 고도 안정성이 부족하고, 현재 문서의 실행 명령은 JSBSim 1.2.4와 완전히 일치하지 않음
- 권장 다음 작업: nominal_mission을 고도 제어 포함 형태로 개정하고 재검증

## [2026-08-20 16:10] INDEX-20260820-1610-001 — DONE

- 프로젝트명: evtol-6dof
- 기록 시각: 2026-08-20 16:10 KST
- 최근 수행 과업: jsbsim_workflow를 부모 Git 저장소에 일반 폴더로 편입하고 GitHub push 준비
- 현재 상태: jsbsim_workflow 소스/문서 173개와 최상위 .gitignore 변경이 staged 상태
- 최근 변경 파일: .gitignore, jsbsim_workflow/*, docs/agent-log/*
- 주요 결정: jsbsim_workflow를 submodule이 아니라 evtol-6dof의 일반 추적 폴더로 포함하고, logs/ 및 jsbsim_workflow_data/는 제외
- 미완료 TODO: D:\\dev\\evtol-6dof clone에서 git pull 후 폴더 반영 확인
- 남은 리스크: 내부 repo .git 메타데이터는 /home/junyeopkwon/jsbsim_workflow_git_backup_20260820_160500에 백업되어 있으며, 별도 repo 이력은 부모 Git 이력에 병합되지 않음
- 권장 다음 작업: commit/push 후 Windows D드라이브 clone에서 git pull 실행

## [2026-08-20 16:55] INDEX-20260820-1655-001 — DONE

- 프로젝트명: evtol-6dof
- 기록 시각: 2026-08-20 16:55 KST
- 최근 수행 과업: jsbsim_workflow 부모 repo 편입 commit 및 GitHub push 완료
- 현재 상태: origin/main에 commit 0530bb6까지 push 완료
- 최근 변경 파일: .gitignore, jsbsim_workflow/*, docs/agent-log/*
- 주요 결정: jsbsim_workflow는 submodule이 아닌 일반 폴더로 관리하고 대용량 logs/ 및 jsbsim_workflow_data/는 제외
- 미완료 TODO: Windows D드라이브 clone에서 git pull 실행 필요
- 남은 리스크: 기존 내부 repo 이력은 /home/junyeopkwon/jsbsim_workflow_git_backup_20260820_160500 백업에만 보존됨
- 권장 다음 작업: D:\\dev\\evtol-6dof에서 git pull 후 jsbsim_workflow 존재 확인

## [2026-08-20 17:20] INDEX-20260820-1720-001 — IN_PROGRESS

- 프로젝트명: evtol-6dof
- 기록 시각: 2026-08-20 17:20 KST
- 최근 수행 과업: jsbsim_workflow CSV 로그를 날짜 기준으로 정리하고 8월 이후 로그를 Git LFS 추적 대상으로 추가
- 현재 상태: D:\dev\evtol-6dof에서 8월 이후 CSV 47개가 Git LFS pointer로 staged됨
- 최근 변경 파일: .gitattributes, .gitignore, jsbsim_workflow/.gitignore, jsbsim_workflow/logs/csv/**/*.csv, docs/agent-log/*
- 주요 결정: 7월 CSV는 repo 밖 archive에 보관하고, 8월 이후 CSV는 Git LFS로 관리
- 미완료 TODO: GitHub LFS push 성공 여부 최종 확인
- 남은 리스크: GitHub LFS quota 또는 bandwidth 제한이 있으면 push가 실패할 수 있음
- 권장 다음 작업: push 성공 후 origin/main과 D드라이브 clone 상태 확인

## [2026-08-20 17:35] INDEX-20260820-1735-001 — DONE

- 프로젝트명: evtol-6dof
- 기록 시각: 2026-08-20 17:35 KST
- 최근 수행 과업: 8월 이후 CSV 로그 Git LFS push 완료
- 현재 상태: origin/main에 commit 5cff978까지 push 완료, D드라이브 clone은 main...origin/main 상태
- 최근 변경 파일: .gitattributes, .gitignore, jsbsim_workflow/.gitignore, jsbsim_workflow/logs/csv/**/*.csv, docs/agent-log/*
- 주요 결정: CSV 로그는 Git LFS로 연결하고, 7월 CSV는 D:\dev\evtol-6dof_log_archive\jsbsim_workflow_csv_pre_2026_08에 보관
- 미완료 TODO: Windows가 아닌 WSL repo에서 실제 LFS CSV를 받아야 하면 WSL git-lfs 설치 필요
- 남은 리스크: Git LFS를 사용하지 않는 환경에서는 CSV가 pointer로만 체크아웃될 수 있음
- 권장 다음 작업: Claude/Codex는 D:\dev\evtol-6dof에서 작업하고, 새 CSV도 같은 LFS 패턴으로 관리
