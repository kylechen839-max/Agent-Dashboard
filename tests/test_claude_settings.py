"""The repo's Claude Code settings only pre-approve what Kyle allowed:
starting sessions (2026-10-21, for the trusted relay on his own machines)."""

import json
from pathlib import Path

SETTINGS = Path(__file__).resolve().parent.parent / ".claude" / "settings.json"


def test_settings_allow_only_create_session():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    assert data == {"permissions": {"allow": ["mcp__claude-code-remote__create_session"]}}
