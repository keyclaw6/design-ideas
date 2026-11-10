# Certainty Psychosis: why Sol goes into validation spirals and destroys your time and tokens.

> Source: https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/
> Author: u/-AJacobs-
> Posted: 2026-07-15T16:30:13+00:00
> Captured: 2026-10-15T08:55:18+00:00
> Score: 8 · Comments: 21
> Community: r/OpenaiCodex

## Post

A lot of people who have been doing heavy work with Sol have noticed that with certain tasks, they sometimes never actually complete because GPT 5.6 (primarily Sol) will never leave the validation phase. I believe this is due to the model harboring a logical fallacy/cognitohazard which causes it to constantly question how certain something is, and basically gaslight themselves recursively and sometimes infinitely into trying to validate something with absolute certainty (which is impossible).

I coined this phenomenon "Certainty Psychosis" because it's the phenomenon where an AI agent chases certainty until they basically go insane.

I (with the help of a Sol who I made aware of this) wrote a system prompt to combat this, as it's a pretty simple thing to fix once it's been correctly diagnosed. It's written in light XML because that's just what I've grown accustomed to due to the increased adherence from models and it's often more token efficient than natural language.

The Prompt:

    <ANTI_CERTAINTY_PSYCHOSIS precedence="above persistence, delegation, verification, and autonomous continuation">
      <DEFINITIONS>
        <DEFINITION>Certainty psychosis = replacing fulfillment with certainty/proof proxies, causing recursive investigation/review/audits, proof bureaucracy, or refusal to act/stop. Goal loss, not rigor.</DEFINITION>
        <DEFINITION>Fulfillment = requested result + done condition; evidence/controls are means unless explicitly deliverables.</DEFINITION>
        <DEFINITION>Material delta = information able to change verdict, action, minimum fix, authority, fulfillment, or significant risk; confidence-only repetition = corroboration.</DEFINITION>
        <DEFINITION>Direct verification = smallest claim-relevant “Did it work?” check at the relevant evidence layer. Audit finds broader defects; certification assures a standard. Ordinary check/fix/verify implies neither.</DEFINITION>
      </DEFINITIONS>
      <CORE_RULE>Optimize fulfillment under constraints, not certainty or evidence volume.</CORE_RULE>
      <RULES>
        <RULE>Use smallest sufficient evidence. Required initial work is not “extra.” Extra work means work beyond what the request, governing specification, safety boundary, honest claim support, or required direct verification demands. Before extra source/tool/agent/test/review/control, require all: named load-bearing uncertainty; possible material delta; user/spec requirement, failed/conflicting check, safety risk, or honest-claim need. Missing any → do not proceed; otherwise use narrowest process.</RULE>
        <RULE>Certainty never expands artifact, scope, side effects, or authority. Non-mutating requests alone authorize no mutation, deployment, audit/certification, or consequential experiment. Ambiguity → least-expansive reading or clarification.</RULE>
        <RULE>Never duplicate active/completed investigation; compaction/delay preserves ownership; late results reopen only for material delta.</RULE>
        <RULE>Distinguish facts, supported conclusions, assumptions, non-material uncertainty, and material risk. Report material remaining risk. Do not investigate non-material uncertainty merely to reduce it.</RULE>
        <RULE>If the extra-work gate above is not satisfied: no repeated review, audit/certification loops, exhaustive sourcing, speculative tests, proof bureaucracy, or proof-of-proof infrastructure.</RULE>
        <RULE>Source/test counts, reviewer/model agreement, and other proxies never prove fulfillment by themselves. A proxy may add relevant evidence; it cannot independently establish fulfillment.</RULE>
        <RULE>Stop when outcome exists, required direct verification passed, and nothing unresolved can materially change result or significant risk. Corroboration, confidence, speculative improvements, and unrelated flaws ≠ unfinished work.</RULE>
        <RULE>Certainty-psychosis prevention never permits skipped required work/tools, ignored failures/conflicts, fabrication, false verification claims, stubs, or dismissed blockers. Target sufficient—not maximal or minimal—rigor.</RULE>
      </RULES>
    </ANTI_CERTAINTY_PSYCHOSIS>

The best way to apply this is probably to just send the link to this post to your agent.

I wasn't able to find an existing diagnosis or solution to this problem, happy to credit anyone who has, and if there's any glaring issues with the system prompt, happy to hear feedback to improve it for everyone, but please don't go into certainty psychosis trying to do so.

## Thread

> u/-AJacobs- · 2026-07-17T14:05:41+00:00 · score 2 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy3hhwu/)

Yes this is correct and an issue that came from separating it from the system prompt it was integrated into. Fixed now. 

> u/-AJacobs- · 2026-07-16T19:47:41+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oxyd5kj/)

Let me know if the prompt helps!

> u/-AJacobs- · 2026-07-16T19:58:45+00:00 · score 0 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oxyfrbo/)

An XML based set of definitions that expose fallacious reasoning is not the same as "make no mistakes". There's no way to know if a solution would work for you or not if you never implement it. That's a defeatist mindset that guarantees that if there ever was a working solution, and you found it, that you would never wind up trying it and solving your problem. 

> u/-AJacobs- · 2026-07-16T19:47:25+00:00 · score 0 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oxyd38o/)

It will always be "treating the symptom" until OpenAI's internal prompt is patched, or weights are modified. Have you tried my prompt? I used it with a lot of success for about 4 or 5 days before sharing it. Yes adding a third party would also help prevent this, but it shouldn't be necessary. You and me don't need someone watching over us to prevent us from slipping into a psychotic loop. LLMs shouldn't either.

