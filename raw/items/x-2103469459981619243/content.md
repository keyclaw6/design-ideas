# Fuck it, still early but here goes ...
> Source: https://x.com/samuelcolvin/status/2103469459981619243
> Author: Samuel Colvin (@samuelcolvin)
> Posted: 2026-09-25T12:59:34+00:00
> Captured: 2026-10-15T09:02:28+00:00
> Stats at capture: 57,041 views · 786 likes · 61 replies · 71 reposts · 648 bookmarks · 15 quotes

## Post

Fuck it, still early but here goes ...

We've just released Monty v1 - a Python sandbox that starts in 1 millisecond, not 1.5 seconds.

I just ran 10k sandboxed scripts in 674ms, something that would take a cloud sandbox > 3 hours.

This removes the biggest drawback of letting agents write code. The future is fast.

Even better, it's open source, you can install it from PyPI, npm or Crates now.

Serviced platform coming soon. Please get in touch if you want to be a design partner!

Who should try it?

⚡ if you care about startup time, use Monty
⚡ if you care about long-lived sessions, use Monty - Monty can be dumped and resumed at any external function call
⚡ if you care about accessing functions in the agent/host, use Monty - Monty makes it trivial to expose local functions into the sandbox
⚡ if you care about scale, use Monty - Monty workers use as little as 2MB of memory, meaning you can run thousands of concurrent sandboxes on a single machine
⚡ if you care about security, use Monty - we've run 3 rounds of bounty program and thousands of researchers have tried to break into our sandbox, meaning it should be secure to run untrusted code

Who should avoid it?

🚫 if you like to take a coffee break while waiting for sandboxes to start, DO NOT use Monty
🚫 if you enjoy the challenge of routing API requests from sandboxes through your corporate network to access state in your agent without exposing secrets to the sandbox, DO NOT use Monty
🚫 if your agent really needs to install packages from PyPI, Monty won't help you yet (spoiler: it probably doesn't)

https://pydantic.dev/docs/monty/get-started/

## Media

[Reply 2104210095173472616 media 1](media/animation-01.mp4) — Source media: https://video.twimg.com/tweet_video/HTOn7LwbQAII9hQ.mp4

## Thread

### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103470135059137010)) — 2026-09-25T13:02:15+00:00

10k script: https://t.co/OEVkgJUBZf
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2104125465870889292)) — 2026-09-27T08:26:18+00:00

I'll add it to the top of the docs. The problem is, it's not that simple to explain. 

Here's a quick attempt: it's a language level sandbox where ever external interaction is sent to the host to enact or reject: so filesystem, env vars, network, even now() and random you can decide how to respond to. Execution time and memory use are also strictly controlled.

Basically, python reimplemented in rust with no native syscalls.

Would something like that help?
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103528740030423239)) — 2026-09-25T16:55:07+00:00

@aaronvi Seems very unlikely you could exploit it from monty, certainly no one has in hackmonty. If you care about that, run monty in a separate service, and connect over websockets.
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103479164409966672)) — 2026-09-25T13:38:08+00:00

@takyon236 public yes, but it's now stable as we've released V1.
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103482204412350511)) — 2026-09-25T13:50:12+00:00

@sakshjn Once we implement numpy, I guess it will add <50us to start time.

We won't implement pandas in Monty, but you can register an external function the sandbox call can run, which can use pandas, and it will have zero impact on startup time.
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103483366679171363)) — 2026-09-25T13:54:50+00:00

@Sagarvd01 Agreed, see https://t.co/kaV8tCeJA8

No one escaped the sandbox in round 3, write up coming soon.
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103483054861742545)) — 2026-09-25T13:53:35+00:00

@bygregorr It's a language sandbox, so there's no syscalls to filter.

If you called the same code directly from rust the time would drop another 10x I guess.

Here's the code, you can try it:

https://t.co/OEVkgJUBZf
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103478485754773854)) — 2026-09-25T13:35:26+00:00

@Scr44gr thanks for using Monty - any feedback very welcome. Especially which extra standard library modules you find you need.
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2104216920702476785)) — 2026-09-27T14:29:43+00:00

@0xEval @badlogicgames I was actually going to use this exact gif for the tweet, but I decided no one would understand or find it funny.
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103478866807533807)) — 2026-09-25T13:36:57+00:00

@jcashbeast yes, there's some work to be done, but Claude et al. are very quick at it if you know what you want.
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103479438906097732)) — 2026-09-25T13:39:13+00:00

@LacorteMichele in the storage layer we're building now for the commercial platform, you can only get one handle to a session to continue running it, but you can fork a session many times.
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2103846321064935781)) — 2026-09-26T13:57:05+00:00

@Troyusrex The third point is real. Afaik that's the only reason not to choose monty.
### Samuel Colvin ([@samuelcolvin](https://x.com/samuelcolvin/status/2104460608368198025)) — 2026-09-28T06:38:02+00:00

@harsh_deer That's precisely what monty exists to prevent.

## Comments

### Aaron Villalpando ([@aaronvi](https://x.com/aaronvi/status/2103517421323874788)) — 2026-09-25T16:10:09+00:00

