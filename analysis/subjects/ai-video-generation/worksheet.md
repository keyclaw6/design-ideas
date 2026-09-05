# Judgment worksheet: AI video models (ai-video-generation)

Owner aliases: video generation, Seedance, Kling, Veo. If a *3D camera stage* exists, stop and open [blockout-to-video-flythrough](../blockout-to-video-flythrough/worksheet.md). Code-rendered timelines live in [code-motion-graphics](../code-motion-graphics/worksheet.md).

## ai-video-generation — short stack to try

1. **Identity lock, then motion.** Must-read: GPT Image 2 face-swap stills → Seedance 2.5 ([x-2094819241916801165](../../items/x-2094819241916801165/card.md)). Same idea with paper storyboards + Claude keyframes + Arcads ([x-2095156045303701766](../../items/x-2095156045303701766/card.md)).
2. **Audio repair and local preview before API spend.** H3 audio downscale / high-step regen ([x-2095427702325231977](../../items/x-2095427702325231977/card.md)). H3 as a local product-CG renderer ([x-2095483352375837020](../../items/x-2095483352375837020/card.md)). Magnific H3 Max “5s 480p in under 5s” is a latency note, not a quality note ([x-2091957150793023651](../../items/x-2091957150793023651/card.md)).
3. **Agent cut, not a new model.** video-use / Video Use ([x-2092980272819999227](../../items/x-2092980272819999227/card.md), [x-2094061655990702150](../../items/x-2094061655990702150/card.md)).
4. **Story / faceless pipelines.** OpenStory script-to-styled-video ([x-2091713204418490406](../../items/x-2091713204418490406/card.md)). Calliope idea→2D YouTube ([x-2093481253043380418](../../items/x-2093481253043380418/card.md)).

fal.ai is the API bus ([web-fal-ai](../../items/web-fal-ai/card.md)). Launch-video view-count threads are craft references, not model scores.

## ai-video-generation — axis scores

| item | control beyond text | audio / lipsync | character or product lock | local preview before paid API | duration / res numbers |
|---|---|---|---|---|---|
| GPT Image 2 + Seedance 2.5 | high (face-swap stills) | unknown | high (stated identity lock) | stills are cheap; video is not | none on the card |
| Paper boards + Arcads | high (human boards) | unknown | mid (sheets) | mid | tweet 480p/1080p; host has Seedance 7-day promo |
| H3 audio repair | mid (resolution / steps) | high (this *is* the fix) | n/a | mid | low-res plate then composite |
| H3 local product-CG | mid (local lock) | unknown | product, not character | high | unknown |
| H3 Max on Magnific | low (host toggle) | unknown | unknown | unlimited trial stated | 5s / 480p / <5s gen (stated) |
| video-use | high (folder of footage) | n/a (edit) | n/a | high (local files) | n/a |
| OpenStory | mid (script + style) | unknown | mid (cross-scene style) | unknown | unknown |
| Calliope | mid (script→2D→VO) | VO claimed | 2D characters | unknown | no matching product host this pass; calliope.so is Decision Intelligence |
| Higgsfield + Fable + Cursor | mid (design then animate) | unknown | unknown | mid | unknown |
| LightReel 160k/day | product is UGC researcher (10k TikToks/day meta) | unknown | unknown | 3-day trial stated | **160k/day not on lightreel.ai** |
| Base44 / Intelligence Co breakdowns | craft, not a control | unknown | n/a | n/a | Base44 landing live; intelligence.co → Design Arena (not a craft page); view counts still tweet-only |
| fal.ai | API routing | model-dependent | model-dependent | pay-per-call | catalog, not one number |
| H3 unlimited on Runway | host quota (terms: Hailuo 3.0, 7 days) | unknown | unknown | Max-plan promo; MCP/Agent excluded | none |

## ai-video-generation — claims that need a receipt

- Face-swap → Seedance identity lock — must-read recipe; need two scenes with the same face and a still that is not the first frame.
- H3 Max 5s@480p in under 5s — host blog; re-time on a named prompt.
- 7.5M / 4.6M launch-video views — attributed views, no property export.
- LightReel 160k daily TikTok — unsupervised stack claim; no account ids. Live site is a UGC researcher (**10,000** TikToks/day, **4,000+** brands); 160k is not on the page ([lightreelai](../../tools/lightreelai.md)).
- OpenStory / Calliope “finished video from a script” — OpenStory is first-party (repo + openstory.so). Calliope thread is `captured_full`; public hosts this pass are Decision Intelligence (`calliope.so`) or Cloudflare **403** (`calliope.ai`) — [calliope](../../tools/calliope.md).
- H3 audio repair — Japanese field note. Quoted URL is Reddit `1w5zh4z` (www + old both **403**). Amplify video **10.354 s** / 854×472. Downscale / step-count integers still missing ([minimax-h3](../../tools/minimax-h3.md)).

