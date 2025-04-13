from fractions import Fraction
from tabulate import tabulate
import io
import sys

# Capture print output to format it later if needed, or just print directly
# output_buffer = io.StringIO()
# sys.stdout = output_buffer # Redirect stdout

# --- Step 1: Variable Substitution and Standardization (Explanation) ---

explanation = """
====================================================================
 变量替换与标准化 (Variable Substitution and Standardization)
====================================================================

**原问题是：**
最大化 Z = 10x + 35y
约束条件：
1.  8x + 6y <= 48
2.  4x + y <= 20
3.  y >= 5
4.  x >= 0, y >= 0

**处理约束 y >= 5：**
单纯形法通常处理的是小于等于 (<=) 的约束和非负变量。约束 "y >= 5" 不符合标准形式。
为了解决这个问题，我们引入一个新变量。设一个新的变量，我们叫它 `x2`，让 `y = x2 + 5`。
因为原始约束要求 `y` 必须大于或等于 5 (`y >= 5`)，那么代入 `y = x2 + 5` 后，就得到 `x2 + 5 >= 5`， 这意味着 `x2 >= 0`。这样，我们就把约束 `y >= 5` 转换成了对新变量 `x2` 的非负要求，这符合单纯形法的标准。
同时，我们让原来的变量 `x` 保持不变，并称之为 `x1`，即 `x = x1`。

**将新变量代入原问题：**
我们将 `x = x1` 和 `y = x2 + 5` 代入到原问题的目标函数和所有约束中。

1.  **代入目标函数:**
    `Max Z = 10(x1) + 35(x2 + 5) = 10x1 + 35x2 + 175`

2.  **代入约束 1:**
    `8(x1) + 6(x2 + 5) <= 48  =>  8x1 + 6x2 + 30 <= 48  =>  8x1 + 6x2 <= 18`

3.  **代入约束 2:**
    `4(x1) + (x2 + 5) <= 20  =>  4x1 + x2 + 5 <= 20  =>  4x1 + x2 <= 15`

4.  **处理非负约束:**
    `x >= 0` 变成了 `x1 >= 0`。
    `y >= 5` 变成了 `x2 >= 0`。

**整理变换后的问题：**
我们最大化 `Z = 10x1 + 35x2 + 175`。
由于 `+175` 是常数，我们先最大化 `z = 10x1 + 35x2`，最后再将 175 加回。
变换后的标准问题是：
最大化 `z = 10x1 + 35x2`
约束条件：
1.  `8x1 + 6x2 <= 18`
2.  `4x1 + 1x2 <= 15`
3.  `x1 >= 0`, `x2 >= 0`

**引入松弛变量 (y1, y2):**
将不等式约束变为等式，引入松弛变量 `y1 >= 0`, `y2 >= 0`。
约束 1 变为: `8x1 + 6x2 + y1 = 18`
约束 2 变为: `4x1 + 1x2 + y2 = 15`

**准备表格形式：**
目标函数 `z = 10x1 + 35x2` 移项写成 `-10x1 - 35x2 + z = 0`。
问题的表格形式是：
`8x1 + 6x2 + y1 = 18`
`4x1 + 1x2 + y2 = 15`
`-10x1 - 35x2 + z = 0`
所有变量 `x1, x2, y1, y2, z >= 0`。

====================================================================
              开始执行单纯形法步骤
====================================================================
"""

print(explanation)


# Helper function to display the tableau
def display_tableau(tableau_data, headers, title):
    """Displays the simplex tableau using tabulate."""
    formatted_data = []
    for row in tableau_data:
        formatted_row = [row[0]] # Keep the basis variable as string
        for item in row[1:]:
             if isinstance(item, (int, float, Fraction)):
                 # Format fractions nicely
                 frac = Fraction(item).limit_denominator()
                 if frac.denominator == 1:
                     formatted_row.append(str(frac.numerator)) # Display integers directly
                 else:
                     formatted_row.append(f"{frac.numerator}/{frac.denominator}") # Display as fraction
             else:
                 formatted_row.append(str(item)) # Keep other things as string (like '*')
        formatted_data.append(formatted_row)

    print(f"\n--- {title} ---")
    # Use a simpler table format for potentially better rendering in various terminals
    print(tabulate(formatted_data, headers=headers, tablefmt="heavy_grid", numalign="right", stralign="right"))
    print("-" * (sum(len(h) for h in headers) + len(headers)*3 + 1) ) # Adjust separator length


