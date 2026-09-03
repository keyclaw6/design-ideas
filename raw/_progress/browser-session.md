# Browser session (resume)

**CDP port:** `BU_CDP_URL=http://127.0.0.1:33789` (headed agent-browser — **not** Grok Bot / `127.0.0.1:9222`)

**Tabs:**
- `t1` — X login wall
- `t2` — **Google “Sign in to continue to X”** (email form open — **needs you now**)

### Option A — Google OAuth (headed Chrome tab t1)

1. In headed Chrome (`BU_CDP_URL` above), open tab **t1** (`x.com` login)
2. Click **“Fortsæt med Google”** / **Continue with Google** (must be a real click — popup is blocked for automation)
3. Complete Google sign-in → allow X access
4. Confirm `https://x.com/i/bookmarks` loads

### Option B — Cookie paste (if already logged in elsewhere)

From DevTools → Application → Cookies → `https://x.com`, copy `auth_token` and `ct0`, then:

```bash
export BU_CDP_URL=http://127.0.0.1:33789
export X_AUTH_TOKEN='...' X_CT0='...'
python3 /home/kab/design-ideas/scripts/x_inject_cookies.py
```

Then reply **`logged in`**.

### After login (agent runs)

```bash
export BU_CDP_URL=http://127.0.0.1:40289
/home/kab/design-ideas/scripts/x_clear_lists.sh   # Bookmarks + Likes
# then git commit/push, reddit_clear_saved.sh, catalog rebuild
```
