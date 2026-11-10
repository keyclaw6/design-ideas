# Some mistakes you might be making:
> Source: https://x.com/mattpocockuk/status/2109973273924579720
> Author: Matt Pocock (@mattpocockuk)
> Posted: Tue Oct 13 11:43:24 +0000 2026
> Captured: 2026-10-15T09:02:28+00:00
> Stats at capture: 197,198 views · 3,940 likes · 266 replies · 241 reposts · 3,380 bookmarks · 58 quotes

## Post

Some mistakes you might be making:

Your effort level is too high
Your skills are too long
You're not aligning before you start work
You're aligning too often, and too hard
Your automated checks are too lax
Your custom tooling is too token-inefficient
You aren't doing enough automated review
You aren't reviewing previous coding sessions (with an agent)
You're doing too much human review
You aren't vibe coding enough prototypes
Your agent can't verify its own work
You're babysitting the agent too much
You've overloaded your global steering files
Your codebase is hard to navigate
You aren't building a shared language
Your codebase architecture allows bad tests to be written
You aren't thinking strategically enough
You aren't thinking enough

## Thread

### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2109973745053929735)) — 2026-10-13T11:45:16+00:00

If you think you might be making some of these mistakes, ask me how you can improve and I'll help
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2109973894866104408)) — 2026-10-13T11:45:52+00:00

Definitions of various terms here:

https://t.co/28UlV9Mjtz
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2109975055883247831)) — 2026-10-13T11:50:29+00:00

@diancodes If exploring your codebase costs 100K tokens
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2110270455525560727)) — 2026-10-14T07:24:18+00:00

@jbezford Monorepo is usually better - single commit history, single directory.

But TBH agents can do fine working across multiple repos too.
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2110340053989773625)) — 2026-10-14T12:00:51+00:00

@tom_13z It sounds like you're expecting too much of agents

They're not mind-readers, and never will be
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2110001628497477754)) — 2026-10-13T13:36:04+00:00

@Douglance @acoyfellow IMO "You're running evals" would be a mistake I'd add
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2110001811058765938)) — 2026-10-13T13:36:48+00:00

@Acezhang01 Lol that's how it goes

It's task-dependent. You shouldn't align hard on small diffs. Just create the diff, then align afterwards.
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2110270656105631834)) — 2026-10-14T07:25:06+00:00

@JoshuaSega1 https://t.co/dh6hnFu2qT
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2109975229657497965)) — 2026-10-13T11:51:10+00:00

@manvankaliber The tweet is a prompt
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2109974133798797670)) — 2026-10-13T11:46:49+00:00

@asmirkn Every week, on a schedule:

"/writing-for-agents find ways to cull my global steering files"
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2110637063938687322)) — 2026-10-15T07:41:04+00:00

@revengeteh Absolutely
### Matt Pocock ([@mattpocockuk](https://x.com/mattpocockuk/status/2109974555783766311)) — 2026-10-13T11:48:30+00:00

@ashkaidev Clank clank

## Comments

### Dian ([@diancodes](https://x.com/diancodes/status/2109974612910002568)) — 2026-10-13T11:48:43+00:00

@mattpocockuk how do you tell your effort level is too high?
### Jake Beresford ([@jbezford](https://x.com/jbezford/status/2110186263277924810)) — 2026-10-14T01:49:45+00:00

@mattpocockuk Do you have a take or vibe on whether agents perform better in a monorepo/monolith vs. polyrepo/microservices?
### Tom S ([@tom_13z](https://x.com/tom_13z/status/2110339409069662343)) — 2026-10-14T11:58:17+00:00

@mattpocockuk Why is the cause of every AI problem “you’re not holding it right” instead of “AI ain’t all that smart?”

If I have to utter magic words to get it to work, then it is snake oil.
### Doug Lance ([@Douglance](https://x.com/Douglance/status/2109981261812887663)) — 2026-10-13T12:15:09+00:00

@mattpocockuk @acoyfellow You're not running evals.
### Acezhang ([@Acezhang01](https://x.com/Acezhang01/status/2109977184320532673)) — 2026-10-13T11:58:56+00:00

@mattpocockuk half these cancel each other out lol. how do you know when you've hit "aligning too hard"?
### Josh ([@JoshuaSega1](https://x.com/JoshuaSega1/status/2110150943060926897)) — 2026-10-13T23:29:24+00:00

