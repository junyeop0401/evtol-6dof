# F450_DATCOM 공력 적용 검증 문서

## 1. 목적

이 문서는 첨부 파일 C:/Users/junyeopkwon/Downloads/jsbsim_aerodynamic_database.xml의 flight_control, metrics, aerodynamics가 F450 파생 모델 F450_DATCOM에 실제로 적용되었는지 확인하기 위한 검증 절차와 실행 결과를 정리한다.

핵심 판단 기준은 단순 10 m hover 성공이 아니다. hover에서는 상대풍과 qbar가 작아서 공력 효과가 작거나 controller 보상에 묻힐 수 있다. 따라서 다음 6개 항목을 분리해서 확인했다.

1. XML 로딩 및 property 존재 확인
2. 공력 계수 테이블 보존 확인
3. qbar 변화에 따른 aerodynamic force/moment 응답 확인
4. 조종 입력과 aerosurface 및 coefficient 부호 확인
5. 동일 attitude-mode 미션에서 F450과 F450_DATCOM 동역학 A/B 비교
6. propulsion/controller 영향을 제거한 free-response 비교

## 2. 대상 모델과 입력 파일

- 원본 F450 실행 모델: /home/junyeopkwon/jsbsim/aircraft/F450
- 파생 F450_DATCOM 실행 모델: /home/junyeopkwon/jsbsim/aircraft/F450_DATCOM
- 프로젝트 보관 사본: /home/junyeopkwon/evtol-6dof/jsbsim_workflow/aircraft_variants/F450_DATCOM
- 첨부 원본 XML: C:/Users/junyeopkwon/Downloads/jsbsim_aerodynamic_database.xml

F450_DATCOM은 원본 F450의 mass, gear, propulsion, effectors, autopilot, sensor 구성을 유지하고, 첨부 XML의 metrics, aerosurface scale flight_control channel, aerodynamic axes를 병합한 모델이다.

## 3. 중요 적용 방식

첨부 XML의 coefficient table 숫자 데이터는 변경하지 않았다.

다만 JSBSim 1.2.4 catalog 로딩에서 첨부 XML의 2축 base table 형식 row plus table이 FGTable missing lookup axis column 오류를 발생시켰다. 따라서 CL_base, CD_base, CY_beta, Cl_beta, Cm_base, Cn_beta의 6개 base table은 숫자값을 그대로 유지하면서 Mach breakPoint 블록을 column 축으로 합친 row plus column 2D table로 재구성했다.

row plus column plus table 구조의 control increment table은 유지했다.

## 4. 실행한 테스트

### 4.1 XML 로딩 및 property 존재 확인

실행 명령 개념:

- JSBSim --root=/home/junyeopkwon/jsbsim --aircraft=F450_DATCOM --catalog --nohighlight

확인 property:

- aero/coefficient/CL_base
- aero/coefficient/CD_base
- aero/coefficient/Cm_base
- aero/coefficient/CL_de
- aero/coefficient/CD_de
- aero/coefficient/Cm_de
- fcs/elevator-pos-deg
- fcs/effective-aileron-pos-deg
- forces/fbx-aero-lbs, forces/fby-aero-lbs, forces/fbz-aero-lbs
- moments/l-aero-lbsft, moments/m-aero-lbsft, moments/n-aero-lbsft

결과: 모두 PASS.

metrics 적용 확인:

- wingarea = 1.0650005 M2
- wingspan = 3 M
- chord = 0.36967129 M

결과: 첨부 XML 값과 F450_DATCOM Metrics.xml 값 일치.

### 4.2 공력 계수 테이블 보존 확인

첨부 XML과 F450_DATCOM Aero.xml을 파싱해서 function별 table 데이터 보존 여부를 비교했다.

검증한 function:

- CL_base
- CL_de
- CD_base
- CD_de
- CY_beta
- Cl_beta
- Cl_da
- Cm_base
- Cm_de
- Cn_beta
- Cn_da

결과: 11개 function 모두 PASS.

