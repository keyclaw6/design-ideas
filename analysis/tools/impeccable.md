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

**2026-09-04 capture — mobile viewport `--viewport 390x844`.** One command, three targets, exit **2**. Do not collapse with the desktop URL pass above.

| target | findings | notes |
|---|---|---|
| fixture `analysis/_work/captures/default-claude-landing.html` | **20** (18 warning / 2 advisory) | `side-tab` ×3; `low-contrast` ×5 (2.8–4.2:1); `gradient-text` ×2; `dark-glow` ×3; `oversized-h1` 83px / 42 chars; `overused-font` Inter; `numbered-section-labels` ×2 **advisory**; `ai-color-palette`; `radial-halo`; `marketing-buzzword` (10× / Supercharge) |
| https://blume.codes | **85** (80 warning / 4 advisory / 1 error) | `undersized-ui-text` ×37 (9–10px); `bounce-easing` ×19; `nested-cards` ×8; `content-hidden-at-rest` **error** now **70%** (2095/2989 chars) vs desktop 72% (2512/3476) |
| https://frontal.so | **138** (135 warning / 3 advisory) | `undersized-ui-text` ×72 (9–10.53px); `nested-cards` ×19; `dark-glow` ×11; `radial-spotlight-glow` ×8; `all-caps-body` ×9 |

CLI help confirms `--viewport WxH` (default 1280x800) and that advisories never change the exit code. Exit 2 = primary findings on at least one target.

**2026-09-04 capture — live detect timeouts.** `npx impeccable detect https://www.nateherk.com/ --json` and `https://mengto.github.io/complete-shelf/ --json` both printed `Error: Navigation timeout of 30000 ms exceeded` then `[]`. Exit **0**. No findings file. These two URLs are not a third landing receipt; they only show the 30 s Puppeteer budget can miss a long first paint (scroll-craft / Three CDN).

**2026-09-04 capture — 90 s local patch still networkidle0 timeout.** Single-URL detect uses `waitUntil: networkidle0` (`crates/browser/src/lib.rs`). Local clone only: `NAVIGATION_TIMEOUT` 30000→90000, `cargo build -p impeccable` debug. `PUPPETEER_DANGEROUS_NO_SANDBOX=true`. Same two URLs: `Error: Navigation timeout of 90000 ms exceeded`, JSON `[]`, exit **1**. Same binary on `https://example.com` still returns **3** findings, exit **2** (do not collapse with earlier npx exit 0). So the miss is `networkidle0` on long-lived connections (fonts / Three CDN), not “these pages have zero slop.” Receipt `analysis/_work/captures/impeccable-90s-timeout.json`. Remaining: a `waitUntil: load` (or headed GPU) pass, not another 30s bump.

**2026-09-04 capture — official multi-URL path uses `waitUntil: load`.** Passing two URLs shares one browser (`SharedBrowserHandle`, `settleMs: 100`). Stock `npx impeccable detect https://www.nateherk.com/ https://example.com --json`: exit **2**, **15** findings (nateherk **12** / example **3**). nateherk rules: `low-contrast` ×8, `dark-glow` ×1, `kicker-above-heading`, `overused-font`, `radial-spotlight-glow`. Local 90s debug binary same pair: exit **2**, **16** findings (nateherk **13** / example **3**) — extra `dark-glow` + `buried-raster`; `low-contrast` ×7. Do not collapse 15/16 or 12/13. Local `detect https://mengto.github.io/complete-shelf/ https://example.com --json`: exit **2**, **35** findings (shelf **32** / example **3**). Shelf rules: `undersized-ui-text` ×11, `dark-glow` ×9, `gpt-thin-border-wide-shadow` ×7 **advisory**, `all-caps-body` ×2, plus `extreme-negative-tracking`, `layout-transition`, `overused-font`. Summary `analysis/_work/captures/impeccable-load-summary.json`.

**2026-09-05 capture — skill-v4.2.0 is later than the 4.1 must-read card.** `GET …/releases/tags/skill-v4.2.0` **200**, published **2026-09-04T20:28:37Z**, name *Skill 4.2.0*. Notes: static binary / no Node; hook **10.6 ms** vs Node **46.9 ms**; CLI **110** files **132 ms** vs **282 ms**; replay **830** commands / **16,058** function calls. Tags also list skill-v4.1.3 / 4.1.2 / 4.1.1 after 4.1.0. Do not treat this card as 4.2.

**2026-09-05 leftover19.** `impeccable.style` **200 / 109,943 B** markets **61** checks / **23** commands / **177** worlds and `npx impeccable install`. Homepage does not name 4.1 vs 4.2.0.

**2026-09-05 leftover21.** `skill-v4.1.0` release JSON published **2026-08-14**. Notes: roll argues with itself; full-fidelity comps; safer/bolder steer. Do not collapse with **4.2.0**.

**2026-09-05 leftover27.** Unused `impeccable.style` **109,943 B** restates **66k+** / **61** / **23** / **177** / `npx impeccable install` / Node **22.12+** — same leftover19 homepage integers, not a new 4.1 inventory. Unused GitHub `skill-v4.2.0` **5,961 B** published **2026-09-04T20:28:37Z** restates leftover05 (static binary; hook **10.6 ms** vs **46.9 ms**; CLI **110** files **132 vs 282 ms**; replay **830** / **16,058**). Do not collapse 4.1 homepage with 4.2.0. Receipt `leftover27-2026-09-05.json`.

**2026-09-05 leftover29.** Unused Anthropic `frontend-design/SKILL.md` **9,390 B** — neighbor aesthetic-direction skill, not the 61 detectors. Receipt `leftover29-2026-09-05.json`.
<!-- NOTES:END -->