@mattpocockuk What’s meant by build a shared language? Is the language stored somewhere explicitly? Examples would be awesome
### Jack van der Bilt ([@manvankaliber](https://x.com/manvankaliber/status/2109973723696832876)) — 2026-10-13T11:45:11+00:00

@mattpocockuk Now how can I fix all of this in one prompt?
### Asmir ([@asmirkn](https://x.com/asmirkn/status/2109973696131785167)) — 2026-10-13T11:45:05+00:00

@mattpocockuk the global file only ever grows bro, every time the agent screws up you add one more line to stop it and nobody ever goes back and deletes any
### Chris | TehRevenge ([@revengeteh](https://x.com/revengeteh/status/2110590608805179486)) — 2026-10-15T04:36:28+00:00

@mattpocockuk Am I able to use the skills you made in a project I'm already pretty deep into?
### ashkaidev ([@ashkaidev](https://x.com/ashkaidev/status/2109973953426911241)) — 2026-10-13T11:46:06+00:00

@mattpocockuk Which of these do you see people mess up the most?
### Ling ([@ling97091](https://x.com/ling97091/status/2110413068010455308)) — 2026-10-14T16:50:59+00:00

@mattpocockuk Hey Matt, most of my team is vibe coding without following engineering principles, and things seem fine in the short term. I try to follow the principles you advocate, but keep getting pushback. It’s frustrating. Any advice?
### Sankalp Mukim ([@sankalpgotbaned](https://x.com/sankalpgotbaned/status/2110252062382620878)) — 2026-10-14T06:11:12+00:00

@mattpocockuk have you tried the 'install-anti-slop' skill by Dillion Mullroy (Ex- OpenAI employee xD)?

Some of these things (like codebase architecture) would be a lot easier if they were codified in skills themselves
### Shelton Louis ([@SheltonLouisGT](https://x.com/SheltonLouisGT/status/2110024921183125612)) — 2026-10-13T15:08:38+00:00

@mattpocockuk I can't self critique on any of these things! I do need to align better! I keep getting results that I don't want! Not because the code is bad but it isn't what I wanted.
### carc ([@marctytus](https://x.com/marctytus/status/2110157633810243867)) — 2026-10-13T23:55:59+00:00

@mattpocockuk calling me out like this publicly pretty rude
### Kevin Rajan ([@_kvnloo](https://x.com/_kvnloo/status/2110009344846639256)) — 2026-10-13T14:06:44+00:00

@mattpocockuk hi matt, do u ever do live coding sessions? could be a vibeee
### Djara Colman ([@DjaraColman](https://x.com/DjaraColman/status/2110266789737492953)) — 2026-10-14T07:09:44+00:00

@mattpocockuk forgot "You are poor so you can not use enough tokens"
### shin ([@shin86dev](https://x.com/shin86dev/status/2109991766896296144)) — 2026-10-13T12:56:53+00:00

@mattpocockuk i have a friend who camps fable5.1-xhigh as his daily driver and 😭😭
### Devin ([@imn0tdevin](https://x.com/imn0tdevin/status/2109993519465304356)) — 2026-10-13T13:03:51+00:00

@mattpocockuk what is you suggestion in terms of the effort level?!
### Billi Ramirez ([@billiramirezdev](https://x.com/billiramirezdev/status/2110028328778559904)) — 2026-10-13T15:22:10+00:00

@mattpocockuk You have all the possible connectors enabled too.
### Chris Cardenas ([@cardechr](https://x.com/cardechr/status/2109987913693843495)) — 2026-10-13T12:41:34+00:00

@mattpocockuk In an enterprise(my current situation) setting it's not as easy as to just change the architecture (this is an internal issue, I know). Are there ways to improve agent written unit/integration/regression testing?
### Vishnu Dutt Sharma ([@VishnuD2011](https://x.com/VishnuD2011/status/2110056968677425610)) — 2026-10-13T17:15:58+00:00

@mattpocockuk Need help with you are aligning too much and too hard. Its aligning more and more better? Wont ai come up with even better ideas than my own? @mattpocockuk
### Smiley ([@WhySoSanee](https://x.com/WhySoSanee/status/2109984224673509420)) — 2026-10-13T12:26:55+00:00

@mattpocockuk What tests are you referring to in "Your codebase architecture allows bad tests to be written" ?
### Khalid ([@RedwanSun56966](https://x.com/RedwanSun56966/status/2109978565215203341)) — 2026-10-13T12:04:26+00:00

