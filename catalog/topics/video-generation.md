# Video generation

Topic slug: `video-generation`. Adjacent: [camera-control](camera-control.md), [bess-3d-flythrough](bess-3d-flythrough.md), [gaussian-splatting](gaussian-splatting.md), [ui-motion](ui-motion.md).

This lane is generative video as a *production hop*: Veo / Kling / Seedance / MiniMax, image-to-video, HTML-to-MP4, and the APIs that run them. It is not in-browser WebGL (see [three-js](three-js.md)) and not CSS/Lottie page motion (see [ui-motion](ui-motion.md)). The harvest is small and pipeline-shaped: a developer platform (fal), prompt galleries (MeiGen), an HTML→video path (html-video / OpenDesign HyperFrames), and 3D-conditioned clips (scroll-world, ArtiFixer, Atlas→spark.js).

The long-form BESS recipe — Blender blockout + MCP camera → motion-reference / first+last frames → Seedance/Veo/Kling/H3 — lives in `raw/notes/blender-minimax-h3-video-generation.md` (`note-blender-minimax-h3-video-generation`). That note is not yet tagged on this slug; treat it as the camera/video spine anyway.

Query here for “turn this still into a clip,” “HTML landing as MP4,” “which API hosts Seedance,” or “video model after a Blender path.” For authored camera rigs and depth passes open [camera-control](camera-control.md). For site-flythrough marketing, also open [bess-3d-flythrough](bess-3d-flythrough.md). Presence is not a recommendation.

## Pipelines

- **HTML/CSS → MP4** — author the shot in HTML, render via HyperFrames (`github-nexu-io-html-video`, `github-nexu-io-open-design`).
- **Prompt gallery → model** — copy a Seedance / GPT Image / Nano Banana prompt, run on fal or MeiGen MCP (`web-meigen-ai`, `web-fal-ai`).
- **Scroll-scrubbed 3D clip** — isometric diorama + Seedance/Monid as a landing hero (`github-oso95-scroll-world`).
- **Blender blockout → video model** — MCP camera path, first/last frames + motion reference (`note-blender-minimax-h3-video-generation`; also [camera-control](camera-control.md)).
- **Repair then re-render** — diffusion on broken/blurry 3D reconstructions before a flythrough (`github-nv-tlabs-ArtiFixer`, `x-2094929928865341832`).
- **Photo → world → orbit clip** — Atlas reconstruction presented with spark.js + three.js (`x-2094864872853119216`).

## Tools

- [fal](../../raw/items/web-fal-ai/) — `web-fal-ai` — genmedia APIs (Seedance / MiniMax / FLUX) plus GPUs; `llms.txt` for agents.
- [html-video](../../raw/items/github-nexu-io-html-video/) — `github-nexu-io-html-video` — HTML/CSS → MP4 via HyperFrames; OpenDesign video path.
- [OpenDesign](../../raw/items/github-nexu-io-open-design/) — `github-nexu-io-open-design` — vibe-design studio with HyperFrames / html-video motion.
- [MeiGen](../../raw/items/web-meigen-ai/) — `web-meigen-ai` — free GPT Image 2 / Nano Banana / Seedance prompt gallery + MCP.
- [ArtiFixer](../../raw/items/github-nv-tlabs-ArtiFixer/) — `github-nv-tlabs-ArtiFixer` — NVIDIA auto-regressive diffusion that enhances/extends 3D reconstructions.

## Techniques

- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world` — agent skill for Seedance/Monid isometric flythrough landings (also `bess-3d-flythrough`, `camera-control`).
- [NVIDIA ArtiFixer thread](../../raw/items/x-2094929928865341832/) — `x-2094929928865341832` — video diffusion that rebuilds broken/blurry 3D scans.
- [Atlas + spark.js + three.js](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216` — one still → World Labs Atlas → orbitable scene (also splat / camera / three-js).
- [Blender Minimax H3 note](../../raw/notes/blender-minimax-h3-video-generation.md) — `note-blender-minimax-h3-video-generation` — Blender MCP camera + depth-Z for tight interiors; H3/Seedance/Veo/Kling comparison.

