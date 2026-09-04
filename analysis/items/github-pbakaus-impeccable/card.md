# Impeccable: agent design skill with PRODUCT.md, detectors, and 23 slash commands

`github-pbakaus-impeccable` · github · repo · en · [source](https://github.com/pbakaus/impeccable) · [raw](../../../raw/items/github-pbakaus-impeccable/)
**Author:** Paul Bakaus (@pbakaus) · **Published:** — · **Captured:** 2026-09-02T17:15:42Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Also:** [landing-ui-motion](../../subjects/landing-ui-motion/brief.md) · **Roles:** tool, technique · **Platforms:** cursor, cli, browser

**Summary.** GitHub repo (~65k stars) shipping one design skill, 23 slash commands, live browser iteration, and 61 deterministic anti-slop detector rules. Evolved from Anthropic frontend-design; init writes PRODUCT.md separately from DESIGN.md.
**Question it answers.** How do I install Impeccable to split PRODUCT.md from DESIGN.md and run deterministic slop audits?

**Claims.**
- `github-pbakaus-impeccable#c1` (recipe, stated) Install via npx impeccable install then /impeccable init writes PRODUCT.md for audience and voice apart from DESIGN.md visual direction. — evidence: "Install: `npx impeccable install`, then `/impeccable init`." [linked-page]
- `github-pbakaus-impeccable#c2` (capability, stated) 61 deterministic detector rules flag Inter-everywhere, purple-blue gradients, and card-in-card patterns without calling an LLM. — evidence: "Design guidance for AI coding agents: 1 skill, 23 slash commands, live browser iteration, 61 deterministic detector rules." [linked-page]
- `github-pbakaus-impeccable#c3` (result, demonstrated) npx impeccable detect against https://example.com returned exit 0 with three findings: line-length and low-contrast twice. — evidence: "detect https://example.com --json: line-length ~96 chars/line; low-contrast 1.1:1 on Example Domain and body; exit 0" [note]
- `github-pbakaus-impeccable#c4` (result, demonstrated) npx impeccable detect --viewport 390x844 on a default-Claude fixture + blume.codes + frontal.so exited 2 with 20 / 85 / 138 findings. Do not collapse with the earlier desktop URL pass. — evidence: "390x844: fixture 20 (18 warning / 2 advisory numbered-section-labels); blume 85 including content-hidden-at-rest error 70% 2095/2989; frontal 138 with undersized-ui-text x72." [note]
**Numbers.** GitHub stars: 64933  (note); slash commands: 23  (note); detector rules: 61  (note)
**Recipe.** —
**Techniques.** [design-md-contract](../../techniques/design-md-contract.md), [anti-slop-ui-skills](../../techniques/anti-slop-ui-skills.md), [screenshot-verify-loop](../../techniques/screenshot-verify-loop.md)
**Tools.** [impeccable](../../tools/impeccable.md)
**Links.** repo (https://github.com/pbakaus/impeccable), product (https://impeccable.style), https://github.com/anthropics/skills/tree/main/skills/frontend-design
**Related items.** [github-google-labs-code-design-md](../github-google-labs-code-design-md/card.md), [github-emilkowalski-skills](../github-emilkowalski-skills/card.md), [github-leonxlnx-taste-skill](../github-leonxlnx-taste-skill/card.md), [github-nateherkai-scroll-craft](../github-nateherkai-scroll-craft/card.md), [web-checklist-design](../web-checklist-design/card.md)
**Media.**
`raw/items/github-pbakaus-impeccable/media/favicon.ico` (other, carries_technique=false) — Site favicon asset bundled with the GitHub capture.
**Judge hints.** must_read: False · compare with: —
