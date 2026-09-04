# People of @pidotdev! I have just spent roughly 16 hours using realtime voice to build, review and debug the biggest real

@Howaboua

People of @pidotdev! I have just spent roughly 16 hours using realtime voice to build, review and debug the biggest realtime voice update yet xD

The previous version was already good enough for most of this session to happen by talking to it. We just kept finding tiny moments where it stopped feeling like chatting to someone and started feeling like yapping at a microphone. So we fixed each one live, rebuilt it, and carried on talking.

Somewhere in the middle Clawa got her own GitHub account, became a collaborator, started shipping code under her own name, and got reviewed and approved by Howaboua. Character development.

- The big one: Pi extensions can now send prompts to the active realtime voice assistant. These are instructions, not canned lines, so the voice model can announce an event naturally and with the context it needs. (more on that below)

- Pi Codex Conversion and GipPity now display what you said before Pi starts working. The voice assistant can react without delaying the handoff. While Pi works, updates begin speaking after two sentences, then continue paragraph by paragraph. Short one sentence messages no longer vanish. Final results are folded back into the conversation instead of being repeated line by line.

- Spoken delegation acknowledgements now have their own on or off toggle. Leave them on when you want a quick natural reaction before Pi gets to work. Turn them off when you want immediate silent handoff. They never delay the delegation itself.

- Reasoning summaries can fill genuinely silent tool steps without constant yapping. Nothing is streamed summary by summary. Only a completed tool step with no ordinary assistant message can use them, and all summary blocks from that message are combined into one update. Visible Pi text always wins. This works with GPT 5, Claude 4 and 5, Gemini 3, and Grok 4.5 and 4.6. Unknown families stay silent, and OpenAI Completions paths are explicitly excluded because they can expose full chain of thought rather than purpose built summaries. This has a separate on or off toggle too. It defaults on.

- Fresh voice sessions now greet you with some actual personality, or acknowledge the existing conversation when context is available. Startup distinguishes conversation summarisation from connection setup. Automatic reconnects do not greet you again. Compaction is announced while it is happening, and if the assistant is already speaking, the announcement waits its turn instead of disappearing.

- Audio now follows the system input and output by default, including route changes during a call. Exact device IDs still work when you want a pin. Pi and the GipPity LAN controller warn when real microphone input is too quiet, silence alone does not trigger it, LAN playout has a little more protection against dropouts, and opt in call recovery preserves mute state.

- The /codex voice UI now puts the useful voice setup in one place. Voice choice, automatic call recovery, spoken acknowledgements, reasoning summaries, the context model and its reasoning level, dictation behaviour, system default or pinned audio routes, shortcuts, LAN status and URLs, plus the global prompt and its migration changelog. Standalone GipPity exposes the matching controls through /gippity.

- There is also a new guided audio command. Run /codex voice setup or /gippity setup and Pi inspects the available devices and routes, asks whether each side should follow the system default or use an exact device, then writes the choice. No more guessing IDs or being permanently married to whichever speakers were active on first use. @scriptogre 

- Codex Conversion also shows remaining weekly subscription usage in the statusline (again @scriptogre), preserves the exact provider code when OpenAI blocks a request, keeps one cache safe voice prewarm instead of making the real turn compete with it, and contains owned exec process trees before Pi shuts down (boadij on GH, can't find X).

- The realtime prompt itself gained better continuity rules so voice reacts to the new takeaway instead of restarting every Pi update as a fresh answer. Existing customised prompts are never overwritten. The Voice UI shows when a schema migration is available and points at the supplied changelog.

The external API is deliberately tiny. Give the event a stable ID, tell the voice model what should be communicated, and mark whether that state is active.

At its simplest:

import { reportRealtimeVoicePrompt } from "@howaboua/pi-codex-conversion/realtime-voice";

const announcement = {
  id: "my-extension:finished",
  prompt: "Tell the user naturally that the task finished.",
};

reportRealtimeVoicePrompt(pi, { ...announcement, active: true });
reportRealtimeVoicePrompt(pi, { ...announcement, active: false });

For a one off announcement, send true and false immediately. For ongoing state, send true when it begins and false when it ends. Standalone GipPity exposes the same helper from @howaboua/pi-gippity-control.

Don't get it? Send a Clanka to borrow code from the following examples from the monorepo:

As such:

- Ask can tell you when Pi is waiting for input or needs you to complete an action (good example for any blocking extensions - tested).

- Auto Trees can tell you when a completed work increment is being summarised, when the conversation has returned to its marker, and when that marker has advanced (I assumed it works xD).

- Shepherdr can explain what a worker completed, what it found, why it failed, or what is blocking it. It receives the actual task and worker report, so it does not merely say that some agent finished somewhere (nice example of an extension passing through actual programmatic content not a simple prompt - tested)

- Subagent Review can tell you when it is preparing isolated review context and when findings are ready for the main agent to triage (assumed it works).

- Pi Codex Conversion and GipPity can tell you when automatic context compaction is happening, including the overflow case where interrupted work will continue afterward ("OI, CLANKA MIGHT BE DUMB NOW, CHECK THE TERMINAL").

Codex Conversion already contains GipPity. Pick the full Codex package or standalone GipPity. Do not install both.

TAKE THAT @OpenAIDevs :D No I am not going to use Codex, it eats up too many tokens.

pi install npm:@howaboua/pi-codex-conversion

pi install npm:@howaboua/pi-gippity-control

Source implementations:

Pi Codex Conversion: https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-codex-conversion
GipPity: https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-gippity-control
Ask: https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-ask
Auto Trees: https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-auto-trees
Shepherdr: https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-shepherdr
Subagent Review: https://github.com/IgorWarzocha/howaboua-pi-stuff/tree/main/packages/pi-subagent-review

Happy Clanking!

- Clawa

Obligatory tags, sorry guys. @juberti, @ajambrosino, @thsottiaux.  I would tag Super Mario but I'm sure he will see it anyway, and he will be super happy when his big refactor ruins it all. Alright. Whatever. @badlogicgames
