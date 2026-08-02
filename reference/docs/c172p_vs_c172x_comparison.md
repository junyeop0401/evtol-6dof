# JSBSim C172P vs C172X 비교

비교 대상:

- `/home/junyeopkwon/jsbsim/aircraft/c172p/c172p.xml`
- `/home/junyeopkwon/jsbsim/aircraft/c172x/c172x.xml`
- `/home/junyeopkwon/jsbsim/aircraft/c172x/c172ap.xml`

| 항목 | c172p | c172x |
|---|---:|---:|
| 주 XML 길이 | 941 lines | 1280 lines |
| 기본 성격 | 단순 C172P 6DOF 모델 | C172P 계열 확장 모델 |
| Autopilot | 없음 | 있음 (`c172ap.xml`) |
| 추가 system | 없음 | Navigation, Fuel volume, Mixture control, GNCUtilities, Autopilot |
| Engine | `eng_io320` | `eng_io320` |
| Propeller | `prop_75in2f` | `prop_75in2f` |
| Wing area | 174 ft^2 | 174 ft^2 |
| Wingspan | 35.8 ft | 36.0 ft |
| Chord | 4.9 ft | 4.9 ft |
| H-tail area | 21.9 ft^2 | 21.9 ft^2 |
| H-tail arm | 15.7 ft | 15.7 ft |
| V-tail area | 16.5 ft^2 | 16.5 ft^2 |
| V-tail arm | 0 ft | 15.7 ft |
| Empty weight | 1500 lb | 1454 lb |
| Ixx | 948 slug*ft^2 | 948 slug*ft^2 |
| Iyy | 1346 slug*ft^2 | 1346 slug*ft^2 |
| Izz | 1967 slug*ft^2 | 1967 slug*ft^2 |
| Fuel capacity | 185 lb x 2 | 130 lb x 2 |
| Initial fuel contents | 100 lb x 2 | 130 lb x 2 |
| FCS pitch input | pilot/trim only | AP + pilot + trim |
| FCS roll input | pilot/trim only | AP + guidance + pilot + trim |
| FCS yaw input | pilot/trim only | pilot/trim |
| Heading hold | 없음 | `ap/heading_hold` |
| Altitude hold | 없음 | `ap/altitude_hold` |
| Attitude hold / wing leveler | 없음 | `ap/attitude_hold` |
| Airspeed hold property | 없음 | `ap/airspeed_hold`, `ap/throttle-cmd-norm` |
| Reset files | `reset00.xml`, `reset01.xml` | `reset00.xml`, `reset01.xml`, `reset_at_rest.xml`, `elevator_doublet_init.xml` |

## 해석

`c172p`는 기체/공력/추진/FCS가 비교적 단순해서 자연 6DOF 응답을 보기 좋다. 다만 autopilot이 없으므로 엔진정지 후 조종면을 중립에 두면 roll-yaw coupling이나 spiral mode가 그대로 나타날 수 있다.

`c172x`는 `c172p` 계열을 확장한 모델에 가깝고, autopilot과 guidance 관련 property가 들어 있다. 따라서 heading 유지, wing level, altitude hold 같은 기준선 시나리오를 만들기 쉽다. 엔진정지 후 진행방향을 유지하는 glide 기준선을 만들 때는 `c172x`가 더 적합하다.
