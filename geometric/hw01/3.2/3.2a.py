import numpy as np

#题目不要求求解 可以删除
from scipy.optimize import linprog

# 数据点 (a) 数据集
x = np.array([1.0, 2.3, 3.7, 4.2, 6.1, 7.0])
y = np.array([3.6, 3.0, 3.2, 5.1, 5.3, 6.8])
n = len(x)

# 变量顺序为 [a, b, t]，其中 t 为最大绝对偏差
# 目标是最小化 t
c = np.array([0, 0, 1])

# 对于每个数据点有两个约束： 
# 1) a*x_i + b - y_i <= t
# 2) -a*x_i - b + y_i <= t
# 将不等式整理为 A_ub * [a, b, t] <= b_ub

A1 = np.column_stack((x, np.ones(n), -np.ones(n)))  # a*x+b-t <= y  --> (系数乘变量) <= y
b1 = y

A2 = np.column_stack((-x, -np.ones(n), -np.ones(n)))  # -a*x-b-t <= -y --> (系数乘变量) <= -y
b2 = -y

A_ub = np.vstack([A1, A2])
b_ub = np.concatenate([b1, b2])

# 定义变量边界：a, b 无界，t >= 0
bounds = [(None, None), (None, None), (0, None)]

# 使用 linprog 求解，该方法直接支持无界变量
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

if result.success:
    a, b, t = result.x
    print("最优解：")
    print("a =", a)
    print("b =", b)
    print("最大偏差 t =", t)
else:
    print("求解失败:", result.message)