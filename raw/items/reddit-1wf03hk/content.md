# Deep Dog 2: I made the fifth best ranked deep research agent and am releasing it completely open source. It is easy to install and runs with a variety of LLM and search engine providers (default is deepseek + exa). It is completely free to use and runs async in python by default.

> Source: https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/
> Author: u/pizzababa21
> Posted: 2026-09-13T06:35:55+00:00
> Captured: 2026-10-15T08:55:18+00:00
> Score: 16 · Comments: 9
> Community: r/OpenSourceAI

## Post



Repository: https://github.com/beneadie/deep\_dog\_2

The quickest setup is:

    python -m pip install "git+https://github.com/beneadie/deep\_dog\_2.git"

Add your provider keys to a \`.env\` file:

    DEEPSEEK\_API\_KEY=your-deepseek-key
    EXA\_API\_KEY=your-exa-key

Then import it directly into Python:

    import asyncio
    from pathlib import Path
    
    from dotenv import load\_dotenv
    
    load\_dotenv()
    
    from deep\_research.integration import run\_research
    
    
    async def main():
        result = await run\_research(
            "What are the main benefits and limitations of sodium-ion batteries?"
        )
    
        print(result.status)
    
        if result.status == "completed":
            Path("report.md").write\_text(result.final\_report, encoding="utf-8")
            print("Saved report.md")
        else:
            print(result.failure)
    
    
    asyncio.run(main())

The default setup uses DeepSeek V4 Flash for the supervisor, research sub-agents, and drafting, with Exa for web search. The result is returned as a Markdown string, so developers can print it, save it, send it to another application, or process it however they want.

The more configurable quickstart lets you choose the models, search engine, enabled agents, research time, iteration limits, search budgets, read limits, and output behavior. Available specialist agents include Web, PubMed, Reddit, Substack, SEC Edgar, Arxiv, and others.

The code is designed to be modified. Developers can add agents, change prompts, swap providers, alter the supervisor and sub-agent behavior, adjust budgets, or integrate the result into their own application. The engine is packaged so you can use the integration layer without having to rebuild the orchestration system from scratch.

This project is completely free and released under the MIT License. I’m not building a business around it or offering a hosted service. The only potential costs are the provider APIs you choose to use, such as DeepSeek or Exa.

## Thread

> u/pizzababa21 · 2026-09-13T06:39:38+00:00 · score 2 · [comment](https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/p9i0s9w/)

Shit I don't know what happened to the link. Thanks for that

> u/pizzababa21 · 2026-09-13T06:40:39+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/p9i0wur/)

Link is fixed. Was the way reddit changed format when reposting 

> u/pizzababa21 · 2026-09-13T06:41:31+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/p9i10tj/)

Didn't make a video but I might later I guess 

> u/pizzababa21 · 2026-09-13T11:39:59+00:00 · score 2 · [comment](https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/p9j27bc/)

Just added a video demo. Also a bit of text comparing costs vs Gemini deep research api

> u/pizzababa21 · 2026-09-13T06:48:48+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/p9i1xn5/)

Well it's ranked well above those options on the benchmarks (although I noticed Gemini 3 deep research was removed from the leaderboard a while ago) and it's completely configurable to whatever model you want so cost is up to you. 

Thanks for the feedback though. 

> u/pizzababa21 · 2026-09-14T05:17:52+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/p9p3qr4/)

Sorry reddit keeps changing the link when I copy it over

## Comments

> u/AccomplishedFail9857 · 2026-09-13T06:38:26+00:00 · score 2 · [comment](https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/p9i0mqj/)

Is there a demo or video demonstration? I personally hate git repos where the only thing I can see is the usage after the setup on my local pc...

  
BTW: your link is broken...

> u/AccomplishedFail9857 · 2026-09-13T06:44:33+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/p9i1ecz/)

One short demo with speed up would be great. I speak from my POV - I want to see the value for every step I take. To setup all this - first you need to convince me that it is better than chatgpt research or gemini research. Atm the readme does not do that. Just an advice to grow your repo.

> u/JeffyPros · 2026-09-14T00:18:27+00:00 · score 1 · [comment](https://www.reddit.com/r/OpenSourceAI/comments/1wf03hk/deep_dog_2_i_made_the_fifth_best_ranked_deep/p9npw3i/)

The link doesn't work

Found it from your account: https://github.com/beneadie/deep_dog_2

## Links

- https://github.com/beneadie/deep\_dog\_2
- https://github.com/beneadie/deep\_dog\_2.git"
