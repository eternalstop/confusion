# -*- coding: utf-8 -*-
# import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatchs

# X轴，Y轴数据
y1_list = list()
x1_list = list()
y2_list = list()
x2_list = list()
prex1 = 1
prex2 = 1
with open(r"E:\WorkDocs\209-apc.txt") as y1_value:
    for y1_tmp_value in y1_value:
        y1_list.append(y1_tmp_value)
        x1_list.append(prex1)
        prex1 = prex1 + 1
x1 = x1_list
y1 = y1_list

with open(r"E:\WorkDocs\209-noapc.txt") as y2_value:
    for y2_tmp_value in y2_value:
        y2_list.append(y2_tmp_value)
        x2_list.append(prex2)
        prex2 = prex2 + 1
x2 = x2_list
y2 = y2_list

plt.figure(figsize=(8, 4))
# 创建绘图对象
apc, = plt.plot(x1, y1, "g")
noapc, = plt.plot(x2, y2, "r")
# 在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xlabel("Time(ab -r -k -n5000 -c100)")
# X轴标签
plt.ylabel("Value")
# Y轴标签
plt.title("Requests per second")
# 图标题
red_patch = mpatchs.Patch(color='red', label='NoApc')
green_patch = mpatchs.Patch(color='green', label='Apc')
blue_patch = mpatchs.Patch(color='blue', label='OpCache')

plt.legend(handles=[red_patch, green_patch, blue_patch])
# 图例
plt.show()
# 显示图
# plt.savefig(r"E:\WorkDocs\209-noapc.png")
# 保存图
