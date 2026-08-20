# PX4 JSBSim QGC 실행 매뉴얼

대상 모델은 `standard_vtol_demo_hover_px4`입니다. 이 모델은 PX4/QGC가 제어를 담당하고, JSBSim은 공력, 추력, 질량, 지상반력, 외력 계산만 담당합니다.

## 1. 기본 경로

- JSBSim workflow:
  - `/home/junyeopkwon/evtol-6dof/jsbsim_workflow`
- PX4:
  - `/home/junyeopkwon/px4_versions/PX4-v1.16.0`
- QGroundControl AppImage:
  - `/home/junyeopkwon/Downloads/QGroundControl-x86_64.AppImage`
- PX4 ULog 저장 위치:
  - `/home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/YYYY-MM-DD/HH_MM_SS.ulg`
- combined CSV 저장 위치:
  - `/home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/combined/standard_vtol_demo_hover_px4/<ulog_name>/`

## 2. 추천 실행 방법

Ubuntu 터미널에서 아래처럼 실행합니다.

```bash
cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts
python3 run_px4_jsbsim_qgc_workflow.py --launch-qgc
```

이 스크립트가 하는 일:

- QGC AppImage 실행
- PX4 JSBSim SITL 실행
- `jsbsim_standard_vtol_demo_hover_px4__RKSS` target 실행
- QGC가 붙을 수 있도록 UDP 14550 열림
- PX4 종료 후 최신 `.ulg`를 찾아 combined CSV로 변환

PX4 shell이 뜨면 터미널에 `pxh>` 프롬프트가 보입니다. 미션 확인이 끝나면 아래 명령으로 종료합니다.

```px4
shutdown
```

종료 후 스크립트가 최신 `.ulg`와 변환된 combined CSV 경로를 출력합니다.

## 3. 수동 실행 방법

### 3.1 QGC 실행

Ubuntu 터미널에서 QGC를 먼저 켭니다.

```bash
/home/junyeopkwon/Downloads/QGroundControl-x86_64.AppImage
```

실행 권한 오류가 나면 한 번만 실행 권한을 줍니다.

```bash
chmod +x /home/junyeopkwon/Downloads/QGroundControl-x86_64.AppImage
/home/junyeopkwon/Downloads/QGroundControl-x86_64.AppImage
```

AppImage/FUSE 문제가 나면 압축 해제된 실행 파일을 사용할 수 있습니다.

```bash
/home/junyeopkwon/Downloads/squashfs-root/usr/bin/QGroundControl
```

### 3.2 PX4 JSBSim bridge 실행

다른 Ubuntu 터미널에서 PX4를 실행합니다. 기본 위치는 김포공항 14번 활주로(RKSS)입니다.

```bash
cd /home/junyeopkwon/px4_versions/PX4-v1.16.0
HEADLESS=1 JSBSIM_QUIET=1 make px4_sitl jsbsim_standard_vtol_demo_hover_px4__RKSS
```

정상 연결이면 터미널에 아래 로그가 보여야 합니다.

```text
INFO  [init] found model autostart file as SYS_AUTOSTART=3020
INFO  [simulator_mavlink] Simulator connected on TCP port 4560.
INFO  [logger] Opened full log file: ./log/YYYY-MM-DD/HH_MM_SS.ulg
```

## 4. QGC에서 미션 넣는 순서

QGC가 자동 연결되면 상단에 vehicle 연결 상태가 표시됩니다.

1. `Plan` 화면으로 이동
2. `Takeoff` 추가
3. waypoint 또는 시험 코스 추가
4. `Land` 추가
5. `Upload` 클릭
6. `Fly` 화면으로 이동
7. Arm 가능 상태 확인
8. 미션 시작
9. 미션 종료 후 PX4 터미널에서 `shutdown`

초기 검증 단계에서는 복잡한 미션보다 아래 순서가 좋습니다.

```text
Arm -> Takeoff 5~10 m -> Hover -> Land -> Disarm
```

## 5. 로그 저장과 CSV 변환

PX4는 실행 중 logger가 자동으로 `.ulg`를 저장합니다.

예:

```text
/home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-14/00_55_52.ulg
```

자동화 스크립트를 사용하면 종료 후 자동으로 combined CSV가 생성됩니다.

수동 변환은 아래처럼 실행한 뒤 목록에서 `.ulg` 번호를 선택합니다.

