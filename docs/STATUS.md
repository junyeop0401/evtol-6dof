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
- [ ] bash 도구 마운트 버그 — WSL UNC 경로 폴더가 연결돼 있으면 대상 경로와
      무관하게 해당 세션의 모든 bash 호출이 마운트 단계에서 즉시 실패함(이번
      세션에서 `D:\evtol 6dof` 대상 명령으로도 동일한 WSL 경로 에러가 나는 것을
      확인해 원인 특정, 아래 로그 참고). Read/Write/Edit/Glob 도구는 WSL UNC
      경로에서도 정상 동작하므로 문서 편집 자체는 계속 가능하나, git
      add/commit/push나 JSBSim 실행 같은 bash 필수 작업은 이 폴더가 연결된 채로는
      불가능. 사용자가 실제 WSL 터미널(Cowork 도구 우회)에서 직접 git
      add/commit/push를 실행해 미커밋 변경사항은 이미 push 완료(commit
      `40c038f`, 2026-08-02) — 이제 `D:\evtol 6dof`를 새 작업 루트로 git clone하는
      단계만 남음(다음 작업 0번 참고).

## 다음 작업

0. **[최우선, 준비 완료] `D:\evtol 6dof`에 GitHub 저장소(`junyeop0401/evtol-6dof`)를
   `git clone`해서 새 작업 루트로 삼을 것.** WSL 쪽 미커밋 변경사항은 아래 1번
   항목으로 전부 push 완료(commit `40c038f`)했으므로, GitHub 원격 저장소가 곧
   최신 상태 — 이제 clone만 하면 됨. 이번 세션에서 bash 도구 버그의 원인도
   특정함(아래 2026-08-02 로그 "bash 도구 마운트 버그 원인 특정" 항목 참고) —
   WSL UNC 경로 폴더(`\\wsl.localhost\...`)가 연결돼 있으면 대상 경로와 무관하게
   세션의 모든 bash 호출이 마운트 단계에서 실패함. 다음 세션(새 채팅)은
   `D:\evtol 6dof`만 연결한 상태로 시작해 git clone부터 진행할 것.
1. ~~`reference/` 병합분과 이 STATUS.md/체크리스트 갱신분을 git add/commit/push.~~
   **완료(2026-08-02)** — commit `40c038f`, `b58d748..40c038f` push 성공(사용자가
   실제 WSL 터미널에서 직접 실행, Cowork bash 도구 버그와 무관하게 정상 동작
   확인). 커밋 범위: `docs/STATUS.md`, `docs/coordinate_frame_checklist.md`,
   `reference/docs/lessons_learned.md`(수정) + `docs/mission_reports/` 전체,
   `docs/F450_1.2_box_hover_land_report.md`, `docs/F450_mission_ppt_outline.md`(신규,
   총 15개 파일). `reference/harness`·`aircraft/LiftCruise2kg`·`scripts`·
   `earth_models`, `automation/`, `docs/agent-log/`, `docs/gpt_crosscheck_template.md`,
   고도홀드 관련 `models/systems/QuadX_FCS.xml`/`scripts/QuadX_nominal_mission.xml`은
   `git status`에 안 잡힌 것으로 보아 이전 세션에서 이미 커밋되어 있었던 것으로
   확인됨. `jsbsim_workflow/` 원본은 기존 `.gitignore`가 이미 제외 처리 중이라
   추가 조치 불필요했음.
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
9. (선택) 사용자가 로컬 MATLAB에서 `run_jsbsim_csv_plotter_v7.m`으로 F450
   2.0.4/1.2.22 raw CSV의 "표준 분석 패키지"를 생성해 PNG 폴더를 공유해주면,
   c172x 5.16과 동일한 방식으로 F450 두 리포트에 "그래프 분석" 절 추가

---

### 2026-08-17 — [claude] 배터리/서보 예시값을 pointmass로 추가 (웹 검색 기반)

- 사용자가 "인터넷에 minitalon 배터리/서보 스펙 나와있을 테니 그거 기준으로 예시
  구현해봐"라고 요청. 직전 항목(구조체 CAD 값 + 모터 pointmass만 있던 상태)에
  이어서 배터리/서보를 EXAMPLE로 추가.
- 웹 검색 결과: 킷 정품 스펙은 서보 4x9g(HXT900급, 실측 9.8g), 배터리는 4S
  5000~8000mAh 권장(ItsQv 빌드로그가 실제 사용한 8000mAh와 일치). "4S 8000mAh"
  질량은 소매처마다 630g~1140g으로 크게 갈려서(스펙 표기 오류로 추정) 중간값
  ~830g을 예시치로 채택 — SOURCE가 아니라 ASSUMPTION/EXAMPLE로 명시.
- 부수적으로 CAD 보고서 6절에서 "Motor support" 부품 자체의 무게중심
  (X≈781.2mm)이 모터 위치의 더 나은 추정치라는 예시 문구를 발견해, 기존에
  추력기(프로펠러) 위치(x=0.920)로 근사했던 모터 pointmass 위치를 x=0.790으로
  보정. 보고서 예시가 다른 모터(Cobra 2221/16, 88g)를 썼다는 점도 혼동 방지를
  위해 주석에 명시(실제 장착 모터가 어느 쪽인지는 여전히 LIM-ENGINE-001로 OPEN).
- `aircraft/MiniTalon/Mass.xml`: 배터리(0.830kg, x=0.20, 앞쪽 해치 자리 추정)와
  서보 4개(각 0.0098kg, 에일러론 L/R + 러더베이터 L/R, 대략적 스팬/코드 위치
  추정) pointmass를 활성화. ESC/수신기+FC는 여전히 주석 스텁으로 남김.
