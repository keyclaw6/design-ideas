# cards-05 handoff

**Worker:** cards-05  
**Batch:** batch-05  
**Written:** 2026-09-04

## IDs owned (20)

```
github-emilkowalski-skills
github-wuyoscar-gpt-image2-skill
web-designmd-me
web-oryzo-ai
x-2080856252687745093
x-2087178722420171020
x-2087708050002239702
x-2088254428730085690
x-2088830609615397333
x-2090079734571098131
x-2091441060153278565
x-2091729720303874220
x-2092106682302140648
x-2093013941412852083
x-2093374092795846745
x-2093766772029559077
x-2094424821450817563
x-2094840529997410525
x-2095159781883597031
x-2095512142766342624
```

## IDs done (20)

All 20 IDs above have `analysis/items/<id>/card.json` written and validated (`validate_cards.py` exit 0).

## Disposition summary

| Disposition | Count | IDs |
|-------------|-------|-----|
| analyze | 16 | all except shelved below |
| shelf | 4 | x-2088830609615397333 (duplicate), x-2091729720303874220 (out-of-scope), x-2094424821450817563 (noise) |

## Blocked / failed

None. All cards validate.

## Notable gaps flagged

- `web-designmd-me` — `linked-page-unfetched` (Vercel 429 checkpoint)
- `x-2093374092795846745` — `linked-page-unfetched` (tutorial URL not in capture)
- `x-2095159781883597031` — `translation-needed` (Japanese post)
- Several X items show `ready-with-gaps` due to partial `thread.json` from thread worker (no card gaps added)

## Media notes

- `x-2088830609615397333`, `x-2092106682302140648`, `x-2093766772029559077` — `media_0.jpg` files are MP4 video; typed as `video` per `file` detection.
- `x-2093374092795846745` — source notes media omitted (>100 MB); no media folder.

## Alias proposals

```json
[]
```

## Reclass proposals

```json
[
  {
    "from": "x-2094424821450817563",
    "to": "outbound-gtm-agents",
    "why": "Employee-led LinkedIn GTM playbook content fits outbound-gtm-agents seed_items, but shelved as engagement-bait because the artifact is DM-gated with no capture."
  }
]
```
