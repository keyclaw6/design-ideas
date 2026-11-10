# Negative Parallelism: The biggest culprit that makes claude "sound like an LLM" (I definitely didn't use Claude to write this)

> Source: https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/
> Author: u/out-of-phase
> Posted: 2026-10-11T15:36:49+00:00
> Captured: 2026-10-15T08:55:18+00:00
> Score: 141 · Comments: 22
> Community: r/ClaudeCode

## Post

I want to talk about the most recognizable tic in LLM writing, and I want to keep this simple. No jargon. No hype. No 4,000-word Medium essay that opens with a Marcus Aurelius quote and closes with a link to book a "free discovery call." Just the pattern, and how to get rid of it.

You've seen it even if you don't know the name. The model makes a positive statement, stacks a few negatives under it, and sometimes lands on one last positive to close things out:

>She'd finally learned to live simply. No car. No TV. No smart fridge that texts her about expired yogurt while she's at her nephew's recital. Just books. Tea. Quiet.

Once you see it, it's everywhere.

# How to spot it

There are three tells.

**• The stack of "No"s:** It's almost always "No X," rarely "Not X." Three in a row is standard. Four if the model is feeling something.

**• One oddly specific item:** Somewhere in the stack, one negative gets wildly more detail than the others. The car and the TV get two words each, and then suddenly there's a fridge, a nephew, and a recital. That item is the fingerprint.

**• The closing "Just.":** Optional, but common. A short positive, often followed by one or two single-word fragments for rhythm. Clean. Simple. Earned.

**• (Separate but related:) Excessive colons and emoji bullet lists:** This got so bad that some frontier providers started adding a UI toggle to control it. No quiet change. No system prompt rewrite.

**• (Separate but related:) Using the adverbs "Quietly" and "Silently":** LLMs have been quietly adding the word "quietly" in writing everywhere since the beginning. 

# Why it happens

The model wants to sound grounded and decisive, and the pattern delivers that instantly. No hedging. No qualifiers. No "it depends," which is the honest answer to roughly every question anyone has ever paid a consultant to answer. Just confidence. Rhythmic. Final.

# 1. Name the pattern explicitly

"Write naturally" won't cut it. The model can't avoid a pattern you never described, so describe it. Here's the block I use in my system prompt:

    Avoid negative parallelism: a positive statement followed by a stack
    of "No X." fragments, often ending with "Just Y.": State the point once,
    in full sentences. This is a hard requirement. No exceptions. No "just
    this once." No quietly swapping "No" for "Zero" or "Without" and assuming I
    won't notice.

# 2. Explain why

Models follow reasons better than rules, so give it the reason: the stack describes things nobody asked about. Nobody read "No flashy cars" and thought "oh thank god, I was so worried about the cars." It's padding dressed up as precision. No new information. No real contrast. Just rhythm.

# 3. Show it what to do instead

The fix is almost always deletion. Take the example above, keep the first sentence, and fold in anything that actually matters: "She'd finally learned to live simply, mostly reading and drinking tea." That's it. No list. No drumroll. No dramatic pause like a reality show host waiting for the music to swell before telling someone they're going home. Just the sentence.

# 4. Don't overcorrect

Lists are fine. If you're writing a spec, "No external dependencies" is actual information. No need to ban the word. No need to grep every output. No need to write a regex that flags every "No" and then lose a Saturday arguing with it about whether "No problem" counts. Just quiet awareness.

# Results

My outputs are tighter now. Quieter. No filler. No fake drama. No paragraphs that read like a minimalist influencer describing their one (1) linen shirt and the ceramic mug a Kyoto artisan made for them after a "really honest conversation." Just clean prose. Direct. Human. Silently.

Hope this helps silently someone:

**•** No pressure. 

**•** No obligation. 

Just sharing.

**TL;DR:** Name the pattern, explain why it's bad, show the fix. No more stacks. No more "Just." No more sentences that end like a cologne commercial.

**Edit:** For anyone who wants to go deeper, [feel free check out how I made $1B prompting LLMs](https://billion-dollar-company.vercel.app). No fluff. No upsell. No 14-email drip sequence that opens with "Quick question 👀" and ends with a $1,997 "Prompt Mastery Accelerator" that's 40% off for the next 6 hours. Just value. 

**Obligatory discussion-starter / "Question" that I think somehow makes this thinly-veiled self-promotion feel authentic:** 

Agree? Disagree? I'm genuinely curious: what's the one LLM writing habit you've trained out of your models that nobody talks about? 👇

## Thread

> u/AutoModerator · 2026-10-11T15:36:50+00:00 · score 1 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pf9e16s/)

Hey! Thanks for posting to r/ClaudeCode 

While participating in this thread, please follow our [community rules](https://www.reddit.com/r/ClaudeCode/about/rules). Keep discussions constructive. Attack the idea, not the person.

## For help, project discussions, tips, and general chat, join the [ClaudeCode Discord](https://discord.gg/4QbtMRErUc).


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/ClaudeCode) if you have any questions or concerns.*

## Comments

> u/SomeTwelveYearOld · 2026-10-12T02:56:31+00:00 · score 70 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfdh3wm/)

Nice touch of adding them in every paragraph. Not just the intro. Not just the example. 

