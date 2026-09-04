# Impeccable

**Slug:** `impeccable` · **Kind:** repo · **URL:** https://github.com/pbakaus/impeccable · **Canonical item:** [github-pbakaus-impeccable](../items/github-pbakaus-impeccable/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md), [landing-ui-motion](../subjects/landing-ui-motion/brief.md)
**Referenced by (3):**
- [Impeccable: agent design skill with PRODUCT.md, detectors, and 23 slash commands](../items/github-pbakaus-impeccable/card.md) — tool, technique — design-agent-skills
- [Chinese field report: four design skills kept after trials](../items/x-2086715093707063445/card.md) — reference, claim-source — design-agent-skills
- [Impeccable 4.1 release — critique, native review, live mode fixes](../items/x-2088254428730085690/card.md) — tool, reference — design-agent-skills

<!-- NOTES:START -->
Fetched 2026-09-04 README https://github.com/pbakaus/impeccable

README lead: “1 skill, 23 commands, live browser iteration, and 61 deterministic detector rules.” `/impeccable init` writes `PRODUCT.md`; visual system goes in `DESIGN.md`. Detectors run with no LLM/API key (`npx impeccable detect`). Docs: https://impeccable.style/docs/detector — page fetched, does not enumerate all 61 ids in the HTML.

**Ran 2026-09-04** `npx impeccable detect` on a local 15-line slop `index.html` (purple gradient, bounce, glow, “cutting-edge”, 11px button). Exit **0**. Text report: **9 anti-patterns**. Rule ids that fired: `gradient-text` (×2), `low-contrast` (×2, 1.0:1), `dark-glow` (×2), `bounce-easing`, `ai-color-palette`, `marketing-buzzword`. CLI also documents `--json`, `--scope type,layout`, `--viewport WxH`, URL mode via Puppeteer, and advisory findings that never change the exit code. Not a live-site URL pass.

**2026-09-04 capture — 61 detector ids.**
Clone `pbakaus/impeccable`. `crates/live/assets/antipatterns.json` has **exactly 61** objects. Ids: `side-tab`, `border-accent-on-rounded`, `overused-font`, `flat-type-hierarchy`, `gradient-text`, `ai-color-palette`, `cream-palette`, `nested-cards`, `monotonous-spacing`, `bounce-easing`, `pulsing-dot`, `blinking-cursor`, `shape-assembled-illustration`, `organic-clip-path`, `buried-raster`, `dark-glow`, `radial-halo`, `radial-spotlight-glow`, `marquee`, `icon-tile-stack`, `italic-serif-display`, `hero-eyebrow-chip`, `kicker-above-heading`, `numbered-section-labels`, `em-dash-overuse`, `marketing-buzzword`, `aphoristic-cadence`, `oversized-h1`, `extreme-negative-tracking`, `broken-image`, `script-error`, `content-hidden-at-rest`, `edge-flush-cards`, `text-occlusion`, `first-viewport-column-overflow`, `gray-on-color`, `low-contrast`, `layout-transition`, `line-length`, `cramped-padding`, `body-text-viewport-edge`, `tight-leading`, `skipped-heading`, `heading-rhythm`, `justified-text`, `tiny-text`, `undersized-ui-text`, `all-caps-body`, `wide-tracking`, `text-overflow`, `repeated-container-text`, `clipped-overflow-container`, `design-system-font`, `design-system-color`, `design-system-radius`, `design-system-font-size`, `gpt-thin-border-wide-shadow`, `repeating-stripes-gradient`, `codex-grid-background`, `theater-slop-phrase`, `image-hover-transform`.

**2026-09-04 capture — live URL detect.** `npx impeccable detect https://example.com --json`. Exit **0**. Three findings: `line-length` (~96 chars/line), `low-contrast` ×2 (pixel contrast 1.1:1 on “Example Domain” and body copy). URL mode via Puppeteer works on this host. Not a design-system site; only proves the live-URL path.

**2026-09-04 capture — GitHub releases.** `GET https://api.github.com/repos/pbakaus/impeccable/releases`. Tag **`skill-v4.1.0`** published 2026-08-14 matches the tweet: native iOS/Android verify/review; Windows install; live mode on ddev/valet; full-fidelity comps; direction “the roll argues with itself.” Later patches: 4.1.1 / 4.1.2 / 4.1.3. Latest this fetch: **`skill-v4.2.0`** + **`cli-v4.0.0`** + **`ext-v1.4.0`** dated 2026-09-04 (static binary, no Node for the hook; 10.6 ms vs 46.9 ms). Do not treat 4.2 as the 4.1 card’s claim.

**2026-09-04 capture — live detect on real landings** (exit 0 both). `npx impeccable detect https://blume.codes --json`: `nested-cards` (×2+), **`content-hidden-at-rest` error** — 72% of page text (2512/3476 chars) stays opacity 0 after reveal (e.g. “Download”). `npx impeccable detect https://frontal.so --json`: `undersized-ui-text` (8.5px “Score”, “Personalize”, etc.).
<!-- NOTES:END -->
