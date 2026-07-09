# 第 2 天：Dataset 与 DataLoader 学习记录

## 学习目标

今天的目标是理解 PyTorch 如何读取数据。

一句话总结：

```text
Dataset 负责定义数据怎么取，DataLoader 负责按 batch 批量取数据。
```

## 练习代码

代码文件：

```text
dataset_dataloader_commented.py
```

运行命令：

```bash
python dataset_dataloader_commented.py
```

## 本次练习内容

这次使用了一个很小的人工数据集：

```text
x = 1, 2, 3, 4, 5, 6, 7, 8
y = 2x + 1
```

也就是说：

```text
x = 1 -> y = 3
x = 2 -> y = 5
x = 3 -> y = 7
```

后面训练模型时，模型要学习的就是这个对应关系。

## 对 class 的理解

`class` 用来定义一种“东西”或“模板”。

在这次代码里：

```python
class SimpleRegressionDataset(Dataset):
```

意思是：定义一个叫 `SimpleRegressionDataset` 的数据集模板。

括号里的 `Dataset` 表示：这个类继承 PyTorch 的 `Dataset` 规则，所以 PyTorch 会把它当作标准数据集使用。

## 对 def 的理解

`def` 用来定义函数。

如果 `def` 写在 `class` 下面，它就是这个类自己的方法。

例如：

```python
def __len__(self):
```

这表示这个数据集自己有一个方法，可以告诉别人它有多少条数据。

## 对 __init__ 的理解

`__init__` 是一个特殊方法。

创建对象时，它会自动执行。

在这次代码里，`__init__` 用来准备 `self.x` 和 `self.y`。

## 对 self 的理解

`self` 表示“这个对象自己”。

例如：

```python
self.x
self.y
```
