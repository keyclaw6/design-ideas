# Opus 5.5 + Blender won in motion design. Three.js didn't match the quality needed

> Source: https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/
> Author: u/mementomori2344323
> Posted: 2026-10-13T12:45:12+00:00
> Captured: 2026-10-15T08:55:18+00:00
> Score: 135 · Comments: 63
> Community: r/SaaS

## Post

We don't pay for motion designers anymore

The cinematic hook is done with seedance 2.5 in the spirit of those quirky AI influencers trend

Then the motion design itself I tried to use Three.js as some people recommended but it couldn't model the asana and clickup screens in a high resolution (no idea why)

So I asked Opus to move back to Blender and make it in 1080p

All those small diagonal 3d tilts of the screen adds to the dynamic feeling compared to showing flat screens.

The small details make a difference.

Another learning for us is to only show one sentence to explain each phase

The whole thing took Opus around 3 hours of work with minor feedback.

total generations costed around $20

Same video before Opus 5.5 would be quoted for at least $5,000 by a motion designer

I wonder what they are going to do next because there is very little need at least for these kind of launch videos for humans now.   
  
which I believe bite right in the mid level motion designer market tier

## Media

![](media/01-reddit-media.png)

> Original media URL: https://external-preview.redd.it/dzhpY3IzdG9jOHZoMZuhHNXEbdjuwGSC6n0dUF1-BvqWRgy_B3w6CiZ01TQf.png?format=pjpg&auto=webp&s=5ca72e7ec1667546c0b0683f875dbc08b6b5f6d0

[media/02-reddit-media.mp4](media/02-reddit-media.mp4)

> Original media URL: https://v.redd.it/4lhs3fsoc8vh1

## Thread

> u/mementomori2344323 · 2026-10-13T18:11:19+00:00 · score 3 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgj2quu/)

You nailed it. So for now we ask it for a complete local build of every frame and every part. exactly so it won't need to redo the whole thing for every edit and instead can just fix stuff that is wrong and ffmpeg that part again and stitch it back to the video. 

We are working on a bigger integration where our built in editor will have the toolkit an agent needs to basically produce any type of launch video like that or any content basically with versioning to give a visual interface for a human or a commentable timeline for another agent to ask for fixes.

> u/mementomori2344323 · 2026-10-13T13:59:32+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghebn8/)

There is a programattic part of making the video that we are prototyping to soon render on a visual editor inside maxfusion.

Majority of the heavy lifting can be done on it's own as well using OPUS 5.5 + Blender locally.

> u/mementomori2344323 · 2026-10-13T13:58:22+00:00 · score 8 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghe2f6/)

Opus searched the web, found out the interfaces of Asana and the likes, rebuilt it all in blender on it's own. the only process we followed is talk about the message, 

Opus then gave a suggested storyboard with shot ideas. I used Wispr flow to dictate all my vision with long messages. 

Then let it cook for 2 hours on its own and went to sleep.

When I woke up I saw the issue with the resolution and it suggested to build in Blender (what I wrote above)

It also creates all the sound effects locally on the device and times them to the frames.

We just waited for it to fix all the comments and that's it.

The hook idea was made by my co founder who said let's do one of those AI influencers trolling someone in the office as if annoying everyone and not working

Until someone notices the tickets are moving on their own.

and then the closure where they all fool around together in the office because their work was automated until the pissed off boss comes in.

Opus did the editing everything.

Important to say on EFFORT MAX. so it does eat a lot of tokens but we have a max plan on Claude anyway.

> u/mementomori2344323 · 2026-10-13T17:17:31+00:00 · score 3 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgipe1d/)

ask it to install blender locally and read the API docs. done.

> u/mementomori2344323 · 2026-10-13T18:12:27+00:00 · score -1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgj3132/)

It's all just a very long chat with Opus 5.5. It took some time to make this process more efficient. some skills were saved over time for how to move certain parts and not to learn each time from the start how to make good motion. now it's just long chatting and letting it cook for 2 hours on its own. then discussing feedback rounds.

> u/mementomori2344323 · 2026-10-13T14:00:49+00:00 · score 2 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghelqm/)

We found that for the concepts of 3d objects and screen tilting Claude could with quite ease navigate the Blender API and get results faster. Could be that you can do it all in raw. I did saw it's perfect for 2D and you don't need anything but Vanilla JS.

But the Blender increased the fine quality of some renders for us so we kept it

> u/mementomori2344323 · 2026-10-13T14:52:57+00:00 · score 2 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghqfce/)

Hey Blender is opensource. I just downloaded it and installed locally. I wouldn't see a need to host it on VM. unless you have an extremely low CPU machine for some reason?

> u/mementomori2344323 · 2026-10-13T18:13:02+00:00 · score 2 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgj36gm/)

2 - 30 seconds generations hit good enough for the opening and ending of the video. that's it.

> u/mementomori2344323 · 2026-10-13T15:46:52+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgi373q/)

Thanks we measured performance and found out the faster worked better but I agree it does move fast

