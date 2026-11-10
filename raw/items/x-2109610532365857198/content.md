# People keep asking how I make my PCBs with Claude Opus 5.5. So here's the whole pipeline in 60 seconds, all real captures.
> Source: https://x.com/VectorCrossProd/status/2109610532365857198
> Author: Nigel Hungerford-Symes (@VectorCrossProd)
> Posted: 2026-10-12T11:42:00+00:00
> Captured: 2026-10-15T09:02:28+00:00
> Stats at capture: 7,503 views · 182 likes · 12 replies · 8 reposts · 254 bookmarks · 1 quotes

## Post

People keep asking how I make my PCBs with Claude Opus 5.5. So here's the whole pipeline in 60 seconds, all real captures.

Based on the Kookabus-03 board, an 8xAA battery pack for my robots:

What part of this do you want me to go deeper on?

## Media

[Post media 1](media/video-01.mp4) — Source media: https://video.twimg.com/amplify_video/2109595301023768577/vid/avc1/1280x720/ZYmDYfE7W4v3nLs_.mp4?tag=29
![](media/image-01.jpg) — Post media 1 thumbnail. Source media: https://pbs.twimg.com/amplify_video_thumb/2109595301023768577/img/HeBBWPumuOpYU07X.jpg

## Thread

### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109770770289455509)) — 2026-10-12T22:18:43+00:00

Yes that is part of my workflow. I do have Claude use the Kicad MCP to select the standard PCBA parts for cost savings. I really want to push the capability of routing, so I made TraceMaker which optimises the component placement and routing, it runs locally. https://t.co/QXXc9mLbl9
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109867245056954396)) — 2026-10-13T04:42:05+00:00

@unfinishedplans Are you using Claude Code on a Linux machine that has kicad and FreeCad installed? I think that is a big part of it
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2110560126533005774)) — 2026-10-15T02:35:21+00:00

@DorleenSullivan Yep, under-load current and the idle sag are the useful ones. I've got the INA226 live on Kookabus-01 already, will tidy up the efficiency numbers next.
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109771641773588540)) — 2026-10-12T22:22:11+00:00

It is a day from idea to production ready board files. Then the board takes a couple of days to be made and is then shipped.   Claude Opus 5.5 did about 99% of the work, I stepped in probably 8 times total, with a review of placement, or a BOM review, or it needed to ask a question which I responded to in text.
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109770252431298680)) — 2026-10-12T22:16:40+00:00

For constraints like size, I just include that in the initial prompt "I need X, the board must be 75mm x 75mm, please follow mounting holes and other features in Project Y..."  I let Claude handle the component footprints, it selects components based on what is available for PCBA at JLCPCB and if there is a missing footprint it will search pretty hard and if needed it will also grab the datasheet and make its own in kicad.   If I need to hold a component at a location (mounting) I either ask Claude to do it in text or I can open the pcb in kicad and specify it is a non-movable component.
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109625358094078355)) — 2026-10-12T12:40:54+00:00

@Fuchiio Simple boards are about $30 per board when you buy 5. The cost can go up really easily if you aren't careful. The duration is about 5 days, you can rush ship. The AI is used to my project environment so I can have a designed board each day in this kookabus series.
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109769465974206746)) — 2026-10-12T22:13:32+00:00

@hugospdx Thanks, if there is more detail needed in any step let me know and I can expand it.
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109769330594623637)) — 2026-10-12T22:13:00+00:00

@DanDermodyLLC It uses FreeRouting with kicad locally, now I have moved to TraceMaker because TraceMaker can optimise component placement as well as routing.  https://t.co/vdP6pxOxPV
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109772143554887762)) — 2026-10-12T22:24:11+00:00

@adam_bicke16564 Thanks, I think everyone with a cool idea should try this out at least once.
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109772057689092425)) — 2026-10-12T22:23:50+00:00

@furt_tech Yes Claude and I chatted about the board and it did 99%of the work required to get it into production.   The first of these worked 100% and I have two more in the mail.
### Nigel Hungerford-Symes ([@VectorCrossProd](https://x.com/VectorCrossProd/status/2109771850301784356)) — 2026-10-12T22:23:01+00:00

@SixtusStar Yep Opus 5.5 is very capable of basic placement. To give it a better tool, I started TraceMaker which optimises placement for routing. https://t.co/vdP6pxOxPV

## Comments

### UnfinishedPlans ([@unfinishedplans](https://x.com/unfinishedplans/status/2109782732515455414)) — 2026-10-12T23:06:15+00:00

@VectorCrossProd I have a board I need to design and I thought I'd try your method... Seems more involved than I initially thought. Maybe I'll ask Claude to explain what's happening here haha
### Dorleen Sullivan ([@DorleenSullivan](https://x.com/DorleenSullivan/status/2110338356789809262)) — 2026-10-14T11:54:07+00:00

@VectorCrossProd Güç bütçesi + İNA226 okuması çok işime yarardı. Özellikle yük altı gerçek akım ve boşta/batarya voltajındaki düşüş, verimi de merak ediyorum.
### Austin Castorena ([@CastorenaA99618](https://x.com/CastorenaA99618/status/2109719607200346403)) — 2026-10-12T18:55:25+00:00

@VectorCrossProd This is really cool! About how long did it take to go from prompt to finished PCB? Did you have to step in much? Thanks for putting this video together, very cool.
### 1Broom ([@The1Broom](https://x.com/The1Broom/status/2109666361781682469)) — 2026-10-12T15:23:51+00:00

@VectorCrossProd How do you feed the board constraints and component footprints into the project context before the layout pass?
### Fuchiio ([@Fuchiio](https://x.com/Fuchiio/status/2109622236143669287)) — 2026-10-12T12:28:30+00:00

@VectorCrossProd Do you have an idea of cost per pcb design and duration of this process? Thanks for sharing pipeline!
### Hugo ([@hugospdx](https://x.com/hugospdx/status/2109669551994733049)) — 2026-10-12T15:36:31+00:00

@VectorCrossProd this is pretty cool.
### Dan Dermody ([@DanDermodyLLC](https://x.com/DanDermodyLLC/status/2109670763250782394)) — 2026-10-12T15:41:20+00:00

@VectorCrossProd Are you using any routing harnesses or letting Claude decide?

I pretty much have the same workflow letting Claude decide the routes.  1st order on the way now so I’ll see how it turns out!  

Love the video pipeline!
### ajax ([@adam_bicke16564](https://x.com/adam_bicke16564/status/2109644688546513169)) — 2026-10-12T13:57:43+00:00

@VectorCrossProd Fantastic work!
### Furt_Tech ([@furt_tech](https://x.com/furt_tech/status/2109654189852799051)) — 2026-10-12T14:35:28+00:00

@VectorCrossProd You me how cluade made a pcb and you watched.
### SixtusStella ([@SixtusStar](https://x.com/SixtusStar/status/2109675565481427260)) — 2026-10-12T16:00:25+00:00

@VectorCrossProd how do u make parts placements? AI too?

## Other returned timeline records

> The CLI did not expose reply relationships. These records do not start with a reply mention and were authored by someone other than the saved-post author. They may include recommendations or promoted posts; they are retained as source context, not verified replies.

### Constantin ([@canary_earth](https://x.com/canary_earth/status/2109668229790499207)) — 2026-10-12T15:31:16+00:00

Seems overly complicated. You can use Claude directly in EasyEDA Pro via an MCP server it sets up itself, and it is amazing at doing traces. The advantage is that it can pick components JLC actually has in stock. You can even tell it to prefer basic parts to save some cash on reel loading fees.
