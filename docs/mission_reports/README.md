# 미션 리포트 컨벤션

기체별 실행 결과를 매번 일관된 형식으로 남기기 위한 규칙. PPT 실물 생성은
bash 도구가 막혀 있는 동안은 못 하지만(아래 참고), 이 컨벤션대로 문서를
쌓아두면 나중에 한 번에 변환하는 작업으로 대체할 수 있다.

## 디렉토리 구조

```
docs/mission_reports/
  README.md                      (이 파일)
  _notation_common.md            (모든 기체 공용 표기법 — t_sim, s_mis 등)
  _aircraft_spec_template.md     (기체 제원 문서 템플릿 — 기체당 1회)
  _scenario_template.md          (시나리오 문서 템플릿 — init+runscript 조합당 1회)
  _template/
    jsbsim_ppt_template.pptx     (사용자 제공 PPT 템플릿 — 아래 "PPT 템플릿 보관" 참고)
  <Aircraft>/
    _aircraft_spec.md            (기체 제원 — 그 기체의 모든 시나리오가 공유)
    <runscript_scenario>.md      (시나리오 1개 = 파일 1개)
```

예: `docs/mission_reports/F450/_aircraft_spec.md`,
`docs/mission_reports/F450/1.2__ten_meter_box_hover_land.md`,
`docs/mission_reports/F450/2.0__nominal_mission_profile.md`,
`docs/mission_reports/c172x_4x75kg_cg_aligned_ksfo28r_landing/_aircraft_spec.md`,
`docs/mission_reports/c172x_4x75kg_cg_aligned_ksfo28r_landing/5.16__ksfo28r_runway_return_circular_landing.md`
(멀티콥터 F450과 고정익 C172x 두 기종에서 컨벤션이 그대로 일반화됨을 확인한
사례 — `_notation_common.md`의 "일반화 확인 이력" 참고)

## PPT 5-챕터 구조 (사용자 지정)

기체당 PPT deck 1개는 아래 순서로 구성한다.

1. **기체 제원** — `_aircraft_spec.md` 내용 그대로(Metrics/Mass/Propulsion/
   Aero/Gear를 JSBSim 서브파일에서 직접 읽어 표로 정리)
2. **초기조건** (표) — 시나리오 문서 1장
3. **Runscript 이벤트별 조건/명령** (표) — 시나리오 문서 2장
4. **분석** — 미션이 의도대로 작동했는지, 안 됐다면 무엇이 문제였는지
5. **결론**

기체 제원(1번)은 그 기체의 시나리오 전체가 공유하는 공통 챕터이고, 2~5번은
시나리오(=init+runscript 조합)마다 반복된다. 즉 기체 1개, 시나리오 2개면
deck 구조는 "기체제원 → [시나리오A: 초기조건/runscript/분석/결론] →
[시나리오B: 초기조건/runscript/분석/결론]"이 된다.

## 규칙

1. **기체별로 폴더를 나누고, `_aircraft_spec.md`(기체 제원, 공유)와
   init/runscript 조합(=시나리오)별 파일로 나눈다.** 같은 기체의 기체 제원을
   시나리오 파일마다 반복 기술하지 않는다.
2. **기체 제원은 `_aircraft_spec_template.md`, 시나리오는
   `_scenario_template.md` 구조를 그대로 따른다** — 시나리오 문서는
   초기조건 표 → runscript 이벤트표 → 분석 → 결론 → 산출물 경로 → 한계 →
   PPT 슬라이드 매핑까지 한 파일에 담는다.
3. **실패한 실행도 반드시 기록한다.** 성공만 남기면 나중에 왜 그 방식을 버렸는지
   알 수 없다(F450 2.0 사례 참고 — 조용한 실패였는데 기록 안 했으면 똑같은
   실수를 반복했을 것).
4. **정량 수치는 콘솔/CSV/기체 XML에서 실제로 읽은 값만 적는다.** 추정치는
   "추정"이라고 표시.
5. **초기조건/runscript 표에는 JSBSim 프로퍼티 경로를 그대로 쓰지 않고 기호로
   바꿔 수식처럼 쓴다.** 공용 기호는 `_notation_common.md`, 기체 고유 기호는
   `<Aircraft>/_aircraft_spec.md`의 "표기법" 절에 정의한다(예:
   `simulation/sim-time-sec ge 3.0` → `t_sim ≥ 3.0`). 한 이벤트에 `<set>`
   명령이 2개 이상이면 `• 항목1<br>• 항목2` 글머리 기호로 줄을 나누고,
   반복되는 범위조건은 이름 붙여(`Conv ≡ …`) 한 번만 정의한다. 미션 로직과
   무관한 부기 프로퍼티(`simulation/next-event-time` 등)는 표에서 생략하고
   생략 사실을 명시한다.
6. **"분석" 절은 텍스트 서술만이 아니라 CSV 그래프 기반으로 진행한다.**
   `jsbsim_workflow/ploting/<Aircraft>/<Run ID>/raw_time_series/`에 사전
   렌더링된 개별 프로퍼티 PNG가 있으면 관련 항목끼리 묶어서(cmd vs 실제
   위치, setpoint vs 실제, 미션상태 마스터 타임라인, 착지/WOW, 서브시스템
   게이트의 중간신호 vs 최종출력, 거리/궤적) 직접 열어 대조하고 근거로 쓴다.
   그래프가 없으면(플로팅 파이프라인 미실행) 그 사실을 한계 절에 명시하고
   텍스트/콘솔 근거로 대체한다 — 근거 없이 "그래프로 확인했다"고 쓰지 않는다.
   상세 그룹 가이드는 `_scenario_template.md` 3절 참고.

## PPT 실물 생성 — 현재 상태

이 세션은 bash 도구가 UNC 경로 마운트 실패로 막혀 있어서 pptx 스킬(markitdown,
pptxgenjs, LibreOffice 변환)을 전혀 실행할 수 없다. 그래서 지금은 이 컨벤션대로
마크다운 리포트만 쌓아두고, PPT 실물 생성은 **bash가 복구된 시점에 한 번에
일괄 처리**하는 방식으로 미룬다. 그 시점이 되면:

1. `_template/jsbsim_ppt_template.pptx`를 `thumbnail.py`로 분석해 슬라이드
   레이아웃을 파악
2. `docs/mission_reports/<Aircraft>/*.md`의 "PPT 슬라이드 매핑" 섹션을 그대로
   슬라이드 내용으로 사용해, 기체 1개당 deck 1개(내부에 시나리오별 섹션)로 생성
3. QA(콘텐츠/파일/시각) 후 전달

## PPT 템플릿 보관

업로드된 `jsbsim ppt 템플릿.pptx`는 대화 세션의 임시 업로드 폴더에 있어서 이
세션이 끝나면 사라질 수 있다. **`docs/mission_reports/_template/jsbsim_ppt_template.pptx`
경로로 evtol-6dof 안에 직접 저장해 두면** 나중에 bash가 복구됐을 때 바로 쓸 수
있다(Claude는 바이너리 파일을 직접 복사할 수 있는 도구가 없어서, 이 저장은
사용자가 직접 해줘야 함).