> u/mementomori2344323 · 2026-10-13T17:17:00+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgip9m3/)

Appreciate the feedback

> u/mementomori2344323 · 2026-10-13T12:55:48+00:00 · score -1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgh0zqh/)

you are viewing the result now. what do you mean by "final render"?

> u/mementomori2344323 · 2026-10-13T15:07:16+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghtsf2/)

Generated by Opus 5.5 using Suno

> u/mementomori2344323 · 2026-10-13T16:28:01+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgid7uc/)

and every individual SFX you hear that is not music was synthesised locally by Claude 

> u/mementomori2344323 · 2026-10-13T15:06:59+00:00 · score 3 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghtpw2/)

I know that it can use AE but Blender is free and I didn't see any need to use AE for this. If you can share some results you found better due to using after effects will be great to learn

> u/mementomori2344323 · 2026-10-13T18:14:30+00:00 · score 2 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgj3jqo/)

For now with Opus 5.5 and soon stronger models I believe any desktop software that was designed for human use is more of a handicap then an enabler. We need frameworks that are built for agents from the ground up

> u/mementomori2344323 · 2026-10-13T15:45:58+00:00 · score 3 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgi2z44/)

the cinematic parts were made with maxfusion MCP x seedance 2.5

> u/mementomori2344323 · 2026-10-13T16:02:32+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgi6zye/)

Why not? didn't get it

> u/mementomori2344323 · 2026-10-13T17:17:54+00:00 · score -1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgiphha/)

yes it is

> u/mementomori2344323 · 2026-10-13T13:54:36+00:00 · score 3 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghd8wg/)

I don't hate anyone. I just show case that we delegate all of this to Opus 5.5

## Comments

> u/Local_Interaction_99 · 2026-10-13T21:53:42+00:00 · score 7 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgkk4xj/)

Man I love how sloppy ad posters nowadays look and now see who is behind it. Really nice job /s 

I hope this phase of sloppy work will be over soon

> u/DayCompetitive1106 · 2026-10-14T08:02:26+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgncmov/)

yes, AI will get dumber over time bro....

> u/Local_Interaction_99 · 2026-10-14T09:14:36+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgnl4tx/)

But sadly what I see is just that the public models get more dumber over time and see specialised models beat those records or be fantastically successful in doing things. 

Currently they WILL get dumber because if the training material is getting worse (they feed ai slop into ai) then the resulting model will be dumber. 

> u/keepitfriend · 2026-10-14T07:10:09+00:00 · score 5 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgn6ev4/)

Who in their right mind would use three.js for anything outside of web design?

Obviously Blender is better - but the point of three.js is that it runs easily in a browser

Like it's a library for animating on a website. It has benefits and it has drawbacks.

> u/Critical_Hunter_6924 · 2026-10-14T10:38:15+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgnvv7q/)

three.js is great to agentically build models and animations

No MCP bloat, no running processes, quick iteration. Lots of scenarios where it's a better pick than blender or as a pre blender step in your pipeline. 

> u/john006868 · 2026-10-13T17:56:21+00:00 · score 5 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgiz15u/)

How much of this ends up reusable, like a scene file you can re-render, vs rebuilt from scratch every time the product ui changes? Day one is cheap. The fourth video is where the upkeep shows.

> u/Dedelelelo · 2026-10-13T15:57:30+00:00 · score 16 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgi5s34/)

this is so ass i can’t stand the jerky cadence ai slop has 

> u/DrJ_PhD · 2026-10-13T20:12:09+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgjwktu/)

Which parts are you talking about, like the transitions or the motion elements? Im curious to see where AI falls apart when held to higher motion design standards. 

> u/Dedelelelo · 2026-10-13T21:38:54+00:00 · score 3 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgkgyn4/)

everything is slightly too punchy for lack of better explanation 

> u/corporat · 2026-10-13T21:49:44+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgkjak1/)

it's 2x too fast. also they gave too much prominence to logos that were not their own logo

> u/CaptainDivano · 2026-10-13T13:18:47+00:00 · score 10 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgh5ncd/)

How is [maxfusion.ai](http://maxfusion.ai) involved in the production of this? Or you just used Opus 5.5 and Blender + Seedance 2.5 to produce an AD for [maxfusion.ai](http://maxfusion.ai) ?

> u/xjuslipjaditbshr · 2026-10-13T13:24:06+00:00 · score 6 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgh6r9p/)

This is very cool. So what was the working process? Did you collect the assets and then prompt opus to use them in blender or what steps did you take?

> u/kirrttiraj · 2026-10-13T17:15:48+00:00 · score 3 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgioz54/)

damn cool vid. How do you connect Opus with Blender?

> u/SatisfactionGlass448 · 2026-10-13T19:05:37+00:00 · score 3 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgjg5lt/)

That's cool dude

> u/Square-Tone-6787 · 2026-10-13T17:57:00+00:00 · score 2 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgiz6za/)

This is super impressive and I'd love to see the full workflow

> u/swallace36 · 2026-10-13T13:44:40+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghb4ir/)

