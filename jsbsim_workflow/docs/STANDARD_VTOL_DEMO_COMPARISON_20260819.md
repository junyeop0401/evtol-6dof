# standard_vtol_demo.xml vs standard_vtol_demo_motor_updated_ko_px4 비교 - 2026-08-19

## 비교 대상

- 전환 성공 XML: `/mnt/d/ProjectAirSim-jsbsim/core_sim/jsbsim/models/aircraft/standard_vtol_demo/standard_vtol_demo.xml`
- 현재 PX4-JSBSim 모델: `/home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/standard_vtol_demo_motor_updated_ko_px4.xml`
- 현재 PX4-JSBSim bridge config: `/home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_motor_updated_ko_px4.xml`
- 현재 PX4 airframe: `/home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4`

## 결론

`standard_vtol_demo.xml`이 VTOL 천이에 성공했던 이유는 단순히 같은 4 lift + 1 pusher 구조라서가 아니라, 전환을 위해 이미 여러 보호/튜닝이 들어간 데모 모델이기 때문이다. 현재 새 모델은 hover용 모터/질량/좌표 문제는 어느 정도 해결됐지만, fixed-wing transition에 필요한 PX4 airframe 설정, bridge 조종면 매핑, elevator/rudder 공력 derivative, full-envelope aero가 부족하다.

## 핵심 차이

### 1. PX4 airframe이 다르다

현재 3021 airframe은 다음처럼 순수 multicopter에 가깝다.

- `rc.mc_defaults`
- `@type Quadrotor Wide`
- `CA_AIRFRAME 0`
- `CA_ROTOR_COUNT 4`
- `PWM_MAIN_FUNC1..5 = 101..105`

반면 PX4 표준 VTOL 예제는 다음 요소를 가진다.

- `rc.vtol_defaults`
- `VT_TYPE 2`
- `CA_AIRFRAME 2`
- `CA_ROTOR_COUNT 5`
- `CA_ROTOR4_AX 1`
- `CA_SV_CS_COUNT 3`
- `PWM_MAIN_FUNC*`에 motor + servo surface를 함께 배치
- `FW_AIRSPD_*`, `VT_F_TRANS_THR` 등 전환/고정익 파라미터

따라서 현재 새 모델은 XML이 VTOL 형태여도 PX4 제어 stack 입장에서는 전환 가능한 Standard VTOL로 충분히 설정되어 있지 않다.

### 2. 성공 XML은 full-envelope aero를 가진다

성공 XML 주석에는 다음 의도가 명확히 기록되어 있다.

- transition 중 `0..90 deg` 받음각까지 유한하게 동작하도록 full-envelope aero 사용
- `CLmax 1.32 @ 14 deg`
- `V_stall 17.4 m/s`, `cruise 22-24 m/s`
- 과거 `no lift during transition` quad-chute를 고치기 위해 CAD planform과 full-envelope CL/CD로 교체

현재 새 모델은 다음과 다르다.

- `wingarea 0.5720 m2`
- `emptywt 20.0 kg`
- `alphalimits -24..11 deg`
- DATCOM clean table 기반 `CL_base`, `CD_base`

즉 새 모델은 실제 데이터 기반이지만 transition high-alpha 과도 구간을 성공 XML처럼 명시적으로 보호하지 않는다. wing loading도 성공 XML 약 `243 N/m2` 대비 새 모델 약 `343 N/m2`로 더 높아서 같은 조건이면 요구 속도가 올라간다.

### 3. 성공 XML은 elevator/rudder 공력 효과가 있다

성공 XML에는 다음 fixed-wing control derivative가 존재한다.

- `CLde` uses `fcs/elevator-pos-rad`, value `-0.35`
- `Cmde` uses `fcs/elevator-pos-rad`, value `1.10`
- `Cndr` uses `fcs/rudder-pos-rad`
- `Clda` uses `fcs/effective-aileron-pos`

특히 성공 XML 주석에는 elevator sign fix가 기록되어 있다. 과거에는 `Cmde` 부호가 반대라서 FW 진입 후 pitch가 발산했고, 이를 `Cmde` positive / `CLde` negative로 고쳤다고 되어 있다.

현재 새 `Aero.xml`에는 `fcs/elevator-pos-rad`, `fcs/rudder-pos-rad`를 사용하는 항목이 없다. `FlightControl.xml`이 elevator/rudder 위치를 만들어도 공력 모델이 그 값을 쓰지 않으면 fixed-wing pitch/yaw 조종면은 사실상 효과가 없다. 현재 새 모델에서 확인된 조종면 관련 항목은 `Cl_da`, `Cn_da`가 `fcs/effective-aileron-pos-deg`를 쓰는 정도다.

