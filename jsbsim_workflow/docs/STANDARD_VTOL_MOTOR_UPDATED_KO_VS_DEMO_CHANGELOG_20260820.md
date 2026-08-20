# standard_vtol_demo_motor_updated_ko vs standard_vtol_demo — 변경점/근거/문제/대안 종합 문서

- 작성일: 2026-08-20
- 비교 대상 A(레퍼런스, "성공 모델"): `/mnt/d/ProjectAirSim-jsbsim/core_sim/jsbsim/models/aircraft/standard_vtol_demo/standard_vtol_demo.xml` (ProjectAirSim/JSBSim 통합용, monolithic 단일 XML)
- 비교 대상 B(현재 작업 모델): `/home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/` (PX4/JSBSim bridge용, F450 스타일 모듈 분리: Metrics/Mass/Gear/ExternalReactions/Aero/FlightControl.xml)
- 참고: A는 ProjectAirSim 전용 시스템이라 PX4 airframe/bridge 설정 자체가 없음. PX4 쪽 비교는 PX4 표준 예제(`1040_gazebo-classic_standard_vtol`, `10043_sihsim_standard_vtol`)를 별도 기준으로 사용함.

## 0. 요약

두 모델은 같은 "standard_vtol_demo" 계보에서 갈라진 서로 다른 기체다. A는 AD3000 CAD 데이터를 반영해 발전한 5.0 wingarea/23.6kg 모델이고, B는 실측 CAD(nose 기준 CG 649mm)와 실측 프로펠러 pull-test 데이터를 반영한 0.572㎡/20.0kg 모델이다. 이번 세션(2026-08-19~20)에서 B를 실제 PX4 SITL로 비행 가능하게 만드는 과정에서 발견·수정한 것과, 아직 A에는 있지만 B에는 없는 것들을 아래에 정리한다.

---

## 1. 기체 형상 (Metrics.xml)

| 항목 | A(레퍼런스) | B(현재 모델) | 근거 | 비고 |
|---|---|---|---|---|
| wingarea | 0.953 m² | 0.572 m² | B는 이 세션 이전에 이미 확정된 값(CAD 실측으로 추정, 이번 세션에서 직접 검증하지 않음) | A는 자체 주석에 CAD STEP bbox 적분값이라고 명시(root chord 0.355→tip 0.275, half-span 1.546m, S=0.953㎡) |
| wingspan | 3.092 m | 3.000 m | 상동 | |
| chord | 0.308 m | 0.215 m | 상동 | |
| AERORP | (0,0,0) = CG | **(0,0,0) → (0.649,0,0)로 이번 세션에 수정** | JSBSim 소스 확인(`FGAerodynamics.cpp:247-288`, `M=r×F`)으로 AERORP가 실제 모멘트암에 쓰이는 물리량임을 확인 | **문제**: CAD 반영으로 CG를 원점→nose 기준 649mm로 옮길 때 AERORP를 안 옮겨서, 매 스텝 0.649m 허위 피칭모멘트가 발생 → 전환 시도 시 크래시의 핵심 원인이었음(2026-08-20 발견·수정) |
| VRP | (0,0,0) = CG | (0,0,0) → (0.649,0,0)로 수정 | 물리(EOM) 비관여, 시각화 전용(`FGAuxiliary.cpp` vLocationVRP) 프로퍼티임을 소스로 확인 | AERORP와 같은 이유로 동반 수정. 크래시와는 무관(참고용) |
| EYEPOINT | (0.15,0,-0.05) | (0.15,0,-0.05) → (0.799,0,-0.05)로 수정 | A의 "CG 대비 +0.15" 관계를 B의 새 프레임에서 보존 | 물리 비관여(시각화 전용). 원래 데모에서 이 오프셋 자체가 실측인지 placeholder인지는 불명확 — **미검증** |

**대안**: AERORP를 CG와 다른 실제 공력중심 위치로 별도 산정하는 방법도 있으나, 풍동/CFD 데이터가 없어 이번엔 A의 "AERORP=CG" 설계를 그대로 계승(모멘트암 0)하는 쪽을 선택함.

