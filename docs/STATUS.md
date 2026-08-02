# STATUS.md — 핸드오프 로그

다른 AI 툴로 넘어가기 전/후에 항상 이 파일을 갱신할 것.
새 툴 프롬프트 맨 앞에 아래 "현재 상태" 섹션을 붙여넣어 맥락을 이어줄 것.

---

## 현재 상태

- 연구 주제: JSBSim + PX4 기반 eVTOL 6DOF 비행동역학 시뮬레이션 (석사 졸업논문)
- 담당 파트: 6DOF 비행동역학 (JSBSim 모델링)
- 논문 본체 기체 형상은 **틸트로터**로 방향을 잡음(확정 아님, 개념설계 전 단계).
  `models/aircraft/eVTOL_template.xml`이 실제 목표 기체이며, LiftCruise2kg/ADS 계열은
  별도 과제("과제")용이지 논문 본체가 아님 — 혼동하지 말 것.
- evtol-6dof가 에이전트(Claude/Cowork) 기반 작업의 1차 저장소로 확정됨. GitHub
  `junyeop0401/evtol-6dof`에 연동 완료(2026-08-01, main 브랜치 push 확인).
- 이전 약 6주간(06-15~07-31) Codex 중심으로 진행된 별도 작업 이력인
  `jsbsim_workflow/`를 사용자가 evtol-6dof 안으로 직접 복사해 넣었고, 그중 재사용
  가치가 높은 자산만 골라 `reference/`로 부분 병합 완료(harness 스크립트, LiftCruise2kg
  기체 정의, F450/LiftCruise2kg 미션 스크립트, 지구모델 XML, 비교 문서, 교훈 정리
  — `reference/docs/lessons_learned.md` 참고). `jsbsim_workflow/` 원본 폴더 자체는
  과거 이력 참고용으로만 로컬에 남기고 GitHub에는 올리지 않을 예정(아래 다음 작업 참고).
- QuadX_Baseline(순수 쿼드콥터 파이프라인 검증용)은 Codex 실행 검증까지 완료, 고도홀드
  폐루프 재검증만 남음(아래 미해결 이슈 참고).
- 프로젝트 스켈레톤 생성 완료 (eVTOL_template.xml 등은 여전히 템플릿 상태, 실제 파라미터 없음)

## 최근 결정사항

- JSBSim 기준 4대 산출물: 기체 xml, FCS(비행제어) xml, 초기조건(IC) xml, run script xml
- PX4 연동은 jsbsim-bridge 사용, state/control 값 매핑이 핵심 작업
- 좌표계: JSBSim body axis ↔ PX4 NED/FRD 변환 지점을 최우선 검증 대상으로 지정
- 논문 본체 = 틸트로터, LiftCruise2kg/ADS = 별도 과제. 향후 모든 응답/설계에서 이 구분을
  유지할 것(사용자가 명시적으로 정정한 사항, 2026-08-01).
- evtol-6dof를 1차 저장소로, jsbsim_workflow는 과거 이력 참고 자료로만 취급.
- 4-에이전트 역할분배 확정: Gemini(문헌조사/개념설계 근거), Claude(오케스트레이션/
  XML 1차 작성/독립 정적검증/CSV 정량분석/문서화), Codex(WSL에서 JSBSim 1.2.4 실제
  실행), GPT(교차검증 — 고위험 산출물에 한해 Claude 작업을 완전히 다른 모델 계열로
  재검토). GPT는 API/MCP 연결이 없어 수동 핸드오프(복붙) 방식이며, 요청 템플릿은
  `docs/gpt_crosscheck_template.md` 참고. 매 산출물마다 쓰지 않고 Claude가 "고위험"
  으로 판단한 항목(최종 개념설계, 최종 손계산, 논문에 실릴 CSV 판정)에만 사용.
- XML 작성 분업 원칙: 기체 정의(기체.xml+서브파일 세트)는 파일 간 상호의존성이
  커서 변형 1개당 한 세션이 한 번에 작성한다(병렬 분할 금지). IC/런스크립트는
  기체 프로퍼티가 확정된 뒤 별도 작업으로 분리 가능. 검토는 반드시 작성자와 다른
  세션이 맡는다(정적검증 → 필요시 GPT 교차검증 → Codex 실행검증 순).