## ai-video-generation — do not treat as load-bearing

- Secondary blockout items (cafe Seedance, Unreal MCP, CozyClay, 3D Director) — wrong subject.
- “AI coding models make imperfect handcrafted motion” — that argument belongs with Remotion / html-video. leftover14 attach: tweet names no renderer; Remotion first-party stays leftover6 **113,524 B** / **58,331★** ([x-2091622751756751211#c2](../../items/x-2091622751756751211/card.md)).
- Unlimited H3 on Runway / Magnific trial windows — quota copy, expires. leftover12 Runway terms are **Hailuo 3.0** / **7 days** / MCP+Agent excluded, not MiniMax H3 ([minimax-h3](../../tools/minimax-h3.md); [x-2090098441200517416#c2](../../items/x-2090098441200517416/card.md)).

## ai-video-generation — next capture work

1. leftover19: `wuyoscar/GPT-Image2-Skill` MIT **5,153★** documents multi-reference `/v1/images/edits`. Official image-generation docs **1,248,104 B**. Neither names identity lock. leftover24 unused GitHub recount is **5,154★** (`#c5`). Seedance 2.5 page still has no identity-lock copy ([seedance](../../tools/seedance.md); [gpt-image-2](../../tools/gpt-image-2.md)). Face-swap stills stay the tweet recipe. Thread stays 1/57.
2. video-use README still describes a local-folder path; Browser Use Cloud is optional ([video-use](../../tools/video-use.md)). Local `helpers/render.py` on a two-range lavfi EDL wrote draft `final.mp4` **132,217** B / **1.666** s / **1280×720** / 24 fps (`analysis/_work/captures/video-use-edit/`). Remaining: a Claude Code / ElevenLabs skill-loop edit of real talking-head takes.
3. Keep launch-video breakdowns as craft notes; do not score models by view counts. Base44.com is a vibe-coding product landing (**435,678 B**). intelligence.co 301s to intelligence.ai Design Arena (**52,359 B**). Titouan “full breakdown” is the X amplify video **106.24 s** / 3840×2160; thread stays 20/1.
4. fujiryu00 “H3 is free” video is **13.723 s** / 1108×720. Hailuo homepage **848,994 B** says H3 is live with **From /mo** + Sign In; page “Free” is an image-pack category. Pricing page **617,559 B** names Standard **$14.99/mo** / Pro **$54.99/mo** (card `#c4`). Tool page **651,974 B** “Free Credits to Start Creating!” is a signup bonus (card `#c5`). Research blog `/blog/minimax-h3` **98,310 B** (15 s @ 2K; weights planned). Tweet 無料 stays tweet-only ([minimax-h3](../../tools/minimax-h3.md)).
5. OpenStory is first-party on [openstory](../../tools/openstory.md): openstory.so **270,063 B** (5-minute films / consistent characters); repo MIT **574★**; Fal.ai + Cloudflare on the README only ([x-2091713204418490406#c3](../../items/x-2091713204418490406/card.md)).
6. Calliope card is now `ready` (thread `captured_full`). Product hunt: calliope.so is Decision Intelligence; calliope.ai **403** — do not hammer ([x-2093481253043380418#c3](../../items/x-2093481253043380418/card.md)).
7. Higgsfield leftover homepage is first-party **530,348 B** ([higgsfield](../../tools/higgsfield.md); [x-2093236801079279978#c2](../../items/x-2093236801079279978/card.md)). ChatGPT + Fable 5 workflow strings absent. Pricing `/pricing` is a **78,150 B** shell (visible **332 B**, no plan table). `fable.ai` is a Spaceship listing at **$1,500,000** — do not collapse with Fable 5.
8. Local H3 product-CG leftover now points at Hailuo pricing/blog ([minimax-h3](../../tools/minimax-h3.md); [x-2095483352375837020#c2](../../items/x-2095483352375837020/card.md)). Pages do not document a local H3 renderer.
9. leftover12 Arcads homepage **198,802 B** / **1,000+** actors / 7-day Seedance 2.5 promo. No official Arcads MCP repo (GH search **3** / **0★**). Paper-board 480p/1080p/4K stays tweet-only ([seedance](../../tools/seedance.md); [x-2095156045303701766#c2](../../items/x-2095156045303701766/card.md)). MiniMax Agent H3 plugins leftover still tweet-only ([x-2092702228947902622#c2](../../items/x-2092702228947902622/card.md)).
10. leftover28 unused `fal.ai/docs/llms.txt` **95,947 B**: **198** unique doc links; **1,000+** models ([fal-api](../../tools/fal-api.md); [web-fal-ai#c3](../../items/web-fal-ai/card.md)). Did not call a model.
