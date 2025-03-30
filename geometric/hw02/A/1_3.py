import numpy as np
import matplotlib.pyplot as plt

# 设置随机数种子，保证结果可重复
np.random.seed(42)

# 设置图形的全局字体为SimHei（黑体），支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def calculate_pi(num_points):
    """
    使用蒙特卡洛方法计算π值
    
    原理：在单位正方形(0≤x≤1, 0≤y≤1)内随机生成点，
         计算落在1/4圆内(x²+y²≤1)的点的比例，
         然后利用公式：π/4 = (1/4圆面积)/(正方形面积)
    
    参数：
        num_points: 随机点的数量
        
    返回：
        pi_approx: π的近似值
        points_inside: 落在1/4圆内的点
        points_outside: 落在1/4圆外的点
    """
    # 在单位正方形内生成随机点
    x = np.random.random(num_points)  # 生成[0,1)之间的随机数
    y = np.random.random(num_points)  # 生成[0,1)之间的随机数
    
    # 计算每个点到原点的距离的平方
    distance_squared = x**2 + y**2
    
    # 判断点是否在1/4圆内（距离≤1）
    is_inside = distance_squared <= 1.0
    
    # 计算在圆内的点的数量
    num_inside = np.sum(is_inside)
    
    # 计算π的近似值：(圆内点数/总点数) * 4
    pi_approx = (num_inside / num_points) * 4
    
    # 分离圆内和圆外的点（用于可视化）
    points_inside = (x[is_inside], y[is_inside])
    points_outside = (x[~is_inside], y[~is_inside])
    
    return pi_approx, points_inside, points_outside


def plot_pi_simulation(points_inside, points_outside, pi_approx, num_points):
    """
    可视化π值计算的蒙特卡洛模拟
    
    参数：
        points_inside: 落在1/4圆内的点
        points_outside: 落在1/4圆外的点
        pi_approx: 计算得到的π近似值
        num_points: 使用的随机点数量
    """
    plt.figure(figsize=(8, 8))
    
    # 绘制1/4圆
    theta = np.linspace(0, np.pi/2, 100)
    x_circle = np.cos(theta)
    y_circle = np.sin(theta)
    plt.plot(x_circle, y_circle, 'r-', linewidth=2)
    
    # 绘制正方形边界
    plt.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], 'b-', linewidth=2)
    
    # 绘制随机点
    plt.scatter(points_inside[0], points_inside[1], c='green', s=1, alpha=0.5, label='圆内点')
    plt.scatter(points_outside[0], points_outside[1], c='red', s=1, alpha=0.5, label='圆外点')
    
    # 设置图形属性
    plt.title(f'蒙特卡洛方法计算π值\n点数：{num_points}, π ≈ {pi_approx:.6f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)
    plt.legend()
    
    # 显示理论值与近似值的比较
    plt.figtext(0.5, 0.01, f'理论值：π = {np.pi:.6f}\n近似值：π ≈ {pi_approx:.6f}\n相对误差：{abs(pi_approx-np.pi)/np.pi*100:.4f}%',
                ha='center', bbox={'facecolor':'yellow', 'alpha':0.5, 'pad':5})
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig('1_3.png', dpi=300)


def main():
    """
    
    主函数：运行蒙特卡洛模拟并显示结果
    """
    # 设置随机点的数量
    num_points = 100000
    
    print("\n===== 蒙特卡洛方法计算π值 =====")
    pi_approx, points_inside, points_outside = calculate_pi(num_points)
    print(f"使用 {num_points} 个随机点")
    print(f"π的近似值：{pi_approx:.10f}")
    print(f"π的理论值：{np.pi:.10f}")
    print(f"相对误差：{abs(pi_approx-np.pi)/np.pi*100:.8f}%")
    
    # 可视化π值计算
    plot_pi_simulation(points_inside, points_outside, pi_approx, num_points)
    print("\n图像已保存为 '1_3.png'")


# 如果直接运行此脚本，则执行主函数
if __name__ == "__main__":
    main()