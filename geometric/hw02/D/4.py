import numpy as np

def natural_cubic_spline(x, y):
    """
    计算自然三次样条插值的系数
    参数:
        x: x坐标点列表
        y: y坐标点列表
    返回:
        coefficients: 每段样条的系数 [a, b, c, d]
        其中每段样条函数形式为: f(x) = a(x-xi)^3 + b(x-xi)^2 + c(x-xi) + d
    """
    n = len(x) - 1  # 区间数
    h = [x[i+1] - x[i] for i in range(n)]  # 计算每个子区间的长度
    
    # 构建方程组的系数矩阵A和右端向量b
    A = np.zeros((n+1, n+1))
    b = np.zeros(n+1)
    
    # 设置第一个和最后一个方程（自然边界条件：两端二阶导数为0）
    A[0, 0] = 2
    A[0, 1] = 1
    A[-1, -2] = 1
    A[-1, -1] = 2
    
    # 设置中间方程
    for i in range(1, n):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        
        b[i] = 3 * ((y[i+1] - y[i]) / h[i] - (y[i] - y[i-1]) / h[i-1])
    
    # 求解方程组得到二阶导数
    M = np.linalg.solve(A, b)
    
    # 计算每段样条的系数
    coefficients = []
    for i in range(n):
        a = (M[i+1] - M[i]) / (6 * h[i])
        b = M[i] / 2
        c = (y[i+1] - y[i]) / h[i] - h[i] * (M[i+1] + 2 * M[i]) / 6
        d = y[i]
        coefficients.append([a, b, c, d])
    
    return coefficients

def print_spline_equations(x, coefficients):
    """
    打印样条方程
    """
    for i, coef in enumerate(coefficients):
        a, b, c, d = coef
        print(f"区间 [{x[i]}, {x[i+1]}] 的样条方程:")
        print(f"f(x) = {a:.6f}(x-{x[i]})^3 + {b:.6f}(x-{x[i]})^2 + {c:.6f}(x-{x[i]}) + {d:.6f}")

if __name__ == "__main__":
    # 给定的数据点
    x = np.array([3, 4, 6])
    y = np.array([10, 15, 35])
    
    # 计算样条系数
    coefficients = natural_cubic_spline(x, y)
    
    # 打印样条方程
    print("自然三次样条方程:")
    print_spline_equations(x, coefficients)