# Judgment worksheet: design skills & DESIGN.md (design-agent-skills)

Owner aliases: DESIGN.md, taste skill, anti-slop. The question is which packs *change agent output on a real page*, versus prompt galleries and component kits.

## design-agent-skills — short stack to try

Five jobs. Do not install all 50 primaries.

1. **Checkable anti-slop on UI.** [Impeccable](../../items/github-pbakaus-impeccable/card.md) (PRODUCT.md + 61 detectors + 23 slash commands). [Taste Skill](../../items/github-leonxlnx-taste-skill/card.md) and the Spanish promo ([x-2094069236524061059](../../items/x-2094069236524061059/card.md)). [Emil Kowalski skills](../../items/github-emilkowalski-skills/card.md) for motion craft; [/animate-expo](../../items/x-2090031918523842766/card.md) if the surface is React Native. [interfaces.dev better-*](../../items/github-jakubkrehel-skills/card.md) for review passes (UI, type, color, a11y).
2. **DESIGN.md as a contract.** Spec + lint CLI ([github-google-labs-code-design-md](../../items/github-google-labs-code-design-md/card.md)). Catalogs: getdesign.md ([web-getdesign-md](../../items/web-getdesign-md/card.md)), Refero 2000+ ([web-styles-refero-design](../../items/web-styles-refero-design/card.md)). Extractors: Sokosumi ([web-sokosumi-design-md](../../items/web-sokosumi-design-md/card.md)), Hyperbrowser ([web-design-md-hyperbrowser](../../items/web-design-md-hyperbrowser/card.md)). Neuform exports a remixable DESIGN.md after a prompt-to-HTML pass ([web-neuform-ai](../../items/web-neuform-ai/card.md)).
3. **Taste encoding (write your own).** Opale essay ([web-opale-ui-taste](../../items/web-opale-ui-taste/card.md)). MengTo capture-to-prompt ([github-mengto-skills](../../items/github-mengto-skills/card.md)). Chinese field shortlist after trials: Impeccable, Emil, transitions.dev ([x-2086715093707063445](../../items/x-2086715093707063445/card.md)).
4. **In-repo visual loop.** AIDesigner MCP (21 tools) ([web-aidesigner-mcp](../../items/web-aidesigner-mcp/card.md)). OpenDesign local workspace ([github-nexu-io-open-design](../../items/github-nexu-io-open-design/card.md)). Orca on-page annotate ([x-2087708050002239702](../../items/x-2087708050002239702/card.md)). /human-review local editor ([x-2085006701984698712](../../items/x-2085006701984698712/card.md)).
5. **Prose anti-slop (not pixels).** Google developer-docs voice ([x-2087346803268260043](../../items/x-2087346803268260043/card.md), [x-2089457435459404093](../../items/x-2089457435459404093/card.md)), avoid-ai-writing CLI ([x-2092656414351118647](../../items/x-2092656414351118647/card.md)), Hassid pack ([x-2093654908322951447](../../items/x-2093654908322951447/card.md)), /bro ([x-2086845465140842638](../../items/x-2086845465140842638/card.md)).

Prompt libraries (SceneAI, motionsites 590+) are *dumps*. Use them after a contract exists, not instead of one.

## design-agent-skills — axis scores

| item | installable vs dump | DESIGN.md / contract | anti-slop checkable | visual verify loop | changes a real page |
|---|---|---|---|---|---|
| Impeccable | installable (`npx impeccable`) | PRODUCT.md + DESIGN.md split | high (61 detectors named) | live browser iteration stated | stated; no A/B in this bank |
| Taste Skill | installable MIT repo | none required | mid (layout/type/motion rules) | unknown | endorsed; no page log |
| Emil skills | installable | none | mid (animation craft) | unknown | unknown |
| interfaces.dev better-* | installable | none | mid (review skills) | review, not generate | unknown |
| Google DESIGN.md | spec + CLI | high (the spec) | lint/diff, not taste | n/a | only if the agent reads it |
| getdesign.md / Refero | catalogs | high (other people’s files) | low (you inherit their tokens) | n/a | mid (paste a file in) |
| Sokosumi / Hyperbrowser | extractors | high (emit DESIGN.md) | low | remote browser stated | mid (clone tokens) |
| Neuform | hosted builder | exports DESIGN.md | low | hosted preview | mid (HTML out) |
| MengTo skills | installable | none | mid (capture→prompt) | video/HTML loop stated | unknown |
| Opale essay | essay | “write your own SKILL.md” | n/a | n/a | method, not a pack |
| AIDesigner MCP | remote MCP | brand-kit tools stated | low | in-editor sessions | stated clone of live HTML/CSS |
| OpenDesign | local app | skills composable | unknown | desktop canvas | unknown (product site + repo) |
| Orca / /human-review | annotate / local editor | none | n/a | high (spatial / visual) | mid (human in the loop) |
| SceneAI / motionsites | dump | none | low | preview pages | low (prompt paste) |
| /unlazy + ponytail | installable | none | mid | unknown | one field report |
| Aura.build | hosted builder | none captured | unknown | hosted | capture is meta-only |
| Fable 5.1 praise tweet | model, not a skill | n/a | n/a | n/a | one-shot claim, no repo |