```bash
cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow
python3 scripts/px4_ulog_to_combined_csv.py
```

특정 `.ulg`를 바로 지정하는 기존 방식도 계속 사용할 수 있습니다.

```bash
cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow
python3 scripts/px4_ulog_to_combined_csv.py \
  /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-14/00_55_52.ulg
```

To merge PX4 ULog data with JSBSim applied properties and generate plots, run this command and select a `.ulg` number.

```bash
cd /home/junyeopkwon/evtol-6dof/jsbsim_workflow
python3 scripts/px4_jsbsim_compare_plot.py
```

Output is written under:

```text
/home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/combined_px4_jsbsim/standard_vtol_demo_hover_px4/<ulog_name>/
```

The output folder contains PX4 combined CSV, JSBSim property CSV, PX4+JSBSim merged CSV, and `plots/*.png` files.

topic별 CSV가 필요하면 `ulog2csv`를 직접 사용할 수 있습니다.

```bash
ulog2csv \
  -m actuator_outputs,vehicle_status,vehicle_local_position,vehicle_attitude,vehicle_gps_position,estimator_status,sensor_combined \
  -o /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/px4_ulog/standard_vtol_demo_hover_px4/manual \
  /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-14/00_55_52.ulg
```

## 6. 자주 보는 PX4 shell 명령

PX4 터미널의 `pxh>` 프롬프트에서 사용합니다.

```px4
listener actuator_outputs 1
listener vehicle_status 1
listener vehicle_local_position 1
listener vehicle_attitude 1
commander status
logger status
```

actuator 연결만 빠르게 확인할 때:

```px4
actuator_test set -m 1 -v 0.2 -t 1
listener actuator_outputs 1
actuator_test set -m 5 -v 0.2 -t 1
listener actuator_outputs 1
```

기대값:

- motor 1 -> `actuator_outputs.output[0]` 증가
- motor 2 -> `actuator_outputs.output[1]` 증가
- motor 3 -> `actuator_outputs.output[2]` 증가
- motor 4 -> `actuator_outputs.output[3]` 증가
- motor 5 -> `actuator_outputs.output[4]` 증가

## 7. 문제 해결

### QGC가 연결되지 않음

우선 WSL 안에서 QGC AppImage를 실행하는 방식을 사용합니다. Windows에서 QGC를 켜면 WSL2 UDP localhost 연결이 환경에 따라 막힐 수 있습니다.

확인할 로그:

```text
INFO  [mavlink] mode: Normal ... udp port 18570 remote port 14550
```

### `Unknown model jsbsim_standard_vtol_demo_hover_px4`

ROMFS airframe 목록이 build rootfs에 반영되지 않은 상태입니다. 아래를 한 번 실행합니다.

```bash
cd /home/junyeopkwon/px4_versions/PX4-v1.16.0
DONT_RUN=1 HEADLESS=1 make px4_sitl jsbsim_standard_vtol_demo_hover_px4__RKSS
```

### `ekf2 missing data`

시작 직후에는 EKF 데이터가 아직 충분하지 않을 수 있습니다. QGC에서 바로 arm하지 말고 5~10초 기다린 뒤 상태를 확인합니다.

```px4
listener vehicle_status 1
listener vehicle_local_position 1
```

### 로그는 생겼는데 CSV 컬럼이 적음

짧은 actuator test 로그에는 position/attitude topic이 적게 남을 수 있습니다. 실제 mission을 수행하면 `vehicle_local_position`, `vehicle_attitude`, `vehicle_gps_position` 계열 컬럼이 더 채워집니다.

## 8. 주의 사항

- QGC mission 검증에서는 JSBSim standalone runscript를 사용하지 않습니다.
- PX4용 모델에서는 JSBSim 내부 hover controller가 제거되어 있습니다.
- 멀티콥터 자동 제어는 4개 lift rotor 기준입니다.
- 5번째 pusher는 actuator path 확인용으로 연결되어 있지만 현재 멀티콥터 control allocation geometry에는 포함하지 않았습니다.
- 실제 takeoff 전에는 roll/pitch/yaw 부호와 rotor geometry를 짧은 저고도 테스트로 확인해야 합니다.

## 9. standard_vtol_demo_motor_updated_ko_px4 직접 실행

이번에 연결한 새 후보 모델은 `standard_vtol_demo_motor_updated_ko_px4`입니다. 현재 검증 기준은 `20.0 kg` 질량, `MPC_THR_HOVER=0.535`, RKSS scene입니다.

