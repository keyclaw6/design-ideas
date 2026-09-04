# Google Labs DESIGN.md spec with lint and diff CLI

`github-google-labs-code-design-md` · github · repo · en · [source](https://github.com/google-labs-code/design.md) · [raw](../../../raw/items/github-google-labs-code-design-md/)
**Author:** Google Labs Code (@google-labs-code) · **Published:** — · **Captured:** 2026-09-02T17:15:42Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [design-agent-skills](../../subjects/design-agent-skills/brief.md) · **Also:** — · **Roles:** tool, reference · **Platforms:** cli, cursor

**Summary.** Google Labs repo defining DESIGN.md: YAML token front matter plus markdown rationale so coding agents persist a lintable design system, with npx lint for WCAG contrast and diff for CI governance.
**Question it answers.** What is the canonical DESIGN.md file format and how do you lint or diff design tokens for coding agents?

**Claims.**
- `github-google-labs-code-design-md#c1` (capability, stated) DESIGN.md combines YAML front matter tokens with markdown prose so agents get exact values and application rationale. — evidence: "Tokens give agents exact values; prose tells them why and how to apply them." [linked-page]
- `github-google-labs-code-design-md#c2` (capability, stated) CLI supports lint for WCAG contrast and token validation plus diff to compare design system versions. — evidence: "CLI: `npx @google/design.md lint DESIGN.md` — WCAG contrast, token validation" [linked-page]
**Numbers.** —
**Recipe.** —
**Techniques.** [design-md-contract](../../techniques/design-md-contract.md), [anti-slop-ui-skills](../../techniques/anti-slop-ui-skills.md)
**Tools.** [google-design-md-cli](../../tools/google-design-md-cli.md)
**Links.** repo (https://github.com/google-labs-code/design.md), product (https://stitch.withgoogle.com/docs/design-md/specification)
**Related items.** [web-getdesign-md](../web-getdesign-md/card.md), [web-sokosumi-design-md](../web-sokosumi-design-md/card.md), [github-pbakaus-impeccable](../github-pbakaus-impeccable/card.md)
**Media.** —
**Judge hints.** must_read: ['research.md'] · compare with: [web-getdesign-md](../web-getdesign-md/card.md), [web-designmd-me](../web-designmd-me/card.md)
