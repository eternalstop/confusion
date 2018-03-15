#!/usr/local/python/bin/python
# coding=utf-8

"""
输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
"""

alpha = 0
digit = 0
space = 0
other = 0
ssum = 0

string = input("Please input some strings.")
for tstr in string:
	if tstr.isalpha():
		alpha += 1
	elif tstr.isdigit():
		digit += 1
	elif tstr.isspace():
		space += 1
	else:
		other += 1
	ssum += 1
print("此字符串中有%s个字母" % alpha)
print("此字符串中有%s个数字" % digit)
print("此字符串中有%s个空格" % space)
print("此字符串中有%s个其他字符" % other)
print("此字符串中共有%s个字符" % ssum)
