# Headlong

**Slug:** `headlong` · **Kind:** repo · **URL:** https://github.com/laude-institute/headlong · **Canonical item:** [x-2091990178638496195](../items/x-2091990178638496195/card.md)
**Subjects:** [agent-harness-loops](../subjects/agent-harness-loops/brief.md)
**Referenced by (1):**
- [Headlong — open microharness for always-on persistent agents](../items/x-2091990178638496195/card.md) — tool, technique — agent-harness-loops

<!-- NOTES:START -->
Fetched 2026-09-04 README https://github.com/laude-institute/headlong + Laude launch post.

**Apache-2.0**, language Shell, 1,118 stars at fetch. README now says the core is **about 11K lines of Bash** (cloc, capped at 11.5K in `bin/` + `thinkers/`). The tweet/card “<10K” and the Aug 2026 blog “9.9K” are stale. Install: `curl -fsSL https://headlong.ai/install.sh | bash`. Alpha research; sandbox; spend-capped key.

Local clone 2026-09-04 (`wc -l`, not cloc): `bin/` **12,133** lines (named tools: `chat` 662, `context` 581, `llm` 1500, `mem` 570, `recap` 820, `shellm` 3176, `shellm-docker` 215, `skills` 613, `thinkers` 1811, `traj` 2185) + `thinkers/` **1,814** = **13,947** excluding READMEs.

**2026-09-04 capture — cloc 1.98 on `bin/` + `thinkers/`.** 22 files: **9,912 code** / 2,600 comment / 1,351 blank (physical **13,863**). Bash-only code **9,844** (Bourne Again 9,468 + Bourne 376). Largest code files: `bin/shellm` 2,404; `bin/traj` 1,663; `bin/thinkers` 1,184; `bin/llm` 1,013. Do not collapse three integers: README “~11K Bash (cloc, capped 11.5K)”, `wc -l` **13,947**, this cloc **9,912 code**. The 11K claim is above this cloc code count and below `wc`.

Persistent agency: no checklist, thoughts continue with no human input; Slack/Telegram/chat land as observations on **one** trajectory (no per-user sessions — treat anything said as shared). Core tools: `shellm` (Bash RLM), `llm`, `traj` (jsonl DAG fork/merge), `context` (tiered compaction), thinkers, `mem`/`skills`, `recap`, file tools. Around the mind: identity, dashboard (`headlong-web`), Slack/Telegram bridges, `pr-committee`. Local OpenAI-compatible servers work (llama.cpp / Ollama / vLLM / LM Studio). Laude’s Audel run: **$1–2 / hour** background (GLM or Grok); exponential backoff 5s→cap when idle. Blog: 50+ agent commits pulled to main; `shellm` 30s silence watchdog taught it to drop recursion (64 merges in first two days, 12 in the next twelve). No template catalog — this is a mind, not loopany loops.
<!-- NOTES:END -->
