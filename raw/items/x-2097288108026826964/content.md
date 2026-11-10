# Everyone keeps saying Astra's new compaction "saves notes" and "searches messages." But I thought: couldn't it do that

> Source: https://x.com/owengretzinger/status/2097288108026826964 — @owengretzinger (owen) — posted Tue Sep 08 11:37:05 +0000 2026 — 23 replies, 15 reposts, 261 likes, 459 bookmarks, 49231 views — captured 2026-09-21T15:05:37Z
> Author bio: head of engineering @boardyai | posts about startups, tech, & toronto 🇨🇦 | husband | ✝︎

## Post

@owengretzinger

Everyone keeps saying Astra's new compaction "saves notes" and "searches messages."

But I thought: couldn't it do that before?

So I traced the Codex implementation. Here's how it ACTUALLY works with specific details like tool names (insightful if you're building agents):

Traditional compaction

1. Token threshold reached
2. Interrupt the main agent flow
3. Append a request to summarize the conversation 
4. Replace the old context with the summary + some recent messages

The summary request is appended to the existing message history to leverage token caching (opposed to a separate 1-shot prompt). 

Afterward, the agent continues with that condensed account of what happened.

It works ok. But the LLM has to decide what it thinks will be important later. Which can cause issues when new information comes up or when you want to revisit something it thought was finished.

And after several compactions, specific decisions and instructions can disappear from the summaries entirely, leading to duplicated work or rediscovering things from scratch.

(I'll give a specific example at the end)

Astra's new flow

1. Codex inserts a developer message when context runs low

After a model response and its tool calls finish, Codex checks the remaining tokens. Once the count reaches the reminder threshold (configurable), it appends a message telling Astra to preserve its progress, decisions, next steps, and references to earlier messages before resetting.

2. The agent writes notes through tool calls

It uses tools like notes.write_file and notes.append_to_file. It can organize the notes into separate files however it decides. 

(It can also edit these notes mid-session if it wants to)

3. The agent calls new_context when it's ready

Codex uses this tool to explicitly decide when it's ready to replace the active conversation with a fresh context window (no summarization).

There's also a forced reset eventually if the agent keeps going and hits a separate threshold.

4. The next window gets instructions and pointers to what was saved

After the reset, alongside base instructions & context, it gets references to previous context windows and notes.

Here's an example of the notes hint inserted into context, from a Codex integration test:
```
Recent notes (up to 5, most-recent first):
- /root/notes/latest.md (2 lines, 14 UTF-8 bytes)
```
https://github.com/openai/codex/blob/rust-v0.153.0/codex-rs/app-server/tests/suite/v2/history_notes_extension.rs#L32-L33

5. The agent fetches what it needs to continue

It can call notes​.read_file to read the files, then history​.search_contents and history​.read_item to find and read earlier messages or tool results.

And then the great thing is that these tools stay available throughout the session. So when new information comes up or you want to revisit something, the agent knows to find the relevant notes and original message history.

Example

Say I'm working on a frontend. I go back and forth with Codex workshopping a component, move on to other things (compaction happens here), then come back to that component later.

With ordinary compaction, it might save only high-level details about the component because it thinks we're done with that part. Then I bring it up again and get really frustrated because it's forgotten things we already worked through.

Yes, if I directly asked, it could fetch older messages with the right tools. But by default it would probably keep working from an incomplete summary without realizing what was missing.

With the new method, it's explicitly instructed to recover context from notes and earlier messages. When I return to the component, it can look up our exact discussion, even if the notes only kept high-level details.

Enabling it

Paste this into Codex:
Enable experimental context management in my config.toml https://learn.chatgpt.com/docs/models#experimental-context-management

## Media

![](media/card.jpg)

Original: https://pbs.twimg.com/card_img/2099825187726258177/a3PxGNa7?format=jpg&name=800x419

## Thread

**@owengretzinger** (2026-09-09T10:53:16.000Z) — https://x.com/owengretzinger/status/2097639469906047267

i think over a long session it would probably actually save tokens but yeah i agree would be cool to see the stats

**@owengretzinger** (2026-09-08T18:19:59.000Z) — https://x.com/owengretzinger/status/2097389501144281123

yeah!!

## Comments

**@sacino** (2026-09-09T02:57:32.000Z) — https://x.com/sacino/status/2097519745700696402

great post

would love to see some stats from openai around the implications of this change from both an accuracy and token efficiency standpoint

e.g. more accurate in 5% of cases but costs 30% more (made-up numbers)

as it’s likely a trade-off rather than demonstrably superior

**@RexxDzn** (2026-09-08T22:41:05.000Z) — https://x.com/RexxDzn/status/2097455209505042909

now THIS is why I downloaded Twitter

**@_ngenome** (2026-09-08T18:03:24.000Z) — https://x.com/_ngenome/status/2097385329921605749

Way better than automated compaction... i hope this solves the codex amnesia problem

**@OnFinality** (2026-09-08T21:32:17.000Z) — https://x.com/OnFinality/status/2097437894436941955

The off-by-default part is key. Most people assume it's automatic, but you have to explicitly enable it with that prompt. Curious if the tool calls in earlier windows are fully searchable or just metadata.

**@HeySilasReed** (2026-09-09T16:23:00.000Z) — https://x.com/HeySilasReed/status/2097722449127505941

wondering if adding the concept of a ‘loop’

a background process would monitor for ‘open loops’ and keep a record of loops. this record would be durable and adjacent to context. whenever the thread compacts, the agent can check the loops to see what’s left unresolved.

**@bestaiprice** (2026-09-13T14:24:08.000Z) — https://x.com/bestaiprice/status/2099142086465323202

A fresh session is sometimes cheaper

**@habibislop** (2026-09-08T14:04:34.000Z) — https://x.com/habibislop/status/2097325222651171247

so uh how much of my usage is this burning? I know the old compaction happened on the backend. but this one recruits our own agents

## Links

- https://github.com/openai/codex/blob/rust-v0.153.0/codex-rs/app-server/tests/suite/v2/history_notes_extension.rs#L32-L33
- https://learn.chatgpt.com/docs/models#experimental-context-management
