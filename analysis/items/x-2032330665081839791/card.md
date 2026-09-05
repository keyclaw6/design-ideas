# Autoquant: Karpathy autoresearch swarm applied to multi-factor quant backtests

`x-2032330665081839791` · x · thread · en · [source](https://x.com/varun_mathur/status/2032330665081839791) · [raw](../../../raw/items/x-2032330665081839791/)
**Author:** Varun (@varun_mathur) · **Published:** — · **Captured:** 2026-09-04T06:49:23Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** example, technique · **Platforms:** cli

**Summary.** Varun Mathur describes Autoquant v2.6.9: 135 agents mutate four-layer trading pipelines (macro, sector, alpha, risk officer) via Darwinian selection on ten years of market data, with out-of-sample and crisis stress gates.
**Question it answers.** What pipeline shape does Autoquant use for distributed autoresearch on quantitative finance?

**Claims.**
- `x-2032330665081839791#c1` (capability, stated) Autoquant runs ~135 agents with 30 mutations per round and Darwinian selection across a P2P gossip network. — evidence: "30 mutations compete per round. Best strategies propagate across the swarm." [post]
- `x-2032330665081839791#c2` (result, contested) Agents independently converged on dropping three factors and risk-parity sizing, claiming Sharpe 1.32 versus 1.04 baseline. — evidence: "Sharpe 1.32, 3x return, 5.5% max drawdown" [post]
- `x-2032330665081839791#c3` (counter-claim, demonstrated) Install t.co → agents.hyper.space/api/install 5,803 B shell (title Hyperspace Agent). Commit t.co → github.com/hyperspaceai/agi MIT 2,038★. GitHub search `autoquant` total 92 is other products (AdrianAntico/AutoQuant AGPL 251★ and neighbors) — do not collapse this leftover with those repos. Tweet 135 agents / Sharpe 1.32 stay tweet-only. — evidence: "agents.hyper.space 5803 B; hyperspaceai/agi MIT 2038★; GH search autoquant total 92. leftover12 + leftover12b." [note]
**Numbers.** agent count: 135 agents (post); claimed Sharpe: 1.32 ratio (post)
**Recipe.** —
**Techniques.** [autoresearch-loop](../../techniques/autoresearch-loop.md), [autoresearch-loop](../../techniques/autoresearch-loop.md)
**Tools.** [hyperspace](../../tools/hyperspace.md)
**Links.** product (https://agents.hyper.space/)
**Related items.** [x-2032671842230501729](../x-2032671842230501729/card.md), [x-2080856252687745093](../x-2080856252687745093/card.md), [x-2074912810803560497](../x-2074912810803560497/card.md), [x-2087151807965401320](../x-2087151807965401320/card.md)
**Media.**
`raw/items/x-2032330665081839791/media/media_0.jpg` (image, carries_technique=true) — ASCII infographic: 135 Autoquant agents on a P2P gossip network, Darwinian selection box, and claimed Sharpe 1.32 result card.
**Thread.** captured_partial · reported 79 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
