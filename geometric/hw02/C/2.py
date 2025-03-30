import numpy as np
from prettytable import PrettyTable

def create_difference_table(x, y):
    """构造均差表
    参数:
        x: x值列表
        y: y值列表
    返回:
        table: 格式化的均差表
    """
    n = len(x)
    table = PrettyTable()
    table.field_names = ["x", "y", "一阶差分"]
    
    differences = []
    for i in range(n-1):
        diff = y[i+1] - y[i]
        differences.append(diff)
    
    # 填充表格数据
    for i in range(n):
        row = [x[i], y[i]]
        if i < n-1:
            row.append(differences[i])
        else:
            row.append("-")
        table.add_row(row)
    
    return table

def fit_linear(x, y):
    """使用最小二乘法拟合一次多项式 y = ax + b
    参数:
        x: 自变量数组
        y: 因变量数组
    返回:
        a, b: 拟合系数
    """
    x = np.array(x)
    y = np.array(y)
    A = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(A, y, rcond=None)[0]
    return a, b

def main():
    # 给定数据
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    y = np.array([23, 48, 73, 98, 123, 148, 173, 198])
    
    # 构造并打印均差表
    table = create_difference_table(x, y)
    print("均差表:")
    print(table)
    print("\n从均差表可以看出，一阶差分基本相等，说明数据呈线性关系，可以使用一次多项式拟合")
    
    # 拟合一次多项式
    a, b = fit_linear(x, y)
    print(f"\n拟合结果: y = {a:.2f}x + {b:.2f}")
    
    # 预测x=8时的y值
    x_pred = 8
    y_pred = a * x_pred + b
    print(f"\n当x = {x_pred}时，预测的y值为: {y_pred:.2f}")

if __name__ == "__main__":
    main()