## design-agent-skills — claims that need a receipt

- Impeccable 61 detectors and 23 slash commands — **README lead confirms the counts**. `crates/live/assets/antipatterns.json` is **exactly 61 ids** (listed on [impeccable](../../tools/impeccable.md)). A local slop HTML run fired `gradient-text`, `low-contrast`, `dark-glow`, `bounce-easing`, `ai-color-palette`, `marketing-buzzword` (9 findings, exit 0 — advisory/fail split means detect is not “exit 2”). Live URL: example.com (3 findings); **blume.codes** (`nested-cards`, `content-hidden-at-rest` 72% / 2512 of 3476 chars); **frontal.so** (`undersized-ui-text` 8.5px). **Mobile `--viewport 390x844`** on fixture + blume + frontal: **20 / 85 / 138** findings, exit 2. Blume hidden-text on mobile is **70%** (2095/2989). GitHub `skill-v4.1.0` (2026-08-14) matches the 4.1 tweet; latest skill on 2026-09-04 is **4.2.0** (do not collapse).
- Chinese “keep four after trials” — practitioner shortlist, 3 replies / 1 captured; transitions.dev is not a primary here.
- /unlazy “works well with Opus 5 + ponytail” — one user ([x-2088742864310481025](../../items/x-2088742864310481025/card.md)).
- AIDesigner “21 MCP tools” and live-site clone — marketing page lists **22** snake_case titles under a “Twenty-one tools” heading; unauthed MCP `initialize` is 401. Names on [aidesigner-mcp](../../tools/aidesigner-mcp.md).
- Refero / getdesign.md “550+” / “2000+” — getdesign sitemap union **627** brand slugs (homepage shows 76; `awesome-design-md` tree 147 folders). Refero public API **1,289** style ids / **1,241** siteNames, not 2,000. Linear detail `GET /api/styles/90ce5883-…` is **81,180** bytes of `fullResult.designSystem` (16 colors, 12 components, Agent Prompt Guide) — **not** a `.md` file. See [getdesign-md](../../tools/getdesign-md.md) and [styles-refero-design](../../tools/styles-refero-design.md).
- Fable 5.1 “best one-shot website” ([x-2095549461737111905](../../items/x-2095549461737111905/card.md)) — ranking language in the source; do not echo it as a finding.
- designmd.me / designmd.supply / typeui.sh — capture blocked (Vercel 429). Treat as missing, not as products.

`x-2093669411685110141` is `failed`. The linked index https://designengineer.tools/ **is live**: 20 section headings (Inspiration … Emoji) and **129 unique external hrefs** this pass. Still a bookmark list, not a DESIGN.md pack. Do not treat empty X replies as “no discussion.”

## design-agent-skills — do not treat as load-bearing

- Aura.build — meta capture, no generated HTML in-repo.
- skills.sh “top 10 anti-slop” list ([x-2090834948332655011](../../items/x-2090834948332655011/card.md)) — community ranking, not a bake-off.
- Matt Pocock 25-skill tour — harness-adjacent; only the design-relevant subset belongs here.
- pdfcn — PDF kit, not a design skill.
- Component libraries (Cult, Originkit, Vengeance) — landing-ui-motion.
- Image prompt galleries — image-prompt-galleries.

## design-agent-skills — next capture work

1. 61-id list + desktop URL detects + **mobile 390x844** (fixture 20 / blume 85 / frontal 138) are on [impeccable](../../tools/impeccable.md). Single-URL `networkidle0` still times out on nateherk / complete-shelf. Official **two-URL** path (`waitUntil: load`): stock npx nateherk+example **15** findings (12+3), exit 2; local debug **16** (13+3); local complete-shelf+example **35** (32+3). Remaining: do not treat 4.2.0 as the 4.1 card.
2. Refero Linear / Notion / Stripe records are JSON `designSystem` blobs (81,180 / 68,148 / 70,976 B), not DESIGN.md files ([styles-refero-design](../../tools/styles-refero-design.md)). Sokosumi unauthed `POST /api/design-md` works: example.com job **1940** in 43.6 s (12,675 B, `source=llm`); gallery **1,211** llm rows; Linear/Stripe/Notion published YAML have **47** color keys. Same-brand overlap with Refero: Linear surface `#08090a`, Notion `#0075de`, Stripe `#533afd`. Linear CTA diverges (`#e5e5e6` vs Refero `#e4f222`). Hyperbrowser `POST /api/generate` is still **401** ([sokosumi-design-md](../../tools/sokosumi-design-md.md)). Remaining: a keyed Hyperbrowser extract of the same two URLs.
3. AIDesigner names are on the marketing page (**22** titles vs “Twenty-one tools”). Evening re-fetch still 200; unauthed `initialize` is **401** `OAuth access token required` ([aidesigner-mcp](../../tools/aidesigner-mcp.md)). Remaining: an authed `tools/list`.
4. Re-fetch `x-2093669411685110141` and the blocked designmd.me / designmd.supply hosts. Neighbor **designmd.app** homepage says **562** files; `/library` title says **561**; sitemap-0.xml is **198** locs (**74** library slugs, **35** brand slugs). Do not collapse those. Originkit MCP hello: **4** tools, registry **461** (not the 468 RSC slugs).
