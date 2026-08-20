# AD3000 가정 및 한계

## 현재 가정

- 이 모델은 JSBSim 통합용 시드 모델이며, 비행시험으로 검증된 최종 모델이 아니다.
- 공력 기준값은 제공된 jsbsim_aerodynamic_database.xml의 DATCOM 형상과 계수 테이블을 우선한다.
- STEP bounding box는 SOURCE_MATRIX.csv에 추적용으로 기록했지만 DATCOM span을 대체하지 않았다. STEP에서 추출한 span-like extent와 공력 DB의 wingspan 값이 서로 다르기 때문이다.
- DB 정리.xlsx의 F60 셀은 mac LE로 표시되어 있어 lateral CG로 직접 사용하지 않았다. lateral CG는 부품 질량과 F 좌표로 재계산했다.
- products of inertia, 즉 Ixy, Ixz, Iyz는 최종 CAD mass property가 JSBSim 좌표계로 export되기 전까지 0으로 둔다.
- lift motor와 propeller는 총 질량 기준으로 산정한 placeholder다. 현재 목표는 VTOL 제어 여유를 위해 총 thrust-to-weight 약 2.0을 확보하는 것이다.
- pusher motor와 propeller는 15 kg급 기체의 초기 cruise/transition 검토용 placeholder다.

## 추진계 산정 한계

- lift rotor 최대 추력 목표는 rotor별 약 73.27 N이다.
- hover 평균 추력은 rotor별 약 36.63 N이다.
- 현재 FlightControl.xml은 동일 collective를 4개 lift rotor에 배분한다.
- 하지만 CG가 전방 rotor 쪽에 가까우므로 실제 hover에는 front/rear 추력 split이 필요하다.
- 현재 CG와 rotor x 위치 기준 정적 pitch moment 균형 추력은 front rotor 약 60.3 N each, aft rotor 약 13.0 N each로 추정된다.
- 이 split은 실제 CG, rotor hub 위치, thrust line이 확정되면 다시 계산해야 한다.

## 현재 검증 한계

- XML 문법 검사는 통과했다.
- JSBSim catalog load는 통과했다.
- 1.5초 짧은 통합 실행은 통과했다.
- 8초 smoke hover 실행은 Floating point exception으로 실패했다.
- 따라서 현재 모델은 aircraft 구성과 초기 로딩 검증까지 완료된 상태이며, 안정 hover 모델로 간주하면 안 된다.

## 필요한 후속 작업

- 실제 CAD에서 nose datum 기준 CG와 inertia tensor를 export한다.
- DATCOM moment reference point를 확인하고 AERORP가 CG와 다른 경우 Metrics.xml을 수정한다.
- lift rotor front/rear collective split을 FlightControl.xml에 반영한다.
- ground reaction의 spring, damping, contact 위치를 정지 자세 기준으로 재튜닝한다.
- 실제 모터, 프롭, ESC, 배터리 전압 강하 데이터를 확보해 제품 기반 motor/prop XML을 재보정한다. 특히 cruise는 원래 의도한 Falcon C2E 20x10 직접 thrust/power sheet 확보 후 AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml의 임시 적용값을 교체해야 한다.
- 조종면 최대 deflection과 부호를 실측한 뒤 DATCOM control property와 연결한다.