주의: base table 6개는 JSBSim 호환을 위해 구조만 row plus table에서 row plus column으로 바꾸었고, alpha/beta/Mach breakpoints 및 coefficient 숫자값은 보존했다.

### 4.3 qbar 변화에 따른 aerodynamic force/moment 응답 확인

attitude step 미션과 propulsion-off free-response 미션에서 qbar-area와 aero force/moment 로그를 비교했다.

핵심 결과:

- attitude step 미션 F450_DATCOM qbar-area range: 0 to 10.64
- propulsion-off free-response F450_DATCOM qbar-area range: 6.329 to 13.74
- propulsion-off free-response에서 abs forces/fbx-aero-lbs와 qbar-area correlation: 0.9999
- propulsion-off free-response에서 abs forces/fbz-aero-lbs와 qbar-area correlation: 0.9913

해석: propulsion/controller가 꺼진 free-response 조건에서 qbar 변화에 따라 aero force가 강하게 같이 변하므로, qbar 기반 공력 힘 계산이 실제 로그에 반영됨을 확인했다.

### 4.4 조종 입력 및 부호 확인

attitude step 로그에서 조종 명령과 aerosurface 출력의 상관을 확인했다.

- fcs/elevator-cmd-norm vs fcs/elevator-pos-deg correlation = 1.0
- fcs/aileron-cmd-norm vs fcs/effective-aileron-pos-deg correlation = 1.0

첨부 XML table 기준 control increment 부호도 확인했다.

- CL_de: positive elevator에서 증가 방향
- Cm_de: positive elevator에서 감소 방향
- Cl_da: positive aileron에서 증가 방향
- Cn_da: positive aileron에서 증가 방향

결과: 모두 PASS.

### 4.5 동일 attitude-mode 미션 A/B 비교

미션 파일:

- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/runscript/1.0__attitude_axis_datcom_compare_run.xml

실행 결과 CSV:

- /home/junyeopkwon/jsbsim_workflow/logs/csv/combined/F450/1.0__attitude_axis_datcom_compare/1.0.1__attitude_axis_datcom_compare_combined_08102235.csv
- /home/junyeopkwon/jsbsim_workflow/logs/csv/combined/F450_DATCOM/1.0__attitude_axis_datcom_compare/1.0.1__attitude_axis_datcom_compare_combined_08102235.csv

핵심 비교:

| 항목 | F450 | F450_DATCOM |
|---|---:|---:|
| final hover 60-70 s 평균 고도 | 10.0053 m | 9.66485 m |
| final hover 마지막 고도 | 10.0037 m | 9.8536 m |
| final hover 평균 수직속도 | 0.0001668 m/s | 0.0106851 m/s |
| positive roll 20-30 s 평균 roll | 4.29243 deg | 3.52658 deg |
| positive pitch 40-50 s 평균 pitch | 4.30446 deg | 4.18374 deg |
| positive pitch 40-50 s 마지막 pitch | 4.65964 deg | 8.52152 deg |

해석: 같은 controller와 같은 setpoint를 사용했는데 F450_DATCOM은 고도 유지, 자세 응답, 수평 drift가 원본과 다르게 나타난다. 이는 DATCOM 공력 force/moment가 동역학에 영향을 주고 있음을 보여준다.

### 4.6 propulsion/controller 영향 분리 free-response 테스트

추가 생성한 초기조건과 미션:

- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/initial_condition/2.0__free_response_10ms_theta5_init.xml
- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/scripts/F450_DATCOM/runscript/2.0__propulsion_off_free_response_run.xml

조건:

- 초기 고도: 100 m AGL
- 초기 속도: 10 m/s
- 초기 pitch: 5 deg
- ap/mode = 0
- fcs/ScasEngage = 0
- throttle command = 0
- roll, pitch, yaw command = 0
- 실행 시간: 8 s

실행 결과 CSV:

- /home/junyeopkwon/jsbsim_workflow/logs/csv/combined/F450/2.0__propulsion_off_free_response/2.0.1__propulsion_off_free_response_combined_08102253.csv
- /home/junyeopkwon/jsbsim_workflow/logs/csv/combined/F450_DATCOM/2.0__propulsion_off_free_response/2.0.1__propulsion_off_free_response_combined_08102253.csv

