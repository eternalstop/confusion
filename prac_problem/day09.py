#!/usr/local/python/bin/python
# coding=utf-8

"""
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""
num_list = [1, 2, 3, 4]
fin_list = []
for i in num_list:
	for j in num_list:
		for k in num_list:
			if (i == j) | (i == k) | (j == k):
				continue
			else:
				fin_list.append(i * 100 + j * 10 + k)
print(len(fin_list))
print(fin_list)
