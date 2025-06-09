#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
随机数生成与排序
"""

import numpy as np


def main():
    # 设置随机种子以确保结果可重现
    np.random.seed(42)

    # 生成10个[2, 30]之间的随机整数
    random_numbers = np.random.randint(2, 31, size=10)
    print("生成的随机数:")
    print(random_numbers)

    # 使用Python内置排序函数
    sorted_numbers = sorted(random_numbers)
    print("\n排序后的结果:")
    print(sorted_numbers)


if __name__ == "__main__":
    main()