핵심 비교:

| 항목 | F450 | F450_DATCOM |
|---|---:|---:|
| max abs engine thrust | 0 lbf | 0 lbf |
| aero Fz range | -2.88378 to 0 lbf | -5.47923 to -1.96083 lbf |
| aero Fz mean | -1.62373 lbf | -3.09047 lbf |
| aero pitch moment range | 0 to 0 lbf-ft | -0.254481 to 0.177365 lbf-ft |
| aero pitch moment mean | 0 lbf-ft | 0.0000668 lbf-ft |

해석: 두 모델 모두 thrust가 0인 상태에서, F450_DATCOM은 원본 F450보다 큰 aero Fz와 비영 pitch moment를 생성했다. 따라서 모터와 controller 영향 없이도 DATCOM 공력이 동역학에 직접 반영됨을 확인했다.

## 5. 산출물

정량 검증 CSV:

- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/combined/F450_DATCOM/aero_validation_08102253/aero_validation_checks_08102253.csv

기존 attitude 비교 요약 CSV:

- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/logs/csv/combined/F450_DATCOM/1.0__attitude_axis_datcom_compare/1.0.1__F450_vs_F450_DATCOM_attitude_compare_summary_08102235.csv

그래프:

- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/plots/F450_DATCOM_attitude_compare_08102235/01_overview_altitude_attitude_velocity.png
- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/plots/F450_DATCOM_attitude_compare_08102235/02_attitude_tracking_and_aerosurfaces.png
- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/plots/F450_DATCOM_attitude_compare_08102235/03_aero_forces_moments.png
- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/plots/F450_DATCOM_attitude_compare_08102235/04_datcom_coefficients.png
- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/plots/F450_DATCOM_attitude_compare_08102235/05_aero_state.png
- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/plots/F450_DATCOM_aero_validation_08102253/06_propulsion_off_free_response.png
- /home/junyeopkwon/evtol-6dof/jsbsim_workflow/plots/F450_DATCOM_aero_validation_08102253/07_propulsion_off_thrust_check.png

## 6. 결론

현재 기준에서 F450_DATCOM에 DATCOM 공력은 제대로 적용된 것으로 판단한다.

근거는 다음과 같다.

- JSBSim catalog에서 DATCOM coefficient와 aerosurface property가 존재한다.
- 첨부 XML의 11개 공력 function table 데이터가 F450_DATCOM Aero.xml에 보존되어 있다.
- 조종 입력이 elevator와 effective aileron deflection으로 정상 변환된다.
- F450_DATCOM 로그에서 DATCOM coefficient, aero force, aero moment가 비영 값으로 기록된다.
- 같은 attitude-mode 미션에서 원본 F450과 F450_DATCOM의 고도, 자세, 속도 응답이 다르게 나타난다.
- propulsion-off free-response에서 thrust가 0인데도 F450_DATCOM의 aero force/moment가 원본과 다르게 발생한다.

## 7. 한계와 다음 작업

이번 검증은 적용 여부 확인에 초점을 둔 것이다. DATCOM 모델이 실제 F450 형상과 물리적으로 맞는지, 또는 controller tuning이 충분한지는 별도 문제다.

남은 리스크:

- DATCOM reference area, span, chord가 기존 F450 frame보다 크다.
- attitude-mode 미션은 position hold 검증이 아니다.
- row plus table을 row plus column으로 재구성한 것은 JSBSim 로딩 호환 조치이며, 숫자 데이터는 보존했지만 원 생성기의 보간 의도와 100 percent 동일한지는 별도 확인 여지가 있다.

권장 다음 작업:

1. 10 m mode 3 position-hold hover 전용 미션 실행
2. headwind와 crosswind를 넣은 hover 비교
3. 전방속도 5, 10, 15 m/s 조건에서 qbar scaling 재확인
4. F450_DATCOM 전용 autopilot gain과 hover throttle base tuning 여부 판단
