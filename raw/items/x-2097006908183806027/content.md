# Copy My $78k MRR Solo Agency (THE FULL SYSTEM)

> Source: https://x.com/DeRonin_/status/2097006908183806027 — Ronin (@DeRonin_) — Mon Sep 07 16:59:42 +0000 2026 — 626 likes · 51 reposts · 42 replies · 130608 views — captured 2026-09-21T15:29:07Z

## Post

**Author:** Ronin (@DeRonin_)
**URL:** https://x.com/DeRonin_/status/2097006908183806027

https://x.com/i/article/2096907368365744130

## Article (full text, verbatim)

# Copy My $78k MRR Solo Agency (THE FULL SYSTEM)

> Article: https://x.com/i/article/2096907368365744130 — by Ronin (@DeRonin_) — created 2026-09-07T16:59:41.000Z

I built a distribution agency to $78k MRR and there is almost nobody else in it

9 clients, 3 multi-billion AI/tech products, no project managers, no researchers, no writers, no analyst pulling numbers at midnight, and the whole thing runs on under $1,400 a month

But you are not here to read about my agency

An agency was never a set of skills, it is a set of LOOPS

Research is a loop

Qualification is a loop

Production is a loop

Review is a loop

Reporting is a loop

Every one of those was somebody's salary five years ago

Change what flows through them and the same machine runs a marketing agency, a devops consultancy, a design studio, a recruiting firm or a bookkeeping practice

The seven loops never change, only the payload does

And here is the part I have never written about before, because until this year it did not work: every loop now improves itself (in my system)

Not "the model got smarter when they shipped a new one", that is their improvement and not yours

I mean each department keeps its own written record of what worked, what failed and why, updates it after every single job, and is measurably better next Friday than it was this one

I do not write those files

I only read them

That is the whole difference between a system you babysit and a system that compounds

**After reading and building this, you will have:**

1. The seven departments of any service business, mapped to your own niche in one table
2. Two self-improvement mechanisms, built once, that every department then inherits
3. A model routing layer that puts each job on the model that actually wins that job, with the benchmark receipts
4. Seven working departments, each with the exact files, prompts, schedules and metrics
5. A weekly operating rhythm that takes about 40 minutes a day at nine clients
6. The real unit economics, so you know what this costs before you commit
7. A 12 week build order, in the sequence I would use if I started again on Monday
Fair warning on length: this is the full system, not a teaser

