#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
猎犬追兔子问题求解
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation
import os

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 使用SimHei字体
plt.rcParams["axes.unicode_minus"] = False


def dog_rabbit_model(state, t, v_rabbit=10):
    """
    猎犬追兔子的微分方程模型

    参数:
    state - 状态向量 [猎犬x坐标, 猎犬y坐标]
    t - 时间点
    v_rabbit - 兔子的速度，默认10m/s

    返回:
    猎犬位置的导数 [dx/dt, dy/dt]
    """
    # 猎犬当前位置
    x_dog, y_dog = state

    # 计算兔子当前位置 (初始在(100,0)，以速度v向(100,100)移动)
    # 兔子y坐标随时间线性增加
    y_rabbit = min(v_rabbit * t, 100)  # 不超过洞穴位置
    x_rabbit = 100  # 兔子x坐标固定

    # 计算猎犬到兔子的方向向量
    dx = x_rabbit - x_dog
    dy = y_rabbit - y_dog
    distance = np.sqrt(dx**2 + dy**2)

    # 如果距离为0，则已经追上
    if distance <= 0.0:
        return [0, 0]

    # 猎犬的速度是兔子的2倍
    v_dog = 2 * v_rabbit

    # 计算猎犬的速度分量
    dx_dt = v_dog * dx / distance
    dy_dt = v_dog * dy / distance

    return [dx_dt, dy_dt]


def solve_hunting_problem(v_rabbit=10.0, t_max=15.0):
    """
    求解猎犬追兔子问题

    参数:
    v_rabbit - 兔子的速度，默认10m/s
    t_max - 最大模拟时间，默认15秒

    返回:
    t - 时间点
    solution - 猎犬位置随时间变化
    rabbit_positions - 兔子位置随时间变化
    catch_time - 追上兔子的时间
    catch_position - 追上兔子的位置
    """
    # 初始条件: 猎犬在原点(0,0)
    initial_state = [0, 0]

    # 时间点
    t = np.linspace(0, t_max, 1000)

    # 求解微分方程
    solution = odeint(dog_rabbit_model, initial_state, t, args=(v_rabbit,))

    # 计算每个时间点兔子的位置
    rabbit_positions = np.zeros((len(t), 2))
    rabbit_positions[:, 0] = 100  # x坐标固定为100
    rabbit_positions[:, 1] = np.minimum(v_rabbit * t, 100)  # y坐标随时间变化，不超过100

    # 确定追上兔子的时间和位置
    distances = np.sqrt(np.sum((solution - rabbit_positions) ** 2, axis=1))
    catch_index = np.argmin(distances)

    # 如果最小距离仍然较大，则可能没有在模拟时间内追上
    if distances[catch_index] > 0.5:
        # 尝试更精确地计算追上时间
        for i in range(len(t) - 1):
            if distances[i + 1] < 0.5:
                catch_index = i + 1
                break

    catch_time = t[catch_index]
    catch_position = solution[catch_index]

    return t, solution, rabbit_positions, catch_time, catch_position


def plot_trajectories(t, dog_positions, rabbit_positions, catch_time, catch_position):
    """绘制猎犬和兔子的运动轨迹"""
    plt.figure(figsize=(10, 8))

    # 找到追上时刻的索引
    catch_index = np.argmin(np.abs(t - catch_time))

    # 只绘制追上之前的轨迹
    # 绘制猎犬轨迹
    plt.plot(
        dog_positions[: catch_index + 1, 0],
        dog_positions[: catch_index + 1, 1],
        color="navy",
        linestyle="-",
        linewidth=2,
        label="猎犬轨迹",
    )

    # 绘制兔子轨迹
    plt.plot(
        rabbit_positions[: catch_index + 1, 0],
        rabbit_positions[: catch_index + 1, 1],
        "r-",
        linewidth=2,
        label="兔子轨迹",
    )

    # 标记起始位置
    plt.plot(0, 0, "bo", markersize=10, label="猎犬起点")
    plt.plot(100, 0, "ro", markersize=10, label="兔子起点")
    plt.plot(100, 100, "go", markersize=10, label="兔子洞穴")

    # 标记追上位置
    plt.plot(
        catch_position[0],
        catch_position[1],
        "mo",
        markersize=10,
        label=f"追上位置 ({catch_position[0]:.2f}, {catch_position[1]:.2f})",
    )

    # 设置图形属性
    plt.grid(True)
    plt.xlabel("x坐标 (米)")
    plt.ylabel("y坐标 (米)")
    plt.legend(loc="best")
    plt.axis("equal")

    # 保存图形到当前文件所在目录
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 确保figures目录存在
    figures_dir = os.path.join(os.path.dirname(current_dir), "figures")
    os.makedirs(figures_dir, exist_ok=True)
    output_path = os.path.join(figures_dir, "2.png")
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"图像已保存到: {output_path}")


if __name__ == "__main__":
    # 第一问：当v=10m/s时的特定情况
    v_rabbit = 10.0  # 兔子速度10m/s
    t, dog_positions, rabbit_positions, catch_time, catch_position = (
        solve_hunting_problem(v_rabbit)
    )

    # 输出结果
    print("\n第一问：v = 10 m/s 的特定情况")
    print(f"兔子速度: {v_rabbit} m/s")
    print(f"猎犬速度: {2*v_rabbit} m/s")
    print(f"追上兔子的时间: {catch_time:.4f} 秒")
    print(f"追上兔子的位置: ({catch_position[0]:.4f}, {catch_position[1]:.4f}) 米")

    # 绘制轨迹图
    plot_trajectories(t, dog_positions, rabbit_positions, catch_time, catch_position)

    # 第二问：一般情况下的分析
    print("\n第二问：一般情况下的分析")
    print("对于任意速度v，我们可以通过数学分析得到：")

    # 计算一般情况下的追及时间和位置
    # 对于任意v，追及时间为t = 2/3 * 100/v
    # 追及位置为(100, 2/3 * 100)
    general_time = 2 / 3 * (100 / 1)  # 用v=1表示一般情况
    general_position_x = 100
    general_position_y = 2 / 3 * 100

    print(f"追上兔子的时间: t = (2/3) * (100/v) = 200/(3v) 秒")
    print(f"当v = 10 m/s时，t = {general_time/10:.4f} 秒")
    print(f"追上兔子的位置: (100, (2/3) * 100) = (100, 66.6667) 米")
    print("注意：追上位置与兔子速度v无关")

    # 验证不同v值的情况
    print("\n验证不同v值的情况：")
    for v in [5, 10, 15, 20]:
        t, _, _, catch_time, catch_position = solve_hunting_problem(v)
        print(
            f"v = {v} m/s: 时间 = {catch_time:.4f} 秒, 位置 = ({catch_position[0]:.4f}, {catch_position[1]:.4f}) 米"
        )
