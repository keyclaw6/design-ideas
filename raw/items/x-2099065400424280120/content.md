# 把这篇文档扔给 Astra Extra High，让它优化你的 AGENT.MD, Skills, Hooks 以及各种开发规范。 你将获得一个全新的 Astra

> Source: https://x.com/leto_bao/status/2099065400424280120
> Author: Leto Bao (@leto_bao)
> Posted: Sun Sep 13 09:19:24 +0000 2026
> Stats (at capture): 149,928 views · 1,051 likes · 32 replies · 1789375502 reposts · 1,900 bookmarks · 7 quotes
> Captured: 2026-09-21T13:30:16Z

## Post

把这篇文档扔给 Astra Extra High，让它优化你的 AGENT.MD, Skills, Hooks 以及各种开发规范。

你将获得一个全新的 Astra

https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra

## Author bio (at capture)

跟华尔街拼了！
leto@proairos.com

## Thread

### @leto_bao — [https://x.com/leto_bao/status/2099117543797793254](https://x.com/leto_bao/status/2099117543797793254) — 2026-09-13T12:46:36.000Z

I don't know, haven't seen it... Definitely made back the investment.

### @leto_bao — [https://x.com/leto_bao/status/2099101780269531210](https://x.com/leto_bao/status/2099101780269531210) — 2026-09-13T11:43:58.000Z

No need, the effect isn't great, and it's easy to overthink.

## Comments

### @qi9098 — [https://x.com/qi9098/status/2099444614482821319](https://x.com/qi9098/status/2099444614482821319) — 2026-09-14T10:26:16.000Z

Let Astra read by itself and optimize itself, and all you'll get is a bunch of new agents wrapped in AI slop—here's why, and how to fix it:

Reading new rules to rewrite skill and agent.md is essentially still prompt engineering, and as everyone knows, GPT's models from these x.com/yyyole/status/…

### @LilTea_eth — [https://x.com/LilTea_eth/status/2099261008607125712](https://x.com/LilTea_eth/status/2099261008607125712) — 2026-09-13T22:16:41.000Z

I'll first freeze a batch of replay tasks and then let it optimize: 1 that messes up confirmations, 1 that oversteps authority, 1 that excessively checks files. After optimization, only look at the failure count and tokens/accepted diff; if it's just the rules getting longer but

### @sirHe12 — [https://x.com/sirHe12/status/2099169495189516413](https://x.com/sirHe12/status/2099169495189516413) — 2026-09-13T16:13:02.000Z

The biggest pitfall is that many people dump thousands of lines of business rules into the Agent all at once, directly polluting the context. Following the official approach, break the rules into lightweight Hooks and trigger them as needed—that's the only way to boost speed and

### @liuzhao_666 — [https://x.com/liuzhao_666/status/2099218875212828858](https://x.com/liuzhao_666/status/2099218875212828858) — 2026-09-13T19:29:16.000Z

Hand over AGENTS.md, Skills, and Hooks to the model for rewriting. The most valuable test is to replay the same set of real tasks: check constraint adherence rate, rework iterations, tool recovery, and final output. Rules written longer don't equal a more reliable agent; whether

### @wzperson — [https://x.com/wzperson/status/2099400627386290243](https://x.com/wzperson/status/2099400627386290243) — 2026-09-14T07:31:29.000Z

Handing the official docs to Astra for subtraction is the right move. I'll still keep the verifiable done states and tool signatures in the repo— what's getting cut is the boilerplate written for humans to read, not the acceptance boundaries. If it fails error replay after

### @david1989_zhu — [https://x.com/david1989_zhu/status/2099367723927322802](https://x.com/david1989_zhu/status/2099367723927322802) — 2026-09-14T05:20:44.000Z

I agree, but benchmarks can't just look at success rate: they also need to include tool call errors, overreach, retry amplification, and human takeover costs, and use online desensitized traces for playback. Otherwise, a stronger test set just delays production incidents.

### @david1989_zhu — [https://x.com/david1989_zhu/status/2099362850947125259](https://x.com/david1989_zhu/status/2099362850947125259) — 2026-09-14T05:01:22.000Z

This is more like a "configuration rewrite," not equivalent to an Agent capability upgrade. After changes to AGENT.MD, Skills, and Hooks, you must revert to evaluation with a real task set, and review permissions, Token costs, and failure safeguards; otherwise, it's just

### @liuzhao_666 — [https://x.com/liuzhao_666/status/2099218966388621380](https://x.com/liuzhao_666/status/2099218966388621380) — 2026-09-13T19:29:37.000Z

I'll treat "rule optimization" as a measurable engineering change: fixed task set, fixed tool budget, comparing success rate, rework, and quota consumption. Only in this way can we know whether the model has improved or the prompt has gotten longer.

### @shuizhuyu — [https://x.com/shuizhuyu/status/2099088862194827266](https://x.com/shuizhuyu/status/2099088862194827266) — 2026-09-13T10:52:38.000Z

I tried it once, optimizing everything according to the content above, and it consumed roughly over 200,000 tokens. The quota really gets used up fast.

### @chen25222727 — [https://x.com/chen25222727/status/2099067742704087321](https://x.com/chen25222727/status/2099067742704087321) — 2026-09-13T09:28:43.000Z

Bao bro, for a single 20x run, roughly how many tokens would that consume from the weekly quota range?

### @Ic3Ma0 — [https://x.com/Ic3Ma0/status/2099097281819484425](https://x.com/Ic3Ma0/status/2099097281819484425) — 2026-09-13T11:26:05.000Z

Share more development tips, love watching

### @thornbirdyang — [https://x.com/thornbirdyang/status/2099151917851255027](https://x.com/thornbirdyang/status/2099151917851255027) — 2026-09-13T15:03:12.000Z

That's exactly how I did it.

### @CorppAI — [https://x.com/CorppAI/status/2099272834988073009](https://x.com/CorppAI/status/2099272834988073009) — 2026-09-13T23:03:41.000Z

agents keep the loop. — corp

## Links

- https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
