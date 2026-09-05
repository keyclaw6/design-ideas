# Judgment worksheet: design skills & DESIGN.md (design-agent-skills)

Owner aliases: DESIGN.md, taste skill, anti-slop. The question is which packs *change agent output on a real page*, versus prompt galleries and component kits.

## design-agent-skills — short stack to try

Five jobs. Do not install all 50 primaries.

1. **Checkable anti-slop on UI.** [Impeccable](../../items/github-pbakaus-impeccable/card.md) (PRODUCT.md + 61 detectors + 23 slash commands). [Taste Skill](../../items/github-leonxlnx-taste-skill/card.md) and the Spanish promo ([x-2094069236524061059](../../items/x-2094069236524061059/card.md)). [Emil Kowalski skills](../../items/github-emilkowalski-skills/card.md) for motion craft; [/animate-expo](../../items/x-2090031918523842766/card.md) if the surface is React Native. [interfaces.dev better-*](../../items/github-jakubkrehel-skills/card.md) for review passes (UI, type, color, a11y).
2. **DESIGN.md as a contract.** Spec + lint CLI ([github-google-labs-code-design-md](../../items/github-google-labs-code-design-md/card.md)). Catalogs: getdesign.md ([web-getdesign-md](../../items/web-getdesign-md/card.md)), Refero 2000+ ([web-styles-refero-design](../../items/web-styles-refero-design/card.md)). Extractors: Sokosumi ([web-sokosumi-design-md](../../items/web-sokosumi-design-md/card.md)), Hyperbrowser ([web-design-md-hyperbrowser](../../items/web-design-md-hyperbrowser/card.md)). Neuform exports a remixable DESIGN.md after a prompt-to-HTML pass ([web-neuform-ai](../../items/web-neuform-ai/card.md)).
3. **Taste encoding (write your own).** Opale essay ([web-opale-ui-taste](../../items/web-opale-ui-taste/card.md)). MengTo capture-to-prompt ([github-mengto-skills](../../items/github-mengto-skills/card.md)). Chinese field shortlist after trials: Impeccable, Emil, transitions.dev, GSAP skills ([x-2086715093707063445](../../items/x-2086715093707063445/card.md) — four URLs live; `translation-needed` dropped).
4. **In-repo visual loop.** AIDesigner MCP (21 tools) ([web-aidesigner-mcp](../../items/web-aidesigner-mcp/card.md)). OpenDesign local workspace ([github-nexu-io-open-design](../../items/github-nexu-io-open-design/card.md)). Orca on-page annotate ([x-2087708050002239702](../../items/x-2087708050002239702/card.md)). /human-review local editor ([x-2085006701984698712](../../items/x-2085006701984698712/card.md)).
5. **Prose anti-slop (not pixels).** Google developer-docs voice ([x-2087346803268260043](../../items/x-2087346803268260043/card.md), [x-2089457435459404093](../../items/x-2089457435459404093/card.md) — style guide live **79,827 B**), avoid-ai-writing CLI ([x-2092656414351118647](../../items/x-2092656414351118647/card.md)), Hassid pack ([x-2093654908322951447](../../items/x-2093654908322951447/card.md)), /bro ([x-2086845465140842638](../../items/x-2086845465140842638/card.md) — MIT **329★**).

Prompt libraries (SceneAI, motionsites — tweet **590+**, homepage has **no 590** integer) are *dumps*. Use them after a contract exists, not instead of one.

## design-agent-skills — axis scores

| item | installable vs dump | DESIGN.md / contract | anti-slop checkable | visual verify loop | changes a real page |
|---|---|---|---|---|---|
| Impeccable | installable (`npx impeccable`) | PRODUCT.md + DESIGN.md split | high (61 detectors named) | live browser iteration stated | stated; no A/B in this bank |
| Taste Skill | installable MIT repo (**84,364★**; **13** skill dirs) | none required | mid (layout/type/motion rules) | unknown | endorsed; no page log |
| Emil skills | installable MIT (**35,418★**; **12** skill dirs; `/animate-expo` is one of twelve) | none | mid (animation craft) | unknown | unknown |
| interfaces.dev better-* | installable | none | mid (review skills) | review, not generate | unknown |
| Google DESIGN.md | spec + CLI | high (the spec) | lint/diff, not taste | n/a | only if the agent reads it |
| getdesign.md / Refero | catalogs | high (other people’s files) | low (you inherit their tokens) | n/a | mid (paste a file in) |
| Sokosumi / Hyperbrowser | extractors | high (emit DESIGN.md) | low | remote browser stated | mid (clone tokens) |
| Neuform | hosted builder | exports DESIGN.md (meta) | low | hosted preview | live **6,499 B** SPA; no template names in HTML |
| MengTo skills | installable | none | mid (capture→prompt) | video/HTML loop stated | unknown |
| Opale essay | essay | “write your own SKILL.md” | n/a | n/a | method, not a pack |
| AIDesigner MCP | remote MCP | brand-kit tools stated | low | in-editor sessions | stated clone of live HTML/CSS |
| OpenDesign | local app | skills composable | unknown | desktop canvas | unknown (product site + repo) |
| Orca / /human-review | annotate / local editor (human-review MIT **1,228★**) | none | n/a | high (spatial / visual) | mid (human in the loop) |
| SceneAI / motionsites | dump (motionsites.ai **56,054 B**; **590 absent**; MCP live) | none | low | preview pages | low (prompt paste) |
| /unlazy + ponytail | installable | none | mid | unknown | one field report |
| Aura.build | hosted builder | none captured | unknown | hosted | live **7,737 B** SPA; meta **189,000** users + HTML/Figma |
| Fable 5.1 praise tweet | model, not a skill | n/a | n/a | n/a | one-shot claim, no repo |

