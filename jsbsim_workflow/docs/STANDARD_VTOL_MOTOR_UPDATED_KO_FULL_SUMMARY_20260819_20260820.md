# standard_vtol_demo_motor_updated_ko — 종합 진행 정리 (2026-08-19 ~ 2026-08-20)

- 작성일: 2026-08-20
- 목적: 8/19~8/20 이틀간 `standard_vtol_demo_motor_updated_ko` 기체를 PX4 SITL/JSBSim에서 실제로 비행 가능하게 만드는 작업 전체를 발표(PPT) 준비용으로 한 문서에 종합 정리
- 대상 기체: 20.0kg / wingarea 0.572㎡ VTOL(V-tail), CAD 실측 CG(nose 기준 0.649m), DATCOM 공력 데이터
- 최종 목표: 멀티콥터 이착륙 + 고정익 순항 전환이 모두 되는 VTOL을 PX4 SITL에서 실비행 검증

---

## 0. 한눈에 보는 결론

| | 상태 |
|---|---|
| 멀티콥터 이착륙(호버/착륙) | ✅ 완전히 안정적 |
| PX4 제어 배선(에일러론/승강타/러더/pusher/airspeed) | ✅ 전부 정상 작동 확인 |
| 좌표계 일관성(CAD 기준 CG 반영) | ✅ 버그 발견 및 수정 완료(AERORP) |
| 고받음각(수직상승) 발산 | ✅ 해결(alpha 게이트) |
| 고정익(FW) 상태 도달 | ✅ 도달은 함(vtol_state=4 확인, 최고 25m/s) |
| 고정익 **유지** 비행 | ❌ **아직 안 됨** — 전환 후 2~3초 내 quad-chute로 MC 강제복귀 |
| quad-chute 원인 | ✅ 규명 완료(전환 중 고도손실 20m 초과, 원인은 승강타 공력계수 부재로 인한 양력 부족) |
| 근본 해결책 | ⏳ V-tail 러더베이터 실측 공력데이터 확보(사용자 별도 진행 중) |

---

## 1. 배경 — 8/19 이전 상태

이 기체는 원래 "데모"로 시작해(CG가 원점(0,0,0)인 단순 스캐폴드), 이후 사용자가 CAD 실측을 받아 CG를 nose 기준 649mm 지점으로 확정하고, 실측 프로펠러 pull-test 데이터를 반영해 발전시킨 모델. 8/19 시작 시점에는 PX4/JSBSim 연동이 전혀 검증되지 않은 상태(순수 JSBSim standalone 테스트만 있었음)였고, 사용자가 이 XML을 첨부하며 "PX4/JSBSim 실행 가능성 검토"를 요청하며 작업이 시작됨.

---

## 2. 8/19 — PX4 최초 연결과 고정익 전환 문제 발견

