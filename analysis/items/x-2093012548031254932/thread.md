# Thread — vgpu: minimal WebGPU shader library built for coding agents (x-2093012548031254932)

**Status:** captured_partial · **Author thread:** none · **Replies reported:** 71 · **Captured:** 1 · **Relevant:** 1 · **Unfetched:** 70 · **Truncated:** False
**Fetch log:** x-web-dom→ok (2026-09-04T17:54:20Z); fxtwitter-api→ok (2026-09-04T17:54:20Z)
**Raw payloads:** `raw/items/x-2093012548031254932/thread-raw/x-web-dom-20260904T175324Z.html`

**Author continuation (0 posts).**
**Quoted.**
> **@matiNotFound** · 2093012551596396694
> My first attempt at this library was to design a minimal API that let me ship shaders with a few lines of code.

It was the "dream api" that I always wanted, super minimal, abstracting all the verbosity away, but it came with a cost: It was hard for agents to use

It had too many https://t.co/vuHKnTtxTg

> **@matiNotFound** · 2093012554947670024
> I started going back and forth between abstraction levels to find the right utilities. Keeping low-level control while making it easier for agents to understand.

After shipping many shaders on https://t.co/bMBjNsc9U2, we found that allowed us to improve on performance a lot https://t.co/Z5CHY6fTHD

> **@matiNotFound** · 2093012558554730838
> Agents usually just open a browser to check their work; waiting ~10 seconds to check for a syntax error is too slow.

This is where the CLI helps:
- `vpgu docs` and `vgpu examples` to quickly learn
- `vgpu check` to validate shader code syntax https://t.co/qcNydXfC0f

> **@matiNotFound** · 2093012561943785844
> If your agent is shipping in a cloud sandbox, it probably won't have a GPU.

Usually they go, "oh I cannot render this", and give up.

vgpu solves this by shipping a CPU renderer that they can install to test their code.

This also makes `agent-browser --webgpu` work anywhere https://t.co/vKPMgntdBP

> **@matiNotFound** · 2093012565005566216
> The headless renderer also lets us write tests that run on CI.

...or render our shaders as high-resolution videos locally.

On Mac, rendering runs natively on Metal, so it's real GPU speed https://t.co/d3qpaqo8U0

> **@matiNotFound** · 2093012568696659973
> And finally, my favorite feature: WGSL modules.

This allows us to write shaders in the WebGPU Shader Language

We can now create shader libraries and registries.

The WGSL code gets minified and validated at build time. https://t.co/UoQikHJonZ

> **@matiNotFound** · 2093012571569692962
> Docs and examples are available at https://t.co/OGcCMpMLvi

All feedback is welcome!

**Relevant replies (1 of 1 captured).**
> **@vercel** · 2093172148978487504 · depth 1 · link
> @matiNotFound awfully recreated balatro fire with vgpu https://t.co/dzUuNpvU3f

**Dropped as noise:** 0 replies (praise, emoji, bots, unrelated promo).
