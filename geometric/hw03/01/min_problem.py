import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# 设置字体支持中文
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 使用SimHei字体
plt.rcParams["axes.unicode_minus"] = False


# 解题步骤说明
"""
1. 最小化问题：Min (x + y)
   约束条件：
   - x + y ≥ 6
   - 3x - y ≥ 9
   - x, y ≥ 0

2. 解题步骤：
   1) 绘制约束条件的边界：
      - x + y = 6 (直线1)
      - 3x - y = 9 (直线2)
      - x = 0 (y轴)
      - y = 0 (x轴)
   
   2) 确定可行域：
      - 同时满足上述约束条件的区域
   
   3) 找到可行域中使得x+y最小的点
"""

# 创建图形
plt.figure(figsize=(10, 8))
ax = plt.gca()

# 设置坐标轴显示范围
x_min, x_max = 0, 8
y_min, y_max = 0, 8
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# 绘制约束条件边界
x = np.linspace(x_min, x_max, 1000)

# x + y = 6 直线
y1 = 6 - x
plt.plot(x, y1, "b-", label="x + y = 6")

# 3x - y = 9 直线
y2 = 3 * x - 9
plt.plot(x, y2, "g-", label="3x - y = 9")

# x轴和y轴
plt.axhline(y=0, color="k", linestyle="-")
plt.axvline(x=0, color="k", linestyle="-")

# 计算交点
# x + y = 6 和 3x - y = 9 的交点
# 解方程组：x + y = 6, 3x - y = 9
# 4x = 15, x = 3.75, y = 2.25
p1 = (3.75, 2.25)

# x + y = 6 和 y = 0 的交点
p2 = (6, 0)

# 3x - y = 9 与 y = 8 的交点
# 3x - 8 = 9
# 3x = 17
# x = 5.67
p3 = (5.67, 8)

# 标注交点坐标
plt.plot(p1[0], p1[1], "ro")
plt.plot(p2[0], p2[1], "ro")
plt.plot(p3[0], p3[1], "ro")

plt.text(p1[0], p1[1] + 0.2, f"({p1[0]:.2f}, {p1[1]:.2f})", fontsize=10)
plt.text(p2[0], p2[1] + 0.2, f"({p2[0]}, {p2[1]})", fontsize=10)
plt.text(p3[0], p3[1] + 0.2, f"({p3[0]:.2f}, {p3[1]})", fontsize=10)

# 标注可行域（只在可行区域绘制颜色）
# min问题的可行域为同时满足x+y≥6和3x-y≥9的区域（第一象限内）
vertices = [
    (p1[0], p1[1]),  # (3.75, 2.25)
    (p2[0], p2[1]),  # (6, 0)
    (8, 0),  # 右下角点
    (8, 8),  # 右上角点
    (p3[0], p3[1]),  # (5.67, 8)
]
poly = Polygon(vertices, alpha=0.3, color="skyblue")
ax.add_patch(poly)

# 计算目标函数在各个顶点的值
vertices_values = {}
vertices_values[p1] = p1[0] + p1[1]  # (3.75, 2.25) -> 6
vertices_values[p2] = p2[0] + p2[1]  # (6, 0) -> 6
vertices_values[p3] = p3[0] + p3[1]  # (5.67, 8) -> 13.67
vertices_values[(8, 0)] = 8 + 0  # (8, 0) -> 8
vertices_values[(8, 8)] = 8 + 8  # (8, 8) -> 16

# 找出最小值和对应点
min_value = min(vertices_values.values())  # 6
min_points = [point for point, value in vertices_values.items() if value == min_value]

# 两个最小值点，可以选择其中一个
min_point = p1  # 选择(3.75, 2.25)作为最优解点

# 绘制最优目标函数等值线（一条虚线）
y_obj = min_value - x
plt.plot(x, y_obj, "r--", alpha=0.7, linewidth=1.5, label=f"x + y = {min_value}")

# 标出最优解
plt.plot(min_point[0], min_point[1], "ro", markersize=8)
plt.text(
    min_point[0] - 1.5,
    min_point[1] + 0.5,
    f"最优解: ({min_point[0]:.2f}, {min_point[1]:.2f})",
    color="red",
    fontsize=12,
)
plt.text(
    min_point[0] - 1.5,
    min_point[1] + 0.1,
    f"目标函数值: {min_value}",
    color="red",
    fontsize=12,
)


# 添加图例和标题
plt.legend(loc="upper right")
plt.title("Min(x + y)的图解法（几何解法）", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)

# 保存图像
plt.savefig("min_problem.png", dpi=300, bbox_inches="tight")
plt.show()

# 总结解题过程
"""
解题过程总结：

1. 首先绘制约束条件的边界线：
   - x + y = 6
   - 3x - y = 9
   - x = 0 (y轴)
   - y = 0 (x轴)

2. 确定可行区域：
   约束条件 x + y ≥ 6 表示直线 x + y = 6 上方和右侧的区域
   约束条件 3x - y ≥ 9 表示直线 3x - y = 9 上方的区域
   约束条件 x, y ≥ 0 表示第一象限
   这些约束条件的交集形成了可行区域（图中蓝色区域）

3. 通过判断可行域顶点的函数值：
   - 点(3.75, 2.25)：x + y = 3.75 + 2.25 = 6
   - 点(6, 0)：x + y = 6 + 0 = 6
   - 点(8, 0)：x + y = 8 + 0 = 8
   - 点(8, 8)：x + y = 8 + 8 = 16
   - 点(5.67, 8)：x + y = 5.67 + 8 = 13.67
   
   可以确定最小值为6，在点(3.75, 2.25)和(6, 0)之间的直线上均可取得

6. 因此，Min(x+y) = 6，在可行区直线上一点(3.75, 2.25)可取得
"""
