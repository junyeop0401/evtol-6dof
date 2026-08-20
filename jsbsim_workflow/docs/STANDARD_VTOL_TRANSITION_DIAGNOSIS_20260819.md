# Standard VTOL Transition Diagnosis - 2026-08-19

## 대상

- JSBSim workflow 모델: `/home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/standard_vtol_demo_motor_updated_ko/standard_vtol_demo_motor_updated_ko.xml`
- PX4 JSBSim bridge 모델: `/home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/standard_vtol_demo_motor_updated_ko_px4.xml`
- PX4 airframe: `/home/junyeopkwon/px4_versions/PX4-v1.16.0/ROMFS/px4fmu_common/init.d-posix/airframes/3021_jsbsim_standard_vtol_demo_motor_updated_ko_px4`
- PX4 JSBSim bridge config: `/home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/configs/standard_vtol_demo_motor_updated_ko_px4.xml`

## 결론

멀티콥터 hover가 가능하지만 고정익 전환에서 문제가 나는 가장 유력한 원인은 JSBSim 공력 table 이전에 PX4 설정과 bridge 매핑이 아직 표준 VTOL 구성이 아니라는 점이다.

현재 airframe은 `rc.mc_defaults`, `@type Quadrotor Wide`, `CA_AIRFRAME 0`, `CA_ROTOR_COUNT 4`로 설정되어 있다. 이 조합은 PX4가 기체를 순수 멀티콥터로 초기화하게 만든다. 표준 VTOL 전환에 필요한 `rc.vtol_defaults`, `VT_TYPE 2`, `CA_AIRFRAME 2`, 5번째 전방추진 로터, 조종면 servo control allocation, fixed-wing tuning parameter가 빠져 있다.

또한 JSBSim bridge config는 actuator index 0-4만 `fcs/esc-cmd-norm[0..4]`로 전달한다. 반면 분리 XML의 `FlightControl.xml`은 `fcs/aileron-cmd-norm`, `fcs/elevator-cmd-norm`, `fcs/rudder-cmd-norm` 입력을 기대한다. 따라서 현재 구성에서는 PX4의 fixed-wing 조종면 출력이 JSBSim 모델로 들어가지 않는다.

## 현재 구성의 문제점

1. PX4 vehicle type이 VTOL이 아니다.

현재 3021 airframe은 `rc.mc_defaults`와 `CA_AIRFRAME 0`을 사용한다. 이 상태에서는 전환 관리, fixed-wing controller, VTOL-specific mixer/control allocation 경로가 표준 VTOL 예제와 다르게 동작한다.

2. 전방추진 로터가 VTOL allocation에 포함되어 있지 않다.

현재 `PWM_MAIN_FUNC5 105`는 있지만 `CA_ROTOR_COUNT 4`라서 control allocation 측면에서 5번째 전방추진 로터가 명확히 모델링되지 않는다. 표준 VTOL 예제는 `CA_ROTOR_COUNT 5`와 `CA_ROTOR4_AX 1`을 함께 둔다.

3. 조종면 명령이 JSBSim에 연결되어 있지 않다.

현재 bridge config는 `fcs/esc-cmd-norm[0..4]`만 갱신한다. 하지만 JSBSim `FlightControl.xml`은 `fcs/aileron-cmd-norm`, `fcs/elevator-cmd-norm`, `fcs/rudder-cmd-norm` 입력을 사용한다. 따라서 전환 후 fixed-wing controller가 roll/pitch/yaw 조종면 출력을 만들어도 현재 bridge 설정으로는 JSBSim 조종면 property가 움직이지 않는다.

4. airspeed 센서 경로가 빠져 있다.

현재 bridge config의 `<sensors>`에는 `imu`, `gps`, `barometer`, `magnetometer`만 있다. JSBSim bridge에는 `SensorAirspeedPlugin`이 있고, `rascal.xml` 예제처럼 `<airspeed>` 블록을 추가하면 차압 기반 airspeed를 전달할 수 있다. 표준 VTOL 전환과 fixed-wing 제어는 airspeed 정보에 민감하므로, 전환 안정성 검증 전 airspeed 센서/파라미터 경로를 명시해야 한다.