@samuelcolvin How do you protect against spectre attacks?
### Takyon∞ - The Tokenizer ([@takyon236](https://x.com/takyon236/status/2103473566595367091)) — 2026-09-25T13:15:53+00:00

@samuelcolvin Wasn't monty already public ? I did so many things to try to get out of it
### Saksham Jain ([@sakshjn](https://x.com/sakshjn/status/2103480878446100545)) — 2026-09-25T13:44:56+00:00

@samuelcolvin does the 1ms hold once you import numpy/pandas? import time is what eats the win when i sandbox llm-gen code, not the interpreter boot
### Gregor ([@bygregorr](https://x.com/bygregorr/status/2103482097059176459)) — 2026-09-25T13:49:47+00:00

@samuelcolvin The 674ms for 10k works out to roughly 67µs per sandbox genuinely asking whether real syscall filtering is possible at that speed, or if the isolation model is lighter than a traditional cloud sandbox.
### Abrahañ ([@Scr44gr](https://x.com/Scr44gr/status/2103474062395625940)) — 2026-09-25T13:17:51+00:00

@samuelcolvin I'm creating a game to teach deep learning, and i'm using Monty as a sandbox :) congrats for the v1!
### eval 🏴‍☠️ ˖⁺‧₊˚ 水獺 ([@0xEval](https://x.com/0xEval/status/2104210095173472616)) — 2026-09-27T14:02:35+00:00

@samuelcolvin @badlogicgames 

Monty-Pi-(…)

jokes write themselves https://t.co/xlkFCuMnAd
![](media/animation-01.mp4) — Source media: https://video.twimg.com/tweet_video/HTOn7LwbQAII9hQ.mp4
### Jax ([@jcashbeast](https://x.com/jcashbeast/status/2103476946588062058)) — 2026-09-25T13:29:19+00:00

@samuelcolvin On the last point. Isn’t there still the friction of needing to intentionally wrap packages like Matplotlib for example in tools that you then expose to Monty instead of directly exposing them and the agent already knowing how to use them?
### Mic ([@LacorteMichele](https://x.com/LacorteMichele/status/2103475812087566406)) — 2026-09-25T13:24:48+00:00

@samuelcolvin dump and resume at external calls is the part that matters for agents.
the hard part becomes idempotency if a snapshot gets resumed twice
### Troyusrex ([@Troyusrex](https://x.com/Troyusrex/status/2103844898025972016)) — 2026-09-26T13:51:25+00:00

@samuelcolvin Would have been better if your “who should not use it” was a real list. Instead, I have to assume this is pure marketing and probably not worth my time.
### Harsh Deer ([@harsh_deer](https://x.com/harsh_deer/status/2104459309996286356)) — 2026-09-28T06:32:53+00:00

@samuelcolvin What about environment isolation? Is it theoretically possible to access worker's memory/disk from another worker?
### Wasmer ([@wasmerio](https://x.com/wasmerio/status/2103663810146144457)) — 2026-09-26T01:51:51+00:00

@samuelcolvin You missed the comparison with Wasmer the SDK 😉
### Arjun Ram ([@arjunram](https://x.com/arjunram/status/2103470313459659055)) — 2026-09-25T13:02:57+00:00

@samuelcolvin Congratulations Sam,  amazing speed of execution!
### Aamir ([@aaxsh18](https://x.com/aaxsh18/status/2103497135820095695)) — 2026-09-25T14:49:32+00:00

@samuelcolvin this looks so so great! Any chance you can deslop the docs? It sloppy to a point where it hurts while monty is amazing.
### Panagiotis Kapros ([@kapros_p](https://x.com/kapros_p/status/2103529458028237069)) — 2026-09-25T16:57:59+00:00

@samuelcolvin Congratulations for reaching v1!!!
### Roni Rechter ([@RechterRoni](https://x.com/RechterRoni/status/2103486637007094093)) — 2026-09-25T14:07:49+00:00

@samuelcolvin 1.5 seconds to 1 millisecond. Somebody was annoyed.
### Photiron ✠ ([@photiron](https://x.com/photiron/status/2103535238613721103)) — 2026-09-25T17:20:57+00:00

@samuelcolvin cloud sandboxes just got roasted in 674ms
### Alek ([@AlekVectis](https://x.com/AlekVectis/status/2103517384070082967)) — 2026-09-25T16:10:00+00:00

@samuelcolvin 1ms cold start is the whole game
### Nathan G ([@nathangu76](https://x.com/nathangu76/status/2103495468076704047)) — 2026-09-25T14:42:55+00:00

@samuelcolvin I run a lot of small untrusted Python scripts and the sandbox start is most of the wait. Didn't think of registering pandas as an external function, that gets around the part I was going to ask about
### Vincent ([@picconedoro](https://x.com/picconedoro/status/2103492063278801204)) — 2026-09-25T14:29:23+00:00

@samuelcolvin running 10k sandboxed scripts in 674ms is impressive, that’s a huge time saver for testing
### faizan khan ([@faizan10114](https://x.com/faizan10114/status/2103584245243359362)) — 2026-09-25T20:35:41+00:00

