# UC Berkeley just open-sourced FreeToken. (2–4x faster local LLM inference than Ollama) the results are wild: - Qwen3.6-3

@akshay_pachaar

UC Berkeley just open-sourced FreeToken.

(2–4x faster local LLM inference than Ollama)

the results are wild:

- Qwen3.6-35B on an 8GB GPU at 39.3 tokens/s
- DeepSeek-V4-Flash 284B on a 32GB GPU at 22 tokens/s
- GLM-5.2 753B on a 96GB GPU at 14.9 tokens/s

a 35B model at 16-bit precision needs about 70GB just for its weights. even at 4 bits it is close to 18GB, and FreeToken serves it on an 8GB GPU.

let me explain how:

all three models mentioned above are Mixture-of-Experts, and that is what FreeToken takes advantage of. each layer holds hundreds of separate experts plus a small router that picks a few of them per token.

Qwen3.6-35B activates roughly 3B of its 35B parameters per token. DeepSeek-V4-Flash picks 6 of 256 experts per layer, so 13B of its 284B run at a time.

so compute was never the bottleneck. the weights a single step touches fit comfortably on a consumer GPU.

every expert the router might pick still has to exist somewhere. they sit in system RAM, and the GPU keeps a cache of the ones the model has been using recently.

so everything comes down to what happens when the router picks an expert that is not on the GPU.

there are two ways to serve that miss:

1. copy it over PCIe and run it on the GPU
2. run it on the CPU, where it already lives

both read from the same system memory, so they compete for one pool of bandwidth instead of adding to each other. existing engines pick one option and freeze it when the model loads.

but routing changes on every token, so a fixed choice misses most of what the model asks for.

FreeToken measures both bandwidths on your machine and splits each step's misses between the two paths in proportion. the GPU and CPU results then merge exactly, with no approximation.

two machines with the same GPU can end up wanting opposite strategies, which I did not expect. a 5090 in a gaming desktop should push nearly everything over PCIe, while an 8GB laptop is better off computing most misses on the CPU.

none of that is readable off a spec sheet, so the engine profiles it once per machine.

the second half of the design is about agents. coding agents constantly rewrite their own history, and every edit normally forces thousands of tokens back through prefill.

FreeToken saves its checkpoints at the exact boundaries agent frameworks cut on, so it only reprocesses the new part. its slowest first token stays under 44 seconds, while llama.cpp peaks at 232 and KTransformers at 946.

it serves the OpenAI and Anthropic APIs under Apache 2.0, so Claude Code and Codex can point at it directly.

releasing weights publicly decides who can download a model, not who can afford to run one. frontier open models keep shipping, and running them still assumes a rented cluster.

meanwhile there are over a hundred million consumer machines with discrete GPUs sitting mostly idle. closing that gap was never a hardware problem, and work like this is what turns open weights into something you can actually use.

paper: https://arxiv.org/pdf/2608.16157

repo: https://github.com/FlashML-org/FreeToken

almost every idea in this post, from why memory bandwidth decides the outcome to why moving weights costs more than computing on them, comes straight out of how a GPU is built. I wrote a detailed primer on that.

the article is quoted below.
