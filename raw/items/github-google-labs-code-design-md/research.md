# Research

## What it is

Google Labs’ DESIGN.md format: YAML front matter (machine-readable tokens) plus markdown prose (rationale) so coding agents persistently share a design system. Spec also used by Stitch.

## How it works

- Tokens encode exact colors, type scales, radii, spacing; prose explains when to apply them.
- CLI: `npx @google/design.md lint DESIGN.md` (WCAG contrast, token validation) and `npx @google/design.md diff` for version compare — CI-style design governance.
- Spec published at stitch.withgoogle.com/docs/design-md/specification.
- Agents reading the file are expected to match palette and fonts rather than inventing Inter + purple.
- Ecosystem of extractors (Hyperbrowser, Sokosumi, Refero, getdesign.md) all target this file shape.

## Why saved

This is the contract format for vibe-design and BESS marketing sites: one file agents and humans can lint. Every DESIGN.md generator in the bank is downstream of this spec.

## Topics

`design`, `agent-skills`

## Related

`web-getdesign-md`, `web-sokosumi-design-md`, `web-styles-refero-design`, `web-design-md-hyperbrowser`, `github-pbakaus-impeccable`

## Use when

Standing up a brand DESIGN.md; wiring lint/diff in CI; comparing extractors; locking Cursor/Stitch/OpenDesign to energy-sector or product tokens.