- 업로드받은 `run_jsbsim_timestamped_no_fg_prompt_csv_only.py` 하니스는 ROOT가
  `/home/junyeopkwon/jsbsim_workflow`에, discover_aircraft()가 스캔하는 기체 XML
  경로는 `/home/junyeopkwon/jsbsim/aircraft/<이름>/`에 하드코딩되어 있음. 따라서
  틸트로터 변형들의 실제 작업 위치는 그 WSL 트리로 두고, evtol-6dof는 완성된
  산출물만 주기적으로 `reference/`에 동기화하는 이원화 구조로 간다(QuadX_Baseline을
  evtol-6dof 안에 둬서 이 하니스가 못 찾았던 문제의 재발 방지).

## 미해결 이슈

- [ ] eVTOL 기체 형상 확정 (틸트로터 vs 멀티로터+고정익 vs 리프트+크루즈 등)
- [ ] 공력계수/추력모델 출처(문헌 or 자체 CFD/풍동) 미정 — eVTOL 본체 기준. QuadX_Baseline은
      F450 공식 예제 기반으로 해결됨(docs/QuadX_Baseline_model.md 2절)
- [ ] jsbsim-bridge에서 실제 사용하는 메시지 필드 확인 필요
- [x] (실행 검증 완료) 좌표계 변환식 — Codex가 QuadX_control_response_test.xml을
      JSBSim 1.2.4로 실제 실행해, 양의 aileron/elevator/rudder 입력에 양의 p/q/r
      응답이 나옴을 확인함(구조좌표계/동체좌표계 변환과 FCS 믹서 부호가 실행
      기준으로 정합). docs/coordinate_frame_checklist.md 갱신 완료.
- [x] (실행 검증 완료) QuadX_FCS.xml 요(yaw) 믹서 부호 — 위와 동일 실행으로 양의
      rudder-cmd-norm이 양의 velocities/r-rad_sec을 만드는 것 확인.
- [x] (실행 검증 완료) propulsion/engine[n]/power-hp, propeller-rpm 프로퍼티가
      electric_engine 타입에서 실제로 tie됨을 Codex 실행(CSV 기록)으로 확인.
- [ ] **QuadX_nominal_mission.xml 고도홀드 재설계 후 재검증 필요(신규, 최우선)** —
      Codex의 1차 실행에서 open-loop 스로틀 프로파일이 목표 10m AGL 대비 최대
      약 243.8 ft(약 74m)까지 오버슈트하고 90초 종료 시점에도 약 30.5 ft에
      떠 있어(착지 실패) 체크리스트 불합격 판정을 받음. 이에 Claude가
      models/systems/QuadX_FCS.xml에 고도 오차 PID 외곽 루프(Altitude Hold)를
      추가하고 scripts/QuadX_nominal_mission.xml을 target-altitude-agl-ft 기반
      제어로 재작성함(가동 로직은 QuadX_FCS.xml/스크립트 주석 참고). PID 게인은
      손계산 선형화 기반 1차 설계값이라 **아직 실행 검증/재튜닝 전** — Codex가
      다시 실행해 오버슈트·정착시간·최종 착지 고도를 확인하고 필요시 kp/ki/kd를
      조정해야 함.
- [ ] QuadX_Baseline JSBSim 1.2.4 표준 루트 레이아웃 불일치 — 1.2.4는
      --aircraft-path/--engine-path/--systems-path를 지원하지 않아 Codex가
      /tmp 심볼릭 링크로 우회함(docs/agent-log/DECISIONS.md 참고). 재현
      가능한 실행 스크립트(예: scripts/run_quadx_jsbsim.sh)로 고정할 것
      (docs/agent-log/TODO.md TODO-20260801-1830-002).
