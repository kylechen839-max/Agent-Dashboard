# Agent dashboard: notes for Claude Code sessions

This repo is one static page, `dashboard/index.html`, published as the
claude.ai artifact https://claude.ai/artifact/BWYCUWxJxBvG6MJvnsaqvn, plus
its docs, desktop launchers and tests. The `/build-feature` master that
writes the dashboard's data lives in the Hey Claude repo
(kylechen839-max/Claude-Personal-Assistant); the row schemas it writes are
in `dashboard/README.md`, and changes to them go in both repos.

## Layout
- `dashboard/index.html`: the page (no external assets, no document tags;
  claude.ai wraps it).
- `dashboard/moved.html`: a static card (no script) published over the
  old artifact URL, linking to the current one.
- `dashboard/README.md`: schemas, views, chat box, rules, manifest.
- `dashboard/WATCHDOG.md`: the hourly watchdog's prompt (one fenced block).
- `dashboard/desktop/`: `open-dashboard.cmd` (CRLF) and
  `open-dashboard.command` (LF, executable). "Get desktop app" in the page
  embeds the same text (`LAUNCHER_TEXT`, `LAUNCHER_KINDS`); keep them in
  step, the tests compare them byte for byte.
- `.claude/skills/`: vendored design skills (`frontend-design`,
  `web-design-guidelines`, `accessibility`); sources, pins and where
  these rules win are in `.claude/skills/DESIGN_SKILLS.md`.
- `tests/`: pytest (`test_agent_dashboard.py`) and node
  (`tests/js/agent-dashboard.test.mjs`).

## How to test
```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest -q
node --test tests/js/agent-dashboard.test.mjs   # give the file; the directory form fails on Node 22
```
Every change comes with a test; a new test must fail on the old code.
Never skip or weaken a test to get green.

## Rules
- **The page never writes the db.** No `.set(`/`.update(`/`.delete(`/
  `.add(` anywhere in the page (Map and Set included; keep page state in
  arrays or plain objects). The one exception is the single
  `assets.delete` for an attachment Kyle removes before sending. Its only
  other writes are the chat box's comment (Kyle's own press:
  `sendToClaude`, or a plain `comments.create`/`comments.reply` when no
  Claude session is watching) and its five localStorage keys.
- **Rows are untrusted data.** Render with `textContent` and elements
  only (no `innerHTML` and friends); links only to the session and PR
  prefixes, with `noopener noreferrer`.
- **No secrets in this repo.** There are none to hold; if one is ever
  needed it goes in a gitignored `.env`, never in a file that is
  committed, logged or published.
- **No CDN or external assets** in the page.
- **Desktop only:** no phone layout.
- Platforms: the launchers are for Windows and macOS; the tests need only
  Python 3.10+ with pytest and Node 18+ (CI runs them on Ubuntu).
- Docs match the code: README, SECURITY.md, PRIVACY.md and CHANGELOG.md.
- Don't commit secrets, don't force-push, and leave merging to Kyle (PRs).
