# Judgment worksheet: landing pages & UI motion (landing-ui-motion)

Owner aliases: landing motion, UI kits, scroll. A design agent should copy a *finished grammar or a kit*, not invent slop. Skills that change how the agent designs live in [design-agent-skills](../design-agent-skills/worksheet.md).

## landing-ui-motion — short stack to try

1. **Scroll grammar, not a vibe.** [nateherk/scroll-craft](../../items/github-nateherkai-scroll-craft/card.md) (eight page grammars + refuse-lists). The Fable 5.1 walkthrough is the field note ([x-2094978216146452971](../../items/x-2094978216146452971/card.md)). The skill promo thread is the claim-source ([x-2093900284896657841](../../items/x-2093900284896657841/card.md)).
2. **Installable kits (shadcn / React).** Cult UI ([web-cult-ui](../../items/web-cult-ui/card.md)), Originkit ([web-originkit-dev](../../items/web-originkit-dev/card.md)), Vengeance UI ([web-vengence-ui](../../items/web-vengence-ui/card.md)), 23rd.dev shader registry ([x-2089740155179643231](../../items/x-2089740155179643231/card.md)). ReactBits Pro is the “restyle 90%” argument ([x-2087812720762425743](../../items/x-2087812720762425743/card.md)), not a captured install.
3. **Finished-page breakdowns to steal structure from.** Blume.codes four effects ([x-2094524951025914278](../../items/x-2094524951025914278/card.md)), scroll-scrubbed 300-frame Gemini + Framer ([x-2094984529853530345](../../items/x-2094984529853530345/card.md)), Cartier Ballon Bleu PDP ([web-cartier-ballon-bleu](../../items/web-cartier-ballon-bleu/card.md)), unive.ai shoutout ([x-2093774183356379560](../../items/x-2093774183356379560/card.md)).
4. **Polish around the page.** TinyShots ([web-tinyshots](../../items/web-tinyshots/card.md)), DiceBear avatars ([web-dicebear](../../items/web-dicebear/card.md)). Flowmapp is agency planning, not motion ([web-flowmapp](../../items/web-flowmapp/card.md)).

AICSS / beautifului.dev cover *agent-chat chrome* (thinking, tools, streaming). Keep them if the landing is an agent product; skip them for a marketing hero.

## landing-ui-motion — axis scores

| item | finished-page vs kit | scroll vs hover/micro | copy-paste cost | shadcn/React | mobile covered |
|---|---|---|---|---|---|
| scroll-craft | grammar (generates a page) | high scroll-timeline | skill install + QA | high (Claude Code) | fixture 390×844 shots exist; no `shoot.mjs` on a `data-sc-act` page |
| Cult UI | kit + agent-pattern gallery | hover / app chrome | npm / registry | high | unknown |
| Originkit | kit (homepage RSC **468** unique gallery slugs; marketing said 363+) | mixed (text, bg, galleries) | MCP hello; `/pricing` Free $0 / Pro $79/yr / Studio $179/yr (metered copies) | React / Next | unknown (no @media in fetched HTML) |
| Vengeance UI | kit (live **46 / 9 families**; registry.json **132** items) | hover + text motion | MIT registry; `/pricing` and `/pro` 404 | high | unknown |
| 23rd.dev | curated registry | shader / animated bg | shadcn add | React + Svelte | unknown |
| ReactBits Pro | kit (paid) | marketing motion | restyle primitives | React | unknown |
| AICSS / beautifului | kit (agent UI) | micro / streaming | copy-paste | React implied | unknown |
| Blume.codes article | finished-page breakdown | seven-layer parallax + scroll-drawn | recipe, not a package | Next / Turborepo | unknown |
| 300-frame scroll-scrub | finished technique | high (300 frames bound to scroll) | ChatGPT + Gemini + Ezgif + Claude | Framer Motion | unknown |
| Cartier PDP | finished reference | luxury product motion | screenshot only | n/a | high (commerce PDP) |
| recent.design / unive.ai / doss.com | reference feed or one page | varies | look, don’t install | n/a | unknown |
| TinyShots | polish tool | n/a | macOS + CLI | n/a | n/a (screenshots) |
| DiceBear | avatar API | n/a | HTTP / SDK | any | n/a |
| Forja / Hogwarts / Brass Hands teasers | example stills or clips | motion implied | not reusable | unknown | unknown |

