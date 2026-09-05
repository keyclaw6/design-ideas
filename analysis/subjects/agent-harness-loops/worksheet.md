# Judgment worksheet: agent harnesses & loops (agent-harness-loops)

Owner aliases: autoresearch, harness, agent ops. Memory/KB systems → [agent-memory-knowledge](../agent-memory-knowledge/worksheet.md). MCP/browsers → [mcp-and-agent-browsers](../mcp-and-agent-browsers/worksheet.md).

## agent-harness-loops — short stack to try

The 35 primaries are mostly essays and pointers. Four *runnable* control planes showed up.

1. **Named loops you can rerun.** loop-library / loopany.ai templates ([x-2086790895538700379](../../items/x-2086790895538700379/card.md)). Headlong always-on Bash microharness ([x-2091990178638496195](../../items/x-2091990178638496195/card.md)). session-migrate when you change harness mid-job ([x-2091970263088816272](../../items/x-2091970263088816272/card.md)).
2. **Autoresearch with an eval, not a long chat.** Must-read Chadha primer ([x-2080856252687745093](../../items/x-2080856252687745093/card.md)). Must-read Codex QR kernel 212× claim ([x-2074912810803560497](../../items/x-2074912810803560497/card.md)). Hyperspace / Autoquant swarms ([x-2032671842230501729](../../items/x-2032671842230501729/card.md), [x-2032330665081839791](../../items/x-2032330665081839791/card.md)). rauchg is-agentic loop-to-100 ([x-2090858571613470919](../../items/x-2090858571613470919/card.md)).
3. **Permission / blast radius.** Kun Chen disposable Nix + gated secrets ([x-2082316720086405524](../../items/x-2082316720086405524/card.md)). fini “one login, six bots, 24k actions” ([x-2094110975045554191](../../items/x-2094110975045554191/card.md)).
4. **Observe the session.** Blume Sidecar config-drift watch ([web-blume-codes](../../items/web-blume-codes/card.md)). Sideshow.sh visual inspect ([x-2091622497393225801](../../items/x-2091622497393225801/card.md)). Pi-family extensions (shepherdr, clarify, voice) if the harness is already Pi.

Cookbooks (Anthropic Dynamic Workflows, cost_optimization, Control Plane X article, LangChain MDA) are references. Use them after a loop exists.

## agent-harness-loops — axis scores

| item | runnable loop vs essay | permission / blast-radius | eval / OOS check | session persist / migrate | multi-agent vs single |
|---|---|---|---|---|---|
| loop-library | high (23 named prompts on loopany.ai) | local agent; server does not run LLM | “shipped” still marketing | cadence per loop | varies |
| Headlong | high (README ~11K cap 11.5K; `wc` **13,947**; cloc 1.98 **9,912 code**) | Slack/Telegram in; Docker default | none in card | designed always-on | one mind, many people |
| session-migrate | n/a (converter) | n/a | n/a | high (this *is* migrate) | n/a |
| Chadha primer | essay + site | n/a | primer on evals | n/a | research swarm |
| Codex 212× QR | example write-up | unknown | GPU Mode task | unknown | search loop |
| Hyperspace / Autoquant | claimed swarm | unknown | backtests claimed | DAG claimed | multi |
| is-agentic 100/100 | high (external scorer) | n/a | high (the scorer) | loop until pass | single |
| Kun Chen YOLO + Nix | technique | high (disposable machine) | none | n/a | single |
| fini 24k actions | warning | high (shared profile) | none | n/a | six bots, one login |
| Blume Sidecar | watcher | n/a | n/a | config files | n/a |
| Sideshow.sh | visual inspect | n/a | n/a | mid | n/a |
| pi-shepherdr | high (271-token orchestrator) | pane isolation | none | Herdr panes | multi Pi |
| Ouroboros | high (MIT harness; paper + site) | reviewed commits; Hope live | Terminal-Bench / OSWorld / CL-Bench stated | git + Hope memory | self-modify |
| Anthropic / Control Plane / MDA | cookbook / X article (no Stanford string; not arXiv 2505.06817) | varies | cookbook has a task; article is a pharma case | folder-as-agent (MDA) | multi (article: one reasoner + fetch sub-agents) |
| awesome lists / training hubs | index | n/a | n/a | n/a | n/a |

