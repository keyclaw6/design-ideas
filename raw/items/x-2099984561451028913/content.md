# New blog post: we had a million lines of Python to clean up — 1,393 subagents, 19 hours, 34.4% smaller

> Source: https://x.com/NousResearch/status/2099984561451028913
> Author: Nous Research (@NousResearch)
> Posted: 2026-09-15T22:11:49Z
> Stats (at capture): 1,495,941 views · 4,532 likes · 299 replies · 275 reposts · 1,875 bookmarks
> Captured: 2026-09-21T13:28:31Z

## Post

New blog post:

We had a million lines of Python to clean up. On September 2nd @Teknium asked Hermes Agent to do it. 

1,393 subagents and nineteen hours later, the codebase was 34.4% smaller, saving us nearly $2m in engineering hours.

https://nousresearch.com/refactoring-hermes-with-1393-agents

## Media

![](media/media_0.jpg)

## Author bio (at capture)

A bunch of nerds making progress

https://discord.gg/nousresearch

## Comments

299 replies on the original; 15 captured below via logged-in browser extract.

### Regi Kusumaatmadja @abdurrahmanregi · Sep 16 ([@abdurrahmanregi](https://x.com/abdurrahmanregi)) — [2100053778145612227](https://x.com/abdurrahmanregi/status/2100053778145612227)

2026-09-16T02:46:52.000Z

> i thought you were announcing rust rewrite 
> 1
> 213


### max guy  @GolerGkA · Sep 16 ([@GolerGkA](https://x.com/GolerGkA)) — [2100305328357220820](https://x.com/GolerGkA/status/2100305328357220820)

2026-09-16T19:26:26.000Z

> How did you end up with so much code?
> 57


### timur kharisov @normisdeath · Sep 16 ([@normisdeath](https://x.com/normisdeath)) — [2100281346622967864](https://x.com/normisdeath/status/2100281346622967864)

2026-09-16T17:51:09.000Z

> u didn't mention the original code repo was vibecoded as well, so it is slop based slop reduction
> 34


### Code and Covenant @codecovenant · Sep 16 ([@codecovenant](https://x.com/codecovenant)) — [2100006117187158270](https://x.com/codecovenant/status/2100006117187158270)

2026-09-15T23:37:29.000Z

> $20,000 in tokens. Yikes.
> 138


### Kash @karpathism · Sep 16 ([@karpathism](https://x.com/karpathism)) — [2100263036619485328](https://x.com/karpathism/status/2100263036619485328)

2026-09-16T16:38:23.000Z

> How many tokens did it cost?
> 1
> 46


### Jatin Garg @jatingargiitk · Sep 16 ([@jatingargiitk](https://x.com/jatingargiitk)) — [2099991355598795262](https://x.com/jatingargiitk/status/2099991355598795262)

2026-09-15T22:38:49.000Z

> Nearly $2m across roughly 344k removed lines is about $5.80 a line, which prices deletion at authoring rates. Human cleanup tends to move in whole modules, where one decision drops thousands of lines at once. Curious what baseline the estimate used.
> 2
> 346


### Justin Kalland @justinkalland · Sep 16 ([@justinkalland](https://x.com/justinkalland)) — [2100009896729366598](https://x.com/justinkalland/status/2100009896729366598)

2026-09-15T23:52:30.000Z

> $25k for 19 hours with an average of 218 subagents is cheap.
> 2
> 183


### Jed | Breed VC @JedBreed · Sep 16 ([@JedBreed](https://x.com/JedBreed)) — [2100014450719809930](https://x.com/JedBreed/status/2100014450719809930)

2026-09-16T00:10:36.000Z

> hermes making hermes better...compounding loops. well done 
> @Teknium
> 1
> 123


### Macro Bombastic @MacroBombastic · Sep 16 ([@MacroBombastic](https://x.com/MacroBombastic)) — [2099999032806342906](https://x.com/MacroBombastic/status/2099999032806342906)

2026-09-15T23:09:20.000Z

> 1,393 subagents is wild, I need this for my own backlog
> 1
> 46


### JJ @jeffreyajewett · Sep 16 ([@jeffreyajewett](https://x.com/jeffreyajewett)) — [2100017577753805241](https://x.com/jeffreyajewett/status/2100017577753805241)

2026-09-16T00:23:01.000Z

> Seems to align with Amdahl’s law. Eventually the scarce resource becomes verification?
> 1
> 54


### Nikolai Yakovenko @ivan_bezdomny · Sep 16 ([@ivan_bezdomny](https://x.com/ivan_bezdomny)) — [2100077761272455423](https://x.com/ivan_bezdomny/status/2100077761272455423)

2026-09-16T04:22:10.000Z

> very cool! thanks for the writeup
> 1
> 145


### 𝛼 @deeperflows · Sep 16 ([@deeperflows](https://x.com/deeperflows)) — [2099999462307381469](https://x.com/deeperflows/status/2099999462307381469)

2026-09-15T23:11:02.000Z

> Without the shadow of a doubt, 
> @Teknium
>  delivered.
>
> But how did you guys test non-regression ?
> 1
> 46


### Avenged Stoic @AvengedStoic · Sep 16 ([@AvengedStoic](https://x.com/AvengedStoic)) — [2100223800042508645](https://x.com/AvengedStoic/status/2100223800042508645)

2026-09-16T14:02:28.000Z

> One message within this message:  A new developer sets up his dev box for GIT, coding, debugging, and serving test builds.  
>
> In 2026, the human in the loop needs to plan the dev/test infrastructure for the swarms of AI devs, or they’ll do it themselves.. likely inefficiently.
> 2
> 155


### Adam · Arcyton @arcyton · Sep 16 ([@arcyton](https://x.com/arcyton)) — [2100053180839055767](https://x.com/arcyton/status/2100053180839055767)

2026-09-16T02:44:30.000Z

> 34.4% smaller is measurable; the number I would want beside it is behaviour held constant. Deleted code that was never called and deleted code that ran once a quarter look the same on a diff. How did you check the rarely-used paths?
> 1
> 167


### Arsh - 16 y/o builder @be_arsh · Sep 16 ([@be_arsh](https://x.com/be_arsh)) — [2100010623115612418](https://x.com/be_arsh/status/2100010623115612418)

2026-09-15T23:55:23.000Z

> 1393 subagents, 19 hours, and somehow none of them force-pushed to main. the blog is leaving out the best part
> 2
> 97


## Links

- https://nousresearch.com/refactoring-hermes-with-1393-agents
