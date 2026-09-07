# Agent console path (not the human)

Signed-out shell still shows the sidebar. Proof of session: **not** “Signed Out”, and Billing controls are enabled.

1. Login: https://console.thundercompute.com/login (Google / GitHub / email).
2. Billing: https://console.thundercompute.com/settings/billing — card + credit (min $10).
3. Tokens: https://console.thundercompute.com/settings/tokens — create `splat-mesh-maxqual`, copy once.
4. `tnr login --token '<token>'` then write token to `$ROOT/.env` (`chmod 600`). Never paste the token into chat.
5. Optional: Settings → Authentication → SSH Keys if create-response `key` is empty.
6. Do **not** click Create in the console; `playbook/go.sh` owns create/delete.

`tnr login` without `--token` opens the OS browser. Prefer Cursor browser + `--token`.