### 9.1 빌드와 등록만 확인

PX4 target 등록이 반영되는지 먼저 확인할 때 사용합니다. 실제 시뮬레이션은 실행하지 않습니다.

```bash
cd /home/junyeopkwon/px4_versions/PX4-v1.16.0
DONT_RUN=1 HEADLESS=1 make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS
```

정상 결과 예:

```text
Not running simulation (DONT_RUN is set).
```

### 9.2 PX4 shell에서 직접 arm-hover-land

QGC 없이 터미널에서 바로 확인하려면 아래처럼 실행합니다.

```bash
cd /home/junyeopkwon/px4_versions/PX4-v1.16.0
HEADLESS=1 JSBSIM_LOG_ONLY=1 make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS
```

`pxh>` 프롬프트가 뜨고 `Ready for takeoff!`가 보이면 아래 명령을 순서대로 입력합니다.

```px4
commander arm
commander takeoff
commander land
shutdown
```

권장 대기 시간:

- 시작 후 `Ready for takeoff!`까지 약 10초 대기
- `commander arm` 후 약 5초 대기
- `commander takeoff` 후 10~20초 정도 짧게 hover 확인
- `commander land` 후 `Landing detected`, `Disarmed by landing` 확인

성공 시 확인할 로그:

```text
INFO  [commander] Ready for takeoff!
INFO  [commander] Armed by internal command
INFO  [navigator] Using default takeoff altitude: 2.5 m
INFO  [commander] Takeoff detected
INFO  [commander] Landing at current position
INFO  [commander] Landing detected
INFO  [commander] Disarmed by landing
```

### 9.3 한 번에 자동 실행

동일 시퀀스를 자동으로 흘려보낼 때 사용합니다. 실행 로그는 `/tmp/px4_motor_updated_hover/arm_hover_land_20kg_manual.log`에 저장됩니다.

```bash
cd /home/junyeopkwon/px4_versions/PX4-v1.16.0
mkdir -p /tmp/px4_motor_updated_hover
{
  sleep 10
  echo "commander arm"
  sleep 5
  echo "commander takeoff"
  sleep 15
  echo "commander land"
  sleep 18
  echo "shutdown"
} | env \
  HEADLESS=1 \
  JSBSIM_LOG_ONLY=1 \
  JSBSIM_LOG_FILTER="\[JSBSIM\]|\[GPS\]|commander|Commander|arming|Arming|takeoff|Takeoff|land|Land|health_and_arming|WARN|ERROR|INFO" \
  make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS \
  > /tmp/px4_motor_updated_hover/arm_hover_land_20kg_manual.log 2>&1
```

### 9.4 결과 빠른 확인

콘솔 로그에서 arm/takeoff/land/disarm이 모두 찍혔는지 확인합니다.

```bash
grep -En \
  "Armed by internal command|Using default takeoff altitude|Takeoff detected|Landing at current position|Landing detected|Disarmed by landing" \
  /tmp/px4_motor_updated_hover/arm_hover_land_20kg_manual.log
```

NaN, FPE, crash, arming 실패가 없는지 확인합니다.

```bash
grep -Eic \
  "(^|[^A-Za-z])nan([^A-Za-z]|$)|Floating point|CRASH DETECTED|Preflight Fail|Arming denied|Takeoff denied|failsafe|ERROR" \
  /tmp/px4_motor_updated_hover/arm_hover_land_20kg_manual.log
```

결과가 `0`이면 해당 패턴은 발견되지 않은 것입니다.

JSBSim CSV 위치:

```text
/home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/jsbsim_bridge/standard_vtol_demo_motor_updated_ko_px4/latest_jsbsim_properties.csv
```

최신 PX4 ULog 위치는 보통 아래 폴더에 생성됩니다.

```text
/home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/YYYY-MM-DD/HH_MM_SS.ulg
```

최신 `.ulg`를 확인하려면:

```bash
find /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log \
  -type f -name "*.ulg" -printf "%T@ %p %s\n" | sort -n | tail -5
```

### 9.5 현재 알려진 한계

이번 검증 run에서는 arm, takeoff, 약 1 m 저고도 hover, landing, disarm까지 성공했습니다. 다만 PX4 기본 takeoff altitude는 `2.5 m`였고 실제 JSBSim AGL 최대값은 약 `1.03 m`였습니다. 목표고도 2.5 m까지 정확히 추종하려면 land 명령 대기 시간을 늘리고, `vehicle_local_position`, setpoint, actuator command, JSBSim AGL을 같이 비교해야 합니다.