- [ ] `/home/junyeopkwon/jsbsim/aircraft/F450/`(F450 실체 모델 소스) 접근 여전히
      미해결 — Cowork 폴더 연결 도구가 UNC 경로(`\\wsl.localhost\...`,
      `\\wsl$\...`) 요청에서 반복적으로 실패함(툴 버그로 판단, jsbsim_workflow
      요청 때와 동일 증상). 사용자가 jsbsim_workflow를 수동 복사해 넣었던
      방식과 동일하게, 이 폴더도 evtol-6dof 안으로 수동 복사해 주면 해결됨.
- [ ] `reference/` 병합 이후 git add/commit/push 마무리 — `jsbsim_workflow/`
      원본 폴더는 중복/용량 문제로 `.gitignore`에 추가해 GitHub에는 올리지
      않는 방향을 제안함(사용자 확인 필요). `reference/`와 갱신된
      docs/STATUS.md, docs/coordinate_frame_checklist.md는 커밋 대상.

## 다음 작업

1. **[신규] `reference/` 병합분과 이 STATUS.md/체크리스트 갱신분을 git add/commit/push.**
   `jsbsim_workflow/` 원본은 `.gitignore` 처리를 제안(용량/중복 방지) — 사용자
   확인 후 확정.
2. Claude가 추가한 고도홀드(Altitude Hold) 폐루프를 Codex가 JSBSim 1.2.4로
   재실행해 오버슈트 해소 여부 확인, 필요시 PID 게인 재튜닝
3. JSBSim 1.2.4 표준 실행 루트 구성 방식을 실행 스크립트 또는 문서로 고정
4. 위 두 가지가 끝나면 QuadX_Baseline 검증 완료로 간주하고, 확립된
   모델링/검증/문서화 패턴 + `reference/docs/lessons_learned.md`의 교훈을
   틸트로터 본체(eVTOL_template.xml)에 이식
5. 틸트로터 개념설계 확정 (Gemini로 유사 연구 조사 — 리프트로터 개수/배치,
   틸트축 위치, 순항 전환(transition) 전략 등)
6. models/aircraft/eVTOL_template.xml 채우기 (Codex) — 이때
   docs/STATUS.md의 "독립 검증(2차 감사)" 로그에 남긴 aerodynamics
   qbar-area 곱셈 누락 이슈, `reference/docs/lessons_learned.md`의 AGL/좌표계/
   상태 머신 패턴을 함께 반영할 것
7. jsbsim-bridge 소스 코드 확인해서 bridge/README.md 필드 매핑 구체화 (Codex) —
   QuadX_Baseline으로 PX4 연동을 먼저 검증해보는 것도 고려 (docs/QuadX_Baseline_model.md 8절)
8. (선택) `/home/junyeopkwon/jsbsim/aircraft/F450/`을 evtol-6dof로 수동 복사해
   주면, F450 실체 모델까지 QuadX_Baseline과 교차 검증 가능

---

## 로그 (최신이 위로)

### 2026-08-02 — [claude] 로컬 에이전트 오케스트레이션 스크립트(automation/) 작성

- 사용자가 "AI 에이전트면 미리 설정해두면 알아서 도는 거 아니냐"고 질문. 실제로는
  Codex/Gemini/GPT가 서로 API/MCP로 연결돼 있지 않아 사람이 매번 복붙으로 이어주는
  수동 핸드오프 구조라는 걸 확인해주고(mcp-registry에서 OpenAI/Gemini 커넥터 검색
  결과 없음 확인), 진짜 자동화하려면 (1) WSL 로컬 스크립트로 codex/gemini CLI를
  순서대로 호출하거나 (2) API 키 기반 오케스트레이터를 만드는 두 갈래가 있다고 설명.
- 사용자가 "돈 없는 석사과정이라 구독 한도 내에서" 진행해야 한다고 확정 →
  API 키 방식은 배제하고 로컬 CLI 재사용 방식으로 결정.
- `automation/run_agent_pipeline.py` 작성: `codex exec`(실행 단계)와
  `gemini -p`(조사 단계) 두 가지만 자동화 대상으로 삼음. 안전장치: 새 API 키
  미사용(기존 로그인 세션 재사용), 하루 호출 상한(기본 Codex 8회/Gemini 20회)을
  넘으면 자동 중단(`usage_log.jsonl` 기준 카운트, Codex의 5시간+주간 이중 한도를
  스크립트 버그로 소진하는 사고 방지), git add/commit/push나 파일 삭제 같은
  되돌리기 어려운 작업은 스크립트가 절대 대신하지 않음, cron 없이 수동 실행이
  기본값(신뢰가 쌓이기 전까지 보류).
