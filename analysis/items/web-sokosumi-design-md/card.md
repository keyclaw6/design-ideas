# Sokosumi free DESIGN.md generator from any website URL

`web-sokosumi-design-md` · website · product · en · [source](https://sokosumi.com/tools/design-md) · [raw](../../../raw/items/web-sokosumi-design-md/)
**Author:** Sokosumi (@sokosumi) · **Published:** — · **Captured:** 2026-09-02T17:42:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Also:** — · **Roles:** tool · **Platforms:** browser, claude-code, cursor

**Summary.** Sokosumi free tool at sokosumi.com/tools/design-md opens a remote browser on any URL, reads computed styles, and writes a Google DESIGN.md spec for colors, type, spacing, and components. Edit, copy, or download for Claude Code, Cursor, or Codex.
**Question it answers.** What is the free URL-to-DESIGN.md extractor in the Sokosumi toolchain?

**Claims.**
- `web-sokosumi-design-md#c1` (capability, stated) Tool reads computed styles via remote browser and outputs Google DESIGN.md format. — evidence: "Remote browser opens the page, reads computed styles, writes structured DESIGN.md." [linked-page]
- `web-sokosumi-design-md#c2` (recipe, stated) Shortcuts include Stripe, Linear, Vercel, and Notion example URLs. — evidence: "Shortcuts: Stripe, Linear, Vercel, Notion." [linked-page]
- `web-sokosumi-design-md#c3` (result, demonstrated) Unauthed POST /api/design-md queued example.com and returned a 12,675-byte LLM DESIGN.md in 43.6 s (extractionId 1940, source=llm). Hyperbrowser POST /api/generate still 401 API key required. — evidence: "job d00a14fe-213e-4152-a92f-c05e3cb1ec49 done; surface #eeeeee primary #334488. Hyperbrowser {"error":"API key required"}. See sokosumi-design-md NOTES." [note]
- `web-sokosumi-design-md#c4` (result, demonstrated) Sokosumi gallery lists 1,211 llm extracts. Published Linear/Stripe/Notion YAML have 47 color keys each. Linear surface #08090a matches Refero Void, but Linear primary #e5e5e6 does not match Refero Acid Lime #e4f222; Notion #0075de and Stripe #533afd do match Refero. — evidence: "GET /api/design-md/gallery total 1211. Analysis pages + cached POST linear.app 1872 / stripe.com 1755. Refero NOTES for the JSON side." [note]
**Numbers.** —
**Recipe.** —
**Techniques.** [design-md-contract](../../techniques/design-md-contract.md)
**Tools.** [sokosumi-design-md](../../tools/sokosumi-design-md.md)
**Links.** repo (https://github.com/google-labs-code/design.md), product (https://sokosumi.com/tools/design-md), https://x.com/tranmautritam/status/2095078647652917329
**Related items.** [github-google-labs-code-design-md](../github-google-labs-code-design-md/card.md), [web-design-md-hyperbrowser](../web-design-md-hyperbrowser/card.md), [web-getdesign-md](../web-getdesign-md/card.md), [web-styles-refero-design](../web-styles-refero-design/card.md), [web-neuform-ai](../web-neuform-ai/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: —
