# Greg Mushen production agent stack: Hermes, skills, CLIs, telemetry

`x-2093437790969385283` · x · opinion · en · [source](https://x.com/gregmushen/status/2093437790969385283) · [raw](../../../raw/items/x-2093437790969385283/)
**Author:** Greg Mushen (@gregmushen) · **Published:** — · **Captured:** 2026-09-04T07:36:46Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** technique, reference · **Platforms:** cli, mcp

**Summary.** Architecture note separating Hermes judgment layer, slim procedural skills, deterministic CLIs, and closed-loop telemetry for token spend, breakage detection, and agent self-repair on mission-critical workloads.
**Question it answers.** How should production agents split judgment, skills, tools, and telemetry?

**Claims.**
- `x-2093437790969385283#c1` (recipe, stated) Hermes owns judgment, objectives, and timing while skills hold procedural knowledge and CLIs provide deterministic tools. — evidence: "Hermes - owns judgement, objectives, timing, etc.
Skills - procedural knowledge, not code. Still very slim
CLIs - tools for the agents that are deterministic" [post]
- `x-2093437790969385283#c2` (capability, stated) Mission-critical deployments need telemetry on breakage, token spend, and which agent changed what, fed back to the agent. — evidence: "If you're running mission critical stuff, you need to be able to determine:

- Are things breaking?
- What's token spend?
- Which agent made that change and when?" [post]
- `x-2093437790969385283#c3` (counter-claim, demonstrated) Do not collapse Greg Mushen’s Hermes judgment-layer name with NousResearch/hermes-agent. That repo is MIT, 241,533★ (leftover7), homepage https://hermes-agent.nousresearch.com/ 200 / 90,409 B: “The Agent That Grows With You”, Hermes Agent v0.21.0, install.sh, desktop apps for macOS/Windows/Linux. Mushen’s post is an architecture split (judgment / slim skills / deterministic CLIs / telemetry), not that product. — evidence: "leftover7 hermes-nous MIT 241533★ homepage hermes-agent.nousresearch.com; leftover9 homepage 90409 B title Hermes Agent — Open-Source AI Agent That Grows With You v0.21.0." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [agent-harness-ops](../../techniques/agent-harness-ops.md), [session-hardening](../../techniques/session-hardening.md)
**Tools.** [hermes](../../tools/hermes.md)
**Links.** —
**Related items.** —
**Media.**
`raw/items/x-2093437790969385283/media/media_0.jpg` (image, carries_technique=true) — Architecture diagram: human chat surface, Hermes judgment layer, Grafana-fed detection pipeline, slim skills invoking CLIs, and telemetry loop back to observability.
**Thread.** captured_partial · reported 24 · captured 3 · relevant 2 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [x-2091990178638496195](../x-2091990178638496195/card.md), [web-blume-codes](../web-blume-codes/card.md), [x-2087263510090874911](../x-2087263510090874911/card.md)
