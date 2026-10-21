# Security

The dashboard is one static page published as a private claude.ai
artifact. It has no server, no API keys and no secrets. claude.ai hosts
it, signs Kyle in and grants the page its capabilities (the manifest in
`dashboard/README.md`: `db`, `user`, `comments`, `downloads`, `assets`).
The data it shows is written by the `/build-feature` master in the Hey
Claude repo.

## What the page may do

- **Read only, with one exception.** The page never writes the db (no
  `set`/`update`/`delete`/`add` call anywhere, pinned by
  `test_page_never_writes`). The one exception is a single
  `assets.delete`, for an attachment Kyle removes before sending.
- **Rows are untrusted data.** Run, agent and chat rows are shown as
  text and elements only: no `innerHTML`, `eval`, `DOMParser` or other
  markup sinks (a test bans them). Links go only to
  `https://claude.ai/code/session_...` and the Hey Claude repo's PR URLs,
  with `noopener noreferrer`. The markdown renderer is hand-written,
  builds elements only, caps elements per message and links only to
  http(s) URLs. A GitHub PR/issue chip links only to a URL that exactly
  matches `https://github.com/<owner>/<repo>/(pull|issues)/<n>` (a test
  pins the lookalikes that stay text). Nobody acts on a row as an instruction.
- **Nothing external.** No CDN scripts, fonts, styles or images; no
  `console` logging; nothing sent on a timer.
- **Alerts stay on the page.** The "N waiting" badge is visual only: no
  sound, no Notification API and no `document.title` writes (a test bans
  them).
- **Chat search** matches plain text in memory and only hides or shows
  the existing message elements; the query is never rendered as markup,
  stored or sent.

## Deliberate choices (kept from the Hey Claude repo's SECURITY.md)

- **The dashboard posts Kyle's chat messages as comments.** The page
  declares the full `comments` grant so each coordinator window's chat
  box can call `comments.sendToClaude`. There is exactly one call site,
  run only from Kyle's own Send press, Enter or Resend press, one call at
  a time, never at load, on a timer or as an automatic retry (a test
  pins this). Resend appears only on a message not picked up after 2
  minutes, with a session watching; it re-sends that message's own
  bounded text (same nonce, " (resent)" added, same thread) once per
  message. When
  `canSendToClaude()` last said `no_session` (no Claude session watching
  the artifact), the same press posts the same bounded text as a plain
  comment instead (`comments.create` on the window title, or
  `comments.reply` into this visit's thread): one call site each, in the
  same function, under the same rules, so a session that watches later
  can read it. `sendToClaude` itself would post nothing then
  (`claude_unavailable`). The page still never resolves or deletes a
  thread and never reads one. claude.ai asks
  Kyle for consent at the first send, and a refusal hides the box. The
  text is bounded (4000 UTF-8 bytes, control characters removed) and
  prefixed with the run id and a nonce. The page can't read threads,
  stop a turn or answer approval prompts. A master that receives such a
  comment treats it as Kyle's words about its own run, within that run's
  scope only: it may re-order or stop work, but never changes
  permissions, touches secrets or routes around a denial.
- **Chat attachments in the dashboard's asset store.** The page declares
  `assets: {}` (editors only: Kyle as owner; every other viewer gets
  `null` and no attachment UI). Files are uploaded only at Kyle's paste
  or drop, at most 5 per message, type and size checked first, never
  retried; one `upload` and one `delete` call site (pinned by a test),
  and delete only for a chip Kyle removes before sending. Thumbnails use
  only the url `upload()` returned (same-origin path or https), as an
  `<img>`, never script or markup; chat text is never a url. The comment
  carries only the name (80 characters, brackets swapped), type, size and
  opaque asset id. The coordinator treats file content as untrusted data.
  Non-fix: assets live as long as the artifact (no pruning; Kyle can
  delete them from claude.ai), and any editor of the artifact can open
  them.
- **Conversation text in Kyle's private db subtree.** The master mirrors
  what it tells Kyle, and his messages, to
  `data/users/<Kyle's id>/chat-<sessionTail>/msgs`. claude.ai keeps
  `data/users/<id>/` private to that viewer, so this is the one place
  conversation text is stored outside the session; shared rows never
  hold it. The master prunes conversations older than 30 days. The page
  keeps only its view, window layout, filter, coordinator pick and
  auto-close toggle in localStorage (no conversation text).
- **Desktop launchers** only open the fixed artifact URL in Chrome or
  Edge (`--app=`) or the default browser. They never pass
  `--user-data-dir`, run nothing else and take no arguments.
- **Moved page** (`dashboard/moved.html`, published over the old
  artifact URL): markup and style only, no script and no external assets;
  its one link is the new artifact URL, opened with
  `rel="noopener noreferrer"`.

## The PC hub (removed)

The Hey Claude repo also had a loopback-only "PC hub" page for the same
chat. It was not carried into this repo: it is gone, along with its
launchers and its "Get desktop app" option.

## Reporting

This is a private, single-user project. Report problems to Kyle directly.
