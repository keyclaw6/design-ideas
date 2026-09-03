# Browser session (resume)

**CDP port:** `BU_CDP_URL=http://127.0.0.1:40289` (headed agent-browser — **not** Grok Bot / `127.0.0.1:9222`)

**Tabs:**
- `t1` — X login wall
- `t2` — **Google “Sign in to continue to X”** (email form open — **needs you now**)

### Exact click (headed Chrome on desktop)

1. Switch to tab **“Sign in - Google Accounts”**
2. Enter your **X Google account** email → **Next**
3. Password + 2FA if prompted → allow X access

Then reply **`logged in`**.

### After login (agent runs)

```bash
export BU_CDP_URL=http://127.0.0.1:40289
/home/kab/design-ideas/scripts/x_clear_lists.sh   # Bookmarks + Likes
# then git commit/push, reddit_clear_saved.sh, catalog rebuild
```
