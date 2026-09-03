## What they are actually doing

Garry Tan (YC CEO; GStack / GBrain) is pointing at **receipts**, not a new product launch. The bookmark is a still of the [gbrain-evals](https://github.com/garrytan/gbrain-evals) comparison table plus a claim that retrieval-for-agents is SOTA **without an LLM in the retrieval loop**, and that they added **memory-save from agent transcript** evals.

**gbrain** — https://github.com/garrytan/gbrain (MIT, TypeScript, **29,487★** / 4,396 forks at capture). README one-liner: “Garry's Opinionated OpenClaw/Hermes Agent Brain.” Long-term memory the agent reads and writes.

**gbrain-evals** — https://github.com/garrytan/gbrain-evals (MIT, TypeScript, **406★** / 73 forks, created 2026-04-22). `package.json` 0.5.1: “BrainBench — public benchmark for personal knowledge agent stacks. Consumes gbrain as a library” (`gbrain` pin `2a56b512…`). Scripts: LongMemEval-style runner, Cat 34/35, world-view, bun tests.

README headline numbers at capture (broader than the tweet still):

- LongMemEval retrieval component: **97.6% any-hit R@5 / 83.4% official `recall_all@5`**, no LLM in the loop. MemPalace 96.6% any-hit settled as that variant ([arXiv 2604.21284](https://arxiv.org/abs/2604.21284)). Cost ~$0.50 / 1,000 questions vs MemPal’s Haiku reranker.
- Cat 35 write path: **88.1%** salient content survives; **1.2% junk leakage (1/86)** in the README — the tweet still says “zero junk leakage.”
- Cat 34: 0 know-to-ask failures on the published harness.
- August 2026 35-agent self-audit: 239 findings, 236 fixed, errata instead of silent edits.

**Same-day changelog:** `[0.5.1] - 2026-08-31` closes the LongMemEval erratum at **83.40% `recall_all@5`** from May raw rows at $0. **`[0.6.0] - 2026-09-01`** (after this tweet) adds receipt gates, Cat 34/35 provenance, session-diversity adapters; ContextFit self-reported All@5 sits at or above gbrain pending a fresh-pin re-run.

Elev_30’s visible reply is the independent-benchmark question (LongMemEval is a public dataset; Cat 34/35 are in-house).

## Open questions

- Tweet-still “zero junk leakage” vs README 1.2% — screenshot predates or omits the Cat 35 correction.
- Remaining ~96 of 99 replies (possible extra harness links).
- Whether anyone posted a third-party memory bench number in those unlisted replies (Elev_30’s ask).
