# I bet you didn't know that by default Codex only runs max 3 subagents concurrently. That's not ambitious enough for

> Source: https://x.com/daniel_mac8/status/2096634766883696666
> Author: Dan McAteer (@daniel_mac8)
> Posted: Sun Sep 06 16:20:56 +0000 2026
> Stats at capture: 543 likes / 36 reposts / 63 replies / 112356 views / 819 bookmarks
> Author bio at capture: I build AI agents for a living and write about it. Writing at http://attentionheads.blog · Writing @latentspacepod · Agentic Ops @ AnswerRocket

## Post

I bet you didn't know that by default Codex only runs max 3 subagents concurrently.

That's not ambitious enough for Astra.

OpenAI tested Astra with up to 64 subagents.

Copy this into your config.toml:

[agents]
max_concurrent_threads_per_session = 64

Astra orchestrating 64 Luna subagents in parallel is a sight to behold!

## Media

![](media/media_0.mp4)
Original: https://video.twimg.com/amplify_video/2096634632758538240/vid/avc1/2786x2014/WU21KUrliloqcZLC.mp4?tag=29

## Thread

### @daniel_mac8 — [2096634768452448381](https://x.com/daniel_mac8/status/2096634768452448381)

> I will say that it made the Codex UI a bit laggy.
>
> Probably overloading my CPU?

### @daniel_mac8 — [2096639194013515991](https://x.com/daniel_mac8/status/2096639194013515991)

> Worked for 19 mins and used 5% of my Pro 5x weekly limit on the task in the video.

### @daniel_mac8 — [2096637160682115231](https://x.com/daniel_mac8/status/2096637160682115231)

> Used 5% of my weekly limit on the task in the video working for 19 minutes.

### @daniel_mac8 — [2096640952513310971](https://x.com/daniel_mac8/status/2096640952513310971)

> Totally, you should always customize your agents to what suits you.
>
> It’s good to be aware of the upper limits, though.

### @daniel_mac8 — [2096674624553521609](https://x.com/daniel_mac8/status/2096674624553521609)

> Also viable, but I think in that case it won’t use the multi-agent v2 so you’re missing out on the native inter-agent communication.

### @daniel_mac8 — [2096762420303692267](https://x.com/daniel_mac8/status/2096762420303692267)

> Cheers my friend!

### @daniel_mac8 — [2096639823268168149](https://x.com/daniel_mac8/status/2096639823268168149)

> That’s for you to decide!

### @daniel_mac8 — [2096683297938055557](https://x.com/daniel_mac8/status/2096683297938055557)

> Not sure but that would be a great thing to test!

## Comments

### @altryne — [2096674072545689715](https://x.com/altryne/status/2096674072545689715)

> Why not ask it to spin up codex sessions instead? they are easier to interact with and see, and there's no limit

### @AIadventure3 — [2096639429171384772](https://x.com/AIadventure3/status/2096639429171384772)

> but does 64 luna sub agents produce better work than 1 astra agent on low?

### @jonkragh — [2096681532324725145](https://x.com/jonkragh/status/2096681532324725145)

> does it choose luna without any manual guidance?

### @juminoz — [2096640563240169943](https://x.com/juminoz/status/2096640563240169943)

> For most people, they don’t need more than 4-8. You should also setup the specs for named agents so they are predefined with exact models, etc, so you don’t even up with only Luna, etc when you forget to be specific.

### @kcosr — [2096682705953931621](https://x.com/kcosr/status/2096682705953931621)

> Just a warning, don't ask it to make use of the full pool or it will invent work for them to do to satisfy your request. Just make it available.

### @barnc0re — [2096678916878713337](https://x.com/barnc0re/status/2096678916878713337)

> That's not true, my Codex ran 5 subagents today and I never changed any settings so it must be default

### @neslyio — [2097039153028268395](https://x.com/neslyio/status/2097039153028268395)

> in my case codex by default runs up to 6 subagents concurrently, not 3

