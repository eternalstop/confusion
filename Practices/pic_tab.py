# -*- coding: utf-8 -*-
# import numpy as np
import matplotlib.pyplot as plt

# X轴，Y轴数据
y_list = list()
x_list = list()
prex = 1
with open("M:\Python Pro\Practices\meminfo.txt") as y_value:
    for y_tmp_value in y_value:
        y_list.append(y_tmp_value)
        x_list.append(prex)
        prex = prex + 1
x = x_list
y = y_list
plt.figure(figsize=(8, 4))
# 创建绘图对象
plt.plot(x, y, "b--", linewidth=1)
# 在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xlabel("Time(h)")
# X轴标签
plt.ylabel("Value")
# Y轴标签
plt.title("Tcp Connections")
# 图标题
plt.show()
# 显示图
plt.savefig("test.jpg")
# 保存图