- "XML 1차 작성"과 "독립 정적검증"은 의도적으로 자동화하지 않음 — Claude가 기존
  맥락(좌표계 규약, 손계산, 이전 실패 사례)을 들고 있는 채로 직접 하는 게 codex
  exec로 맥락을 매번 새로 먹이는 것보다 안전하다고 판단.
- `automation/README.md`, 예시 프롬프트(`automation/prompts/example_research.txt`,
  `example_execute.txt`) 작성. `usage_log.jsonl`/`run_logs/`는 `.gitignore` 처리.
- **다음 단계(사용자 확인 필요)**: `codex exec "echo hello"`, `gemini -p "hello"`를
  WSL에서 손으로 먼저 실행해 로그인 세션이 재사용되는지 확인 후 결과 공유. 그 뒤
  몇 차례 수동 실행으로 `run_logs/` 품질을 확인하고, 신뢰가 쌓이면 cron 여부를
  재논의.

### 2026-08-01 — [claude] jsbsim_workflow 재사용 자산 병합 + 교훈 정리 + git 연동

- 사용자가 `jsbsim_workflow/`(6주간 Codex 작업 이력) 전체를 evtol-6dof 폴더 안으로
  직접 복사해 넣음. 이를 근거로 (1) 무엇을 하고 있었는지, (2) 합리적/효율적으로
  진행했는지, (3) 최종 목표가 무엇인지, (4) AI 역할분배를 어떻게 하면 좋을지
  종합 검토를 수행함(별도 서브에이전트 2개로 agent-log 전체와 산출물 인벤토리를
  나눠 분석, 상충되는 결과 1건은 직접 Glob으로 재검증해 정정).
- **중요 정정**: 검토 과정에서 LiftCruise2kg/ADS 계열을 논문 본체 기체로 오인했으나,
  사용자가 "리프트크루즈형은 별도 과제(과제)용이고 논문은 틸트로터를 생각 중"이라고
  정정함. 이후 모든 판단에서 이 구분을 유지함 — LiftCruise2kg는 재사용 가능한 참고
  자산일 뿐 논문 본체 목표가 아님.
- 사용자의 GitHub 계정(junyeop0401)에 evtol-6dof를 1차 저장소로 연동함(jsbsim_workflow가
  아니라 evtol-6dof를 선택한 이유: 에이전트 기반 워크플로로 전환하는 시점이라
  jsbsim_workflow는 참고 자료 역할로 한정하기로 함). `git remote add origin` +
  `git push -u origin main`으로 사용자가 직접 push, 성공 확인.
- `jsbsim_workflow`에서 재사용 가치가 높은 자산만 골라 `reference/`로 부분 병합함(전체
  복사가 아니라 선별 병합 — "일부 병합" 방식을 사용자가 직접 선택):
  - `reference/harness/`: run_jsbsim_timestamped 계열 실행 스크립트 + 로그/플롯 후처리
    스크립트 10종
  - `reference/aircraft/LiftCruise2kg/`: LiftCruise2kg 기체 정의 9개 파일 전체(참고용,
    논문 본체 아님)
  - `reference/scripts/F450/`, `reference/scripts/LiftCruise2kg/`: 검증된 호버/10m
    박스 미션 스크립트(성공 이력: F450 정확도 약 9.91 m, LiftCruise2kg 약 9.94 m,
    07-26 로그 기준)
  - `reference/earth_models/`: 지구 모델 4종 + README
  - `reference/docs/`: 기체 비교/C172P·C172X 비교/C172X 테스트플랜 원문 + 신규 작성한
    `lessons_learned.md`