**[ Let's build it ] ↓↓↓**

---

## Every Agency Is Seven Repeating Jobs That Used to Be Salaries

Here is the mistake almost everyone makes, and I made it for a year

They ask "which of my tasks can AI do"

That question gets you a pile of disconnected shortcuts, a folder of prompts, and a business that still runs entirely on you remembering to open the folder

The better question is "which of my departments is secretly a loop"

Because a loop has a shape: an input arrives, a fixed process runs, an artifact comes out, and the result teaches you something for next time

Research is scan, extract, cluster, repeat

Qualification is pull, score against criteria, rank, repeat

Production is brief in, draft out, repeat

Review is check against rules, flag, return, repeat

Reporting is pull numbers, compare to last period, narrate, repeat

Every one of those was a salary five years ago because a loop needed a human to walk it

None of them need that now, and the ones that still feel like they do are usually just loops you have not written down yet

The seven departments

Every service business, in every niche I have looked at, staffs some version of these seven:

1. The Radar, the research department, which figures out what is happening in your market before your clients ask
2. The Scout, the qualification department, which decides what is worth your attention and what is noise
3. The Forge, the production department, which makes the thing you actually sell
4. The Gate, the review department, which stops bad work from reaching a client
5. The Lab, the strategy department, which tests things before you bet money on them
6. The Ledger, the operations department, which handles the plumbing nobody sees
7. The Relay, the account department, which keeps clients informed and retainers alive
You are the eighth seat: taste, judgment, and relationships

That never leaves, and pretending otherwise is how people build impressive machines that lose every client in six months

The same seven, in your niche

This is the table that makes the rest of the article yours instead of mine:

```plaintext
judge_panel:
  models: [kimi-k3, claude-opus-5, gpt-5.6-sol, qwen-3.8-max]

  each judge receives:
    the audience definition from radar context
    the variant, with no indication of who wrote it
    no other variants, judged independently, no anchoring

  each returns:
    would_stop_scrolling   0-10
    would_act              0-10
    the specific line that made the decision
    what it thinks the offer is, which catches unclear variants

  keep only variants that win across DIFFERENT families
  agreement within a family means nothing
```

Find your column

If your business is not on it, write your own version before you continue, because every department below assumes you know what flows through it

Everything after this point is the same regardless of which column you are in

**[ The part that makes it compound ] ↓↓↓**

## The Two Mechanisms (Build These Before Any Department)

Do not start with a department

Start here, because these two mechanisms are what every department inherits, and if you build them after the fact you will retrofit seven systems instead of one

## Mechanism 1: The Playbook

Every department owns one file called playbook.md

It is not a prompt, and this distinction is the whole thing

A prompt is what you tell the model to do

A playbook is what the department has LEARNED about doing it, accumulated from its own results, in its own words, and injected into every run

The mechanism comes from a 2026 paper on agentic context engineering, and the reason to use their version rather than inventing your own is that they measured the two ways it goes wrong

Link: https://arxiv.org/abs/2510.04618

The first failure is context collapse: if you let a model rewrite the whole playbook each time, details erode with every pass, and after twenty cycles the hard-won specifics have been smoothed into generic advice

The second is brevity bias: models prefer tidy summaries, so left alone they will delete the strange, specific, domain-earned line that was the most valuable thing in the file

Their fix is the rule you have to enforce mechanically: never rewrite the playbook, only append and amend individual entries

Their split is three roles, and it is worth keeping the separation:

- the Generator does the actual work and produces the artifact
- the Reflector looks at what happened and diagnoses why, without touching the playbook
- the Curator turns that diagnosis into small structured edits
Run this way, they measured +10.6% on agent benchmarks and +8.6% on a finance domain, with lower adaptation latency and lower rollout cost, and a smaller open model matching a top production agent on the AppWorld leaderboard

Those gains came from execution feedback, with no labelled training data, which is exactly the situation you are in

The file format, which you should copy exactly:

---

Four rules that make this work in practice, all of them learned the annoying way:

Entries are conditional, not general. WHEN x THEN y beats "write good hooks" because a condition can be checked and a platitude cannot

Every entry carries a counter. Hits and misses are updated by the Reflector each run, and an entry that keeps missing gets demoted rather than silently obeyed

Confidence is a field, not a feeling. New entries start low, earn their way to high, and only high-confidence entries are treated as hard constraints

Entries expire. Anything at low confidence with no hits in 30 days gets pruned, otherwise the file grows into noise and you are back to context collapse by a slower route

The curation prompt, which runs after every job, on a schedule, with no involvement from you:

---

The last rule matters more than it looks

A curator that must produce something will invent something, and a playbook full of invented lessons is worse than an empty one because it is confidently wrong at scale

## Mechanism 2: The Skill Bank

The playbook is how a department gets smarter about JUDGEMENT

The skill bank is how it gets faster at EXECUTION

The pattern comes from a 2026 self-evolving agents paper, and the numbers are the reason to bother

Link: https://arxiv.org/html/2605.27366v1

Their agent generated its own skills for 35 of 51 benchmark tasks, and on those tasks it hit 87.94% against a 68.40% baseline that used human-written skills

The skills also transferred: injected unmodified into a different agent, they lifted it from 47.89% to 58.40%, closing 79% of the gap to human-written skills

So the skills were real reusable knowledge and not a quirk of one agent's wiring

The lifecycle is five stages, and the third one is the stage everybody skips:

Create. When a department solves something it could not solve before, it writes the solution up as a skill rather than throwing it away

Test. The skill must pass its own unit tests in a sandbox before it is allowed into the bank

This is the gate that keeps the bank trustworthy, and without it you accumulate a folder of plausible files that quietly break things

Register. Indexed by name, description, inputs and outputs, so it can be retrieved by relevance rather than by you remembering it exists

Refine. Failed tests trigger an automatic patch and retest, rather than a human bug report

Prune and merge. Overlapping skills get consolidated, underperforming ones get deleted, because a bank of 200 mediocre skills retrieves worse than a bank of 30 good ones

**The skill format:**

```plaintext
# playbook: the-gate
# every entry is atomic, dated, and carries evidence
# entries are APPENDED or AMENDED, never bulk rewritten

[G-014] 2026-08-12  confidence: high  hits: 23  misses: 1
WHEN a draft opens with a rhetorical question
THEN rewrite the opener, our audience reads it as AI-written
EVIDENCE campaign 41, three creators flagged it unprompted

[G-027] 2026-08-29  confidence: medium  hits: 6  misses: 2
WHEN the client is an infra product
THEN never claim a latency number without a link to their own docs
EVIDENCE legal pushback on campaign 47, cost us four days

[G-031] 2026-09-02  confidence: low  hits: 2  misses: 0
WHEN a post is for LinkedIn rather than X
THEN the first line must survive being cut at 140 characters
EVIDENCE two posts truncated mid-claim last week
```

notes.md is the piece most people leave out and it is quietly the best part

It is per-skill memory: every time the skill runs and something surprising happens, a line goes in the notes, and those notes ride along whenever the skill is used again

That is how a department stops re-deriving the same workaround every month

The promotion rule, which is the only manual policy you need:

If you or a department solves the same problem a third time, it becomes a skill

Not the first time, because the first time you do not yet know the general shape

Not the second, because two data points is a coincidence

The third time is when the pattern is real and the cost of writing it up is repaid immediately

How the two fit together

The playbook changes what the department BELIEVES

The skill bank changes what the department CAN DO

A department with both gets better at deciding and faster at executing, from its own results, every week, without you opening either file

**What to memorize:**

You are not the manager of the agents, you are the editor of the playbooks

The moment your week is spent answering agents rather than reading what they learned, you have rebuilt the job you were trying to delete

Practice, and do this before any department: create playbook.md and skills/ for one process you already run manually, run it five times, and let the Curator write the deltas

Read the file at the end of the week and see whether you agree with what it learned

That single week tells you more than the rest of this article

**[ The routing layer ] ↓↓↓**

---

## The Routing Layer: Put Each Job On The Model That Wins That Job

Most people pick one model and use it for everything

That is the single most expensive decision in the stack, and not for the reason you think

The cost is not money, it is that you are running most of your work on a model that is mediocre at that particular shape of work, and you never find out, because a mediocre output still looks like an output

An agency does four distinct shapes of work, and different models win each one:

Tool orchestration. Long chains that call many different APIs, scrapers, sheets, schedulers and databases in sequence, where the failure mode is losing the thread halfway through a fifteen-tool run

Deep search. Open-ended digging across the live web where the answer is not in any single page and has to be assembled from many

Professional judgment. The one-off call where being wrong costs a client, a claim, or a relationship

Long-horizon endurance. Jobs that run for hours without supervision, where output quality at step 300 has to match step 3

Here is the current picture, with the numbers rather than my opinion, and I am including the places my own stack loses because a comparison that only flatters one model is an advertisement

Tool orchestration. On MCPMark-Verified, which measures whether a model can drive a long chain of real tools without dropping one, Kimi K3 leads at 94.5, GPT-5.6 Sol follows at 92.9, Claude Fable 5 at 87.4 and Claude Opus 4.8 at 76.4

Read that honestly: K3 is first, and its lead over the next model is 1.6 points, not a chasm

Link: https://codersera.com/blog/kimi-k3-benchmarks-comparison-2026/

Business automation. This is the one that actually decides an agency, and the gap is wider: on AutomationBench, K3 scores 30.8 against Claude Opus 5 at 26.0

Note how low both numbers are, because that is the real story of this benchmark, and it is why the Gate in the next section exists

Deep search. K3 posts 91.2 on BrowseComp against Opus 5's 90.8, which is a tie and not a win, and 95.0 F1 on DeepSearchQA, the highest reported

So the honest claim is that K3 is at the front of the pack on search rather than ahead of it

Professional judgment. K3 loses, and plainly: on GDPval-AA v2, built around real professional deliverables, Claude Fable 5 Max scores 1,815 against K3's 1,687

That single result is why verification and every client-facing call route to Claude in the file below

Link: [https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems](https://codingfleet.com/blog/claude-opus-5-vs-kimi-k3/)

General reasoning. K3 also loses the aggregate, and by a real margin

Claude Opus 5 takes BenchAlign at 85.88 against 79.98, HLE at 64.7% against 56.0%, DeepSWE at 68.8% against 67.5% and Terminal-Bench at 89.1% against 88.3%

Link: [https://codingfleet.com/blog/claude-opus-5-vs-kimi-k3/](https://codersera.com/blog/kimi-k3-benchmarks-comparison-2026/)

Speed, which nobody puts in these articles and everybody feels. K3's time to first token is 164.6 seconds against Opus 5's 21.7, and it generates at 32 tokens per second against 58

That is disqualifying for anything you sit and wait for, and completely irrelevant for a sweep that runs at 02:00 while you are asleep, which is most of what an agency actually does

Long-horizon endurance. K3 is a 2.8 trillion parameter mixture of experts with 104B active and a one million token context, demonstrated by Moonshot with a 48 hour autonomous chip design run

The million token window is the operational detail that matters most here: a department holds a client's entire context, brand file, claims file, playbook and campaign history in one window instead of retrieving fragments of it

So no, K3 is not the best model that exists

Claude Opus 5 is a better model in general, and it is first on the overall board at 84 with GPT-6 Astra second at 82

Link: https://benchlm.ai/frontier-ai-models

K3 is the best model for two specific shapes of work that happen to be most of an agency's volume, which are driving long tool chains and running unattended automation, and it is roughly level on search

That is a much narrower claim than the marketing around any of these models, and it is the only one the numbers support

Price is a consequence rather than a reason, $15 per million output against $25 for Opus 5 and $50 for Fable 5

If the prices were identical I would keep the Radar and the Scout on K3 for the automation scores, and I would still keep the Gate on Claude for the judgment ones

The routing file, which lives at the root of the whole system:

```plaintext
frames.yaml

cost_arbitrage:  the same result for a fraction of the price
contrarian:      the thing everyone does is wrong
discovery:       a thing that exists and you did not know
proof:           here is the receipt
identity:        people like you do this
stakes:          what it costs you to keep doing it the old way
```

Decision framework for anything not on that list:

- the job calls more than five tools in a chain, route to whatever wins tool orchestration
- the answer has to be assembled from the live web, route to whatever wins search
- the output goes to a client without you reading it, route to your best judgment model, and then reconsider whether it should go unread at all
- the job runs longer than an hour unattended, route to whatever holds context longest
- you are choosing on price alone, you have not defined the job well enough yet
The rule that saves you the most money is not a model choice at all: the Gate must run on a different model family than the Forge

A model checking its own output is an employee grading their own homework, and the disagreement between families is where real errors surface

That single structural decision catches more than any upgrade you can buy

**[ Department one ] ↓↓↓**

```plaintext
roster/creator-4821.md

screened:     2026-03-11, score 78, verdict INCLUDE
used:         campaign 34, campaign 41
delivered:    on time both, engagement 1.4x predicted
notes:        audience skews more senior than their bio suggests
              do not brief them casually, they respond to data
```

## Department 1: The Radar

What it replaces: the strategist who reads the market so you know what to sell before the client asks for it

Why it goes first: every other department gets smarter when this one exists, because the Radar's output is the input to production, qualification and client conversations

Build it first and the rest inherit context they would otherwise invent

The build

**Step 1: write the source map**

One file per client or niche, listing exactly where your market talks

```plaintext
You are the Forge coordinator for [CAMPAIGN]

Load: brief, voice file, claims file, radar context, playbook

Split the batch by asset type, spawn one worker per type, and give
each worker the FULL context, never a summary of it

Each worker returns:
  the asset
  which claims file lines it relied on
  which radar phrases it used verbatim
  a confidence line, and what it was unsure about

Merge, then hand the batch to the Gate
Never hand anything directly to the human
```

Mine runs about 130 sources across nine clients

Yours should start at fifteen, because a small map you actually read beats a large one you ignore

**Step 2: the nightly sweep**

A scheduled job, running at 02:00, one run per client

The sweep is a tool-orchestration job before it is a reading job: it authenticates against six or seven different APIs, paginates, deduplicates, handles rate limits, and only then does any thinking

That is why it routes to K3 rather than to a model that writes beautifully and drops the seventh tool call

---

The verbatim rule is the one that pays

Paraphrased pain is generic and useless, and the exact phrase a customer used is the hook, the headline and the objection handler all at once

**Step 3: the velocity layer**

Raw volume is a trap, because the loudest topic is usually the oldest one

Every morning, a second pass compares this week's counts against the trailing eight weeks and reports movement rather than size

---

A topic at 60% heat and climbing is worth more than a topic at 90% and flat, every single time

**Step 4: the standing context files**

The sweep writes into four rolling files per client that never get deleted, only appended:

audience-pains.md, hot-questions.md, rising-topics.md, competitor-gaps.md

Every other department reads these

That is the entire point: the Radar is not a report you read, it is the shared memory the rest of the agency runs on

The self-improvement loop

After each sweep, the Reflector asks one question: which extracted items actually got used downstream this week

Items that became campaigns, hooks or client conversations are hits

Items that sat untouched for two weeks are misses

The Curator turns that into playbook deltas about what this particular audience's signal looks like:

```plaintext
# route by the SHAPE of the work, not by a price tier

orchestration:        # multi-tool chains, scrapers, sheets, schedulers
  model: kimi-k3      # MCPMark 94.5 vs 76.4, the widest margin available

research:             # open-web sweeps, competitive digging, synthesis
  model: kimi-k3      # DeepSearchQA 95.0, BrowseComp 91.2

production:           # volume drafting against a long brief
  model: kimi-k3      # 1M context holds the whole client file at once

verification:         # the Gate, different family than the writer ON PURPOSE
  model: claude-opus-5

high_stakes:          # pricing, strategy, anything a client sees unedited
  model: claude-opus-5   # rank 1 overall, and GDPval is its home turf

judge_panel:          # pre-testing, deliberately mixed families
  models: [kimi-k3, gpt-5.6-sol, qwen-3.8-max]

cleanup:              # formatting, boilerplate, extraction
  model: local
```

Within about six weeks your Radar stops surfacing noise, because it has learned what noise looks like in your specific market

That is a thing no generic tool can do for you and it is why this is worth building rather than buying

Metrics that tell you it is working

- percentage of sweeps that produce at least one item used downstream, target above 60%
- number of client conversations you started rather than received, this is the real one
- time from a topic appearing to you shipping something about it, mine is under 48 hours
What changed in my business

Clients used to bring me briefs

Now I bring them briefs, and "your audience started asking about X this week, nobody has answered it, here is the campaign" is a sentence that renews retainers without a renewal conversation

Practice: build the Radar for ONE client with fifteen sources, run it for seven nights, and on day eight read the four context files and count how many things you did not already know

**Common failures:**

- sweeping too many sources on day one. Fix: fifteen, and add only when you have read a week's output
- letting the model summarise instead of quote. Fix: make the quote a required field and reject items without one
- no velocity layer, so you keep rediscovering the same evergreen complaint. Fix: the eight week trailing comparison
**[ Department two ] ↓↓↓**

```plaintext
orchestration + research + production        ~$430
  the Radar's nightly sweeps, the Scout's screening batches,
  the Forge's campaign runs, the standing background loops

verification + high-stakes judgment          ~$280
  every Gate pass, judge panel seats, client-facing strategy

local / cheap tier                              ~$0
  cleanup, formatting, extraction

infrastructure                               ~$310
  hosting, scheduler, databases, dashboards

tools and SaaS                               ~$380
  tracking, comms, scheduling, storage, misc

TOTAL                                      ~$1,400/mo
```

## Department 2: The Scout

What it replaces: the analyst who decides what is worth your time, before you spend money on it

The universal job: every agency has a moment where it commits resources to something external, and every agency loses money on that decision more often than it admits

For me it is paying creators for reach

For a recruiter it is shortlisting

For an agency doing paid work it is publishers

For devops it is deciding which alert is real

The build

**Step 1: define the disqualifiers first**

Not the criteria, the disqualifiers

A scoring system that can only rank is useless, because everything scores something

A scoring system that can REJECT is a filter

---

**Step 2: pull the shape, not the numbers**

This is the part that separates a real Scout from a spreadsheet

Follower count is trivially bought and everyone knows it

What cannot be cheaply faked is the SHAPE of engagement: do the comments have replies, does reply depth vary, do views scale sanely with follower count, is there a tail after the spike, do the same accounts appear on every post

```plaintext
performance/
  asset_id, campaign, client, frame, format, creator,
  posted_at (local time and weekday), panel_scores,
  live_test_result, actual_views, actual_engagement,
  actual_conversions, and the delta between predicted and actual
```

This is a heavy tool-orchestration job across several platform APIs with pagination and rate limits, running hundreds of profiles per batch, which is exactly why it routes to K3 rather than to a stronger writer

**Step 3: the two-tier verdict**

Screening runs on the orchestration model

The verdict paragraph, the part a client actually reads and makes a decision on, gets a second pass on the judgment model when the money on the line is large

A wrong include on an anchor campaign costs more than every token you would save by skipping that pass

**Step 4: the roster memory**

Every entity you ever screen goes into a permanent record with its outcome

```plaintext
You are the Radar for [CLIENT], operating on [DATE]

Read the sources in sources.yaml from the last 24 hours

Extract, and only extract, the following, with a link for every item:
  PAINS      problems stated in the author's own words
  QUESTIONS  things asked more than once this week
  OBJECTIONS reasons people gave for not buying or not adopting
  PHRASES    the exact vocabulary they use, verbatim, not paraphrased
  GAPS       things asked that no competitor content answers

Rules:
  every item carries a source link and a direct quote
  never summarise a quote into your own words, quote it
  group by theme, count frequency, do not rank by your own opinion
  if a theme appeared last week, carry its previous count forward

Load playbook.md before you start and apply every entry above
medium confidence

Write to clients/[CLIENT]/radar/[DATE].md
```

**The self-improvement loop**

The Scout has the cleanest feedback signal in the whole agency, because reality grades it

Every prediction it made gets checked against what actually happened, and the gap becomes playbook entries:

```plaintext
You are the Curator for the [DEPARTMENT] playbook

Inputs:
1. the current playbook
2. this run's artifact
3. the outcome: what the reviewer changed, what the client said,
   or what the metrics did

Produce ONLY a list of delta operations. Never output a rewritten playbook

Allowed operations:
  ADD [new-id] WHEN ... THEN ... EVIDENCE ...
  HIT [existing-id]        this entry applied and helped
  MISS [existing-id]       this entry applied and was wrong or irrelevant
  AMEND [existing-id] ...  narrow or widen the condition, keep the id
  PRUNE [existing-id]      justify with the counters

Rules:
- do not ADD an entry that restates an existing one, AMEND instead
- do not ADD anything without concrete evidence from this run
- at most 3 ADDs per run, you are curating, not brainstorming
- if nothing was learned, output NOTHING, that is a valid result
```

After a few hundred screenings, your Scout is calibrated to YOUR market in a way no off-the-shelf tool can be, because it has been graded by your own results rather than by a vendor's general model

**Metrics**

- prediction error: predicted versus actual, tracked per campaign, should trend down every month
- rejection rate, which should be high, because a Scout that approves everything is a formality
- cost per verified real unit, which is the number you negotiate with
What changed in my business

I negotiate from arithmetic instead of vibes

When a creator quotes $2,000 I know within minutes whether that is a deal or a donation, and when a client asks why these forty and not those forty, I show them the analysis

Most agencies buy reach, and the ones that win buy attention

Practice: screen twenty candidates by hand, write down your reasoning for each, then build the Scout to reproduce your reasoning and run it on the same twenty

Where it disagrees with you, one of you is wrong, and finding out which is the most valuable afternoon in this whole article

**Common failures:**

- scoring without disqualifiers, so everything gets a number and nothing gets rejected
- trusting follower counts, which are the one metric that is cheapest to fake
- no roster memory, so you re-screen the same people every quarter and never learn who actually delivers
**[ Department three ] ↓↓↓**

## Department 3: The Forge

What it replaces: the writers, the producers, the people who make the thing you sell

The trap: this is the department everybody builds first and it is the one that matters least on its own, because production without verification is a liability that scales exactly as fast as your revenue does

The build

**Step 1: the input contract**

The Forge refuses to start without a complete brief

This sounds pedantic and it is the highest-value rule in the department, because most bad output is not a model failure, it is a model being asked to make something nobody had defined

---

**Step 2: the fan-out**

Production is a volume problem, not a quality problem, once the brief is right

One campaign for one of my anchor clients is around 150 assets: 40 creator briefs, 60 post drafts, 20 hook variants, launch copy, follow-ups

The pattern is a coordinator that splits the batch, spawns parallel workers, and merges

Two properties decide whether this works at volume, and both are why this seat is on K3

The first is context: the whole brief, the voice file, the claims file, the radar context and the playbook have to stay live for the entire run, and a million token window means asset 140 is written against the same complete context as asset 3 rather than against a summary of a summary

The second is endurance across a long unattended run, which is the difference between a batch you review and a batch you re-do

```plaintext
For each candidate, pull the last 30 posts and compute:

  engagement_curve      views over time per post, is there a tail
  comment_depth         percentage of comments with real replies
  commenter_overlap     percentage of commenters appearing on 5+ posts
  velocity_variance     do posts vary the way human content varies
  audience_sample       200 commenter profiles, geography and bio topic

Botted accounts have a signature: uniform likes, hollow one-word
comments, a spike with no tail, and the same 300 accounts every time

Output a verdict paragraph and a score, and always cite the metric
that drove the verdict
```

That last line is not a formality

The moment you let production reach you directly, you have re-appointed yourself as the editor, and you are the bottleneck again

**Step 3: variants by default**

The Forge never produces one of anything that matters

Hooks come in populations of twenty to thirty across different frames, openers come in threes, subject lines in fives

Variants cost almost nothing to generate and they are the raw material the Lab needs in order to test anything at all

The self-improvement loop

The Forge learns from two signals, and they teach different things

Signal one, from the Gate: every rejection reason, aggregated weekly

If the Gate keeps rejecting the same category of mistake, that becomes a playbook entry so the Forge stops making it, rather than the Gate catching it forever

Signal two, from the Lab and the real world: which assets actually performed

This is slower and more valuable, because it teaches what good looks like rather than what wrong looks like

```plaintext
clients/self/sources.yaml

signals:
  - "just launched" posts in my niche, first 48 hours
  - job posts for the role my service replaces
  - funding announcements under $10M, they buy services not headcount
  - public complaints about the exact problem I solve
  - competitors announcing price rises or layoffs
```

And this is where the skill bank earns its place

The third time the Forge builds the same type of asset, it becomes a tested skill with its own notes file, so the fourth time is a retrieval rather than a generation

My bank has roughly forty of these now, and the ones that get used weekly have notes files longer than the skills themselves

**Metrics**

- Gate pass rate on first attempt, which should climb every month, this is the single best proxy for whether your self-improvement loop is real
- assets per campaign that reach you unedited
- time from approved brief to full batch
Mine sits around 78% first-pass, up from about 50% when I started measuring, and that climb is entirely the playbook loop

**Practice**

Take one deliverable you make repeatedly, write its brief contract, and make yourself refuse to start without it for two weeks

You will discover you have been starting without a definition for years

**Common failures:**

- producing before the Radar exists, so everything is written from your assumptions about the audience
- summarising context to save tokens, which is exactly how asset 140 drifts off spec
- one output instead of variants, which leaves the Lab nothing to test
- letting production reach you directly, which quietly reinstates you as the editor
**[ Department four ] ↓↓↓**

---

## Department 4: The Gate

What it replaces: the editor, the QA lead, the person who stops embarrassing work from reaching a client

Why this is the department that decides whether you have a business: when you ship 150 assets per campaign your risk is not that the model writes badly, it writes well

Your risk is the 4% that is subtly wrong: off-voice, an unsupported claim, a compliance problem, something that reads as machine-written

At small scale you catch those yourself

At real scale, personally checking everything is the bottleneck that ends the solo model

The build

**Step 1: the four rule files**

The Gate is only as good as what it checks against, and these files are the actual intellectual property of your agency

---

The claims file is the one that saves you legally

A claim with no line in that file does not ship, no exceptions, and that rule has saved me twice

**Step 2: four independent passes**

Run them as separate checks with separate outputs, not one prompt asking for a general review, because a single blended review reliably misses one category

**Step 3: the routing rule that makes it work**

The Gate does not run on the same model family as the Forge

This is the structural decision, not a preference

My drafts come out of K3 and verification runs on Claude, both because it is a different family and because professional-deliverable judgment is where Claude measurably leads

Disagreement between families is where errors surface, and a model reviewing its own output agrees with itself for the same reasons it made the mistake

**Step 4: the return path**

Failures do not come to you

They go back to the Forge with the specific failure reasons attached, automatically, and most fix themselves on the second pass

Only work that passes reaches your queue, which means your review is a taste call on good work rather than a hunt for typos

The self-improvement loop

The Gate learns from the thing almost nobody instruments: what you overrule

Every time you pass something the Gate flagged, or kill something the Gate approved, that disagreement is the highest-signal training data in the entire agency, because it is your taste being made explicit

```plaintext
[L-012] confidence: high  hits: 22  misses: 3
WHEN the panel splits, K3 high and Claude low
THEN it usually performs, that split is our signature for
     "technically credible but not polished", which our audience likes
EVIDENCE 22 of 25 splits since May

[L-019] confidence: high  hits: 17  misses: 1
WHEN a cost_arbitrage frame runs in the first week of a month
THEN it underperforms its panel score by roughly 30%, budgets
     are already committed
EVIDENCE monthly cohort analysis, six months
```

Six months of overrides and the Gate is checking against your judgment rather than against a generic quality bar

**What to memorize:**

An automated editor with a stale rulebook is confidently wrong at scale, which is worse than being slow

The rule files are the one thing in this entire system you should maintain by hand, forever

**Metrics**

- catch rate: problems caught by the Gate versus problems you caught after it
- override rate, which should FALL over time, since a stable override rate means the loop is not running
- second-pass fix rate, mine is around 80%
**Practice**

Take fifty pieces of your own past work, run them through the Gate, and read what it flags

Everything it catches that you shipped anyway is a rule you did not know you had

**Common failures:**

- one blended review instead of four independent passes
- the Gate on the same family as the Forge, which produces polite agreement
- rule files written as adjectives, "professional but friendly" checks nothing, five real samples check everything
- not instrumenting your overrides, which throws away the best signal you have
**[ Department five ] ↓↓↓**

```plaintext
              distribution      devops           design studio    recruiting       bookkeeping
              (mine)            consultancy      

RADAR    what audiences are   what broke in    what visual       who is hiring    what rules
         asking about now     your stack's     language the      and who just     changed, what
                              ecosystem        market moved to   raised           clients keep
                                                                                  getting wrong

SCOUT    which creators       which alerts     which inbound     which candidate  which
         have real reach      are real vs      briefs are        is real vs       transactions
                              noise            worth quoting     keyword-matched  need a human

FORGE    briefs, posts,       runbooks, IaC,   concepts, decks,  outreach, briefs reconciliations,
         hooks, threads       dashboards,      copy, variants    scorecards,      statements,
                              postmortems                        shortlists       filings

GATE     voice, claims,       does it apply    brand rules,      bias, legal      rule compliance,
         platform rules       cleanly, is it   accessibility,    compliance,      arithmetic,
                              reversible       licensing         accuracy         classification

LAB      which hook wins      which fix        which concept     which message    which
         before you spend     actually holds   tests best        gets replies     categorisation
                              under load       with the ICP                       rule holds up

LEDGER   briefs, payouts,     tickets, change  files, versions,  scheduling,      documents,
         approvals, tracking  logs, on-call    approvals         pipeline, offers deadlines

RELAY    weekly client        incident comms,  presentation,     candidate and    monthly
         reports              status, SLAs     revisions, sign   client updates   statements,
                                               off                                queries
```

## Department 5: The Lab

What it replaces: the strategist's intuition, and the part of the business clients think is magic

The reframe: outcomes are treated like weather and they are not

Across hundreds of launches the same mechanical factors decide results: the hook, the format, the messenger, the timing, and the first hour

All five are testable before you spend a dollar, and every one of them can be logged

The build

**Step 1: the variant matrix**

The Forge already produces populations rather than singles

The Lab's first job is to make sure those populations span FRAMES rather than wordings, because twenty rewrites of the same idea test nothing

```plaintext
[O-008] confidence: high  hits: 15  misses: 0
WHEN a brief is sent on Friday
THEN confirmation takes 3.1 days on average versus 0.8 on Tuesday
     so schedule Friday briefs for Monday morning instead
EVIDENCE 60 briefs, Q2 and Q3

[O-014] confidence: high  hits: 11  misses: 1
WHEN a creator has missed one deadline
THEN they miss the next one 60% of the time, so move them to the
     early wave with a buffer rather than dropping them
EVIDENCE roster history, 40 creators
```

Twenty hooks across six frames beats a hundred hooks in one frame, every time

**Step 2: the judge panel**

Before anything goes live, variants are scored by a panel of models role-playing the target audience

The critical design decision: mix model families deliberately

A panel of one family is one judge with extra steps, and it will agree with itself in exactly the places it is wrong

```plaintext
rising-topics.md

theme                    this wk   8wk avg   velocity   status
cost of GPU idle time        41       12      +242%     RISING
operator fatigue             28       31        -9%     flat
migration off vendor X       19        3      +533%     BREAKING
```

Consistent winners across disagreeing judges predict real performance far better than a high average score from one

**Step 3: the small live test**

Simulation is a filter, not an answer

Top variants get quietly tested on small real audiences first, because real engagement on 5,000 followers beats any panel

Cost is nearly nothing, signal is decisive, and this step is what keeps the Lab honest

**Step 4: the performance database**

Every asset that ships lands in a structured record

```plaintext
brief-contract.yaml

required:
  client:            which client, which product
  audience:          which segment, pulled from radar context files
  goal:              the one outcome, stated as a metric
  format:            platform, length, structure
  claims_allowed:    path to the approved claims file
  voice:             path to the voice file for this output
  radar_context:     which pains and phrases this is built on
  done_when:         a test that can be checked in 10 seconds

on_missing: STOP and ask, never assume, never invent
```

That delta column is the entire department

It is what turns the Lab from a testing tool into a prediction engine that gets sharper every launch

The self-improvement loop

This department has the most direct loop in the agency, because it is explicitly in the prediction business

Every launch, the panel's predictions are scored against reality, and systematic errors become playbook entries about your specific market

---

The second one is the kind of finding no general tool will ever give you, because it is true about your market and nobody else's

**Metrics**

- panel-to-reality correlation, tracked per frame, and this should climb
- hit rate on launches, which is the number clients feel
- the cost of a test versus the cost of a failed launch, which is the argument for the whole department
Campaigns that go through the full Lab process at my agency outperform our pre-Lab launches by roughly 3x on views per dollar

Clients call that my touch, and it is a pipeline with a database attached

**Practice**

Take your last twenty shipped things and back-fill the performance database from whatever data you still have

You will find a pattern in an afternoon, and you will have a working Lab before you have built anything

**Common failures:**

- testing wordings instead of frames
- a single-family judge panel
- skipping the live test, which lets simulation quietly replace reality
- not logging the prediction, which makes the delta column impossible and the whole department decorative
**[ Department six ] ↓↓↓**

[embedded tweet: https://x.com/i/status/2062301065312407891]

## Department 6: The Ledger

What it replaces: operations, the department nobody notices until it fails, and the one that actually burns out solo operators

Nobody quits because writing was hard

They quit because of approvals, payouts, chasing, scheduling and the forty small obligations that arrive in twenty-minute pieces all day

The build

The Ledger is almost entirely tool orchestration and almost no writing, which makes it the clearest example of routing by shape: it touches your CRM, your calendar, your payment rails, your storage, your tracker and your scheduler in long chains where dropping one call silently corrupts state

**Step 1: make everything a state machine**

Every unit of work has an explicit state and one owner, and nothing exists outside a state

```plaintext
[G-063] confidence: high  hits: 12  misses: 0
WHEN slop pass flags a one-word paragraph
THEN do not flag it for this client, it is deliberate in their
     voice file and I have overruled this 12 times
EVIDENCE human overrides, campaigns 44 through 51

[G-071] confidence: high  hits: 9  misses: 0
WHEN a claim cites a client blog post rather than their docs
THEN treat as UNSUPPORTED, blog posts get edited and docs do not
EVIDENCE two claims went stale mid-campaign in July
```

The escalation timeouts are what make this run without you

An item that has been in SENT for four days pings the creator, not you

An item in SENT for eight days pings you, once, with the full history attached

**Step 2: the weekly batch**

Payments in one run, approvals in one queue, reporting on one trigger

Batching turns forty interruptions into one thirty-minute session, and the interruption cost is what actually kills solo operators, not the work

**Step 3: tag everything at creation**

Every link, asset and deliverable gets its tracking identity at the moment it is created, never later

Retrofitting attribution is impossible and everyone learns this the same expensive way

The self-improvement loop

The Ledger learns from where things get stuck

Every timeout, escalation and manual intervention is logged, and the pattern in those logs is the process defect

---

Notice these are process improvements that no human ops manager would ever find, because nobody has the patience to correlate 60 briefs against weekday of send

**Metrics**

- items requiring human intervention per week, and this must fall
- average time in each state, which shows you the real bottleneck
- escalations that turned out to need you, and if that is under half, your thresholds are too tight
My involvement in operations across nine clients is about 40 minutes a day, and that used to be two full-time jobs

Practice: write the state machine for your single most annoying recurring process, on paper, today

Half the annoyance is that it has never been written down, so every instance gets re-decided from scratch

**Common failures:**

- automating without a state machine, which produces a system nobody can debug
- no timeouts, so things sit forever and you become the timeout
- escalating everything, which is just a slower inbox
- tagging after the fact
**[ Department seven ] ↓↓↓**

---

## Department 7: The Relay

What it replaces: account management, and the reason retainers renew or do not

The line you must not cross: this is the department where automation is most tempting and most dangerous

Clients pay a person they trust

The day a client feels like they are talking to your pipeline is the day the retainer dies

The Relay exists to give you MORE hours to be present, not to be present for you

The build

**Step 1: reports generate, humans send**

The weekly report assembles itself from the performance database: what shipped, what performed, what is next, written in your voice from your voice file

You read it, change what you disagree with, and send it

Ten minutes instead of two hours, and the client still hears from you

**Step 2: the anomaly watcher, not the reporter**

A standing loop watches campaign metrics continuously and pings you only on things that are actually anomalous: a post underperforming its band, a creator missing a deadline, a spike worth amplifying while it is still hot

This is a long-horizon job, started Monday and expected to still be on task Friday without a restart, which is precisely the endurance property to route for

The bar for a ping is high, because a watcher that pings often is a notification feed and you will mute it in a week

**Step 3: meetings become context, automatically**

Every client call is transcribed, and the extraction writes decisions, commitments and constraints straight into that client's context folder

That single step means every other department knows what was agreed without you re-briefing anything, and it is the highest-leverage twenty minutes of setup in the whole system

The self-improvement loop

The Relay learns from what clients actually respond to

Which sections of your report get replies, which get questions, which get silence, and which precede a renewal conversation

```plaintext
clients/acme/scout-rules.yaml

hard_reject:
  - engagement ratio outside 0.4x to 4x of the size band median
  - comment-to-like ratio below 0.008
  - audience geography under 40% in the client's markets
  - posted paid content for a direct competitor in the last 60 days

score:
  audience_match:     0.35    # do their people match the client ICP
  engagement_quality: 0.30    # is the engagement shaped like humans
  historic_delivery:  0.25    # did they deliver for us before
  price_efficiency:   0.10    # cost per verified real view
```

That second entry is worth the price of the whole department

**Metrics**

- client reply rate on reports
- time from a problem existing to the client hearing about it from you, and this should be shorter than the time it takes them to notice
- renewal rate, the only metric that finally matters
Practice: rewrite your next client report to lead with what you learned rather than what you did, and watch the reply

**Common failures:**

- sending anything client-facing unread
- an anomaly watcher with a low bar, which becomes noise you ignore
- automating the relationship rather than the reporting
**[ Filling the pipeline ] ↓↓↓**

```plaintext
[F-041] confidence: high  hits: 19  misses: 1
WHEN writing for a technical audience
THEN open with the number, not the context, they scroll past setup
EVIDENCE 19 of 20 top-performing posts since June opened on a figure

[F-055] confidence: medium  hits: 8  misses: 3
WHEN a creator's history shows first person storytelling
THEN never brief them with a structured outline, give them the
     insight and let them frame it
EVIDENCE briefs 88-96, structured ones came back flat
```

## Acquisition: The Agency That Markets Itself

Every article like this tells you how to run an agency and skips how to fill one, which is the part that actually decides whether you have a business

The good news is that you already built the machine that does it, you just pointed it at clients instead of at yourself

Point the Radar at your own funnel

Add one more client to your Radar and make it you

Your sources are wherever your buyers complain out loud: launch announcements in your niche, funding news, job posts for the role you replace, and threads where someone says the thing your service fixes

---

The Radar flags each one with context, which turns outreach from cold into almost rude not to send, because you are writing to someone about a thing they said this week

The proof engine

Every campaign you run is content you already paid to produce

The loop, and it is the same shape as everything else in this article:

- the work happens, and the Ledger already logged what shipped and what it did
- a weekly job pulls the most interesting result and drafts the post about it
- the Gate checks it against your claims file, because your own marketing needs the same discipline as a client's
- you approve, and it publishes
My largest clients found me through posts about work I did for much smaller ones, which is the whole argument for showing the work rather than describing the service

The close that nobody else can do

Competitors sell a team of people

You can show a machine

When a prospect asks how you deliver, open the dashboard: the Radar output for their niche, the Scout scores, the Lab's prediction accuracy, the Gate's catch rate

Nobody in your category can show that, and it reframes the conversation from price per deliverable to access to a system

**The referral economics that only work at this margin**

At 90%+ margins you can pay referral fees that a staffed agency literally cannot afford

I pay well above the going rate, and my happiest clients moonlight as my sales team, which costs me nothing until it works

**The self-improvement loop**

Track which proof posts produced inbound, and which outreach context actually got replies

```plaintext
states/creator-brief.yaml

DRAFTED    -> SENT        automatic when the Gate passes it
SENT       -> CONFIRMED   on their reply, parsed, not manually read
CONFIRMED  -> DELIVERED   when the tracked link goes live
DELIVERED  -> VERIFIED    checks the deliverable matches the brief
VERIFIED   -> PAID        enters the weekly payment batch
any state  -> ESCALATED   on timeout, and each state has its own
```

Practice: add yourself as a Radar client this week, and send five pieces of outreach built entirely on things your prospects said in the last seven days

**Common failures:**

- building all seven departments before getting a single client, which is a very sophisticated way to procrastinate
- posting descriptions of your service instead of results from your work
- skipping the Gate on your own marketing, which is how an unsupported claim ends up on your own timeline
**[ The money ] ↓↓↓**

```plaintext
[R-009] confidence: high  hits: 14  misses: 0
WHEN a pain is stated as a comparison to a competitor
THEN it converts to a campaign angle far more often than a
     standalone complaint
EVIDENCE 14 of our last 16 shipped angles came from comparisons

[R-022] confidence: medium  hits: 5  misses: 1
WHEN a question appears in YouTube comments but not on Reddit
THEN it is usually a beginner question, tag it as top-of-funnel
     rather than as a product gap
EVIDENCE three false "product gaps" traced back to this in August
```

## The Unit Economics at $78k

Real numbers, current month, so you can size this before you commit

**Revenue: $78,000**

Nine clients:

- 3 anchor clients on $15,000/mo retainers = $45,000
- 5 growth clients on $5,000/mo campaign retainers = $25,000
- performance bonuses and affiliate arrangements = $8,000
**Costs:**

```plaintext
VOICE     score against this specific voice file, 0-100, cite the
          lines that miss and quote the sample they should match

CLAIM     extract every factual statement, match each to a claims
          file line, output UNSUPPORTED for anything unmatched
          no source, no ship, and this pass has no discretion

SLOP      adversarial pass: find the tells, the summary ending, the
          rhetorical question opener, the tricolon, the corporate
          hedging, the em dash habit

PLATFORM  mechanical only: length, structure, link placement,
          formatting rules for this channel
```

That is roughly 98% gross margin on the operation, before creator payouts, which are client campaign budgets flowing through rather than my cost

The number that actually matters is not the margin, it is the shape of the cost curve

When my revenue went from $40k to $78k, my costs went up by about $600

Btw, here's my previous version of workflow for my solo-agency (it's been improved much)

```plaintext
skills/
  creator-brief-from-radar/
    SKILL.md          what it does, when to use it, inputs, outputs
    run.py            the executable part, if there is one
    tests/            the unit tests that gate registration
    notes.md          accumulated observations from real runs
```

There is no version of that with people, because doubling a staffed agency means roughly doubling payroll, which is why staffed agencies grow revenue and stand still on profit

And the honest version of the model-cost line, because the previous version of this article made a claim I want to correct

I used to justify the routing on price, and that was lazy reasoning that happened to reach the right answer

The correct reasoning is that the orchestration and research seats do work whose benchmark leader is not the same model as the judgment seat, and putting the wrong model in either seat costs more than the token difference in both directions

Running the Radar and the Scout on a general-purpose frontier model would give me worse tool-chain completion and worse search, and I would pay more for that privilege

Running the Gate on the orchestration model would save a little and cost me the thing the Gate exists for

The routing is a capability decision that happens to also be cheaper, and if the prices inverted tomorrow I would not change a single line of it

**Starting from zero, the honest number**

You do not need $1,400 a month to begin

At one or two clients, running the Radar nightly on a single niche, a Forge that produces a handful of deliverables a week and a Gate on top of it, the model spend lands somewhere around $40 to $80 a month, plus whatever hosting and scheduling you already pay for

The costs in the table above are the shape of a business at nine clients, not the entry price

The entry price is a weekend and about the cost of a dinner

**[ The build order ] ↓↓↓**

```plaintext
rules/
  voice/[client].md      how this client and each creator sounds,
                         with 5 real samples, not adjectives
  claims/[client].md     every factual statement you are allowed to
                         make, each with a source link
  platform/[channel].md  length, format, link placement, what gets
                         throttled
  slop.md                the tells of machine writing, maintained
                         from your own real failures
```

## The 12-Week Build Order

If I started again on Monday, this is the exact sequence, and the order is not arbitrary: each one makes the next one cheaper to build

**Weeks 1 and 2: the two mechanisms**

Playbook format, Curator prompt, skill bank structure, promotion rule

Do not build a department yet

Run the mechanisms manually against one process you already do, so you learn what a good delta looks like before seven departments start writing them

**Weeks 3 and 4: the Radar**

Fifteen sources, nightly sweep, velocity layer, four context files

Highest leverage first system, because every later department reads its output

**Weeks 5 and 6: the Forge, on Radar context**

Brief contract first, fan-out second, variants by default

Resist shipping anything to a client from it yet

**Week 7: the Gate**

Write the four rule files, wire the four passes, put it on a different model family, build the return path

This is the week most people skip and it is the week that decides whether you end up with a system or a hobby

**Weeks 8 and 9: the Scout**

Disqualifiers, shape analysis, two-tier verdict, roster memory

Calibrate against twenty candidates you screen by hand first

**Week 10: the Ledger**

State machines, timeouts, weekly batch, tag at creation

Boring, and it returns more hours than everything above it combined

**Week 11: the Lab**

Frames file, judge panel across families, small live tests, performance database

Back-fill the database from your last twenty shipped things on day one

**Week 12: the Relay**

Report generation, anomaly watcher with a high bar, meeting extraction into context

Then, permanently: every time you catch yourself doing something for the third time, stop and turn it into a loop, and every Friday read the seven playbooks and delete what is wrong

That Friday hour is the actual job now

**[ The honest part ] ↓↓↓**

```plaintext
[C-006] confidence: high  hits: 9  misses: 0
WHEN a report leads with what we learned rather than what we shipped
THEN reply rate roughly triples and the reply is usually strategic
EVIDENCE 9 of 9 since we changed the template in June

[C-011] confidence: medium  hits: 4  misses: 1
WHEN a campaign underperforms and we flag it before the client sees
     the numbers
THEN it does not become a renewal risk, and when they find it first
     it does
EVIDENCE four saves, one loss where we waited
```

## The Honest Limits

Every article like this is a sales pitch unless it names where the model strains, so here is where mine does

Taste does not automate. The Gate catches wrong, it does not catch mediocre-but-safe

The call on "shippable" versus "actually good" is still mine, and if I skipped that review for a month, quality would drift and no error message would ever tell me

Relationships do not automate. Anchor clients pay $15k a month to a person

The systems buy me hours to be more present, not absent, and the moment that inverts the business dies quietly over one quarter

Self-improvement is not self-supervision. The playbooks get better at what you measure, and they will happily optimise into a corner if what you measure is wrong

A department with a great playbook and a bad metric is a very efficient way to go in the wrong direction

The rule files rot. An automated editor with a stale rulebook is confidently wrong at scale, and those files are maintained by hand, by me, from real failures, forever

Cold starts are genuinely bad. Every loop in this article is worse than a competent human for the first three to four weeks, because it has no playbook yet

If you judge the system on week one you will turn it off correctly and for the wrong reason

And this does not scale infinitely. Every department is another playbook to read and another rule file to maintain

Seven is manageable by one person

I do not believe fifteen would be, and I would rather run seven excellent loops than fifteen neglected ones

**[ What it adds up to ] ↓↓↓**

## CONCLUSION

The thing worth taking from all of this is not my numbers, and it is not the model routing, which will be out of date within a year

It is the reframe

An agency was always just information flows wearing salaries

Research flows into strategy, strategy into production, production into review, review into publishing, publishing into analysis, and analysis back into strategy

We staffed those flows with people because there was no other option, and now there is, and the operators who see their business as flows rather than as a team are quietly running circles around the ones still hiring like it is 2019

Nine seats of a traditional org at my scale is somewhere around $45,000 to $55,000 a month in salaries

Mine costs about $1,400, and the difference is not that I found cheaper labour, it is that I stopped buying labour and started building loops

**Three things I actually want you to do:**

Build the two mechanisms before you build a single department, because a department without a playbook is a tool and a department with one is an employee that gets better every week

Build the Gate before you build volume, because production without verification just lets you be wrong faster and more expensively

And put each job on the model that wins that job, then check that with numbers rather than habit, because the default choice is almost never the right one twice in a row

The first version of this will be worse than you doing it yourself

Week four is where it turns, and week twelve is where you stop being able to imagine going back

Most people still think an agency is a team

And most of the readers will think that I fake my MRR for engagement, that's for you: 

---

Go prove them wrong ❤️


## Media

![](media/cover.jpg)

Originals:
- media/cover.jpg: https://pbs.twimg.com/media/HRnW6t_WgAAQCAH.jpg

## Links

- https://arxiv.org/abs/2510.04618
- https://arxiv.org/html/2605.27366v1
- https://benchlm.ai/frontier-ai-models
- https://codersera.com/blog/kimi-k3-benchmarks-comparison-2026/
- https://codingfleet.com/blog/claude-opus-5-vs-kimi-k3/
- https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems
- https://x.com/i/article/2096907368365744130
- https://x.com/i/status/2062301065312407891
