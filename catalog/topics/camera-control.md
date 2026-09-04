# Camera control

Topic slug: `camera-control`. Adjacent: [video-generation](video-generation.md), [bess-3d-flythrough](bess-3d-flythrough.md), [three-js](three-js.md), [gaussian-splatting](gaussian-splatting.md).

This lane is *authored cameras*: Blender MCP flythroughs, depth passes, cinematic motion reference, and in-browser camera rigs. Video models without a path invent the move; this file is the path. WebGL chase/orbit skills live here *and* on [three-js](three-js.md). Generative clip APIs stay on [video-generation](video-generation.md).

Items cluster three ways. **Previs in DCC** — the BESS note’s blender-mcp / Blender Lab MCP camera keyframes, first+last frames, and Z-pass depth video (Wan VACE / LTX 3DREAL) when interiors must not hallucinate. **Landing cameras** — scroll-world’s scrubbed isometric path. **Browser rigs** — Three.js Awesome Graphics Agent Skills (authored lenses, chase-orbit, visual-validation mosaics). ArtiFixer and Atlas sit here because a repaired or reconstructed volume still needs a camera to read.

Query here for “lock the flythrough,” “depth as motion reference,” or “agent that authors a Three.js camera.” For which video model consumes the path, open [video-generation](video-generation.md). For the BESS marketing use-case, also open [bess-3d-flythrough](bess-3d-flythrough.md). Presence is not a recommendation.

## Pipelines

- **Blender MCP → motion reference** — LLM keyframes the camera, render first/last (and optional Z-depth) into Seedance/Veo/Kling/H3 (`note-blender-minimax-h3-video-generation`).
- **Depth-conditioned interior** — Blender Z-pass as the only reliable tight-interior route (`note-blender-minimax-h3-video-generation`).
- **Scroll-scrubbed path** — isometric diorama camera tied to page scroll (`github-oso95-scroll-world`).
- **Browser camera rig** — install graphics skills, author lens/chase-orbit, mosaic-validate (`github-scottstts-threejs-awesome-graphics-agent-skills`).
- **Recon then orbit** — Atlas/ArtiFixer volume, then a three.js or video-model camera (`x-2094864872853119216`, `github-nv-tlabs-ArtiFixer`).

## Tools

- [Three.js Awesome Graphics Agent Skills](../../raw/items/github-scottstts-threejs-awesome-graphics-agent-skills/) — `github-scottstts-threejs-awesome-graphics-agent-skills` — camera rigs, PBR/TSL, visual-validation mosaics.
- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world` — scroll-tied isometric camera for landings.
- [ArtiFixer](../../raw/items/github-nv-tlabs-ArtiFixer/) — `github-nv-tlabs-ArtiFixer` — repair the volume the camera will fly through.

## Techniques

- [Blender Minimax H3 note](../../raw/notes/blender-minimax-h3-video-generation.md) — `note-blender-minimax-h3-video-generation` — blender-mcp `create_camera` / `add_keyframe`; start+end frames drift; depth video for interiors.
- [threejs camera / visual-validation](../../raw/items/github-scottstts-threejs-awesome-graphics-agent-skills/) — `github-scottstts-threejs-awesome-graphics-agent-skills` — authored lenses and diagnostic mosaics (also `three-js`).
- [NVIDIA ArtiFixer thread](../../raw/items/x-2094929928865341832/) — `x-2094929928865341832` — diffusion repair so the camera is not staring at holes.
- [Atlas + spark.js + three.js](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216` — reconstructed world with an orbitable camera.

## Examples

- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world` — camera as scroll timeline, not a free fly.
- [Atlas one-image scene](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216` — one still, then an authored orbit.

## All items

