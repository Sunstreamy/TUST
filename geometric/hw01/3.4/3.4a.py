import numpy as np

def fit_quadratic(x, y):
    """
    使用最小二乘法拟合二次模型 y = ax^2 + bx + c
    参数:
        x : 自变量（数组形式）
        y : 因变量（数组形式）
    返回:
        a, b, c : 拟合得到的系数
    """
    #法二 直接求解正规方程  构建误差平方和的函数，分别对参数 a、b 求偏导数并令其为 0
    A = np.vstack([x**2, x, np.ones(len(x))]).T
    ATA = A.T @ A
    ATy = A.T @ y
    a, b, c = np.linalg.solve(ATA, ATy)
    return a, b, c

if __name__ == "__main__":
    # 示例数据
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2.2, 4.8, 9.1, 16.5, 25.3])
    
    # 拟合二次模型
    a, b, c = fit_quadratic(x, y)
    print(f"拟合的二次模型系数: a = {a}, b = {b}, c = {c}")