5. 공력/트림은 아직 2차 검증 대상이다.

PX4 VTOL 설정과 조종면 연결을 고친 뒤에도 `Aero.xml`의 `CL`, `CD`, `Cm`, `Cl_da`, `Cm_de`, pusher thrust, elevator sign/gain, `FW_AIRSPD_MIN/TRIM/MAX`, `VT_F_TRANS_THR`, `VT_ARSP_TRANS` 또는 전환 duration 값이 맞지 않으면 stall, pitch divergence, roll divergence가 날 수 있다. 다만 현재 발견된 구성 문제 때문에 공력 table을 먼저 원인으로 단정하기는 이르다.

## 권장 수정 순서

1. 3021 airframe을 표준 VTOL 기반으로 변경한다.

- `. ${R}etc/init.d/rc.vtol_defaults`
- `@type Standard VTOL`
- `VT_TYPE 2`
- `CA_AIRFRAME 2`
- `CA_ROTOR_COUNT 5`
- lift rotor 0-3 유지
- pusher rotor 4 추가: `CA_ROTOR4_AX 1`, `CA_ROTOR4_AZ 0`
- `VT_FWD_THRUST_EN`, `VT_F_TRANS_THR`, `FW_AIRSPD_*`, `FW_THR_*`, `FW_RR_*`, `FW_PR_*` 추가

2. 조종면 control allocation을 추가한다.

현 XML 구조 기준으로는 single-channel aileron, elevator, rudder가 가장 단순하다.

- `CA_SV_CS_COUNT 3`
- `CA_SV_CS0_TYPE 15`
- `CA_SV_CS1_TYPE 3`
- `CA_SV_CS2_TYPE 4`
- `PWM_MAIN_FUNC5..8` 또는 `PWM_MAIN_FUNC6..8` 배치를 bridge index와 일치시킴

3. bridge actuator mapping을 확장한다.

- pusher output index -> `fcs/esc-cmd-norm[4]`
- aileron output index -> `fcs/aileron-cmd-norm`
- elevator output index -> `fcs/elevator-cmd-norm`
- rudder output index -> `fcs/rudder-cmd-norm`

`ActuatorPlugin`은 config의 `<index>` 값을 PX4 `HIL_ACTUATOR_CONTROLS` 배열 index로 읽어서 지정 property에 그대로 넣는다. 따라서 airframe의 `PWM_MAIN_FUNC*` 순서와 bridge index를 반드시 맞춰야 한다.

4. airspeed 센서를 추가하고 PX4 파라미터를 맞춘다.

bridge config에 `<airspeed>`를 추가하고, 필요하면 `SENS_EN_ARSPDSIM 1`을 airframe에 설정한다. JSBSim 차압 property 기본값을 그대로 쓸 수 있는지 확인하고, 전환 로그에서 `airspeed_validated`, `airspeed`, `vehicle_air_data`를 확인한다.

5. 실제 전환 로그로 2차 원인을 분리한다.

구성 변경 후 QGC 또는 scripted MAVLink로 MC hover -> front transition -> FW hold를 실행하고 `vehicle_status.nav_state`, `vtol_vehicle_status`, `actuator_outputs`, `actuator_controls`, `vehicle_local_position`, `vehicle_attitude`, `airspeed_validated`, JSBSim CSV의 `velocities/vt-fps`, `aero/alpha-deg`, `fcs/*-cmd-norm`, `fcs/esc-out[4]`를 확인한다.

## 현재 판단

현 상태에서 전환 문제가 나는 1순위 원인은 PX4 airframe이 순수 멀티콥터 설정이라는 점이다. 2순위는 고정익 조종면 bridge mapping 누락이다. 3순위는 airspeed 센서/전환 속도 파라미터 누락이다. 공력 table과 trim 문제는 이 세 가지를 연결한 뒤 로그로 확인해야 한다.
