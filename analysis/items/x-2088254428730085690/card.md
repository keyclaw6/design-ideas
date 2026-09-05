# Impeccable 4.1 release — critique, native review, live mode fixes

`x-2088254428730085690` · x · announcement · en · [source](https://x.com/pbakaus/status/2088254428730085690) · [raw](../../../raw/items/x-2088254428730085690/)
**Author:** Paul Bakaus (@@pbakaus) · **Published:** — · **Captured:** 2026-09-04T06:35:39Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Also:** [landing-ui-motion](../../subjects/landing-ui-motion/brief.md) · **Roles:** tool, reference · **Platforms:** cursor, codex, cli

**Summary.** Paul Bakaus announces Impeccable 4.1 with 43 PRs: chat critique reliability, calmer design hooks, native iOS/Android reviews, Windows install fixes, and live mode on ddev/valet hosts.
**Question it answers.** What changed in Impeccable 4.1 for critique, native apps, and live-mode dev hosts?

**Claims.**
- `x-2088254428730085690#c1` (capability, stated) Critique results print in chat before follow-up questions more reliably. — evidence: "critique results more reliably prints in chat before asking you questions" [post]
- `x-2088254428730085690#c2` (capability, stated) Live mode now works on ddev, valet, and other non-localhost dev hosts. — evidence: "works on ddev, valet, and other non-localhost dev hosts" [post]
- `x-2088254428730085690#c3` (recipe, stated) Install or upgrade via npx impeccable install at impeccable.style. — evidence: "npx impeccable install" [post]
- `x-2088254428730085690#c4` (capability, demonstrated) GitHub tag skill-v4.1.0 (2026-08-14) documents native iOS/Android verify, Windows install, live mode on ddev/valet, and full-fidelity comps. — evidence: "https://github.com/pbakaus/impeccable/releases/tag/skill-v4.1.0 body: native verify-and-review pipeline; Windows install; ddev/Valet live mode; full-fidelity comps." [note]
- `x-2088254428730085690#c5` (availability, demonstrated) GitHub skill-v4.2.0 (Skill 4.2.0, published 2026-09-04T20:28:37Z) is a later skill than this 4.1 card. Release notes: no Node/npm runtime (static binary); design hook 10.6 ms vs Node 46.9 ms; CLI scan of 110 files 132 ms vs 282 ms; replay of 830 command invocations and 16,058 function calls. Do not collapse 4.2.0 with skill-v4.1.0 (2026-08-14). — evidence: "GET https://api.github.com/repos/pbakaus/impeccable/releases/tags/skill-v4.2.0 200. analysis/_work/captures/2026-09-05-mustread-retry.json" [note]
- `x-2088254428730085690#c6` (capability, demonstrated) leftover19: impeccable.style 200 / 109,943 B markets 61 checks, 23 commands, and 177 highest-rated worlds. Install copy is npx impeccable install (Node 22.12+). Homepage does not name skill-v4.1.0 vs skill-v4.2.0 — do not collapse those GitHub tags. Testimonial ranking language is source quotes, not a finding. — evidence: "leftover19 impeccable-style 109943 B. 61 checks / 23 commands / 177 worlds visible." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** —
**Tools.** [impeccable](../../tools/impeccable.md)
**Links.** repo (https://github.com/pbakaus/impeccable), product (http://impeccable.style), https://impeccable.style
**Related items.** [github-pbakaus-impeccable](../github-pbakaus-impeccable/card.md), [github-emilkowalski-skills](../github-emilkowalski-skills/card.md), [github-leonxlnx-taste-skill](../github-leonxlnx-taste-skill/card.md), [x-2086715093707063445](../x-2086715093707063445/card.md), [github-google-labs-code-design-md](../github-google-labs-code-design-md/card.md)
**Media.** —
**Thread.** captured_partial · reported 11 · captured 3 · relevant 2 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [github-pbakaus-impeccable](../github-pbakaus-impeccable/card.md)
