# Agent 记忆不该只记成功的——失败的轨迹同样有价值，推理过程本身就是最好的记忆内容。 Google Research 开源 ReasoningBank：经验驱动的记忆被当作继参数规模、测试时计算之后的第三个扩展维度。 Reasoning

**Author:** yibie (@yibie)
**URL:** https://x.com/yibie/status/2087143369181114868

Agent 记忆不该只记成功的——失败的轨迹同样有价值，推理过程本身就是最好的记忆内容。

Google Research 开源 ReasoningBank：经验驱动的记忆被当作继参数规模、测试时计算之后的第三个扩展维度。

ReasoningBank：让 agent 从成功和失败的轨迹里自我进化

是什么

Google Research 刚开源的 ReasoningBank——一个 agent 记忆机制：从成功和失败的轨迹中都学习，把推理本身当作记忆内容存储。

大部分 agent 记忆系统只记成功经验（或者只记事实）。ReasoningBank 的关键差异：失败的轨迹同样进记忆——推理过程（怎么走到那一步的）才是记忆的载体，而不只是结果。

memory-aware test-time scaling（核心贡献）

在记忆配方之上，提出记忆感知的测试时扩展：利用记忆与测试时计算的双向协同。

• 记忆让测试时扩展更高效（已经踩过的坑不用再踩）
• 测试时扩展反哺记忆（探索过程中产生的新经验继续入库）

作者的主张：经验驱动的记忆，是 agent 系统在"模型参数规模"和"测试时计算量"之外的第三个扩展维度。

代码

• SWE-Bench（软件工程）+ WebArena（web 浏览）两个基准的完整实现
• 支持 GPT 模型（gpt-3.5-turbo / gpt-4 / gpt-4o）
• WebArena 里带 llm-as-a-judge 的自动评估（轨迹正确性信号）
• 非官方 Google 产品（社区实验性质）

git clone https://github.com/google-research/reasoning-bank
cd reasoning-bank/SWE-Bench && ./run.sh   # 配置 VertexAI 后直接跑

原文：https://github.com/google-research/reasoning-bank
#Agent记忆 #自我进化 #开源
