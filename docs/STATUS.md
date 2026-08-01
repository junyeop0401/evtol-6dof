# STATUS.md — 핸드오프 로그

다른 AI 툴로 넘어가기 전/후에 항상 이 파일을 갱신할 것.
새 툴 프롬프트 맨 앞에 아래 "현재 상태" 섹션을 붙여넣어 맥락을 이어줄 것.

---

## 현재 상태

- 연구 주제: JSBSim + PX4 기반 eVTOL 6DOF 비행동역학 시뮬레이션 (석사 졸업논문)
- 담당 파트: 6DOF 비행동역학 (JSBSim 모델링)
- 연구 주제 세부 확정 전 단계. 기체 형상(틸트로터 / 멀티로터+날개 등) 미확정.
- 프로젝트 스켈레톤 생성 완료 (모델 xml은 전부 템플릿 상태, 실제 파라미터 없음)

## 최근 결정사항

- JSBSim 기준 4대 산출물: 기체 xml, FCS(비행제어) xml, 초기조건(IC) xml, run script xml
- PX4 연동은 jsbsim-bridge 사용, state/control 값 매핑이 핵심 작업
- 좌표계: JSBSim body axis ↔ PX4 NED/FRD 변환 지점을 최우선 검증 대상으로 지정

## 미해결 이슈

- [ ] eVTOL 기체 형상 확정 (틸트로터 vs 멀티로터+고정익 vs 리프트+크루즈 등)
- [ ] 공력계수/추력모델 출처(문헌 or 자체 CFD/풍동) 미정
- [ ] jsbsim-bridge에서 실제 사용하는 메시지 필드 확인 필요
- [ ] 좌표계 변환식 검증 전 (docs/coordinate_frame_checklist.md 참고)

## 다음 작업

1. eVTOL 기체 형상/개념설계 확정 (Gemini로 유사 연구 조사)
2. models/aircraft/eVTOL_template.xml 채우기 (Codex)
3. jsbsim-bridge 소스 코드 확인해서 bridge/README.md 필드 매핑 구체화 (Codex)

---

## 로그 (최신이 위로)

### 초기 세팅 — Claude
- 프로젝트 스켈레톤 생성 (폴더 구조, xml 템플릿, 체크리스트, README)
- Codex/Gemini/Claude Code 3개 CLI 설치 및 인증 완료
