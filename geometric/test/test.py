import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 定义流量函数
def flow(x1, x2, x3):
    return 2 * x1 + 3 * x2 + 1.5 * x3  # 假设流量和时间的比例系数分别为 2, 3, 1.5


# 设置x1, x2, x3的取值范围
x1_vals = np.linspace(0, 10, 50)  # 绿灯时间范围 0 到 10
x2_vals = np.linspace(0, 10, 50)
x3_vals = np.linspace(0, 10, 50)

# 创建网格
x1, x2 = np.meshgrid(x1_vals, x2_vals)
x3 = 10 - x1 - x2  # 基于总信号灯周期的约束：x1 + x2 + x3 <= 10

# 计算流量
Z = flow(x1, x2, x3)

# 创建三维图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

# 绘制流量函数的表面
ax.plot_surface(x1, x2, Z, cmap="viridis", edgecolor="none", alpha=0.7)

# 绘制约束平面
ax.plot_surface(x1, x2, 10 - x1 - x2, cmap="coolwarm", edgecolor="none", alpha=0.5)

# 设置坐标轴标签
ax.set_xlabel("Green Light Time for A")
ax.set_ylabel("Green Light Time for B")
ax.set_zlabel("Green Light Time for C")
ax.set_title("Traffic Flow Optimization: Maximize Flow")

# 显示图形
plt.show()
