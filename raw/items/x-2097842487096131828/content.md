# Lemlist $1K to $28M/yr bootstrapped: cold email technical system across 140 B2B companies

> Source: https://x.com/draprints/status/2097842487096131828
> Author: Dra (@draprints)
> Posted: 2026-09-10T00:19:59Z
> Stats (at capture): 5,554 views · 37 likes · 10 replies · 6 reposts · 59 bookmarks · 0 quotes
> Captured: 2026-09-21T14:35:05Z

## Post

guillaume moubeche started lemlist with $1,000 and took it past $28M/year...

he did this all bootstrapped AND turned down a $30m investment.

while doing this, he analyzed 400+ million cold emails sent across 100+ countries.

and they found that the #1 reason people fail at cold email is because they lack the technical knowledge.

so that is what i wrote this article on:

- secondary domains only
- authentication on every one
- 2 to 3 weeks of warmup
- verification before every send
- placement checked weekly per mailbox
- etc

we've run this whole system across 140 different B2B companies.

## Media

![](media/media_0.png)

Photo (`media/media_0.png`, 736×416, 354 KB). Original: https://pbs.twimg.com/media/HR0IcofXwA8bFW4.png?name=orig

## Quoted post

[Dra (@draprints)](https://x.com/draprints/status/2096405966770028822) — 2026-09-06T01:11:46Z · 14,940 views · 45 likes · 10 replies · 2 reposts · 83 bookmarks · 2 quotes

https://x.com/i/article/2094188082308280320

Quoted X Article: **breaking down the cold email system we've run for 130+ B2B clients** (https://x.com/i/article/2094188082308280320)

cold email runs alongside linkedin in our system at eaglerev.
linkedin reaches the senior people and anyone whose address you cannot find. 
email carries the raw volume and reaches the founders and

cold email runs alongside linkedin in our system at eaglerev.

linkedin reaches the senior people and anyone whose address you cannot find. 

email carries the raw volume and reaches the founders and operators who live in their inbox.

this is the email side, end to end...

[image]

### the infrastructure layer:

[image]

the client's primary domain never sends cold email.

everything runs on secondaries, bought and configured separately.

how we build it:

- generate 100 to 200 variations of the brand name

- bulk search them, taking whatever is available

- 2 to 3 mailboxes per domain, with 3 being the ratio at volume

- point each secondary at a redirect to the main site, since a domain resolving to nothing is a signal

- keep the names close enough to the brand that a curious prospect finds something coherent

- skip numbers, hyphens, and stuffed keywords

every mailbox needs spf, dkim, and dmarc configured correctly.

set dmarc to none through the ramp, 

since a strict policy on a domain with no sending history creates failures before the reputation exists to absorb them.

we spread across providers deliberately, roughly 80% google and 20% microsoft, adjusted to where the buyers are.

an outlook heavy market shifts that ratio.

esp matching lifts placement where volume justifies segmenting the list, 

meaning google sending to google inboxes and microsoft to microsoft.

on the domain names themselves, keep a mix.

.com carries the highest price of the common extensions, and .xyz or .info cut the bill meaningfully once you are buying in volume.

buy across 2 registrars, so a single account issue never takes the whole sending operation offline.

[image]

### warmup and volume discipline:

a new mailbox sending at full volume gets flagged.

the ramp runs 2 to 3 weeks minimum:

- start at a trickle per mailbox and climb weekly

- stagger start dates across the batch rather than activating everything on one monday

- keep warmup traffic running underneath live campaigns permanently

- spread sends across working hours with irregular gaps

per-mailbox volume stays low forever.

the daily total comes from the NUMBER of mailboxes, 

so work backwards from the target volume and the domain count falls out of it.

keep a batch warming continuously. 

correctly configured inboxes still degrade at 6 to 9 months, and a replacement started the day one burns is 3 weeks late.

a rotation that holds: 

roughly 20% of the fleet warming at any time, the rest sending, and the oldest domains retired on schedule rather than when they fail.

[image]

## the list layer:

[image]

the cleanest infrastructure BURNS on a bad list.

what runs before any send:

- qualification first, meaning a model reads each company against the icp and returns keep or drop with a written reason

- enrichment second, through a waterfall, since single source covers 50 to 60% and stacked reaches 85%+

- verification third, keeping bounce rate under 1%

- a second verification pass on catch-all domains, which report as valid and bounce anyway

- role-based addresses stripped, meaning info@, sales@, and support@ on any list where you want a named person

- deduplication against everyone already contacted

the order carries more weight than the tools.

enriching contacts at companies you were always going to drop burns credits on roughly half the file.

read the drop reasons in bulk before the enrichment step runs.

when a few thousand records get cut for the same cause, the icp needs adjusting, 

and you found that before spending anything on the file.

then expect roughly 0.7 of the raw pull to survive qualification, enrichment, and verification.

plan your send volume against that number.

then the suppression list:

- everyone who replied, in either direction

- current clients and anyone in an active deal

- every opt-out request

- domains already exhausted in previous campaigns

an unsuppressed list means one prospect receiving 3 campaigns from 3 of your domains, which turns a warm contact into a complaint.

[image]

### the message:

the email gets read on a phone between meetings, same as the linkedin message.

4 lines:

- the trigger, meaning something real and recent about them

- the problem that creates, in the words their team uses internally

- 1 result from a comparable company, with the number and the timeframe

- 1 small ask, answerable in a word

under 400 characters, 1 question, no links in the first email.

the subject line stays under 40 characters, plain and specific to them.

we have run the identical structure above 20% reply rate and watched it produce 3%, with the case study in the brackets as the only variable.

a result from a company the prospect recognises as their own kind makes them read themselves into it.

a result from one industry over gets them to decide it does not apply, and they stop at line one.

so the proof you hold tells you which market to point the campaign at.

then the variation layer, since the same message goes out thousands of times:

- 3 to 5 versions of every line, rotated across the send

- trigger, company, role, and industry pulled in as variables from enrichment

- the ask rotated across an opinion, a document, and a referral question

on cadence, 2 follow ups. 3 to 4 days after the first, then 7 to 10 days after that, each carrying something new.

then the thread closes and the lead returns to the list for a later quarter.

[image]

### campaign settings and monitoring:

[image]

what holds at volume:

- open tracking off, since the pixel damages placement and returns nothing actionable

- plain text only

- randomised start times, given every sequencer defaults to 9am

- monday to friday sending

- auto replies counted in the stats as a placement gauge

- sequence starts maxed, since the first email to a fresh contact outperforms every follow-up

monitoring runs weekly at the individual mailbox level:

- bounce rate per campaign

- reply rate per mailbox, since silence usually means spam placement

- blacklist status across the domains

- seed inbox results from live campaigns

any mailbox with placement issues comes out of rotation that day. 

any blacklisted domain gets retired.

reading the failure signals:

- every campaign dropping at once points at infrastructure

- bounces climbing on a verified file means the data source degraded

- auto replies disappearing means you stopped reaching real inboxes

- a single mailbox at zero replies for a week is almost certainly filtered

the diagnostic order matters when something breaks.

check placement first, then the list, then the copy.

rewriting copy while the mail sits in spam produces a month of wasted work and no information.

[image]

### how it connects to linkedin:

we run both surfaces on the same prospect.

some people live in their inbox and never open linkedin, 

and there is no way to tell which from the outside.

the sequence:

- a linkedin touch first for senior contacts, usually an open profile inmail

- a short email 3 days later on the same problem

- a linkedin follow-up if they viewed the profile or engaged

- a final email with a different angle

each touch names a consistent problem, so the prospect sees one coherent approach.

the order flips by prospect. 

a founder who runs their business from their inbox gets email first.

then every reply gets worked within the hour, with one named owner per thread, 

qualification completed in the conversation, and a real human on the phone with anyone interested.

across 140+ companies and 30 industries, the campaigns that produced nothing were rarely short of conversations.

they were just losing the ones they already had.

track reply rate by segment.

1 or 2 segments usually carry a campaign, and the aggregate number hides which, 

so the volume ends up spread evenly across segments that deserve wildly different attention.

track interested rate alongside it. 

a segment replying often with no interest is a segment writing polite rejections.

[image]

- dra

also, DM me "EMAIL" if you want us to run this cold email system in addition to linkedin outbound for your B2B business ...

(must be doing over $10k/month)

we've done this for over 140 companies across 30 industries

or just book a call @ calendly.com/eaglerev/eaglerev-strategy-call

## Author bio (at capture)

increasing deal flow for firms selling expensive products & services @ http://eaglerev.io
Location: run linkedin at scale ➡️ 
Website: http://inmailer.ai

## Thread

None (`replying_to` null). No author self-replies recovered via bridge (0 reply articles visible).

## Comments

10 replies per API. 0 visible. Bridge (logged-in, own tab, page URL verified before every extract, 3–8 scroll rounds per tweet): conversation returned only the main-post `<article>`; 0 reply `<article>` elements visible on any of the 15 tweets (one transient 2nd `<article>` on 2097738059844657256 was the embedded X-Article card, not a reply). A loading skeleton sat unresolved behind the reply position; reload did not resolve it — conversation endpoint not serving children to this session. fx/vx APIs return counts only, no reply list. `r.jina.ai` on `x.com`: AbuseAlleviation 403; on `fixupx.com`: login wall.

## Links

- https://x.com/draprints/status/2096405966770028822
- https://x.com/i/article/2094188082308280320
