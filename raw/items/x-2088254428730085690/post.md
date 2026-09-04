# Impeccable 4.1 is here: core: -critique results more reliably prints in chat before asking you questions - the design ho

**Author:** Paul Bakaus (@pbakaus)
**URL:** https://x.com/pbakaus/status/2088254428730085690

Impeccable 4.1 is here:

core:
-critique results more reliably prints in chat before asking you questions
- the design hook nags less, and ignores can be recorded once
- reduced-motion guidance restored

greenfield design:
- switch between comps of your page/app before any code or skip mockups and go straight to code
- steer ideation to be bolder or safer in the interactive question tool
- mockups for new pages of an existing site/app stay more consistent
- much better fallback for agents without image generation

native apps:
- ios and android builds get reviewed against native conventions
- polish collects native evidence instead of asking for browser screenshots
- web-only checks stop firing on native code

platforms and setup:
- windows: installs, the decision page, and the roll all work now
- plugin installs: the four subagents actually load (they silently never did)
- support for @NousResearch hermes agent and @antigravity 

design issue detection:
- no false low-contrast on gradient backgrounds, image backgrounds, or covered text
- data-impeccable-ignore silences only the element you put it on
- broken-image warnings stop firing on commented-out code
- blade files show up in directory scans
- paths with spaces or quotes stop breaking commands

live mode:
- works on ddev, valet, and other non-localhost dev hosts
- svelte variants render again (broke due to svelte upstream changes)
- copy edits survive long pages

43 prs since the last release - great time to upgrade or try out the latest: npx impeccable install

http://impeccable.style
