# Aircraft Model Comparison

JSBSim workflow에서 사용 중이거나 별도로 만든 aircraft 모델 비교 정리.

## Workflow 사용 현황

| aircraft | workflow 사용 여부 | runscript 수 | 주요 용도 |
|---|---:|---:|---|
| `ball` | 사용 | 1 | JSBSim 기본 ball 모델 기준 비교 |
| `ball_validated` | 사용 | 9 | 검증용 구체 모델, 투척/낙하 케이스 |
| `c172p` | 사용 | 2 | 기본 C172P 고정익 엔진 정지/활공 케이스 |
| `c172x` | 사용 | 4 | 수정/확장 C172 고정익 케이스 |
| `F450` | 미사용 | 0 | 별도 제작/보관 중인 F450 quadcopter 모델 |
| `c172p_2kg_vtol` | 미사용 | 0 | C172P 기반 2 kg VTOL/멀티콥터 실험 모델 |

## 주요 파라미터 비교

| 항목 | `ball` | `ball_validated` | `c172p` | `c172x` | `F450` | `c172p_2kg_vtol` |
|---|---:|---:|---:|---:|---:|---:|
| config name | BALL | BALL_VALIDATED | c172 | Cessna C-172 Skyhawk II | F450 | c172p_2kg_vtol |
| release | BETA | BETA | BETA | BETA | ALPHA | ALPHA |
| wingarea | 1 FT2 | 0.09290304 M2 | 174 FT2 | 174.0 FT2 | 0.016129 M2 | 3.56 FT2 |
| wingspan | 1 FT | 0.3048 M | 35.8 FT | 36.0 FT | 0.127 M | 5.12 FT |
| chord | 1 FT | 0.3048 M | 4.9 FT | 4.9 FT | 0.127 M | 0.701 FT |
| emptywt | 20000 LBS | 9071.8474 KG | 1500 LBS | 1454.0 LBS | 1.4 KG | 2.0 KG |
| Ixx | 10 SLUG*FT2 | 84.3223602977034 KG*M2 | 948 SLUG*FT2 | 948.0 SLUG*FT2 | 0.0190 KG*M2 | 0.077 KG*M2 |
| Iyy | 10 SLUG*FT2 | 84.3223602977034 KG*M2 | 1346 SLUG*FT2 | 1346.0 SLUG*FT2 | 0.0190 KG*M2 | 0.109 KG*M2 |
| Izz | 10 SLUG*FT2 | 84.3223602977034 KG*M2 | 1967 SLUG*FT2 | 1967.0 SLUG*FT2 | 0.0252 KG*M2 | 0.160 KG*M2 |
| propulsion | dummy/rocket force | dummy/rocket force | 1x `eng_io320` + prop | 1x `eng_io320` + prop | 4x `DJI_E305` | 4x `DJI_E305` |
| aero axes | 1 | 1 | 6 | 6 | 6 | 6 |
| FCS channels | 1 | 1 | 4 | 4 | 4 | 4 |
| sensor/system | simple force system | simple force system | 기본 시스템 | navigation, fuel, mixture, AP 포함 | PX4 IMU/baro/GPS 포함 | PX4 IMU/baro/GPS 포함 |

## 모델별 해석

### `ball`

- JSBSim 기본 ball 모델.
- `ball_validated`와 비교하기 위한 reference 성격.
- 단순 구체 공력: drag axis 중심.

### `ball_validated`

- workflow 검증용으로 만든 구체 모델.
- SI 단위 기반으로 `ball`과 같은 물리 의미를 맞춘 모델.
- 투척 방향/상승각 케이스가 가장 많이 연결되어 있다.

### `c172p`

- JSBSim 기본 C172P 계열 모델.
- 고정익 활공, 엔진 정지, trim 비교의 기본 reference.
- `eng_io320` 엔진과 `prop_75in2f` 프로펠러 사용.

### `c172x`

- C172P보다 시스템이 확장된 C172 모델.
- navigation, fuel volume, mixture control, autopilot 관련 system이 추가되어 있다.
- takeoff-cruise-engineout, heading hold, trimmed cruise 케이스에 사용 중.

### `F450`

- 별도 제작된 F450 quadcopter 모델.
- `Metrics.xml`, `Mass.xml`, `Propulsion.xml`, `FlightControl.xml` 등으로 분리 구성.
- PX4 기본 IMU/baro/GPS sensor system 포함.
- 현재 `jsbsim_workflow/scripts/*_run.xml`에는 아직 연결되어 있지 않다.

### `c172p_2kg_vtol`

- C172P 형식을 작게 축소하고 4개 `DJI_E305` 모터를 얹은 2 kg VTOL 실험 모델.
- PX4 기본 sensor system 포함.
- 현재 workflow runscript에는 아직 연결되어 있지 않다.

## 발표용 짧은 표

| 구분 | 모델 | 의미 |
|---|---|---|
| 기본 구체 | `ball` | JSBSim 기본 reference |
| 검증 구체 | `ball_validated` | 직접 검증/단위 정리한 구체 모델 |
| 기본 고정익 | `c172p` | JSBSim C172P reference |
| 확장 고정익 | `c172x` | 시스템/제어 확장 C172 |
| 멀티콥터 | `F450` | 제작된 quadcopter 모델, workflow 미연결 |
| VTOL 실험 | `c172p_2kg_vtol` | 2 kg급 4모터 VTOL 실험 모델, workflow 미연결 |