| 시각 | 작업 | 결과 |
|---|---|---|
| 10:21 | 첨부 XML PX4/JSBSim 실행 가능성 검토 | JSBSim 단독 로딩 실패(`FGTable: missing lookup axis`) |
| 10:31 | 공력 table 형식 보정 | `lookup="row"+"table"` 14개를 JSBSim 1.2.4 호환 `row+column`으로 변환. 이후 Floating point exception 발생 |
| 10:38 | 0속도 보호 보정 | `velocities/vt-fps` 직접 분모 사용 항(CLq/CLadot/Cmq/Cmadot/CYp/Clp/Clr/Cnp/Cnr)을 `aero/ci2vel`·`aero/bi2vel`로 교체. FPE 해소, JSBSim 단독 실행 rc=0 |
| 10:52 | 좌표 절대좌표 보정 | 모터/기어 좌표가 CG 기준값처럼 들어간 걸 절대좌표로 정정(front=1.249, rear=0.049, lift motor -0.105/1.404, pusher 2.249). **14kg 후보는 크래시 재현되어 20.0kg로 롤백** |
| 11:02 | PX4 arm-hover-land 최초 검증 | 성공(NaN/크래시 없음). 다만 목표고도 2.5m 대비 실제 최대고도 약 1.03m |
| 11:08, 11:13 | 실행 매뉴얼(RUNBOOK) 문서화 | 터미널 직접 명령, QGC 버튼/콘솔 입력 방법 정리 |
| 11:33 | 사용자 QGC 실비행 로그 분석 | **20m 고도 호버 + 정밀 재배치(DO_REPOSITION) 성공**(NaN 0, dropout 없음). 다만 `nav_state=ORBIT`으로 종료(Land/Disarm 없이 끝남) |
| 11:40 | F450 스타일 모듈화 | 단일 XML → `Metrics/Mass/Gear/Effectors/FlightControl/ExternalReactions/Aero.xml`로 분리. 원본은 `Monolithic.xml`로 보존 |
| 14:25 | **고정익 전환 문제 원인 진단** | PX4 airframe이 `rc.mc_defaults`(순수 멀티콥터)로 등록돼 VTOL 전환 로직 자체가 비활성. bridge가 조종면(aileron/elevator/rudder) 명령을 JSBSim에 전달하지 않음. airspeed 센서 경로도 없음 |
| 14:48 | 성공 사례(`standard_vtol_demo.xml`, 이하 "A")와 비교 분석 | A는 airframe/bridge가 정상 VTOL로 구성돼있고 elevator/rudder 공력 미분계수(CLde/Cmde/Cndr)도 있음을 확인. 우리 기체는 이 셋 다 없음 |

**8/19 종료 시점 상태**: 멀티콥터 이착륙은 검증됐으나, 고정익 전환은 구조적으로 불가능한 상태(원인은 진단됐으나 수정은 다음 세션으로 이관).

---

## 3. 8/20 — 제어 배선 구현, 크래시 원인 규명·수정, 고정익 전환 근본 원인 규명

### 3.1 PX4 VTOL 제어 배선 구현 (오전)

8/19에 진단된 3가지(airframe 미등록/bridge 조종면 누락/airspeed 누락)를 실제로 구현:

- airframe: `rc.mc_defaults`→`rc.vtol_defaults`, `CA_AIRFRAME 0`→`2`, `CA_ROTOR_COUNT 4`→`5`(pusher를 rotor4로 편입), `CA_SV_CS_COUNT 3`(aileron=15/elevator=3/rudder=4 타입 코드, PX4 표준 예제로 확정)
- bridge config: `<airspeed>` 센서 블록 추가, aileron/elevator/rudder 채널 3개 추가(JSBSim이 기대하는 정확한 프로퍼티명과 대조 확인)
- pusher 로터 좌표(`CA_ROTOR4_PX -1.6`): 기존 4개 로터의 검증된 좌표 변환식(`PX4_PX = CG_x - motor_x`)을 역산해 동일 적용
- **검증**: DONT_RUN 빌드 통과, 30초 headless 실행 NaN/크래시 없음. 기체 XML(공력/질량/모터)은 전혀 수정하지 않음(사용자 지시)

### 3.2 첫 실비행 시도 — 크래시, 원인은 alpha 특이점

arm→takeoff→transition→land 시퀀스 최초 실행 → **지면 충돌 + NaN 발산**. JSBSim CSV 정밀분석 결과:

- 전환 명령 이전, `commander takeoff`로 **수직 상승하는 순간부터 이미 `alpha(받음각)`가 ±90도 부근에서 불안정**(전진속도≈0인 순수 수직상승에서 `alpha=atan2(w,u)`가 갖는 JSBSim 표준 특이점)
- 문제는 DATCOM 공력 테이블이 **-24~11도 구간만 정의**돼 있어, 이 범위 밖에서는 JSBSim이 경계값을 그대로 반환 → 실제로는 다른 비행상태의 큰 계수가 엉뚱한 상황에 적용되며 발산

