import torch
from torch.utils.data import Dataset, DataLoader


# class 用来定义一种“东西”。
# 这里我们定义一种自己的数据集，名字叫 SimpleRegressionDataset。
# 括号里的 Dataset 表示：它继承 PyTorch 的 Dataset 规则。
class SimpleRegressionDataset(Dataset):
    # __init__ 会在创建数据集对象时自动执行。
    # self 表示“这个数据集对象自己”。
    def __init__(self):
        # self.x 保存输入数据。
        # 这里有 8 条数据，每条数据只有 1 个特征。
        self.x = torch.tensor([
            [1.0],
            [2.0],
            [3.0],
            [4.0],
            [5.0],
            [6.0],
            [7.0],
            [8.0],
        ])

        # self.y 保存标签。
        # 这里人为设置规律：y = 2x + 1。
        self.y = 2 * self.x + 1

    # __len__ 用来告诉 PyTorch：这个数据集一共有多少条数据。
    def __len__(self):
        return len(self.x)

    # __getitem__ 用来告诉 PyTorch：给我一个编号 index，
    # 我应该怎么取出这一条数据。
    def __getitem__(self, index):
        return self.x[index], self.y[index]


# 创建一个数据集对象。
# SimpleRegressionDataset() 后面的括号表示：调用这个类，创建对象。
dataset = SimpleRegressionDataset()

print("数据集长度:", len(dataset))

# 手动取出第 1 条样本。
# Python 的编号从 0 开始，所以 dataset[0] 表示第 1 条。
first_x, first_y = dataset[0]
print("第 1 条样本 x:", first_x)
print("第 1 条样本 y:", first_y)


# DataLoader 负责批量读取数据。
# batch_size=2 表示每次取 2 条数据。
# shuffle=True 表示读取前先打乱顺序。
loader = DataLoader(dataset, batch_size=2, shuffle=True)

print("\n按 batch 读取数据:")

# enumerate 会给每个 batch 编号。
# start=1 表示编号从 1 开始。
for batch_index, (batch_x, batch_y) in enumerate(loader, start=1):
    print(f"batch {batch_index}")
    print("batch_x:", batch_x)
    print("batch_y:", batch_y)
