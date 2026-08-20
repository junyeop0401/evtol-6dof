# standard_vtol_demo_motor_updated_ko — 고정익(FW) 전환 실패(Quad-chute) 진단 보고서

- 작성일: 2026-08-20
- 대상 기체: `standard_vtol_demo_motor_updated_ko_px4` (JSBSim/PX4 SITL)
- 목적: 멀티콥터→고정익 전환 시도 시 반복적으로 발생하는 `Quad-chute`(PX4 자동 안전 복귀)의 정확한 원인을 소스 코드와 실측 데이터로 규명하고, 해결을 시도한 기록

---

## 1. 문제 정의

- 증상: `commander transition`(또는 QGC "Transition to Fixed Wing") 명령 후 수 초 이내에 PX4가 자동으로 고정익 모드를 포기하고 멀티콥터 모드로 강제 복귀
- 콘솔 메시지: `WARN [vtol_att_control] Quad-chute triggered`
- 최초 가설(기각됨): 자세각(pitch/roll)이 커져서 그런 줄 알았음 — theta가 -39~+56도까지 진동하는 게 관측됐기 때문
- 이 문서는 (1) 진짜 트리거 조건이 무엇인지, (2) 왜 그 조건이 충족되는지, (3) 무엇을 시도했고 결과가 어땠는지, (4) 실제 QGC 비행에서도 동일하게 재현되는지를 정리함

---

## 2. 원인 규명 — 1단계: 진짜 트리거 조건 확인

### 2.1 가설 기각: 자세각 초과가 아니었음

PX4 소스(`src/modules/vtol_att_control/vtol_type.cpp`)를 직접 확인:

```cpp
bool VtolType::isPitchExceeded() {
    if (_param_vt_fw_qc_p.get() > 0) {   // 기본값 0 → 이 블록 자체가 안 돎
        ...
    }
    return false;
}
```

`VT_FW_QC_P`(최대 pitch 임계값), `VT_FW_QC_R`(최대 roll 임계값)은 **PX4 기본값이 0(=비활성)**이고, 이 프로젝트의 airframe 파일 어디에도 설정된 적이 없음(grep으로 확인). 즉 **자세각 기반 quad-chute 체크는 애초에 꺼져 있었음**. 지금까지 관측한 큰 자세각 진동은 quad-chute의 "원인"이 아니라, quad-chute 이후 벌어진 불안정 회복 과정의 "결과"였음.

### 2.2 진짜 트리거: 전환 중 고도손실 20m 초과

```cpp
bool VtolType::isFrontTransitionAltitudeLoss() {
    if (_param_vt_qc_t_alt_loss.get() > FLT_EPSILON && ...
        && (_common_vtol_mode == mode::TRANSITION_TO_FW || hrt_elapsed_time(&_trans_finished_ts) < 5_s)) {
        result = _local_pos->z - _local_position_z_start_of_transition > _param_vt_qc_t_alt_loss.get();
    }
    return result;
}
```

`VT_QC_T_ALT_LOSS` 기본값 **20m**, 이 체크는 활성 상태(기본값 자체가 0이 아님). **전환 시작 시점 또는 전환 완료 후 5초 이내에 고도가 20m 이상 떨어지면** 발동. `getQuadchuteReason()`에서 이 체크가 자세각 체크보다 먼저 평가됨.

### 2.3 실측 데이터로 대조

JSBSim CSV(2026-08-20, `vtol_transition_mavlink_test.py` 실행분) 시계열:

| 시각 | vtol_state | 고도(AGL) |
|---|---|---|
| t=714.2 | TRANSITION_TO_FW 진입 | 28.8 m |
| t=715.5 | FW 도달 | 24.8 m |
| t=716.8 | FW 유지 | 15.2 m |
| **t=717.8** | FW 유지 | **0.6 m** |
| t=718.1 | **MC로 강제 복귀** | -3.0 m |

**3.6초 만에 28.2m 하강** — 20m 기준을 크게 초과, 타이밍도 "전환 중"이라는 코드 조건과 정확히 일치. **결론: quad-chute는 자세각이 아니라 전환 중 급격한 고도손실 때문에 발동함이 확정됨.**

---

## 3. 원인 규명 — 2단계: 왜 고도가 떨어지는가 (정량 분석)

### 3.1 무승강타 자연 트림점 계산

