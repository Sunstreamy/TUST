import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# 设置字体支持中文
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 使用SimHei字体
plt.rcParams["axes.unicode_minus"] = False

# 解题步骤说明
"""
1. 最大化问题：Max (x + y)
   约束条件：
   - x + y ≤ 6
   - 3x - y ≤ 9
   - x, y ≥ 0

2. 解题步骤：
   1) 绘制约束条件的边界：
      - x + y = 6 (直线1)
      - 3x - y = 9 (直线2)
      - x = 0 (y轴)
      - y = 0 (x轴)
   
   2) 确定可行域：
      - 这四条直线围成的区域
   
   3) 引入目标函数等值线 x + y = c，绘制目标函数的最优值等值线
   
   4) 找到可行域中的最优解
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
# x + y = 6 和 x = 0 的交点
p1 = (0, 6)
# x + y = 6 和 y = 0 的交点
p2 = (6, 0)
# 3x - y = 9 和 y = 0 的交点
p3 = (3, 0)
# x + y = 6 和 3x - y = 9 的交点
# 解方程组：x + y = 6, 3x - y = 9
# 4x = 15, x = 3.75, y = 2.25
p4 = (3.75, 2.25)

# 标注交点坐标
plt.plot(p1[0], p1[1], "ro")
plt.plot(p2[0], p2[1], "ro")
plt.plot(p3[0], p3[1], "ro")
plt.plot(p4[0], p4[1], "ro")

plt.text(p1[0], p1[1] + 0.2, f"({p1[0]}, {p1[1]})", fontsize=10)
plt.text(p2[0], p2[1] + 0.2, f"({p2[0]}, {p2[1]})", fontsize=10)
plt.text(p3[0], p3[1] + 0.2, f"({p3[0]}, {p3[1]})", fontsize=10)
plt.text(p4[0], p4[1] + 0.2, f"({p4[0]:.2f}, {p4[1]:.2f})", fontsize=10)

# 标注可行域（只在可行区域绘制颜色）
points = [(0, 0), (0, 6), (3.75, 2.25), (3, 0)]
poly = Polygon(points, alpha=0.3, color="skyblue")
ax.add_patch(poly)

# 仅绘制最优目标函数等值线（一条虚线）
max_value = p4[0] + p4[1]  # 6
y_obj = max_value - x
plt.plot(x, y_obj, "r--", alpha=0.7, linewidth=1.5, label=f"x + y = {max_value}")

# 标出最优解
max_point = p4  # (3.75, 2.25)
plt.plot(max_point[0], max_point[1], "ro", markersize=8)
plt.text(
    max_point[0] - 1.5,
    max_point[1] + 0.5,
    f"最优解: ({max_point[0]:.2f}, {max_point[1]:.2f})",
    color="red",
    fontsize=12,
)
plt.text(
    max_point[0] - 1.5,
    max_point[1] + 0.1,
    f"目标函数值: {max_value:.2f}",
    color="red",
    fontsize=12,
)

# 添加图例和标题
plt.legend(loc="upper right")
plt.title("Max(x + y)的图解法（几何解法）", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)

# 保存图像
plt.savefig("max_problem.png", dpi=300, bbox_inches="tight")
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
   这些约束条件形成的交集是凸多边形，顶点为(0,0), (0,6), (3,0), (3.75,2.25)

3. 通过分析可知，最优解位于顶点(3.75, 2.25)和（0,6）之间的直线上，此时目标函数的最大值为3.75+2.25=6

3. 因此，Max(x+y)=6，在可行区直线上一点(3.75, 2.25)处可取得
"""