### 4. bridge actuator mapping이 다르다

성공 XML은 ProjectAirSim jsbsim-physics가 `actuator name = fcs/esc-out[N]`일 때 해당 property에 직접 값을 주입하는 구조였다고 주석에 적혀 있다.

현재 PX4-JSBSim bridge config는 다음 5개만 매핑한다.

- index 0 -> `fcs/esc-cmd-norm[0]`
- index 1 -> `fcs/esc-cmd-norm[1]`
- index 2 -> `fcs/esc-cmd-norm[2]`
- index 3 -> `fcs/esc-cmd-norm[3]`
- index 4 -> `fcs/esc-cmd-norm[4]`

현재 config에는 `fcs/aileron-cmd-norm`, `fcs/elevator-cmd-norm`, `fcs/rudder-cmd-norm` 매핑이 없다. 따라서 PX4가 fixed-wing surface output을 만들더라도 JSBSim property로 전달되지 않는다.

### 5. pusher thrust 모델이 다르다

성공 XML pusher는 throttle table에 forward-speed decay를 곱한다.

- static max `23.5 lbf`
- `velocities/vt-fps`가 커질수록 thrust 감소

현재 새 모델 pusher는 제조사 정지 인장시험 기반 table 하나만 사용한다.

- static max 약 `30.60 lbf`
- 전진속도 보정 없음

정지 추력만 보면 새 모델이 더 강하지만, 전환 중 동특성은 더 단순하다. pusher가 충분한지 여부는 bridge/airframe에서 pusher가 실제로 전환 중 구동되는지 확인한 뒤 판단해야 한다.

## 우선순위 판단

1. 1순위: 현재 3021 airframe이 Standard VTOL이 아니라 multicopter 설정이다.
2. 2순위: bridge config가 fixed-wing control surface command를 JSBSim에 전달하지 않는다.
3. 3순위: 새 `Aero.xml`에 elevator/rudder derivative가 없어 fixed-wing pitch/yaw 조종이 약하거나 불가능하다.
4. 4순위: 성공 XML의 full-envelope aero/high-alpha 보호가 새 DATCOM clean aero에는 없다.
5. 5순위: wing loading과 전환 속도 파라미터가 성공 XML과 다르다.

## 권장 적용 방향

먼저 성공 XML의 전환 성공 요소를 새 모델에 맞게 이식하는 순서가 맞다.

1. PX4 airframe을 `rc.vtol_defaults`, `VT_TYPE 2`, `CA_AIRFRAME 2`, `CA_ROTOR_COUNT 5`로 전환
2. pusher를 5번째 forward rotor로 control allocation에 포함
3. aileron/elevator/rudder servo allocation 추가
4. bridge config에 `fcs/aileron-cmd-norm`, `fcs/elevator-cmd-norm`, `fcs/rudder-cmd-norm` 추가
5. 새 `Aero.xml`에 최소한 성공 XML 수준의 `CLde`, `Cmde`, `Cndr`를 추가하고 부호 확인
6. transition high-alpha 보호를 위해 full-envelope fallback 또는 `alphalimits/table` 확장 검토
7. `FW_AIRSPD_MIN/TRIM/MAX`, `VT_F_TRANS_THR`, `VT_ARSP_TRANS` 또는 duration 계열 파라미터를 새 wing loading 기준으로 재설정

## 다음 검증 기준

수정 후 QGC 또는 scripted MAVLink로 MC hover -> front transition -> FW hold를 실행하고 아래를 확인한다.

- ULog: `vehicle_status.nav_state`, `vtol_vehicle_status`, `actuator_outputs`, `airspeed_validated`, `vehicle_attitude`, `vehicle_local_position`
- JSBSim CSV: `fcs/esc-out[4]`, `fcs/aileron-cmd-norm`, `fcs/elevator-cmd-norm`, `fcs/rudder-cmd-norm`, `fcs/elevator-pos-rad`, `velocities/vt-fps`, `aero/alpha-deg`

전환 중 `fcs/elevator-cmd-norm`은 움직이는데 `fcs/elevator-pos-rad` 또는 pitch moment가 반응하지 않으면 XML 공력 연결 문제다. `fcs/esc-out[4]`가 안 움직이면 airframe/control allocation/bridge index 문제다. airspeed가 안 잡히면 sensor/parameter 문제다.
