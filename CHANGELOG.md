# Changelog

## Unreleased

- Dashboard redesign: one calm card look in both themes (no dark terminal
  body); a ⋯ menu at the top right with Close idle, Auto-close, Reset
  layout and Get desktop app; window controls that show on hover or
  focus; a one-line coordinator summary with a History fold for status
  lines and the run id; Claude-app style chat with small delivery icons
  (✓, ✓✓) whose tooltip has the full text; presence carries the working
  step.
- Grid: a "Claude listening" / "No Claude session listening" pill in the
  toolbar (any session watching the dashboard, re-checked on show, focus,
  visibility and at most once a minute). With no session watching, every
  coordinator chat shows a banner saying messages won't wake it (with
  Open session), and Send still posts your message as a plain comment a
  session can read later.
- Grid: an "N waiting" badge counts your messages with no Seen or reply
  yet and jumps to the oldest.
- Grid keyboard shortcuts: `/` to the chat box, Alt+1–9 to maximize a
  window, `?` for the shortcuts panel (Esc closes it).
- Search a coordinator conversation (🔍 in its title bar), with an
  "N of M" count.

- The agent dashboard now lives in its own repo (extracted with its git
  history from kylechen839-max/Claude-Personal-Assistant, where it was
  `tools/agent-dashboard/`). The page is in `dashboard/`, the tests in
  `tests/`, with CI for pytest and the node tests.
- "Get desktop app" offers only the dashboard launcher; the PC hub
  launcher and the PC hub itself were removed (the chat box, through
  claude.ai comments, is the one way to message the coordinator).

## Before the move (from the Hey Claude changelog)

- "Close idle agents" in the Grid toolbar (never coordinator windows) and
  an opt-in auto-close; the maximized window's restore is an icon button
  (⤡); select text in a chat message and Reply to quote it; paste or drop
  images, PDFs and text files into the chat box (up to 5 per message,
  kept in the dashboard's own file store).
- Grid: a Coordinator picker shows only the chosen coordinator session's
  windows (default All); the choice is kept per viewer, and Forget clears
  a pick whose session has no recent runs.
- Desktop-only (the phone layout is gone). Windows can be hidden and
  restored from "Hidden (N)" or Show all, the Runs view and window chrome
  got a calmer unified look, and "Get desktop app" saves the Windows or
  Mac launcher as a small zip.
- The coordinator chat always shows whether the coordinator is in a task
  or idle, and a message sent mid-task shows as queued until the
  coordinator reads it.
- The coordinator chat looks like the Claude Code app (full-width
  replies, your messages in bubbles, collapsible activity rows, an
  animated working line) and shows each message's delivery: Sending,
  Delivered, Seen by coordinator, Working, or an amber warning when the
  coordinator hasn't picked it up after 2 minutes.
- The Grid is a full-screen window workspace: windows auto-tile, with a
  dark monospace body, run colours, maximize (Esc or Restore) and an
  Active only / All recent filter.
- Each coordinator window has a chat box: type to the coordinator (sent
  as a comment to Claude) and read everything it tells you, rendered as
  markdown; the coordinator mirrors its messages to your private
  dashboard storage.
- The Grid view shows one panel per `/build-feature` coordinator (phase,
  round, elapsed time, latest status lines) with a window for each
  researcher, builder and judge, all written by the master.
- Desktop launchers open it in its own Chrome or Edge window on Windows
  and macOS.
- A read-only agent run dashboard (a private claude.ai page): one row per
  `/build-feature` run; the page flags runs that have gone quiet past
  their phase's limit. PR-ready, blocked and dead runs untouched for 7
  days count as done.