---

## 2. 질량/관성 (Mass.xml)

> **사용자 확인(2026-08-20)**: Weight & Balance 확인 작업이 진행 중이며, 현재 시점 기준 **CG의 x좌표(0.649m)만 실측 확정값이고 그 외(ixx/iyy/izz 포함)는 전부 임의값**임. 아래 "불명/발견된 문제"는 버그가 아니라 W&B 확정 전까지의 정상적인 중간 상태.

| 항목 | A | B | 근거 | 비고 |
|---|---|---|---|---|
| emptywt | 23.6 kg | 20.0 kg | 실측(사용자 CAD/부품 중량 확정치로 추정) | |
| ixx/iyy/izz | 10.7 / 8.0 / 18.5 kg·m² | 10.7 / 8.0 / 18.5 kg·m² (A와 완전히 동일) | **임의값 — 사용자가 W&B 확인 중이며 아직 미확정이라고 명시적으로 확인함(2026-08-20)** | A(레퍼런스)의 값이 그대로 남아있는 placeholder 상태. 버그 아님, W&B 확정 시 갱신 예정 |
| CG | (0,0,0) | (0.649, 0, 0) | **사용자 제공 CAD 실측(nose 기준 649mm) — 이 모델에서 유일하게 확정된 W&B 값** | 이번 세션 이전에 이미 반영됨 |

**대안**: W&B 확정 후 CAD 모델(STEP 파일)에서 관성모멘트를 직접 적분하거나, 실측 스윙테스트(bifilar pendulum 등)로 측정. AD3000 쪽에서는 STEP 파일 기반 커스텀 적분 파이프라인을 실제로 썼던 선례가 있음(MiniTalon 관련 8/17 작업 기록 참고).

**후속 작업 시 주의**: CG x 이외의 모든 질량 관련 값(관성모멘트, 필요 시 CG y/z)이 확정되기 전까지는 이 모델의 피치/롤/요 각가속도 응답(특히 quad-chute 발동 시점의 자세 발산 거동)을 정량적으로 신뢰하지 말 것 — 정성적 검증(제어 경로 동작 여부, 발산/NaN 여부)까지만 유효함.

---

## 3. 착륙기어 (Gear.xml)

| 항목 | A | B | 근거 | 비고 |
|---|---|---|---|---|
| front_foot 위치 | x=0.60 | x=1.249 | CAD 실측 반영(2026-08-19 10:52 보정, PROGRESS-20260819-1052-001) | "front"인데 CG(0.649)보다 x가 큼(더 후방) — A도 동일한 명명 관례(front_foot이 CG보다 후방)라 명명 자체는 A 상속, 물리값만 CAD 반영 |
| rear_left/right_foot 위치 | x=-0.60 | x=0.049 | 상동 | |
| spring/damping 계수 | front 600/20, rear 300/12 (LBS/FT, LBS/FT/SEC) | **front 600/20, rear 300/12 (A와 완전히 동일)** | **A 상속, CAD/실측 아님 — placeholder로 추정** | 착지 충격 특성이 실제 기체와 다를 수 있음. 다만 이번 세션 크래시들과는 직접 관련 없음(착지 자체는 정상 동작 확인됨) |

---

## 4. 추진계 (ExternalReactions.xml)

