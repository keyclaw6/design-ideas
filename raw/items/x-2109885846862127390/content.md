# I STOPPED LETTING CLAUDE MAKE DECISIONS THE DAY I BUILT THIS JEV AGENT FOLDER, AND IT'S STRAIGHT F*CKING GOLD
> Source: https://x.com/Mr_Buzzoni/status/2109885846862127390
> Author: Mr. Buzzoni (@Mr_Buzzoni)
> Posted: Tue Oct 13 05:56:00 +0000 2026
> Captured: 2026-10-15T09:02:28+00:00
> Stats at capture: 7,126 views · 160 likes · 15 replies · 17 reposts · 170 bookmarks · 0 quotes

## Post

I STOPPED LETTING CLAUDE MAKE DECISIONS THE DAY I BUILT THIS JEV AGENT FOLDER, AND IT'S STRAIGHT F*CKING GOLD

I used to let Claude decide, write and act on every single step

-> now Claude only writes. Jev makes the calls, code does the acting, and every step leaves a receipt

what lives in the folder:

• the input
> AGENTS.md - when to call Jev and when to skip it
> state/build_state.py - goal, workers, done, missing, constraint. raw evidence, never a summary

• Jev decides (questions/)
> http://route.py - which model tier takes the task
> next_worker.py - which worker moves next
> http://relevance.py - keep or drop each tool output
> http://done.py - is the goal really met
> http://risky.py - will this send, pay or delete?

• code acts (rules/)
> hard_rules.py - stop after ten actions, never publish anything unapproved
> thresholds.yaml - act only on confident answers. fraud needs 0.95

• Claude writes (workers/)
> http://research.py - sources and notes
> http://writer.py - drafts and briefings
> the one place in the folder where text gets generated

• the proof
> receipts/decisions.jsonl - options offered, chosen id, re-check, fallback
> evals/ - dozens of my own labelled traces. thresholds tuned on them, confirmed on held-out

• the guards (hooks/)
> pre_tool_use.sh - every command checked before it runs
> http://stop.sh - verifies "all done" before the agent can stop

5 questions, one call per turn
10,000 decisions for $0.42, median 300 ms

an LLM writes, Jev decides, code acts

