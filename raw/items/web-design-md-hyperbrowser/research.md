# Research

## What it is

design-md.hyperbrowser.ai: web tool that extracts a Google-format DESIGN.md from any website, powered by Hyperbrowser. API key stays in the browser locally.

## How it works

- Paste URL → remote/headless browser reads the site → emit DESIGN.md tokens + prose.
- Requires a Hyperbrowser API key (hyperbrowser.ai); not a fully free extractor like Sokosumi’s marketing claim.
- Follows google-labs-code/design.md spec so lint/diff CLI still applies.
- Capture via r.jina.ai; shadow DOM noted; UI chrome thin.
- Same job as Sokosumi and Refero Styles, different browser backend (Hyperbrowser vs unnamed remote browser).

## Why saved

One of the DESIGN.md extractors in the tranmautritam ecosystem thread. Useful when you already have Hyperbrowser credits or need a key-gated cloud browser for extraction.

## Topics

`design`, `agent-skills`, `mcp`

## Related

`github-google-labs-code-design-md`, `web-sokosumi-design-md`, `web-styles-refero-design`, `web-getdesign-md`, `web-aidesigner-mcp`

## Use when

Generating DESIGN.md from a live URL with Hyperbrowser; comparing extractors; feeding tokens into Impeccable/OpenDesign.