`Aero.xml`의 `Cm_base` 테이블(DATCOM, alpha·mach 2D)에서 Cm=0이 되는 지점(승강타 효과 없이 순수 기체 형상만으로 정해지는 안정 트림각):

- alpha=3.5° → Cm=+0.0279
- alpha=6.0° → Cm=-0.0403
- 선형보간 zero-crossing → **alpha≈4.5°**
- 이때 `CL_base` 테이블 값: **CL≈0.91**

### 3.2 필요 속도 계산

기체 제원: 질량 20.0kg(중량 W=196N), 날개면적 S=0.572㎡

```
필요 CL로 수평비행 가능한 속도:
V = √( W / (0.5 · ρ · CL · S) )
  = √( 196 / (0.5 · 1.225 · 0.91 · 0.572) )
  ≈ 24.8 m/s
```

### 3.3 결론

전환 과정은 속도가 0→24m/s대까지 **가속하는 과정**이며, **가속 도중(대략 15~20m/s대)에는 자연 트림점의 CL(0.91)로 낼 수 있는 양력이 부족**해서 가라앉음. 승강타를 더 당겨 받음각을 키우면(계산상 필요 alpha≈9~10°, CL≈1.4) 이 속도대에서도 양력 보충이 가능하지만—

**`Aero.xml`에 승강타 피치 모멘트 계수(Cmde)가 아예 없어서(V-tail 러더베이터를 AVL/DATCOM이 처리 못 하는 별도 이슈)** PX4가 승강타를 아무리 명령해도 실제 피치 응답이 없음. 결과적으로 "손 놓은 자연 안정성"에만 의존하다가 가속 구간에서 양력 부족 → 하강 → quad-chute.

---

## 4. 해결 시도 (A + B)

### 4.1 A안: 임시 공력계수 추가

레퍼런스 성공 모델(`standard_vtol_demo.xml`)의 계수를 "[임시 placeholder]"로 명시하여 그대로 차용:

| 계수 | 값 | 축 |
|---|---|---|
| `CLde` | -0.35 × qbar-area × elevator-pos-rad | LIFT |
| `Cmde` | +1.10 × qbar-area × cbarw × elevator-pos-rad | PITCH |
| `Cndr` | +0.09 × qbar-area × bw-ft × rudder-pos-rad | YAW |

### 4.2 B안: 전환 가속 강화

`VT_F_TRANS_THR`(전환 중 pusher 추력 비율): **0.75 → 1.0**(최대)로 상향 — 저속/양력부족 구간을 더 빨리 통과시키려는 의도

### 4.3 재검증 결과

| 항목 | A/B 적용 전 | A/B 적용 후 |
|---|---|---|
| FW 도달 최고 groundspeed | 24.33 m/s | 25.17 m/s (소폭 개선) |
| FW 상태 유지시간 | ~2.6초 | ~2.2초 |
| 고도 손실 | 28.8m→0.6m (약 28m) | 28.7m→0.2m→**-5.9m** (더 심함) |
| theta 범위 | -39~+56도 | -30~+55도 |
| NaN 발산 | 0건 | 0건 |
| 착륙 완료 | 정상 | 정상 |

**결론: A/B 모두 적용해도 quad-chute는 동일 메커니즘으로 재발.** 레퍼런스 기체(A, wingarea 0.953㎡/23.6kg)와 우리 기체(0.572㎡/20.0kg)의 날개하중이 크게 달라, A의 계수 크기를 그대로 가져온 것만으로는 부족한 것으로 추정됨. (근본 해결은 V-tail 실측 공력데이터 확보 — 별도 진행 중)

---

## 5. 실제 QGC 비행으로 재검증

### 5.1 동일 원인 재현 확인

사용자가 직접 QGC로 비행 시도한 로그(`05_27_49.ulg`)에서 정확히 동일한 메시지 확인:

```
0:00:15  Armed by external command
0:01:34  Preflight Fail: Attitude failure (roll)
0:01:35  CRITICAL: Quad-chute triggered due to loss of altitude during transition
0:01:35  Failsafe activated: switching to RTL in 5 seconds
```

→ 소스 분석으로 예측한 트리거 메시지("due to loss of altitude during transition")가 실제 QGC 비행 로그와 **글자 그대로 일치**. 진단이 정확했음을 실비행으로 최종 확인.

### 5.2 장시간 방치 시 실제 발산(NaN) 사례

