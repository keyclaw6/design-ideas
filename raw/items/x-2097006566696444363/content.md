# New video generation acceleration for MiniMax-H3 from the NVIDIA Sol team! Faster than playback, fully open-sourced

> Source: https://x.com/MiniMax_AI/status/2097006566696444363 — MiniMax (official) (@MiniMax_AI) — Mon Sep 07 16:58:20 +0000 2026 — 1201 likes · 87 reposts · 52 replies · 127434 views — captured 2026-09-21T15:29:07Z

## Post

**Author:** MiniMax (official) (@MiniMax_AI)
**URL:** https://x.com/MiniMax_AI/status/2097006566696444363

New video generation acceleration for MiniMax-H3 from the NVIDIA Sol team! 

Faster than playback, fully open-sourced, and available via the Reactor API so you can try it before committing your GPU😜

## Media

[media/quote_0.mp4](media/quote_0.mp4)
![](media/quote_0_thumb.jpg)

Originals:
- media/quote_0.mp4: quoted-tweet media (see Quoted post section)
- media/quote_0_thumb.jpg: quoted-tweet media (see Quoted post section)

## Quoted post

**Author:** Enze Xie (@xieenze_jr)
**URL:** https://x.com/xieenze_jr/status/2097000082927399012
**Posted:** Mon Sep 07 16:32:34 +0000 2026

🚀 Sol-H3: @MiniMax_AI H3 Video Generation Faster Than Playback 🤩

Five seconds of world. 1.653 seconds to infer.

We’re releasing Sol-H3, our fastest end-to-end MiniMax-H3 inference stack yet. On one 8× NVIDIA B300 Blackwell system, it generates five seconds of 1344×768 video with stereo audio in 1.653 seconds. Across 1×, 4×, and 8× B300, Sol-H3 reaches up to a 15.54× speedup versus Base H3.

Compared with 50-step Base H3 Dense on the same 8× B300 system, the four-step Sol-H3 profile delivers:
• 5s: 18.250s → 1.653s (11.04×)
• 10s: 50.660s → 3.732s (13.57×)
• 15s: 99.513s → 6.612s (15.05×)

Sol-H3 also scales across GPU counts:
• 4× B300: 2.918s / 6.993s / 12.542s for 5s / 10s / 15s (12.11–15.54×)
• 1× B300: 13.745s / 37.813s / 52.260s for 5s / 10s / 15s (9.45–14.29×)

All figures are medians of three measured runs after one warmup at 1344×768 and 24 FPS with stereo audio. Base H3 uses 50 scheduler points (49 DiT forwards); Sol-H3 uses four DiT forwards, so this is a full-profile comparison—not an attention-only runtime change. Sol-H3 uses Dense attention on 1× B300 and SOL with INT8 QKV / FP8 output transport on 4× / 8×. Timing includes text encoding, DiT denoising, and video/audio VAE decoding; model loading, compilation warmup, and final MP4 encoding are excluded.

Sol-H3 brings Sol-Engine × Sol-Attn into one full-stack runtime:
• dynamic sparse attention with no retraining
• fused norm, RoPE, MLP, and sparse-attention setup
• fused INT8 QKV / FP8 output communication across 8 GPUs
• parallel, batched VAE decoding
• precomputed AdaLN caching

Inside the stack:
• sparse-attention setup: 1.206 → 0.285 ms (−76.4%)
• VAE decode: 7.55 → 0.602 s
• ~24 GB memory freed per GPU

Any MiniMax-H3 few-step LoRA can plug into the same engine, and the code is deployment-friendly under Apache 2.0.

For us, the bigger milestone is crossing from “fast generation” into “faster than playback.” That opens the path toward continuous 24 FPS generation and truly interactive video systems.

We’re excited to partner with @reactorworld to release Sol-H3 and make it available as an API day-0.
Try it now on Reactor: https://www.reactor.inc/sandbox?model=fast-h3

🔗 https://nvlabs.github.io/Sana/Sol-Engine/Sol-H3/

Amazing team effort—full credits in the blog.
@shanasaimoe @lawrence_cjs @yitongli165665 @haopengl33 @HaochengXiUCB @songhan_mit

## Comments

**Gara (@Gara68902)** — https://x.com/Gara68902/status/2097172434453713381

MiniMax H3 delivers top-tier quality without asking for anything. Massive respect to MiniMax for making h3 open-source!

**Tresla (@ahitan76)** — https://x.com/ahitan76/status/2097172992727888257

The Niu Lai skills on MiniMax Design are absolute gold LOL!

**APEX ARTIST (@ApexArtistX)** — https://x.com/ApexArtistX/status/2097189005720965275

The news we are excited more is official 2k regenerate

**Catzilla (@Kratos733974)** — https://x.com/Kratos733974/status/2097173247456645422

Well, these tools are for pros. For us regular folks, I'd say use H3 on Hailuo or Design instead of burning cash on GPUs.

**Kevin Krone | Real Estate AI Studio (@Kevinkrone)** — https://x.com/Kevinkrone/status/2097167240919719952

@grok
 what hourly flu cost is associated here to get a cloud server up tonight?

## Links

- https://nvlabs.github.io/Sana/Sol-Engine/Sol-H3/
- https://www.reactor.inc/sandbox?model=fast-h3
- https://x.com/xieenze_jr/status/2097000082927399012
