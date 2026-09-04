# Judgment worksheet: code-rendered motion (code-motion-graphics)

Owner aliases: Remotion, html-video, HyperFrames. Scroll/UI motion on a live page is [landing-ui-motion](../landing-ui-motion/worksheet.md).

## code-motion-graphics — short stack to try

1. **HTML/CSS as the timeline, local MP4 out.** [nexu-io/html-video](../../items/github-nexu-io-html-video/card.md) (Hyperframes + ffmpeg; 14 agents / README 21 templates / tree **23** yaml). HeyGen launch clip is the public example ([x-2093129469926215800](../../items/x-2093129469926215800/card.md)).
2. **Chat-native recipes with Lottie/MP4 export.** [motion-anything](../../items/github-nexu-io-motion-anything/card.md) (README **403** recipes / tree **218** yaml, eight engines). video-shotcraft is Remotion + README **157** cards / **214** styles ([x-2095204640690147487](../../items/x-2095204640690147487/card.md)).
3. **Script → code film.** Claude Motion Prompt ([x-2088155107544191339](../../items/x-2088155107544191339/card.md)). Claude for motion graphics 2.0 ([x-2094164487381414344](../../items/x-2094164487381414344/card.md)). Glif Vox-style skill ([x-2093081833911058772](../../items/x-2093081833911058772/card.md)).
4. **Lottie when the runtime is the web, not an MP4.** LottieFiles ([web-lottiefiles](../../items/web-lottiefiles/card.md)). animos.app is 25 templates → raster video ([web-animos-editor](../../items/web-animos-editor/card.md)).

After Effects rough comps as H3 plates ([x-2092040265234260091](../../items/x-2092040265234260091/card.md)) is a *handoff into a video model*, not a replacement for Remotion.

## code-motion-graphics — axis scores

| item | code is source of truth | runtime | shot-recipe reuse | agent authors timeline | handoff into video model |
|---|---|---|---|---|---|
| html-video / HyperFrames | high | HTML → Chromium → MP4 | README 21 / tree 23 yaml | high (14 agents stated) | optional (you already have frames) |
| motion-anything | high | live page + Lottie/MP4 | README 403 / tree 218 yaml | high (8 engines) | export, then maybe |
| video-shotcraft | high | Remotion | README 157 cards / 214 styles | high (Claude Code) | n/a |
| Claude Motion Prompt | high | HTML player + MP4 | beat sheet | high | n/a |
| Claude motion graphics 2.0 | mid (script is source) | their renderer | script lines | high | n/a (ships audio) |
| Glif skill | unknown (hosted) | Glif | style presets | mid | n/a |
| LottieFiles | mid (library + Copilot) | Lottie/dotLottie | 800k+ library stated | mid | n/a |
| animos | low (templates) | raster MP4/WebM | 25 templates | low | n/a |
| AE → H3 | low (AE is source) | AE + H3 | comps | human | high |
| CoAnimator + Fable | mid | their 3D scene | unknown | claimed editable | n/a |
| MiniMax M3 logo-to-film | unknown | model | none | low | this *is* the model |
| Opus 5 + Remotion reaction | unknown | Remotion | none | claimed | n/a |

## code-motion-graphics — claims that need a receipt

- html-video default path Hyperframes + ffmpeg — README confirms Chromium + libx264; Remotion adapter **not built** ([html-video](../../tools/html-video.md)). Still no local MP4 from this host.
- html-video README 21 vs tree **23** yaml names listed on [html-video](../../tools/html-video.md). 14-agent count is a card summary of a longer name list.
- motion-anything README **403** vs tree **218** `recipe.motion.yaml` ([motion-anything](../../tools/motion-anything.md)). Do not collapse the two numbers.
- video-shotcraft tweet 152/209 is stale; README + tree **157** cards / **214** styles ([video-shotcraft](../../tools/video-shotcraft.md)).
- LottieFiles “~90% smaller than GIF” and “800k+” — marketing.
- HeyGen HyperFrames “code is in the thread” — confirm the code actually landed in `thread.md`.
- MiniMax M3 logo-to-brand-film — claim-source, no recipe.

## code-motion-graphics — do not treat as load-bearing

- “every pixel fully editable” harness promo ([x-2091688420695564296](../../items/x-2091688420695564296/card.md)).
- OpenDesign as a motion tool — it is a design workspace (secondary).
- AE→H3 as proof that code motion is dead — it is a conditioner path.

## code-motion-graphics — next capture work

1. Render one html-video template locally; attach the MP4 path on the card (needs Playwright Chromium + ffmpeg).
2. If the HeyGen thread promised source, extract it into `thread-raw/` if it is still missing.
3. Dump one loopany prompt body; Headlong local `bin/` + `thinkers/` cloc.