- `reference/docs/lessons_learned.md`를 신규 작성함(원본 로그를 그대로 옮기지 않고
  실제 실행 검증되었거나 원문에서 직접 확인한 항목만 근거와 함께 정리): AGL 고도
  해석, JSBSim 1.2.4 CLI 경로 옵션 미지원, LiftCruise2kg의 "오차수렴+시간" 이중
  게이트 상태 머신 패턴(QuadX_nominal_mission의 open-loop 오버슈트 실패와 대조),
  구조/동체 좌표계 부호, electric_engine 채택 이유, F450 실체 모델 미접근 상태를
  담음.
- `jsbsim_workflow/` 원본 폴더 자체(9개 기체 변형, agent-log 전체 등)는 이번 병합
  대상에서 제외함 — GitHub에는 올리지 않고 로컬 참고 자료로만 유지할 것을 제안(아래
  다음 작업 참고, 사용자 확인 필요).
- **미해결로 남긴 것**: `/home/junyeopkwon/jsbsim/aircraft/F450/`(F450 실체 소스)
  접근은 Cowork 폴더 연결 도구의 UNC 경로 버그로 이번에도 실패함. 사용자가 수동
  복사해 주기 전까지는 QuadX_Baseline과의 직접 대조가 불가능한 상태.

### 2026-08-01 — [claude] Codex 실행 결과 검토 + 고도홀드(Altitude Hold) 폐루프 추가

