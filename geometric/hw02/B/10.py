import numpy as np
import matplotlib.pyplot as plt

# 设置图形的全局字体为SimHei（黑体），支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 原始数据
length = np.array([12.5, 12.625, 14.125, 14.5, 17.25, 17.75])
weight = np.array([17, 16.5, 23, 26.5, 41, 49])

# 绘制原始数据的散点图
plt.figure(figsize=(12, 4))

# 子图1：原始数据散点图
plt.subplot(131)
plt.scatter(length, weight, color='blue')
plt.xlabel('身长（英寸）')
plt.ylabel('重量（盎司）')
plt.title('原始数据散点图')
plt.grid(True)

# 尝试对数变换
log_length = np.log(length)
log_weight = np.log(weight)

# 子图2：对数变换后的散点图
plt.subplot(132)
plt.scatter(log_length, log_weight, color='red')
plt.xlabel('ln(身长)')
plt.ylabel('ln(重量)')
plt.title('对数变换后的散点图')
plt.grid(True)

# 对对数变换后的数据进行线性回归
A = np.vstack([log_length, np.ones(len(log_length))]).T
a, b = np.linalg.lstsq(A, log_weight, rcond=None)[0]

# 绘制拟合线
x_fit = np.linspace(np.min(log_length), np.max(log_length), 100)
y_fit = a * x_fit + b
plt.plot(x_fit, y_fit, 'g--', label=f'拟合线: ln(w) = {a:.4f}ln(l) + {b:.4f}')
plt.legend()

# 子图3：原始数据和拟合曲线
plt.subplot(133)
plt.scatter(length, weight, color='blue')
x_original = np.linspace(np.min(length), np.max(length), 100)
y_original = np.exp(b) * x_original**a
plt.plot(x_original, y_original, 'r--', 
         label=f'拟合曲线: w = {np.exp(b):.4f}l^{a:.4f}')
plt.xlabel('身长（英寸）')
plt.ylabel('重量（盎司）')
plt.title('原始数据和拟合曲线')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig('2.png', dpi=300, bbox_inches='tight')

# 预测身长为19.5英寸的鱼的重量
predict_length = 19.5
predict_weight = np.exp(b) * predict_length**a

print(f"\n模型: w = {np.exp(b):.4f}l^{a:.4f}")
print(f"当身长为{predict_length}英寸时，预测重量为{predict_weight:.2f}盎司")

# 计算R方值来评估模型拟合优度
y_pred = np.exp(b) * length**a
ss_tot = np.sum((weight - np.mean(weight))**2)
ss_res = np.sum((weight - y_pred)**2)
r_squared = 1 - (ss_res / ss_tot)
print(f"模型的R²值为: {r_squared:.4f}")
print("\n图像已保存为 '2.png'")