## Examples

- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world` — scroll-scrubbed diorama as the marketing surface.
- [OpenDesign](../../raw/items/github-nexu-io-open-design/) — `github-nexu-io-open-design` — HTML-video inside a local-first design workspace.
- [Atlas one-image scene](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216` — reconstruction presented as a three.js clip.

## All items

<!-- AUTO:ITEMS -->
- [html-video](../../raw/items/github-nexu-io-html-video/) — `github-nexu-io-html-video`
- [OpenDesign](../../raw/items/github-nexu-io-open-design/) — `github-nexu-io-open-design`
- [ArtiFixer](../../raw/items/github-nv-tlabs-ArtiFixer/) — `github-nv-tlabs-ArtiFixer`
- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world`
- [LLM + Blender → AI Video: Photoreal BESS Flythrough](../../raw/notes/blender-minimax-h3-video-generation.md) — `note-blender-minimax-h3-video-generation`
- [animos — Motion templates for design showcases](../../raw/items/web-animos-editor/) — `web-animos-editor`
- [fal — generative media platform for developers](../../raw/items/web-fal-ai/) — `web-fal-ai`
- [MeiGen — Free GPT Image 2, Nano Banana & Seedance Prompts](../../raw/items/web-meigen-ai/) — `web-meigen-ai`
- [this is terrifying. Claude Opus 5 + Remotion can now generate videos. It can do motion design, demos and animations from](../../raw/items/x-2086030681772376399/) — `x-2086030681772376399`
- [BLENDER + SEEDANCE = FULL CAMERA CONTROL Claude Opus 5 builds a simple 3D mockup of the cafe in Blender. Basic blocks fo](../../raw/items/x-2087565352372723955/) — `x-2087565352372723955`
- [claude dropped Motion Prompt, and the crazy part is this entire animation was made with code, not AI-generated images or](../../raw/items/x-2088155107544191339/) — `x-2088155107544191339`
- [The bike, the ruins, the ramps, the Highlands sky. All of it started as one sentence typed into Atlas. Concept art, 3D a](../../raw/items/x-2088299905324396589/) — `x-2088299905324396589`
- [Animated in Higgsfield Seedance 2.5 + Cursor Composer 2.5 AI Skill: https://github.com/elayadesign/ai-design-skills](../../raw/items/x-2089770081459056765/) — `x-2089770081459056765`
- [Another design direction for this AI SaaS. built by Custom Skills + My Video Tool + Claude + Some Creativity](../../raw/items/x-2090079734571098131/) — `x-2090079734571098131`
- [MiniMax H3 just went unlimited on Runway. Generate responsibly. Or don't. It's unlimited 😌](../../raw/items/x-2090098441200517416/) — `x-2090098441200517416`
- [6 repos de AI Agents que estan explotando en github 1. Graft — https://github.com/NanoNets/Graft Hace que claude code se](../../raw/items/x-2091157554919280688/) — `x-2091157554919280688`
- [AI just changed how we create creative logo videos. MiniMax M3 can turn a simple logo into a polished, premium brand fil](../../raw/items/x-2091441060153278565/) — `x-2091441060153278565`
- [これ無料だから、同時並行で何個も試しまくれるのが超ありがたい。 簡単に使えるので、やり方気になる人多ければ解説記事出します！ 使ってるモデルはMiniMax H3](../../raw/items/x-2091519705911795761/) — `x-2091519705911795761`
- [ok we are paying $17 for 30s... and then one miss and you pay it again also prompting cant hold my whole head so i make ](../../raw/items/x-2091577179914338583/) — `x-2091577179914338583`
- [You can also make beautifully imperfect videos with AI coding models](../../raw/items/x-2091622751756751211/) — `x-2091622751756751211`
- [分享个真正牛逼的 AI 开源项目 OpenStory AI 视频创作真正困难的，往往不是生成一张漂亮的图片，而是让角色、场景、色彩、光线和叙事在每一个镜头中保持一致。 OpenStory 希望把「一段剧本」直接变成一套具有统一视觉风格的视频](../../raw/items/x-2091713204418490406/) — `x-2091713204418490406`
- [ok i dont want slow mo sitting in some other app next to the camera app its a handle on the timeline now stretch it and ](../../raw/items/x-2091722166685610284/) — `x-2091722166685610284`
- [Magnific 3D Motion is insanely cool. Generate an entire 3D space, control the camera motion around it. Export the 3D mot](../../raw/items/x-2091913781236683162/) — `x-2091913781236683162`
- [H3 Max is a post-trained variant of MiniMax H3 Tuned for stronger prompt adherence and elevated visual quality by @fal N](../../raw/items/x-2091924963288580539/) — `x-2091924963288580539`
- [Done before you're done MiniMax H3 Max generates a 5 second clip at 480p in under 5 seconds Unlimited, for the next 3 da](../../raw/items/x-2091957150793023651/) — `x-2091957150793023651`
- [CozyClayっていうオープンソースのプレビス制作ソフトつかってみました。Blenderに比べると拡張性は低いんだけど、MCPあるし格段に使いやすい 一回シーンをつくっちゃったら構図変更するのも30秒くらい。これで何回もやり直して、そこか](../../raw/items/x-2092009056164872620/) — `x-2092009056164872620`
- [AfterEffect → Minimax H3 「AI動画をレンダリングマシンとして使う」 生成するとき… ・AEでラフな同コンテを作成 ・Chat GPTでマテリアルを作成 ・強化するプロンプトを作成 ・H3でAEラフとマテリアル画像を](../../raw/items/x-2092040265234260091/) — `x-2092040265234260091`
- [Consistency across scenes, objects, and characters has never been easier to control. Place the cameras, animate, and par](../../raw/items/x-2092657951618249080/) — `x-2092657951618249080`
- [In this setup, a Blender blockout provides the motion and composition while a reference image guides the environment, su](../../raw/items/x-2092679517588574690/) — `x-2092679517588574690`
- [@MiniMaxAgent just shipped H3-based plugins for dynamic images and white-model rendering! Been playing around with them ](../../raw/items/x-2092702228947902622/) — `x-2092702228947902622`
- [video-use + codex for video editing is mindblowingly good one of the best AI tools I've ever used https://github.com/bro](../../raw/items/x-2092980272819999227/) — `x-2092980272819999227`
- [Introducing Mint Studio → Full 3D camera control for video generation right in your browser! No Blender required!](../../raw/items/x-2093051654937423887/) — `x-2093051654937423887`
- ["Can you actually direct the camera now, or is it still a prompt lottery?" MiniMax Design's 3D Director Stage lets you b](../../raw/items/x-2093053568748319181/) — `x-2093053568748319181`
- [Built a @heyglif skill that generates incredible motion graphics videos end to end, in any style, based on your script o](../../raw/items/x-2093081833911058772/) — `x-2093081833911058772`
- [devastating hyperframes mog 🥀 oh and btw the code for our launch videos, including this one, located in thread](../../raw/items/x-2093129469926215800/) — `x-2093129469926215800`
- [My workflow has completely changed. • Ideate with ChatGPT • Build with Fable 5 • Animate with Higgsfield • Keep iteratin](../../raw/items/x-2093236801079279978/) — `x-2093236801079279978`
- [【note更新しました📢】 本日は「Blenderチュートリアル動画まとめ」から 『崖の上のポニョのファンムービーの制作過程をタイムラプスで大公開！』 （原題：Ponyo and Sosuke | Fan Art Timelapse） をご](../../raw/items/x-2093256024635666465/) — `x-2093256024635666465`
- [Stop burning credits on AI videos. Block the scene in Blender first. Full 19-minute tutorial:](../../raw/items/x-2093374092795846745/) — `x-2093374092795846745`
- [BLENDER LOCKS THE SHOT. SEEDANCE FINISHES IT This is not a lucky night video. The 3D scene was built first. Then the cam](../../raw/items/x-2093377271771865267/) — `x-2093377271771865267`
- [THIS IS REVOLUTIONARY 3D Camera Control → AI Rendered Video ALL in your BROWSER NO BLENDER. NO PROMPT ROULETTE.](../../raw/items/x-2093380307735232543/) — `x-2093380307735232543`
- [This is what faceless video creation should look like. You have an idea. Calliope turns it into a complete 2D video. One](../../raw/items/x-2093481253043380418/) — `x-2093481253043380418`
- [Stop wasting hundreds of AI credits trying to get precise camera movement in Seedance 2.5 🚫 Instead of relying purely on](../../raw/items/x-2093663876692754713/) — `x-2093663876692754713`
- [This launch video got more than 7.5M views. full breakdown:](../../raw/items/x-2093681908227936745/) — `x-2093681908227936745`
- [Walk into Hogwarts... Built this landing for an AI-based Harry Potter Experience event. Built by Custom Skills + My Vide](../../raw/items/x-2093767075131220005/) — `x-2093767075131220005`
- [3 websites every AI filmmaker should bookmark: 🎥 http://eyecannndy.com — camera techniques 🎨 http://sesohq.com/pages/moo](../../raw/items/x-2093986548404428942/) — `x-2093986548404428942`
- [🚨 ADIÓS A LA EDICIÓN DE VIDEO Alguien acaba de crear una herramienta de edición de video gratuita para Claude Code... y ](../../raw/items/x-2094061655990702150/) — `x-2094061655990702150`
- [Today we're launching Claude for motion graphics 2.0. It does the sound now. One person is now a whole production team: ](../../raw/items/x-2094164487381414344/) — `x-2094164487381414344`
- [Gaussian splats let you choose the camera move after you've left the location. We added animation tools and 4K video exp](../../raw/items/x-2094377838774472944/) — `x-2094377838774472944`
- [Atlas + spark.js + three.js scene from one input image](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216`
- [NVIDIA ArtiFixer — video diffusion that rebuilds broken/blurry 3D scans](../../raw/items/x-2094929928865341832/) — `x-2094929928865341832`
- [AI was supposed to replace artists. So I hired one to make an AI Gucci ad. He drew every shot on paper first. Then Claud](../../raw/items/x-2095156045303701766/) — `x-2095156045303701766`
- [BREAKING: An unsupervised AI is doing 160,000 views a day on TikTok We connected 6 models to @lightreelai and Doublespee](../../raw/items/x-2095202138854977756/) — `x-2095202138854977756`
- [Generates cinematic product videos with Claude Code and Remotion using 152 shot recipe cards and motion styles. https://](../../raw/items/x-2095204640690147487/) — `x-2095204640690147487`
- [MiniMax H3の動画生成で生じる音声劣化を、高速に修正する手法が話題。 映像を低解像度にして音声のみを高ステップで再生成し、元動画と合成する仕組み。 生成時間を短縮しつつズレを防ぐため、Latentを縮小する工夫が賢いと好評。 #Mi](../../raw/items/x-2095427702325231977/) — `x-2095427702325231977`
- [This is insane: Hyper3D just dropped WorldGen, an AI that turns ONE photo into a full interactive 3D world Yingmu Techno](../../raw/items/x-2095437841958314100/) — `x-2095437841958314100`
- [MiniMax H3をプロダクトCGのレンダラー的に使うの試してみてる。ローカルで処理できるのはアツいね。 ローカルで方向性が定まってからAPIに投げられるので無駄が少ない。](../../raw/items/x-2095483352375837020/) — `x-2095483352375837020`
- [this launch video generated 4.6M+ views for @intelligenceco. posted by founder @ndrewpignanelli. full breakdown:](../../raw/items/x-2095521587785081193/) — `x-2095521587785081193`
<!-- /AUTO:ITEMS -->
