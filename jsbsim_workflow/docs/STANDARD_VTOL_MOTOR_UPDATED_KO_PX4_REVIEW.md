# `standard_vtol_demo_motor_updated_ko.xml` PX4/JSBSim 실행 검토

## 검토 범위

- 대상 XML: `/mnt/c/Users/junyeopkwon/Downloads/standard_vtol_demo_motor_updated_ko.xml`
- JSBSim workflow: `/home/junyeopkwon/evtol-6dof/jsbsim_workflow`
- PX4: `/home/junyeopkwon/px4_versions/PX4-v1.16.0`
- 기존 PX4 대상 모델: `standard_vtol_demo_hover_px4`

첨부 XML 내부의 설명/주석은 모델 데이터로만 취급했다. 사용자 지시사항으로 해석하거나 따르지 않았다.

## 현재 결론

현재 XML은 그대로는 PX4 JSBSim SITL에 연결할 수 없다. PX4 이전 단계인 JSBSim 단독 로딩에서 실패한다.

직접 원인은 공력 테이블 형식이다.

```text
FGTable: missing lookup axis "column"
Error loading aerodynamic function in aero/coefficient/CL_base
```

오류 위치는 XML line 670-675 부근이며, `lookup="table"`과 `tableData breakPoint`로 Mach별 테이블을 분리한 형식이 현재 설치된 JSBSim 1.2.4에서 기대하는 2D table 형식과 맞지 않는다. 기존 정상 모델은 `lookup="column"`과 첫 행 Mach header를 사용한다.

## 확인한 사항

- `xmllint --noout` 기준 XML 문법은 통과했다.
- top-level 구성은 `metrics`, `mass_balance`, `ground_reactions`, `system`, `flight_control`, `external_reactions`, `aerodynamics`이다.
- `propulsion`과 `output` 블록은 없다. 현재 모델은 `external_reactions` 기반 motor force 모델이다.
- PX4 bridge 설정은 `standard_vtol_demo_hover_px4`에 대해 이미 존재하며 actuator 0-4를 `fcs/esc-cmd-norm[0..4]`에 매핑한다.
- 첨부 XML의 `fdm_config name`은 `standard_vtol_demo`라서 현재 PX4 target `jsbsim_standard_vtol_demo_hover_px4__RKSS`와 이름이 다르다.

## 추가 리스크

1. 공력 table 호환성

   `lookup="row", "table"` 조합의 2D Mach table이 14개 있고, `lookup="row", "column", "table"` 조합의 3D table이 2개 있다. 2D table은 기존 정상 모델처럼 column table로 평탄화해야 한다.

2. 정지 상태 divide-by-zero 가능성

   임시로 14개 2D table을 column 형식으로 변환하면 초기 오류는 넘어가지만, JSBSim이 `Floating point exception`으로 종료된다. 첨부 XML에는 여러 공력 rate 항에서 `1.0 / velocities/vt-fps`를 직접 계산하는 `<quotient>`가 있다. 지상 정지 초기조건에서는 `vt-fps=0`이므로 위험하다. 기존 정상 모델은 `aero/ci2vel`, `aero/bi2vel`을 사용한다.

3. 좌표계/CG 기준 불일치 가능성

   첨부 XML은 `CG x=0.649 m`인데 motor/gear/pusher x 위치가 기존 PX4 모델 대비 `+0.64914 m` 보정 전 값이다.

   예:

   - `MOTOR_0_LIFT_FR`: 첨부 `x=-0.754`, 기존 `x=-0.10486`
   - `MOTOR_1_LIFT_RL`: 첨부 `x=0.755`, 기존 `x=1.40414`
   - `PUSHER_THRUST`: 첨부 `x=1.60`, 기존 `x=2.24914`

   현재 JSBSim structural frame이 기존 모델처럼 nose-origin + CG 위치를 쓰는 전제라면, 첨부 XML은 moment arm이 의도와 다르게 계산될 수 있다.