- 사용자가 Codex로 QuadX_Baseline을 JSBSim 1.2.4에서 실제 실행 검증한 결과를
  검토해달라고 요청. docs/agent-log/*, docs/STATUS.md, docs/QuadX_Baseline_model.md
  9절을 읽고 Codex의 변경사항(init 파일 단위/AGL 해석 수정, 이벤트 시간 게이트
  추가)을 대조 확인함.
- **검증 확인(실행 기준으로 통과)**: 추진계/FCS 로딩 성공(종료코드 0), 롤/피치/요
  입력 부호가 실행 결과와 정합(양의 입력 → 양의 p/q/r), power-hp·propeller-rpm
  프로퍼티가 실제로 tie되어 CSV에 기록됨. Codex가 발견한 JSBSim 1.2.4 관련
  실제 버그 2건(초기조건 속도단위 M/S 미변환, initialize/altitude가 elevation
  기준이 아니라 AGL로 해석됨)은 실행 없이는 발견할 수 없었던 값진 발견이었음.
- **미해결로 확인된 문제**: QuadX_nominal_mission.xml이 open-loop 스로틀
  이벤트만으로 고도를 제어하다 보니 목표 10m AGL 대비 최대 약 243.8 ft까지
  오버슈트하고, 90초 종료 시점에도 약 30.5 ft에 떠 있어 착지가 완료되지
  않음(Codex도 1차 튜닝을 시도했으나 해결하지 못하고 TODO로 남김).
- **조치**: 손계산으로 호버점 근방 플랜트를 선형화(d(수직가속도)/d(스로틀)≈
  60.4 ft/s²/unit)해, 2차 플랜트 기준 ζ=0.8·ωn≈0.83rad/s(정착시간 약 6초
  목표)로 PID 게인(kp=0.0115, ki=0.0010, kd=0.0221)을 역산하고,
  models/systems/QuadX_FCS.xml에 고도 오차 기반 PID 외곽 루프("Altitude Hold"
  채널)를 추가함. 게이팅은 이 파일에 이미 검증된(ScasEngage와 동일한)
  "게인=프로퍼티" 패턴을 재사용해 신규 문법 리스크를 최소화함.
  scripts/QuadX_nominal_mission.xml도 함께 개정해, 이륙~하강 구간은
  fcs/target-altitude-agl-ft만 갱신하고(fcs/AltHoldEngage=1), 아이들/최종
  터치다운 구간만 fcs/throttle-cmd-norm-raw 직접 램프(open-loop)로 남김.
  디버깅용 CSV 컬럼(throttle-cmd-norm-raw, AltHoldEngage, target-altitude-agl-ft,
  altError_ft)도 추가함.
- **중요**: 이 PID 게인은 손계산 선형화에 기반한 1차 설계값이며, 이번에도
  실제로 JSBSim을 실행해 확인하지는 못했다(이 세션은 여전히 실행 불가 환경).
  Codex가 다시 실행해 오버슈트/진동/정착시간/최종 착지 고도를 확인하고
  필요시 게인을 재튜닝해야 완결된다.

### 2026-08-01 — [claude] 독립 검증(2차 감사)에서 발견해 수정한 오류 3건

- 위 QuadX_Baseline 작성 직후, 별도의 독립적인 재검토(에이전트 산출물을 처음
  작성한 것과 다른 시점의 관점에서 파일을 직접 다시 읽고 대조)를 수행해 아래
  3건의 실행 저해 요인을 찾아 즉시 수정함. 셋 다 실제로 JSBSim을 돌려보기 전
  단계의 정적 검토로 발견된 것이므로, 수정 후에도 실행 검증 자체는 여전히
  미실시 상태임.
  1. `models/aircraft/QuadX_Baseline.xml`의 `<flight_control file="QuadX_FCS"/>`
     에 `.xml` 확장자가 빠져 있었음(F450 공식 예제는 `file="FlightControl.xml"`
     처럼 확장자를 명시함). `QuadX_FCS.xml`로 수정.
  2. 같은 파일의 `<aerodynamics>` 축 function들이 계수값(예: CD=1.0)을 qbar-area와
     곱하지 않고 그대로 반환하고 있었음. JSBSim의 axis function 반환값은 계수가
     아니라 그 축에 바로 적용되는 힘/모멘트 그 자체이므로, 곱하지 않으면 저속
     구간에서도 상수 힘(약 4.45N)이 걸려 호버 트림을 오염시키는 실질적 버그였음.
     `aero/qbar-area`(모멘트는 `metrics/bw-ft`/`cbarw-ft`도 추가) 곱셈을 F450
     Aero.xml 패턴대로 추가해 수정. (참고: 이 패턴은 기존
     `models/aircraft/eVTOL_template.xml`에도 동일하게 남아있는 잠재 이슈이므로,
     그 템플릿을 실제로 채울 때도 반드시 이 수정을 반영할 것)
  3. `scripts/QuadX_nominal_mission.xml`의 CSV 출력에 쓰인
     `propulsion/engine[n]/prop-rpm`은 존재하지 않는 프로퍼티명으로 추정됨(F450
     공식 테스트 스크립트는 `propeller-rpm`을 사용). `propeller-rpm`으로 수정하고
     `docs/QuadX_Baseline_model.md` 7절 표도 함께 정정.
- 이 세 건 외의 구조/부호/손계산 로직은 직접 대조 재검토한 결과 이상을 발견하지
  못했으나, 이 역시 정적 검토의 한계 내에서의 결론이며 실행 검증을 대체하지 않음.

### 2026-08-01 — [claude] QuadX_Baseline(순수 쿼드콥터) 베이스라인 모델 작성

- 목적: eVTOL 본체 모델링에 앞서 JSBSim 추진계/FCS 모델링·검증·문서화 파이프라인을
  단순한 쿼드-X 기체로 먼저 확립. eVTOL_template.xml/FCS_template.xml은 건드리지 않고
  완전히 별도의 신규 4종 세트로 작성함.
- 형상/질량/관성/추진계 제원은 JSBSim 공식 저장소(JSBSim-Team/jsbsim)의 F450(DJI 프레임)
  예제 실측값을 재사용/각색. 모터 타입은 F450 원문의 brushless_dc_motor 대신
  electric_engine(FGElectric)을 채택함 — brushless_dc_motor에 알려진 "failed to tie
  property" 버그(GitHub Discussion #1183) 및 스키마 버전 오기(version="3.0"은 존재하지
  않음, 정답은 "2.0") 때문.
- 손계산 재검산 완료: 호버 스로틀 34.7%, 호버 RPM 4909, 최대 T/W 2.03 — 원 설계
  사양과 반올림 수준까지 일치 확인. 롤/피치/요 제어권한도 모멘트 계산으로 직접 재검산.
- 자체 검증 중 두 가지 오류를 발견해 직접 재계산으로 수정함: (1) 프로펠러 관성 클램프
  배율이 원래 "약 700배"로 가정되어 있었으나 정확히 재계산한 결과 약 22.4배로 확인,
  문서/주석 모두 정정함. (2) 요 축 각가속도 "약 5 rad/s²"라는 원 설계 메모도 재계산
  결과(10% 차동 기준 약 1.1 rad/s², 포화 기준 약 11.0 rad/s²)와 정확히 일치하지 않아,
  정성적 결론(요축이 롤/피치보다 약함)은 유지하되 수치는 재계산값으로 교체.
- **신규 생성 파일**: models/aircraft/QuadX_Baseline.xml, models/engine/QuadX_Motor.xml,
  models/engine/QuadX_Prop.xml, models/systems/QuadX_FCS.xml, init/QuadX_ground.xml,
  init/QuadX_hover.xml, scripts/QuadX_nominal_mission.xml,
  scripts/QuadX_control_response_test.xml, docs/QuadX_Baseline_model.md
- **갱신 파일**: docs/STATUS.md(이 로그), docs/coordinate_frame_checklist.md(구조좌표계
  vs 동체좌표계 항목 추가)
- **중요**: 이번 세션은 실제 JSBSim 실행이 불가능한 환경이었으므로, 위 산출물은 전부
  손계산/논리 검증(self-review)까지만 완료된 상태이고 실제 실행 검증은 전혀 하지
  않았음. 반드시 사용자 로컬 WSL에서 실행 후 docs/QuadX_Baseline_model.md 7절
  체크리스트와 대조할 것.

### 초기 세팅 — Claude
- 프로젝트 스켈레톤 생성 (폴더 구조, xml 템플릿, 체크리스트, README)
- Codex/Gemini/Claude Code 3개 CLI 설치 및 인증 완료

### 2026-08-01 — [codex] QuadX_Baseline JSBSim 1.2.4 실행 검증 및 1차 런타임 수정

- 사용자 요청에 따라 README와 STATUS.md의 에이전트 역할 배정을 확인했고, Codex 최우선 과업이 QuadX_Baseline 4종 세트의 실제 JSBSim 실행 검증임을 확인함.
- 로컬 WSL의 JSBSim 1.2.4를 사용해 실행 검증을 수행함. 확인된 실행 파일: /usr/local/bin/JSBSim.
- JSBSim 1.2.4는 문서에 적힌 --aircraft-path, --engine-path, --systems-path 옵션을 지원하지 않아 /tmp/evtol-jsbsim-run-codex 아래에 표준 JSBSim 루트 구조를 심볼릭 링크로 구성해 검증함.
- 실행 차단 오류 2건을 수정함.
  1. init/QuadX_ground.xml, init/QuadX_hover.xml의 속도 단위 M/S가 JSBSim 1.2.4 초기조건 파서에서 변환되지 않아 vt는 KTS, ubody/vbody/wbody는 FT/SEC로 변경.
  2. initialize/altitude가 elevation 위 AGL 높이로 처리되는 것을 확인해 QuadX_ground는 altitude 0m, QuadX_hover는 altitude 10m로 변경.
- 정상 미션의 고도/착지 이벤트가 시작 시점에 바로 발화하는 문제를 수정하기 위해 레벨오프/플레어/터치다운 이벤트에 시간 게이트를 추가함.
- scripts/QuadX_control_response_test.xml은 종료코드 0으로 실행됐고 CSV 기준 양의 roll/pitch/yaw 입력에서 각각 양의 p/q/r 응답이 확인됨. 축별 부호 검증은 통과.
- scripts/QuadX_nominal_mission.xml은 종료코드 0으로 실행되지만 체크리스트는 아직 불합격. 현재 튜닝값 기준 최대 고도 약 243.8 ft, 90초 최종 고도 약 30.5 ft로 10m급 호버/착지 프로파일을 만족하지 못함.
- propulsion/engine[n]/power-hp와 propeller-rpm 출력은 실제 CSV에 기록됨을 확인함.
- 남은 최우선 작업: 정상 미션을 별도 고도 제어 또는 더 정교한 open-loop 스로틀 프로파일로 재설계해 10m급 호버와 안정 착지를 통과시킬 것. 또한 JSBSim 1.2.4용 표준 실행 루트 구성 방식을 문서화하거나 실행 스크립트로 고정할 것.
