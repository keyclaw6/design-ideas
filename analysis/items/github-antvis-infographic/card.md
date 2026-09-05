# AntV Infographic: AI-tuned SVG infographic framework with agent skills

`github-antvis-infographic` · github · repo · en · [source](https://github.com/antvis/infographic) · [raw](../../../raw/items/github-antvis-infographic/)
**Author:** antvis (@—) · **Published:** — · **Captured:** 2026-09-02T17:15:42Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [infographics-diagrams](../../subjects/infographics-diagrams/brief.md) · **Also:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Roles:** tool, reference · **Platforms:** mcp, other

**Summary.** AntV Infographic (@antv/infographic) is an open-source framework for generating and editing SVG infographics from compact template strings, with ~200 built-in layouts, themes, a built-in editor, and a skills/ pack for coding agents.
**Question it answers.** How can an agent generate editable SVG infographics from template syntax instead of hand-drawing charts?

**Claims.**
- `github-antvis-infographic#c1` (capability, stated) Infographic ships ~200 built-in templates and AI-tuned syntax that agents emit as compact template strings rendered to editable SVG. — evidence: "Features: AI-tuned config/syntax, ready-to-use templates, hand-drawn/gradient themes, editable SVG renderer." [linked-page]
- `github-antvis-infographic#c2` (benchmark, demonstrated) built-in.ts registers 137 named templates (93 inline keys plus spread-in records); the README ~200 figure bundles templates with data-item components and layouts and is not a template-id count. — evidence: "inline keys 93 + imported records 44 = 137 named templates; README: ~200 built-in infographic templates, data-item components, and layouts" [note]
- `github-antvis-infographic#c3` (availability, demonstrated) leftover27 unused infographic.antv.vision 79,156 B names AntV Infographic v0.2.20 (Build Infographics with Words). /gallery 382,873 B is a large client bundle; the visible-text extract does not list a template count. leftover27 does not walk a saved gallery item or publish a rendered infographic. — evidence: "leftover27 antv-home 79156 B v0.2.20; antv-gallery 382873 B." [note]
**Numbers.** named built-in templates: 137  (note)
**Recipe.** —
**Techniques.** [svg-infographic-rendering](../../techniques/svg-infographic-rendering.md), [svg-infographic-rendering](../../techniques/svg-infographic-rendering.md)
**Tools.** [antv-infographic](../../tools/antv-infographic.md)
**Links.** repo (https://github.com/antvis/infographic), product (https://infographic.antv.vision), https://infographic.antv.vision/gallery, https://infographic.antv.vision/ai, https://infographic.antv.vision
**Related items.** [github-cathrynlavery-diagram-design](../github-cathrynlavery-diagram-design/card.md), [web-flint-chart](../web-flint-chart/card.md)
**Media.**
`raw/items/github-antvis-infographic/media/preview.webp` (image, carries_technique=false) — Wide gallery preview of colorful AntV infographic templates including list, process, and comparison layouts.
**Judge hints.** must_read: True · compare with: [github-cathrynlavery-diagram-design](../github-cathrynlavery-diagram-design/card.md), [web-flint-chart](../web-flint-chart/card.md)
