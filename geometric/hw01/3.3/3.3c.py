# 数据集 (c)
x = [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
y = [4.32, 4.83, 5.27, 5.74, 6.26, 6.79, 7.23]

n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(xi * yi for xi, yi in zip(x, y))
sum_x2 = sum(xi * xi for xi in x)

# 根据最小二乘法公式计算拟合直线系数 a 和 b：
a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
b = (sum_y - a * sum_x) / n

print("拟合直线参数:")
print("a =", a)
print("b =", b)