| 항목 | A | B | 근거 |
|---|---|---|---|
| lift 모터 추력 테이블 | 0→37.8 lbf @ throttle 1.0 (4점 보간) | 0→24.5 lbf @ throttle 1.0 (23점 보간, 세밀함) | **B는 실측 데이터**. AD3000_generate_aircraft.py 계열 파이프라인에서 Hobbywing V6212 계열 실측 pull-test 데이터를 반영한 것으로 추정(2026-08-11/12 작업) |
| pusher 추력 테이블 | throttle table × 전진속도 감쇠 테이블(advance ratio 근사) | throttle table만 있음(전진속도 감쇠 없음), **B 파일 자체 주석에 명시**: *"Hobbywing V6215 210KV + VSC 22.1x7.4의 46V/12S 정지 인장시험 추력 데이터... 검증된 유입류/전진비 데이터가 확보될 때까지 전진속도 보정은 적용하지 않음"* | **B는 실측(정지 인장시험) 기반이지만 의도적으로 단순화됨** — 실제로는 전진속도가 커질수록(전환 후 순항 시) 추력이 감소해야 정상인데, 현재는 항상 정지추력 기준 곡선을 그대로 씀. A는 반대로 근사식(advance ratio 감쇠)은 있지만 그 자체도 "Replace with BEMT"라는 자체 주석이 달린 미완성 근사임 |
| 모터/pusher 위치 | 모터 ±0.754/±1.163, pusher x=1.60 | 모터 -0.105/1.404 · ±1.163, pusher x=2.249 | CAD 실측(2026-08-19 10:52 보정) |

**문제**: B의 pusher 추력이 실제 순항 속도(20m/s대)에서 과다 추정될 가능성이 있음 — 이번 세션 전환 테스트에서 24m/s까지 가속된 것도 이와 무관하지 않을 수 있음.
**대안**: (1) 실측 유입류/전진비(advance ratio) 데이터를 추가 확보해 A처럼 속도 감쇠 테이블 추가, (2) 프로펠러 BEMT(Blade Element Momentum Theory) 계산으로 대체, (3) 최소한 A의 근사 감쇠 곡선이라도 형태만 차용.

---

## 5. 공력 데이터 (Aero.xml) — 가장 큰 차이

### 5.1 데이터 소스 방식 자체가 다름

| | A | B |
|---|---|---|
| 방식 | 해석적 근사식(thin-airfoil + flat-plate 블렌딩) | **DATCOM 수치해석 결과 테이블**(alpha×mach 2D/3D 테이블) |
| 근거 | 표준 항공역학 근사 공식(CL≈sin(2α), CD≈1-cos(2α) 계열) — 논문/교과서 수준 근사, 실측 아님 | **DATCOM(USAF Digital DATCOM) 산출값** — B의 각 함수 description에 "DATCOM clean case 기반"이라 명시. 반실측(semi-empirical) 항공역학 예측 도구 결과이며, 풍동실측은 아님 |
| alpha 유효범위 | **-180°~+180° 전체** | **-24°~+11°만 정의**(DATCOM 계산이 이 받음각 구간까지만 수행된 것으로 추정) |

### 5.2 alpha 유효범위 문제와 이번 세션의 대응 (신규 추가)

**문제**: DATCOM 테이블이 -24~11도 밖에 없는 상태에서, VTOL 특유의 수직상승/호버 구간은 전진속도가 0에 가까워 `alpha=atan2(w,u)`가 ±90도 부근까지 감(JSBSim 표준 특이점, 소스 `FGAuxiliary.cpp:173`). 이 값이 테이블 밖으로 나가면 JSBSim이 경계값에서 flat 클램프하는데, 이게 실제로는 전혀 다른 비행상태(정상 순항 -24도 근방)의 큰 계수를 엉뚱한 상황(수직상승)에 그대로 적용하는 꼴이 되어 발산 유발.

**A는 이 문제를 원천적으로 안 겪음** — 애초에 -180~180도 전체가 정의돼있어서 alpha가 어디로 가든 유한하고 물리적으로 타당한 값(flat-plate 근사)이 나옴.

**B에 이번 세션 신규 추가한 것**: `aero/coefficient/alpha_validity_gate` — alpha가 -24~11도 테이블 유효범위 밖일 때 계수를 0으로 부드럽게 램프시키는 게이트 함수(-90/-24/11/90도 4점 선형보간). 기존 16개 계수 함수(CL_base, CLq, CLadot, CD_base, CYp, Cl_beta, Clp, Clr, Cl_da, Cm_base, Cmq, Cmadot, Cn_beta, Cnp, Cnr, Cn_da) 전부에 곱셈항으로 삽입.