ai slop

> u/ValenciaTangerine · 2026-10-13T13:40:17+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgha6qc/)

why not just raw html js css? why blender for the mock ups? 

> u/OkayYeti · 2026-10-13T14:40:22+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghnhk9/)

Blender in your local? Or was there some way to have Opus recreate the Blender environment on a VM?

> u/Ok_Phase_3846 · 2026-10-13T17:59:24+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgizshn/)

How much credits did seedance use? 

> u/AllenHere112 · 2026-10-13T23:47:16+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgl6ma1/)

those low res screens are usually a render target thing, not a geometry one. webgl draws at 1x unless you scale the canvas by devicePixelRatio, so the ui looks fine live and turns to mush the moment it gets exported at 1080p. cheap fix, wrong culprit.

> u/Overdose999_ · 2026-10-14T11:02:26+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgnze8l/)

But your own ad looks ass lmao

> u/DawaForensics · 2026-10-14T16:39:06+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgpy7fc/)

Diabolical 

> u/WesternTip4263 · 2026-10-13T14:25:54+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghk6lk/)

Nice!

> u/Novel-Initiative-900 · 2026-10-13T15:28:50+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghyvte/)

I think it looks good however the transitions from one text element to another are very fast. Like, sometimes you want to 'ramp' to a lingering moment where you can see clearly what element it is you're focusing on in the app and then ramp out to the next thing. I've never made a video like this so I don't know but it does feel just a tad quick. But the quality of everything looks great

> u/Jeffelon-Muskergates · 2026-10-14T08:13:07+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgndw5k/)

lol bad measurements

> u/asapbones0114 · 2026-10-13T16:46:29+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgihri5/)

Looks very fake but the improvements have been insane!! 

> u/surfer808 · 2026-10-13T17:11:39+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pginyiq/)

It looks great but I think it’s too fast, I have no idea what the program you’re pitching even does, I saw Asana and that was it. And my two cents, the closing lacks closing. I think your companies pitch would be great here, “(your company), getting things done so you can fuck around…”

> u/Ok_Condition_5509 · 2026-10-13T12:54:46+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgh0s9e/)

Three.js c'est un moteur de rendu, il ne modélise rien. Si tes écrans Asana/ClickUp sortent mal c'est ton mesh ou ta texture, pas la lib. Et le rendu final, il est où? Parce que "on ne paie plus de motion designers" ça demande une preuve.

> u/500Rads · 2026-10-13T13:53:10+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghcxw0/)

So basically AI is just better workflow and we are still in the software era 

> u/killboy123 · 2026-10-13T15:02:55+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghsrly/)

That's a cool video. Where'd you get the music?

> u/rdpl_ · 2026-10-13T16:14:48+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgi9zci/)

What was Opus' role here, just doing the prompt for Suno?

> u/DeliciousGorilla · 2026-10-13T14:56:01+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghr595/)

Sure it can be done in Blender, but it makes way more sense to do this in After Effects (Claude/Codex can drive that too).

> u/DeliciousGorilla · 2026-10-13T18:07:32+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgj1t8r/)

Well the workflow is mostly 2.5D motion graphics... UI, text, transitions, camera movement. So that's pretty AE specific, meaning It might be easier for agents to tweak timing, swap content, and keep things consistent across multiple videos.

Btw there's also [EffectCraft](https://github.com/storytold/effectcraft), one of those new Adobe knock offs.

Would be interesting to see an agent build and revise the same 10-second animation in both software. My guess is AE-style tools would be faster to iterate on, especially at scale. Faster = cheaper.

> u/DeliciousGorilla · 2026-10-13T18:23:06+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgj5ofj/)

That's what EffectCraft did:  
[https://github.com/storytold/effectcraft/blob/main/docs/agents.md](https://github.com/storytold/effectcraft/blob/main/docs/agents.md)

>Everything in EffectCraft is an engine command with a stable id and JSON params. Menus, shortcuts, panel gestures, the CLI, the control channel and MCP all go through the same commands, so anything a user can do, an agent can do too. 

> u/Novel-Initiative-900 · 2026-10-13T15:25:59+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghy7c3/)

Does it generate video as well?? 

> u/underatedd6 · 2026-10-13T15:53:17+00:00 · score 4 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgi4r5n/)

so not $20..

> u/underatedd6 · 2026-10-13T16:08:50+00:00 · score 2 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgi8ivd/)

isnt seedance 2.5 paid model?

> u/IveGotMySources · 2026-10-13T13:47:56+00:00 · score 0 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pghbtt5/)

Sounds like you hate motion designers for some reason. This looks like 2 hours of work in after effects, blender was not needed. The rest of the AI footage wouldn't be billed by a motion designer. Still the actual motion looks just OK.

> u/rdpl_ · 2026-10-13T16:17:01+00:00 · score 1 · [comment](https://www.reddit.com/r/SaaS/comments/1x4vndw/opus_55_blender_won_in_motion_design_threejs/pgiaipu/)

go  cry somewhere else