## landing-ui-motion — claims that need a receipt

- ReactBits Pro does “about 90%” of marketing motion ([x-2087812720762425743](../../items/x-2087812720762425743/card.md)) — author estimate, two-reply thread.
- scroll-craft fingerprint gate — README names the eight grammars and the ≥4-of-6 rule ([scroll-craft](../../tools/scroll-craft.md)). A default-Claude slop fixture (`analysis/_work/captures/default-claude-landing.html`) fires the taste.md refuse list (3-col cards, gradient text, invented stats, AI-purple, em dash, scroll cue, 01/06, dual CTAs) and matches **none** of the eight grammars. Checklist on a fixture, not a headed skill/Playwright run.
- Fable 5.1 “matches Fable 5 landing quality at lower cost” — 149s walkthrough; no side-by-side stills in the card.
- 300-frame Gemini → Framer bind — pipeline named; no public repo of the 300 frames.
- Cult OSS docs: **77** `content/docs/components/*.mdx` including `ai-instructions.mdx`. “92+ AI SDK patterns” still looks Cult Pro, not the OSS count ([cult-ui](../../tools/cult-ui.md)). Homepage fetch 429. Cult Pro `/pricing`: **$129** one-time lifetime (was $179, Summer Sale $50). FAQ: Annual updates = 1 year; Lifetime updates = product lifetime. **aisdkagents.com is a separate product**.
- Originkit homepage RSC **468 unique** `…/components/<slug>-gallery` slugs. Card “363+” is marketing; 363 in the dump was a font hash. MCP `https://mcp.originkit.dev` JSON hello. Public `/registry.json` 404. `/pricing` plan JSON: Free $0/year 3/2/1 daily C/S/T; Pro $79/year (compare-at $108) 10/5/3; Studio $179/year (compare-at $228) 25/10/5. Do not collapse with the integrations-page beta quota.
- Vengeance live site `vengeanceui.com` (not vengence-ui.com): **46 / 9 families**. Registry JSON **132** items — may be more than marketing 46. Install command confirmed on the page. `/pricing` and `/pro` **404**; README MIT. No paid column for a same-copy bake-off.

One X primary is `failed` (see brief thread table). Do not read that silence as “no discussion.”

## landing-ui-motion — do not treat as load-bearing

- Pre-launch teasers and “polish beats paid attention” clips — mood, not a kit ([x-2093364419044794836](../../items/x-2093364419044794836/card.md), [x-2093024468209733756](../../items/x-2093024468209733756/card.md), [x-2095429087141515616](../../items/x-2095429087141515616/card.md)).
- ViscousRealm controller-rooms — 80 Level feature, Blender illustration, not a web kit.
- Flowmapp — sitemap/estimate SaaS; put it in planning, not motion.
- Secondary skill packs (Impeccable, Taste, Emil, MengTo) — judge those on the design-agent-skills worksheet.
- Secondary 3D pages (FeralUI, ORYZO, Utsubo) — web-3d-scenes.

## landing-ui-motion — next capture work

1. Default-Claude fixture scored against taste.md + all eight uniqueness.md grammars — [scroll-craft](../../tools/scroll-craft.md). Impeccable `--viewport 390x844`: **20** findings. Headed Chrome shots at 390×844: Inter, h1 **83.2px**, hero **1012.8px** vs 844 vh (`analysis/_work/captures/claude-landing-mobile/`). Remaining: `shoot.mjs` on a real `data-sc-act` build (this fixture has none).
2. Pricing receipts are on [cult-ui](../../tools/cult-ui.md) (Cult Pro $129 lifetime; Originkit Free/Pro/Studio yearly; Vengeance no `/pricing`). Remaining: same-copy hero + pricing HTML from all three and a mobile breakpoint log. Vengeance has no paid pricing column.
3. Blume homepage first-party copy is on [blume-sidecar](../../tools/blume-sidecar.md). X article `2094493136743473152` still unfetched (jina 403). Card `x-2094524951025914278` gap is `thread-partial`, not `linked-page-unfetched`.
4. Re-fetch the failed landing-ui-motion thread listed in the brief.
