# Sentrux Rust binary scores codebase architecture for agent sessions

`x-2087239769877295158` · x · product · en · [source](https://x.com/simplifyinAI/status/2087239769877295158) · [raw](../../../raw/items/x-2087239769877295158/)
**Author:** Simplifying AI (@simplifyinAI) · **Published:** — · **Captured:** 2026-09-04T06:49:25Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [agent-memory-knowledge](../../subjects/agent-memory-knowledge/brief.md) · **Also:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Roles:** tool, technique · **Platforms:** cli

**Summary.** Sentrux is a pure-Rust architectural sensor that scans repo structure and dependencies into a live treemap and folds five root-cause metrics into one quality score so agents start from a map instead of blind grep.
**Question it answers.** How can an agent keep a live architecture map between sessions without re-explaining the codebase?

**Claims.**
- `x-2087239769877295158#c1` (capability, stated) Sentrux watches a codebase as a live treemap and compresses structure and dependency risk into one continuous quality score. — evidence: "sentrux is a real-time architectural sensor, it watches your codebase as a live treemap and turns file structure and dependencies into one continuous quality score." [post]
- `x-2087239769877295158#c2` (capability, stated) Language support lives in plugin.toml and tags.scm files so adding a language needs no Rust changes. — evidence: "all 52 languages live in plugin.toml and tags.scm query files, so a new language needs zero rust code." [post]
- `x-2087239769877295158#c3` (capability, demonstrated) sentrux.dev 200 / 16,280 B + GitHub sentrux/sentrux MIT **3,170★** / 280 forks. README first-party: **52 languages** via tree-sitter plugins; `sentrux plugin add-standard` installs all 52; plugin.toml + tags.scm; MCP `--mcp`. Public sentrux/plugins tree this pass has **50** language dirs — do not collapse with README 52. Demo quality integers 7342 / 6772 are marketing on the page. — evidence: "GET sentrux.dev 16280 B; api.github.com/repos/sentrux/sentrux 3170 stars MIT. plugins contents 50 language dirs. leftover4-2026-09-05.json" [note]
**Numbers.** languages via plugins: 52  (post)
**Recipe.** —
**Techniques.** [agent-harness-ops](../../techniques/agent-harness-ops.md)
**Tools.** [sentrux](../../tools/sentrux.md)
**Links.** —
**Related items.** [x-2086838432102228008](../x-2086838432102228008/card.md), [x-2091559663833924082](../x-2091559663833924082/card.md), [github-google-labs-code-design-md](../github-google-labs-code-design-md/card.md), [web-davidgasquez-context-engineering](../web-davidgasquez-context-engineering/card.md)
**Media.** —
**Thread.** captured_partial · reported 5 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [x-2091559663833924082](../x-2091559663833924082/card.md), [web-davidgasquez-context-engineering](../web-davidgasquez-context-engineering/card.md)
