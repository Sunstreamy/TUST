import numpy as np

def fit_power(x, y, n):
    """
    使用最小二乘法拟合幂函数模型 y = a * x^n，其中 n 给定
    参数:
        x : 自变量（数组形式）
        y : 因变量（数组形式）
        n : 幂指数，已知常数
    返回:
        a : 拟合得到的系数
    """
    x = np.array(x)
    y = np.array(y)
    # 构造设计矩阵 A，每一行对应 x[i]^n
    A = (x**n).reshape(-1, 1)
    # 法一同理  使用内置的 least squares 求解最优 a
    a = np.linalg.lstsq(A, y, rcond=None)[0][0]
    return a

if __name__ == '__main__':
    # 示例数据
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([1.2, 3.5, 7.8, 14.1, 23.9])
    n = 2  # 例如这里取 n = 2
    a = fit_power(x, y, n)
    print(f"拟合的系数: a = {a}")