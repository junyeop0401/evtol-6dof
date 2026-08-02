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