- 합산 질량 점검: 구조체(761.38g)+모터(140g)+배터리(830g)+서보4개(39.2g) =
  약 1770.6g. 실제 완성기체 무게(ItsQv 빌드로그 1890g)와 약 120g 차이인데, 이
  갭이 아직 안 넣은 ESC+수신기/FC 무게로 설명 가능한 범위라 정합성 점검으로
  나쁘지 않음(증명은 아님, 참고용).
- `aircraft/MiniTalon/Metrics.xml`: htailarm/vtailarm을 새 합산 CG(x≈0.314m)
  기준 0.407m로 재계산(직전 값 0.290m, 그 이전 0.330m에서 순차 갱신). 배터리/
  서보 위치가 전부 추정치라 여전히 잠정치로 문서화.
- `aircraft/MiniTalon/ASSUMPTIONS.md`: ASM-MASS-002(배터리), ASM-MASS-003(서보)
  신규 행 추가, SRC-CAD-002(모터 위치 보정)/ASM-GEO-002/003/ASM-MASS-001 갱신.
- 다음 작업: 실제 배터리 실측 무게/서보 장착 위치를 받으면 EXAMPLE 값을
  교체하고, ESC/수신기+FC pointmass를 채워 최종 AUW 완성. 이후 do_simple_trim
  재시도.

---

### 2026-08-17 — [claude] MiniTalon CAD 질량특성 코드 감사 + Mass.xml/Metrics.xml을 pointmass 구조로 갱신

- 이전 세션(bash가 막힌 이 세션 대신 사용자가 새로 연 별도 세션)이 `Assem4.step`을
  자체 제작 STEP 파서+NURBS 테셀레이터+다면체 질량적분기로 처리해 만든
  `Mini_Talon_Mass_Properties_Report.md` + 파이썬 코드(`step_parse.py`,
  `geom.py`, `tessellate.py`, `massprops.py`, `aggregate.py`, `final_report.py` 등
  14개 파일, 사용자가 이번에 업로드)를 정독.
- 코드 감사 결과: geom.py의 NURBS 평가(find_span/basis_funs)는 표준 알고리즘과
  일치하고 자체 검증 테스트 포함, massprops.py의 질량적분 공식은 표준 다면체
  질량특성 공식(Mirtich 계열)과 일치, aggregate.py/final_report.py의 평행축
  정리 적용도 정확함을 확인 — 지어낸 결과가 아니라 방법론적으로 건전한 파이프라인.
  하드웨어 질량(FILL_FACTOR=0.55, PLATE_THICKNESS_MM=2.5, 재질별 밀도표)은
  코드에 명시적 가정치로 노출되어 있어 실측 시 바로 교체 가능한 구조.
- 수치 정합성: CAD 스팬 1.280m/길이 0.814m가 실제 공개 스펙(1.300m/0.830m)과
  1.5~2% 오차로 일치, CAD "구조물 전체" 질량(761.38g, 모터/배터리/전자장비 제외)과
  실제 완성기체 무게(ItsQv 빌드로그 1890g)의 차이(~1130g)가 배터리+모터+전자장비
  무게로 설명 가능함을 확인.
- 사용자 제안("지금 있는 CAD 데이터로 구성해두고 모터/배터리/서보는 나중에
  pointmass로 추가하면 되지 않냐")이 정확히 JSBSim의 의도된 사용법(emptywt+CG+관성은
  구조체 기준, pointmass는 parallel-axis로 자동 합산)과 일치함을 확인하고 채택.
- `aircraft/MiniTalon/Mass.xml` 갱신: emptywt/CG/Ixx~Iyz를 CAD 구조체 전용 값으로
  교체(기존 ArduPilot-Gazebo seed 폐기), Cobra C-2820/14 모터(실측 아님, 제조사
  스펙 140g, 소매처 2곳 교차확인)를 pointmass로 추가, 배터리/서보/ESC/수신기는
  주석 처리된 pointmass 템플릿으로 남김(값 확보되는 대로 채우기만 하면 됨).
- `aircraft/MiniTalon/Metrics.xml` 갱신: htailarm/vtailarm을 CAD V-tail 25%MAC점
  기준 0.290m로 갱신(기존 0.330m ArduPilot-Gazebo 45도 투영 seed 폐기). 배터리/서보
  추가 전까지는 잠정치로 명시(배터리가 보통 모터 반대편에 실려 CG가 다시 앞으로
  이동할 가능성 문서화).
- `aircraft/MiniTalon/ASSUMPTIONS.md` 갱신: SRC-CAD-001/002, ASM-GEO-002/003 신규
  행 추가, ASM-INERTIA-001/ASM-MASS-001 상태 갱신. 부수적으로 발견한 불일치 2건도
  플래그: (1) ASM-PROP-001의 추력기 위치(x=0.805)가 실제 Propulsion.xml(x=0.920)과
  달라 STALE-FLAGGED 처리, (2) `engine/` 폴더에 Cobra 모터 XML이 2종(C2820/14,
  C2221/16) 존재하는데 Propulsion.xml은 C2820/14만 참조 — 실제 장착 모터가
  어느 쪽인지 사용자 확인 필요(LIM-ENGINE-001).
- 다음 작업: 배터리 실측 무게(또는 4S 8000mAh 스펙)·서보 개수/무게·대략적 장착
  위치를 받으면 Mass.xml의 주석 pointmass 템플릿을 채워 최종 AUW를 완성하고,
  do_simple_trim 재시도 및 minitalon_config.xml(파이썬 크래시 모델용) 작성으로 이어갈 것.

