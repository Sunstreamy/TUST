import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
"""
生成大量随机数，设置固定的种子值可以确保每次运行程序时生成相同的随机数序列。这样做的好处是：1) 便于调试程序，因为每次运行的结果都是一样的 2) 便于复现实验结果 3) 在开发过程中可以更容易地发现和修复问题
"""

# 设置图形的全局字体为SimHei（黑体），支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def calculate_area_under_curve(num_points):
    """
    使用蒙特卡洛方法计算曲线f(x)=√x (1/2≤x≤3/2)下的面积
    
    原理：在矩形区域(1/2≤x≤3/2, 0≤y≤√(3/2))内随机生成点，
         计算落在曲线f(x)=√x下方的点的比例，
         然后乘以矩形面积得到曲线下的面积
    
    参数：
        num_points: 随机点的数量
        
    返回：
        area_approx: 曲线下面积的近似值
        points_inside: 落在曲线下方的点
        points_outside: 落在曲线上方的点
    """
    # 定义区域边界
    x_min, x_max = 0.5, 1.5  # x的范围：1/2 到 3/2
    y_max = np.sqrt(x_max)   # y的最大值：√(3/2)
    
    # 在矩形区域内生成随机点
    x = np.random.uniform(x_min, x_max, num_points)
    y = np.random.uniform(0, y_max, num_points)
    
    # 计算曲线上对应的y值：f(x) = √x
    curve_y = np.sqrt(x)
    
    # 判断点是否在曲线下方
    is_below_curve = y <= curve_y
    
    # 计算在曲线下方的点的数量
    num_below = np.sum(is_below_curve)
    
    # 计算矩形的面积
    rectangle_area = (x_max - x_min) * y_max
    
    # 计算曲线下的面积：(曲线下点数/总点数) * 矩形面积
    area_approx = (num_below / num_points) * rectangle_area
    
    # 分离曲线下和曲线上的点（用于可视化）
    points_below = (x[is_below_curve], y[is_below_curve])
    points_above = (x[~is_below_curve], y[~is_below_curve])
    
    return area_approx, points_below, points_above


def plot_curve_area_simulation(points_below, points_above, area_approx, num_points):
    """
    可视化曲线下面积计算的蒙特卡洛模拟
    
    参数：
        points_below: 落在曲线下方的点
        points_above: 落在曲线上方的点
        area_approx: 计算得到的面积近似值
        num_points: 使用的随机点数量
    """
    plt.figure(figsize=(10, 6))
    
    # 绘制曲线f(x) = √x
    x_curve = np.linspace(0.5, 1.5, 100)
    y_curve = np.sqrt(x_curve)
    plt.plot(x_curve, y_curve, 'r-', linewidth=2, label='f(x) = √x')
    
    # 绘制随机点
    plt.scatter(points_below[0], points_below[1], c='green', s=1, alpha=0.5, label='曲线下点')
    plt.scatter(points_above[0], points_above[1], c='red', s=1, alpha=0.5, label='曲线上点')
    
    # 设置图形属性
    plt.title(f'蒙特卡洛方法计算曲线f(x)=√x (1/2≤x≤3/2)下的面积\n点数：{num_points}, 面积 ≈ {area_approx:.6f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    
    # 计算理论面积：∫(√x)dx从1/2到3/2 = [2/3 * x^(3/2)]从1/2到3/2
    theoretical_area = (2/3) * (1.5**(3/2) - 0.5**(3/2))
    
    # 显示理论值与近似值的比较
    plt.figtext(0.5, 0.01, 
               f'理论值：面积 = {theoretical_area:.6f}\n近似值：面积 ≈ {area_approx:.6f}\n相对误差：{abs(area_approx-theoretical_area)/theoretical_area*100:.4f}%',
               ha='center', bbox={'facecolor':'yellow', 'alpha':0.5, 'pad':5})
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig('1_4.png', dpi=300)


def main():
    """
    主函数：运行蒙特卡洛模拟并显示结果
    """
    # 设置随机点的数量
    num_points = 100000
    
    print("\n===== 蒙特卡洛方法计算曲线下面积 =====")
    area_approx, points_below, points_above = calculate_area_under_curve(num_points)
    theoretical_area = (2/3) * (1.5**(3/2) - 0.5**(3/2))
    print(f"使用 {num_points} 个随机点")
    print(f"面积的近似值：{area_approx:.10f}")
    print(f"面积的理论值：{theoretical_area:.10f}")
    print(f"相对误差：{abs(area_approx-theoretical_area)/theoretical_area*100:.8f}%")
    
    # 可视化曲线下面积计算
    plot_curve_area_simulation(points_below, points_above, area_approx, num_points)
    print("\n图像已保存为 '1_4.png'")


# 如果直接运行此脚本，则执行主函数
if __name__ == "__main__":
    main()