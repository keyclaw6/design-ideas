# Comments / thread

fx/vx return counts only. Conversation list APIs failed:

- `api.fxtwitter.com/.../status/{id}` and `/replies` — parent tweet only
- `api.vxtwitter.com` — reply *count* (2), no thread
- `cdn.syndication.twimg.com/tweet-result` — truncated note-tweet + media
- `r.jina.ai` on `http://x.com/0x0SojalSec/status/…` — post body + HF card only
- `r.jina.ai` on conversation search — login wall
- Threadreader — login wall
- xcancel — shut down; nitter.poast.org — DNS fail

No author self-replies (`replying_to` null). Thread text is the note-tweet in `post.md`. 2 replies not captured without X login.

## Model (from tweet URL, not comments)

Tweet links **https://huggingface.co/nvidia/ArtiFixer**. Verified:

- Paper: de Lutio et al., *ArtiFixer: Enhancing and Extending 3D Reconstruction with Auto-Regressive Diffusion Models*, SIGGRAPH 2026. [arXiv:2603.00492](https://arxiv.org/abs/2603.00492)
- Code: [nv-tlabs/ArtiFixer](https://github.com/nv-tlabs/ArtiFixer) (Apache-2.0, 635★ at capture)
- Project: https://research.nvidia.com/labs/sil/projects/artifixer/
