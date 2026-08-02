# <Aircraft> — 기체 제원

기체 폴더: (경로)
구성: (top-level fdm_config가 참조하는 서브파일 목록)

## Metrics (`Metrics.xml`)

| 항목 | 값 |
|---|---|

## Mass & Balance (`Mass.xml`)

| 항목 | 값 |
|---|---|

## Propulsion (`Propulsion.xml`)

| 모터 | 위치 (x,y,z) | Sense |
|---|---|---|

(모터/프로펠러 스펙 표)

## Aerodynamics (`Aero.xml`)

(축 구성, qbar-area 곱셈 여부 등 특이사항)

## Ground Reactions (`Gear.xml`)

(접점 수, 위치, 스프링/댐핑/마찰 계수)

## Autopilot / FCS 특이사항

(자동조종이 있다면 어떤 프로퍼티를 매 프레임 덮어쓰는지 — 런스크립트 작성 시
반드시 알아야 하는 함정)

## 표기법 (기체 고유)

이 기체의 FCS/자동조종 프로퍼티에 쓰는 기호. 공통 기호(t_sim, s_mis 등)는
`_notation_common.md` 참고 — 여기는 이 기체에서만 쓰는 프로퍼티만 정의한다.

| 기호 | JSBSim 프로퍼티 | 단위 | 설명 |
|---|---|---|---|
