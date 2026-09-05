# Portfolio carousel with inertial swing entry instead of flat slide

`x-2089223944700326052` · x · article · zh · [source](https://x.com/Heylaosan/status/2089223944700326052) · [raw](../../../raw/items/x-2089223944700326052/)
**Author:** 张老三laosan (@Heylaosan) · **Published:** — · **Captured:** 2026-09-04T06:49:30Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [landing-ui-motion](../../subjects/landing-ui-motion/brief.md) · **Also:** — · **Roles:** technique, example · **Platforms:** react, other

**Summary.** Laosan breakdown of YousufSoomroDev open portfolio carousel: cards enter with swing and inertia from off-screen, overshoot, then one or two decaying rebounds. Warns long oscillation hurts browse throughput for photography and poster showcases.
**Question it answers.** What spring motion recipe makes a portfolio carousel feel physical instead of template sliding?

**Claims.**
- `x-2089223944700326052#c1` (recipe, stated) Carousel cards enter with swing and inertia rather than sliding on a flat horizontal track. — evidence: "卡片不是沿着水平轨道简单滑入，而是带着明显的摆动和惯性从画面外进入，最终回到稳定位置。" [post]
- `x-2089223944700326052#c2` (recipe, stated) Author recommends capping rebound count to one or two decay cycles for browse efficiency. — evidence: "保持一到两次明显衰减，会更接近真实物理反馈。" [post]
- `x-2089223944700326052#c3` (availability, demonstrated) The breakdown is an X amplify video 44.559 s at 2560×1626. Thread status is empty (0 replies reported). — evidence: "GET https://api.fxtwitter.com/Heylaosan/status/2089223944700326052. video duration 44.559 width 2560 height 1626. replies 0." [note]
- `x-2089223944700326052#c4` (availability, demonstrated) Quoted tweet 2075520890880827512 points at https://inspo-design.pages.dev/ (200 / 10,859 B). Title Inspo.design - 设计与 UX 收藏. H1 设计灵感. Live copy says 0 条内容 in that section. One outbound href: sanhao-design-weekly.pages.dev. GitHub user YousufSoomroDev 404 this pass; the carousel repo is still not in this bank. — evidence: "GET https://inspo-design.pages.dev/ 200 10859 B. analysis/_work/captures/inspo-design-pages-2026-09-05.json" [note]
**Numbers.** Carousel breakdown duration: 44.559 seconds (note)
**Recipe.** —
**Techniques.** [parallax-scroll-landing](../../techniques/parallax-scroll-landing.md), [ui-motion-physics](../../techniques/ui-motion-physics.md)
**Tools.** —
**Links.** https://inspo-design.pages.dev/
**Related items.** [github-nateherkai-scroll-craft](../github-nateherkai-scroll-craft/card.md), [github-nexu-io-motion-anything](../github-nexu-io-motion-anything/card.md), [web-animos-editor](../web-animos-editor/card.md), [x-2089775679600812150](../x-2089775679600812150/card.md)
**Media.** —
**Thread.** empty · reported 0 · captured 0 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: False · compare with: —
