# HIVE Group 考核执行计划

## 任务范围

目标：在约一个月内完成 HIVE Group 具身智能最小可行培养方案。

最终需要留下的材料包括：

- PyTorch 练习代码和学习笔记。
- Linux、conda、tmux、VSCode Debug 等工具链命令记录。
- 至少 3 篇具身智能相关论文，并加入 Zotero 或其他文献库。
- 一份以 Diffusion Policy 为主线的论文阅读报告。
- 一份 10 页以内的论文汇报 PPT。
- 一个 Diffusion Policy 复现文件夹，包含脚本、配置、结果和 README。
- 一份 10-15 页的最终项目汇报 PPT。

## 第 1-2 周：基础知识

### PyTorch 与 Python

- [ ] 看完或快速过完小土堆 PyTorch 入门。
- [ ] 跟着运行示例代码，不要只看视频。
- [ ] 把不懂的代码块交给 AI 解释，并自己修改运行。
- [ ] 把练习代码放到 `embodied-ai-bootcamp/pytorch_practice/`。
- [ ] 在 `pytorch_practice/README.md` 里记录学到的内容和运行命令。

### 计算机视觉基础

- [ ] 快速学习 CS231N 相关材料，目标是建立整体概念。
- [ ] 理解卷积、池化、ResNet、特征提取、分类任务等概念。
- [ ] 写一页笔记：视觉编码器在机器人学习中起什么作用？

### 具身智能与机器人基础

- [ ] 观看 Notion 页面中推荐的具身智能入门视频。
- [ ] 理解 embodied AI、robot manipulation、pick-place、开门、倒水等任务。
- [ ] 学习机械臂正运动学和逆运动学的基本含义。
- [ ] 整理 10-15 个术语的小词典。

## 第 2 周：科研工具链

### 账号与编辑器

- [ ] 安装 VSCode 或 Cursor。
- [ ] 准备 GitHub、Google Scholar、arXiv、谷歌邮箱等账号。
- [ ] 新建 GitHub 仓库：`embodied-ai-bootcamp`。

### 服务器与 Linux

- [ ] 在 AutoDL、OneThingAI 等平台租用或准备一台 GPU 服务器。
- [ ] 使用 VSCode Remote SSH 连接服务器。
- [ ] 练习常用命令：`pwd`、`ls`、`cd`、`mkdir`、`cp`、`rm`、`cat`、`less`、`nvidia-smi`。
- [ ] 把命令和解释记录到 `linux_notes.md`。

### Conda 与 PyTorch 环境

- [ ] 了解 conda 的作用。
- [ ] 创建一个新的 conda 环境。
- [ ] 按服务器 CUDA 版本安装 PyTorch。
- [ ] 在该环境下成功运行一份 PyTorch 练习代码。
- [ ] 记录环境创建和安装命令。

### Git 基本操作

- [ ] `git clone` 自己的仓库。
- [ ] 添加练习代码和笔记。
- [ ] 使用 `git add`、`git commit`、`git push` 提交。

### tmux 与 Python Debug

- [ ] 新建一个 tmux session。
- [ ] 在 tmux 中运行一段 Python 训练脚本。
- [ ] 练习 detach 和 attach。
- [ ] 创建 `.vscode/launch.json`。
- [ ] 在 VSCode 中设置断点、单步执行、查看变量。

## 第 3 周：科研入门与文献汇报

### 找文献

- [ ] 在 Google Scholar / arXiv 搜索 `robot manipulation`。
- [ ] 选择至少 3 篇具身智能相关论文。
- [ ] 加入 Zotero 或其他文献库，并用 `Embodied` 标签归类。

### 精读 Diffusion Policy

主线论文：

- 题目：Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
- arXiv：https://arxiv.org/abs/2303.04137
- 项目主页：https://diffusion-policy.cs.columbia.edu

阅读时重点回答：

- [ ] 这篇论文解决什么任务？
- [ ] 为什么直接做行为克隆比较困难？
- [ ] diffusion 如何建模动作分布？
- [ ] observation horizon、prediction horizon、action execution horizon 分别是什么意思？
- [ ] 为什么使用 receding-horizon control？
- [ ] 视觉编码器的作用是什么？
- [ ] 实验结果说明了什么？
- [ ] 自己有哪些 2-3 个疑问或扩展想法？

### 文献汇报

- [ ] 做一份 10 页以内的 PPT。
- [ ] 控制在 10-15 分钟讲完。
- [ ] 内容包含问题背景、方法图、关键细节、实验结果、自己的理解与疑问。
- [ ] 排版清晰，中文建议微软雅黑，英文建议 Times New Roman。

## 第 4 周：Diffusion Policy 复现闭环

### 代码准备

- [ ] 从项目主页找到官方 GitHub 仓库。
- [ ] Fork 到自己的 GitHub 账号。
- [ ] 在服务器上 clone 仓库。
- [ ] 创建 conda 环境。
- [ ] 跑通官方 demo 或测试脚本。

### 实验复现

- [ ] 选择一个代表性任务，优先选择小任务或官方 demo。
- [ ] 完成一次训练和测试流程。
- [ ] 记录超参数、训练时长、GPU、随机种子和结果。
- [ ] 保存 loss 曲线、终端日志、评估截图或视频。
- [ ] 如果能对齐论文同一 benchmark，就与论文指标对比。
- [ ] 分析结果差异可能来自哪里。

### 扩展尝试

- [ ] 找到代码中视觉特征提取器的位置。
- [ ] 尝试将视觉 backbone 替换成 CLIP。
- [ ] 训练或至少完成一个小规模对比。
- [ ] 记录性能变化、失败原因或现象。

### GitHub 整理

- [ ] 在 `embodied-ai-bootcamp` 中新建 `diffusion_policy/` 文件夹。
- [ ] 放入脚本、配置、笔记和截图。
- [ ] 写好 `diffusion_policy/README.md`。
- [ ] commit 并 push 到 GitHub。
- [ ] 把链接发给学长学姐检查。

## 时间不够时的优先级

1. GitHub 仓库要干净、清楚、能看懂。
2. 至少跑通官方 demo。
3. 优先完成一个小任务闭环，不要一开始追求大规模 benchmark。
4. PPT 要讲清楚问题、方法、实验、结果和反思。
5. 失败也要记录清楚命令、日志和尝试过的解决方法。
