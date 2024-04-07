"""
圆锥体表面积计算
"""
import math  # 导入math包，用于数学计算

PI = math.pi  # 定义圆周率π
r = float(input("请输入半径:"))  # 输入半径大小
h = float(input("输入圆锥的高:"))  # 圆锥的高
s_d = float(PI * r ** 2)  # 套用公式计算圆锥底面积
s_c = float(PI * r * math.sqrt(r ** 2 + h ** 2))  # 套用公式计算侧面积
s_b = s_d + s_c  # 计算表面积
v = 1 / 3 * PI * r ** 2 * h  # 计算体积
print("圆锥表面积为:%6.2f" % s_b)
print("圆锥体积为:%6.2f" % v)
