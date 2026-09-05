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
| session-migrate | n/a (converter; MIT **82★**; description **18** harnesses) | n/a | n/a | high (this *is* migrate) | n/a |
| Chadha primer | essay + site | n/a | primer on evals | n/a | research swarm |
| Codex 212× QR | example write-up | unknown | GPU Mode task | unknown | search loop |
| Hyperspace / Autoquant | claimed swarm; live shell `agents.hyper.space` **5,803 B**; repo `hyperspaceai/agi` MIT **2,038★** | unknown | backtests claimed | DAG claimed | multi |
| is-agentic 100/100 | high (external scorer; live featured **100/100** on is-agentic.com) | n/a | high (the scorer) | loop until pass | single |
| Kun Chen YOLO + Nix | technique | high (disposable machine) | none | n/a | single |
| fini 24k actions | warning | high (shared profile) | none | n/a | six bots, one login |
| Blume Sidecar | watcher | n/a | n/a | config files | n/a |
| Sideshow.sh | visual inspect (live **51,220 B**; “207 Now playing” is a counter) | n/a | n/a | mid | n/a |
| pi-shepherdr | high (271-token orchestrator) | pane isolation | none | Herdr panes | multi Pi |
| Ouroboros | high (MIT harness; paper + site) | reviewed commits; Hope live | Terminal-Bench / OSWorld / CL-Bench stated | git + Hope memory | self-modify |
| Anthropic / Control Plane / MDA | cookbook / X article (dynamic notebook **52,675 B**: 16 concurrent / **1,000** cap; cost notebook **$0.2906/task** + 90% vs Opus) | varies | cookbook has a task; article is a pharma case | folder-as-agent (MDA) | multi (article: one reasoner + fetch sub-agents) |
| awesome lists / training hubs | index | n/a | n/a | n/a | n/a |

## agent-harness-loops — claims that need a receipt

