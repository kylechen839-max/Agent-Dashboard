# Agent dashboard

Kyle's dashboard for his `/build-feature` dev team: a private claude.ai
page that shows each run (Runs view) and a window workspace of the
coordinator and agent sessions with a chat box per coordinator (Grid
view).

- **Live page:** https://claude.ai/artifact/CpPTyJkkHZ7CK8jsPYZq4G (open it
  signed in to claude.ai on a desktop browser).
- **Source:** [`dashboard/index.html`](dashboard/index.html). The page is
  a claude.ai artifact: a Claude Code session (the coordinator, or
  "master") republishes it from this file. Nothing in this repo runs on
  a server, and there are no secrets or API keys here.
- **Who writes the data:** only the master, from the Hey Claude repo
  (kylechen839-max/Claude-Personal-Assistant), where the
  `/build-feature` skill and its `.claude/settings.json` live. The page
  only reads, except for Kyle's own chat messages (posted as claude.ai
  comments) and his chat attachments.
- **Details:** [`dashboard/README.md`](dashboard/README.md) (the row
  schemas, the views, the chat box and its rules) and
  [`dashboard/WATCHDOG.md`](dashboard/WATCHDOG.md) (the hourly trigger
  that marks dead runs).

## Layout

```
dashboard/
  index.html          the artifact page (HTML, CSS and script in one file)
  README.md           schemas, views, chat, rules
  WATCHDOG.md         the hourly watchdog trigger prompt
  desktop/
    open-dashboard.cmd       Windows launcher (CRLF)
    open-dashboard.command   macOS launcher (LF, executable)
tests/
  test_agent_dashboard.py    page contract, README/watchdog/launcher checks
  js/agent-dashboard.test.mjs  the page's script run in node:vm
```

## Desktop launchers

To keep the dashboard in its own window (no tabs or address bar), use a
launcher. Each opens the page with Chrome's or Edge's `--app=` option and
your normal browser profile (so you are already signed in), or a normal
tab in the default browser if neither is installed.

- **Windows:** double-click `dashboard\desktop\open-dashboard.cmd`.
- **macOS:** double-click `dashboard/desktop/open-dashboard.command`
  (the first time, right-click → Open to get past Gatekeeper).
- **From the page:** **Get desktop app** (in the ⋯ menu, top right) saves the same
  launcher as a small zip.

More, including pinning to the taskbar or Dock, is in
[`dashboard/README.md`](dashboard/README.md#desktop-window).

## Tests

Offline, no packages beyond pytest; Node 18+ for the page tests.

```
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt      # Windows: .venv\Scripts\pip
.venv/bin/python -m pytest -q
node --test tests/js/agent-dashboard.test.mjs
```

The pytest suite also runs the node tests when `node` is installed, and
runs `shellcheck` on the Mac launcher when it is installed. CI
(`.github/workflows/tests.yml`) runs both on Ubuntu.

## Publishing

The master publishes `dashboard/index.html` to the artifact URL above
with the manifest pinned in `dashboard/README.md`. Change the page here
first, with its tests, then republish; the URL stays the same.
