import matplotlib.pyplot as plt
import numpy as np


def f(t):
	return 53 + 50 * np.sin(np.pi * t / 10 - np.pi / 2)


a = np.arange(0.0, 30.0, 0.02)
plt.plot(a, f(a))
plt.xlabel('横坐标(时间)', fontproperties='Kaiti', fontsize=14, color='red')
plt.ylabel('纵坐标(振幅)', fontproperties='SimHei', fontsize=18, color='red')
plt.title('简谐运动 h(t)=53 + 50sin(πt/10 - π/2)', fontproperties='SimHei', fontsize=18, color='green')
plt.grid(True)
plt.axis([0, 30, 0, 120])
plt.annotate('曲线', xy=(10, 105), xytext=(15, 105), arrowprops=dict(facecolor='black', shrink=0.2),
             fontproperties='SimHei', fontsize=12, color='red')
plt.show()
