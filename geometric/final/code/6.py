#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
矩阵的行列式、特征值和特征向量计算
"""

import numpy as np


def main():
    # 定义矩阵A
    A = np.array([[3, 2, 2], [2, 3, 2], [2, 2, 3]])

    print("矩阵A:")
    print(A)

    # 计算行列式
    det_A = np.linalg.det(A)
    print(f"\n行列式|A| = {det_A}")

    # 计算特征值和特征向量
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # 输出特征值
    print("\n特征值:")
    for i, eigenvalue in enumerate(eigenvalues):
        print(f"λ_{i+1} = {eigenvalue}")

    # 输出特征向量（已归一化）
    print("\n对应的特征向量（已归一化）:")
    for i, eigenvector in enumerate(eigenvectors.T):
        print(f"v_{i+1} = {eigenvector}")

    # 验证特征值和特征向量: A·v = λ·v
    print("\n验证特征值和特征向量:")
    for i, (eigenvalue, eigenvector) in enumerate(zip(eigenvalues, eigenvectors.T)):
        Av = np.dot(A, eigenvector)
        lambda_v = eigenvalue * eigenvector
        print(f"对于λ_{i+1} = {eigenvalue}:")
        print(f"A·v_{i+1} = {Av}")
        print(f"λ_{i+1}·v_{i+1} = {lambda_v}")
        print(f"误差: {np.linalg.norm(Av - lambda_v):.10f}\n")


if __name__ == "__main__":
    main()
