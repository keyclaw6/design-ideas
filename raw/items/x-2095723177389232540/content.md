# A lot of people are asking how I pulled off these super long-horizon builds with Astra.  Astra is extremely powerful,

> Source: https://x.com/mattshumer_/status/2095723177389232540 — @mattshumer_ (Matt Shumer) — posted Fri Sep 04 03:58:36 +0000 2026 — likes 4282 · reposts 271 · replies 182 · views 579463 (at capture)

> Author bio: AI whisperer. Investor in @GroqInc @Etched @Rork @DaytonaIO @OpenRouter + more. Prev: CEO @HyperWriteAI | AI @AlphaSchool  Press: mattshumermedia@gmail.com

## Post

A lot of people are asking how I pulled off these super long-horizon builds with Astra.

Astra is extremely powerful, but by default it struggled with a task this difficult. I tested a bunch of approaches to get past this, and the one I landed on is something I'm calling the Manager Loop.

It's basically a couple of tricks we used to use with much less capable models a couple of years ago, with a few new ideas layered on top. Turns out that when you put those together and apply them to Astra, its ability to do extremely difficult long-horizon tasks goes up dramatically.

Here's how it works:

1. Launch an agent (I'm calling this one the "manager"). Chat with it about what you want to get done, and have it build a massive checklist of to-dos, then break that checklist into phases.

2. The manager then spawns a second Codex agent in a separate thread (the "implementer"). The two agents can message each other.

3. Put the manager in /goal mode, and tell it to run each phase on the implementer in /goal mode.

4. The manager messages the implementer: "/goal Complete phase one completely, extremely well." The implementer doesn't stop until that phase is done, then messages the manager back. The manager tells it to start phase two. They repeat until every phase is finished, completely autonomously.

Why I think this works: over a long-horizon task, Astra tends to asymptote. It gets way further than previous models, but at a certain point it kind of just stops improving against the goal as quickly as it did before. It gets stuck in the minutiae, focusing way too much on small details, and overall progress stalls. The Manager Loop forces it to work piecemeal, one phase at a time. It's essentially how a human would steer a model, except the model is doing the steering for me.

That's actually how this started. I was having the model write the checklist and break it into phases, and then I was doing the manager's job by hand. At some point I thought, "Wait, why can't I just get a separate AI to do this?" That's what unlocked full autonomy, which is super useful.

A wording detail that seemed to matter: I ask for each phase to be done "extremely well," not "perfectly." Maybe I'm reading too much into it, but asking for "perfect" sent the model right back into the minutiae. "Extremely well" implies it's allowed to move on once it's good enough, and that worked better in my testing.

One more trick that I think helps (this one is more of a hunch, but it was useful for me): have the implementer build a simple HTML page with the full checklist on it. The implementer checks boxes off as it goes and updates a counter, and the page has a chart of # of boxes ticked over time.

Obviously the boxes aren't all equal, but it forces the model to notice things like "I haven't made progress in a while, time to move on." You can even put this in the prompt directly, like: "if you haven't ticked a box in X amount of time, move on". That helps a lot.

I also ran 96 sub-agents at a time. You can change this in your Codex config (or just ask Codex to change it).

This got me far better long-horizon performance than anything else I tried. I'll be sharing more in the coming days!

## Media

![](media/quoted-video.mp4)
Original (video): https://video.twimg.com/amplify_video/2095609426770010113/vid/avc1/1920x1080/6pvMd9KDllohZyDg.mp4?tag=29

![](media/quoted-thumb.jpg)
Original (thumbnail): https://pbs.twimg.com/amplify_video_thumb/2095609426770010113/img/muj5Lvx5A_wdP3Wh.jpg

## Quoted post

[@mattshumer_ (Matt Shumer)](https://x.com/mattshumer_/status/2095609734845927525) — posted Thu Sep 03 20:27:49 +0000 2026 — likes 18934 · reposts 1009 · replies 577 · views 4603031 (at capture)

> GPT-6 Astra built this Manhattan world in Unreal Engine over the course of a week.
>
> It was literally able to go street by street to make each one perfect.

## Thread

### @mattshumer_ — [2095724719408386326](https://x.com/mattshumer_/status/2095724719408386326)

> I ran out of time to keep improving the Manager Loop, but there are a couple obvious next steps. Haven't tested these yet:
>
> - The implementer's context still grows across phases, so I'd expect the asymptoting to creep back in late in a big task. Have the manager spin up a fresh implementer per phase with a written handoff or something (or have the new implementer read the previous' traces).
>
> - The plan is written before any work starts, so some of it will be wrong. The implementer should be able to propose changes, and the manager decides whether to accept them. Or vice versa, I don't know!

### @mattshumer_ — [2095724925952671794](https://x.com/mattshumer_/status/2095724925952671794)

> @udiWertheimer Names are helpful

### @mattshumer_ — [2095729774064734567](https://x.com/mattshumer_/status/2095729774064734567)

> @SEO I didn’t have a ton of success with gauntlet loops with Astra, unfortunately.
>
> It often got really stuck on over-optimizing and never moving on.

## Comments

### @takesonai — [2095753706968850471](https://x.com/takesonai/status/2095753706968850471)

> @mattshumer_ "we used to use with much less capable models a couple of years ago"
> Like 4 or 5 years ago? https://x.com/takesonai/status/2095753706968850471/photo/1

### @doodlestein — [2095726748096745608](https://x.com/doodlestein/status/2095726748096745608)

> This is pretty similar to my Agent Flywheel approach except that uses beads for the todo list and used a big swarm of full-fledged agent instances controlled using ntm by the manager, with all of them communicating via MCP Agent Mail. The benefit there is that you can mix any agents and models and get the diversity of thought in the reviews.

### @Trace_Cohen — [2095798249298776308](https://x.com/Trace_Cohen/status/2095798249298776308)

> @mattshumer_ Basically your own little corporation with middle managers, managing the actual workers trying to get them to do their job well. Matrix feeling…
>
> Next try performance reviews after and see how that goes 😅

### @jphilipp — [2095787896649273545](https://x.com/jphilipp/status/2095787896649273545)

> @mattshumer_ Cool. I wonder in terms of orientation and perfection what goal statements like the following would do: "Focus on what people playing it would care about, what makes it fun and viral, and what gets the game or app sold (don't necessarily focus on what's right or perfect)."

### @camsoft2000 — [2095796494766846317](https://x.com/camsoft2000/status/2095796494766846317)

> @mattshumer_ This is similar to using voice agent, if you give it a task it will set a goal and the manage other agents until the goal is complete. The task list is a key ingredient here. There are many ways to achieve this and you don’t need a custom harness or even a skill.

### @DamionL13 — [2095724746163814870](https://x.com/DamionL13/status/2095724746163814870)

> @mattshumer_ I have been using a similar workflow for my "studio". Each seat is assigned a specific lane (sim, content, engine, characters, world art, audio, QA, infra) who are all managed by the project coordinator. I was having similar issues and have noticed an exponential improvement.

### @nudevise — [2095809480734695724](https://x.com/nudevise/status/2095809480734695724)

> @mattshumer_ i made something similar in june with Claude, its called the Thorough Twins  skill and i have them do something called Ping Ponging where they message each other and will literally fight all bugs to the death in a hell-in-a-cell fashion, whilst crafting in a /goal

### @alexzenciks — [2095811458936267238](https://x.com/alexzenciks/status/2095811458936267238)

> @mattshumer_ interesting - i run it in a very similar way, but my "manager" is a game director that i discuss creative vision with, have requirements, and then it decides what kind of work needs to be done by spawning subagents with /goal or /loop

### @paul_sousa79 — [2095831391279693892](https://x.com/paul_sousa79/status/2095831391279693892)

> @mattshumer_ Sounds like you just applied SDLC methods to your harness (not dismissing the approach).  Would a separate eval agent help do you think?  Or is the work small enough that the /goal loop handles that within a reasonable context window?

### @udiWertheimer — [2095724020062683364](https://x.com/udiWertheimer/status/2095724020062683364)

> @mattshumer_ this morning i asked astra to find a loop that matt shumer wouldn't name
>
> it thought for a few minutes and then all of the data centers went down

### @lgandecki — [2095776226593960249](https://x.com/lgandecki/status/2095776226593960249)

> @mattshumer_ This is great. Did you basically have unlimited tokens? Any idea how much usage did this use?

### @j_magnusson — [2095808649826386091](https://x.com/j_magnusson/status/2095808649826386091)

> @mattshumer_ Extremely impressive.
>
> It is also comforting to see that you guys are struggling with the same issues as the rest of us, with the agents disappearing down rabbit holes.
