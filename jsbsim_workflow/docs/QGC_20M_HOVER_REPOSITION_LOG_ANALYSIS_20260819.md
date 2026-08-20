# QGC 20m hover/reposition 로그 분석

- 분석 시각: 2026-08-19 11:33 KST
- 분석 대상 ULog: /home/junyeopkwon/px4_versions/PX4-v1.16.0/build/px4_sitl_default/rootfs/log/2026-08-19/02_20_29.ulg
- ULog 크기: 54 MB
- SHA256: e0925f38777a12f13d326835ce8f191a2a8283d37087d6c1e4aa38ca177218cc
- 관련 JSBSim CSV: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/jsbsim_bridge/standard_vtol_demo_motor_updated_ko_px4/latest_jsbsim_properties.csv

## 요약

QGC에서 실행한 것으로 보이는 최신 PX4 ULog를 분석했다. 로그 duration은 약 184.996 s이고 dropout은 없었다. 외부 명령으로 arming 되었고 takeoff가 감지되었으며, 이후 reposition 명령 3회와 orbit 명령 1회가 수락되었다. 고도는 약 20 m 부근까지 상승했고, 마지막 reposition 목표점에는 거의 정확히 도달했다. 단, 로그 마지막 상태는 착륙/Disarm이 아니라 armed + in-air + ORBIT 상태였다.

## 비행 상태 전이

- arming_state: 0.0 s STANDBY -> 14.1 s ARMED
- nav_state: 0.0 s AUTO_LOITER -> 14.1 s AUTO_TAKEOFF -> 19.8 s AUTO_LOITER -> 174.3 s ORBIT
- vehicle_land_detected: 0.0 s landed=1 -> 15.58 s landed=0
- ground_contact: 0.0 s ground_contact=1 -> 15.808 s ground_contact=0
- 로그 끝 상태: ARMED, landed=0, nav_state=ORBIT

## QGC 명령 및 ACK

- VEHICLE_CMD_NAV_TAKEOFF(22): ACK result=0
- VEHICLE_CMD_COMPONENT_ARM_DISARM(400): ACK result=0
- VEHICLE_CMD_DO_REPOSITION(192): 3회 ACK result=0
- VEHICLE_CMD_DO_ORBIT(34): ACK result=0
- 로그 메시지: Ready for takeoff, Armed by external command, Takeoff detected 확인
- 로그 메시지에 Landing detected 또는 Disarmed 이벤트는 없음

## 고도 분석

PX4 vehicle_local_position 기준:

- duration: 184.996 s
- local altitude(-z): min -2.170 m, max 19.849 m, final 19.248 m
- 18-22 m 구간 duration: 148.904 s
- 19-21 m 구간 duration: 147.128 s
- 19.5-20.5 m 구간 duration: 1.308 s
- 20m 부근 수직속도 절대값 평균/최대: 0.353 / 1.726 m/s

JSBSim CSV 기준:

- rows: 23252
- time: 0.0-186.008 s
- AGL: min 0.169 m, max 20.999 m at 57.088 s, final 20.090 m
- NaN count: 0

해석: 사용자가 말한 20m hover는 로그와 대체로 부합한다. PX4 local altitude는 약 19.2-19.8m 부근, JSBSim AGL은 최대 약 21.0m로 나타났다.

## 위치 이동 분석

vehicle_local_position 기준:

- 시작 대비 최대 수평 이동: 263.386 m
- 종료 시 시작 대비 수평 이동: 237.450 m
- x 범위: -0.960 m to 235.529 m
- y 범위: -0.935 m to 139.132 m
- 최대 속도: 6.049 m/s

마지막 DO_REPOSITION 목표:

- target lat/lon/alt: 37.5728214, 126.7796188, 31.15109825 m
- 목표점 최근접: t=165.836 s, 수평거리 0.002 m, alt error +0.709 m
- 종료 시점: t=182.852 s, 목표점 수평거리 47.423 m, alt error +0.937 m

해석: 목표 위치에는 도달했다. 이후 174.288 s에 DO_ORBIT 명령이 들어가면서 종료 시점에는 목표점에서 다시 멀어진 상태였다.

## 이상 징후 확인

- ULog dropout: 없음
- vehicle_status.failsafe: 0 유지
- console/event messages: failsafe, land detected, disarm 메시지 없음
- JSBSim CSV NaN: 0
- actuator_motors control[0..3] max: 1.0, 1.0, 1.0, 1.0
- actuator_motors control[0..3] final: 0.398, 0.572, 0.182, 0.574
- hover_thrust_estimate: min 0.527, max 0.588, final 0.537

## 판단

- 성공: arming, takeoff, 약 20m 고도 유지, 목표 위치 이동, 명령 ACK 수락, NaN 없음
- 주의: 착륙/Disarm 없이 비행 중 ORBIT 상태에서 종료된 로그임
- 다음 확인: QGC에서 종료 전에 Land를 누른 뒤 Landing detected와 Disarmed 이벤트가 남는지 확인
