# Harness canvas worker draws architecture diagrams in chat

`x-2088590355440476343` · x · thread · en · [source](https://x.com/mfpiccolo/status/2088590355440476343) · [raw](../../../raw/items/x-2088590355440476343/)
**Author:** @mfpiccolo (@mfpiccolo) · **Published:** — · **Captured:** 2026-09-04T07:07:49Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [infographics-diagrams](../../subjects/infographics-diagrams/brief.md) · **Also:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Roles:** technique, example · **Platforms:** cursor

**Summary.** @mfpiccolo had the coding harness build a canvas worker so agents draw architecture diagrams directly in chat and via a console-injectable UI instead of screenshotting from external diagramming tools.
**Question it answers.** How can a coding harness render architecture diagrams in-chat without external screenshot paste?

**Claims.**
- `x-2088590355440476343#c1` (recipe, stated) Author built a harness canvas worker so the agent draws diagrams in chat rather than pasting screenshots. — evidence: "I asked my harness to build itself a canvas worker. Now the agent draws the diagram right in the chat" [post]
- `x-2088590355440476343#c2` (capability, stated) The worker also exposes a console-injectable UI for viewing the rendered diagram outside the transcript. — evidence: "console injectable UI" [post]
- `x-2088590355440476343#c3` (counter-claim, demonstrated) Reply t.co/abPVj6fHns resolves to hqflow.vercel.app 200 / 15,455 B. Visible: npx hqflow init / open / validate; local-first .codehq/ contract; no LLM inside. First-party repo WinterArc21/HQFlow MIT, 21★ / 1 fork, homepage hqflow.vercel.app. This is a neighbor OSS workflow canvas, not the author’s in-chat canvas worker. Do not collapse. — evidence: "hqflow.vercel.app 15455 B; WinterArc21/HQFlow MIT 21★ leftover13 + leftover13b." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [agent-harness-ops](../../techniques/agent-harness-ops.md)
**Tools.** —
**Links.** product (https://hqflow.vercel.app/)
**Related items.** [x-2088016749849682120](../x-2088016749849682120/card.md), [github-cathrynlavery-diagram-design](../github-cathrynlavery-diagram-design/card.md), [x-2087329201451855933](../x-2087329201451855933/card.md)
**Media.**
`raw/items/x-2088590355440476343/media/media_0.jpg` (video, carries_technique=false) — Attached demo video showing the harness canvas worker rendering an architecture diagram inside the chat UI.
**Thread.** captured_partial · reported 4 · captured 3 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