### 9.6 QGC에서 명령 넣기

QGC에서 조작하려면 PX4/JSBSim은 터미널에서 실행해 두고, QGC는 같은 SITL vehicle에 붙여서 명령만 넣습니다.

먼저 QGC를 실행합니다.

```bash
/home/junyeopkwon/Downloads/QGroundControl-x86_64.AppImage
```

다른 터미널에서 새 모델 SITL을 실행합니다.

```bash
cd /home/junyeopkwon/px4_versions/PX4-v1.16.0
HEADLESS=1 JSBSIM_LOG_ONLY=1 make px4_sitl jsbsim_standard_vtol_demo_motor_updated_ko_px4__RKSS
```

QGC 상단에 vehicle이 연결되고, PX4 터미널에 `Ready for takeoff!`가 보이면 QGC에서 아래 중 하나로 진행합니다.

#### 방법 A: Fly 화면 버튼으로 실행

1. QGC 왼쪽에서 `Fly` 화면으로 이동
2. 상단 상태가 ready인지 확인
3. 왼쪽/상단의 `Arm` 또는 `Takeoff` 액션 선택
4. takeoff altitude는 처음에는 낮게 설정. 현재 검증 기준은 약 1 m 저고도 hover만 확인됨
5. 기체가 떠서 안정되면 `Land` 선택
6. 착륙 후 QGC 또는 PX4 로그에서 disarm 확인

#### 방법 B: QGC MAVLink Console에서 명령 입력

QGC에서 `Analyze Tools` 또는 `Widgets` 메뉴의 `MAVLink Console`을 열고 아래 PX4 shell 명령을 입력합니다. QGC 버전에 따라 메뉴 이름은 약간 다를 수 있습니다.

```px4
commander arm
commander takeoff
commander land
```

종료는 PX4를 실행한 터미널의 `pxh>`에서 하는 편이 가장 확실합니다.

```px4
shutdown
```

QGC에서 성공 여부를 볼 때는 다음 상태 메시지가 핵심입니다.

```text
Armed
Takeoff detected
Landing detected
Disarmed
```

PX4 터미널 로그 기준 성공 패턴은 아래와 같습니다.

```text
INFO  [commander] Armed by internal command
INFO  [commander] Takeoff detected
INFO  [commander] Landing at current position
INFO  [commander] Landing detected
INFO  [commander] Disarmed by landing
```

주의: QGC 버튼 방식은 takeoff altitude/setpoint를 QGC UI가 보낸 값으로 사용합니다. 현재 모델은 기본 `2.5 m` takeoff 명령에서 실제 JSBSim AGL 약 `1.03 m`까지만 확인됐으므로, 처음에는 낮은 고도와 짧은 hover로 확인하는 것이 좋습니다.


## 10. 새 모델 XML 분리 구조

`standard_vtol_demo_motor_updated_ko` 모델은 F450 스타일로 분리되어 있습니다. 주 XML 파일은 실행 진입점이고, 실제 내용은 아래 모듈 파일로 나뉩니다.

```text
standard_vtol_demo_motor_updated_ko.xml
Metrics.xml
Mass.xml
Gear.xml
Effectors.xml
FlightControl.xml
ExternalReactions.xml
Aero.xml
Monolithic.xml
```

PX4 bridge 쪽도 같은 구조입니다.

```text
/home/junyeopkwon/px4_versions/PX4-v1.16.0/Tools/simulation/jsbsim/jsbsim_bridge/models/standard_vtol_demo_motor_updated_ko_px4/
```

수정할 때 기준:

- 기체 치수: `Metrics.xml`
- 질량/CG/관성: `Mass.xml`
- 착륙장치/접지: `Gear.xml`
- actuator 입력/토크 계산: `Effectors.xml`
- 조종면 변환: `FlightControl.xml`
- 모터/푸셔 힘 위치와 추력 table: `ExternalReactions.xml`
- 공력 table: `Aero.xml`
- 기존 단일본 참조: `Monolithic.xml`

PX4에서 실제 실행되는 모델은 `standard_vtol_demo_motor_updated_ko_px4.xml`입니다. 이 파일은 모듈 include와 CSV output 설정을 포함합니다.