**대응(alpha_validity_gate 신설)**: alpha가 -24~11도 밖일 때 공력 계수를 0으로 부드럽게 억제하는 게이트 함수를 추가해 기존 16개 계수 함수 전부에 곱셈항으로 삽입(DATCOM 원본 수치는 무변경). 검토했던 대안: (1) A처럼 -180~180도 전체 flat-plate 근사 재작성 — 정확하지만 작업량 큼, (2) F450 순정처럼 계수 상수 0 고정 — 순항 양력도 사라져 부적합, (3) 총속도 기준 게이팅 — 기각(A가 겪었던 "no lift during transition" 재발 위험). **재검증 결과: 순수 상승 구간은 안정화됐으나, 전환 시도 시 여전히 발산**(다른 메커니즘).

### 3.3 좌표 버그 발견 — AERORP (전환 시 발산의 진짜 원인)

사용자 요청("모터/기타 부위 좌표가 CAD 기준 CG 변경에 맞춰 일관되게 갱신됐는지 확인")으로 전체 좌표를 재점검 → **`Metrics.xml`의 `AERORP`(공력 기준점)가 CG를 원점→nose 기준 649mm로 옮길 때 함께 안 옮겨지고 옛값(0,0,0)에 방치**된 것을 발견.

- JSBSim 소스(`FGAerodynamics.cpp:247-288`, `M = r×F`)로 AERORP가 실제 모멘트 계산에 쓰이는 물리량임을 확인
- CG만 이동하고 AERORP를 안 옮기면서, 양력/항력이 조금이라도 생기는 순간(=alpha 게이트가 열리는 순간) 0.649m짜리 **허위 피칭모멘트**가 매 스텝 자동으로 더해지고 있었음
- **수정**: AERORP/VRP를 CG와 동일한 (0.649,0,0)으로, EYEPOINT는 원래 오프셋 관계를 보존해 (0.799,0,0)으로 변경
- **재검증 결과: NaN 완전히 사라짐.** arm→takeoff→transition→land 전체 시퀀스가 지면충돌 없이 정상 착지까지 완료(최종 정지상태가 초기 지상정지상태와 정확히 일치)

### 3.4 정상 절차로 재현 — 최초로 FW 상태 도달

사용자 지적("정지 호버에서 바로 전환 명령은 절차 자체가 잘못됐다, pusher로 먼저 가속해야 정상")에 따라, `DO_REPOSITION`으로 실제 전방 목적지를 준 정상 절차로 pymavlink 스크립트를 새로 작성해 재검증:

- Groundspeed가 실제로 5→24m/s까지 가속됨을 확인
- `vtol_state`가 1(TRANSITION_TO_FW)→**4(FW)**로 실제 전이(세션 최초로 진짜 고정익 상태 도달)
- 직후 자세 이탈로 quad-chute 발동, MC로 강제복귀 — 그러나 **NaN 없이 회복 후 정상 착륙**

### 3.5 A(레퍼런스) vs B(현재 모델) 전체 비교 문서화

`STANDARD_VTOL_MOTOR_UPDATED_KO_VS_DEMO_CHANGELOG_20260820.md` 작성. 항목별(형상/질량/기어/추진계/공력/조종계/PX4 설정) 근거(실측/DATCOM/추정/상속)를 표로 정리하며 2가지 핵심 발견:

1. **승강타/러더 공력 모멘트 계수가 전혀 없음**(`Cmde`/`Cndr` 상당 항목 부재, grep으로 전수 확인) — 조종면은 기계적으로 정상 작동하지만 공력 응답이 0. **원인: V-tail(러더베이터) 기체라 AVL/DATCOM이 러더베이터 혼합 효과를 산출 못 함(사용자 확인, 별도 검토 중)**
2. **관성모멘트(ixx/iyy/izz)가 레퍼런스 A와 완전히 동일**(질량·형상이 다 다른데 우연히 일치할 확률 낮음) — **원인: Weight & Balance 확인 작업 진행 중, 현재 CG x좌표만 확정값이고 나머지는 임의값(사용자 확인)**

두 항목 모두 "미발견 버그"가 아니라 사용자가 이미 인지하고 별도로 진행 중인 사안으로 문서에 명시.

