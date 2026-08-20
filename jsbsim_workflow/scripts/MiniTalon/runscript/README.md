# MiniTalon runscript (폴더만 생성됨, 내용 비어있음)

2026-08-03 검토 세션에서 사용자 요청("폴더만 생성해두고 모델 구성 검토만 진행")에
따라 폴더 구조만 먼저 만들어 둔다. 실제 runscript XML은 아직 작성하지 않았다.

- 대상 기체 실체: `/home/junyeopkwon/jsbsim/aircraft/MiniTalon/`
- 실체 쪽에 이미 `scripts/MiniTalon_smoke_test_run.xml`,
  `MiniTalon_control_sign_test_run.xml`, `MiniTalon_trim_test_run.xml`,
  `MiniTalon_ground_test_run.xml`이 존재함(Codex 작성, 2026-08-03).
  longitudinal trim이 아직 수렴하지 않는 상태(TODO-20260803-1528-003)이므로,
  이 폴더의 정식 runscript는 trim 문제 해소 이후 착수를 권장함.
