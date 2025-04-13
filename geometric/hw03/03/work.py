import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 使用SimHei字体
plt.rcParams["axes.unicode_minus"] = False


def f(x):
    """目标函数 f(x) = x² + 2x"""
    return x**2 + 2 * x


def binary_search_min(a, b, epsilon, t):
    """
    使用二分法寻找函数f(x)在区间[a,b]上的最小值点

    参数:
    a, b: 搜索区间的端点
    epsilon: 函数值的误差限
    t: 自变量的误差限

    返回:
    x_min: 最小值点的近似值
    f_min: 对应的函数值
    iterations: 迭代次数
    """
    iterations = 0
    points = []  # 存储每次迭代的点

    while (b - a) > t:
        iterations += 1
        mid = (a + b) / 2
        x1 = mid - epsilon
        x2 = mid + epsilon
        f1 = f(x1)
        f2 = f(x2)

        points.append((mid, f(mid)))

        if f1 < f2:
            b = x2
        else:
            a = x1

    x_min = (a + b) / 2
    f_min = f(x_min)

    return x_min, f_min, iterations, points


# 题目给定参数
a = -3  # 区间下界
b = 6  # 区间上界
epsilon = 0.01  # 函数值误差限
t = 0.2  # 自变量误差限

# 执行二分法求解
x_min, f_min, iterations, points = binary_search_min(a, b, epsilon, t)

# 输出结果
print(f"使用二分法求解最小值问题:")
print(f"函数 f(x) = x^2 + 2x, 区间 [-3, 6]")
print(f"误差限: t = {t}, ε = {epsilon}")
print(f"最小值点的近似值: x ≈ {x_min:.6f}")
print(f"对应的函数值: f(x) ≈ {f_min:.6f}")
print(f"迭代次数: {iterations}")

# 绘制函数图像和迭代过程
x = np.linspace(a, b, 1000)
y = [f(xi) for xi in x]

plt.figure(figsize=(10, 6))
plt.plot(x, y, "b-", label="f(x) = x^2 + 2x")
plt.scatter(
    [p[0] for p in points],
    [p[1] for p in points],
    color="red",
    marker="o",
    label="迭代点",
)
plt.scatter(x_min, f_min, color="green", marker="*", s=200, label="最小值点")
plt.grid(True)
plt.axhline(y=0, color="k", linestyle="-", alpha=0.3)
plt.axvline(x=0, color="k", linestyle="-", alpha=0.3)
plt.title("二分法求解函数最小值")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
# 修改保存路径到指定位置
plt.savefig("/home/sunstreamy/code/TUST/geometric/hw03/03/binary_search_min.png")
plt.show()

# 理论上的最小值点（用于比较）
x_true = -1
f_true = f(x_true)
print(f"理论最小值点: x = {x_true}")
print(f"理论最小值: f(x) = {f_true}")
print(f"误差: |x - x_true| = {abs(x_min - x_true):.6f}")
