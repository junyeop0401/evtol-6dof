# KCI 논문 — UAM 무제어 추락궤적 모델 검증

항공우주시스템공학회 KCI급 논문(연구 과제 산출물, 석사 논문과는 별개) 작성을 위한
폴더. 연구실에서 만든 파이썬 6DOF 추락궤적 모델을, 실제 기체(X-UAV Mini Talon)를
이용해 JSBSim 시뮬레이션 및 실기 추락시험(PX4 로그)과 3자 비교 검증하는 것이 목표.

가정: 순항 중 t=trigger 시점에 조종면 명령이 전부 0(또는 trim값)으로 고정되고
동시에 엔진 추력도 0으로 떨어지는 완전 동력상실 + 무제어 상태의 6DOF 자유낙하
거동을 검증 대상으로 함.

## 폴더 구조

- `python/`: 파이썬 6DOF 추락궤적 모델
  - `UAM_dynamic_simulation.py`: 최초 버전(원본 그대로 보관, 참고용). 공력계수가
    XML의 상수 스칼라(CY=Cl=Cn=0)라 사실상 3DOF(세로축만 동작)였음.
  - `UAM_dynamic_simulation_6dof.py`: 개정판. beta(옆미끄럼각)·p·r 기반 선형
    미계수(CYb/CYp/CYr, Clb/Clp/Clr, Cnb/Cnp/Cnr)를 추가해 실제 6DOF(가로/방향
    포함) 거동이 가능하도록 수정. Cmq도 근거 없는 -10.0에서 출처 있는 값(-12.4,
    JSBSim c172p.xml)으로 교체.
- `config/`: 기체별 설정 XML
  - `cessna172_config.xml`: 1차 개발 단계에서 쓴 세스나 172 스탠드인 설정.
    이번에 Ixz 누락(원본 버그) 수정 + 질량/관성 정합성 수정(1157kg→754kg,
    이유는 파일 내 주석 참고) + `<aero_derivatives>` 블록 신규 추가(JSBSim
    c172p.xml 출처).
  - `Cessna172_AeroCoefficients_Basic.xlsx`, `Cessna172-FlightSimulationData.pdf`:
    **아직 이 폴더에 없음** — 둘 다 바이너리 파일이라 이 세션 도구로는 직접
    복사가 불가능함. 사용자가 직접 이 폴더의 `config/`(xlsx)와 `docs/`(pdf)로
    복사해 넣어야 함.
  - `mini_talon_config.xml`: 아직 작성 전(다음 작업 참고).

## 데이터 출처 정리

- CL/CD/Cm(alpha) 세로축 계수: Marek M. Cel, "Cessna 172 Flight Simulation Data"
  (Technical Report, 2019, CC0 라이선스, OpenFOAM simpleFoam CFD 기반 -180~180도
  전체 받음각 스윕). 질량/관성텐서(Ix/Iy/Iz/Ixz)와 CG도 같은 보고서 22쪽 표
  (공허중량 754kg 기준) 출처.
- CYb/CYp/CYr, Clb/Clp/Clr, Cnb/Cnp/Cnr, Cmq 가로/방향 및 감쇠 미계수: 위 CFD
  보고서에는 없어서, JSBSim 공식 오픈소스 c172p 기체 정의(`aircraft/c172p/c172p.xml`)
  에서 가져옴. 원본 테이블이 alpha/flap에 따라 조금씩 달라지는 부분은 alpha=0,
  flap=0 슬라이스 값을 대표 선형 미계수로 고정해서 사용(논문에 이 근사를 명시할 것).

## 다음 작업

1. 사용자가 xlsx/pdf 원본을 이 폴더(`config/`, `docs/`)에 수동 복사
2. MiniTalon용 `mini_talon_config.xml` + alpha 테이블 xlsx 작성
   (`/home/junyeopkwon/jsbsim/aircraft/MiniTalon/Aero.xml`, `Mass.xml`, `Metrics.xml`
   값을 그대로 이식, beta 기반 CYb/Clb/Cnb, Clp/Cnr은 이미 그 Aero.xml에 있음)
3. JSBSim MiniTalon 완전동력상실+조종면고정 크래시 시나리오(Codex 실행, 별도
   진행 중 — `/home/junyeopkwon/jsbsim/scripts/MiniTalon_crash_zero_controls_run.xml`)
   결과와 이 파이썬 모델의 MiniTalon 파라미터 실행 결과 1차 비교
4. 실기 추락시험 PX4 로그 확보 후 3자 비교로 확장
