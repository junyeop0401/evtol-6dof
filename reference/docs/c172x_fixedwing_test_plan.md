# C172X Fixed-Wing Test Plan

이 워크플로에서는 고정익 모드의 `c172x`만 대상으로 한다.

## Earth Model

1차 테스트 지구 모델은 `earth_models/04_nonrotating_spherical_earth.xml`을 사용한다.

- 지구 자전 없음: Coriolis/centrifugal 항을 제거해서 짧은 추락 궤적 해석이 단순해진다.
- 구형 지구: geocentric/geodetic 차이와 타원체 곡률 효과를 최소화한다.
- `gravity_model=gtStandard`, `J2=0`: 구형 중심중력 조건이다.

권장 순서:

1. `04_nonrotating_spherical_earth.xml`로 cruise와 추락 이벤트가 정상 동작하는지 확인한다.
2. 결과가 안정적이면 `03_nonrotating_default_earth.xml`로 WGS84 형상/J2 중력 영향만 비교한다.
3. 최종 지리좌표 기반 결과가 필요하면 planet XML을 지정하지 않는 JSBSim 기본 Earth 또는 별도 WGS84 rotating 모델로 재검증한다.

## Initial Condition

반복 테스트 기준 초기조건:

- `scripts/c172x/initial_condition/1.1__cruise_4k_trimmed_init.xml`
- 4,000 ft MSL, 100 kt 수준의 pre-trimmed cruise 상태
- heading 200 deg, latitude 28 deg, longitude -90 deg
- engine running

`scripts/c172x/initial_condition/1.0__cruise_4k_untrimmed_init.xml`는 simple trim 자체를 검증할 때 사용하고, 추락 시나리오 비교에는 pre-trimmed init을 우선 사용한다.

## Runscripts

Cruise 확인:

```bash
python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py \
  --aircraft c172x \
  --init /home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/1.1__cruise_4k_trimmed_init.xml \
  --runscript /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/1.1__cruise_4k_trimmed_run.xml \
  --planet /home/junyeopkwon/jsbsim_workflow/earth_models/04_nonrotating_spherical_earth.xml
```

Engine-out, autopilot 유지:

```bash
python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py \
  --aircraft c172x \
  --init /home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/1.1__cruise_4k_trimmed_init.xml \
  --runscript /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/2.0__cruise_4k_trimmed_engineout_apon_run.xml \
  --planet /home/junyeopkwon/jsbsim_workflow/earth_models/04_nonrotating_spherical_earth.xml
```

Engine-out, autopilot 정지:

```bash
python3 /home/junyeopkwon/jsbsim_workflow/scripts/run_jsbsim_timestamped.py \
  --aircraft c172x \
  --init /home/junyeopkwon/jsbsim_workflow/scripts/c172x/initial_condition/1.1__cruise_4k_trimmed_init.xml \
  --runscript /home/junyeopkwon/jsbsim_workflow/scripts/c172x/runscript/2.1__cruise_4k_trimmed_engineout_apoff_run.xml \
  --planet /home/junyeopkwon/jsbsim_workflow/earth_models/04_nonrotating_spherical_earth.xml
```

## Event Timing

- `t=0 s`: trimmed cruise control 값을 적용한다.
- `t=5 s`: AP heading/altitude hold를 켠다.
- `t=35 s`: AP가 켜진 cruise 30초 후 engine-out 이벤트를 건다.
- `t=35.2 s 이후`: engine/AP off 조건이 다시 켜지지 않도록 유지 이벤트를 둔다.
- 지면 접촉 시 `simulation/terminate=1`로 종료한다.

## Engine-Out Definition

C172X는 단발 모델이므로 engine-out은 다음 명령으로 정의한다.

- `fcs/throttle-cmd-norm = 0`
- `fcs/mixture-cmd-norm = 0`
- `propulsion/magneto_cmd = 0`
- `propulsion/starter_cmd = 0`

AP off 시나리오는 추가로 다음을 0으로 둔다.

- `ap/heading_hold`
- `ap/altitude_hold`
- `ap/attitude_hold`
- `ap/airspeed_hold`
- `ap/aileron_cmd`
- `ap/elevator_cmd`
- `ap/throttle-cmd-norm`
