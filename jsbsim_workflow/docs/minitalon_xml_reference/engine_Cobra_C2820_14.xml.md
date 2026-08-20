# engine/Cobra_C2820_14.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `engine/Cobra_C2820_14.xml`

| XML 값 | 현재 값 | 의미 | 근거 | 신뢰도 |
|---|---:|---|---|---|
| root tag | `brushless_dc_motor` | JSBSim brushless DC motor model | JSBSim propulsion model | 활성 |
| `<velocityconstant>` | `840` | motor Kv, rpm/V 성격 | Cobra C-2820/14 840 Kv manufacturer data, Bacchini propulsion selection | `PAPER-DIRECT / MANUFACTURER` |
| `<coilresistance unit="OHMS">` | `0.071` | winding resistance | manufacturer seed | `MANUFACTURER` |
| `<noloadcurrent unit="AMPERES">` | `1.00` | no-load current | manufacturer seed | `MANUFACTURER` |
| `<maxvolts unit="VOLTS">` | `14.8` | 4S nominal voltage | propulsion selection 4S assumption | `PAPER-DIRECT / ASSUMPTION` |

현재 ESC dynamics, voltage sag, current limit, thermal limit은 없다.
