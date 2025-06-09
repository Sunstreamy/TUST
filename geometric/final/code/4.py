#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
最佳仓库位置问题求解

问题描述：
某连锁企业在某地区有6个销售点，已知该地区的交通网络如图所示，
其中点(v1,v2,v3,v4,v5,v6)代表销售点，边代表公路，连线上数字为销售点间的公路距离，
问仓库应该建在哪个小区，可使离仓库最远的销售点到仓库的路程最近？

解题思路：
这是一个经典的"最小化最大距离"问题，也称为"minimax问题"。我们需要：
1. 构建交通网络的图模型
2. 计算每个销售点作为仓库位置时，到其他所有销售点的最短路径
3. 找出每个位置的"最远距离"（即到最远销售点的距离）
4. 选择"最远距离"最小的位置作为最佳仓库位置
"""

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 使用SimHei字体
plt.rcParams["axes.unicode_minus"] = False


def create_graph():
    """
    创建表示交通网络的图

    在这一步中，我们将题目中描述的交通网络转化为图论模型。
    每个销售点作为图的一个节点，公路作为边，距离作为边的权重。

    返回:
    G - NetworkX图对象，表示交通网络
    """
    # 创建无向图
    G = nx.Graph()

    # 添加节点（销售点）
    for i in range(1, 7):
        G.add_node(f"v{i}", label=f"销售点{i}")

    # 添加边（公路）及其权重（距离）
    edges_with_weights = [
        ("v1", "v2", 20),
        ("v1", "v5", 15),
        ("v2", "v3", 20),
        ("v2", "v5", 25),
        ("v2", "v4", 60),
        ("v3", "v4", 30),
        ("v3", "v5", 18),
        ("v5", "v6", 15),
    ]

    G.add_weighted_edges_from(edges_with_weights)

    return G


def find_best_warehouse_location(G):
    """
    寻找最佳仓库位置

    这是算法的核心部分。对于每个可能的仓库位置（即每个销售点），
    我们计算从该位置到所有其他销售点的最短路径。然后找出最远的销售点距离。
    最终，我们选择"最远距离"最小的位置作为最佳仓库位置。

    这种方法被称为"minimax"策略，即最小化最大距离。

    参数:
    G - NetworkX图对象，表示交通网络

    返回:
    best_location - 最佳仓库位置
    min_max_distance - 最远销售点到仓库的最短距离
    all_distances - 从每个点作为仓库时，到各销售点的距离
    """
    # 存储每个可能仓库位置的最远距离
    max_distances = {}
    all_distances = {}

    # 对每个可能的仓库位置（即每个销售点）
    for warehouse in G.nodes():
        # 计算该位置到所有其他销售点的最短路径
        # 这里使用Dijkstra算法，适用于带正权重的图
        shortest_paths = nx.single_source_dijkstra_path_length(G, warehouse)
        all_distances[warehouse] = shortest_paths

        # 找出最远的销售点距离
        max_distance = max(shortest_paths.values())
        max_distances[warehouse] = max_distance

    # 找出使最远距离最小的仓库位置
    best_location = min(max_distances, key=max_distances.get)
    min_max_distance = max_distances[best_location]

    return best_location, min_max_distance, all_distances


def visualize_graph(G, best_location=None):
    """
    可视化交通网络图

    通过可视化，我们可以直观地看到交通网络的结构和最佳仓库位置。

    参数:
    G - NetworkX图对象
    best_location - 最佳仓库位置（如果已计算）
    """
    plt.figure(figsize=(10, 8))

    # 设置节点位置
    pos = {
        "v1": (0, 0),
        "v2": (1, 1),
        "v3": (2, 0),
        "v4": (3, -1),
        "v5": (1, -1),
        "v6": (2, -2),
    }

    # 绘制节点
    node_colors = ["skyblue" if node != best_location else "red" for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)

    # 绘制边
    nx.draw_networkx_edges(G, pos)

    # 添加边权重标签
    edge_labels = {(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # 添加节点标签
    nx.draw_networkx_labels(G, pos)

    plt.axis("off")
    plt.tight_layout()
    plt.savefig("../figures/4.png", dpi=300)
    plt.show()


def print_results(best_location, min_max_distance, all_distances):
    """
    打印结果

    详细展示每个销售点作为仓库位置的情况，以及最终的最佳选择。
    这有助于我们理解算法的决策过程。

    参数:
    best_location - 最佳仓库位置
    min_max_distance - 最远销售点到仓库的最短距离
    all_distances - 从每个点作为仓库时，到各销售点的距离
    """
    print("\n" + "=" * 50)
    print("最佳仓库位置问题求解")
    print("=" * 50)

    print("\n每个销售点作为仓库位置时，到其他销售点的距离:")
    for warehouse, distances in all_distances.items():
        print(f"\n当仓库位于 {warehouse} 时:")
        for dest, dist in distances.items():
            print(f"  到 {dest} 的距离: {dist}")
        print(f"  最远距离: {max(distances.values())}")

    print("\n" + "-" * 50)
    print(f"最佳仓库位置: {best_location}")
    print(f"此时离仓库最远的销售点距离为: {min_max_distance}")
    print("=" * 50)


def main():
    """
    主函数

    按照明确的步骤解决问题，使得解题过程清晰可追踪。
    """
    # 第一步：创建表示交通网络的图
    print("第一步：创建交通网络图...")
    G = create_graph()

    # 第二步：寻找最佳仓库位置
    print("第二步：计算每个销售点作为仓库位置的情况...")
    best_location, min_max_distance, all_distances = find_best_warehouse_location(G)

    # 第三步：打印结果
    print("第三步：分析结果...")
    print_results(best_location, min_max_distance, all_distances)

    # 第四步：可视化结果
    print("第四步：生成可视化图表...")
    visualize_graph(G, best_location)

    # 总结
    print("\n结论分析：")
    print(f"1. 经过计算，最佳仓库位置是在销售点 {best_location}。")
    print(f"2. 此时，离仓库最远的销售点距离为 {min_max_distance}。")
    print("3. 这是所有可能选择中，最远距离最小的方案。")
    print("4. 该方案保证了最差情况下的路程最短，符合'最小化最大距离'的优化目标。")


if __name__ == "__main__":
    main()
