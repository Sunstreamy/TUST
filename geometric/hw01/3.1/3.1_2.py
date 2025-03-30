# 导入需要的工具箱
import numpy as np  # 数学计算工具箱，处理数字和数组
import matplotlib.pyplot as plt  # 画图工具箱，用来画各种图表
from scipy import stats  # 统计工具箱，用来做数学分析
import matplotlib.font_manager as fm  # 字体管理工具箱，处理中文显示问题

# 设置中文显示（为了让图表能显示汉字）
try:
    # 尝试使用电脑里已有的中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'SimSun']  # 设置字体列表
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示为方框的问题
except:
    print("警告：可能无法正确显示中文")  # 如果出错就提示可能有中文显示问题

# 实验数据准备（老师给的题目数据）
# 拉力数据（单位：磅/平方英寸），先转换成小数更方便计算
S = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) * 1e-3  # 1e-3 就是除以1000
# 伸长率数据（单位：英寸/英寸），同样转换成小数
e = np.array([0, 19, 57, 94, 134, 173, 216, 256, 297, 343, 390]) * 1e-5  # 1e-5 就是除以100000

# 第一步：画散点图（把数据点画在纸上）
plt.figure(figsize=(10, 6))  # 准备一张画布，尺寸是10寸宽6寸高
plt.scatter(S, e, color='blue', marker='o', label='实验数据')  # 画蓝色圆圈的点，图例叫"实验数据"

# 给每个数据点加标注（像给地图上的地点加名称）
for i in range(len(S)):
    # 在点旁边写坐标，格式举例：(0.005, 0.00019)
    plt.text(S[i], e[i], f'({S[i]:.3f}, {e[i]:.5f})',  # 坐标保留3位和5位小数
             fontsize=8,  # 字体大小
             ha='right',  # 水平方向向右对齐（文字在点右边）
             va='bottom',  # 垂直方向向下对齐（文字在点下方）
             rotation=15,  # 文字旋转15度（防止重叠）
             alpha=0.7)  # 透明度70%（让文字不那么显眼）

# 第二步：做数学分析（找数据点的规律）
# 用统计工具找最合适的直线公式 y = kx + b
slope, intercept, r_value, p_value, std_err = stats.linregress(S, e)
# slope是斜率（就是公式里的k）
# intercept是截距（就是公式里的b）
# r_value是相关系数，说明xy关系有多紧密

# 打印找到的直线参数
print(f"弹簧系数 c1 = {slope:.4f}")  # 保留4位小数
print(f"相关系数 R² = {r_value**2:.4f}")  # R平方值越接近1说明直线越合适

# 第三步：画拟合直线（把找到的规律画出来）
x_line = np.linspace(0, max(S)*1.1, 100)  # 生成100个均匀的x值，从0到最大拉力多10%
y_line = slope * x_line + intercept  # 用公式算出对应的y值
plt.plot(x_line, y_line, 'r-', label=f'拟合曲线: e = {slope:.4f}S + {intercept:.6f}')  # 画红色直线

# 第四步：装饰图表（让图表更清楚好看）
plt.title('钢丝弹簧的拉力与伸长关系')  # 大标题
plt.xlabel('拉力 S (磅/平方英寸)')  # x轴说明
plt.ylabel('伸长率 e (英寸/英寸)')  # y轴说明
plt.grid(True)  # 显示网格线（方便读坐标）
plt.legend()  # 显示图例（说明哪些颜色代表什么）

# 在图表上写弹簧系数公式
plt.rcParams['mathtext.fontset'] = 'stix'  # 设置数学公式字体
plt.rcParams['font.family'] = 'STIXGeneral'  # 设置字体家族
plt.annotate(r'$c_1 = %.4f$' % slope,  # 要显示的内容（c₁用数学符号显示）
             xy=(0.6*max(S), 0.85*max(e)),  # 文字位置（x是最大值的60%，y是最大值的85%）
             fontsize=12,  # 字体大小
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.3))  # 给文字加黄色半透明圆角框

# 保存图表到图片文件
plt.savefig('3.1_2res.png', dpi=300, bbox_inches='tight')  # 保存为PNG格式，分辨率300，裁剪多余空白

# 显示画好的图表（像翻开画册一样）
plt.show()

# 第五步：验证模型（检查我们的公式准不准）
predicted_e = slope * S  # 用公式计算预测值
relative_error = np.abs(predicted_e - e) / e * 100  # 计算误差百分比

print("\n模型验证:")
print("拉力(S)\t实测伸长率\t预测伸长率\t误差百分比")  # 制表符对齐数据
for i in range(len(S)):
    if e[i] > 0:  # 避免除以0（当实测为0时不计算误差）
        print(f"{S[i]:.3f}\t{e[i]:.5f}\t{predicted_e[i]:.5f}\t{relative_error[i]:.2f}%")
    else:
        print(f"{S[i]:.3f}\t{e[i]:.5f}\t{predicted_e[i]:.5f}\t-")  # 0的情况显示"-"