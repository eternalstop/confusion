#!/usr/local/python/bin/python
# coding=utf-8
"""
求一个整数任意次方后的最后三位数，
即求x^y的最后三位数，x和y的值由键盘输入。
"""

x = input("请输入底数： ")
y = input("请输入指数： ")

result = int(x) ** int(y) % 1000

if result < 100:
	print("%s的%s次方的后三位是0%d" % (x, y, result))
else:
	print("%s的%s次方的后三位是%d" % (x, y, result))