# --- Simplex Tableau 0 (Initial Tableau) ---
headers_0 = ['Basis', 'x1', 'x2', 'y1', 'y2', 'z', 'RHS'] # Use y1, y2 as slack names
data_0 = [
    ['y1',  8,   6,  1,  0, 0,  18],
    ['y2',  4,   1,  0,  1, 0,  15],
    ['z', -10, -35,  0,  0, 1,   0]
]

display_tableau(data_0, headers_0, "单纯形表 0 (原始表 / Simplex Tableau 0)")

print("\n分析表 0 (Analysis of Tableau 0):")
print("*   相关变量 (Basic): {y1, y2, z}")
print("*   独立变量 (Non-Basic): {x1, x2} = (0, 0)")
print("*   当前极点 (Transformed x1, x2): (0, 0)")
print("*   当前目标函数值 (z): 0")

# --- Iteration 1: Pivot Selection ---
print("\n--- 迭代 1: 确定枢轴元素 (Iteration 1: Pivot Selection) ---")
print("1. 最优化检验 (Optimality Check): 检查 'z' 行是否存在负系数。")
print("   最小负系数是 -35，在 x2 列。")
print("   ==> x2 为进入变量 (Entering Variable)。")

print("\n2. 可行性检验 (比值测试 / Feasibility Check - Ratio Test): 用右端项 (RHS) 除以进入变量列 (x2) 中的正系数。")
ratio1 = Fraction(data_0[0][-1], data_0[0][2]) if data_0[0][2] > 0 else float('inf')
ratio2 = Fraction(data_0[1][-1], data_0[1][2]) if data_0[1][2] > 0 else float('inf')
print(f"   y1 行: {data_0[0][-1]} / {data_0[0][2]} = {ratio1} = 3")
print(f"   y2 行: {data_0[1][-1]} / {data_0[1][2]} = {ratio2} = 15")
print("   最小正比值是 3，对应于 y1 行。")
print("   ==> y1 为退出变量 (Leaving Variable)。")

pivot_element = data_0[0][2]
print(f"\n3. 枢轴元素 (Pivot Element): 进入变量列 (x2) 和退出变量行 (y1) 的交叉点。")
print(f"   枢轴元素 = {pivot_element} (在 y1 行, x2 列)")

# --- Iteration 1: Pivot Operation ---
print("\n--- 迭代 1: 执行旋转变换 (Iteration 1: Performing Pivot Operation) ---")
print(f"目标: 使枢轴元素变为 1，枢轴列的其他元素变为 0。")

# Calculate new rows using fractions
pivot_row_old = [Fraction(x) for x in data_0[0][1:]] # y1 row, numerical part
pivot_val = Fraction(pivot_element)

# 1. New Pivot Row (new x2 row)
new_x2_row_vals = [x / pivot_val for x in pivot_row_old]
print(f"1. 新 x2 行 = (旧 y1 行) / {pivot_val}")
print(f"   [{', '.join(map(str, pivot_row_old))}] / {pivot_val} = [{', '.join(f'{v.numerator}/{v.denominator}' if v.denominator != 1 else str(v.numerator) for v in new_x2_row_vals)}]")

# 2. New y2 row
old_y2_row_vals = [Fraction(x) for x in data_0[1][1:]] # y2 row
factor_y2 = Fraction(data_0[1][2]) # Coefficient in pivot column for y2 row
new_y2_row_vals = [old - factor_y2 * new for old, new in zip(old_y2_row_vals, new_x2_row_vals)]
print(f"2. 新 y2 行 = (旧 y2 行) - ({factor_y2}) * (新 x2 行)")
print(f"   [{', '.join(map(str, old_y2_row_vals))}] - {factor_y2} * [...] = [{', '.join(f'{v.numerator}/{v.denominator}' if v.denominator != 1 else str(v.numerator) for v in new_y2_row_vals)}]")


