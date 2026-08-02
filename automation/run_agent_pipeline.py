#!/usr/bin/env python3
"""로컬 AI 에이전트 오케스트레이션 스크립트 (구독 한도 내 사용 전제).

설계 원칙(반드시 지킬 것):
  1. 새 API 키를 쓰지 않는다. `codex exec`와 `gemini -p`는 이미 로그인된
     구독 세션(ChatGPT / Google 계정)을 그대로 재사용한다.
  2. 모든 호출을 usage_log.jsonl에 기록하고, 하루 호출 상한을 넘으면
     자동으로 멈춘다 — 스크립트 버그로 Codex 주간 한도를 한번에
     소진해버리는 사고를 막기 위함(Codex는 5시간 롤링 + 주간 한도가
     같이 걸려 있어서 한 번 다 쓰면 며칠 못 쓴다).
  3. git add/commit/push, 파일 삭제처럼 되돌리기 어려운 작업은 이 스크립트가
     절대 대신하지 않는다. 항상 사람이 마지막 확인을 한다.
  4. cron 없이 수동 실행이 기본값이다. 여러 번 손으로 돌려보고 usage_log.jsonl과
     run_logs/를 검토한 뒤에만 cron으로 옮기는 걸 고려할 것.
  5. 이 스크립트는 "실행"(Codex)과 "조사/연구"(Gemini) 두 단계만 자동화한다.
     "XML 1차 작성"과 "독립 정적검증"은 Claude(Cowork 세션)가 맥락을 이미
     들고 있는 채로 직접 하는 게 더 정확하고 안전해서 일부러 자동화하지
     않았다. GPT 교차검증도 API/CLI가 없어 여전히 수동(복붙) 핸드오프다
     (docs/gpt_crosscheck_template.md 참고).

사용 전 확인(반드시 먼저 손으로 실행해볼 것):
  $ codex exec "echo hello"      # 새 로그인 창 없이 바로 답하면 OK
  $ gemini -p "hello"             # 새 로그인 창 없이 바로 답하면 OK
둘 중 하나라도 로그인을 다시 요구하면, 이 스크립트를 돌리기 전에
`codex login` / `gemini` 쪽 로그인부터 먼저 끝내야 한다.

사용 예:
  $ python3 automation/run_agent_pipeline.py \\
      --stage research \\
      --prompt-file automation/prompts/tiltrotor_concept_research.txt

  $ python3 automation/run_agent_pipeline.py \\
      --stage execute \\
      --prompt-file automation/prompts/tiltrotorA_execute.txt \\
      --cwd ~/jsbsim_workflow
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
USAGE_LOG = ROOT / "usage_log.jsonl"
RUN_LOG_DIR = ROOT / "run_logs"

# 보수적인 기본값. Codex는 ChatGPT Plus 기준 주간 한도가 넉넉하지 않으므로
# 낮게 잡았다. 필요하면 --max-codex-calls-per-day / --max-gemini-calls-per-day로
# 매 실행마다 조정할 것(스크립트 코드 자체를 고치지 않아도 됨).
DEFAULT_MAX_CODEX_CALLS_PER_DAY = 8
DEFAULT_MAX_GEMINI_CALLS_PER_DAY = 20


def today_str() -> str:
    return datetime.now().astimezone().strftime("%Y-%m-%d")


def load_today_usage() -> dict[str, int]:
    counts = {"codex": 0, "gemini": 0}
    if not USAGE_LOG.exists():
        return counts
    today = today_str()
    with USAGE_LOG.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("date") == today:
                tool = entry.get("tool")
                if tool in counts:
                    counts[tool] += 1
    return counts


def log_usage(tool: str, prompt_summary: str, ok: bool) -> None:
    USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "date": today_str(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tool": tool,
        "prompt_summary": prompt_summary[:200].replace("\n", " "),
        "ok": ok,
    }
    with USAGE_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def check_budget(tool: str, max_per_day: int) -> None:
    counts = load_today_usage()
    if counts[tool] >= max_per_day:
        print(
            f"[중단] 오늘 {tool} 호출이 이미 {counts[tool]}회로 상한({max_per_day}회)에 "
            f"도달했습니다. 구독 한도 보호를 위해 자동 중단합니다. "
            f"필요하면 --max-{tool}-calls-per-day 값을 조정해서 다시 실행하세요.",
            file=sys.stderr,
        )
        sys.exit(2)


def _write_run_log(tool: str, prompt: str, proc: "subprocess.CompletedProcess[str]") -> Path:
    RUN_LOG_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = RUN_LOG_DIR / f"{stamp}_{tool}.log"
    path.write_text(
        f"PROMPT:\n{prompt}\n\n--- STDOUT ---\n{proc.stdout}\n\n--- STDERR ---\n{proc.stderr}\n",
        encoding="utf-8",
    )
    return path


def run_codex(prompt: str, *, sandbox: str, cwd: Path, max_per_day: int) -> str:
    check_budget("codex", max_per_day)
    cmd = ["codex", "exec", "--sandbox", sandbox, prompt]
    print(f"[codex exec 실행] sandbox={sandbox} cwd={cwd}", file=sys.stderr)
    proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    ok = proc.returncode == 0
    log_usage("codex", prompt, ok)
    log_path = _write_run_log("codex", prompt, proc)
    print(f"[로그 저장] {log_path}", file=sys.stderr)
    if not ok:
        print(proc.stderr, file=sys.stderr)
        raise RuntimeError(f"codex exec 실패 (exit={proc.returncode}). 로그: {log_path}")
    return proc.stdout.strip()


def run_gemini(prompt: str, *, cwd: Path, max_per_day: int, output_format: str = "text") -> str:
    check_budget("gemini", max_per_day)
    cmd = ["gemini", "-p", prompt, "--output-format", output_format]
    print(f"[gemini -p 실행] cwd={cwd}", file=sys.stderr)
    proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    ok = proc.returncode == 0
    log_usage("gemini", prompt, ok)
    log_path = _write_run_log("gemini", prompt, proc)
    print(f"[로그 저장] {log_path}", file=sys.stderr)
    if not ok:
        print(proc.stderr, file=sys.stderr)
        raise RuntimeError(f"gemini 실패 (exit={proc.returncode}). 로그: {log_path}")
    return proc.stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Codex/Gemini CLI 순차 호출 오케스트레이터 (구독 한도 보호 포함, API 키 미사용)"
    )
    parser.add_argument(
        "--stage",
        required=True,
        choices=["research", "execute"],
        help="research=Gemini로 개념설계/문헌조사, execute=Codex로 JSBSim 실행+디버깅",
    )
    parser.add_argument("--prompt-file", type=Path, required=True, help="해당 단계에 넘길 프롬프트 텍스트 파일")
    parser.add_argument(
        "--cwd",
        type=Path,
        default=Path.home() / "jsbsim_workflow",
        help="codex/gemini를 실행할 작업 디렉토리 (기본: ~/jsbsim_workflow, harness ROOT와 동일)",
    )
    parser.add_argument(
        "--sandbox",
        default="workspace-write",
        choices=["read-only", "workspace-write", "danger-full-access"],
        help="codex exec 샌드박스 권한 (기본: workspace-write, execute 단계에만 적용)",
    )
    parser.add_argument("--max-codex-calls-per-day", type=int, default=DEFAULT_MAX_CODEX_CALLS_PER_DAY)
    parser.add_argument("--max-gemini-calls-per-day", type=int, default=DEFAULT_MAX_GEMINI_CALLS_PER_DAY)
    args = parser.parse_args()

    if not args.prompt_file.exists():
        print(f"프롬프트 파일을 찾을 수 없습니다: {args.prompt_file}", file=sys.stderr)
        sys.exit(1)
    prompt = args.prompt_file.read_text(encoding="utf-8")
    cwd = args.cwd.expanduser()

    if args.stage == "research":
        output = run_gemini(prompt, cwd=cwd, max_per_day=args.max_gemini_calls_per_day)
    else:
        output = run_codex(prompt, cwd=cwd, sandbox=args.sandbox, max_per_day=args.max_codex_calls_per_day)

    print("\n===== 최종 출력 =====")
    print(output)


if __name__ == "__main__":
    main()