> u/robertbowerman · 2026-10-12T09:09:23+00:00 · score 16 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfev0sc/)

I did a PhD in AI focussed on the logic of reasoning.  I think I can see why these LLMs like Negative Parallelism and find it hard to shake.  If you have a claim,  "She lives simply" for example, sitting very close to it in the network of nodes, parameters and arguments are reasons for and against.  These reasons are called argumentation and they build together to enable a conclusion to be drawn.  So in "She'd finally learned to live simply. No car. No TV. No smart fridge that texts her about expired yogurt while she's at her nephew's recital. Just books. Tea. Quiet."  There are likely to be arguments touching the Lives Simply claim - arguments for and against about cars, TVs, smart fridges, books, tea and quiet.  So she has a car rebuts the claim, but its negation, no car, supports and confirms the claim.  A key paper on the way this argumentation logic works is Besnard and Hunter (2001 IIRC) - before LLMs arose.  What I'm saying is that LLMs are rather mechanical and logical in their reasoning and typically or oftentimes lack  poetry or nuance.   

> u/Admirable-Language65 · 2026-10-12T09:18:44+00:00 · score 5 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfew48k/)

Almost of they are not human. It’s sort of weird, though since they have been trained on so much data of people talking casually or even papers or books. I get your point and it makes sense, it’s writing mini argumentative essays (except not essays just a few things to back up one simple sentence or claim that doesn’t need it). It sees a phrase or comment and want to try and validate it so it searches it’s context for adjacent statements to bolster it, and bam.

> u/SomeTwelveYearOld · 2026-10-12T13:51:05+00:00 · score 2 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfg3s8h/)

but at the same time its forming sentences (ie "No car.") that dont follow grammatical rules. how does that work?

> u/Thundechile · 2026-10-12T05:04:15+00:00 · score 10 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfe0og0/)

Damn, I almost started to review your output.

> u/crusoe · 2026-10-11T16:34:43+00:00 · score 5 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pf9ru1v/)

Ops page says at the bottom:

"Parody / satire. "u/out-of-phase," all revenue figures, the Stripe dashboard, customer logos, and testimonials are fictional and for entertainment. Not affiliated with Stripe, OpenAI, Reddit, or any real company. Results not typical, or real."

> u/Beautiful-Crab-815 · 2026-10-11T15:44:30+00:00 · score 12 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pf9ftp0/)

Small thing: the section about excessive colons sits under a heading that has a colon in it. So does your title.

> u/jaerie · 2026-10-12T07:58:52+00:00 · score 27 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfemnpu/)

This guy commented seriously under a humor post. No reading. No parsing. No laughing. Just pedantry.

> u/RedScharlach · 2026-10-12T03:30:53+00:00 · score 19 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfdmsm2/)

You: are absolutely right.

> u/this_is_a_long_nickn · 2026-10-12T04:43:22+00:00 · score 6 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfdxrku/)

This load bearing is too heavy at the seams 

> u/Better_Membership583 · 2026-10-12T02:01:45+00:00 · score 1 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfd7o27/)

Wut 

> u/WardedDruid · 2026-10-11T23:39:28+00:00 · score 4 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfchrbg/)

Thank you, those negative parallels drive me fucking insane

> u/damonkey47 · 2026-10-12T07:41:41+00:00 · score 3 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfeklix/)

I don't know what you're selling, but I like your humor. 

> u/Distinct-Delay7131 · 2026-10-12T07:43:42+00:00 · score 4 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfekua1/)

Bro literally just asked Ai to write its flaws and it did it with that very flaw

*Why it happens*

The model wants to sound grounded and decisive, and the pattern delivers that instantly. ~No hedging. No qualifiers. No "it depends," which is the honest answer to roughly every question anyone has ever paid a consultant to answer~. Just confidence. Rhythmic. Final.

> u/KelianJL · 2026-10-13T11:29:21+00:00 · score 2 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pgglkyu/)

![gif](giphy|aVUZCRPzNE3R9VGk1z)

> u/Spiritual_Flow_501 · 2026-10-13T06:41:30+00:00 · score 1 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pgfkwdl/)

"The model cant avoid a pattern you never describe". I cant tell you how many people I know who get actually pissed about AI and when I ask their prompt style they never explain what they want or dont want clearly. it all boils down to garbage in garbage out imo

> u/nattyandthecoffee · 2026-10-14T09:27:33+00:00 · score 1 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pgnmoli/)

Help me understand how to prompt out the weird backwards sentences and half sentences that Claude uses? 

> u/Background-Vast487 · 2026-10-14T10:20:49+00:00 · score 1 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pgnth4x/)

That website is great

> u/dwoj206 · 2026-10-12T04:07:52+00:00 · score 1 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pfdsmqc/)

Ya I ain’t reading all that. 

THE SUNDAY 9pm RESET! PRAISE BE! 

> u/Beautiful-Crab-815 · 2026-10-11T15:43:31+00:00 · score -1 · [comment](https://www.reddit.com/r/ClaudeCode/comments/1x3b9aa/negative_parallelism_the_biggest_culprit_that/pf9fl3q/)

Small thing: the section about excessive colons sits under a heading that has a colon in it. So does your title.

## Links

- https://billion-dollar-company.vercel.app