### 3.6 정상 시나리오 풀세트 실행 (시동~착륙 8단계)

사용자 요청으로 시동/이륙/상승/천이/미션(선회 2회)/RTL/역천이/착륙 전 구간을 pymavlink 스크립트로 실행:

| 단계 | 결과 |
|---|---|
| 시동/이륙/상승 | 정상(37m 도달, 28초) |
| 천이 | FW 도달했으나 2.6초만 유지, quad-chute로 MC 복귀 |
| 미션 선회 2회 | FW 복귀 실패로 MC 상태로 비행(예상된 동작) |
| RTL | 정상 |
| 역천이 | 이미 MC라 사실상 no-op |
| 착륙/disarm | **매우 매끄러운 단조 하강, 완전 정상 disarm 확인** |

**NaN 0건, 전체 시퀀스가 크래시 없이 완주.**

### 3.7 quad-chute 정확한 원인 규명 (자세각이 아니라 고도손실)

사용자 요청("고정익 비행 안되는 이유 확인하고 해결할 방법 제시")에 따라 PX4 소스(`vtol_type.cpp`)를 직접 분석:

- **가설 기각**: 자세각(pitch/roll) 임계값 체크(`VT_FW_QC_P`/`VT_FW_QC_R`)는 **기본값 0(비활성)**이고 이 프로젝트에서 설정한 적이 없음 — 지금까지 관측한 theta -30~+56도 진동은 quad-chute의 "결과"이지 "원인"이 아니었음
- **진짜 트리거**: `isFrontTransitionAltitudeLoss()` — `VT_QC_T_ALT_LOSS`(기본 20m), 전환 중/완료 후 5초 이내 고도손실이 20m를 넘으면 발동. **CSV 데이터로 확인: 전환 진입 직후 28.8m→0.6m까지 3.6초 만에 28.2m 하강** — 기준 초과, 타이밍도 일치
- **정량적 원인 분석**: `Cm_base` 테이블의 무승강타 자연 트림점은 alpha≈4.5°(CL≈0.91). 이 CL로 20kg/0.572㎡ 기체가 수평비행하려면 필요속도 **V≈24.8m/s**. 전환 가속 구간(15~20m/s대)에서는 이 자연 트림 CL로 양력이 부족해 가라앉는데, **Cmde가 없어 PX4가 받음각을 능동적으로 키워 보정할 수단이 없음**

### 3.8 해결 시도 A(임시 공력계수) + B(전환 가속 강화)

- **A**: 레퍼런스 A의 계수를 "[임시 placeholder]"로 명시해 그대로 차용 — `CLde=-0.35`, `Cmde=+1.10`, `Cndr=+0.09`
- **B**: `VT_F_TRANS_THR` 0.75→1.0(전환 중 최대 pusher 추력)
- **재검증 결과**: 최고 groundspeed 24.33→25.17m/s로 소폭 개선됐으나 **quad-chute는 동일 메커니즘으로 재발**(고도손실이 오히려 더 심함: 28.8→0.6m였던 것이 28.7→0.2→-5.9m). NaN 0건, 착륙은 여전히 정상
- **추정 원인**: A(레퍼런스)는 wingarea 0.953㎡/23.6kg, 우리 기체는 0.572㎡/20.0kg로 날개하중이 훨씬 큼 — A의 계수 크기를 그대로 가져온 것만으로는 부족한 것으로 판단

### 3.9 실제 QGC 비행으로 최종 확인

사용자가 직접 QGC로 비행 시도(`05_27_49.ulg`) → **소스 분석으로 예측한 메시지가 실제 로그와 글자 그대로 일치**:

```
0:01:35  CRITICAL: Quad-chute triggered due to loss of altitude during transition
```

이 세션은 quad-chute 이후 곧바로 개입하지 않고 계속 비행을 이어갔고, 결과적으로 상태가 계속 악화되며(Compass fault 반복, Airspeed invalid, "Autopilot disengaged → Descend") **JSBSim 물리 시뮬레이션 자체가 NaN으로 완전히 발산**함(해당 세션 CSV 18,067행이 NaN). QGC 화면의 고도 `-2147498.5m` 표시는 NaN이 정수로 잘못 변환된 쓰레기값이었음.

