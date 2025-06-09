#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
向量组极大线性无关组计算
"""

import numpy as np
from sympy import Matrix


def calculate_max_independent_vectors(vectors):
    """
    计算向量组的极大线性无关组，并将其余向量用极大无关组线性表示

    参数:
    vectors - 向量组，每行是一个向量

    返回:
    independent_vectors - 极大线性无关组
    dependent_vectors - 依赖向量
    coefficients - 依赖向量表示为极大无关组线性组合的系数
    """
    # 转换为numpy数组
    vectors_array = np.array(vectors, dtype=float)

    # 使用sympy的Matrix进行行简化
    A = Matrix(vectors_array.T)  # 转置，使每个向量成为矩阵的一列
    rref, pivots = A.rref()  # 行简化阶梯形
    rref_np = np.array(rref).astype(float)

    print("行简化阶梯形矩阵:")
    print(rref_np)
    print("主元位置:", pivots)

    # 提取极大线性无关组
    independent_indices = list(pivots)
    independent_vectors = vectors_array[independent_indices]

    # 找出依赖向量的索引
    all_indices = set(range(len(vectors)))
    dependent_indices = list(all_indices - set(independent_indices))
    dependent_vectors = vectors_array[dependent_indices] if dependent_indices else []

    # 直接从RREF矩阵中提取系数
    # 非主元列中的元素就表示该列(向量)如何被主元列(向量)线性表示
    coefficients = []

    for dep_idx in dependent_indices:
        coef = []
        for i, ind_idx in enumerate(independent_indices):
            # 对于每个主元列，从RREF矩阵中提取对应的系数
            # 系数直接就是非主元列在主元行的元素
            coef.append(rref_np[i, dep_idx])
        coefficients.append(coef)

        # 验证提取的系数是否正确
        reconstructed = np.zeros_like(vectors_array[0])
        for i, ind_idx in enumerate(independent_indices):
            reconstructed += coef[i] * vectors_array[ind_idx]

        # 如果重构的向量与原向量方向相反，则所有系数取反
        if np.linalg.norm(reconstructed + vectors_array[dep_idx]) < np.linalg.norm(
            reconstructed - vectors_array[dep_idx]
        ):
            coefficients[-1] = [-c for c in coef]

    return (
        independent_vectors,
        dependent_vectors,
        coefficients,
        independent_indices,
        dependent_indices,
    )


def print_results(
    vectors,
    independent_vectors,
    dependent_vectors,
    coefficients,
    independent_indices,
    dependent_indices,
):
    """打印结果"""
    vectors_array = np.array(vectors, dtype=float)

    print("\n向量组:")
    for i, v in enumerate(vectors):
        print(f"α_{i+1} = {v}")

    print("\n极大线性无关组:")
    for i, idx in enumerate(independent_indices):
        print(f"α_{idx+1} = {vectors[idx]}")

    print("\n其余向量表示为极大线性无关组的线性组合:")
    for i, idx in enumerate(dependent_indices):
        coef = coefficients[i]
        expression = " + ".join(
            [f"{coef[j]:.1f} * α_{independent_indices[j]+1}" for j in range(len(coef))]
        )
        print(f"α_{idx+1} = {expression}")

        # 验证结果
        calculated = np.sum(
            [
                coef[j] * np.array(vectors[independent_indices[j]], dtype=float)
                for j in range(len(coef))
            ],
            axis=0,
        )
        print(f"验证: {calculated}")
        print(f"原向量: {vectors[idx]}")
        print(
            f"误差: {np.linalg.norm(calculated - np.array(vectors[idx], dtype=float)):.10f}\n"
        )


if __name__ == "__main__":
    print("问题三：向量组极大线性无关组计算")
    print("=" * 50)

    # 定义向量组
    vectors = [
        [2, 1, 4, 3],
        [-1, 1, -6, 6],
        [-1, -2, 2, -9],
        [1, 1, -2, 7],
        [2, 4, 4, 9],
    ]

    # 计算极大线性无关组
    (
        independent_vectors,
        dependent_vectors,
        coefficients,
        independent_indices,
        dependent_indices,
    ) = calculate_max_independent_vectors(vectors)

    # 打印结果
    print_results(
        vectors,
        independent_vectors,
        dependent_vectors,
        coefficients,
        independent_indices,
        dependent_indices,
    )