**검토했던 대안** (2026-08-19~20 논의):
1. **A처럼 -180~180 전체 테이블 재작성**(flat-plate 근사로 블렌딩) — 가장 정확하지만 새 데이터 합성/작업량 큼. DATCOM 원본 실측/해석 데이터를 버리고 근사식으로 덮어써야 함
2. **F450(JSBSim 순정 예제)처럼 alpha 계수를 상수 0으로 고정** — 원천 차단이지만 순항 시 양력도 사라짐(우리 기체는 순항 필요하므로 부적합)
3. **총속도(Vt) 기준 게이팅** — 검토했으나 기각. 수직상승 중에도 Vt 자체는 크므로(상승속도), A가 겪었던 "no lift during transition"과 같은 실수를 반복할 위험
4. **채택: alpha 기준 연속 게이팅**(현재 방식) — DATCOM 원본 데이터 보존, 문제의 직접 원인(alpha가 테이블 밖)에 정확히 대응, 천이 중 자연스럽게 양력 복귀

**남은 리스크**: 이 게이트는 alpha "밖"에서 힘을 죽이는 것이지, alpha가 "안"으로 들어왔을 때의 정확도를 보장하진 않음. 게이트가 재개방되는 순간의 전이 특성(램프 폭 -90~-24, 11~90도)이 실제 물리와 정확히 맞는지는 미검증.

### 5.3 승강타(elevator)·러더(rudder) 공력 계수 부재 (원인 확인됨: V-tail 러더베이터 한계)

> **사용자 확인(2026-08-20)**: 이 기체는 **V-tail(러더베이터) 기체**이며, AVL/DATCOM 계열 공력해석 프로그램이 V-tail의 러더베이터 혼합 효과를 직접 산출하지 못하는 한계가 있어 현재 별도로 검토 중임. 즉 아래 내용은 미발견 버그가 아니라 **사용자가 이미 인지하고 대응 방안을 고민 중인 사안**. JSBSim 쪽 `elevator`/`rudder` 채널은 V-tail 물리 조종면을 편의상 "등가 피치 채널"/"등가 요 채널"로 분리해 표현한 것으로 보이며, 실제 러더베이터 2개 곡면으로의 혼합(mixing)과 그로 인한 커플링된 공력 효과는 JSBSim 모델 범위 밖에 있음.

Aero.xml 전체를 grep한 결과, **`fcs/elevator-pos-rad`와 `fcs/rudder-pos-rad`를 참조하는 함수가 단 하나도 없음**을 확인함(2026-08-20). 즉:

| 조종면 | 기계적 작동(mechanical) | 공력 모멘트 계수(aerodynamic) |
|---|---|---|
| 에일러론 | O (fcs/aileron-cmd-norm → 실제 편향) | **O** — `Cl_da`(롤), `Cn_da`(역요) 존재, alpha/mach/편향각 3D 테이블 |
| 승강타 | O (fcs/elevator-cmd-norm → 실제 편향) | **X — 없음.** Cm_base/Cmq/Cmadot 어디에도 elevator 항 없음 |
| 러더 | O (fcs/rudder-cmd-norm → 실제 편향) | **X — 없음.** Cn_beta/Cnp/Cnr/Cn_da 어디에도 rudder 항 없음 |

**A(레퍼런스)는 셋 다 있음**: `CLde`(-0.35 × elevator-pos-rad), `Cmde`(+1.10 × elevator-pos-rad), `Cndr`(+0.09 × rudder-pos-rad) — 전부 위치에 비례하는 단순 선형 계수(실측/DATCOM 아님, 임의 추정 상수로 보임. A 파일 자체 주석에 "Cmde was NEGATIVE... verified against PX4 CA_SV_CS1_TRQ_P... now POSITIVE"라는 부호 수정 이력만 있고 계수 크기 자체의 출처 설명은 없음).

