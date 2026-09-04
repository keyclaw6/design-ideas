# Research

## What it is

DiceBear: privacy-focused open-source avatar library — 61 styles, deterministic pictures from a seed via HTTP API and many language SDKs. Playground, editor, Figma custom-style pipeline.

## How it works

- API: `https://api.dicebear.com/10.x/{style}/{format}?seed=...` (e.g. lorelei SVG).
- Libraries: JS (`@dicebear/core` + styles), PHP, Python, Rust, Go, Dart, C#, CLI `npx dicebear`.
- Editor at editor.dicebear.com for no-code PNG export.
- Custom styles: Figma components with naming conventions → Studio plugin → JSON consumed by all runtimes.
- Core MIT. Use cases: profiles, chat, games, forums, placeholders — no Gravatar upload.

## Why saved

Daily-seeded decorative avatars/easter eggs on marketing sites without storing user photos. Lightweight craft asset next to TinyShots polish.

## Topics

`design`

## Related

`web-tinyshots`, `github-deedy-qr-data-transfer`, `web-checklist-design`, `github-wuyoscar-gpt-image2-skill`, `web-cult-ui`

## Use when

Need deterministic avatars from user ids or dates; shipping a custom avatar style from Figma; placeholders on a community/marketing site.
