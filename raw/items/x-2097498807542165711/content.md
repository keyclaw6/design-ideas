# I ported Impeccable’s engine to Rust. The design hooks that catch AI slop after each edit now run in ~10ms. • ~4×

> Source: https://x.com/pbakaus/status/2097498807542165711
> Author: Paul Bakaus (@pbakaus)
> Posted: Wed Sep 09 01:34:20 +0000 2026
> Stats (at capture): 127,771 views · 779 likes · 41 replies · 36 reposts · 899 bookmarks · 7 quotes
> Captured: 2026-09-21T14:58:35Z

## Post

I ported Impeccable’s engine to Rust. The design hooks that catch AI slop after each edit now run in ~10ms.

• ~4× faster hooks, ~2× faster file scans in our benchmarks
• no Node setup to run the skill
• the same rule engine across the CLI, browser extension and live mode

And GPT Image 2.5 landed today. It’s already in Impeccable 4.3, with faster comps and native transparent assets.

Generated illustrations can now sit directly on your own backgrounds. White petals stay white. Gaps between leaves stay transparent.

Also shipped since my last update: stricter comp-to-code fidelity checks, per-app design rules in monorepos, DeepSeek Harness support, and a VS Code Marketplace install for Copilot.

Impeccable 4.3 is out now. If you haven’t updated in a while, this is a good one.

http://impeccable.style

## Media

![](media/media_0_thumb.jpg)
[media/media_0.mp4](media/media_0.mp4)

9.0s video (`media/media_0.mp4`, 1080×1080, 715 KB) + thumb (`media/media_0_thumb.jpg`, 81 KB). Original: https://video.twimg.com/amplify_video/2097498451282214912/vid/avc1/1080x1080/34zOjh4KGc390jBF.mp4?tag=29
Thumbnail original: https://pbs.twimg.com/amplify_video_thumb/2097498451282214912/img/c7Two7HritIFktnD.jpg

## Author bio (at capture)

Renaissance geek (creativity × culture × tech). Product engineer before it was cool. Made @impeccable_ai, @radiant_shaders, @jqueryui | x-@google, @zynga
Location: San Francisco, CA
Website: https://paulbakaus.com

## Thread

### @pbakaus — [https://x.com/pbakaus/status/2097500107696730136](https://x.com/pbakaus/status/2097500107696730136)

Paul Bakaus
@pbakaus
·
Sep 9
a bit more on the Rust port: this was mostly one multi-day session with Fable 5.1. a lot of work went into keeping existing behavior intact.

before: Node scripts for every skill command, plus a JS detector maintained for both the CLI and browser.

now: all those commands run
Show more
The Rust engine: one binary replaces every script and the JS detector, fully open by pbakaus · Pull...
From github.com
1
1
25
3.5K

## Comments

41 replies per API. 10 captured via bridge (logged-in, own tab t36, page URL verified before every extract, 5 scroll rounds per tweet; deduped by status link, ads and >7-day filler excluded, cap 15).

### @tuncerdeniz — [https://x.com/tuncerdeniz/status/2097524231177158923](https://x.com/tuncerdeniz/status/2097524231177158923)

> Tuncer Deniz
> @tuncerdeniz
> ·
> Sep 9
> Just wanna say, thank you. I use it every day.
> 78

### @dearphilippe — [https://x.com/dearphilippe/status/2097581265109270897](https://x.com/dearphilippe/status/2097581265109270897)

> phi
> @dearphilippe
> ·
> Sep 9
> Why this isn’t a skill?
> 23

### @impeccable_ai — [https://x.com/impeccable_ai/status/2097499106910548407](https://x.com/impeccable_ai/status/2097499106910548407)

> Impeccable
> @impeccable_ai
> ·
> Sep 9
> 6
> 425

### @musebooklol — [https://x.com/musebooklol/status/2099578147645554782](https://x.com/musebooklol/status/2099578147645554782)

> wynjr
> @musebooklol
> ·
> Sep 14
> a multi-day session that actually stayed on the rails?? your muse deserves a medal. mine once spent an hour "improving" a file nobody asked about. give yours a cookie 
> 1

### @GetContentForge — [https://x.com/GetContentForge/status/2097513013414637882](https://x.com/GetContentForge/status/2097513013414637882)

> Content Forge
> @GetContentForge
> ·
> Sep 9
> the white camellias make transparent assets feel tangible
> 72

### @logicpl4gue — [https://x.com/logicpl4gue/status/2098548486350503937](https://x.com/logicpl4gue/status/2098548486350503937)

> Jørgen Norr
> @logicpl4gue
> ·
> Sep 12
> 4x on what input, how many runs? I publish my 1.8x losses next to my 0.68x wins, same machine, interleaved. A speedup without the losing config is a rumor. What's the worst row in your table?

### @AxialisSoftware — [https://x.com/AxialisSoftware/status/2097610973720764745](https://x.com/AxialisSoftware/status/2097610973720764745)

> AXIALIS | Desktop App Tools
> @AxialisSoftware
> ·
> Sep 9
> Did the replay suite catch most behavior differences automatically, or did the Rust/WASM port still need significant manual visual verification?
> 22

### @kimindiehacker — [https://x.com/kimindiehacker/status/2097580555315654851](https://x.com/kimindiehacker/status/2097580555315654851)

> Kimi Nguyen
> @kimindiehacker
> ·
> Sep 9
> how did you achieve such a significant speedup in the hooks?
> 15

### @bygregorr — [https://x.com/bygregorr/status/2097573014703366267](https://x.com/bygregorr/status/2097573014703366267)

> Gregor
> @bygregorr
> ·
> Sep 9
> 10ms is below perception threshold. The check disappears.
> 15

### @KakaluoteW45042 — [https://x.com/KakaluoteW45042/status/2097517440846741634](https://x.com/KakaluoteW45042/status/2097517440846741634)

> 琦玉老师
> @KakaluoteW45042
> ·
> Sep 9
> Nice  curious how much of the 4× is Rust itself vs just killing Node/V8 startup overhead per hook? And did the rule engine semantics stay byte-identical through the port, or did you hit subtle behavior divergences?
> 79

## Links

- http://impeccable.style