- Codex “212×” QR kernel — **blog says 232×** (419,000 µs → 1,805 µs), 12th of 183, GPU Mode `qr_v2` compact-Householder QR ([codex](../../tools/codex.md)). Tweet number is stale.
- Autoquant 135 agents / four-layer pipeline — architecture claim. Hyperspace v3 237 / 14,832 is tweet-only; first-party is `hyperspaceai/agi` MIT **2,038★** + a **5,803 B** agents.hyper.space shell. leftover12 install/commit t.co hit the same two hosts. GitHub search `autoquant` total **92** is other products — do not collapse ([hyperspace](../../tools/hyperspace.md); [x-2032330665081839791#c3](../../items/x-2032330665081839791/card.md)).
- fini 23,999 actions in 20 minutes — warning anecdote; useful as a blast-radius story, not a benchmark. leftover12 github t.co is `0xf1n1` with **0** public repos; X article **404** ([x-2094110975045554191#c3](../../items/x-2094110975045554191/card.md)).
- Pocock `/improve-codebase-architecture` is first-party on aihero.dev **368,578 B**: survey HTML report, **no code change**. Repo `mattpocock/skills` MIT **250,614★** this pass (leftover12 was **250,588★**) ([x-2086838432102228008#c2](../../items/x-2086838432102228008/card.md)). leftover14 Pi leftover: grilling + official handoff are in `productivity/`; wayfinder / ask-matt **404**; custom `/handoff` at 100k stays tweet-only; ponytail is `DietrichGebert/ponytail` MIT **126,322★** ([x-2087263510090874911#c3](../../items/x-2087263510090874911/card.md)).
- Anthropic cost $0.29 → 90% less — raw notebook now first-party: **$0.2906/task** print + “roughly 90% under the Opus baseline” ([claude-agent-sdk](../../tools/claude-agent-sdk.md)). Still not a re-run on this host.
- Headlong “<10K LOC” — **README now says ~11K** (cloc, capped 11.5K). Local `wc -l` is **12,133 + 1,814 = 13,947**. cloc 1.98 on the same dirs is **9,912 code** / 2,600 comment / 1,351 blank. Do not collapse the three integers. Blog 9.9K / tweet <10K are stale. Persistent-agency + $1–2/hr idle cost are first-party ([headlong](../../tools/headlong.md)).
- loopany reddit-karma paste prompt lives in `meta.json` `description`; author story −4→92 comment karma / 7 days is first-party, not a bake-off ([loop-library](../../tools/loop-library.md)).
- Ouroboros first-party this pass: abs **42,948 B** + `/benchmarks` **6,553 B** + `razzant/ouroboros` MIT **1,265★**. TB 2.1 Opus 5 **86.74%** after one reward-hack zero (raw **86.97%**); OSWorld-Verified **90.69%** vs previous public **90.19%**; CL-Bench **0.2301**. Hope **161-day** in the abstract. Do not add $110.6K / 79.7B unless re-fetched from a longer PDF. Ranking language is the paper/site’s. Do not collapse with `Q00/ouroboros` (**5,769★**). Thread stays `failed` ([agent-harness-ops](../../techniques/agent-harness-ops.md)).

## agent-harness-loops — do not treat as load-bearing

- Sindresorhus awesome, awesome-llm-apps, Spanish six-repo roundups — indexes.
- Rivet PDF is live **11,889,432 B / 893 pages** (Edition 2026.08). Tweet **825** is stale ([rivet](../../tools/rivet.md)). Manual, not a loop you can start tonight.
- Karpathy REASONING paste — prompt wording, not a harness.
- Secondary design / memory / MCP items — wrong primary.

## agent-harness-loops — next capture work

1. leftover19: `gpu-mode/popcorn-cli` MIT **178★**; `reference-kernels` **303★** NOASSERTION. README still names `popcorn submit --leaderboard qr_v2 --profile-brev`. `submit_logs/` stays local. Live board Harbor **796445** / 26th 3916 µs vs blog 12th / 1805 / **232×** already on [codex](../../tools/codex.md) `#c3–#c5`. Remaining: do not keep hunting a public dump.
2. Headlong cloc 1.98 (**9,912 code**) vs `wc` 13,947 vs README ~11K, and the reddit-karma prompt location, are on the tool NOTES. Harbor id **796445** is not a log dump; blog now says `submit_logs/` is local.
3. Chadha primer is live at `https://aman.ai/primers/ai/autoresearch-and-metaharness/` (**308,037** B, 14 H2 / 143 H3). `autoresearch.aman.ai` still times out; `aman.ai/autoresearch` is still **404**. Five-component working definition + Meta-Harness optimize list on [autoresearch-loop](../../techniques/autoresearch-loop.md). Thread is now `captured_full` (4/4); card is `ready`. Reply names Arbor (arXiv:2606.11926): HTR tree; **>2.5×** held-out gain vs Codex/Claude Code; MLE-Bench Lite **86.36%** Any Medal (GPT-5.5). Keep fini’s shared-profile warning next to any “six Grok bots” outbound pitch.
4. Ondrej X article **2094424686499160065** body is on [herdr](../../tools/herdr.md) (14,952 chars; eight H2s; bb/cmux/Herdr/Pi/skills). Cursor “10–15% → 60%” merged-PR share stays the author’s graph. Card gap is now `thread-partial` (51/3), not `linked-page-unfetched`.
5. Control Plane article **2087107935079940096** is on [agent-harness-ops](../../techniques/agent-harness-ops.md): **15,151** chars / no Stanford / **3–4 weeks → 20–30 minutes** (tweet 4 weeks / ~10× tokens is paraphrase). Do not collapse with Kandasamy arXiv 2505.06817. Card gap stays `thread-partial` (30/3).
6. leftover19 HF traces are now on the card: OSWorld-Verified Opus 5 **361** rows self-reported **90.69%**; CL-Bench **6** rows self-reported **0.2301**. Paper + `/benchmarks` + `razzant/ouroboros` MIT **1,265★** already folded. Thread stays `failed`. Do not treat `Q00/ouroboros` as this paper.
7. pi-clarify npm **1.0.1** MIT / GitHub **175★** is on [pi-clarify](../../tools/pi-clarify.md) ([x-2087304957011911157#c2](../../items/x-2087304957011911157/card.md)). Did not run `pi install`.
8. Greg Mushen “Hermes” is an architecture layer name — do not collapse with `NousResearch/hermes-agent` MIT **241,533★** / homepage **90,409 B** v0.21.0 ([hermes](../../tools/hermes.md); [x-2093437790969385283#c3](../../items/x-2093437790969385283/card.md)). leftover12 EP four-layer prompt also does **not** collapse with LifeOS MIT **18,886★** ([x-2086920236079681607#c4](../../items/x-2086920236079681607/card.md)).
9. leftover22 unused Laude Headlong post **227,836 B** still says **9.9K**; install.sh **25,935 B** ([headlong](../../tools/headlong.md) `#c4`). leftover22 unused `pi-gippity-control` README **3,878 B** ([pi-shepherdr](../../tools/pi-shepherdr.md)).
10. leftover26 unused `laude.org` host string is leftover22 `#c4`. leftover26 unused OpenReview `CGO1hDTHNe` stays gated — do not hammer.
11. leftover27 unused `learn.chatgpt.com/training` **305,746 B** lists Work + Codex walkthroughs — no signed-in completion ([chatgpt-training](../../tools/chatgpt-training.md); [web-chatgpt-training#c3](../../items/web-chatgpt-training/card.md)). leftover27 unused `careers.blume.codes` **51,037 B** Teamtailor: Head of Growth + Founding Engineer; founded **2025** ([blume-sidecar](../../tools/blume-sidecar.md); [web-blume-codes#c2](../../items/web-blume-codes/card.md)).
12. leftover28 unused OpenAI Academy events **612,752 B** (**24** Register / **17** Livestream) ([chatgpt-training](../../tools/chatgpt-training.md); [web-chatgpt-training#c4](../../items/web-chatgpt-training/card.md)).
