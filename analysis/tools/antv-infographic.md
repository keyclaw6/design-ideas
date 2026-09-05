# Antv Infographic

**Slug:** `antv-infographic` · **Kind:** repo · **URL:** https://github.com/antvis/infographic · **Canonical item:** [github-antvis-infographic](../items/github-antvis-infographic/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md), [infographics-diagrams](../subjects/infographics-diagrams/brief.md)
**Referenced by (1):**
- [AntV Infographic: AI-tuned SVG infographic framework with agent skills](../items/github-antvis-infographic/card.md) — tool, reference — infographics-diagrams

<!-- NOTES:START -->
**2026-09-04 capture — templates vs README ~200.** Clone `antvis/infographic`. README: “~200 built-in infographic templates, data-item components, and layouts” — bundled phrase, not a template-id count. `src/templates/built-in.ts` builds `BUILT_IN_TEMPLATES` then `Object.entries(...).forEach(registerTemplate)`. Inline object keys: **93**. Spread-in records: chart-pie 6, compare-quadrant 3, hierarchy-tree 5, hierarchy-mindmap 10 (`createTemplate` names), sequence-stairs 3, word-cloud 2, list-zigzag 4, relation-dagre-flow 5, sequence-interaction 4, hierarchy-structure 2. Sum of those named templates: **137**. Do not collapse 137 with “~200”.

**Skills.** Five skill folders: `infographic-creator`, `infographic-item-creator`, `infographic-structure-creator`, `infographic-syntax-creator`, `infographic-template-updater`.

**SVG export sample.** Repo fixture `__tests__/unit/ssr/output/01-basic-list.svg` (4,981 bytes): SVG + `foreignObject` XHTML spans. Fills are hardcoded hex (`#262626`, `#5a5a5a`, `#1783ff`, `#00c9c9`, `#f0884d`) — not CSS variables. Tokens are editable in the template/syntax layer, not as `:root` custom properties on the exported SVG. Live gallery `https://infographic.antv.vision/gallery` HTTP 200 (382,873 bytes) this pass.

**2026-09-05 leftover27.** Unused `infographic.antv.vision` **79,156 B** names AntV Infographic **v0.2.20**. Unused `/gallery` **382,873 B** is a client bundle — visible extract has no template count. Receipt `leftover27-2026-09-05.json`.
<!-- NOTES:END -->