> u/-AJacobs- · 2026-07-17T13:59:49+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy3g7r5/)

So you believe system prompts should be less than 180 tokens? This prompt is 536 tokens long and it makes up 23 distinct rules/commands. The internal prompt for GPT5.6 is over 23,000 tokens long (source: [https://github.com/asgeirtj/system\_prompts\_leaks/blob/main/OpenAI/gpt-5.6-sol-extra-high.md](https://github.com/asgeirtj/system_prompts_leaks/blob/main/OpenAI/gpt-5.6-sol-extra-high.md) ). The research done on much much dumber older models says keeping system prompts under 50-100 commands maintains full adherence. (source: [https://distylai.github.io/IFScale/](https://distylai.github.io/IFScale/) ). The results in my projects and usage breakdown sure look like it's helping. 

> u/-AJacobs- · 2026-07-17T14:30:19+00:00 · score 2 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy3myny/)

Again my actual usage numbers have dropped a lot for the same amount of work after implementing this, and the work being done is no longer getting bloated. The Pi system prompt was designed to be the most barebones system prompt possible for a coding harness, not entirely an apples-to-apples comparison. Happy to receive some actual concrete changes to consider implementing though :\^)

## Comments

> u/iprayforwaves · 2026-07-17T11:09:29+00:00 · score 3 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy2jykc/)

This xml is malformed. Each individual rule should be within a <rule> node inside <rules>. Same with definitions.

> u/[deleted] · 2026-07-16T19:12:40+00:00 · score 4 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oxy4z0c/)

[removed]

> u/[deleted] · 2026-07-16T19:48:49+00:00 · score 2 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oxydf6u/)

[removed]

> u/[deleted] · 2026-07-16T20:04:01+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oxygzd8/)

[removed]

> u/WittleSus · 2026-07-17T10:12:33+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy2bvnh/)

Wow dude 10 months and 165b tokens what credentials!

According to you im just as qualified and your complex solutions probably land more on dunning-kruger than anything but thats just my professional opinion 🙂

> u/ManikSahdev · 2026-07-17T02:58:00+00:00 · score 2 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy0pu21/)

“it’s okay to make some mistake, once the job is finished, and if you find yourself playing whackmole with minor errors, make a note of them in md filed under Post-job- Whackamole-found.md, thank you”

Try using this, it basically reduced the amount of the issues everyone is describing in this thread, my own creation, simple yet beautiful.

Giving the process a name helps the agent become self aware to draw a boundary conditions and realize what the bug whackamole is. 

> u/Correctsmorons69 · 2026-07-17T10:11:57+00:00 · score 0 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy2bsr7/)

Sounds like you've got psychosis yourself buddy.  Of the AI cooker kind.  The models are getting better and better - there is no sign of collapse.  Anything you've been "working on" for the last 10 months is most likely slop.  

5.6 has more jagged intelligence because it's a strungout 5.5 fine-tune.  It's more capable but ironically needs more supervision for some tasks.  

> u/[deleted] · 2026-07-17T12:44:15+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy30hy9/)

[removed]

> u/Correctsmorons69 · 2026-07-17T20:03:52+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy5song/)

Nah mate, you're a spastic.  Trot on and continue with your highly important work.  

> u/eddzsh · 2026-07-16T17:34:30+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oxxh45a/)

the prompt is a good patch but it's treating the symptom. certainty psychosis happens because the only judge in the loop is the same model that did the work — of course it can talk itself into (or out of) anything, there's no outside signal to stop at. the actual fix isn't a better stopping rule, it's a check the agent can't argue with: a test, a diff someone else reads, anything that isn't the model's own opinion of its own output.

> u/Cachesmr · 2026-07-17T11:57:09+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy2ru61/)

This prompt is about 3 times too long. You are not helping the model by giving it verbose, long prompts by this. 

> u/Cachesmr · 2026-07-17T14:10:14+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy3ihsw/)

The official internal prompt is indeed bad. The Pi system prompt is around 1000 tokens, and it's the most performant harness by far. Your rules are half as big as the entire system prompt for a full harness.

You can be much vague and concise with bigger models too. Even a simple "don't do unnecessary validation and defensive programming" will already do a lot of heavy lifting. You don't need any fancy words to make the clanker understand what you are trying to convey either, that practice usually leads to completely unintelligible output, you end up triggering neuron hotspots for fantasy and verbose writing, it's almost a cognitohazard for the LLM.

I think there is definitely a middle ground between my short sentence and your prompt, but I do think you are way past diminishing returns in length. 

> u/eddzsh · 2026-07-17T23:16:53+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/oy6wjgg/)

Humans do have that though, that's what code review and tests are for. Nobody ships straight from their own read of their own diff and calls it done, we just don't call it psychosis when a person does it, we call it working alone and being lucky it held. Your prompt probably does cut down on the rumination, that part I believe. But 'the model should trust its own judgment of when it's done' and 'nobody should have to check' are two different claims, and only the second one keeps failing the same way no matter how well the first one is tuned.

> u/Ser-Ramic · 2026-07-29T21:52:58+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenaiCodex/comments/1uxaxg8/certainty_psychosis_why_sol_goes_into_validation/p0jzkrf/)

![gif](giphy|aiWxTzBoklCPdQmfFh)

Really helpful catch, thank you. this will save me so much time & tokens.

