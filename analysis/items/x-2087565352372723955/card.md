# Blender blockout camera path fed to Seedance 2.0/2.5 for cafe flythrough

`x-2087565352372723955` · x · demo-video · en · [source](https://x.com/abyssallD/status/2087565352372723955) · [raw](../../../raw/items/x-2087565352372723955/)
**Author:** Abyssal (@abyssallD) · **Published:** — · **Captured:** 2026-09-04T07:01:47Z
**Disposition:** analyze · **Readiness:** ready · **Gaps:** —
**Subject:** [blockout-to-video-flythrough](../../subjects/blockout-to-video-flythrough/brief.md) · **Also:** [ai-video-generation](../../subjects/ai-video-generation/brief.md) · **Roles:** technique, example · **Platforms:** blender, other

**Summary.** Demo of Claude Opus 5 building a crude cafe blockout in Blender, keying the real camera in the .blend file, then using that 3D camera move as the Seedance 2.0/2.5 motion reference for frame-accurate composition.
**Question it answers.** How do you lock a Seedance flythrough to a Blender-authored camera path instead of prompt-guessing?

**Claims.**
- `x-2087565352372723955#c1` (recipe, stated) Author keys an animated camera inside Blender on blockout geometry and feeds that move to Seedance 2.0/2.5 for starting-frame match and controlled push-through timing. — evidence: "Exact camera path animated inside the real .blend file

That 3D camera move becomes the reference for Seedance." [post]
- `x-2087565352372723955#c2` (capability, demonstrated) Quoted tweet 2083928568376004931 carries X article 2083925419800002560, titled Claude + Blender MCP: When AI Starts Controlling the Real Tool. fxtwitter article payload is 44 blocks / 42 nonempty / 3,924 chars. — evidence: "GET https://api.fxtwitter.com/abyssallD/status/2083928568376004931. article.id 2083925419800002560. First sentence: Most people still treat AI in 3D as a generator of pretty pictures." [note]
- `x-2087565352372723955#c3` (recipe, demonstrated) Article requirements: Claude Desktop + Blender 4.2+ (5.1+ recommended). Live check: delete the default cube and create a red metallic sphere. Sequential campsite recipe plus a four-stage angel animation (hover, scatter, spiral, reassembly). The result stays an editable .blend; high-end sculpting, rigging, and look-dev stay human. — evidence: "How to connect and verify / Building a full scene from conversation / Complex character animation through conversation / Where the human remains necessary. No cafe .blend filename in the 3,924-char body." [note]
- `x-2087565352372723955#c4` (availability, demonstrated) The cafe flythrough is an X amplify video 46.733 s at 1920×1080. No separate .blend or Seedance project file in this bank. Thread status is empty (0 replies reported). — evidence: "GET https://api.fxtwitter.com/abyssallD/status/2087565352372723955. video duration 46.733 width 1920 height 1080. replies 0." [note]
**Numbers.** Cafe flythrough duration: 46.733 seconds (note); Quoted Blender MCP article body: 3924 chars (note)
**Recipe.** 1. Block out scene geometry in Blender with simple primitives 2. Animate CineCamera path inside the .blend file 3. Export camera motion as Seedance 2.0/2.5 reference
**Techniques.** [blender-blockout-camera](../../techniques/blender-blockout-camera.md), [seedance-motion-reference](../../techniques/seedance-motion-reference.md)
**Tools.** [blender](../../tools/blender.md), [seedance](../../tools/seedance.md)
**Links.** https://x.com/i/article/2083925419800002560, https://x.com/abyssallD/status/2083928568376004931
**Related items.** [note-blender-minimax-h3-video-generation](../note-blender-minimax-h3-video-generation/card.md), [web-fal-ai](../web-fal-ai/card.md)
**Media.** —
**Thread.** empty · reported 0 · captured 0 · relevant 0 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [note-blender-minimax-h3-video-generation](../note-blender-minimax-h3-video-generation/card.md), [x-2092008677834387672](../x-2092008677834387672/card.md)
