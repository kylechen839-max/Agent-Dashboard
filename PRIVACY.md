# Privacy

The dashboard stores nothing itself; everything below lives on claude.ai
(the artifact) or in your browser.

| What | Where | Notes |
|---|---|---|
| Run and agent rows | The dashboard artifact's db on claude.ai (`runs`, `agents`) | Written by the `/build-feature` master: names, links, phases, counts, short reasons and the master's own short summaries. No conversation text, logs or secrets |
| Dev team dashboard chat | The artifact's db, under your private `data/users/<your id>/chat-<session>/msgs` subtree (readable only by you) | Your messages to a coordinator and its replies, written by the coordinator; the page only reads them. Messages you send from the chat box are also posted as comments on the artifact (claude.ai asks for consent once). Chats older than 30 days are pruned |
| Chat attachments | The artifact's asset store | Files you paste or drop into the chat box, which only you (its owner and editor) can open; kept until you delete them or the artifact |
| Browser storage | localStorage in your browser | Only the view, window layout (including which windows you hid), filter, the coordinator you picked (one claude.ai session link) and whether auto-close is on. It never leaves your browser |
| Desktop launchers | Your computer | They only open the dashboard URL; they store nothing |
