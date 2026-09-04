# Thread — Memoria — git-like snapshots and branches for AI agent memory (x-2087208634493095978)

**Status:** captured_partial · **Author thread:** none · **Replies reported:** 4 · **Captured:** 3 · **Relevant:** 2 · **Unfetched:** 1 · **Truncated:** False
**Fetch log:** x-web-dom→ok (2026-09-04T17:54:20Z); fxtwitter-api→ok (2026-09-04T17:54:20Z)
**Raw payloads:** `raw/items/x-2087208634493095978/thread-raw/x-web-dom-20260904T175304Z.html`

**Author continuation (0 posts).**
**Quoted.**
> **@tom_doerr** · 2087322314820268058
> 🧵 Just open-sourced SodaMem — a continuously learning agentic memory system for AI agents.
It does more than store and retrieve.
It can plan how to recall, trace claims back to the original conversation turns, and track when a fact is still valid or has been superseded.
If https://t.co/UAo4x4ivBV

**Relevant replies (2 of 3 captured).**
> **@tom_doerr** · 2087326166369869970 · depth 1 · alternative-tool
> @tom_doerr Interesting to see version-control style memory (snapshots/branches).
We took a different route in SodaMem — temporal validity with valid_from / valid_until and SUPERSEDES links, so old versions stay readable instead of being rewritten.
Every memory also points back to the exact

> **@hellovirgil_** · 2087238234614968811 · depth 1 · alternative-tool
> @tom_doerr Campfire works at the layer beneath memory: the actual execution state. Instead of persisting memory across sessions, we fork the entire session using git worktrees. Each fork is a branch: a snapshot of the codebase at that moment, plus the full JSONL trace of what the agent did

**Dropped as noise:** 1 replies (praise, emoji, bots, unrelated promo).
