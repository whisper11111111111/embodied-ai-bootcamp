import torch

print("PyTorch 版本:", torch.__version__)

# 1. 创建张量
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

print("a:", a)
print("b:", b)

# 2. 张量加法
c = a + b
print("a + b:", c)

# 3. 查看 shape 和 dtype
print("a 的形状:", a.shape)
print("a 的数据类型:", a.dtype)

# 4. 创建矩阵
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
y = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

print("x:", x)
print("y:", y)

# 5. 矩阵乘法
z = x @ y
print("x @ y:", z)

# 6. 检查 GPU
print("CUDA 是否可用:", torch.cuda.is_available())

if torch.cuda.is_available():
    device = torch.device("cuda")
    x_gpu = x.to(device)
    y_gpu = y.to(device)
    z_gpu = x_gpu @ y_gpu
    print("GPU 上的计算结果:", z_gpu)
else:
    print("当前没有可用 GPU，使用 CPU 完成练习。")