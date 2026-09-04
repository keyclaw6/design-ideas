# Impeccable

**Slug:** `impeccable` · **Kind:** repo · **URL:** https://github.com/pbakaus/impeccable · **Canonical item:** [github-pbakaus-impeccable](../items/github-pbakaus-impeccable/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md), [landing-ui-motion](../subjects/landing-ui-motion/brief.md)
**Referenced by (2):**
- [Impeccable: agent design skill with PRODUCT.md, detectors, and 23 slash commands](../items/github-pbakaus-impeccable/card.md) — tool, technique — design-agent-skills
- [Chinese field report: four design skills kept after trials](../items/x-2086715093707063445/card.md) — reference, claim-source — design-agent-skills

<!-- NOTES:START -->

Fetched 2026-09-04 README https://github.com/pbakaus/impeccable

README lead: “1 skill, 23 commands, live browser iteration, and 61 deterministic detector rules.” `/impeccable init` writes `PRODUCT.md`; visual system goes in `DESIGN.md`. Detectors run with no LLM/API key (`npx impeccable detect`). Docs: https://impeccable.style/docs/detector — page fetched, does not enumerate all 61 ids in the HTML.

**Ran 2026-09-04** `npx impeccable detect` on a local 15-line slop `index.html` (purple gradient, bounce, glow, “cutting-edge”, 11px button). Exit **0**. Text report: **9 anti-patterns**. Rule ids that fired: `gradient-text` (×2), `low-contrast` (×2, 1.0:1), `dark-glow` (×2), `bounce-easing`, `ai-color-palette`, `marketing-buzzword`. CLI also documents `--json`, `--scope type,layout`, `--viewport WxH`, URL mode via Puppeteer, and advisory findings that never change the exit code. Not a live-site URL pass.

**2026-09-04 capture — 61 detector ids.**
Clone `pbakaus/impeccable`. `crates/live/assets/antipatterns.json` has **exactly 61** objects. Ids: `side-tab`, `border-accent-on-rounded`, `overused-font`, `flat-type-hierarchy`, `gradient-text`, `ai-color-palette`, `cream-palette`, `nested-cards`, `monotonous-spacing`, `bounce-easing`, `pulsing-dot`, `blinking-cursor`, `shape-assembled-illustration`, `organic-clip-path`, `buried-raster`, `dark-glow`, `radial-halo`, `radial-spotlight-glow`, `marquee`, `icon-tile-stack`, `italic-serif-display`, `hero-eyebrow-chip`, `kicker-above-heading`, `numbered-section-labels`, `em-dash-overuse`, `marketing-buzzword`, `aphoristic-cadence`, `oversized-h1`, `extreme-negative-tracking`, `broken-image`, `script-error`, `content-hidden-at-rest`, `edge-flush-cards`, `text-occlusion`, `first-viewport-column-overflow`, `gray-on-color`, `low-contrast`, `layout-transition`, `line-length`, `cramped-padding`, `body-text-viewport-edge`, `tight-leading`, `skipped-heading`, `heading-rhythm`, `justified-text`, `tiny-text`, `undersized-ui-text`, `all-caps-body`, `wide-tracking`, `text-overflow`, `repeated-container-text`, `clipped-overflow-container`, `design-system-font`, `design-system-color`, `design-system-radius`, `design-system-font-size`, `gpt-thin-border-wide-shadow`, `repeating-stripes-gradient`, `codex-grid-background`, `theater-slop-phrase`, `image-hover-transform`.

<!-- NOTES:END -->
