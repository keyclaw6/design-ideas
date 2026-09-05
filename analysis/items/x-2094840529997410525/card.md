# Atlas Fields Studio — free 3D EM field viewer for PCB designs

`x-2094840529997410525` · x · product · en · [source](https://x.com/Trevs_Dev/status/2094840529997410525) · [raw](../../../raw/items/x-2094840529997410525/)
**Author:** Trevor B (@@Trevs_Dev) · **Published:** 2026-09-01T17:31:17Z · **Captured:** 2026-09-02T17:39:26Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** —
**Subject:** [ai-cad-hardware](../../subjects/ai-cad-hardware/brief.md) · **Also:** [web-3d-scenes](../../subjects/web-3d-scenes/brief.md) · **Roles:** tool, reference · **Platforms:** browser, three-js

**Summary.** Arena Physica releases Atlas Fields Studio at fields-studio.arenaphysica.com, a free web app to explore electromagnetic fields around PCB designs powered by the Heaviside-1 foundation model. Shows millisecond E/H field predictions with hairpin filter templates.
**Question it answers.** What free web tool visualizes electromagnetic fields around PCB designs using Heaviside-1?

**Claims.**
- `x-2094840529997410525#c1` (capability, stated) Atlas Fields Studio lets you explore electromagnetic behavior around PCB designs for free. — evidence: "The Fields Studio App lets you explore electromagnetic behavior around PCB designs" [post]
- `x-2094840529997410525#c2` (result, demonstrated) Guest mode predicts 10,000 field vectors in about 45 ms at 10 GHz on a hairpin filter template. — evidence: "10,000 field vectors predicted in 45 ms | f = 10.000 GHz" [media]
- `x-2094840529997410525#c3` (capability, demonstrated) fields-studio.arenaphysica.com **225,703 B** (title Atlas Fields Studio). Beta launch: interactive viewer; predicted E/H fields update in milliseconds vs a commercial solver that can take hours. Default query **10,000** points; render 720p–8K; Heaviside-1 deep dive linked. arenaphysica.com **75,739 B** announces Heaviside-1 + Atlas Fields Studio Beta. Publication `/publications/heaviside-1` **382,556 B** (13 min; Sep 1, 2026): foundation model for 3D EM fields; natively encodes 3D structures + materials + excitation; try Atlas Fields Studio in beta. Tweet 45 ms / 10 GHz is on the capture screenshot, not repeated as a live HUD string in this HTML. — evidence: "GET fields-studio.arenaphysica.com 225703 B; arenaphysica.com 75739 B; /publications/heaviside-1 382556 B. leftover7-2026-09-05.json" [note]
**Numbers.** Field vectors predicted: 10000 vectors (media); Prediction time: 45 ms (media); Frequency: 10 GHz (media); Fields Studio HTML: 225703 bytes (note)
**Recipe.** —
**Techniques.** —
**Tools.** —
**Links.** paper (https://www.arenaphysica.com/publications/heaviside-1), product (https://fields-studio.arenaphysica.com/), https://www.arenaphysica.com/publications/rf-studio
**Related items.** —
**Media.**
`raw/items/x-2094840529997410525/media/thumb.jpg` (image, carries_technique=true) — Laptop screenshot of Atlas Fields Studio showing a 3D hairpin filter with colored E-field vectors, S-parameter plot, and 45 ms prediction overlay.
`raw/items/x-2094840529997410525/media/video.mp4` (video, carries_technique=true) — 15-second demo video of navigating the Atlas Fields Studio EM field viewer for PCB templates.
**Thread.** captured_partial · reported 71 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
