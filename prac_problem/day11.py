#!/usr/local/python/bin/python
# coding=utf-8

"""
一个数如果恰好等于它的因子之和，这个数就成为“完数”。例如6=1+2+3。编程找出1000以内的所有完数。
"""
import time
start = time.clock()
for i in range(1, 1001):
	num_list = []
	flag = i
	for j in range(1, i):
		if i % j == 0:
			num_list.append(j)
			flag -= j
	if flag == 0:
		print("%s 是完全数" % i)
end = time.clock()
print(end - start)
