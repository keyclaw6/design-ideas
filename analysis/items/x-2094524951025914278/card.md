# Blume.codes landing page build breakdown (X article)

`x-2094524951025914278` · x · article · en · [source](https://x.com/olavlj/status/2094524951025914278) · [raw](../../../raw/items/x-2094524951025914278/)
**Author:** olav (@olavlj) · **Published:** 2026-08-31T20:37:17Z · **Captured:** 2026-09-02T18:49:18Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [landing-ui-motion](../../subjects/landing-ui-motion/brief.md) · **Also:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Roles:** technique, example · **Platforms:** cursor, codex, other

**Summary.** Olav's X article documents four blume.codes effects: seven-layer Codex parallax hero, Turborepo-shared live product demo, scroll-drawn Dicebear vine, and a six-theme flower picker—framed as attention-budget craft for an agent sidecar landing page.
**Question it answers.** How did Blume build parallax, live demos, and scroll motion on their agent sidecar landing page?

**Claims.**
- `x-2094524951025914278#c1` (recipe, stated) The parallax hero used at least seven Codex-generated alpha layers with faster parallax on nearer layers. — evidence: "Minimum 3 layers; they used **7**." [linked-page]
- `x-2094524951025914278#c2` (capability, stated) The landing page embeds a live mock-data instance of the Electron app via a shared Turborepo UI package. — evidence: "Landing page and Electron app share a **Turborepo** UI package; the site embed is a live mock-data instance of the app." [linked-page]
- `x-2094524951025914278#c3` (recipe, stated) A scroll-drawn vector vine uses daily-seeded Dicebear flower crowns as a hidden easter-egg motif. — evidence: "Scroll-drawn vector path; flower crowns from a custom Dicebear style, seeded by the current date so they change daily." [linked-page]
- `x-2094524951025914278#c4` (recipe, demonstrated) fxtwitter article 2094493136743473152 is 68 blocks / 8,070 chars titled How We Built a Next-Level Landing Page. It names four elements: parallax hero, interactive product screenshots, journey vine, flower theme picker. Minimum 3 parallax layers; they used 7. Codex is preferred because it can code and generate images (Claude Code + fal.ai is the alternative). — evidence: "See you can spot the four elements… You should have a minimum of 3 layers… we ended up with 7 layers. Why Codex? Because Codex can both code and generate images." [note]
- `x-2094524951025914278#c5` (capability, demonstrated) Article: landing page and Electron app share a Turborepo UI package (mock-data embed). Codex ran a week-long /goal refactor to get there. Six flower themes; Dicebear crowns seeded by the current date; theme also settable from settings inside the app demo. Body does not say nearer layers move faster. — evidence: "We have a Turborepo setup… Codex ran a week-long /goal task… One recurring theme in Blume is our 6 flowers… crowns are seeded using the current date." [note]
**Numbers.** parallax layers: 7 layers (linked-page); article views at capture: 46503 views (post); flower themes: 6 themes (linked-page)
**Recipe.** —
**Techniques.** [parallax-scroll-landing](../../techniques/parallax-scroll-landing.md), [shadcn-component-kit](../../techniques/shadcn-component-kit.md), [scroll-driven-3d](../../techniques/scroll-driven-3d.md)
**Tools.** [codex](../../tools/codex.md), [dicebear](../../tools/dicebear.md), [blume](../../tools/blume.md)
**Links.** product (https://blume.codes), https://www.dicebear.com, https://fal.ai
**Related items.** [web-blume-codes](../web-blume-codes/card.md), [github-nateherkai-scroll-craft](../github-nateherkai-scroll-craft/card.md), [web-dicebear](../web-dicebear/card.md), [web-cult-ui](../web-cult-ui/card.md)
**Media.**
`raw/items/x-2094524951025914278/media/article-cover.jpg` (image, carries_technique=false) — Cover art: cream UI card listing three agent rows among orange lilies and a green vine beside All Your Agents, in Focus headline.
`raw/items/x-2094524951025914278/media/article-hero-still.jpg` (image, carries_technique=true) — Blume hero over sunflower field: Download DMG callout plus floating Cursor, Codex, and Claude Code windows above Improve-tab analytics gauges.
`raw/items/x-2094524951025914278/media/article-layers.jpg` (image, carries_technique=true) — Eight tilted cards showing far mountains through mid cliffs to foreground wildflowers, illustrating separate parallax layer plates.
`raw/items/x-2094524951025914278/media/article-reference.jpg` (image, carries_technique=true) — Makoto Shinkai-style reference landscape with sunflowers, orange lilies, roses, and bellflowers under a bright blue cloudy sky.
`raw/items/x-2094524951025914278/media/article-video-interactive-thumb.jpg` (image, carries_technique=false) — Still frame of the interactive product demo video showing Blume Improve tab over the parallax hero background.
`raw/items/x-2094524951025914278/media/article-video-interactive.mp4` (video, carries_technique=true) — 16s demo of the live interactive Blume app embed on the landing page with analytics and suggestion cards.
`raw/items/x-2094524951025914278/media/article-video-theme-thumb.jpg` (image, carries_technique=false) — Still of the theme-picker section showing All Your Agents in Focus beside lily-decorated UI cards and Download DMG button.
`raw/items/x-2094524951025914278/media/article-video-theme.mp4` (video, carries_technique=true) — 19s demo cycling Blume flower themes that regenerate page graphics and agent card styling.
`raw/items/x-2094524951025914278/media/article-video-vine-thumb.jpg` (image, carries_technique=false) — Still of the vine section headline Your journey begins here with Cursor, Claude Code, Codex, and Pi logos.
`raw/items/x-2094524951025914278/media/article-video-vine.mp4` (video, carries_technique=true) — 12s scroll capture of the journey vine section with Works With logos and agent list illustration.
**Thread.** captured_partial · reported 13 · captured 3 · relevant 3 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: [github-nateherkai-scroll-craft](../github-nateherkai-scroll-craft/card.md), [web-blume-codes](../web-blume-codes/card.md), [web-dicebear](../web-dicebear/card.md)
