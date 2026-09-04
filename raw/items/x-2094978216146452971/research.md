## What they are actually doing

Nate Herk (AI Automation Society, YouTube) is selling a **workflow + reusable Claude skill**, not a one-off demo. The bookmark video (149s) is the companion to his X article **Fable 5.1 FINALLY Kills AI Website Slop**. Claim: Fable 5.1 matched Fable 5 visual quality in his tests and was cheaper.

**Method (from the article, via fxtwitter quote payload)**

- Brand guidelines + pain / person / promise, not “make it premium.”
- Named visual references (Fora layered landscape for AAS; 21st.dev components for his personal site).
- Layering + subtle scroll feedback; reuse real design-library components.
- Screenshot loop to verify desktop and mobile.
- Same prompt/assets/ScrollCraft skill on Fable 5 vs 5.1: visuals similar; costs e.g. $18.24 vs $20.22, $12.83 vs $21.64, $11.18 vs $17.37. He reports ~45% of weekly Fable 5.1 allowance after 5–6h vs burning Fable 5 in 1–2h.

Sites named in the article: AI Automation Society (layered hero, stacked cards, dynamic sections), nateherk.com (count-up stats, floating 3D cards), Glido (product-demo dictation bar). Two of five sites were single-prompt.

**scroll-craft** — `https://github.com/nateherkai/scroll-craft` (1,547 stars at capture; MIT; Claude Code plugin)

- Skill for scroll-as-timeline sites with a design floor and a uniqueness gate (eight mutually exclusive page grammars; required “signature move”; fingerprint registry).
- Engine (`scrollcraft.js` + CSS) is not edited per project; theme via tokens/fonts.
- Example builds in README: [aiautomationsociety.ai](https://aiautomationsociety.ai), [nateherk.com](https://www.nateherk.com), PERKFORM (no live URL in README excerpt).
- Needs Node 18+, full ffmpeg (scrub encoding), playwright-core + Chrome for screenshot verify. Optional `KIE_AI_API_KEY` for generated assets.
- README: only ever run on Windows so far; generated video is not free.

## Open questions

- Whether the 149s video is the full five-site walkthrough or a cut (not transcribed here).
- Live URL for PERKFORM.
- Remaining ~26 parent replies (possible extra skill mirrors or demo URLs) behind login.