**왜 결과적으로 영향이 큰가**: 브릿지 매핑 검증(2026-08-19~20)에서 확인했듯, PX4 FW 컨트롤러가 승강타/러더 명령을 정확한 스케일로 JSBSim까지 보내고 조종면도 실제로 움직이는데(제어 경로 정상), **승강타는 피치 모멘트를, 러더는 요 모멘트를 전혀 만들지 않음**. 원인은 사용자가 이미 파악한 대로 V-tail 러더베이터 효과를 AVL/DATCOM이 직접 산출 못 하는 한계임. 최근 전환 테스트에서 나타난 자세 발산(theta -39~+41도)에 영향을 줬을 가능성이 있음 — PX4 FW 자세 컨트롤러가 승강타를 아무리 움직여도 실제 피치 응답이 안 나오니, 제어 루프가 사실상 "블라인드" 상태로 계속 명령을 키웠을 수 있음. 다만 W&B(관성모멘트)도 아직 미확정이라, 자세 발산의 정확한 기여 비율을 이 둘 중 어느 쪽이 더 크게 차지하는지는 현재 구분할 수 없음.

**참고용 대안**(사용자가 V-tail 러더베이터 처리 방안을 결정할 때 검토 후보 — 이번 세션에서 적용하지 않음):
1. A처럼 위치 비례 선형 계수(`CLde`, `Cmde`, `Cndr`)를 임시로 추가 — 빠르지만 A의 계수 자체가 V-tail이 아닌 일반 T-tail/근사 기준 추정치라 이 기체에 그대로 쓰기엔 부정확할 수 있음
2. V-tail 전용 공력해석(예: AVL의 별도 surface 정의로 두 개의 경사진 러더베이터 곡면을 개별 모델링 후 JSBSim에서 두 곡면의 힘을 합산) — 정확하지만 재해석 작업량 큼. 사용자가 언급한 "AVL/DATCOM이 V-tail 러더베이터를 못 본다"는 한계가 바로 이 지점
3. 얇은 익형 이론 + V-tail 기하학적 혼합각(dihedral angle)을 이용한 등가 CLde/Cmde/Cndr 약식 계산 — 중간 수준의 정확도, 계산량 적음. V-tail 기체의 표준적인 근사 처리 방식 중 하나

---

## 6. 조종계 (FlightControl.xml)

A와 B의 Roll/Pitch/Yaw 채널 구조(summer → aerosurface_scale(±25도, gain 0.0174533) → actuator(±0.4363rad clip) → output)가 **거의 동일**함(승강타/러더 사인 규약 포함). B가 A를 그대로 계승한 것으로 보이며, 이번 세션에서 확인한 결과 A가 겪었다는 "elevator 부호 반전" 버그(A 자체 주석 참고: PX4 `CA_SV_CS1_TRQ_P=+1`과 JSBSim 부호 불일치)는 B에서는 처음부터 A의 수정된(올바른) 부호 규약을 상속해서 재발하지 않은 것으로 판단됨(정식 검증은 안 함 — Cmde 자체가 없으므로 검증 대상이 아직 없음).

---

## 7. PX4 airframe / bridge 설정 (이번 세션 신규 작업, 레퍼런스는 gazebo-classic/sihsim 표준 예제)

| 항목 | 근거 | 문제/이유 |
|---|---|---|
| `rc.mc_defaults`→`rc.vtol_defaults`, `CA_AIRFRAME 0`→`2`, `CA_ROTOR_COUNT 4`→`5` | PX4 표준 VTOL 예제(`1040_gazebo-classic_standard_vtol`) 패턴 그대로 적용 | 기존 airframe이 순수 멀티콥터로 등록돼있어 PX4가 VTOL 전환 로직 자체를 활성화하지 않았음 |
| `CA_SV_CS0/1/2_TYPE 15/3/4`(aileron/elevator/rudder) | `10043_sihsim_standard_vtol` 예제의 명시적 주석("single channel aileron"/"elevator"/"rudder")으로 타입 코드 확정 | 조종면 3개를 PX4 control allocator에 등록해야 FW 컨트롤러가 조종면 명령을 생성함 |
| `CA_ROTOR4_PX -1.6` | 기존 4개 로터의 검증된 좌표(`PX4_PX = CG_x - motor_x`)에서 역산한 공식을 pusher에 동일 적용 | JSBSim 구조좌표(+X=aft)와 PX4 CA_ROTOR 좌표(+X=forward-from-CG)의 프레임 차이를 일관되게 처리 |
| bridge에 aileron/elevator/rudder/airspeed 채널 추가 | JSBSim FlightControl.xml이 기대하는 정확한 프로퍼티명(`fcs/aileron-cmd-norm` 등)과 대조 확인 후 추가 | 기존 bridge config가 4개 리프트모터+pusher 채널만 있어 조종면 명령이 JSBSim까지 전달되지 않았음 |
| `FW_AIRSPD_MIN/TRIM/MAX 10/15/22` | **실측 없는 잠정값** — 참고 예제(gazebo: 25, sih: 7~12)의 중간값 정도로 추정 설정 | B 기체의 실제 실속속도/순항속도 데이터가 없어 우선 동작 가능한 잠정치로 설정 |

