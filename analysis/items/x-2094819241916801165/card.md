# GPT Image 2 face-swap stills plus Seedance 2.5 for realistic character video

`x-2094819241916801165` · x · thread · en · [source](https://x.com/abxxai/status/2094819241916801165) · [raw](../../../raw/items/x-2094819241916801165/)
**Author:** abxxai (@abxxai) · **Published:** — · **Captured:** 2026-09-04T06:54:39Z
**Disposition:** analyze · **Readiness:** ready-with-gaps · **Gaps:** thread-partial
**Subject:** [ai-video-generation](../../subjects/ai-video-generation/brief.md) · **Also:** [image-prompt-galleries](../../subjects/image-prompt-galleries/brief.md) · **Roles:** technique, example · **Platforms:** fal, other

**Summary.** Thread recipe for realistic AI character video: swap faces into reference stills with GPT Image 2, lock identity across scenes, then drive clips with detailed Seedance 2.5 prompts including dialogue and whip pans.
**Question it answers.** How do you combine GPT Image 2 face swaps with Seedance 2.5 to keep character identity across video scenes?

**Claims.**
- `x-2094819241916801165#c1` (recipe, stated) Author replaces characters in a reference still with a face photo using GPT Image 2 while preserving outfit, lighting, and pose before animating with Seedance 2.5. — evidence: "drop this image in GPT Image 2 as image_1, then drop YOUR own face photo as image_2

paste this prompt and it swaps your face into the scene, outfit and lighting untouched:" [quoted-post]
- `x-2094819241916801165#c2` (capability, demonstrated) Official Seedance 2.5 page advertises 30-second clips, reference control, white-model and green-screen editing — not face-swap or identity lock. — evidence: "https://seed.bytedance.com/en/seedance2_5 HTTP 200: up to 30 seconds, extend twice, precise reference control, white-model control, green-screen; no identity/face/character copy." [note]
- `x-2094819241916801165#c3` (availability, demonstrated) The root demo is an X amplify video 10.08 s at 1920×1080. Official Seedance 2.5 copy still does not claim identity lock. Thread stays captured_partial (1/57). — evidence: "GET https://api.fxtwitter.com/abxxai/status/2094819241916801165. video duration 10.08 width 1920 height 1080. replies 57." [note]
- `x-2094819241916801165#c4` (capability, demonstrated) leftover19: wuyoscar/GPT-Image2-Skill MIT 5,153★. README (2026-09-04) is a prompt gallery + 2 agent skills + CLI; edits use POST /v1/images/edits with repeatable -i for multi-reference. Official developers.openai.com image-generation guide 200 / 1,248,104 B. Neither page names identity lock. Face-swap stills stay the tweet recipe. — evidence: "leftover19 gh-gpt-image2-skill 5153 MIT; openai-image-gen 1248104 B. README multi-reference edit section." [note]
- `x-2094819241916801165#c5` (availability, demonstrated) leftover24 unused GitHub wuyoscar/GPT-Image2-Skill is MIT 5,154★ this pass (leftover19 was 5,153★). README still a prompt gallery + skills + CLI. Official Seedance 2.5 and this repo still do not name identity lock. — evidence: "leftover24 gh-gpt-image2-skill 5154 MIT." [note]
**Numbers.** Face-swap recipe demo duration: 10.08 seconds (note)
**Recipe.** 1. Swap face into reference still with GPT Image 2 using image_1 and image_2 2. Repeat for second character reference still 3. Attach locked stills to Seedance 2.5 with a single-scene cinematic prompt
**Techniques.** [agent-video-editing](../../techniques/agent-video-editing.md), [seedance-motion-reference](../../techniques/seedance-motion-reference.md)
**Tools.** [gpt-image-2](../../tools/gpt-image-2.md), [seedance](../../tools/seedance.md)
**Links.** https://github.com/wuyoscar/GPT-Image2-Skill, https://developers.openai.com/api/docs/guides/image-generation
**Related items.** [x-2092980272819999227](../x-2092980272819999227/card.md), [x-2095482056180638142](../x-2095482056180638142/card.md)
**Media.** —
**Thread.** captured_partial · reported 57 · captured 1 · relevant 1 · author thread: none → [thread.md](thread.md)
**Judge hints.** must_read: True · compare with: [x-2092980272819999227](../x-2092980272819999227/card.md)