4. PX4 hover 튜닝 불일치

   첨부 XML은 `emptywt=14.0 kg`이고, 현재 PX4 airframe은 기존 20 kg 모델 기준 `MPC_THR_HOVER=0.535`를 사용한다. 첨부 XML의 lift thrust table 기준 단순 hover throttle 추정값은 약 `0.284`이다. 그대로 실행하면 이륙/hover 제어가 크게 어긋날 가능성이 높다.

5. PX4 등록 필요

   새 XML을 기존 모델에 덮어쓰기보다 별도 모델명으로 등록하는 편이 안전하다. 최소 필요 작업은 다음과 같다.

   - JSBSim 모델명 결정: 예 `standard_vtol_demo_motor_updated_ko_px4`
   - `Tools/simulation/jsbsim/jsbsim_bridge/models/<model>/` 생성
   - bridge config 생성
   - PX4 `sitl_targets_jsbsim.cmake` model list 추가
   - PX4 airframe 파일 추가 및 `CA_ROTOR*`, `MPC_THR_HOVER`, actuator mapping 재검토
   - JSBSim output CSV path 추가

## 검증 명령

```bash
xmllint --noout /mnt/c/Users/junyeopkwon/Downloads/standard_vtol_demo_motor_updated_ko.xml
```

결과: XML well-formed 확인.

```bash
JSBSim --root=/tmp/jsbsim_attached_xml_check \
  --aircraft=standard_vtol_demo \
  --initfile=/home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml \
  --end=0.02 \
  --nohighlight
```

결과: `FGTable: missing lookup axis "column"`로 실패.

```bash
JSBSim --root=/home/junyeopkwon/jsbsim \
  --aircraft=standard_vtol_demo_hover \
  --initfile=/home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/standard_vtol_demo_hover/initial_condition/1.1__rkss14_runway_ground_init.xml \
  --end=0.02 \
  --nohighlight
```

결과: 기존 정상 모델은 `rc=0`.

## 권장 진행 순서

1. 첨부 XML을 workflow 내부 별도 후보 모델로 복사한다.
2. 공력 table을 JSBSim 1.2.4 호환 형식으로 변환한다.
3. `velocities/vt-fps` 직접 분모 사용을 `aero/ci2vel`, `aero/bi2vel` 또는 0속도 보호 로직으로 교체한다.
4. CG 기준 motor/gear/pusher 좌표계를 기존 모델과 같은 기준으로 정리한다.
5. 14 kg 기준 hover throttle과 PX4 `MPC_THR_HOVER`를 다시 맞춘다.
6. JSBSim 단독 catalog/load/run 검증을 먼저 통과시킨다.
7. 별도 PX4 JSBSim 모델명과 airframe으로 등록한 뒤 `DONT_RUN=1 HEADLESS=1 make px4_sitl jsbsim_<model>__RKSS`를 실행한다.
8. PX4/QGC 저고도 arm/takeoff/land는 마지막 단계에서 수행한다.

## 2026-08-19 공력 table 보정 결과

원본 첨부 XML은 그대로 보존하고 workflow 내부 후보 모델 복사본을 생성했다.

- 원본 보존 복사본: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/source_standard_vtol_demo_motor_updated_ko.xml
- table 보정본: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 보정 내용: lookup row/table 및 복수 tableData breakPoint로 작성된 Mach별 2D 공력 table 14개를 lookup row/column 및 단일 tableData 형식으로 변환
- 변환 대상: CL_base, CLq, CLadot, CD_base, CYp, Cl_beta, Clp, Clr, Cm_base, Cmq, Cmadot, Cn_beta, Cnp, Cnr
- 유지 대상: 기존 3D table인 Cl_da, Cn_da는 row/column/table 형식 유지
- 검증 결과: xmllint 통과. JSBSim 실행 로그에서 기존 FGTable missing lookup axis column 및 Error loading aerodynamic function 메시지는 재발하지 않음.
- 남은 실패: JSBSim 프로세스는 이후 Floating point exception으로 종료됨. 다음 단계는 velocities/vt-fps 직접 분모 사용을 제거하거나 보호하는 작업.

