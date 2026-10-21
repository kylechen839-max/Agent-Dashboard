"""The hourly heartbeat workflow wakes the coordinator through a check run
on the `claude/heartbeat` PR, with the narrowest token it needs."""

from pathlib import Path

WORKFLOW = Path(__file__).resolve().parent.parent / ".github" / "workflows" / "heartbeat.yml"


def test_heartbeat_runs_hourly_and_by_hand():
    text = WORKFLOW.read_text(encoding="utf-8")
    assert 'cron: "17 * * * *"' in text
    assert "workflow_dispatch:" in text


def test_heartbeat_token_can_only_post_checks():
    text = WORKFLOW.read_text(encoding="utf-8")
    perms = text.split("\npermissions:", 1)[1].split("\njobs:", 1)[0]
    lines = [line.strip() for line in perms.splitlines() if line.strip()]
    assert lines == ["checks: write", "pull-requests: read"]
    assert "actions/checkout" not in text  # it never runs repo code


def test_heartbeat_targets_only_the_heartbeat_pr():
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "--head claude/heartbeat --state open" in text
    assert "conclusion=success" in text
    assert "exit 0" in text  # no open PR is not a failure
