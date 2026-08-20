# MiniTalon.xml

> 기준 모델: /home/junyeopkwon/jsbsim/aircraft/MiniTalon  
> 작성일: 2026-08-10  
> 좌표계: JSBSim structural frame, nose-tip datum, X aft, Y right, Z up

파일: `aircraft/MiniTalon/MiniTalon.xml`

### 4.1 파일 자체의 의미

이 파일은 JSBSim aircraft root file이다. 실제 물리 파라미터를 직접 많이 담기보다, 어떤 하위 XML을 로드할지 지정한다.

| XML 값 | 의미 | 현재 값 | 근거 | 신뢰도/비고 |
|---|---|---|---|---|
| `<fdm_config name>` | JSBSim에 표시되는 aircraft 이름 | `X-UAV Mini Talon fixed-wing geometry-locked model` | 작업자가 정한 모델 식별명 | 문서용 |
| `version=2.0` | JSBSim XML schema version 성격 | `2.0` | JSBSim config 관례 | 유지 |
| `release=ALPHA` | 모델 성숙도 표시 | `ALPHA` | 아직 검증 미완료 | 유지 권장 |
| `<author>` | 모델 작성자 | `OpenAI - assembled for the JSBSim 6DOF project` | 작업 기록 | 문서용 |
| `<filecreationdate>` | 파일 생성일 | `2026-08-09` | 작업일 | 문서용 |
| `<version>` | 모델 내부 revision | `0.2.1` | nose-tip datum update 반영 | 변경 시 갱신 |
| `<reference refID=Bacchini2020>` | Bacchini 박사학위논문 출처 | 논문명/저자/연도 | Mini Talon wind-tunnel / eVTOL 연구 | 공력/기하 source |
| `<reference refID=Bacchini2021>` | 논문 출처 | Aerospace Science and Technology 2021 논문 | eVTOL lift+cruise 성능 연구 | audit source |

### 4.2 로드 모듈

| 태그 | 연결 파일 | 의미 |
|---|---|---|
| `<metrics file=Metrics/>` | `Metrics.xml` | 기준 형상 및 기준점 위치 |
| `<mass_balance file=Mass/>` | `Mass.xml` | 질량/CG/관성 |
| `<ground_reactions file=Gear/>` | `Gear.xml` | skid/contact ground reaction |
| `<propulsion file=Propulsion/>` | `Propulsion.xml` | motor/prop 연결 |
| `<flight_control file=FlightControl/>` | `FlightControl.xml` | 조종 명령/servo/mixer |
| `<aerodynamics file=Aero/>` | `Aero.xml` | 공력 force/moment |
