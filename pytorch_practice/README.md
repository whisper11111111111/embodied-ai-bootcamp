# PyTorch 练习记录

这个文件夹用于记录 HIVE Group 考核第一阶段的 PyTorch 学习。

## 当前目标

先跑通基础 PyTorch 代码，不追求一次学完所有细节。重点是形成“代码能运行、命令有记录、问题有总结”的学习证据。

## 需要完成

- [x] 确认 Python / PyTorch 环境可用。
- [x] 跑通张量基础代码。
- [ ] 跑通 Dataset / DataLoader 示例。
- [ ] 跑通一个简单神经网络训练示例。
- [ ] 把每次运行的命令和问题记录下来。

## 运行记录

### 第 1 次练习：Tensor 基础与 GPU 检查

- 日期：2026-07-02
- 代码文件：`tensor_basics.py`
- 运行环境：`latex_env`
- PyTorch 版本：`2.7.0+cu128`
- CUDA 是否可用：`True`

运行命令：

```bash
python tensor_basics.py
```

运行结果摘要：

- 成功创建了一维 tensor 和二维矩阵。
- 成功完成 tensor 加法。
- 成功查看 tensor 的 `shape` 和 `dtype`。
- 成功完成矩阵乘法 `x @ y`。
- 成功检测到 CUDA 可用。
- 成功把 tensor 移动到 GPU，并在 `cuda:0` 上完成矩阵乘法。

本次收获：

- 了解了 PyTorch 中 tensor 的基本创建方式。
- 知道了 `.shape` 可以查看张量形状，`.dtype` 可以查看数据类型。
- 学会了使用 `@` 进行矩阵乘法。
- 学会了用 `torch.cuda.is_available()` 检查 GPU 是否可用。
- 初步理解了 `.to("cuda")` 的作用：把数据移动到 GPU 上计算。

遇到的问题：

- 暂无，脚本运行正常。

下一步：

- 学习 `Dataset` 和 `DataLoader`。
- 写一个最简单的神经网络训练脚本。
