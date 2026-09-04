# Research

## What it is

fal.ai: developer genmedia platform — 1,000+ image/video/audio/3D models via one API, plus serverless GPUs and dedicated H100/H200/B200 clusters. Docs llms.txt at fal.ai/docs/llms.txt.

## How it works

- Model APIs: playground, inference, CDN, ACLs, workflows, sandbox, usage or reserved pricing.
- Homepage samples at capture: MiniMax H3 Max T2V/I2V, FLUX 3 I2V, Seedance 2.5 I2V — the same family scroll-world uses via Monid.
- Serverless: on-demand, private models, BYO weights; Compute: reserved clusters from cited ~$1.89/hr H100.
- Claims 10x inference engine vs alternatives on flux[dev], 99.99% uptime, SOC2/SSO/private endpoints.
- No weights stored in this bank; agents should fetch llms.txt before deep dives.

## Why saved

Default HTTP backend for image-to-video in landing and BESS flythrough experiments when not using html-video/Hyperframes. Pairs with prompt galleries (MeiGen, GPT Image 2).

## Topics

`video-generation`, `agent-skills`

## Related

`github-oso95-scroll-world`, `github-nexu-io-html-video`, `github-wuyoscar-gpt-image2-skill`, `web-meigen-ai`, `github-nv-tlabs-ArtiFixer`

## Use when

Calling Seedance/MiniMax/FLUX from an agent; comparing API video vs HTML-rendered video; provisioning GPUs for genmedia.
