# Judgment worksheet: image prompt galleries (image-prompt-galleries)

Owner aliases: prompt gallery, nano banana, GPT Image. Website/UI prompts belong in [design-agent-skills](../design-agent-skills/worksheet.md). Video prompts belong in [ai-video-generation](../ai-video-generation/worksheet.md).

## image-prompt-galleries — short stack to try

1. **Prompt-as-code, not a chat paste.** GPT Image 2 skill + CLI ([github-wuyoscar-gpt-image2-skill](../../items/github-wuyoscar-gpt-image2-skill/card.md)) — CLI run is already `demonstrated`. awesome-gpt-image-2 template engine ([x-2092222199620833420](../../items/x-2092222199620833420/card.md)).
2. **Searchable galleries with a model name.** YouMind Nano Banana Pro recommender, 10k+ grep-style ([github-youmind-openlab-nano-banana-pro-prompts](../../items/github-youmind-openlab-nano-banana-pro-prompts/card.md)). MeiGen cross-model + MCP ([web-meigen-ai](../../items/web-meigen-ai/card.md)).
3. **Reusable brand fill-in.** PRYNE 16:9 editorial template ([x-2092979866836648104](../../items/x-2092979866836648104/card.md)) — prompt text is `demonstrated`.

Sol website-prompt teasers and Imageory.in stills are examples without a stored prompt. Do not plan a gallery around them.

## image-prompt-galleries — axis scores

| item | model family named | stored as code / searchable | reproducible params | license / attribution |
|---|---|---|---|---|
| wuyoscar gpt-image2-skill | GPT Image 2 | gallery + CLI + skill | CLI `-p` demonstrated | MIT |
| awesome-gpt-image-2 | GPT Image 2 | `cases.json` **541** / images **544** / badge 544; **22** templates in style-library | template engine + live SPA `gpt-image2.canghe.ai` | MIT |
| YouMind Nano Banana skill | Nano Banana Pro / Gemini image | **14,965** unique ids / manifest **15,508** / file-sum **22,466** (11 JSON cats; 7,299 ids in 2+ files) | top-3 + sample images stated | package.json MIT; no LICENSE file |
| MeiGen | GPT Image, Seedance, Nano Banana, Midjourney | MCP repo `data/trending-prompts.json` **1,446**; **9** named tools | community prompts; homepage live **129,701 B** (SSR shell) | MCP repo MIT; live gallery still uncounted |
| PRYNE brand template | GPT (implied) | one 16:9 template + fill-in line | demonstrated on-thread | author examples |
| Imageory.in | ChatGPT (tweet-only; homepage **167,558 B** has no ChatGPT string) | marketplace site (category chips; no prompt bodies) | stills only | unknown |
| GPT 5.6 Sol teasers | Sol | prompt **not captured**; quoted marketplace is **sceneai.art** (36 Copy Prompt / 46 previews) | video only | sceneai.art is a UI library, not the Sol text |

## image-prompt-galleries — claims that need a receipt

- YouMind “10,000+” — tree counted 2026-09-04: unique ids **14,965**, manifest `totalPrompts` **15,508**, category-file sum **22,466**. Do not collapse. See [nano-banana-pro-prompts-recommend](../../tools/nano-banana-pro-prompts-recommend.md).
- MeiGen “1,446+ / nine MCP tools” — repo file is **exactly 1,446**; nine `src/tools` names listed on the same NOTES. Live `meigen.ai` was Cloudflare 403 this pass.
- awesome-gpt-image-2 2,449 stars in 24h / 16,477 total — capture snapshot. API 2026-09-04: **28,017** stars. Case file counts on [gpt-image-2](../../tools/gpt-image-2.md).
- Sol website prompts — the prompt text is missing. Quoted “unlimited” link is **sceneai.art** (308,165 B; no GPT 5.6 / unlimited in HTML) ([gpt-5-6-sol](../../tools/gpt-5-6-sol.md)).

## image-prompt-galleries — do not treat as load-bearing

- Sol teasers and marketplace “unlimited site prompts.”
- fal.ai as a gallery — it is an API bus (secondary).
- Face-swap → Seedance — video identity lock, not an image gallery.

## image-prompt-galleries — next capture work

1. Save the Sol prompt text if the author posts it. Marketplace destination is now **sceneai.art**; still no Sol body. Keep those cards as examples-only.
2. YouMind + MeiGen file counts are on [nano-banana-pro-prompts-recommend](../../tools/nano-banana-pro-prompts-recommend.md). awesome-gpt-image-2 tree counts are on [gpt-image-2](../../tools/gpt-image-2.md). MeiGen homepage **200 / 129,701 B** (403 cleared; card `#c4`) is still an SSR shell — no headed card count. Do not treat the marketing HTML as 1,446.
3. Fold this subject into design-agent-skills only if a later pass finds no image-only users. Grain is already inside 6–60.
4. PRYNE / ARCO leftover: `pryne.com` is a **616 B** wasm-pack hello page; `lexnlin.com` NXDOMAIN. Brands are prompt-fill examples, not products ([gpt-image](../../tools/gpt-image.md); [x-2092979866836648104#c3](../../items/x-2092979866836648104/card.md)). Same attach on stills leftover [x-2092890365930131920#c2](../../items/x-2092890365930131920/card.md).
5. leftover27 unused `youmind.com/nano-banana-pro-prompts` **1,244,866 B** titles **10,000+**; footer TOTAL **15,508**. Do not collapse title 10k / footer 15,508 / tree **14,965** / category sum **22,466** ([nano-banana-pro-prompts-recommend](../../tools/nano-banana-pro-prompts-recommend.md); [github-youmind-openlab-nano-banana-pro-prompts#c4](../../items/github-youmind-openlab-nano-banana-pro-prompts/card.md)).