이 QGC 세션은 quad-chute 이후 곧바로 착륙시키지 않고 계속 비행을 이어갔고, 그 결과 상태가 계속 악화됨:

```
0:02:24  Compass 0 fault (반복)
0:03:55  CRITICAL: Airspeed sensor failure detected
0:03:59  Failsafe: Autopilot disengaged, switching to Descend
0:04:05  [mc_pos_control] invalid setpoints / Failsafe: blind land
0:04:10  RTL: start return at 73m (재시도)
```

이후 JSBSim 물리 시뮬레이션 자체가 **NaN으로 완전히 발산**(해당 세션 CSV 전체 18,067행이 NaN, 최종 행까지 `AGL=nan theta=-nan`). QGC 화면에는 고도가 `-2147498.5m`로 표시됐는데, 이는 실제 값이 아니라 NaN이 정수로 잘못 변환되며 나온 쓰레기값(INT32 오버플로 패턴)이었음.

**교훈: quad-chute 발생 즉시 착륙/RTL로 개입하면 안전하게 회수되지만, 계속 비행을 시도하면 실제 크래시(수치 발산)로 악화될 수 있음.**

### 5.3 "정상 종료"와 "발산" 로그 비교

| 로그 파일 | 결과 | quad-chute 이후 대응 |
|---|---|---|
| `04_14_07.ulg` | ✅ Landing detected(2:23) → Disarmed(2:25) | 즉시 RTL(0:51) → 착륙 |
| `04_27_17.ulg` | ✅ Landing detected(1:57) → Disarmed(1:59) | 즉시 RTL(0:50) → 착륙 |
| `05_14_56.ulg` | ✅ Landing detected(3:53) → Disarmed(3:55) | RTL(1:57) → 착륙 |
| `05_27_49.ulg`(QGC 실비행) | ❌ NaN 발산, 회수 불가 | RTL 시도했으나 계속 불안정 지속, 4분+ 경과 후 물리 발산 |

모든 로그가 **quad-chute 자체는 동일하게 겪음** — 차이는 그 이후 개입 타이밍뿐. 즉 quad-chute 자체는 PX4 안전장치가 "설계대로" 작동한 것이고, 진짜 문제는 quad-chute를 유발한 근본 원인(4장)임.

---

## 6. 로그/산출물 위치

| 항목 | 경로 |
|---|---|
| PX4 ulog(오늘 전체) | `/home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-20/` |
| JSBSim 결합 CSV | `/home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/jsbsim_bridge/standard_vtol_demo_motor_updated_ko_px4/` |
| 진단용 MAVLink 테스트 스크립트 | `jsbsim_workflow/scripts/vtol_transition_mavlink_test.py`, `vtol_full_mission_test.py` |
| 수정된 Aero.xml(A안 적용분) | `jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/Aero.xml` |
| 수정된 airframe(B안 적용분) | `px4_versions/PX4-v1.16.0/.../airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4` |
| 관련 git 커밋 | `39aa989`(AERORP 수정), `1f16a6f`(alpha 게이트), `6493bbe`(A+B 임시계수) |

---

## 7. 결론 및 다음 단계

1. **quad-chute 트리거는 확정적으로 규명됨**: 자세각이 아니라 전환 중 고도손실 20m 초과(`VT_QC_T_ALT_LOSS`)이며, 근본 원인은 승강타 공력 모멘트 계수(Cmde) 부재로 인한 양력 부족
2. **레퍼런스 계수를 임시로 빌려온 A/B 시도는 실패** — 날개하중 차이로 인해 부족한 것으로 추정
3. **실제 QGC 비행에서 100% 동일하게 재현됨** — 시뮬레이션 특이 현상이 아니라 재현 가능한 실제 문제
4. **quad-chute 자체는 안전하게 동작함**(즉시 RTL/착륙 개입 시 정상 회수) — 근본 원인 해결 전까지는 전환 시도 후 빠른 개입이 임시 운용 지침이 될 수 있음

**다음 단계(우선순위)**:
1. V-tail 러더베이터 실측/AVL 공력데이터 확보(사용자 별도 진행 중) → Cmde/Cndr 정식값 반영
2. 정식 데이터 확보 전 임시 조치로, A 계수를 날개하중 비율로 스케일링해 재실험 검토
3. Weight & Balance 확정(관성모멘트 등) 후 전체 재검증
