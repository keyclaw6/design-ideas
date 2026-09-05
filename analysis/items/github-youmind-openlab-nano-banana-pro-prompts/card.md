# YouMind Nano Banana Pro prompt recommender skill (10k+ prompts)

`github-youmind-openlab-nano-banana-pro-prompts` · github · repo · en · [source](https://github.com/youmind-openlab/nano-banana-pro-prompts-recommend-skill) · [raw](../../../raw/items/github-youmind-openlab-nano-banana-pro-prompts/)
**Author:** YouMind OpenLab (@YouMind-OpenLab) · **Published:** — · **Captured:** 2026-09-02T17:15:19Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [image-prompt-galleries](../../subjects/image-prompt-galleries/brief.md) · **Also:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Roles:** tool · **Platforms:** cli, gemini

**Summary.** MIT agent skill searching 10,000+ curated Nano Banana Pro (Gemini image) prompts via grep-style lookup, returning top three matches with samples; supports direct search or article-to-illustration remix.
**Question it answers.** How do you install and use the Nano Banana Pro prompt recommender skill for Gemini image generation?

**Claims.**
- `github-youmind-openlab-nano-banana-pro-prompts#c1` (capability, stated) Skill searches 10,000+ curated Nano Banana Pro prompts and returns the top three matches with sample images. — evidence: "Agent skill searching 10,000+ curated Nano Banana Pro (Gemini image model) prompts. Returns top 3 matches with sample images." [linked-page]
- `github-youmind-openlab-nano-banana-pro-prompts#c2` (recipe, stated) Token-efficient grep-style search avoids loading full category files. — evidence: "Token-efficient: grep-style search, never loads full category files." [linked-page]
- `github-youmind-openlab-nano-banana-pro-prompts#c3` (benchmark, demonstrated) A 2026-09-04 clone of references/*.json has 14,965 unique prompt ids, while manifest.totalPrompts is 15,508 and the 11 category-file lengths sum to 22,466 because 7,299 ids appear in two or more files. — evidence: "unique ids 14965; manifest totalPrompts 15508; category-file sum 22466; 7299 ids in 2+ files" [note]
- `github-youmind-openlab-nano-banana-pro-prompts#c4` (availability, demonstrated) leftover27 unused youmind.com/nano-banana-pro-prompts 1,244,866 B titles 10,000+ prompts; footer visible text says TOTAL 15,508. Do not collapse title 10,000+, footer 15,508, and any 30,000+ repo copy into one inventory. leftover27 does not download the prompt set. — evidence: "leftover27 youmind-nano 1244866 B. Title 10000+; footer TOTAL 15508." [note]
**Numbers.** GitHub stars: 1843  (note); social media prompt count: 10000  (linked-page); unique prompt ids in references/: 14965  (note); manifest totalPrompts: 15508  (note)
**Recipe.** —
**Techniques.** [prompt-to-html-landing](../../techniques/prompt-to-html-landing.md), [taste-skill-encoding](../../techniques/taste-skill-encoding.md)
**Tools.** [nano-banana-pro-prompts-recommend](../../tools/nano-banana-pro-prompts-recommend.md), [clawhub](../../tools/clawhub.md)
**Links.** repo (https://github.com/youmind-openlab/nano-banana-pro-prompts-recommend-skill), product (https://youmind.com/nano-banana-pro-prompts), https://clawhub.com/skill/nano-banana-pro-prompts-recommend, https://youmind.com/nano-banana-pro-prompts
**Related items.** [github-wuyoscar-gpt-image2-skill](../github-wuyoscar-gpt-image2-skill/card.md), [web-meigen-ai](../web-meigen-ai/card.md)
**Media.** —
**Judge hints.** must_read: False · compare with: —