# 3. New z row
old_z_row_vals = [Fraction(x) for x in data_0[2][1:]] # z row
factor_z = Fraction(data_0[2][2]) # Coefficient in pivot column for z row
new_z_row_vals = [old - factor_z * new for old, new in zip(old_z_row_vals, new_x2_row_vals)]
print(f"3. 新 z 行  = (旧 z 行) - ({factor_z}) * (新 x2 行)")
print(f"   [{', '.join(map(str, old_z_row_vals))}] - ({factor_z}) * [...] = [{', '.join(f'{v.numerator}/{v.denominator}' if v.denominator != 1 else str(v.numerator) for v in new_z_row_vals)}]")

# --- Simplex Tableau 1 ---
headers_1 = ['Basis', 'x1', 'x2', 'y1', 'y2', 'z', 'RHS']
# Assemble data_1 with correct types (strings for basis, Fractions for numbers)
data_1 = [
    ['x2'] + new_x2_row_vals,
    ['y2'] + new_y2_row_vals,
    ['z']  + new_z_row_vals
]

display_tableau(data_1, headers_1, "单纯形表 1 (Simplex Tableau 1)")

print("\n分析表 1 (Analysis of Tableau 1):")
print("*   相关变量 (Basic): {x2, y2, z}")
print("*   独立变量 (Non-Basic): {x1, y1} = (0, 0)")
# Find the value of basic variables from RHS
x1_val_t1 = 0 # non-basic
x2_val_t1 = data_1[0][-1] # Find x2 row, get RHS
print(f"*   当前极点 (Transformed x1, x2): ({x1_val_t1}, {x2_val_t1}) = (0, 3)")
z_val_t1 = data_1[2][-1] # Find z row, get RHS
print(f"*   当前目标函数值 (z): {z_val_t1} = 105")

# --- Optimality Check after Iteration 1 ---
print("\n--- 表 1 最优化检验 (Optimality Check for Tableau 1) ---")
print("检查 'z' 行中非基变量 (x1, y1) 的系数。")
coeff_x1 = data_1[2][1]
coeff_y1 = data_1[2][3]
print(f"   x1 的系数 = {coeff_x1.numerator}/{coeff_x1.denominator if coeff_x1.denominator != 1 else ''} = 110/3")
print(f"   y1 的系数 = {coeff_y1.numerator}/{coeff_y1.denominator if coeff_y1.denominator != 1 else ''} = 35/6")
print("   'z' 行中的所有系数（对应非基变量）都非负。")
print("==> 当前解对于变换后的问题是最优的 (Optimal for the transformed problem)。")

# --- Final Solution ---
print("\n--- 最终解 (Final Solution) ---")
opt_x1 = 0 # Non-basic
opt_x2 = data_1[0][-1] # Basic variable x2's value from RHS
opt_z = data_1[2][-1] # Value from RHS in z row

print(f"变换后问题的最优解 (Optimal x1, x2): ({opt_x1}, {opt_x2}) = (0, 3)")
print(f"变换后问题的最优目标值 (Optimal z): {opt_z} = 105")

# Convert back to original variables
opt_x = opt_x1
opt_y = opt_x2 + 5
opt_Z = opt_z + 175

print("\n转换回原始变量 (x, y, Z):")
print(f"*   x = x1 = {opt_x}")
print(f"*   y = x2 + 5 = {opt_x2} + 5 = {opt_y}")
print(f"*   最大 Z = z + 175 = {opt_z} + 175 = {opt_Z}")

print("\n====================================================================")
print(f"  原问题的最终答案:")
print(f"  最优解为 x = {opt_x}, y = {opt_y}")
print(f"  最大目标函数值为 Z = {opt_Z}")
print("====================================================================")

# # If using output buffer, print it now
# sys.stdout = sys.__stdout__ # Restore standard output
# print(output_buffer.getvalue())