<!-- AUTO:ITEMS -->
- [ArtiFixer](../../raw/items/github-nv-tlabs-ArtiFixer/) — `github-nv-tlabs-ArtiFixer`
- [scroll-world](../../raw/items/github-oso95-scroll-world/) — `github-oso95-scroll-world`
- [Three.js Awesome Graphics Agent Skills](../../raw/items/github-scottstts-threejs-awesome-graphics-agent-skills/) — `github-scottstts-threejs-awesome-graphics-agent-skills`
- [codex + blender is insane](../../raw/items/x-2065843739340509693/) — `x-2065843739340509693`
- [BLENDER + SEEDANCE = FULL CAMERA CONTROL Claude Opus 5 builds a simple 3D mockup of the cafe in Blender. Basic blocks fo](../../raw/items/x-2087565352372723955/) — `x-2087565352372723955`
- [Gemini 3.7 Flash High in Antigravity 🔥🔥 it created this in ~4 mins - pretty fast and perfect > Bugatti W16 engine with m](../../raw/items/x-2088240171565412733/) — `x-2088240171565412733`
- [The bike, the ruins, the ramps, the Highlands sky. All of it started as one sentence typed into Atlas. Concept art, 3D a](../../raw/items/x-2088299905324396589/) — `x-2088299905324396589`
- [@threejs Awesome Graphics Agent Skills v0.8.0 is out! npx threejs-awesome-graphics-agent-skills@latest install --agent c](../../raw/items/x-2088738850705113398/) — `x-2088738850705113398`
- [MiniMax H3 just went unlimited on Runway. Generate responsibly. Or don't. It's unlimited 😌](../../raw/items/x-2090098441200517416/) — `x-2090098441200517416`
- [HIGGSFIELD BUILDS A FULL LOW-POLY WORLD INSIDE BLENDER One prompt. Claude Opus 5 takes control through the Higgsfield pl](../../raw/items/x-2091497597743612379/) — `x-2091497597743612379`
- [ok we are paying $17 for 30s... and then one miss and you pay it again also prompting cant hold my whole head so i make ](../../raw/items/x-2091577179914338583/) — `x-2091577179914338583`
- [分享个真正牛逼的 AI 开源项目 OpenStory AI 视频创作真正困难的，往往不是生成一张漂亮的图片，而是让角色、场景、色彩、光线和叙事在每一个镜头中保持一致。 OpenStory 希望把「一段剧本」直接变成一套具有统一视觉风格的视频](../../raw/items/x-2091713204418490406/) — `x-2091713204418490406`
- [ok i dont want slow mo sitting in some other app next to the camera app its a handle on the timeline now stretch it and ](../../raw/items/x-2091722166685610284/) — `x-2091722166685610284`
- [Magnific 3D Motion is insanely cool. Generate an entire 3D space, control the camera motion around it. Export the 3D mot](../../raw/items/x-2091913781236683162/) — `x-2091913781236683162`
- [New in Toolbag 5.03: SpaceMouse Support! 🖱️ By popular request, we’ve added robust SpaceMouse support in Toolbag 5 for v](../../raw/items/x-2091918691747189053/) — `x-2091918691747189053`
- [CLAUDE DIRECTS A FULL CINEMATIC SHOT IN UNREAL One prompt. Claude takes control through Unreal MCP > Spawns CineCamera >](../../raw/items/x-2092008677834387672/) — `x-2092008677834387672`
- [CozyClayっていうオープンソースのプレビス制作ソフトつかってみました。Blenderに比べると拡張性は低いんだけど、MCPあるし格段に使いやすい 一回シーンをつくっちゃったら構図変更するのも30秒くらい。これで何回もやり直して、そこか](../../raw/items/x-2092009056164872620/) — `x-2092009056164872620`
- [Introducing Higgsfield in Blender. > Prompt the scene and build the blockout > Describe the camera move and get it anima](../../raw/items/x-2092255768770920506/) — `x-2092255768770920506`
- [Polly Pockets, but for gamers: ViscousRealm imagined tiny gaming rooms inside different controllers. Which animation is ](../../raw/items/x-2092644473868050684/) — `x-2092644473868050684`
- [Consistency across scenes, objects, and characters has never been easier to control. Place the cameras, animate, and par](../../raw/items/x-2092657951618249080/) — `x-2092657951618249080`
- [In this setup, a Blender blockout provides the motion and composition while a reference image guides the environment, su](../../raw/items/x-2092679517588574690/) — `x-2092679517588574690`
- [We use GLM-5.3-Flash build a dream kitchen. A 3D world built in Blender. This is not a generated video.](../../raw/items/x-2093047548550525165/) — `x-2093047548550525165`
- [Introducing Mint Studio → Full 3D camera control for video generation right in your browser! No Blender required!](../../raw/items/x-2093051654937423887/) — `x-2093051654937423887`
- ["Can you actually direct the camera now, or is it still a prompt lottery?" MiniMax Design's 3D Director Stage lets you b](../../raw/items/x-2093053568748319181/) — `x-2093053568748319181`
- [CLAUDE BUILDS AN ALCHEMIST SHOP ACROSS TWO MCP SERVERS This is not one tool doing everything. Claude Code runs the whole](../../raw/items/x-2093064017468145963/) — `x-2093064017468145963`
- [【note更新しました📢】 本日は「Blenderチュートリアル動画まとめ」から 『崖の上のポニョのファンムービーの制作過程をタイムラプスで大公開！』 （原題：Ponyo and Sosuke | Fan Art Timelapse） をご](../../raw/items/x-2093256024635666465/) — `x-2093256024635666465`
- [Stop burning credits on AI videos. Block the scene in Blender first. Full 19-minute tutorial:](../../raw/items/x-2093374092795846745/) — `x-2093374092795846745`
- [BLENDER LOCKS THE SHOT. SEEDANCE FINISHES IT This is not a lucky night video. The 3D scene was built first. Then the cam](../../raw/items/x-2093377271771865267/) — `x-2093377271771865267`
- [THIS IS REVOLUTIONARY 3D Camera Control → AI Rendered Video ALL in your BROWSER NO BLENDER. NO PROMPT ROULETTE.](../../raw/items/x-2093380307735232543/) — `x-2093380307735232543`
- [Stop wasting hundreds of AI credits trying to get precise camera movement in Seedance 2.5 🚫 Instead of relying purely on](../../raw/items/x-2093663876692754713/) — `x-2093663876692754713`
- [How about one image straight to an editable UE5 or Blender scene? Lumera just dropped paper - Engine-Native Editable 3D ](../../raw/items/x-2093937170717585657/) — `x-2093937170717585657`
- [3 websites every AI filmmaker should bookmark: 🎥 http://eyecannndy.com — camera techniques 🎨 http://sesohq.com/pages/moo](../../raw/items/x-2093986548404428942/) — `x-2093986548404428942`
- [Gaussian splats let you choose the camera move after you've left the location. We added animation tools and 4K video exp](../../raw/items/x-2094377838774472944/) — `x-2094377838774472944`
- [Atlas + spark.js + three.js scene from one input image](../../raw/items/x-2094864872853119216/) — `x-2094864872853119216`
- [NVIDIA ArtiFixer — video diffusion that rebuilds broken/blurry 3D scans](../../raw/items/x-2094929928865341832/) — `x-2094929928865341832`
- [Blender MCPでFable 5.1を使い、右のエクイレクタングラー方式の都市パノラマ画像をリソースとして都市を構築させたところ、一発でこの情報量のモデルが完成。 これを手作業で作れと言われたら、3人日はかかるかな……。 テストでこの](../../raw/items/x-2095159781883597031/) — `x-2095159781883597031`
- [AIでBlenderを操作する方法 - CLIとMCPの使い分け｜npaka @npaka123 https://note.com/npaka/n/n7f7531e7b9ed?sub_rt=share_sb](../../raw/items/x-2095288402606514424/) — `x-2095288402606514424`
- [This is insane: Hyper3D just dropped WorldGen, an AI that turns ONE photo into a full interactive 3D world Yingmu Techno](../../raw/items/x-2095437841958314100/) — `x-2095437841958314100`
- [Take a photo of the real world Paste it into Blender 3D](../../raw/items/x-2095512142766342624/) — `x-2095512142766342624`
<!-- /AUTO:ITEMS -->