---

### 2026-08-03 — [claude] "mini palcon"(=MiniTalon) 모델 검토 + jsbsim_workflow/script 폴더 생성

- 새 채팅에서 사용자가 "jsbsim에 새로 mini palcon 모델을 구성해봤다, 검토해달라,
  evtol-6dof/jsbsim_workflow/script에 초기조건·runscript 만들 건데 일단 폴더만
  생성해두고 모델 검토만 하라"고 요청.
- "mini palcon"이라는 이름은 evtol-6dof, junyeopkwon 홈, /home/junyeopkwon/jsbsim
  어디에도 문자열 그대로는 존재하지 않음을 확인. 대신 /home/junyeopkwon/jsbsim의
  agent-log에서 오늘(2026-08-03 15:28) Codex가 X-UAV **MiniTalon** 부트스트랩
  모델(aircraft/MiniTalon/*, engine/MiniTalon_*, scripts/MiniTalon_*_run.xml 등)을
  막 생성한 기록을 발견 — 시간상 정확히 일치해 이것을 지칭하는 것으로 판단하고 검토
  진행(사용자에게 확인 요청 없이 합리적 추정으로 진행, 최종 답변에는 이 추정을 명시).
- 정적 검토 결과: 문서화(SOURCE/DERIVED/ASSUMPTION/LIMITATION 분류) 품질 높음,
  fdm_config version="2.0" 정상, qbar-area 곱셈 전 축 정상 적용, airborne init의
  AGL 처리 정상. 원 저자가 이미 TODO로 남긴 문제(longitudinal trim 미수렴, CAD/AVL
  데이터 미반영 등)도 확인.
- **새로 발견한 위험(원 저자 TODO에 없던 것)**: MiniTalon 추진계가
  `<brushless_dc_motor>` 타입을 쓰는데, 이는 `reference/docs/lessons_learned.md`
  6절이 "failed to tie property" 버그(GitHub Discussion #1183)를 이유로
  QuadX_Baseline에서 이미 electric_engine으로 대체한 바로 그 컴포넌트. smoke test는
  exit 0 + CSV bad 0건으로 통과했지만, 이 기준은 propeller-rpm/power-hp가 실제로
  0이 아닌지까지는 보장하지 않음 — F450AP의 "종료코드 정상인데 실제로는 이륙
  안 함" 조용한 실패와 같은 패턴 위험. 다음 세션(Codex 권장)에서 CSV 실제 수치
  확인 필요.
- `jsbsim_workflow/scripts/MiniTalon/{initial_condition,runscript}/` 폴더를
  README 자리표시자만으로 생성(사용자가 이번 턴엔 폴더 생성까지만 요청, 실제
  init/runscript XML 작성은 다음 턴).
- 이번 세션도 bash 도구가 WSL UNC 마운트 버그로 막혀 있어 JSBSim 실행이나 CSV
  수치 직접 확인은 못 함 — Read/Glob/Grep 기반 정적 검토만 수행.
- 다음 작업(신규, 이 항목이 최우선): (1) brushless_dc_motor 유지/교체 결정,
  (2) MiniTalon_smoke_test.csv의 propeller-rpm/power-hp/thrust-lbs 실제 값 확인,
  (3) trim 미수렴 해결(CG/Cm0/Cmde/thrust line 동시 조정), (4) 위 3가지 정리 후
  jsbsim_workflow/scripts/MiniTalon에 실제 초기조건/runscript 작성.

**추가(같은 날 후속)**: 사용자가 Codex에게 do_simple_trim 없는 오픈루프 근사평형
비행시험을 맡김(지시문은 이 세션이 작성). Codex가 76개 조합 격자 탐색
(`tools/minitalon_openloop_sweep.py`)을 수행해 theta=0.8deg/elevator=0.0/
throttle=0.45 조합에서 90초간 추락·NaN 없이 유지되는 걸 확인(round2_38, score
17.78). 이 세션이 원본 CSV(`MiniTalon_quasitrim_sweep_summary.csv`,
`MiniTalon_quasitrim_flight.csv`, `MiniTalon_smoke_test.csv`)를 직접 열어 대조
검증함 — Codex 보고 수치(h_end 854.29ft, v_end 54.06fps, propeller-rpm 6542.8,
power-hp 0.0596, thrust-lbs 0.444)가 원본과 정확히 일치, 조작/과장 없음 확인.
브러시리스 모터도 이번엔 실제로 0이 아닌 값이 나옴을 재확인(지난번 우려 해소).
다만 이 결과는 진짜 트림이 아니라 "90초 동안은 안 터지는 근사값"일 뿐이며,
고도가 5초 이후 +15.77 ft 계속 완만히 상승 중(theta도 0.8→1.52deg로 계속 증가)
— Codex도 TODO-20260803-1733-001로 같은 한계를 스스로 기록해 둠. CAD/AVL 데이터
반영과 정식 trim은 여전히 미해결.

---

### 2026-08-02 — [claude] bash 도구 마운트 버그 원인 특정 + `D:\evtol 6dof` git clone 전환 결정

- 새 채팅 시작. 프로젝트 규칙(9번, "새 채팅에서는 이전 대화 무시하고 필요한 걸
  먼저 물어봐라")에 따라 사용자가 "변경했어 이제 너가 하는거야?"라고만 말한
  시점에 무엇이 바뀌었는지 먼저 질문함.
- 질문 전, 배경 파악을 위해 `docs/agent-log/*`와 `docs/STATUS.md`를 먼저 읽어
  직전 세션 마지막 상태(사용자 제공 MATLAB CSV 플로터 검토, 여전히 git 미커밋,
  bash 도구 장애 지속 언급)를 확인함.
- 사용자 답변: `D:\evtol 6dof` 폴더를 연결하고 새 채팅으로 넘어가서 거기서
  git clone부터 이어가겠다는 계획.
- 이 계획의 근거를 이번 세션에서 직접 재현/특정함: `mcp__workspace__bash`로
  `D:\evtol 6dof` 대상 명령(`ls`)을 실행해도 에러 메시지가 `D:\evtol 6dof`가
  아니라 `\\wsl.localhost\ubuntu-22.04\home\junyeopkwon\evtol-6dof`(UNC 경로)를
  가리킴 — 즉 **bash 도구가 세션에 연결된 폴더를 전부 마운트하려 시도하고,
  그중 WSL UNC 경로 폴더 하나만 있어도 명령 대상과 무관하게 전체 마운트 단계에서
  실패**하는 것으로 확인됨. 과거 로그들이 "bash 도구 장애 지속"이라고만 반복
  기록하고 원인은 특정하지 못했던 부분을 이번에 진단함.
- Read/Write/Edit/Glob 도구는 WSL UNC 경로에서도 정상 동작함을 재확인(이 파일
  자체도 그 경로로 직접 편집). 다만 `Glob`으로 저장소 루트 전체(`**/*`, 확장자
  없는 `*`)를 조회하면 20초 타임아웃이 반복 발생(`*.md`처럼 확장자를 좁히면
  정상) — 저장소 규모(특히 `jsbsim_workflow/` 원본)가 커서 WSL 마운트를 통한
  전체 탐색 자체가 느린 것으로 추정, 별도 조치는 하지 않음(범위를 좁혀 조회하는
  방식으로 충분히 우회 가능).
- **결론/조치**: `docs/STATUS.md` "다음 작업" 0번, "미해결 이슈"에 이 진단
  내용과 `D:\evtol 6dof` git clone 전환 계획을 기록. 실제 git clone과 이후
  작업은 사용자가 다음 세션(D:\evtol 6dof만 연결한 새 채팅)에서 이어가기로 함 —
  이번 세션에서는 bash가 막혀 있어 clone을 대신 실행할 수 없었음.
- **인수인계 시 주의사항(다음 세션에서 반드시 확인)**: 현재 WSL 폴더
  (`\\wsl.localhost\...\evtol-6dof`) 쪽에는 `reference/` 병합분, 이 STATUS.md
  갱신분, `docs/mission_reports/` 전체, `docs/coordinate_frame_checklist.md`
  등 다수의 git 미커밋 변경사항이 남아있음. `D:\evtol 6dof`에 GitHub 원격
  저장소를 그대로 clone하면 그 마지막 push 시점(2026-08-01, `reference/` 병합
  이전) 상태만 받아오게 되므로, WSL 쪽 미커밋 변경분을 먼저 커밋/푸시하거나
  D: 쪽으로 수동 반영하지 않으면 그 작업 내용이 새 작업 루트에서 누락됨.
  다음 세션 시작 시 이 문제를 최우선으로 사용자와 확인할 것.

### 2026-08-02 — [claude] 사용자 제공 MATLAB CSV 플로터(`run_jsbsim_csv_plotter_v7.m`) 검토

- 사용자가 본인이 작성한 MATLAB GUI 앱 스크립트를 업로드하고, 이걸로 미션
  그래프를 뽑아 정리할 수 있는지 질문. 스크립트 전체(3527줄, uifigure 기반
  App Designer 앱)를 읽고 실제 사용 가능 여부를 검증함.
- **결론: 그대로 사용 가능하며, 특히 F450 2.0.4/1.2.22의 "플로팅 파이프라인
  미실행" 갭을 bash 없이 즉시 메울 수 있는 실질적 대안.** 앱 내
  "표준 분석 PNG + summary CSV 저장" 버튼(`exportStandardAnalysisPackage`)이
  CSV 1개를 불러오면 자동으로 공통 6개 그룹(고도/속도/자세/각속도/위치/조종면
  명령) + 기체별 프리셋 추가 그룹(F450: 로터 RPM·추력·유도오차 3개, C172:
  활주로 오차·착륙기어 WOW 2개)의 PNG와 `summary_metrics.csv`
  (최대고도/최종거리/로터별 최대RPM 등), `skipped_plots.txt`(매칭 안 된 열
  기록)를 지정 폴더에 한 번에 생성함. 이건 이 세션에서 c172x 5.16 리포트에
  수동으로 했던 "관련 항목 묶어서 그래프 분석" 작업의 자동화 버전과 사실상
  동일한 목적.
- **컬럼 매칭 실측 검증**: F450 2.0.4 raw CSV와 c172x 5.16.5 raw CSV의 실제
  헤더(`/fdm/jsbsim/...` 전체 프로퍼티 경로)를 스크립트의 후보 열 목록
  (`altitudeCandidates`, `rotorRpmCandidates`, `northErrorCandidates`,
  `runwayCrossCandidates` 등)과 직접 대조. 거의 모든 후보가 이 프로젝트의
  실제 컬럼명과 정확히 일치함 — 이미 이 프로젝트 CSV 스키마에 맞춰 튜닝된
  스크립트로 판단됨. **발견한 사소한 불일치 1건**: `gearWowCandidates`가
  0번 기어를 `gear/unit[0]/WOW`(대괄호 포함)로 찾는데, 실제 CSV 헤더는
  `gear/unit/WOW`(대괄호 없음, 0번 암묵적)라서 0번 기어만 매칭 실패 —
  1/2번 기어는 정상 매칭. C172 프리셋에서만 영향(F450 프리셋엔 gear 그룹
  자체가 없어 무관).
- **실행 환경 제약**: `uifigure`/App Designer 기반 GUI 앱이라 로컬 MATLAB
  desktop에서 직접 Run해야 함. 이 세션의 sandbox bash는 MATLAB 자체가 없고,
  있었어도 headless 환경이라 GUI 실행은 불가 — Claude가 대신 실행할 수 없다.
  사용자가 본인 컴퓨터에서 CSV 선택 → 프리셋 지정 → 표준 분석 패키지 버튼
  실행 후, 결과 PNG 폴더를 공유해주면 그걸 근거로 F450 2.0/1.2 리포트에도
  c172x 5.16과 동일한 "그래프 분석" 절을 추가할 수 있음(가능해지는 즉시 우선
  진행할 작업으로 다음 작업 목록에 반영).
- 이 스크립트가 자동 커버하지 못하는 부분(이번 세션 c172x 분석에서 다뤘던
  것 중): 미션-스테이트 마스터 타임라인, 서브시스템 게이트의 중간신호 vs
  최종출력 대조, 오토파일럿 setpoint-실제값 추종오차 정량화 — 이런 건 앱의
  2D 설정 탭에서 원하는 두 열을 수동으로 골라 그려야 함(가능은 함, 표준
  패키지처럼 원클릭 자동화는 안 됨). 단, XML 이벤트 수직선 오버레이 기능은
  런스크립트 XML을 함께 로드하면 지원됨(수동 2D 탭 한정, 표준 패키지 PNG엔
  미적용).

---

### 2026-08-02 — [claude] "분석" 절을 CSV 그래프 기반 그룹 분석으로 격상(c172x 5.16 리포트)

- 사용자 요청: 결과 분석을 CSV 그래프로 진행하되 관련 항목끼리 묶어서(cmd가
  제대로 들어갔는지, cmd와 조종면 실제 이동을 비교해 딜레이가 있는지, 거리
  정보로 궤적 확인) 하고, 사용자가 미처 생각 못한 것도 능동적으로 찾아보라고
  지시.
- `jsbsim_workflow/ploting/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16.5__.../
  raw_time_series/`에 이미 사전 렌더링된 개별 프로퍼티 PNG(376개)가 있음을
  확인하고, 이를 9개 그룹(스로틀 cmd/pos, 엘리베이터 체인, 롤/에일러론,
  플랩 cmd/pos, 자동조종 setpoint 추종, 미션상태 마스터 타임라인, 착륙기어
  WOW, 원형선회 서브시스템 게이트 검증, 활주로축 거리 궤적)으로 묶어 총
  20여 개 이미지를 직접 열람·대조함.
- 새로 발견/보강된 사실: (1) 스로틀은 cmd=pos로 완전 일치(액추에이터 지연
  모델 없음), 엘리베이터/에일러론은 실제 lag가 있음 — 차이를 그래프로 대비
  확인. (2) 플랩 cmd(계단)와 flap-pos-deg(1~2초 경사)로 킨매틱 traverse
  지연을 시각적으로 확인. (3) `ap/aileron_cmd`에 t≈25.5s +270이라는 비정상
  스파이크가 있으나 `clipto[-1,1]`로 하류에서 무해화됨을 확인(내부 과도현상,
  실제 조종면엔 영향 없음). (4) 헤딩/고도 setpoint vs 실제를 대조해 추종
  지연(헤딩 최대 약 50초)과 오버슈트(고도 약 20~30ft)를 정량화. (5)
  mission-state 계단 그래프를 판독해 콘솔에 없던 중간 상태 전이 근사 시각을
  얻었고, 이 과정에서 이전 리포트의 "원형선회가 t≈280s 시작" 서술이 부정확
  (실제 t≈180s)했음을 발견해 정정. (6) **가장 중요한 발견**: 원형선회
  뱅크홀드 서브시스템의 중간신호(`mission/circular-bank-cmd-norm`)는 활발히
  진동해 "죽은 코드"라는 이전 결론과 모순돼 보였으나, 최종 게이트 출력
  (`ap/roll-cmd-norm-output`)을 별도로 확인한 결과 전 구간 정확히 0.0으로
  확인 — 서브시스템이 실제로 비활성이라는 결론이 콘솔 대조보다 훨씬 강한
  근거(그래프 직접 대조)로 재확인됨. 이는 "중간신호만 보고 판단하면 안
  되고 최종 게이트 출력까지 확인해야 한다"는 일반 원칙으로 정리해
  템플릿에도 반영.
- `docs/mission_reports/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing.md`
  3절에 "그래프 분석(CSV 기반, 관련 항목 그룹별)" 서브섹션 신설, 한계·PPT
  매핑 절도 갱신.
- `_scenario_template.md` 3절에 그래프 분석 표준 절차(6개 그룹 가이드,
  "중간신호뿐 아니라 최종 게이트 출력까지 확인" 원칙 포함) 추가.
  `README.md` 규칙 6번으로 명문화.
- F450 2.0.4/1.2.22는 이 런들에 대한 플로팅 파이프라인이 실행된 적이 없어
  (다른 F450 런인 1.1.1만 존재) 이번엔 그래프 분석 절을 추가하지 못함 —
  두 리포트의 한계 절에 그 사실과 향후 계획을 명시. bash 복구 또는 Codex
  실행 시 최우선으로 플로팅 파이프라인부터 돌릴 것.
- 다음 작업: 여전히 git 미커밋.

### 2026-08-02 — [claude] 문서화 컨벤션을 F450 외 기체(C172x)로 일반화 검증

- 사용자가 `5.16__ksfo28r_runway_return_circular_landing_run.xml`을 업로드하고
  지금까지 만든 문서화 컨벤션(2단 구조 + 기호 표기법)이 F450 외에도
  일반화되는지 확인해달라고 요청. 기체(c172x_4x75kg_cg_aligned_ksfo28r_landing,
  4인승 75kg 탑승 C172P 변형)·초기조건(`2.4__ksfo_28r_flightgear_default_init.xml`)·
  실행결과(가장 최근 `5.16.5`, 07271258, 5회 실행 중 마지막)를 전부 원본에서
  직접 읽어 확인.
- `docs/mission_reports/c172x_4x75kg_cg_aligned_ksfo28r_landing/_aircraft_spec.md`
  신규 작성 — F450과 근본적으로 다른 자동조종 아키텍처(단일 `ap/mode` 대신
  `ATT_hold`/`ALT_hold`/`HDG_hold` 3개 독립 플래그, 게이트 조건이 아니라
  가산형 명령 합산)와 아치파일 내 커스텀 서브시스템(원형선회 뱅크홀드,
  활주로축 좌표변환)까지 문서화.
- `5.16__ksfo28r_runway_return_circular_landing.md` 신규 작성 — 24개 상태(0~23)
  + 4개 안전중단 이벤트 전체를 기호 표기 이벤트표로 정리. 콘솔 로그(자동
  Takeoff/Touchdown/GEAR_CONTACT 리포트)로 이륙(t≈30.5s)·착지(t=627.0s)·
  미션완료(t=636.7s)를 실측 확인했고, 이륙활주 중 짧은 기어이탈과 착지
  롤아웃 중 반복 바운스라는 2개의 새로운 특이사항을 발견해 기록. 궤적 3D
  플롯을 직접 열어 "원형선회"가 실제로 둥근 루프임을 시각적으로 확인(90°
  헤딩스텝 4회로도 둥글게 나온 이유까지 해석).
- 일반화 과정에서 `_notation_common.md`에 새 구성요소 3종을 추가: (1)
  `ubody/vbody/wbody` 기반 초기속도 지정 방식(u₀/v₀/w₀), (2) 비행상태/착지
  공통 기호(h_AGL/ḣ/V_cas/α/WOW_i), (3) `<delay>`와 `FG_RAMP` 표기 규칙(↝ 기호,
  +delay Xs). 기체 고유 기호(δ_thr 등 구체 매핑, ATT_h/ALT_h/HDG_h,
  x_rwy/y_rwy 등)는 예정대로 `_aircraft_spec.md`에만 추가 — 애초 설계한
  "공용/기체고유 2단 분리"가 실제로 작동함을 확인(`_notation_common.md`
  "일반화 확인 이력" 절에 기록).
- `docs/mission_reports/README.md`에 이 사례를 예시로 추가.
- 다음 작업: 여전히 git 미커밋. 향후 다른 기체/시나리오도 같은 절차(기체
  스펙 먼저 확인 → 필요시 공용 표기법 확장 → 시나리오 리포트 작성)로 진행.

### 2026-08-02 — [claude] runscript 조건/명령을 JSBSim 프로퍼티 경로 대신 수식 기호로 전환

- 사용자 지적: 조건/명령 열이 여전히 `sim-time-sec`, `mission-state` 같은 실제
  XML 프로퍼티명을 그대로 쓰고 있어 읽기 어려움 — 기호를 따로 정의하고
  (예: `sim-time-sec` → `t_sim`, 단위 s는 별도 표기) 조건식을 `t_sim > 1`처럼
  수식으로 쓰는 게 낫다는 제안. 채택.
- `docs/mission_reports/_notation_common.md` 신규 작성 — 모든 기체가 공유하는
  초기조건 기호(V₀/Lat/Lon/h₀/h_terr/φ₀/θ₀/ψ₀)와 시뮬레이션 제어 기호
  (t_sim/k_frame/s_mis/trim/term/t_trig)를 JSBSim 프로퍼티 경로·단위·설명과
  함께 표로 정의.
- `_aircraft_spec_template.md`와 `F450/_aircraft_spec.md`에 "표기법(기체
  고유)" 절을 추가 — F450의 FCS/자동조종 프로퍼티 기호(δ_thr/δ_ail/δ_ele/
  δ_rud/SCAS/m_ap/N_sp/E_sp/h_sp/ψ_sp/ref_alt/e_N/e_E/e_h/h_AGL/ḣ/v_N/v_E/rpm_i)
  정의.
- F450 2.0/1.2 시나리오 리포트와 `_scenario_template.md`의 초기조건 표,
  좌표계 확인 절, runscript 이벤트표, 3장 분석 표·본문을 전부 이 기호로
  재작성. 부수적으로 1.2 리포트의 오차수렴 게이트를 "8개 부등식"으로 잘못
  세던 것을 재검산해 "6개 범위조건(개별 부등식 12개)"으로 정정하고, `Conv`
  라는 이름의 술어로 한 번만 정의해 표에서는 그 이름만 참조하도록 정리.
- `docs/mission_reports/README.md` 규칙 5번으로 이 표기법 컨벤션(공용/기체
  고유 기호 분리, 글머리 기호, Conv 같은 명명된 술어, 부기 프로퍼티 생략)을
  명문화.
- 다음 작업: 여전히 git 미커밋(bash 도구 장애 지속). 향후 다른 기체
  리포트를 쓸 때도 이 표기법 체계를 그대로 재사용할 것.

### 2026-08-02 — [claude] F450 초기조건 좌표계 검증 + runscript 조건 표기 기호화

- 사용자 요청 2건 처리: (1) 미션 리포트 "초기조건" 절에 좌표계 확인, (2) runscript
  이벤트표의 JSBSim 연산자(ge/le/gt/eq)를 부등호/등호 기호(≥/≤/>/=)로 표기.
- 좌표계 검증 중 새 결함을 발견함: `1.0__ground_park_init.xml`(2.0 시나리오가
  사용)이 `altitude`를 `elevation`과 같은 값(285.2111 M)으로 채워 "지면 주기"를
  표현하려 했으나, JSBSim 1.2.4가 `initialize/altitude`를 AGL로 해석한다는
  기존 규칙(lessons_learned 1절) 때문에 실제로는 h-agl-ft=935.7 ft(285 m
  상공)에서 스폰됨 — 콘솔 로그(`2.0__nominal_mission_profile` 실행 첫 notify)로
  확인. `1.1__ground_park_heading0_init.xml`(altitude=0.0)은 문제없음(첫
  notify부터 h-agl-ft=-0.000000). 이 결함은 2.0 시나리오의 주된 실패 원인
  (ap/mode 미설정)과는 별개이며, do_simple_trim이 곧바로 지면에 재배치해 최종
  실패에 결정적 영향을 준 것은 아니지만 향후 재사용 시 반드시 고쳐야 할
  잠재적 함정으로 기록.
- 갱신 파일: `docs/mission_reports/F450/2.0__nominal_mission_profile.md`,
  `docs/mission_reports/F450/1.2__ten_meter_box_hover_land.md`(각각 "좌표계
  확인" 절 신설 + 이벤트표 기호화), `docs/mission_reports/_scenario_template.md`
  (좌표계 확인 체크리스트 + 기호 표기 컨벤션 추가), `reference/docs/lessons_learned.md`
  1절(추가 발견 서술), `docs/coordinate_frame_checklist.md`(반례 항목 추가).
- 다음 작업: `1.0__ground_park_init.xml`의 `altitude`를 0.0으로 수정하는 건
  아직 미실행(문서화만 완료, 실제 XML 수정은 향후 작업으로 남김 — 이 세션은
  문서화 요청이었으므로 원본 스크립트는 건드리지 않음). git 커밋/푸시도 여전히
  bash 도구 장애로 미완료.
- (같은 세션, 후속 요청) runscript 이벤트표에서 `<set>` 명령이 2개 이상인 셀은
  `• 항목<br>• 항목` 글머리 기호로 항목별로 줄을 나누도록 재포맷(단일 명령
  셀은 그대로 유지). `simulation/next-event-time`(재알림 타이머 갱신용 부기
  프로퍼티)은 미션 로직과 무관해 표에서 생략하고 그 사실을 표 위에 명시.
  `_scenario_template.md`에도 이 컨벤션(글머리 기호 + next-event-time 생략
  규칙)을 반영해 향후 리포트가 동일하게 따르도록 함.

### 2026-08-02 — [claude] 미션 리포트 컨벤션을 기체제원/시나리오 2단 구조로 세분화

- 사용자가 문서화 챕터 순서를 구체적으로 지정함: (1) 기체 제원(JSBSim
  Metrics/Aerodynamics/Mass_balance 등 서브파일에서 직접 정리) → (2) 초기조건
  (표) → (3) runscript 이벤트별 조건/명령(표) → (4) 분석(미션이 제대로
  작동했는지, 안 됐다면 원인) → (5) 결론. 기존의 단일 `_template.md`(메타데이터/
  미션개요/결과요약표/해석 뭉뚱그림)로는 이 구조를 만족하지 못해 즉시 재설계.
- 템플릿을 2단으로 분리: `_aircraft_spec_template.md`(기체 1개당 1회 —
  Metrics/Mass/Propulsion/Aero/Gear/자동조종 특이사항) + `_scenario_template.md`
  (init+runscript 조합마다 1회 — 초기조건 표 → runscript 이벤트표 → 분석 →
  결론 → 산출물경로 → 한계 → PPT 매핑). 기체 제원을 시나리오 파일마다 반복
  기술하지 않기 위함. 옛 `_template.md`는 두 템플릿을 가리키는 안내 스텁으로
  대체.
- `docs/mission_reports/F450/_aircraft_spec.md`를 신규 작성 — `jsbsim/aircraft/
  F450/{Metrics,Mass,Propulsion,Aero,Gear}.xml`을 직접 읽어 실제 수치로 채움
  (WingArea 0.016129 m², Empty Weight 1.4kg, DJI E305/9450 모터×4 위치/사양,
  qbar-area 스케일링 정상 확인, F450AP 4단 체인과 `ap/mode` 덮어쓰기 함정 요약).
- 기존 F450 시나리오 리포트 2건을 새 구조로 전면 재작성:
  `docs/mission_reports/F450/2.0__nominal_mission_profile.md`(실패 사례),
  `docs/mission_reports/F450/1.2__ten_meter_box_hover_land.md`(성공 사례).
  두 파일 모두 `jsbsim_workflow/scripts/F450/{initial_condition,runscript}/*.xml`
  원본을 다시 읽어 초기조건 표와 이벤트표를 원문 그대로 재구성함(요약에 의존한
  재구성이 아니라 XML 원문 대조). 1.2는 mission-state 0~20 전체 22개 이벤트를
  표로 정리(오차수렴 게이트 조건 포함).
- `docs/mission_reports/README.md`를 2단 구조/PPT 5-챕터 구조 설명으로 갱신.
- 다음 작업: 이 문서들을 git에 커밋/푸시(아직 안 함). PPT 실물 생성은 여전히
  bash 도구 장애로 보류 중.

### 2026-08-02 — [claude] 미션 리포트 컨벤션(`docs/mission_reports/`) 신설 + PPT 파이프라인 설계

- 사용자가 매 미션 실행마다 PPT까지 만들어 저장해두고 싶어하며, 기체별로
  구성하고 init/runscript 조합별로 PPT 구역을 나누자고 제안. 토큰 비용이 크면
  문서화만 먼저 하고 PPT화는 나중으로 미뤄도 된다고 대안도 제시.
- 사용자가 `jsbsim ppt 템플릿.pptx`를 업로드했으나, 이 세션 내내 bash가
  막혀 있어(UNC 마운트 실패, 반복 확인됨) pptx 스킬 전체(markitdown,
  pptxgenjs, LibreOffice)를 실행할 수 없어 이번에도 열어보지 못함 — PPT 실물
  생성은 이번 세션에서 원천적으로 불가능(토큰 비용 문제가 아니라 도구 자체가
  막힘).
- 이에 사용자가 제시한 대안(문서화 먼저, PPT화는 나중)을 채택해
  `docs/mission_reports/` 컨벤션을 신설함: 기체별 폴더, init/runscript 조합별
  파일 1개, 표준 템플릿(`_template.md`: 메타데이터/미션개요/결과요약표/해석/
  산출물경로/한계/**PPT 슬라이드 매핑**)을 매번 그대로 채워 쌓아두고, bash가
  복구되면 "PPT 슬라이드 매핑" 섹션들을 그대로 슬라이드 내용으로 써서 기체당
  deck 1개로 일괄 생성하는 방식.
- 기존 F450 리포트 2건(성공/실패 사례)을 이 컨벤션으로 이전:
  `docs/mission_reports/F450/1.2__ten_meter_box_hover_land.md`,
  `docs/mission_reports/F450/2.0__nominal_mission_profile.md`. 이전 위치의
  `docs/F450_1.2_box_hover_land_report.md`,
  `docs/F450_mission_ppt_outline.md`는 새 위치를 가리키는 스텁으로 대체.
- **사용자 확인 필요**: 업로드된 pptx 템플릿은 대화의 임시 업로드 폴더에 있어
  세션이 끝나면 사라질 수 있음. `docs/mission_reports/_template/jsbsim_ppt_template.pptx`
  경로로 evtol-6dof 안에 직접 저장해 둘 것을 요청함(Claude는 바이너리 파일을
  직접 복사할 도구가 없어 사용자가 수동으로 저장해야 함).

### 2026-08-02 — [claude] F450 실체 모델 미션 실행-분석-문서화 파이프라인 1회 시연

- 사용자가 F450 실체 모델(이제 evtol-6dof에 직접 마운트되어 접근 가능해짐)로
  실행→분석→문서화→PPT 전체 파이프라인을 한 번 시연해보자고 요청.
- 1차 시도: `scripts/F450/runscript/2.0__nominal_mission_profile_run.xml` 실행 —
  종료코드 정상이었으나 **실제로는 전혀 이륙하지 않음**을 콘솔 notify 로그로
  직접 확인(h-agl-ft 32초 내내 지상고 고정, propeller-rpm 4개 전부 0). 원인은
  F450AP.xml이 `fcs/throttle-cmd-norm`/`ScasEngage` 등을 `ap/mode` 기반 SWITCH로
  매 프레임 재계산하는데, 이 런스크립트는 `ap/mode`를 한 번도 안 쓰고 저
  프로퍼티들을 직접 `<set>`해서 다음 프레임에 자동조종이 덮어써버림. 종료코드만
  보면 알 수 없는 "조용한 실패" — `reference/docs/lessons_learned.md` 8절에
  근거와 함께 기록.
- 2차 시도: `scripts/F450/runscript/1.2__ten_meter_box_hover_land_run.xml`
  (+ `1.1__ground_park_heading0_init.xml`, heading 0)로 전환 — `ap/mode=3`을
  정식으로 쓰는, 과거 22회 실행 이력이 있는 성숙한 미션. **완전 성공**: 이륙
  t≈2.1s, 목표고도(10m) 오버슈트 전혀 없이 단조 수렴, 8구간 박스 패턴 t≈204s에
  완주, 착륙 t=205.12s에 3개 기어 동시 접지, 최종 위치오차 출발점 대비 약 1.8mm.
  콘솔 로그를 직접 읽어(jsbsim_workflow가 evtol-6dof 마운트를 통해 접근 가능해진
  덕분에 CSV/콘솔을 사용자가 붙여넣지 않아도 직접 분석 가능했음) 정량 분석 후
  `docs/F450_1.2_box_hover_land_report.md`로 문서화 완료.
- **PPT 단계는 이번 세션에서 완료 불가**: 이 세션 내내 있었던 bash 도구 버그
  (UNC 경로 마운트 실패)가 여전히 살아있어 pptx 스킬(markitdown, pptxgenjs,
  LibreOffice 변환)을 전혀 실행할 수 없음. 사용자가 참고로 올린 pptx도 열어보지
  못함. 다음 세션(버그가 세션 한정일 가능성)이나 bash 복구 후 마무리 필요.
- **후속 조치 제안**: (1) `2.0__nominal_mission_profile_run.xml`을 `ap/mode` 기반으로
  재작성하거나 사용 중단 처리, (2) CSV 50Hz 전체를 pandas 등으로 정식 집계하는
  건 Codex 몫으로 남김(이번엔 콘솔 1초 notify 표본만으로 분석, 근거는 보고서에
  명시).

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