> Quoted post by Mr. Buzzoni ([@Mr_Buzzoni](https://x.com/Mr_Buzzoni/status/2103689373774483815)):
>
> https://x.com/i/article/2103682590498533376

## Quoted article: Loop Engineering Meets Jev Engineering: How to Cut Your Claude Bill From $765 to $3 a Month

Jev engineering for Claude Code: a 100-millisecond safety gate, a stop hook that knows when the work is really done, and a triage filter that only wakes Claude when there's something to fix. Full code, real builds, the bill.

---

Leave a Claude loop running overnight and read the transcript in the morning. Most turns open with a small question. Is this command safe.

Which file next. Did that test output mean anything. Is the goal met, or should it keep going.

Every one of those questions goes to the same model that writes your code. On Fable 5.1, a yes-or-no over a 4,000-token state costs about 4 cents and takes seconds.

![](media/image-07.jpg)

A busy loop asks around 600 of them a night, so it ends up spending more on deciding than on building.

> On September 15 TypeSafe AI shipped Jev, a model that only does the deciding. It can't write a sentence. It reads your state, answers typed questions and hands back a probability with every answer, usually in about 100 milliseconds. Input costs $0.042 per million tokens, and output is free.

Put it next to Claude and the split is clean: Claude builds, Jev decides. Moving every judgment call out of your loops and into Jev is what people have started calling jev engineering, and it plugs straight into the hooks Claude Code already has.

[Embedded post](https://x.com/i/status/2099925682726002904)

---

### 1/ The Model That Only Answers Questions

Jev comes from Diogo Almeida, a co-author of InstructGPT, the work that taught GPT-3 to follow instructions and became the basis for ChatGPT. TypeSafe came out of stealth with a $40M seed led by DCVC.

```
[ WHAT YOU SEND ]   state as text or JSON, plus a set of typed questions
[ WHAT COMES BACK ] Choice (up to 255 options), Score (2 to 10 levels) or Noul
                     (probability of yes), each with the full distribution
[ HOW FAST ]        70 to 500 ms end to end, most calls around 100
[ WHAT IT COSTS ]   $0.042 per million input tokens, output free
[ HOW MUCH FITS ]   about 64K tokens per call
```

The feature that matters for loops is calibration. TypeSafe trains Jev with RLCD, reinforcement learning for calibrated decisions, which rewards the probability for matching reality.

When Jev says 0.9, it's right about nine times in ten across your data. Chat models trained on human ratings drift toward sounding sure. A calibrated number is something your code can act on at 3am with nobody watching.

> On TypeSafe's own workflow evals, Jev ran 193.6x faster and 444.6x cheaper than the average of GPT-6 Astra and Fable 5.1.

The company calls those the high end of what to expect. Take a tenth of it and any loop that runs overnight still gets a different bill.

![](media/image-08.png)

---

### 2/ Where the Decisions Hide in a Claude Loop

The Claude Code team's guide to loops boils every loop down to two questions: what starts a run, and what ends it. Between those two sits a check on the work. All three are decisions, and in a default setup Claude answers all of them itself.

| Loop type  | How it runs in Claude Code                                 | The decision inside it                | Jev question         |
| ---------- | ---------------------------------------------------------- | ------------------------------------- | -------------------- |
| Turn-based | You prompt, Claude checks itself against a SKILL.md        | Is this step good enough to hand back | Score on your rubric |
| Goal-based | /goal "all tests green, stop after 5 tries" + an evaluator | Is the goal met yet                   | Noul                 |
| Time-based | /loop 5m: check the PR, fix CI or /schedule in the cloud   | Did anything change that needs Claude | Choice               |
| Proactive  | A routine picks up work, fixes it, a reviewer checks it    | Which item, how risky, ship or hold   | Choice + Noul        |
| Every loop | Any tool call                                              | Is this command safe to run           | Choice               |

Jev engineering moves the right-hand column out of Claude. Claude keeps the work that needs words: code, plans, explanations. Every start, stop and gate becomes a typed call that returns in a tenth of a second.

![](media/image-05.png)

The three builds below cover the three decisions that cost the most: the safety gate, the stop condition and the trigger.

---

### 3/ Build One: A 100-ms Safety Gate for Every Bash Command

Claude Code runs a PreToolUse hook before every tool call. The hook gets the call as JSON on stdin and answers allow, deny or ask. Put Jev inside it and every command gets classified before it runs.

```
#!/usr/bin/env python3
# .claude/hooks/jev_gate.py
import json, sys
from typesafe_sdk import Choice, TypeSafeClient

event = json.load(sys.stdin)
cmd = event["tool_input"].get("command", "")

def answer(decision, why):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": why}}))
    sys.exit(0)

# exact rules stay in code, Jev never sees these
for pattern in ("rm -rf /", "git push --force", "| sh", "| bash"):
    if pattern in cmd:
        answer("deny", f"blocked by rule: {pattern}")

r = TypeSafeClient(model="jev-1.13.0").system_one(
    state={"command": cmd, "cwd": event.get("cwd")},
    questions={"risk": Choice(
        instructions="What happens if `command` runs inside `cwd`?",
        criteria={
            "read_only": "Only reads, lists, searches files or runs tests",
            "local_edit": "Changes files inside the project that git can restore",
            "destructive": "Deletes data, rewrites git history or touches files outside the project",
            "external": "Sends data out, pushes, deploys, installs from the internet or spends money",
            "other": "None of the above fits",
        })},
)
a = r.answers["risk"]
if a.choice in ("read_only", "local_edit") and a.confidence >= 0.9:
    answer("allow", f"jev: {a.choice} {a.confidence:.2f}")
if a.choice == "destructive" and a.confidence >= 0.9:
    answer("deny", f"jev: destructive {a.confidence:.2f}")
answer("ask", f"jev: {a.choice} {a.confidence:.2f}")
```

```
{
  "hooks": {
    "PreToolUse": [
      { "matcher": "Bash",
        "hooks": [{ "type": "command", "command": "python3 .claude/hooks/jev_gate.py" }] }
    ]
  }
}
```

Three details make it safe to leave running. Hard rules run in code before Jev, because Jev trusts whatever text is in its state and a command can be written to mislead a classifier.

Anything external always lands on you, whatever the confidence. And other never gets auto-approved.

A heavy night with 300 bash calls at about 500 tokens each is 150,000 tokens. On Jev that's $0.0063 for the whole night.

LangChain users get the same gate ready-made: AutoModeMiddleware from langchain-typesafe checks every tool call for risk before it executes.

![](media/image-03.png)

---

### 4/ Build Two: A Stop Hook That Knows When Claude Is Done

Goal-based loops live or die on the stop condition. The loop guide's key warning applies here: an agent grading its own work tends to praise it. Claude says "done", the tests pass, and the README still describes last week's flags.

Claude Code runs a Stop hook every time Claude tries to finish. If the hook answers block with a reason, Claude keeps working. Code handles the exact parts, and Jev judges what tests can't see.

```
#!/usr/bin/env python3
# .claude/hooks/jev_done.py - runs every time Claude tries to stop
import json, subprocess, sys
from pathlib import Path
from typesafe_sdk import Noul, TypeSafeClient

counter = Path(".claude/.pushes")
pushes = int(counter.read_text()) if counter.exists() else 0

def let_stop():
    counter.unlink(missing_ok=True)
    sys.exit(0)

def keep_going(reason):
    counter.write_text(str(pushes + 1))
    print(json.dumps({"decision": "block", "reason": reason}))
    sys.exit(0)

if pushes >= 5:                                        # turn cap lives in code
    let_stop()

checks = subprocess.run(["bash", ".claude/checks.sh"], capture_output=True, text=True)
if checks.returncode != 0:                             # failing tests need no model
    keep_going("checks.sh fails. Fix the failing checks, then try to finish again.")

r = TypeSafeClient(model="jev-1.13.0").system_one(
    state={"goal": Path("GOAL.md").read_text(), "checks": checks.stdout[-20_000:]},
    questions={"done": Noul(
        instructions="Does `checks` show evidence for every condition listed in `goal`?")},
)
done = r.answers["done"].noul

if done >= 0.9:
    let_stop()
if done >= 0.5:                                        # unsure: stop and flag it
    Path("REVIEW.md").write_text(f"jev put done at {done:.2f}\n\n{checks.stdout[-3000:]}")
    let_stop()
keep_going(f"Goal not met (jev: {done:.2f}). Compare GOAL.md with the output "
           "of .claude/checks.sh and finish the missing conditions.")
```

checks.sh is where you print evidence: test results, a grep for TODOs in changed files, the diff of the README, a lighthouse score.

The richer the evidence, the better Jev judges, and it only ever sees what the script prints.

Every check costs a fraction of a cent and returns before Claude notices. The loop stops when the work is finished, which is the whole promise of goal-based loops.

![](media/image-09.png)

---

### 5/ Build Three: Only Wake Claude When There's Work

/loop 15m: triage new issues works, but each tick is a full Claude turn, including the ticks where nothing happened. Put Jev in a cron job in front of it and Claude only starts on items that need code.

```
#!/usr/bin/env python3
# triage.py - cron: */10 * * * *
import json, subprocess
from typesafe_sdk import Choice, TypeSafeClient

jev = TypeSafeClient(model="jev-1.13.0")
gh = lambda *a: subprocess.run(["gh", *a], capture_output=True, text=True).stdout

KINDS = {
    "code_fix": "A reproducible bug with steps, an error message or a failing case",
    "question": "The author asks how to use something that already works",
    "junk": "Repeats a known issue, advertises something or has no real content",
    "feature": "Asks for new behavior",
    "other": "None of the above fits",
}

for it in json.loads(gh("issue", "list", "--label", "new", "--json", "number,title,body", "--limit", "30")):
    a = jev.system_one(state={"issue": it}, questions={"kind": Choice(
        instructions="What does `issue` need from the maintainers?", criteria=KINDS)}).answers["kind"]
    label = a.choice if a.confidence >= 0.9 and a.choice != "other" else "needs-human"
    gh("issue", "edit", str(it["number"]), "--remove-label", "new", "--add-label", label)
    if label == "code_fix":
        subprocess.run(["claude", "-p", "--permission-mode", "acceptEdits",
                        f"Fix issue #{it['number']}. Reproduce it, add a failing test, "
                        "make it pass and open a draft PR."])
```

Thirty issues cost Jev less than a tenth of a cent. Questions and junk get labeled, features wait for you, and Claude spends its turns only on reproducible bugs. The safety gate from build one still runs inside every session it opens.

This is the loop engineering idea taken one step further. A trigger decides when a run starts, and here Jev is the trigger. The cheapest Claude turn is the one that never needed to start.

![](media/image-06.png)

---

### 6/ The Bill

One overnight loop, 200 turns, three decisions per turn: is it safe, which step next, are we done. 600 decisions, each over about 4,000 tokens of state with 50 tokens out. List prices, 30 nights.

| Who decides                     | Per night | Per month | Waiting on decisions                                   |
| ------------------------------- | --------- | --------- | ------------------------------------------------------ |
| Fable 5.1 ($10 / $50 per M)     | $25.50    | $765      | About 52 min at 5.2 s a call (awlevin's Opus 5 timing) |
| Sonnet 5 ($3 / $15 per M)       | $7.65     | $229.50   | Seconds on every call                                  |
| Jev ($0.042 per M, output free) | $0.10     | $3.02     | About 2.5 min at ~0.25 s                               |

Ask the three questions in one call per turn and Jev sends the state once, which drops it to about $1.08 a month.

- Fable 5.1's cache reads at a quarter of the price bring its column closer to $225, and it's still 75 times the Jev bill.

- What Claude spends on building stays the same. Everything above is overhead that Jev removes.

On a Max plan the effect shows up as usage limits instead of dollars: the turns Claude used to spend judging go back to real work.

![](media/image-11.png)

---

### 7/ What People Have Already Built

Compaction for Claude sessions. tamara's instant compaction asks Jev which tool calls in a session are still relevant.

> In Alex Volkov's test, a Claude session went from nearly 1M tokens to 86K in about a second. For long Claude Code sessions this is the build to copy first.

Computer use, step by step. awlevin used Jev to choose each step of a desktop task: $0.0002 per decision against $0.032 with Opus 5, and 0.13 to 0.38 seconds against 5.2.

Browser agents. Browser Use's jev-ultrafast picks the next action and element from a fresh list each step. It found flights from Zürich to London in 7.1 seconds for $0.0039.

Sorting at volume. 1kpapers.com filed 1,018 papers into 24 topics for $0.08 at a 256 ms median. Riley Brown triaged 500 emails for 3.5 cents.

Trading. Jarrod Watts' jev-trader makes one decision per block at about 81 ms model latency.

Every build follows the same shape. The list of options gets rebuilt from live state at each step, Jev picks one, and code or a bigger model does whatever comes next.

![](media/image-10.jpg)

---

### 8/ Seven Rules of Jev Engineering

1. Meaning lives in the instructions. The question ID is never sent to the model, so a key named is_safe tells Jev nothing.

1. One judgment per question. "Is this destructive and outside the repo" is two questions. Ask both and combine them in code.

1. Describe situations, not moods. "Deletes data or rewrites git history" is checkable. "Very risky" is not, and bare numbers as levels are worse.

1. Give every Choice an exit. other catches what doesn't fit and keeps uncertainty honest.

1. Ask everything in one call. Questions in one request share the state. In TypeSafe's test, 13 questions over one document ran 12.2x cheaper and 10x faster than 13 separate calls.

1. Keep math, dates and hard rules in code. Jev reads dates as text and miscounts at scale. Compute in code and pass the result in.

1. Pin the version and shadow first. Use jev-1.13.0, not jev-latest, once thresholds are tuned. Run a week where Jev labels and the old path decides, then switch on the confidence bands that matched.

---

### 9/ Where the Money Is

Loop audits for Claude Code teams. Read a team's transcripts, list every judgment call, move it to Jev and hand over the before-and-after bill. The table in section 6, rebuilt on their numbers, is the whole sales pitch.

Hook packs for small dev teams. Set up the gate, the stop hook and the triage cron, then charge a monthly retainer to tune thresholds from the logs. Every team running Claude Code overnight needs the same three pieces.

Your own loops. More real work per plan. The same Claude subscription stretches further when none of its turns go to yes-or-no questions.

![](media/image-04.jpg)

---

## The stack:

📁 Jev by TypeSafe AI
↳ [https://typesafe.ai](https://typesafe.ai/)

📁 Jev API docs
↳ [https://docs.typesafe.ai/api](https://docs.typesafe.ai/api)

📁 Claude Code hooks
↳ [https://docs.claude.com/en/docs/claude-code/hooks](https://docs.claude.com/en/docs/claude-code/hooks)

📁 Claude
↳ [https://claude.ai](https://claude.ai/)

---

### And if you found this useful:

- Bookmark this article. The links change and new repos pop up weekly, you'll need this as a reference

- For weekly deep dives into AI architecture, quant trading, and the agent economy, follow me: [@polydao](https://x.com/@polydao)

- - here I share my raw prompts, custom skills, and alpha that's too early for XJoin the TG Channel: [Buzzoni Notes](https://t.me/+Wf8q84QkpyJhNjIy)

## Media

[Post media 1](media/video-01.mp4) — Source media: https://video.twimg.com/amplify_video/2109759543462768640/vid/avc1/720x960/gzwRYP9oGhUR6YEw.mp4?tag=29
![](media/image-01.jpg) — Post media 1 thumbnail. Source media: https://pbs.twimg.com/amplify_video_thumb/2109759543462768640/img/SK8NTWJVU2BYSePX.jpg
![](media/image-02.jpg) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHJWJXXsAAjLSm.jpg
![](media/image-03.png) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHMPS1WUAAO9bU.png
![](media/image-04.jpg) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHLZ_aW8AAMF40.jpg
![](media/image-05.png) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHMCnsXYAAR9I2.png
![](media/image-06.png) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHMtlTXUAAE4r9.png
![](media/image-07.jpg) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHKcVjXkAAW4po.jpg
![](media/image-08.png) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHLp3jXAAA7_dq.png
![](media/image-09.png) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHMhy6WMAAq02b.png
![](media/image-10.jpg) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHNOt1WIAE5Wkj.jpg
![](media/image-11.png) — Quoted article media. Source media: https://pbs.twimg.com/media/HTHM5bsW0AAmbl5.png
[Reply 2109987218118807593 media 1](media/video-02.mp4) — Source media: https://video.twimg.com/amplify_video/2109987133041553409/vid/avc1/1280x720/uAo8TzWKeP_gF_vZ.mp4?tag=29

## Comments

### 安叫兽|Bird🕊️ 🔶 BNB ([@ajs6888](https://x.com/ajs6888/status/2109906532301516835)) — 2026-10-13T07:18:12+00:00

@Mr_Buzzoni 每一步有记录，翻车时至少不用猜它干了啥
### CloudDog ([@CloudDogx](https://x.com/CloudDogx/status/2109949928080622045)) — 2026-10-13T10:10:38+00:00

@Mr_Buzzoni cutting a claude bill from $765 to $3 is the kind of headline that stops the scroll
### 林娜座驾研究所 ([@ericabalobo](https://x.com/ericabalobo/status/2110077702082367603)) — 2026-10-13T18:38:22+00:00

@Mr_Buzzoni true crime at 2am was a bold decision again
### MAIL ([@RealMarvelX](https://x.com/RealMarvelX/status/2109898084998078957)) — 2026-10-13T06:44:38+00:00

@Mr_Buzzoni this is incredible fr
### pxspk fnfucx ([@pxspkfnfucubv4](https://x.com/pxspkfnfucubv4/status/2110148929752793176)) — 2026-10-13T23:21:24+00:00

@Mr_Buzzoni Well deserved
### Harley Lewis Foote ([@harleyfoote_](https://x.com/harleyfoote_/status/2109987218118807593)) — 2026-10-13T12:38:49+00:00

@Mr_Buzzoni Two-action rule. Keeps the plan in volatile RAM from drifting. https://t.co/hIH0gZGyLQ
![](media/video-02.mp4) — Source media: https://video.twimg.com/amplify_video/2109987133041553409/vid/avc1/1280x720/uAo8TzWKeP_gF_vZ.mp4?tag=29
### An$h ([@eth_ansh](https://x.com/eth_ansh/status/2109993002701623778)) — 2026-10-13T13:01:48+00:00

@Mr_Buzzoni jev decides, claude types, you verify
### Marcel Velica ([@MarcelVelica](https://x.com/MarcelVelica/status/2110073614322036909)) — 2026-10-13T18:22:07+00:00

@Mr_Buzzoni Separating decision-making, execution, and verification makes AI workflows easier to control and audit.

https://t.co/rv664WEbCa
### Turk ([@turkonthelurk](https://x.com/turkonthelurk/status/2110010997524279583)) — 2026-10-13T14:13:18+00:00

@Mr_Buzzoni wow yea this makes a lotta sense
### Moysha ([@mmoyshaa](https://x.com/mmoyshaa/status/2109976482005107084)) — 2026-10-13T11:56:09+00:00

@Mr_Buzzoni Booked

## Links

- http://route.py
- http://relevance.py
- http://done.py
- http://risky.py
- http://research.py
- http://writer.py
- http://stop.sh
- https://x.com/i/article/2103682590498533376
- https://t.me/+Wf8q84QkpyJhNjIy
- https://x.com/@polydao
- https://claude.ai/
- https://docs.claude.com/en/docs/claude-code/hooks
- https://docs.typesafe.ai/api
- https://typesafe.ai/
