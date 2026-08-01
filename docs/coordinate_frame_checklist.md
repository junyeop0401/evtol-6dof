# 좌표계 / 부호 규약 검증 체크리스트

jsbsim-bridge에서 JSBSim ↔ PX4 값을 주고받을 때 부호/축 정의가 뒤집히는 게
가장 흔한 실수. 아래 항목을 값 하나하나 실제 로그 찍어서 확인할 것.

## 좌표계 기본 정의

- [ ] JSBSim body axis 정의 확인 (X: 기수 방향, Y: 우측, Z: 하방 — 버전/설정에 따라
      다를 수 있으니 문서로 재확인)
- [ ] PX4는 NED(북-동-하) local frame + FRD(전-우-하) body frame 사용
- [ ] JSBSim의 지구고정좌표계(ECEF/geodetic)와 PX4 local NED 원점(home position)
      정의 일치 여부

## 자세(Attitude)

- [ ] Euler angle 순서(roll-pitch-yaw, 321 순서) JSBSim/PX4 동일한지
- [ ] 쿼터니언 사용 시 스칼라 성분 위치(w,x,y,z vs x,y,z,w) 확인
- [ ] 기준 자세(레벨 비행 시 pitch=0) 정의가 두 시스템에서 같은지

## 각속도 / 선속도

- [ ] 각속도(p,q,r) body frame 부호 일치 여부
- [ ] 속도 벡터가 body frame인지 NED frame인지 bridge 코드에서 명확히 구분되는지

## 추력/액추에이터

- [ ] 모터 추력 방향(양수=추력 방향) 정의 통일
- [ ] 틸트 액추에이터 각도 기준(0도 = 수직/수평 어느 쪽인지) 통일
- [ ] PX4 actuator_controls 출력 범위(-1~1 또는 0~1)와 JSBSim FCS 입력 범위 매핑 확인

## 검증 방법

1. 정지 상태(hover, 자세 0)에서 값 하나씩 로그 찍어서 기대값과 비교
2. 단순 입력(예: pitch만 5도) 줬을 때 양쪽에서 부호가 같은 방향으로 움직이는지 확인
3. 위 결과를 대조 검증
