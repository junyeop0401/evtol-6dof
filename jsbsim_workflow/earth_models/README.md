# Earth Models

JSBSim 실행 시 `--planet=<xml path>`로 넘길 수 있는 지구모델들을 한곳에 모아둔다.

## Gravity Model

이 workflow의 JSBSim은 planet XML에서 `gravity_model` 태그를 읽도록 수정되어 있다.
따라서 각 지구모델 XML 안에서 중력모델까지 함께 선언한다.

- `gravity_model = gtStandard`: 구형 중심중력
- `gravity_model = gtWGS84`: WGS84 J2 중력

호환을 위해 runner는 generated runscript에도 `simulation/gravity-model`을 같이 넣는다.

- `J2 = 0.0`: `gtStandard`
- `J2 != 0.0`: `gtWGS84`

## 01 Default Earth

- 파일: `01_default_earth_builtin.md`
- XML 없음.
- JSBSim의 기본 `Earth` 값을 그대로 사용한다.
- 별도 planet XML을 넘기지 않으면 이 모델로 계산한다.

## 02 Spherical Earth

- 파일: `02_spherical_earth.xml`
- 지구 자전은 기본값으로 유지한다.
- 적도 반지름과 극 반지름을 같게 둔다.
- `J2 = 0.0`으로 두어 구형 중심중력 조건으로 쓴다.

## 03 Non-Rotating Default Earth

- 파일: `03_nonrotating_default_earth.xml`
- 기본 지구의 적도 반지름, 극 반지름, GM, J2는 유지한다.
- 지구 자전 각속도만 `0.0`으로 둔다.

## 04 Non-Rotating Spherical Earth

- 파일: `04_nonrotating_spherical_earth.xml`
- 적도 반지름과 극 반지름을 같게 둔다.
- 지구 자전 각속도를 `0.0`으로 둔다.
- `J2 = 0.0`으로 둔다.
