# Autoresearch Loop

**Slug:** `autoresearch-loop` · **Owner subject:** [agent-harness-loops](../subjects/agent-harness-loops/brief.md)
**Subjects:** [agent-harness-loops](../subjects/agent-harness-loops/brief.md), [agent-memory-knowledge](../subjects/agent-memory-knowledge/brief.md)
**Referenced by (5):**
- [Autoquant: Karpathy autoresearch swarm applied to multi-factor quant backtests](../items/x-2032330665081839791/card.md) — example, technique — agent-harness-loops
- [Hyperspace v3: generic Karpathy autoresearch swarms, Research DAG, and Warps](../items/x-2032671842230501729/card.md) — technique, claim-source — agent-harness-loops
- [Codex auto-research loop: 212× faster QR kernel on GPU Mode](../items/x-2074912810803560497/card.md) — example, claim-source — agent-harness-loops
- [Survey maps reliable evaluation for self-evolving agents (L0–L4)](../items/x-2087444616832594022/card.md) — reference, claim-source — agent-harness-loops
- [Garry Tan gbrain-evals: SOTA memory retrieval without LLM-in-loop](../items/x-2094462971598754010/card.md) — tool, claim-source — agent-memory-knowledge

<!-- NOTES:START -->
Self-improving research swarms with an eval, not a single long chat.
Owner subject: `agent-harness-loops`. Referenced by 5 item(s): x-2032330665081839791, x-2032671842230501729, x-2074912810803560497, x-2087444616832594022, x-2094462971598754010.
Score items that use this method on the owner brief's comparison axes. Do not treat the slug as a product name.
If a later pass splits this slug, file a registry alias — do not edit cards by hand.

**2026-09-04 capture — Chadha primer host still unreachable.** `https://autoresearch.aman.ai` connect-timeout (25s) and jina 422 (page.goto 15s). Wayback CDX also timed out. No GitHub repo from `autoresearch + chadha` search. The tweet screenshot of the TOC remains the only outline. Do not invent section names beyond that still.

**2026-09-04 capture — neighbor hosts.** `https://autoresearch.aman.ai/` still connect-timeout (12s). `https://aman.ai/autoresearch` HTTP **404**. `https://www.aman.ai/autoresearch` **301**. GitHub HTML search `autoresearch chadha` returned a results page with no obvious primer repo. Screenshot TOC on the card remains the only outline.

**2026-09-04 capture — live primer is on aman.ai, not the timed-out subdomain.** Homepage `https://aman.ai/` HTTP 200, **64,480** B, title “aman.ai • the art of artificial intelligence”, lists href `primers/ai/autoresearch-and-metaharness`. Live page `https://aman.ai/primers/ai/autoresearch-and-metaharness/` HTTP **200**, **308,037** B (301 to trailing slash). Title “Aman's AI Journal • Primers • Autoresearch and Metaharness”. **14** H2 / **143** H3. Overview: “an AI coding agent proposes a change, edits an executable research artifact, runs a bounded experiment, reads the metric, keeps or reverts the change, and repeats until the search budget is exhausted.” Working definition: five components — bounded sandbox, editable artifact, proposer agent, evaluator, durable memory. Concrete single-GPU example is `karpathy/autoresearch` (`train.py`, fixed **5-minute** runs, `val_bpb`). Meta-Harness is “the natural generalization … from ‘optimize a training file’ to ‘optimize the harness around an LLM system’” (cites Lee et al. 2026). “What gets optimized” names **Prompt construction**, **Retrieval policy**, **Memory update**, **Tool orchestration**, **Output parsing and repair**. Harness = “executable environment wrapped around a fixed model” / “policy over context and control flow.” Page citation bibtex year is **2020** (`Chadha2020DistilledAutoresearchMetaharness`); do not collapse that with the 2026 Lee paper. `autoresearch.aman.ai` is still not this page. Receipt `analysis/_work/captures/aman-autoresearch-primer.json`.

**2026-09-05 capture — Arbor reply + paper.** Must-read [x-2080856252687745093](../items/x-2080856252687745093/card.md) now `captured_full` (4/4). New reply `2081160818394034487` (@papersdatacode) names Arbor and proposes sideways embedding edges. Paper `https://arxiv.org/abs/2606.11926` **200 / 44,678 B**; ar5iv **645,538 B**. Title **Toward Generalist Autonomous Research via Hypothesis-Tree Refinement**. Coordinator + short-lived executors + Hypothesis Tree Refinement (HTR). Autonomous Optimization: best held-out on **all six** tasks; **>2.5×** average relative held-out gain vs Codex and Claude Code. MLE-Bench Lite **86.36% Any Medal** with GPT-5.5. Ranking language (“strongest result”) is the paper’s — quote integers only. Receipt `analysis/_work/captures/arbor-arxiv-2606.11926.json`. Do not collapse Arbor with the Chadha primer host.
<!-- NOTES:END -->