@mattpocockuk @mattpocockuk  "Your codebase architecture allows bad tests to be written",  any solution for that?
### Carlos 🐯 ([@cajotafer](https://x.com/cajotafer/status/2109984369301753910)) — 2026-10-13T12:27:29+00:00

@mattpocockuk "Your codebase architecture allows bad tests to be written" one of the issues I have
### Rushiraj ([@rushirajjj](https://x.com/rushirajjj/status/2110034242109640849)) — 2026-10-13T15:45:40+00:00

@mattpocockuk my agent read this list and apologized for existing. then wrote a longer skill about it
### Everlier ([@Everlier](https://x.com/Everlier/status/2109981369895911915)) — 2026-10-13T12:15:34+00:00

@mattpocockuk You are doing too much
You are doing too little
You are doing just enough, but in a wrong way
### sanjeev ([@thesnjvsharma](https://x.com/thesnjvsharma/status/2109990698409992328)) — 2026-10-13T12:52:38+00:00

@mattpocockuk wow! I've been able to address all of these issue in last few months. looks like im on the right track. 🫡
### Dawg ([@dawgoncoc](https://x.com/dawgoncoc/status/2109974710012576218)) — 2026-10-13T11:49:06+00:00

@mattpocockuk i wanted to say thanks, yesterday i used your retro skill and found out orchestration sucks for me -  meaning orchestration wasnt happening the way i wanted and just finding out this thing, alot of anger was gone from inside me, your skills are just awesome
### The LeeBase - I Can't…Until I Can ([@TheLeeBase](https://x.com/TheLeeBase/status/2110095738130538865)) — 2026-10-13T19:50:02+00:00

@mattpocockuk Thank you - fed it to my chief of staff, determined we could improve and set the improvements in motion
### cooresh ([@TheQuietFloor](https://x.com/TheQuietFloor/status/2109977445847929122)) — 2026-10-13T11:59:59+00:00

@mattpocockuk Any advice on thinking strategically?
### MaximalVibe ([@MaximalVibe](https://x.com/MaximalVibe/status/2110174330810470671)) — 2026-10-14T01:02:20+00:00

@mattpocockuk the real list: every one of these is a knob nobody knows the setting for.
### Kitty Smalls 🐱 ([@smalls_kitty](https://x.com/smalls_kitty/status/2110088178270867510)) — 2026-10-13T19:19:59+00:00

@mattpocockuk What's the max amount of lines, skills should have? Most around around 50-100, with a handful 200-300 lines

## Other returned timeline records

> The CLI did not expose reply relationships. These records do not start with a reply mention and were authored by someone other than the saved-post author. They may include recommendations or promoted posts; they are retained as source context, not verified replies.

### Starlink ([@Starlink](https://x.com/Starlink/status/2068115197718593741)) — 2026-06-19T23:34:21+00:00

Get connected with fast, reliable internet for streaming, video calls, online gaming and more.

Order online in minutes.
### Link Finder ([@LinkFinderOK](https://x.com/LinkFinderOK/status/2099919655498383713)) — 2026-09-15T17:53:55+00:00

Reverse engineer your competitor's backlink profile with Link Finder.

Every new link they got, how much they paid for it, which page it points to, and what that placement goes for today.

Then you decide what to take.
### Robert Wayne ([@robertjwayne](https://x.com/robertjwayne/status/2109987271818744100)) — 2026-10-13T12:39:01+00:00

to move away from human review, do you have an opinion on the “best” setup for automated code review? i.e. have you figured out a setup that allows you to fully automate code review, for both code quality (enforcing coding patterns you care about) and finding potential logic issues?
### Starlink ([@Starlink](https://x.com/Starlink/status/2098108930002194658)) — 2026-09-10T17:58:44+00:00

Starlink offers fast, reliable internet in the most rural and remote locations. Portable and easy to set up, Starlink works wherever you are.

Order online in minutes.
### Alex Spînu ([@alspinu](https://x.com/alspinu/status/2110018659666051541)) — 2026-10-13T14:43:45+00:00

Hey Matt, 

Love your content and all the work you're putting out there for us to learn! 

I have a question, have you ever approached or been approached by the labs to help them make the models/harnesses better? I am sure they have been ingested in their training data scraping but lately with all the emphasis on RL, I could not not imagine how cool it would be to have some of your workflows "baked" into the weights
