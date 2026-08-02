# 좌표계 / 부호 규약 검증 체크리스트

jsbsim-bridge에서 JSBSim ↔ PX4 값을 주고받을 때 부호/축 정의가 뒤집히는 게
가장 흔한 실수. 아래 항목을 값 하나하나 실제 로그 찍어서 확인할 것.

## 좌표계 기본 정의

- [ ] JSBSim body axis 정의 확인 (X: 기수 방향, Y: 우측, Z: 하방 — 버전/설정에 따라
      다를 수 있으니 문서로 재확인)
- [ ] PX4는 NED(북-동-하) local frame + FRD(전-우-하) body frame 사용
- [ ] JSBSim의 지구고정좌표계(ECEF/geodetic)와 PX4 local NED 원점(home position)
      정의 일치 여부

## 구조좌표계(structural) vs 동체좌표계(body) — 이 프로젝트에서 가장 흔한 실수 지점

- [x] (문서상 확인, 실행검증 대기) JSBSim은 두 개의 서로 다른 좌표계를 쓴다.
      (1) 구조좌표계(structural frame): 질량중심(CG), 엔진, 랜딩기어 등
      "형상/위치"를 정의하는 `<location>` 요소에 쓰이며, X는 기체 **후방(aft)이
      양수**, Z는 **위(up)가 양수**다. (2) 동체좌표계(body frame): 속도, 각속도,
      공력 계산에 쓰이며, X는 **기수(전방, forward)가 양수**, Z는 **하방(down)이
      양수**다. 즉 X와 Z의 부호 기준이 서로 반대다(Y는 우측이 양수로 두 좌표계가
      동일).
- [x] (문서상 확인, 실행검증 대기) 근거: JSBSim 공식 저장소(JSBSim-Team/jsbsim)의
      F450 쿼드콥터 예제 Propulsion.xml에서 전방 모터(front right, front left)의
      `<location>` x 좌표가 **음수(-0.1651)**로, 후방 모터(aft left, aft right)는
      **양수(+0.1651)**로 표기되어 있다. 이는 구조좌표계(X=aft+) 관례를 그대로
      따른 것이며, 동체좌표계(X=forward+)로 착각해 부호를 반대로 넣으면 전후방
      모터 위치가 뒤바뀌어 피치 축 제어가 정반대로 동작하게 된다. 이번 프로젝트의
      `models/aircraft/QuadX_Baseline.xml`도 동일한 구조좌표계 부호 관례를 그대로
      재사용해 작성했고(front right/front left: x=-0.1651, aft left/aft right:
      x=+0.1651), `models/systems/QuadX_FCS.xml`의 피치 믹서 부호를 이 좌표계
      기준으로 직접 모멘트 계산(τ=r×F)까지 재검산해 정합성을 확인했다. 자세한
      계산 과정은 `docs/QuadX_Baseline_model.md` 4절 참고.
- [ ] (실행 검증 미실시) 위 문서상 확인 내용을 실제 JSBSim 실행 로그(예:
      QuadX_control_response_test.xml 실행 후 CSV에서 피치 펄스 부호와
      attitude/theta-rad 변화 방향 대조)로 재확인할 것. 이번 세션은 실행이
      불가능한 환경이었으므로 아직 로그 기반 확인이 이루어지지 않았다.
- [ ] jsbsim-bridge/PX4 연동 시에는 이 구조좌표계가 아니라 동체좌표계(및 PX4의
      FRD)가 기준이 되므로, bridge 코드에서 위치 관련 값을 다룰 때 어느
      좌표계인지 반드시 재확인할 것(구조좌표계 값을 그대로 PX4에 넘기면 안 됨).
- [x] (별개 기체에서 교차 확인, 문서상) `jsbsim_workflow/aircraft_variants/LiftCruise2kg/Propulsion.xml`
      도 동일한 구조좌표계 부호 관례를 쓴다(전방 리프트 모터 x=-0.250 M, 후방
      리프트 모터 x=+0.250 M). QuadX_Baseline과 독립적으로 만들어진 별개 기체
      정의에서 같은 부호 규약이 재확인된 것이므로, 위 F450 근거와 더불어 이 부호
      관례가 이 프로젝트/jsbsim_workflow 전반에서 일관되게 적용되고 있다는
      근거가 하나 더 늘었다(단, 이 역시 문서 대조 확인이며 LiftCruise2kg 자체의
      실행 로그로 부호를 재확인한 것은 아님). 상세는
      `reference/docs/lessons_learned.md` 4절 참고.

## AGL vs MSL — `initialize/altitude` 해석 (실행 검증됨)

- [x] (실행 검증 완료) JSBSim 1.2.4의 `initialize/altitude`는 문서상 기대(해수면
      기준 MSL)와 달리 지형 고도 위의 AGL 높이로 해석된다. Codex가
      QuadX_Baseline 실행에서 직접 확인했고(`docs/STATUS.md` 2026-08-01 로그),
      `jsbsim_workflow`의 F450/LiftCruise2kg 미션 스크립트들도 동일 전제로
      작성되어 있어(예: 호버 목표 고도를 `position/h-agl-ft`와 직접 비교) 서로
      다른 시점·다른 기체에서 같은 결론이 재확인됐다. 틸트로터 본체의 초기조건도
      AGL 기준으로 설계할 것. 상세는 `reference/docs/lessons_learned.md` 1절 참고.

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

## 2026-08-01 Codex 실행 검증 메모

- [x] scripts/QuadX_control_response_test.xml을 JSBSim 1.2.4에서 실행해 양의 aileron/elevator/rudder 명령이 각각 양의 velocities/p-rad_sec, velocities/q-rad_sec, velocities/r-rad_sec 응답을 만드는 것을 CSV로 확인했다.
- [ ] scripts/QuadX_nominal_mission.xml은 실행은 되지만 10m급 호버/착지 프로파일이 아직 불합격이므로, 정상 미션 기반의 최종 좌표계/운용 검증은 대기 상태로 둔다.
