# MiniTalon initial_condition (폴더만 생성됨, 내용 비어있음)

2026-08-03 검토 세션에서 사용자 요청("폴더만 생성해두고 모델 구성 검토만 진행")에
따라 폴더 구조만 먼저 만들어 둔다. 실제 초기조건 XML은 아직 작성하지 않았다.

- 대상 기체 실체: `/home/junyeopkwon/jsbsim/aircraft/MiniTalon/`
  (Codex가 2026-08-03 15:28 세션에서 X-UAV Mini Talon 부트스트랩 모델로 생성,
  evtol-6dof/jsbsim_workflow 안이 아니라 실제 JSBSim 설치 트리 쪽에 있음)
- 기존 관례(`scripts/<기체>/initial_condition/*_init.xml`, F450/c172x 등 참고)를
  그대로 따를 예정
- 착수 전 확인 필요: `aircraft/MiniTalon/initAir.xml`, `initGround.xml`이 이미
  존재하므로, 이 폴더에 새로 만들 initial_condition이 그것을 대체/보완하는
  용도인지 사용자와 먼저 합의할 것(현재는 폴더만 생성, 내용 없음)
