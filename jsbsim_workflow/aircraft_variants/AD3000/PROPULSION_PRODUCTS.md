# AD3000 추진계 제품 자료 반영

## 기준 데이터

- workbook: C:/Users/junyeopkwon/Downloads/DB 정리.xlsx
- sheet: 기체 Spec
- cruise table: H5:R28, V6215 210KV VSC 22.1x7.4 Motor Propeller Pull Test Data
- lift table: H30:R53, V6212 180KV Motor Propeller Thrust Test Data

## 적용 제품

- cruise motor: 6215 210KV
- lift motor: V6212-180KV
- cruise prop 의도 규격: 20*10
- lift prop: 22.1x7.4
- cruise prop XML 임시 적용: VSC 22.1x7.4

## 반영 방식

기체 Spec 시트에는 V6215 210KV와 VSC 22.1x7.4 조합, V6212 180KV와 VSC 22.1x7.4 조합의 공식 홈페이지 pull test 표가 정리되어 있다. PROPULSION_SOURCE_DATA.csv에는 해당 표의 전체 throttle 행을 보존하고, prop XML 계수 산정에는 33-100% throttle 전체 행을 used_for_coefficient=Y로 표시하고 prop XML 계수 산정에 사용한다.

AD3000 실기에서 원래 사용하려는 cruise prop은 기체 Spec 시트의 Curise Prop 항목에 있는 20*10이다. 다만 이 조합의 thrust/power sheet가 시트에 없으므로 현재 XML에는 V6215+VSC 22.1x7.4 공개 데이터를 임시 적용했다.

## 산출 계수

- lift prop Ct0: 0.07460
- lift prop Cp0: 0.02795
- cruise prop Ct0: 0.07388
- cruise prop Cp0: 0.02772

## 생성 파일

- /home/junyeopkwon/jsbsim/engine/AD3000_lift_motor_V6212_180KV.xml
- /home/junyeopkwon/jsbsim/engine/AD3000_lift_prop_Hobbywing_VSC_22x7_4.xml
- /home/junyeopkwon/jsbsim/engine/AD3000_cruise_motor_V6215_210KV.xml
- /home/junyeopkwon/jsbsim/engine/AD3000_cruise_prop_Hobbywing_VSC_22x7_4.xml
- /home/junyeopkwon/jsbsim/engine/AD3000_cruise_prop_Falcon_C2E_20x10.xml
- /home/junyeopkwon/jsbsim/aircraft/AD3000/PROPULSION_SOURCE_DATA.csv

## 전진비 table 산정 주석

기체 Spec 시트의 공식 pull test 표는 정지 시험(static test) 데이터다. 따라서 각 행에서 직접 계산 가능한 값은 전진속도 V=0, 즉 전진비 J=0 조건의 Ct와 Cp다.

전진비는 다음 식으로 계산한다.

```text
J = V / (n * D)
n = RPM / 60
D = prop diameter [m]
```

현재 엑셀 시트에는 전진속도 V가 없으므로 모든 pull test 행은 J=0으로 해석된다. 그래서 AD3000 prop XML의 J=0 값은 엑셀 데이터 전체 33-100% 행에서 계산한 Ct/Cp 평균을 사용한다. 반면 J=0.1부터 J=1.0까지의 C_THRUST/C_POWER table 값은 엑셀에서 직접 산출한 값이 아니라, J=0 계수에 일반적인 임시 advance-ratio 감소 shape를 곱한 초기 가정이다.

정확한 전진비별 prop table을 만들려면 airspeed, RPM, thrust, power가 함께 포함된 prop performance map 또는 전진풍 시험 데이터가 필요하다.

## 한계

- JSBSim propeller XML은 motor-prop coupled map 전체를 그대로 재현하지 않고, 평균 정지 Ct/Cp와 advance-ratio curve를 사용하는 초기 모델이다.
- cruise prop은 실제 의도 규격 20*10과 다르다. V6215+20*10 벤치 데이터 또는 제조사 성능표가 확보되면 cruise prop XML을 재보정해야 한다.
- 기존 AD3000 hover FPE 문제는 front/rear lift split 및 ground reaction 튜닝 문제이며, 이번 제품 파일 교체만으로 안정 hover가 보장되지는 않는다.
