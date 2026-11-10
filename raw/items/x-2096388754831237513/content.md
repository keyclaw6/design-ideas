# LinkedIn sender fleet: you need a FLEET of sender accounts, not DMs from one account

> Source: https://x.com/DinScales26/status/2096388754831237513
> Author: Din (@DinScales26)
> Posted: 2026-09-06T00:03:22Z
> Stats (at capture): 7,654 views · 38 likes · 0 replies · 4 reposts · 60 bookmarks · 0 quotes
> Captured: 2026-09-21T14:35:05Z

## Post

to succeed on linkedin, you cannot just be sending DMs from one account...

you need a FLEET of sender accounts.

everything is broken down in this article:

## Media

![](media/thumb_0.jpg)
[media/media_0.mp4](media/media_0.mp4)

19.7s video (`media/media_0.mp4`, 1920×1080, 6.5 MB) + thumb (`media/thumb_0.jpg`, 70 KB). Original: https://video.twimg.com/amplify_video/2096387955938275328/vid/avc1/1920x1080/7_p9y49itdzx8NZZ.mp4?tag=29
Thumb original: https://pbs.twimg.com/amplify_video_thumb/2096387955938275328/img/n4XlVqraCzRUIxP0.jpg

## Quoted post

[Din (@DinScales26)](https://x.com/DinScales26/status/2096306903416521206) — 2026-09-05T18:38:07Z · 14,876 views · 29 likes · 1 replies · 4 reposts · 71 bookmarks · 1 quotes

https://x.com/i/article/2095955475623718914

Quoted X Article: **how we built a linkedin sender fleet that pushes 10,000+ DMs** (https://x.com/i/article/2095955475623718914)

one linkedin account sends around 30 dms a day before it gets restricted.
we push 10,000+ across our clients at eaglerev, and the volume comes from how the fleet is built.
this is the full build...

one linkedin account sends around 30 dms a day before it gets restricted.

we push 10,000+ across our clients at eaglerev, and the volume comes from how the fleet is built.

this is the full build...

[image]

### why a fleet instead of an account:

[image]

every meaningful limit on linkedin applies per account.

- connection requests cap near 100 a week

- connection based messaging caps around 30 a day

- inmail credits come with the seat rather than the operation

pushing a single account past those numbers gets it restricted, 

so more volume through one profile is unavailable at ANY price.

the arithmetic runs the other way instead.

a safe daily volume per account, multiplied across a warmed fleet, 

running every working day, produces the number.

each account stays well inside its own limits, which keeps the whole fleet sending.

so run the arithmetic before building anything.

if you need 10,000 messages a month and each account safely carries 500, that is 20 accounts, plus a buffer for the ones resting or warming.

budget 25 to have 20 sending on any given day.

[image]

### sourcing and preparing the accounts:

a profile created this month CANNOT carry load.

what every account needs before it sends anything:

- age and real history, meaning an account that has existed for months rather than weeks

- a real photo of a real face, well lit, filling most of the frame

- a headline naming the outcome the person creates, with a number in it where possible

- an about section in first person, 3 or 4 short paragraphs

- 2 or 3 experience entries with dates that make sense

- 500+ connections

- a custom url rather than the string of numbers linkedin assigns

- some recent posts and comments

the profile does the pre-selling.

a prospect who receives a cold message opens the profile before deciding what to do with it, 

and an empty one raises the chance of a report.

on infrastructure, each account gets its own clean ip, kept CONSISTENT.

an account logging in from 3 countries in a week is a stronger signal to linkedin than any volume metric.

match the ip to the profile's stated location too.

an account with a london headline logging in from a data center in another region is a mismatch the platform can read.

residential connections hold up better than data center ones, 

and a consistent ip beats a high quality one that changes.

[image]

### the warmup ramp:

[image]

a new account sending at full volume gets flagged inside days.

the ramp runs 3 to 4 weeks per account:

- week 1. activity only. 5 to 10 connection requests a day, 15 to 20 profile views, likes and comments on feed posts, 1 or 2 posts published. ZERO cold messages.

- week 2. 15 to 20 connection requests a day. messages only to people who have accepted, and only conversational ones. continued posting.

- week 3. 25 to 30 connection requests a day. first cold messages at low volume, heavily varied. open profile inmails start here.

- week 4 onward. operating volume, held steady.

stagger the start dates across the batch.

100 accounts activating on the same monday is a pattern regardless of what each one does individually.

keep a batch warming continuously so replacements are ready before you need them.

what to watch during the ramp itself:

- acceptance rate on the early connection requests, since under 20% means the targeting is wrong before you have sent a single cold message

- whether the profile gets any inbound views, which indicates it reads as real

- any early warning banner, which means the ramp was too fast

if an account struggles in week 2, hold it at week 2 volumes for another week.

[image]

### routing the volume:

connection requests are the most restricted action, so we route around them.

where our volume goes:

- open profile inmails, which need no connection request and spend no credit

- inmail credits, refunded whenever the recipient replies within 90 days

- event attendee messages, free once you register for the same event

- event invites, on their own weekly allowance of around 1,000

- connection requests, reserved for closed profiles at accounts worth the slot

on one campaign, 4,705 of 4,905 sends were inmails and connection requests carried 200.

the refund rule changes the economics of the whole fleet.

a message that earns a reply costs nothing, so reply rate governs how much the fleet can send.

that puts the copy work and the sending budget in the same place.

check open profile status during list building.

it turns 2 separate campaigns into one list with a routing rule, 

and it stops you spending connection requests on people you could have reached free.

[image]

### pacing and monitoring:

[image]

linkedin scores behaviour, so pacing carries as much weight as the numbers.

how we run the sending:

- activity spread across working hours in the account's own timezone

- randomized gaps between actions rather than fixed intervals

- weekends lighter than weekdays

- volume distributed evenly across the fleet, so no single profile spikes

what gets monitored per account, weekly:

- acceptance rate, healthy above 30% and a problem under 20%

- reply rate, since replies are the strongest positive signal linkedin has

- spam reports and "i don't know this person" flags

- any warning banner, temporary lock, or identity verification prompt

restrictions arrive in tiers, meaning a warning, then a temporary lock, 

then an identity check, then a permanent ban.

an account that receives a warning leaves rotation for 2 weeks.

sending through the first signal is how profiles get lost permanently, 

and a 2 week pause costs a fraction of rebuilding an aged account.

what to do with an account coming back from a rest:

- restart at week 2 volumes rather than where it left off

- send only to your highest fit segment for the first week back

- watch acceptance rate daily rather than weekly

an account that gets a second warning inside a month comes out of the fleet ENTIRELY.

[image]

### the copy layer that protects the fleet:

identical message bodies across thousands of recipients get pattern matched and reported fast.

what varies on every send:

- 3 to 5 versions of each line, rotated across the batch

- name, company, role, and trigger pulled in as variables from enrichment

- sentence order shifted between versions

- the ask rotated across an opinion, a document, and a referral question

qualification runs before any of it.

a model reads every profile against the icp and drops the ones that miss, with a written reason attached.

sending to people with no reason to hear from you generates reports, and reports do more damage than any volume metric.

so relevance protects the fleet while it lifts the reply rate.

on follow-ups, 2 maximum on a silent thread.

3 to 4 days after the first, then 7 to 10 days after that, each carrying something new.

a fourth message into silence is where reports come from, 

and one report costs more than the reply that message was never going to get.

[image]

- din

also, DM me "SENDER" if you want us to run this exact linkedin outbound system and cold email for your business ...

(must be making over $10k/month)

we've done this for over 140 companies across 30 industries

or just book a call @ calendly.com/eaglerev/eaglerev-strategy-ca

[image]

## Author bio (at capture)

Scaling Offers https://calendly.com/eaglerev/eaglerev-strategy-call
Website: http://eaglerev.io

## Thread

None (`replying_to` null). No author self-replies recovered via bridge (0 reply articles visible).

## Comments

0 replies per API. 0 visible. Bridge (logged-in, own tab, page URL verified before every extract, 3–8 scroll rounds per tweet): conversation returned only the main-post `<article>`; 0 reply `<article>` elements visible on any of the 15 tweets (one transient 2nd `<article>` on 2097738059844657256 was the embedded X-Article card, not a reply). A loading skeleton sat unresolved behind the reply position; reload did not resolve it — conversation endpoint not serving children to this session. fx/vx APIs return counts only, no reply list. `r.jina.ai` on `x.com`: AbuseAlleviation 403; on `fixupx.com`: login wall.

## Links

- https://x.com/DinScales26/status/2096306903416521206
- https://x.com/i/article/2095955475623718914