**대조**: 같은 quad-chute를 겪은 다른 3개 로그(`04_14_07`, `04_27_17`, `05_14_56.ulg`)는 quad-chute 직후 빠르게 RTL/착륙으로 개입해 전부 `Landing detected`→`Disarmed by landing`으로 정상 종료함. **quad-chute 자체는 PX4 안전장치가 설계대로 작동한 것**이며, 문제는 그 이후 방치 시 상태가 계속 악화될 수 있다는 점.

---

## 4. 종합 결론

### 4.1 해결된 것

1. JSBSim 1.2.4 호환성(테이블 형식, 0속도 보호)
2. PX4 VTOL 제어 배선 전체(airframe, bridge, 조종면 3채널, airspeed) — **완전 검증됨**
3. 좌표계 일관성 버그(AERORP) — **발산/크래시의 핵심 원인이었고, 수정으로 완전히 해결**
4. 고받음각(수직상승) 발산 — alpha 게이트로 해결
5. 멀티콥터 전체 비행 사이클(이착륙/RTL/착륙) — **완전히 안정적**

### 4.2 아직 해결 안 된 것 (근본 원인까지 규명됨)

**고정익 유지비행 실패 = quad-chute(전환 중 고도손실 20m 초과) = 승강타 공력 모멘트 계수 부재(Cmde) = V-tail 러더베이터를 AVL/DATCOM이 처리 못 하는 한계**

이 마지막 한 가지가 남은 유일한 핵심 이슈이며, 임시방편(A/B)으로는 해결이 안 되고 **정식 V-tail 공력데이터 확보**가 필요함(사용자 별도 진행 중, Weight & Balance 확정 작업과 함께).

### 4.3 우선순위

1. **V-tail 러더베이터 공력데이터 확보**(AVL 개별 곡면 모델링 또는 근사 계산) → Cmde/Cndr 정식값 반영 — 근본 해결
2. **Weight & Balance 확정**(관성모멘트 등) — 현재 CG x좌표만 확정
3. (참고) 정식 데이터 전 임시조치로 A 계수를 날개하중 비율로 스케일링한 재실험 여지 있음

---

## 5. 관련 문서 인덱스

| 문서 | 날짜 | 내용 |
|---|---|---|
| `STANDARD_VTOL_MOTOR_UPDATED_KO_PX4_REVIEW.md` | 8/19 | 최초 PX4 실행 가능성 검토 |
| `STANDARD_VTOL_TRANSITION_DIAGNOSIS_20260819.md` | 8/19 | 고정익 전환 불가 원인 최초 진단(airframe/bridge/airspeed) |
| `QGC_20M_HOVER_REPOSITION_LOG_ANALYSIS_20260819.md` | 8/19 | 20m 호버+재배치 QGC 실비행 로그 분석 |
| `STANDARD_VTOL_DEMO_COMPARISON_20260819.md` | 8/19 | 성공 모델(A) vs 신규 모델 1차 비교 |
| `STANDARD_VTOL_MOTOR_UPDATED_KO_VS_DEMO_CHANGELOG_20260820.md` | 8/20 | A vs B 전 항목 상세 비교(근거/문제/대안), 승강타·러더·관성모멘트 이슈 발견 |
| `STANDARD_VTOL_MOTOR_UPDATED_KO_QUADCHUTE_DIAGNOSIS_20260820.md` | 8/20 | quad-chute 원인 규명 상세(소스코드+정량계산+A/B실험+QGC실비행 검증) |
| **본 문서** | 8/20 | 8/19~8/20 전체 종합 타임라인 |

주요 코드 변경 git 커밋(jsbsim_workflow 저장소): `9f4c792`(제어배선), `1f16a6f`(alpha 게이트), `39aa989`(AERORP 수정), `6493bbe`(A+B 임시계수)