**대안**: 실측/CFD 기반 실속속도 계산 후 FW_AIRSPD_* 재설정. 또는 A의 주석에 있던 예측치(V_stall 17.4 m/s, cruise 22-24 m/s, wingarea 0.953㎡ 기준)를 B의 wingarea(0.572㎡, 더 작음→같은 중량이면 실속속도가 더 높아야 함)에 맞게 스케일링해 재추정 가능.

---

## 8. 종합 — 근거 유형별 분류

| 근거 유형 | 해당 항목 |
|---|---|
| **실측(CAD/pull-test)** | Mass.xml **CG x좌표만**(0.649m), Gear/ExternalReactions 위치, lift/pusher 추력 테이블(정지 인장시험) |
| **DATCOM(반실측 해석)** | Aero.xml CL_base/CD_base/Cm_base 등 -24~11도 구간 값 |
| **표준 공식/근사** | alpha_validity_gate(이번 세션 신규, 물리적 근거는 있으나 램프 폭은 임의 설정), A의 flat-plate 근사(-180~180도) |
| **임의값 — W&B 확인 진행 중(사용자 확인, 버그 아님)** | Mass.xml 관성모멘트(ixx/iyy/izz), CG y/z |
| **A(데모) 상속, 미검증** | Gear.xml spring/damping 계수, EYEPOINT 오프셋 |
| **PX4 표준 예제 상속** | CA_SV_CS_TYPE 코드, VTOL airframe 파라미터 골격 |
| **잠정값(placeholder)** | FW_AIRSPD_MIN/TRIM/MAX, VT_F_TRANS_THR |
| **부재 — 원인 확인됨(사용자 확인): V-tail 러더베이터를 AVL/DATCOM이 처리 못 함, 별도 검토 중** | 승강타/러더 공력 모멘트 계수(Cmde, Cndr 상당) |

## 9. 다음 순위 제안

> 2026-08-20 사용자 확인: 5.3절(승강타/러더 계수 부재)과 2절(관성모멘트) 둘 다 **미발견 버그가 아니라 사용자가 이미 인지하고 별도로 진행 중인 사안**(V-tail 러더베이터는 AVL/DATCOM 한계로 검토 중, 관성모멘트는 W&B 확인 작업 진행 중이며 CG x좌표만 확정). 아래 우선순위는 이 두 가지가 사용자 쪽에서 해결/확정된 이후를 전제로 한 순서로 재조정함.

1. **W&B 확정 대기** — 관성모멘트를 포함한 나머지 질량 특성이 확정되면 그 즉시 Mass.xml 갱신
2. **V-tail 러더베이터 공력 처리 방안 확정 대기** — 사용자가 검토 중인 방식이 정해지면 그에 맞춰 Aero.xml의 승강타/러더 등가 계수 추가
3. **(참고, 낮은 우선순위) Pusher 전진속도 감쇠 테이블 추가** — 순항 시 추력 과다 추정 가능성, 위 두 항목보다 영향은 작음
4. **(참고, 낮은 우선순위) FW_AIRSPD_* 재추정** — wingarea 차이를 반영한 실속속도 재계산
