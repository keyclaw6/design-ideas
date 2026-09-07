# Your only job

1. Open https://console.thundercompute.com/login
2. Create an account (Google, GitHub, or email).
3. Add a **payment card** under Settings → Billing.
4. Add credit if the console asks — Thunder’s minimum shown in the UI is **$10** (not $5).

Then ping me. Do nothing else: no tokens, no SSH keys, no `tnr`, no Create instance.

I will use the Cursor browser on this machine to mint an API token, log the CLI in, rent the GPU, use the SSH key Thunder returns, run the splat→mesh pipeline, download results, and delete the instance.

Kill switch after a run starts: `touch /home/kab/.cache/splat-mesh-maxqual/KILL`

GPU: Thunder **A100 80GB** (~$1.66/hr with 16 vCPU + 400 GB), not H100.