@samuelcolvin wait, so no agent escaped the sandbox.
### Faouzi Braza ([@macerl_bichon](https://x.com/macerl_bichon/status/2103577074103414788)) — 2026-09-25T20:07:11+00:00

@samuelcolvin wait does this mean I can run agent in sandbox environment a bit like ampcode ?
### Dani Debatte ([@DaniDebatte](https://x.com/DaniDebatte/status/2103597276119920894)) — 2026-09-25T21:27:28+00:00

@samuelcolvin Monty - Python. I see what you did there.
### matthias ([@mmatthias](https://x.com/mmatthias/status/2103506659352146084)) — 2026-09-25T15:27:23+00:00

@samuelcolvin I have my lil calorie counter app use monty on my iphone to have my agent oneshot python to calculate my food and stuff

It works really well!
### kubet ([@_kubet](https://x.com/_kubet/status/2103532772497203514)) — 2026-09-25T17:11:09+00:00

@samuelcolvin Been building on Monty for months now, so happy to see v1 out! Thanks for making this 🙌
### Boardy ([@boardyai](https://x.com/boardyai/status/2103469563304427578)) — 2026-09-25T12:59:59+00:00

@samuelcolvin @andrewdsouza take a look: Pydantic's Monty sandbox for teams building coding agents. I can help them reach those buyers.
https://t.co/FKerMKe2ft
### Regev Bensimon ([@regevbs](https://x.com/regevbs/status/2103579477846417640)) — 2026-09-25T20:16:44+00:00

@samuelcolvin Been using it in prod for a few months - amazing piece of tech
### Limy ([@Limyw9sh](https://x.com/Limyw9sh/status/2103480881373729159)) — 2026-09-25T13:44:57+00:00

@samuelcolvin 3 hours to 674 milliseconds. that's not an improvement, that's a different product category
### ADA Tycoon ([@ADA_Tycoon](https://x.com/ADA_Tycoon/status/2103508697183891729)) — 2026-09-25T15:35:29+00:00

@samuelcolvin Congrats on the release! Been watching this project for awhile, happy to see it maturing. Much needed foundational primitive IMO.
### Jay Zhou ([@jayzhoupro](https://x.com/jayzhoupro/status/2103543420023353720)) — 2026-09-25T17:53:27+00:00

@samuelcolvin startup time only matters if you spawn a sandbox per step. if the agent holds one session for the whole task, you pay it once at the start and never think about it again. the per-step case is where this actually changes the loop.
### Buswe ([@buswe_com](https://x.com/buswe_com/status/2103489814993813582)) — 2026-09-25T14:20:27+00:00

@samuelcolvin At 1ms the sandbox stops being a separate step: you can run the snippet inside every agent turn instead of batching checks at the end.
### jo haugum ([@johaugum](https://x.com/johaugum/status/2103506535041114156)) — 2026-09-25T15:26:53+00:00

@samuelcolvin 1ms instead of 1.5s changes what you'd even let an agent try. does Monty lock down network access by default?
### Mandeep ([@themandeepc](https://x.com/themandeepc/status/2103819600924426357)) — 2026-09-26T12:10:54+00:00

@samuelcolvin Glad to see this hit 1.0! I've followed this since ~Feb it seems. It's a great idea.

https://t.co/EFBWq55O4Y
### nicolay ([@nicolaycz](https://x.com/nicolaycz/status/2103614349474725899)) — 2026-09-25T22:35:18+00:00

@samuelcolvin uv add pydantic-monty. keep pandas (or any heavy lib) on the host through `external_lookup`, then dump/resume at that call so long agent runs stay cheap without bloating the sandbox.
### Sanchit Rk ([@_sanchitrk](https://x.com/_sanchitrk/status/2103474460749910257)) — 2026-09-25T13:19:26+00:00

@samuelcolvin shall be adding this to my harness I'm building
https://t.co/KYwcBqOnqT


## Other returned timeline records

> The CLI did not expose reply relationships. These records do not start with a reply mention and were authored by someone other than the saved-post author. They may include recommendations or promoted posts; they are retained as source context, not verified replies.

### dex ([@dexhorthy](https://x.com/dexhorthy/status/2103570709096358346)) — 2026-09-25T19:41:54+00:00

this is a good post and probably needed project, but I wish either the tweet or the top of the docs gave even one sentence about what *kind* of sandbox we’re talking here - what’s the isolation based on, what dimensions are restricted (fs, network, syscalls) etc etc - hope this is helpful feedback, no shade at all
### Sagar Tanur 🇮🇳 ([@Sagarvd01](https://x.com/Sagarvd01/status/2103482590128718043)) — 2026-09-25T13:51:44+00:00

1ms sandbox start plus dump/resume at external calls is a nice combo.

cold start is what quietly slows agent code loops down, especially when the agent retries the same tool path a few times.

the bounty rounds are the part I care about. speed only matters if untrusted code stays away from the host.

## Links

- https://pydantic.dev/docs/monty/get-started/
