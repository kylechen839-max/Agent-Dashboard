# Coordinator heartbeat

This branch exists only so its draft PR can carry the hourly
`coordinator-heartbeat` check (`.github/workflows/heartbeat.yml` on
`main`). The coordinator session is subscribed to the PR, so each check
wakes it, and it re-arms its dashboard watch. Never merge this PR; close
it to stop the heartbeat.
