# LangChain managed deep agent folder architecture (MDA)

`x-2088345102540587356` · x · article · en · [source](https://x.com/caspar_br/status/2088345102540587356) · [raw](../../../raw/items/x-2088345102540587356/)
**Author:** Caspar (@caspar_br) (@@caspar_br) · **Published:** — · **Captured:** 2026-09-04T06:49:30Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** [mcp-and-agent-browsers](../../subjects/mcp-and-agent-browsers/brief.md) · **Roles:** reference, technique · **Platforms:** mcp, other

**Summary.** Caspar shares LangChain's managed deep agent diagram: an agent is a folder with instructions, skills, memory, tools, MCP connectors, middleware, sandbox, identity, channels, schedules, and evals. CLI flow is mda init, mda dev, mda deploy to LangSmith.
**Question it answers.** How should an agent repo map skills, MCP connectors, memory, and evals for deployment?

**Claims.**
- `x-2088345102540587356#c1` (recipe, stated) MDA maps agent features to a folder tree including skills/, connectors/, and evals/. — evidence: "anatomy of a managed deep agent. https://langch.in/mda" [post]
- `x-2088345102540587356#c2` (capability, demonstrated) langch.in/mda 200 / 890,993 B. Title Managed Deep Agents - Docs by LangChain. First-party: MDA is the simplest way to build and deploy production agents; example agent is a project folder (Model & configuration, Instructions, Skills, Tools, Middleware, MCP). Matches a hosted deep-agent folder architecture, not a local loop library. — evidence: "GET 200 https://langch.in/mda 890993 B." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [agent-harness-ops](../../techniques/agent-harness-ops.md), [agent-harness-ops](../../techniques/agent-harness-ops.md)
**Tools.** —
**Links.** https://langch.in/mda
**Related items.** [github-punkpeye-awesome-mcp-servers](../github-punkpeye-awesome-mcp-servers/card.md), [web-davidgasquez-context-engineering](../web-davidgasquez-context-engineering/card.md), [x-2087026930323247306](../x-2087026930323247306/card.md), [github-emilkowalski-skills](../github-emilkowalski-skills/card.md), [web-blume-codes](../web-blume-codes/card.md)
**Media.**
`raw/items/x-2088345102540587356/media/media_0.jpg` (image, carries_technique=true) — Infographic titled Your agent is a folder mapping instructions, skills, memory, tools, MCP connectors, and evals to files.
**Thread.** captured_partial · reported 34 · captured 3 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
