# Headlong — open microharness for always-on persistent agents

`x-2091990178638496195` · x · repo · en · [source](https://x.com/andykonwinski/status/2091990178638496195) · [raw](../../../raw/items/x-2091990178638496195/)
**Author:** Andy Konwinski (@andykonwinski) · **Published:** — · **Captured:** 2026-09-04T07:01:50Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [agent-harness-loops](../../subjects/agent-harness-loops/brief.md) · **Also:** — · **Roles:** tool, technique · **Platforms:** cli

**Summary.** Headlong is an open-source Bash microharness (<10K LOC) where agents generate continuous inner thoughts, accept Slack/Telegram messages as observations, and self-direct fixes — installable via curl from headlong.ai.
**Question it answers.** How does a persistent agent harness differ from reactive task-completion loops?

**Claims.**
- `x-2091990178638496195#c1` (capability, stated) Headlong agents never sleep; they keep self-guided thought streams between external messages. — evidence: "A Headlong agent is never asleep. It keeps generating thoughts about whatever it decides is interesting, in a self-guided loop inspired by human inner monologue." [post]
- `x-2091990178638496195#c2` (pricing, stated) Background thinking reportedly costs about one to two dollars per hour in the authors' internal deployment. — evidence: "Background thinking costs us $1 to $2 an hour" [post]
- `x-2091990178638496195#c3` (benchmark, demonstrated) cloc 1.98 on Headlong bin/ + thinkers/ reports 9,912 code / 2,600 comment / 1,351 blank (22 files). Do not collapse with README ~11K (capped 11.5K) or wc -l 13,947. — evidence: "cloc 1.98: Bourne Again 9468 + Bourne 376 + MD 65 + JSON 3 = 9912 code. wc -l on the same dirs was 13,947." [note]
- `x-2091990178638496195#c4` (availability, demonstrated) leftover22 unused Laude post is first-party 227,836 B (Aug 24, 2026). Official body still says core less than 10K / 9.9K lines in bin/ + thinkers/ — do not collapse with cloc 9,912 code or wc 13,947 already on #c3. $1–2/hour background (GLM or Grok) is first-party. install.sh 25,935 B clones laude-institute/headlong to ~/.headlong/app; BIN_TOOLS 10 + AUX_TOOLS 13; default dash :8080 in Docker path. — evidence: "leftover22 laude-headlong 227836 B; headlong-install 25935 B. Quote: The core of Headlong is currently less than 10K lines of Bash (9.9K lines in bin/ and thinkers/)." [note]
**Numbers.** background thinking cost: 1-2 USD/hour (post)
**Recipe.** —
**Techniques.** [agent-harness-ops](../../techniques/agent-harness-ops.md)
**Tools.** [headlong](../../tools/headlong.md)
**Links.** repo (https://github.com/laude-institute/headlong), https://www.laude.org/updates/headlong-a-microharness-for-persistent-agents, https://headlong.ai/install.sh
**Related items.** —
**Media.** —
**Thread.** captured_partial · reported 139 · captured 3 · relevant 2 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
