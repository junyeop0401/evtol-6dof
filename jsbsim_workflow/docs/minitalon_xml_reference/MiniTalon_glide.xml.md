# MiniTalon_glide.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `aircraft/MiniTalon/MiniTalon_glide.xml`  
상태: geometry-locked glide checks에서 사용하는 현재 권장 smoke-test 초기조건.

| XML 값 | 현재 값 | 의미 | 근거 |
|---|---:|---|---|
| `<ubody unit="M/SEC">` | `17.5` | body X 방향 초기속도 | paper-condition 17.5 m/s |
| `<vbody unit="M/SEC">` | `0.0` | body Y 초기속도 | wings-level glide seed |
| `<wbody unit="M/SEC">` | `0.0` | body Z 초기속도 | alpha 0 초기화 seed |
| `<latitude unit="DEG">` | `37.0` | 초기 위도 | test location seed |
| `<longitude unit="DEG">` | `127.0` | 초기 경도 | test location seed |
| `<altitude unit="FT">` | `1000.0` | 초기 고도 | glide smoke test용 충분한 고도 |
| `<phi/theta/psi unit="DEG">` | `0/0/0` | 초기 자세 | neutral glide seed |
