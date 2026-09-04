# Portfolio carousel with inertial swing entry instead of flat slide

`x-2089223944700326052` · x · article · zh · [source](https://x.com/Heylaosan/status/2089223944700326052) · [raw](../../../raw/items/x-2089223944700326052/)
**Author:** 张老三laosan (@Heylaosan) · **Published:** — · **Captured:** 2026-09-04T06:49:30Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [landing-ui-motion](../../subjects/landing-ui-motion/brief.md) · **Also:** — · **Roles:** technique, example · **Platforms:** react, other

**Summary.** Laosan breakdown of YousufSoomroDev open portfolio carousel: cards enter with swing and inertia from off-screen, overshoot, then one or two decaying rebounds. Warns long oscillation hurts browse throughput for photography and poster showcases.
**Question it answers.** What spring motion recipe makes a portfolio carousel feel physical instead of template sliding?

**Claims.**
- `x-2089223944700326052#c1` (recipe, stated) Carousel cards enter with swing and inertia rather than sliding on a flat horizontal track. — evidence: "卡片不是沿着水平轨道简单滑入，而是带着明显的摆动和惯性从画面外进入，最终回到稳定位置。" [post]
- `x-2089223944700326052#c2` (recipe, stated) Author recommends capping rebound count to one or two decay cycles for browse efficiency. — evidence: "保持一到两次明显衰减，会更接近真实物理反馈。" [post]
**Numbers.** —
**Recipe.** —
**Techniques.** [parallax-scroll-landing](../../techniques/parallax-scroll-landing.md), [ui-motion-physics](../../techniques/ui-motion-physics.md)
**Tools.** —
**Links.** —
**Related items.** [github-nateherkai-scroll-craft](../github-nateherkai-scroll-craft/card.md), [github-nexu-io-motion-anything](../github-nexu-io-motion-anything/card.md), [web-animos-editor](../web-animos-editor/card.md), [x-2089775679600812150](../x-2089775679600812150/card.md)
**Media.** —
**Thread.** empty · reported 0 · captured 0 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
