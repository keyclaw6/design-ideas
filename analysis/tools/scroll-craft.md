# Scroll Craft

**Slug:** `scroll-craft` · **Kind:** repo · **URL:** https://github.com/nateherkai/scroll-craft · **Canonical item:** [github-nateherkai-scroll-craft](../items/github-nateherkai-scroll-craft/card.md)
**Subjects:** [design-agent-skills](../subjects/design-agent-skills/brief.md), [landing-ui-motion](../subjects/landing-ui-motion/brief.md)
**Referenced by (3):**
- [scroll-craft: Claude Code skill for scroll-driven landing QA](../items/github-nateherkai-scroll-craft/card.md) — tool, technique — landing-ui-motion
- [scroll-craft skill: eight page grammars and fingerprint anti-sameness gate](../items/x-2093900284896657841/card.md) — reference, claim-source — landing-ui-motion
- [Nate Herk Fable 5.1 landing workflow with scroll-craft skill](../items/x-2094978216146452971/card.md) — technique, tool — landing-ui-motion

<!-- NOTES:START -->

Fetched 2026-09-04 README https://github.com/nateherkai/scroll-craft

MIT Claude Code plugin. Install: `/plugin marketplace add nateherkai/scroll-craft` then `/plugin install nateherk-design`; invoke `/nateherk-design:scroll-craft`. **Eight mutually exclusive page grammars** named: filmic one-shot, chaptered editorial, live surface, continuous world, typographic poster, gallery, split stage, rhythmic cutlist. Fingerprint gate: differ on ≥4 of 6 dimensions (grammar, nav, hero, act shape, close, signature move). Headless QA: dead scroll, faded cues, composited contrast, stuck posters + contact sheet. Refuse-list includes feature-card grids, `01/06` counters, gradient text, invented stats, AI-purple. Three public example sites on the README (aiautomationsociety.ai, nateherk.com, PERKFORM).

**2026-09-04 capture — EXAMPLES.md registry + one live page.** `EXAMPLES.md` now has a built row for **all eight grammars** (filmic: perkform/nateherk/agency/saas; live surface: vesper-v2; continuous world: descent + orrery; rhythmic cutlist: airfield; gallery: pigment; chaptered editorial: maison; typographic poster: scrollcraft-showcase; split stage: phase). Live fetch: `https://www.nateherk.com/` HTTP 200, mounts `ScrollCraft` via `/scroll/scrollcraft.js` + `/scroll/scrollcraft.css`; HTML has `data-sc-act|span|stage|tilt|pan|cue|…` (12 attr names). `perkform.com` now 403/parked at nameics. `aiautomationsociety.ai` 403 this pass. Still no local refuse-run against a default Claude landing.

<!-- NOTES:END -->