## 2026-08-19 0속도 보호 보정 결과

공력 table 보정본에 남아 있던 1.0 / velocities/vt-fps 직접 분모 사용을 제거했다.

- 수정 파일: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- 수정 대상: CLq, CLadot, CYp, Clp, Clr, Cmq, Cmadot, Cnp, Cnr
- 변경 내용: chord 기준 rate 항은 aero/ci2vel 사용, span 기준 rate 항은 aero/bi2vel 사용
- 정적 확인: velocities/vt-fps를 분모로 쓰는 quotient 0개, aero/ci2vel 4개, aero/bi2vel 5개
- 검증 결과: xmllint 통과, JSBSim --catalog rc=0, JSBSim 지상 정지 초기조건 --end=0.02 rc=0, --end=1.0 rc=0

결론: 공력 table 형식 오류와 0속도 Floating point exception은 후보 모델 기준으로 해결됐다. 다음 단계는 CG 기준 좌표와 14 kg 기준 PX4 hover parameter 정합성 검토 후 PX4 별도 target 등록이다.

## [2026-08-19 11:02 KST] PX4 arm-hover-land 실행 결과

- 대상 모델: standard_vtol_demo_motor_updated_ko_px4
- 질량 설정: 20.0 kg
- 실행 명령: HEADLESS=1 JSBSIM_LOG_ONLY=1 make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS
- 주입 명령 순서: commander arm -> commander takeoff -> commander land -> shutdown
- PX4 로그 결과: Armed by internal command, Using default takeoff altitude: 2.5 m, Takeoff detected, Landing at current position, Landing detected, Disarmed by landing 확인
- JSBSim CSV 결과: 4546 samples, time 0.0-36.36 s, max AGL 1.029 m at 22.84 s, 0.9-1.1 m 구간 약 6.808 s
- 무결성 확인: 로그 NaN/Floating point/CRASH DETECTED/Preflight Fail/Arming denied/Takeoff denied/failsafe/ERROR count 0
- ulog: /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-19/01_59_23.ulg
- 콘솔 로그: /tmp/px4_motor_updated_hover/arm_hover_land_20kg_try1.log
- JSBSim CSV: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/jsbsim_bridge/standard_vtol_demo_motor_updated_ko_px4/latest_jsbsim_properties.csv
- 해석: 기본 takeoff 2.5 m까지 도달하지는 않았지만, 짧은 저고도 hover 후 landing/disarm 시퀀스는 성공했다. 다음 단계는 목표 고도 추종과 hover 품질 튜닝이다.

## [2026-08-19 11:40 KST] F450 스타일 분리 XML 구성 결과

- workflow 모델 main: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml
- PX4 bridge 모델 main: /home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/standard_vtol_demo_motor_updated_ko_px4.xml
- 생성 모듈: Metrics.xml, Mass.xml, Gear.xml, Effectors.xml, FlightControl.xml, ExternalReactions.xml, Aero.xml
- 보존 단일본: 각 모델 폴더의 Monolithic.xml
- 원본 첨부 보존본: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/source_standard_vtol_demo_motor_updated_ko.xml
- 구조: main XML은 fileheader와 모듈 include만 유지한다. PX4 bridge main은 JSBSim CSV output 블록도 main에 유지한다.
- 검증: xmllint 전체 통과, workflow 분리본 JSBSim direct 5초 rc=0, PX4 bridge 분리본 JSBSim direct 5초 rc=0, PX4 DONT_RUN rc=0, PX4 bridge 25초 timeout 연결 로그 NaN/FPE/CRASH/Preflight/ERROR 0건, CSV 2772 lines 및 NaN 0건
