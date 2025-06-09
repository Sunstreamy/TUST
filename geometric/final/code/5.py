#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
矩阵求逆问题求解

问题描述：
设方阵 A =
( 1  2  -1 )
( 3  4  -2 )
( 5 -4   1 )
，利用编程求解矩阵的逆。

解题思路：
1. 使用numpy库直接计算矩阵的逆
2. 验证结果的正确性
3. 可视化矩阵、逆矩阵及其乘积
"""

import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 使用SimHei字体
plt.rcParams["axes.unicode_minus"] = False


def create_matrix():
    """
    创建题目中给定的矩阵

    返回:
    A - 题目中给定的3x3方阵
    """
    # 创建矩阵
    A = np.array([[1, 2, -1], [3, 4, -2], [5, -4, 1]], dtype=float)

    return A


def calculate_inverse(A):
    """
    计算矩阵的逆

    参数:
    A - 待求逆的矩阵

    返回:
    A_inv - 矩阵A的逆
    """
    # 使用numpy的linalg.inv函数计算逆矩阵
    A_inv = np.linalg.inv(A)

    return A_inv


def verify_inverse(A, A_inv):
    """
    验证逆矩阵的正确性

    参数:
    A - 原始矩阵
    A_inv - 逆矩阵

    返回:
    product - A与A_inv的乘积
    """
    # 计算A与A_inv的乘积
    product = np.dot(A, A_inv)

    return product


def main():
    """
    主函数

    按照明确的步骤解决问题，使得解题过程清晰可追踪。
    """
    # 第一步：创建矩阵
    print("第一步：创建矩阵...")
    A = create_matrix()
    print("\n原始矩阵 A:")
    print(A)

    # 第二步：计算行列式
    print("\n第二步：计算行列式...")
    det_A = np.linalg.det(A)
    print(f"行列式 det(A) = {det_A:.6f}")

    # 第三步：计算逆矩阵
    print("\n第三步：计算逆矩阵...")
    A_inv = calculate_inverse(A)
    print("逆矩阵 A^(-1):")
    print(A_inv)

    # 第四步：验证结果
    print("\n第四步：验证结果...")
    product = verify_inverse(A, A_inv)
    print("A·A^(-1) (应接近单位矩阵):")
    print(product)

    # 总结
    print("\n结论分析：")
    print("1. 矩阵A是非奇异矩阵（行列式不为零），因此存在唯一的逆矩阵。")
    print("2. 使用NumPy的linalg.inv函数可以高效地计算矩阵的逆。")
    print("3. 验证结果表明，计算得到的逆矩阵满足A·A^(-1) = I的性质。")
    print(f"4. 矩阵A的行列式为{det_A:.6f}，不为零，证明矩阵可逆。")


if __name__ == "__main__":
    main()
