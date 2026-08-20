# Decisions Log


## [2026-08-01 18:30] DECISION-20260801-1830-001 — ACCEPTED

- 문제: 현재 저장소의 models/aircraft, models/engine, models/systems 구조가 JSBSim 1.2.4의 --root 표준 aircraft, engine, systems 구조와 직접 맞지 않음
- 고려한 대안: 저장소 파일 이동, XML include 경로 변경, 임시 표준 루트에 심볼릭 링크 구성
- 최종 선택: /tmp/evtol-jsbsim-run-codex 아래에 심볼릭 링크 기반 표준 루트를 구성해 검증
- 선택 이유: 사용자/기존 작업 파일을 대량 이동하지 않고 실행 검증을 진행할 수 있음
- 영향 범위: 검증 실행 경로에만 영향, 저장소 구조 자체는 유지
- 장점: 최소 변경, 반복 실행 가능, 원본 XML을 그대로 참조
- 단점: 재현 명령이 길고, 별도 실행 스크립트가 없으면 사용자가 같은 루트를 다시 구성해야 함
- 검증 결과: JSBSim 1.2.4에서 두 runscript 로딩 및 실행 가능
- 남은 리스크: 장기적으로는 실행 스크립트 또는 JSBSim 표준 레이아웃과의 정합성 결정 필요

## [2026-08-20 17:20] DECISION-20260820-1720-001 — ACCEPTED

- 문제: 8월 이후 CSV 로그 중 100MB를 초과하는 파일이 있어 일반 Git으로 GitHub에 push할 수 없음
- 고려한 대안: 일반 Git에 직접 추가, CSV 압축 또는 분할, Git LFS 사용, 별도 archive만 유지
- 최종 선택: 8월 이후 CSV는 Git LFS로 추적하고 7월 CSV는 repo 밖 archive에 보관
- 선택 이유: 파일명과 경로는 Git으로 동기화하면서 대용량 blob은 LFS object로 분리할 수 있음
- 영향 범위: .gitattributes, .gitignore, jsbsim_workflow/.gitignore, jsbsim_workflow/logs/csv/**/*.csv
- 장점: Windows clone에서 CSV 경로를 유지하고 GitHub 일반 blob 100MB 제한을 피함
- 단점: Git LFS 설치와 GitHub LFS quota에 의존함
- 검증 결과: 가장 큰 CSV가 Git index에서 134 bytes LFS pointer로 staged됨
- 남은 리스크: WSL 환경에는 git-lfs가 설치되어 있지 않아 WSL에서 실제 LFS 파일을 받을 수 없음
- 기존 결정과의 관계: 2026-08-20 jsbsim_workflow 일반 폴더 편입 결정은 유지하고, logs/csv에 한해 LFS 추적 예외를 추가함
