#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
线性规划问题求解：机床生产优化问题
"""

import pulp
import matplotlib.pyplot as plt
import numpy as np


def solve_machine_production():
    """
    求解机床生产问题

    问题描述：
    某机床厂生产甲、乙两种机床，每台销售后的利润分别为4000元与3000元。
    生产甲机床需要A、B机器加工，加工时间分别为每台2小时和1小时；
    生产乙机床需用A、B、C三种机器加工，加工时间均为每台1小时。
    若每天可用于加工的机器时数分别为A机器10小时，B机器8小时，C机器7小时，
    问该厂应生产甲、乙机床各几台，才能使总利润最大？
    """
    # 创建问题实例
    prob = pulp.LpProblem("机床生产优化问题", pulp.LpMaximize)

    # 定义决策变量
    x1 = pulp.LpVariable("甲机床数量", lowBound=0)  # 甲机床数量
    x2 = pulp.LpVariable("乙机床数量", lowBound=0)  # 乙机床数量

    # 设置目标函数
    prob += 4000 * x1 + 3000 * x2, "总利润"

    # 添加约束条件
    prob += 2 * x1 + x2 <= 10, "A机器时间约束"
    prob += x1 + x2 <= 8, "B机器时间约束"
    prob += x2 <= 7, "C机器时间约束"

    # 求解问题
    prob.solve()

    # 输出结果
    print("求解状态:", pulp.LpStatus[prob.status])
    print("\n最优解:")
    for v in prob.variables():
        print(f"{v.name} = {v.varValue}")
    print(f"\n最大利润 = {pulp.value(prob.objective)} 元")

    # 考虑整数解
    prob_int = pulp.LpProblem("机床生产优化问题(整数解)", pulp.LpMaximize)

    # 定义整数决策变量
    x1_int = pulp.LpVariable("甲机床数量", lowBound=0, cat=pulp.LpInteger)
    x2_int = pulp.LpVariable("乙机床数量", lowBound=0, cat=pulp.LpInteger)

    # 设置目标函数
    prob_int += 4000 * x1_int + 3000 * x2_int, "总利润"

    # 添加约束条件
    prob_int += 2 * x1_int + x2_int <= 10, "A机器时间约束"
    prob_int += x1_int + x2_int <= 8, "B机器时间约束"
    prob_int += x2_int <= 7, "C机器时间约束"

    # 求解问题
    prob_int.solve()

    # 输出结果
    print("\n整数解:")
    for v in prob_int.variables():
        print(f"{v.name} = {v.varValue}")
    print(f"\n整数解最大利润 = {pulp.value(prob_int.objective)} 元")

    return {
        "x1": x1.varValue,
        "x2": x2.varValue,
        "max_profit": pulp.value(prob.objective),
        "x1_int": x1_int.varValue,
        "x2_int": x2_int.varValue,
        "max_profit_int": pulp.value(prob_int.objective),
    }

if __name__ == "__main__":
    result = solve_machine_production()

