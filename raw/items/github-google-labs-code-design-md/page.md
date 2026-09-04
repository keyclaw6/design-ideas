# DESIGN.md

**URL:** https://github.com/google-labs-code/design.md

## What it is

Google Labs format spec: a DESIGN.md file combines YAML front matter (machine-readable tokens) with markdown prose (design rationale) so coding agents persistently understand a design system.

## Notable files / links

- Specification at stitch.withgoogle.com
- CLI: `npx @google/design.md lint DESIGN.md` — WCAG contrast, token validation
- `npx @google/design.md diff` — compare design system versions

## Key README excerpts (summarized)

> Tokens give agents exact values; prose tells them why and how to apply them. Example includes colors (Primary, Secondary, Tertiary, Neutral), typography scales, rounded corners, spacing. Agent reading the file produces UI matching the specified palette and fonts.
