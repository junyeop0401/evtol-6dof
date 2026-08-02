# 로컬 에이전트 오케스트레이션

Codex CLI(`codex exec`)와 Gemini CLI(`gemini -p`)를, 이미 로그인된 구독 세션
그대로 순서대로 호출하는 로컬 자동화다. 새 API 키는 쓰지 않는다 — 이미
결제 중인 ChatGPT/Codex, Google 계정 구독 한도 안에서만 돈다.

## 왜 이렇게 만들었나

- API 키 기반 오케스트레이터(OpenAI/Google API를 서버나 Cowork에 붙이는 방식)
  대신 이 방식을 고른 이유: 새 자격증명이 없어서 유출 리스크가 없고, 종량제
  과금이 아니라 이미 내고 있는 구독 한도 안에서만 쓰이므로 예상 못한 청구가
  안 생긴다. 서버 운영/보안 관리도 필요 없다.
- Codex는 5시간 롤링 한도 + 주간 한도가 같이 걸려 있어서, 스크립트가 잘못
  돌면 한 번에 주간 한도를 다 써버릴 수 있다. 그래서 하루 호출 상한을 코드에
  박아 두고(`usage_log.jsonl` 기준 카운트) 넘으면 자동으로 멈춘다.
- git add/commit/push, 파일 삭제처럼 되돌리기 어려운 작업은 이 스크립트가
  절대 대신하지 않는다. 항상 사람이 마지막 확인을 한다.
- cron 등록은 아직 하지 않는다. 여러 번 손으로 돌려보고 `usage_log.jsonl`,
  `run_logs/`를 검토해 신뢰가 쌓인 뒤에만 고려할 것.

## 자동화 범위 — 딱 두 단계만

- `research`: Gemini로 개념설계/문헌조사(4-에이전트 구조의 Gemini 역할)
- `execute`: Codex로 harness 실행 + 실행 중 발견되는 런타임 버그 1차 수정
  (4-에이전트 구조의 Codex 역할)

**"XML 1차 작성"과 "독립 정적검증"은 일부러 자동화하지 않았다.** 이 두 단계는
Claude(Cowork 세션)가 지금까지 쌓인 맥락(좌표계 규약, 손계산, 이전 실패 사례)을
들고 있는 상태에서 직접 하는 게 훨씬 정확하고, codex exec로 매번 그 맥락을
새로 먹이는 것보다 안전하다. GPT 교차검증도 API/CLI가 없어 여전히 수동
(복붙) 핸드오프다 — `docs/gpt_crosscheck_template.md` 참고.

## 사용 전 확인 (반드시 먼저 손으로 실행)

```bash
codex exec "echo hello"
gemini -p "hello"
```

둘 다 새 로그인 창 없이 바로 답이 나오면 준비된 것이다. 로그인을 다시
요구하면 `codex login` / `gemini` 로그인부터 먼저 끝낼 것.

## 사용법

```bash
# 개념설계 조사 (Gemini)
python3 automation/run_agent_pipeline.py \
  --stage research \
  --prompt-file automation/prompts/example_research.txt

# JSBSim 실행 (Codex)
python3 automation/run_agent_pipeline.py \
  --stage execute \
  --prompt-file automation/prompts/example_execute.txt \
  --cwd ~/jsbsim_workflow
```

프롬프트는 매번 `automation/prompts/`에 새 파일로 만들어서 넘긴다
(`example_research.txt`, `example_execute.txt`가 템플릿). 결과는 화면 출력과
함께 `automation/run_logs/<타임스탬프>_<tool>.log`에 프롬프트/stdout/stderr가
전부 남는다.

## 호출 상한 조정

기본값은 하루 Codex 8회, Gemini 20회다. 필요하면:

```bash
python3 automation/run_agent_pipeline.py --stage execute \
  --prompt-file automation/prompts/example_execute.txt \
  --max-codex-calls-per-day 3
```

실제 Codex 잔여 한도는 스크립트가 알 수 없으므로(구독사 쪽 값), ChatGPT
Settings > Usage 또는 Codex CLI 안에서 `/status`로 직접 확인하는 습관을
같이 가져갈 것.

## 다음 단계 (아직 안 함)

- [x] `codex exec`, `gemini -p` 둘 다 헤드리스 동작 확인(2026-08-02)
- [ ] Gemini API 키가 결제 계정에 연결돼 있는지 확인(위 참고)
- [ ] `git status`로 `jsbsim_workflow`가 실수로 이미 add되지 않았는지 확인
- [ ] `automation/run_agent_pipeline.py --stage research ...`로 실제 파이프라인
      1회 시험 실행, `usage_log.jsonl`/`run_logs/` 품질 확인
- [ ] 신뢰가 쌓이면 그때 cron 여부 재논의(지금은 보류)

## 확인 결과 (2026-08-02)

- `codex exec "echo hello"` — 성공. 기존 로그인 세션(구독) 그대로 재사용됨,
  새 로그인 불필요. 참고로 `echo hello`처럼 사소한 작업도 토큰 3,621개를
  씀 — 매 호출에 세션/모델 오버헤드가 붙으므로 하루 호출 상한을 낮게
  잡아둔 게 유효함을 확인.
  - 무해한 경고 2건 확인됨(둘 다 실행을 막지 않음):
    1. `failed to load models cache: missing field supports_reasoning_summaries`
       — 모델 캐시 파싱 경고, 무시 가능.
    2. `Codex could not find bubblewrap on PATH` — bubblewrap이 없어 번들된
       것으로 대체 실행됨. 실제 샌드박스 격리 품질에 영향을 주므로,
       `sudo apt-get install bubblewrap`로 설치해 두는 걸 권장(필수는 아님).
- `gemini -p "hello"` — 처음엔 "not running in a trusted directory" 오류로 실패.
  대화형 세션에서 `/permissions trust`로 현재 디렉토리(`~/evtol-6dof/jsbsim_workflow`,
  `~/jsbsim_workflow` 심볼릭 링크의 실제 경로)를 신뢰 등록한 뒤 **해결됨** —
  이후 `gemini -p "hello"` 헤드리스 호출 성공 확인(2026-08-02).
  - 부가 경고: "Ripgrep is not available. Falling back to GrepTool" — 성능
    저하만 있고 동작은 함. 필요하면 `sudo apt-get install ripgrep`로 설치
    가능(선택사항).
  - **미해결 확인 필요**: 시작 화면에 "Authenticated with gemini-api-key"로
    떠서, Google 계정 OAuth(무료 개인 티어)가 아니라 API 키 인증으로
    보임. 이 키가 결제 계정이 연결된 프로젝트 소속이면 종량제 과금 위험이
    있으므로, https://aistudio.google.com/apikey 에서 결제 연결 여부를
    사용자가 직접 확인해야 함. 결제가 붙어 있다면 OAuth 로그인 방식으로
    전환을 검토할 것.

### 원인이었던 경로 문제

`jsbsim_workflow`가 (복사가 아니라) `~/evtol-6dof/jsbsim_workflow`로 통째로
이동되어 있었음. harness의 `ROOT` 상수와, JSBSim 실행 시 출력 경로를
`../jsbsim_workflow/...` 상대경로로 만드는 로직이 `~/jsbsim`과 `jsbsim_workflow`가
형제 디렉토리라는 걸 전제하므로, `ln -s ~/evtol-6dof/jsbsim_workflow ~/jsbsim_workflow`
심볼릭 링크로 복구함(2026-08-02, 사용자가 직접 실행·확인). 최상위 `evtol-6dof/.gitignore`에
`jsbsim_workflow/`를 추가해 git 추적에서는 계속 제외.
