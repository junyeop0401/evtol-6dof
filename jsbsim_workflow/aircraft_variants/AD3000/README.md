# AD3000 JSBSim 시드 모델

이 폴더는 제공된 AD3000 자료를 기준으로 구성한 JSBSim용 lift-plus-cruise VTOL 시드 모델이다. 기존 ADS, F450, MiniTalon 모델은 수정하지 않고 AD3000 신규 aircraft로 분리했다.

## 사용한 원본 자료

- 질량, 부품 위치, 관성 계산: D:/ADSystem/ad3000/DB 정리.xlsx
- 공력 계수: D:/ADSystem/ad3000/jsbsim_aerodynamic_database.xml
- 형상 범위 확인: D:/ADSystem/ad3000/AD3000_CFD.step
- 구조 참고: D:/ProjectAirSim-jsbsim/core_sim/jsbsim/models/aircraft/standard_vtol_demo/standard_vtol_demo.xml

## 주요 적용 값

- 총 질량: 14.9425 kg
- JSBSim nose datum 기준 CG: x=0.3727 m aft, y=-0.0002 m right, z=-0.0140 m up
- JSBSim 축 기준 관성: Ixx=0.5270, Iyy=1.7727, Izz=2.2370 kg*m2
- DATCOM 기준 공력 형상: S=1.0650005 m2, b=3.0 m, c=0.36967129 m
- lift rotor 크기 산정 목표: rotor별 정지 최대추력 약 73.3 N, hover 기준 rotor별 평균 추력 약 36.6 N
- 동일 collective 기준 hover throttle 추정값: 약 0.71

## 좌표계

기체 XML의 구조 좌표는 nose datum 기준 JSBSim 좌표계인 x aft, y right, z up을 사용한다.

XLSX/STEP 축은 부품 배치와 STEP bounding box를 기준으로 다음처럼 해석했다.

- workbook/STEP F/X: spanwise left-positive
- workbook/STEP G/Y: vertical up-positive
- workbook/STEP H/Z: longitudinal aft-negative

따라서 JSBSim 위치 변환은 다음과 같다.

- x_jsbsim = -H_mm / 1000
- y_jsbsim = -F_mm / 1000
- z_jsbsim = G_mm / 1000

## 추진계 산정 근거

모터와 프롭은 아직 실측/제품 확정값이 없으므로 질량 기반 placeholder로 구성했다.

- lift motor/prop: 총 thrust-to-weight 약 2.0을 목표로 4개 rotor에 분배했다.
- rotor별 최대 추력 목표는 14.9425 kg * 9.80665 * 2 / 4 = 73.27 N이다.
- hover 평균 추력은 14.9425 kg * 9.80665 / 4 = 36.63 N이다.
- 20 inch급 저 KV 12S lift prop/motor placeholder를 적용했다.
- pusher는 transition/cruise 초기 검토용으로 15 inch급 12S placeholder를 적용했다.

## 현재 검증 상태

- XML well-formed 검사는 통과했다.
- JSBSim --aircraft=AD3000 --catalog 로딩은 통과했다.
- smoke runscript --end=1.5 짧은 통합 실행은 통과했다.
- 8초 전체 hover smoke run은 약 2초 이후 Floating point exception으로 실패했다.

## 남은 주요 리스크

현재 CG가 전방 rotor 쪽에 가까워 동일 collective 입력만으로는 큰 pitch moment가 발생한다. hover 안정화를 위해 front/rear rotor 추력 split 또는 실제 CG/rotor 위치 재검토가 필요하다.
