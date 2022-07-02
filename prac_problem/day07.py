#!/usr/local/python/bin/python
# coding=utf-8

"""
根据输入的三角形的三条边判断三角形的类型，并输出它的面积和类型。
三角形类型：等边三角形、等腰三角形、直角三角形、普通三角形
海伦公式：p=1/2(a+b+c),S=√[p(p-a)(p-b)(p-c)]
"""
import math

category_list = ['等边三角形', '等腰三角形', '直角三角形', '普通三角形']


<<<<<<< HEAD
# 判断三角形合法性
=======
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9
def judge(a, b, c):
	three = [a, b, c]
	three.sort()
	if three[0] + three[1] > three[2]:
		return 1
	else:
		return 0


<<<<<<< HEAD
# 判断三角形类型
=======
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9
def category(a, b, c):
	t_list = [a, b, c]
	t_list.sort()
	if a == b == c:
		return 0
	elif (a == b) | (a == c) | (b == c):
		return 1
	elif t_list[0] ** 2 + t_list[1] ** 2 == t_list[2] ** 2:
		return 2
	else:
		return 3


<<<<<<< HEAD
# 计算三角形面积
=======
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9
def acreage(a, b, c):
	p = (a + b + c) / 2
	t_acreage = math.sqrt(p * (p - a) * (p - b) * (p - c))
	return t_acreage


if __name__ == '__main__':
	a = int(input("请输入边长a: "))
	b = int(input("请输入边长b: "))
	c = int(input("请输入边长c: "))
	if judge(a, b, c):
		t_class = category(a, b, c)
		print("该三角形为%s" % category_list[t_class])
		t_sum = acreage(a, b, c)
		print("该三角形的面积是： %s" % t_sum)
	else:
		print("Sorry,您输入的三边构不成三角形，Exit！")
