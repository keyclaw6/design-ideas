# send this prompt to GPT-Astra, it might just change your life...

> Source: https://x.com/Av1dlive/status/2099948431511056875
> Author: Avid (@Av1dlive)
> Posted: 2026-09-15T19:48:15Z
> Stats (at capture): 343,333 views · 2,358 likes · 43 replies · 217 reposts · 5,385 bookmarks
> Captured: 2026-09-21T13:28:31Z

## Post

send this prompt to GPT-Astra, it might just change your life...

## Media

![](media/media_0.png)
![](media/media_1.png)
![](media/media_2.png)
![](media/media_3.png)

## Author bio (at capture)

I write, read and build | I normie-maxx | builder of agentic-stack (now on MacOS) | upcoming PhD student

## Quoted post

**Author:** Avid (@Av1dlive)
**URL:** https://x.com/Av1dlive/status/2099816833788567683
**Posted:** 2026-09-15T11:05:20Z
**Stats (at capture):** 423,516 views · 340 likes · 50 replies · 37 reposts · 749 bookmarks

i burned through my entire GPT-6 Astra weekly quota in 3 days

so i'm replacing my $200/mo Codex subscription with this...

a free 32,960-star GitHub repo that runs GLM-5.3 Flash, Kimi K3, and DeepSeek V4 Flash locally

[here's the exact setup i used:]

1. get colibri

download the release archive for Linux, macOS, or Windows. no compiler needed.

python3 coli info

2. or build it from source

git clone https://github.com/JustVugg/colibri
cd colibri/c
./setup.sh
cd ..

3. pick a model

GLM-5.3 Flash: 321B, ~195 GB converted, 25 GB RAM
DeepSeek V4 Flash: 284B, ~167 GB, or ~85 GB for the REAP 150B version
Kimi K3: 2.8T, ~1.6 TB snapshot, 32 GB+ RAM

none of them needs a GPU. a GPU only makes some runs faster.

4. get the weights

GLM-5.3 Flash uses the dedicated converter:

python3 tools/convert_glm53.py --outdir /nvme/glm53_i4 --min-free-gb 30

DeepSeek V4 Flash and Kimi K3 load from their original Hugging Face snapshots. pre-converted containers work too.

5. run it

COLI_MODEL=/nvme/glm53_i4 ./coli chat
./coli web --model /nvme/glm53_i4       # dashboard
./coli serve --model /nvme/glm53_i4     # headless API

6. tune it

./coli doctor   # readiness check
./coli plan     # RAM/VRAM/disk placement
./coli tune     # fastest safe profile

`coli` reads `config.json` and picks the right engine for each model.

the tradeoff is honest: no token bill, no hosted quota... but you need the storage.

the frontier moved from your subscription to your SSD.

Quoted-post media (saved locally):

![](media/qmedia_video_0_thumb.jpg)
[media/qmedia_video_0.mp4](media/qmedia_video_0.mp4)
Original: https://video.twimg.com/amplify_video/2099815443326525440/vid/avc1/1720x1080/HheQA2wvDd-7gPgb.mp4?tag=29

## Comments

43 replies on the original; 5 captured below via logged-in browser extract.

### Summit88 @summit88HQ · Sep 16 ([@summit88HQ](https://x.com/summit88HQ)) — [2100191799687942518](https://x.com/summit88HQ/status/2100191799687942518)

2026-09-16T11:55:19.000Z

> DM me for the full .md prompt
> 469


### alexandriemartinez @alexandriem7 · Sep 16 ([@alexandriem7](https://x.com/alexandriem7)) — [2100281054988792056](https://x.com/alexandriem7/status/2100281054988792056)

2026-09-16T17:49:59.000Z

> It won’t
> 91


### Billy Luca @rada_xy · Sep 15 ([@rada_xy](https://x.com/rada_xy)) — [2099949738141585725](https://x.com/rada_xy/status/2099949738141585725)

2026-09-15T19:53:27.000Z

> W prompt
> 1
> 1.3K


### justin @labsarentbad · Sep 16 ([@labsarentbad](https://x.com/labsarentbad)) — [2100294355625910404](https://x.com/labsarentbad/status/2100294355625910404)

2026-09-16T18:42:50.000Z

> I am building a brand and app for my students that i coach in golf. I currently am running something similar with a “Project Manager”, “Idea Guy”, and “Connection from Website to App” guy. I am very far along in it already and it’s already online and functioning, but do you think
> Show more
> 106


### joe @topdawg30000 · Sep 16 ([@topdawg30000](https://x.com/topdawg30000)) — [2100283966146461875](https://x.com/topdawg30000/status/2100283966146461875)

2026-09-16T18:01:33.000Z

> Can you make a prompt for my digital marketing agency
> 106


## Links

- https://x.com/Av1dlive/status/2099816833788567683
- https://github.com/JustVugg/colibri
