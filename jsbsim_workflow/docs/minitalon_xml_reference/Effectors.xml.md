# Effectors.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

상태: 현재 `MiniTalon.xml`에서 로드되지 않는다. 이전 bootstrap용 effectors 모델이다.

| 항목 | 값 | 의미 | 현재 판단 |
|---|---|---|---|
| ESC actuator lag | `30.0` | throttle command to throttle position lag | current `FlightControl.xml` 체계와 별도, inactive |
| throttle clip | `0..1` | normalized throttle range | 일반적 seed |
| aileron clip | `±0.349066 rad` = `±20 deg` | 과거 aileron limit | 현재 활성 모델은 `±25 deg` 사용 |
| ruddervator clip | `±0.436332 rad` = `±25 deg` | 과거 V-tail limit | current model과 일부 일치 |
| servo rate | `4.0 rad/s` | 과거 servo rate seed | 현재 활성 모델은 `2.5 rad/s` |

이 파일의 값은 현재 active model 설명에 사용하면 안 된다.
