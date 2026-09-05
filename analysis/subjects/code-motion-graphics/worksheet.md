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
| Glif skill | unknown (hosted) | Glif chat card `explainer-motion-graphics-video` live | style presets | mid | n/a |
| LottieFiles | mid (library + Copilot) | Lottie/dotLottie | 800k+ library stated | mid | n/a |
| animos | low (templates) | raster MP4/WebM | 25 templates | low | n/a |
| AE → H3 | low (AE is source) | AE + H3 | comps | human | high |
| CoAnimator + Fable | mid | desktop WebGL (local GPU); unlimited local MP4 | unknown | claimed editable; Claude Code / Codex / Antigravity / OpenClaw named | n/a |
| MiniMax M3 logo-to-film | unknown | model | none | low | this *is* the model |
| Opus 5 + Remotion reaction | unknown | Remotion (React; Agent Skills named) | none | claimed | n/a |

## code-motion-graphics — claims that need a receipt

- html-video default path Hyperframes + ffmpeg — README confirms Chromium + libx264; Remotion adapter **not built** ([html-video](../../tools/html-video.md)). Local smoke `frame-data-chart-nyt` wrote 226,463 bytes (4.77 s) then a banked re-run of **241,922** bytes (4.75 s), both 1920×1080/60 libx264. Do not collapse the two sizes.
- html-video README 21 vs tree **23** yaml names listed on [html-video](../../tools/html-video.md). 14-agent count is a card summary of a longer name list.
- motion-anything README **403** vs tree **218** `recipe.motion.yaml` ([motion-anything](../../tools/motion-anything.md)). Do not collapse the two numbers.
- video-shotcraft tweet 152/209 is stale; README + tree **157** cards / **214** styles ([video-shotcraft](../../tools/video-shotcraft.md)).
- LottieFiles “~90% smaller than GIF” and “800k+” — marketing.
- HeyGen HyperFrames “code is in the thread” — quoted `t.co` resolves to `heygen-com/hyperframes-launches` (`claude-paper-launch/`); **20** launch dirs / README **19** video rows / tree **185** html. Thread still `captured_partial` (5/1). Receipts on [hyperframes](../../tools/hyperframes.md).
- MiniMax M3 logo-to-brand-film — claim-source, no recipe.

## code-motion-graphics — do not treat as load-bearing

- “every pixel fully editable” harness promo ([x-2091688420695564296](../../items/x-2091688420695564296/card.md)) — X video **20 s** / 1920×1080; editability still tweet-only.
- OpenDesign as a motion tool — it is a design workspace (secondary).
- AE→H3 as proof that code motion is dead — it is a conditioner path.

## code-motion-graphics — next capture work

1. Local html-video smoke of `frame-data-chart-nyt` is now in the bank: `analysis/_work/captures/html-video-smoke/output-2026-09-04_22-12-31.mp4` (**241,922** B, 4.75 s, 1920×1080/60). Earlier `/tmp` smoke was 226,463 B / 4.77 s. Path + ffprobe on [html-video](../../tools/html-video.md).
2. HeyGen quoted tweet is `heygen-com/hyperframes-launches` (not missing). Counts + LFS + NOTICE on [hyperframes](../../tools/hyperframes.md). Root video **54.366 s** / 3004×1240. Remaining: the other **4** replies into `thread-raw/` (status stays `captured_partial` until then).
3. loopany reddit-karma prompt body is on [loop-library](../../tools/loop-library.md). Headlong cloc 1.98 (**9,912 code**) is on [headlong](../../tools/headlong.md).
4. AE→H3 Japanese handoff ([x-2092040265234260091](../../items/x-2092040265234260091/card.md)) is an X video **7.061 s** / 1232×1276. Recipe already English. Stale `thread-failed` dropped; thread is `captured_partial` 13/1.
5. Motion Prompt Google Doc is now first-party ([x-2088155107544191339#c3](../../items/x-2088155107544191339/card.md); [claude-motion-prompt](../../tools/claude-motion-prompt.md)): 4–7 beats; `.mp4` + `.html`; 15–20 s / ~600 frames / 5–15 min; Opus 5. Install is a sent `.skill` file, not a public repo.
6. Remotion homepage + GitHub are first-party ([remotion](../../tools/remotion.md)): **58,331★** / license NOASSERTION; Creators **$25/mo/seat**; Automators **$0.01/render** / **$100/mo** min ([x-2086030681772376399#c2](../../items/x-2086030681772376399/card.md)).
7. CoAnimator product page **165,040 B** ([coanimator](../../tools/coanimator.md)): local unlimited MP4; free 720p watermark; Lottie not shipped. Glif t.co → explainer-motion-graphics card ([glif](../../tools/glif.md)).
8. Claude for motion graphics 2.0 leftover is **Raylight** ([claude-motion-graphics](../../tools/claude-motion-graphics.md); [x-2094164487381414344#c3](../../items/x-2094164487381414344/card.md)). Template t.co → `raylight.app/community/templates/q3BBAgWP` (**1,660 B** SPA). Homepage **292,501 B**. Annual: Free **$0** / Hobby **$12** / Pro **$24** / Max **$49**. MCP `https://api.raylight.app/mcp`. Sound-mode t.co is the quoted critique tweet, not a product page. leftover7 GitHub hits are other repos.
9. MiniMax M3 logo-to-film leftover is not Hailuo H3 ([x-2091441060153278565#c2](../../items/x-2091441060153278565/card.md)). Do not collapse M3 with H3.
