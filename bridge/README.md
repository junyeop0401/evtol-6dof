# jsbsim-bridge 연동 노트

PX4 SITL과 JSBSim을 잇는 jsbsim-bridge에서 확인/구현해야 할 것들.
설치된 jsbsim-bridge 레포 소스를 열어서 아래 항목을 채워 넣을 것.

## 데이터 흐름 방향
## 1. JSBSim → PX4 (state/sensor 값)

| PX4가 기대하는 값 | JSBSim property (확인 필요) | 좌표계 | 확인 여부 |
|---|---|---|---|
| 가속도 (accel xyz) | accelerations/... | body FRD? | [ ] |
| 각속도 (gyro xyz) | velocities/p,q,r-rad_sec | body | [ ] |
| 자세 | attitude/... | | [ ] |
| 위치(lat/lon/alt) | position/... | geodetic | [ ] |
| 속도(NED) | velocities/v-north/east/down-fps | NED | [ ] |

## 2. PX4 → JSBSim (액추에이터 명령)

| PX4 출력 | JSBSim 입력 property | 범위 | 확인 여부 |
|---|---|---|---|
| motor1 throttle | fcs/bridge/motor1-cmd-norm | 0~1? | [ ] |
| tilt actuator | fcs/bridge/tilt1-cmd-norm | | [ ] |

## 3. 다음 작업

1. jsbsim-bridge 소스에서 실제 송수신 메시지 구조체 확인
2. 위 표 채우기
3. FCS_template.xml property 이름을 bridge 코드와 일치시키기
4. 좌표계 체크리스트와 대조해서 부호 검증