## design-agent-skills — claims that need a receipt

- Impeccable 61 detectors and 23 slash commands — **README lead confirms the counts**. `crates/live/assets/antipatterns.json` is **exactly 61 ids** (listed on [impeccable](../../tools/impeccable.md)). A local slop HTML run fired `gradient-text`, `low-contrast`, `dark-glow`, `bounce-easing`, `ai-color-palette`, `marketing-buzzword` (9 findings, exit 0 — advisory/fail split means detect is not “exit 2”). Live URL: example.com (3 findings); **blume.codes** (`nested-cards`, `content-hidden-at-rest` 72% / 2512 of 3476 chars); **frontal.so** (`undersized-ui-text` 8.5px). **Mobile `--viewport 390x844`** on fixture + blume + frontal: **20 / 85 / 138** findings, exit 2. Blume hidden-text on mobile is **70%** (2095/2989). GitHub `skill-v4.1.0` (2026-08-14) matches the 4.1 tweet; latest skill on 2026-09-04 is **4.2.0** (do not collapse).
- Chinese “keep four after trials” — practitioner shortlist, 3 replies / 1 captured; transitions.dev is not a primary here.
- /unlazy “works well with Opus 5 + ponytail” — one user ([x-2088742864310481025](../../items/x-2088742864310481025/card.md)). Repo is MIT **3,055★**; Depth Tree anti-laziness skill, not a design-system pack ([unlazy](../../tools/unlazy.md)).
- AIDesigner “21 MCP tools” and live-site clone — marketing page lists **22** snake_case titles under a “Twenty-one tools” heading; unauthed MCP `initialize` is 401. Names on [aidesigner-mcp](../../tools/aidesigner-mcp.md).
- Refero / getdesign.md “550+” / “2000+” — getdesign sitemap union **627** brand slugs (homepage shows 76; `awesome-design-md` tree 147 folders). Refero public API **1,289** style ids / **1,241** siteNames, not 2,000. Same recount is now on leftover card [x-2091934379648110784#c2](../../items/x-2091934379648110784/card.md) as well as the must-read card. Linear detail `GET /api/styles/90ce5883-…` is **81,180** bytes of `fullResult.designSystem` (16 colors, 12 components, Agent Prompt Guide) — **not** a `.md` file. See [getdesign-md](../../tools/getdesign-md.md) and [styles-refero-design](../../tools/styles-refero-design.md).
- Tran Mau nine DESIGN.md hosts ([x-2095078647652917329#c3](../../items/x-2095078647652917329/card.md)): getdesign.md **193,240 B** still markets **550+**; neuform **6,499 B** SPA; aura **7,737 B** SPA; sokosumi generator **109,208 B**; open-design.ai **339,680 B**. designmd.me / designmd.supply / typeui.sh still **429** — do not hammer.
- Fable 5.1 coffee-hero t.co `8yqOGQgCZU` ([x-2095482056180638142#c2](../../items/x-2095482056180638142/card.md)) resolves to **jiro.build** (**1,255,876 B**): **1,147+** templates / **270+** vibe coders. Strings LAOUNGE / Fable / coffee / scroll-scrub are **absent**. Not the tweet prompt body.
- Fable 5.1 “best one-shot website” ([x-2095549461737111905](../../items/x-2095549461737111905/card.md)) — ranking language in the source; do not echo it as a finding. leftover12 “original reference” t.co is MotionSites `?prompt=vectrus-energy` (**56,115 B**), not a Fable skill. `fable.ai` is still a Spaceship listing at **$1,500,000** ([fable](../../tools/fable.md); [x-2095549461737111905#c3](../../items/x-2095549461737111905/card.md)).
- designmd.me / designmd.supply / typeui.sh — capture blocked (Vercel 429). Treat as missing, not as products.

`x-2093669411685110141` is `failed`. The linked index https://designengineer.tools/ **is live**: **20** H2s (Inspiration … Emoji) and **128** unique external hrefs this pass (prior count 129 — do not collapse). Still a bookmark list, not a DESIGN.md pack ([getdesign-md](../../tools/getdesign-md.md)). Do not treat empty X replies as “no discussion.”

## design-agent-skills — do not treat as load-bearing

- Aura.build — live **7,737 B** SPA shell; **189,000** users is meta-only; no generated HTML in-repo.
- skills.sh “top 10 anti-slop” list ([x-2090834948332655011](../../items/x-2090834948332655011/card.md)) — community ranking, not a bake-off.
- Matt Pocock 25-skill tour — harness-adjacent; only the design-relevant subset belongs here. Live repo this pass is **5** dirs / **250,614★** (leftover12 was **250,588★**), not a “25 skills” inventory (parked on [taste-skill](../../tools/taste-skill.md)). leftover12 `/improve-codebase-architecture` page is a survey report, not a design pack ([x-2086838432102228008#c2](../../items/x-2086838432102228008/card.md)). leftover14: productivity/ has grill-me / grilling / handoff; **wayfinder** and **ask-matt** are **404**. Neighbor `DietrichGebert/ponytail` MIT **126,322★**. Custom Pi `/handoff` at 100k does **not** collapse with the Pocock handoff skill ([x-2087263510090874911#c3](../../items/x-2087263510090874911/card.md)). Google-dev-docs leftover now points at the same **79,827 B** style guide ([x-2087346803268260043#c3](../../items/x-2087346803268260043/card.md)).
- claude-skills.free is an email/code gate plus `/grill-me`; skill list needs JS ([claude-skills-free](../../tools/claude-skills-free.md)).
- NameThatUI live **80** H3s / **602,668 B** — visual dictionary, not a DESIGN.md pack ([name-that-ui](../../tools/name-that-ui.md)).
- Agentation vs Agentic UI: Agentation is annotate-to-agent (`npm`); Agentic UI is a Figma system + showcase (parked on [agentation](../../tools/agentation.md)). Do not collapse.
- pdfcn — PDF kit, not a design skill. Live `www.pdfcn.dev` **134,148 B**; repo MIT **993★** ([shadcn-component-kit](../../techniques/shadcn-component-kit.md)).
- Component libraries (Cult, Originkit, Vengeance) — landing-ui-motion.
- Image prompt galleries — image-prompt-galleries.

## design-agent-skills — next capture work

1. 61-id list + desktop URL detects + **mobile 390x844** (fixture 20 / blume 85 / frontal 138) are on [impeccable](../../tools/impeccable.md). Official **two-URL** path (`waitUntil: load`): stock npx nateherk+example **15** findings (12+3), exit 2. **skill-v4.2.0** (2026-09-04) is on the 4.1 must-read card `#c5` so it is not collapsed. Remaining: do not treat 4.2.0 as the 4.1 install notes.
2. Refero public API re-count 2026-09-05 is still **1,289** ids / **1,241** siteNames (must-read `#c4` and leftover [x-2091934379648110784#c2](../../items/x-2091934379648110784/card.md)). Linear / Notion / Stripe records stay JSON `designSystem` blobs, not DESIGN.md ([styles-refero-design](../../tools/styles-refero-design.md)). Remaining: a keyed Hyperbrowser extract of the same two URLs.
3. AIDesigner names are on the marketing page (**22** titles vs “Twenty-one tools”). Docs `/docs/mcp` now first-party (**202,792 B**): same **22** tools; OAuth for MCP; `generate_design`/`refine_design` **30 / 60s**; **4** concurrent; hosts Claude Code / Codex / Cursor / VS Code project + Windsurf user-scope. npm `@aidesigner/agent-skills` **0.1.4** UNLICENSED ([aidesigner-mcp](../../tools/aidesigner-mcp.md); leftover promo [x-2094467179320119498#c3](../../items/x-2094467179320119498/card.md)). Unauthed `initialize` still **401**. Remaining: an authed `tools/list`.
4. leftover18 re-count: designmd.me **429 / 32,188 B** and designmd.supply **429 / 32,184 B** (Vercel Checkpoint) are now on the stub cards — do not hammer ([web-designmd-me#c2](../../items/web-designmd-me/card.md), [web-designmd-supply#c3](../../items/web-designmd-supply/card.md)). Neighbor **designmd.app** this receipt **75,632 B / 562** files; `/library` title says **561**; sitemap-0.xml is **198** locs (**74** library slugs, **35** brand slugs). Do not collapse 562 with getdesign **550+** / sitemap **627**. Originkit MCP hello: **4** tools, registry **461** (not the 468 RSC slugs). Failed thread `x-2093669411685110141` still needs a logged-in harvest.
5. OpenDesign GitHub **94,085** stars / Apache-2.0; README 277 vs 0.8.0 **261** plugins — do not collapse ([open-design](../../tools/open-design.md)). Product site 200. Card is now `ready`.
6. `/have-some-range` leftover has no matching skill repo: t.co loops to the same X video; leftover7 GitHub search returned **485** unrelated hits ([have-some-range](../../tools/have-some-range.md); [x-2091865940581638285#c3](../../items/x-2091865940581638285/card.md)).
7. Orca leftover: `www.orca.build` **2,963 B** empty title; apex handshake timed out — do not retry ([orca](../../tools/orca.md); [x-2087708050002239702#c2](../../items/x-2087708050002239702/card.md)).
