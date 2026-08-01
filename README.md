# eVTOL 6DOF (JSBSim + PX4) 연구 프로젝트

## 이 프로젝트가 하는 일

JSBSim 기반 eVTOL 6DOF 비행동역학 모델을 만들고, PX4(SITL)와 jsbsim-bridge로 연동하는
석사 졸업논문 연구. 메인 담당 파트는 6DOF 비행동역학(JSBSim 모델링)이고,
GPT / Codex / Gemini 등 여러 AI 툴을 역할 분담해서 병행 작업한다.

## 폴더 구조
## AI 에이전트 역할 분배

| 역할 | 담당 | 이유 |
|---|---|---|
| 총괄 관리 | Claude Code | 태스크 관리, 파일 통합, 문서화 허브 |
| JSBSim XML 4종 (기체/FCS/IC/run script) | Codex | 스키마 반복작업 + 직접 실행/디버깅 가능 |
| eVTOL 모델 이론(공력/추진/천이 로직) | Gemini | 긴 컨텍스트로 선행연구 다수 종합 |
| 이론/수식 교차검증 | Codex/GPT 웹 | 2차 검증(second opinion) |
| jsbsim-bridge 연동 코드 | Codex | 소스 레벨 디버깅 필요 |
| 그래프/시각화 | Codex(처리) → Claude(정리) | |
| 문서화/PPT | Claude | |

역할별 세부 내용과 진행상태는 `docs/STATUS.md`에 계속 업데이트할 것.

## 작업 흐름 (핸드오프 방법)

1. 다른 툴로 작업하기 전에 `docs/STATUS.md`를 열어서 최신 상태 확인.
2. 그 툴 프롬프트 맨 앞에 STATUS.md 내용을 붙여넣어 맥락 전달.
3. 작업 끝나면 결과물을 해당 폴더에 저장하고 STATUS.md 갱신.
4. git commit 메시지에 `[codex]`, `[gemini]`, `[claude]` 처럼 태그.

## 주의: 좌표계/부호 규약

JSBSim(body axis)과 PX4(NED + FRD)의 좌표계 변환이 jsbsim-bridge에서 가장 실수가
잦은 지점. 반드시 `docs/coordinate_frame_checklist.md`로 체크할 것.
