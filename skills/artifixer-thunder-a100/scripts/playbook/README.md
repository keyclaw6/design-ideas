# Playbook scripts (git copy)

Canonical instructions: [SKILL.md](../../SKILL.md).

Runtime artifacts (token, PEM, tarball, `instance.env`) live in `$ARTIFIXER_WORKROOT` (default `~/.cache/splat-mesh-maxqual/`), not in this directory.

```bash
DRY_RUN=1 bash skills/artifixer-thunder-a100/scripts/playbook/go.sh
```

Live: `DRY_RUN=0` only after a paid Thunder account and a token in `~/.cache/splat-mesh-maxqual/.env`.