## agent-harness-loops — claims that need a receipt

- Codex “212×” QR kernel — **blog says 232×** (419,000 µs → 1,805 µs), 12th of 183, GPU Mode `qr_v2` compact-Householder QR ([codex](../../tools/codex.md)). Tweet number is stale.
- Autoquant 135 agents / four-layer pipeline — architecture claim.
- fini 23,999 actions in 20 minutes — warning anecdote; useful as a blast-radius story, not a benchmark.
- Anthropic cost $0.29 → 90% less — cookbook; re-run the notebook.
- Headlong “<10K LOC” — **README now says ~11K** (cloc, capped 11.5K). Local `wc -l` is **12,133 + 1,814 = 13,947**. cloc 1.98 on the same dirs is **9,912 code** / 2,600 comment / 1,351 blank. Do not collapse the three integers. Blog 9.9K / tweet <10K are stale. Persistent-agency + $1–2/hr idle cost are first-party ([headlong](../../tools/headlong.md)).
- loopany reddit-karma paste prompt lives in `meta.json` `description`; author story −4→92 comment karma / 7 days is first-party, not a bake-off ([loop-library](../../tools/loop-library.md)).
- Ouroboros tweet numbers match the paper (arXiv:2608.08311, https://ouroboros-agent.ai/): Terminal-Bench 2.1 Opus 5 **86.97% raw / 86.74% audited** (386/445 after one shortcut zeroed); OSWorld-Verified **90.69%** (327.39/361, non-Google-Drive); CL-Bench **0.2301** (five-rollout). Hope: 161 days to 2026-08-06, $110.6K spend, 79.7B tokens, seven surfaces. MIT (`razzant/ouroboros`). Paper uses ranking language; quote the integers only. Do not confuse with `q00/ouroboros` (spec-first workflow engine).

## agent-harness-loops — do not treat as load-bearing

- Sindresorhus awesome, awesome-llm-apps, Spanish six-repo roundups — indexes.
- Rivet 825-page PDF and Ondrej setup article — manuals, not a loop you can start tonight.
- Karpathy REASONING paste — prompt wording, not a harness.
- Secondary design / memory / MCP items — wrong primary.

## agent-harness-loops — next capture work

1. popcorn CLI install/submit and the **live board** (sankalp1999 26th / 3916 µs vs blog 12th / 1805 µs) are on [codex](../../tools/codex.md). GPU Mode `GET /api/leaderboard/773` restores the integers the HTML SPA dropped and names Harbor `submission_id` **796445**. Remaining: the author’s public `submit_logs/` tree (reply `t.co/hBpJvk3YZV` is a photo; five gists unrelated; GitHub code search 401).
2. Headlong cloc 1.98 (**9,912 code**) vs `wc` 13,947 vs README ~11K, and the reddit-karma prompt location, are on the tool NOTES. Remaining: same missing `submit_logs/` tree (API id 796445 is not a log dump).
3. Chadha primer is live at `https://aman.ai/primers/ai/autoresearch-and-metaharness/` (**308,037** B, 14 H2 / 143 H3). `autoresearch.aman.ai` still times out; `aman.ai/autoresearch` is still **404**. Five-component working definition + Meta-Harness optimize list on [autoresearch-loop](../../techniques/autoresearch-loop.md). Keep fini’s shared-profile warning next to any “six Grok bots” outbound pitch.
4. Ondrej X article **2094424686499160065** body is on [herdr](../../tools/herdr.md) (14,952 chars; eight H2s; bb/cmux/Herdr/Pi/skills). Cursor “10–15% → 60%” merged-PR share stays the author’s graph. Card gap is now `thread-partial` (51/3), not `linked-page-unfetched`.
5. Control Plane article **2087107935079940096** is on [agent-harness-ops](../../techniques/agent-harness-ops.md): **15,151** chars / no Stanford / **3–4 weeks → 20–30 minutes** (tweet 4 weeks / ~10× tokens is paraphrase). Do not collapse with Kandasamy arXiv 2505.06817. Card gap stays `thread-partial` (30/3).
