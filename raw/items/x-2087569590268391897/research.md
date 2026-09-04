# Research

## What it is
Empty X capture: title is the placeholder “X post 2087569590268391897”, body is only the author handle @dexhorthy, no text, media, or linked artifact.

## How it works
- Harvest stored a bookmark/like with no tweet body (quote-tweet, deleted post, or failed fetch).
- `post.md` is 43 characters; comments file is a stub; no media directory entries.
- PLAN filter rule: empty quote-tweet with no linked artifact → mark filtered, keep on disk.

## Why saved / why filtered
Nothing actionable remains. Likely a quote-tweet or media-only post that the harvest did not resolve. Filtered so the catalog does not treat a blank folder as a technique.

## Topics
(none — filtered)

## Related
- `x-2087224641849045110` — another empty “X post <id>” capture
- `x-2087733334617063503` — slogan-only Google Cloud post, also filtered
- `x-2087715372787228734` — vendor promo with no technique, also filtered

## Use when
Do not pull. Re-fetch from https://x.com/dexhorthy/status/2087569590268391897 only if a later pass needs to recover deleted context.
