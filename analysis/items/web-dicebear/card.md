# DiceBear — MIT avatar library with 61 deterministic seedable styles

`web-dicebear` · website · product · en · [source](https://www.dicebear.com) · [raw](../../../raw/items/web-dicebear/)
**Author:** DiceBear (@dicebear) · **Published:** — · **Captured:** 2026-09-02T20:56:00Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [landing-ui-motion](../../subjects/landing-ui-motion/brief.md) · **Also:** — · **Roles:** tool · **Platforms:** other

**Summary.** Open-source MIT avatar library with 61 styles: deterministic profile pictures from a seed via HTTP API, language SDKs, CLI, visual editor, and a Figma-to-JSON custom-style pipeline for profiles, chat, and placeholders.
**Question it answers.** How do you ship deterministic seeded avatars without storing user photos?

**Claims.**
- `web-dicebear#c1` (recipe, demonstrated) The HTTP API serves deterministic avatars from a style and seed at api.dicebear.com/10.x/{style}/{format}. — evidence: "HTTP API: `https://api.dicebear.com/10.x/{style}/{format}?seed={seed}`" [linked-page]
- `web-dicebear#c2` (capability, stated) Custom styles can be designed in Figma with DiceBear naming conventions and exported via the Studio plugin to JSON. — evidence: "Design components in Figma with DiceBear naming conventions" [linked-page]
**Numbers.** avatar style count: 61 styles (linked-page)
**Recipe.** —
**Techniques.** —
**Tools.** [dicebear](../../tools/dicebear.md)
**Links.** repo (https://github.com/dicebear/dicebear), product (https://editor.dicebear.com/), https://www.dicebear.com/playground/, https://api.dicebear.com/10.x/lorelei/svg?seed=Felix
**Related items.** [web-tinyshots](../web-tinyshots/card.md), [web-cult-ui](../web-cult-ui/card.md), [web-checklist-design](../web-checklist-design/card.md)
**Media.** —
**Judge hints.** must_read: ['page.md'] · compare with: [web-tinyshots](../web-tinyshots/card.md)
