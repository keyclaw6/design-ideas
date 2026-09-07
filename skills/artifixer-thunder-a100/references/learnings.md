# Live learnings — fill this on the first GPU run

This file starts empty of facts. **Everything in SKILL.md is unproven.** After each surprise, add a dated entry here, then patch SKILL.md / scripts so the next agent does not rediscover it.

Template:

```
## YYYY-MM-DD — <step>
- Observed:
- Command / JSON:
- Fix applied:
- SKILL.md / script updated: yes/no
```

## Still unknown (strike out when proven)

- [ ] `tnr create --json` fields match `parse_tnr_create.py` (`identifier`, `uuid`, `key`)
- [ ] `tnr status --json` is list vs map; `parse_tnr_status.py` finds RUNNING + public IP
- [ ] SSH user is `ubuntu` (else `root`); create-response PEM works without add_key
- [ ] `tnr scp` accepts numeric `identifier` and copies `scenes.tar.gz` + remote scripts
- [ ] Qwen3-VL-30B-A3B caption fits A100 80GB after 3DGRUT; unload before 14B
- [ ] Wan-14B construct survives 128 GB host RAM (16 vCPU); 96 GB fallback
- [ ] C4 30k recon is not needle soup (`c4_gate.py` pass)
- [ ] `dump_rgbd.py` writes `*.color.png` + `*.depth.npy` + `*.pose.txt` + `K.txt`
- [ ] Local Open3D TSDF produces a usable mesh from those dumps
- [ ] Delete actually stops billing (no snapshot left behind)
- [ ] True wall-clock $ for five/six scenes vs ~$1.66/hr estimate
