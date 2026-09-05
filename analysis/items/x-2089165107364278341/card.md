# Anthropic agent cost optimization cookbook pointer ($0.29 to 90% less)

`x-2089165107364278341` · x · article · en · [source](https://x.com/dani_avila7/status/2089165107364278341) · [raw](../../../raw/items/x-2089165107364278341/)
**Author:** Daniel San (@dani_avila7) · **Published:** — · **Captured:** 2026-09-04T06:35:40Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** reference · **Platforms:** claude-code

**Summary.** Daniel San highlights Anthropic's cost_optimization.ipynb cookbook where a real agent task drops from about $0.29 to ninety percent less without accuracy loss by tuning prompts, cache, and tools before downgrading models.
**Question it answers.** How does Anthropic's cost optimization cookbook cut agent spend before switching to cheaper models?

**Claims.**
- `x-2089165107364278341#c1` (result, stated) Cookbook example agent cost falls about ninety percent from $0.29 per task without dropping accuracy. — evidence: "A real agent goes from $0.29/task down 90% without dropping accuracy" [post]
- `x-2089165107364278341#c2` (recipe, stated) Model downgrade is the last cost lever, not the first optimization step. — evidence: "And model downgrade is the last lever, not the first" [post]
- `x-2089165107364278341#c3` (benchmark, demonstrated) Raw cost_optimization.ipynb 200 / 1,286,487 B. First-party printed line: 10/10 correct · 36 turns · $0.2906/task · $2.9063 total. Later prose: roughly 90% under the Opus baseline on cost. Tweet $0.29 / 90% maps to those notebook strings; do not collapse $0.2906 with a different task. — evidence: "notebook print: $0.2906/task; prose 90% under Opus baseline." [note]
**Numbers.** example agent cost before optimization: 0.29 USD per task (post); claimed cost reduction: 90 percent (post)
**Recipe.** —
**Techniques.** —
**Tools.** —
**Links.** repo (https://github.com/anthropics/claude-cookbooks/blob/main/cost_optimization/cost_optimization.ipynb)
**Related items.** [web-anthropic-claude-self-service-data](../web-anthropic-claude-self-service-data/card.md)
**Media.** —
**Thread.** captured_partial · reported 19 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
