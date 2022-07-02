#!/usr/local/python/bin/python
# coding=utf-8

<<<<<<< HEAD
a = [197606169, 197124088, 197685401, 197669749, 197248885, 197210724, 197222852, 197252533, 197133289]
b = [1131, 6524, 6123, 963, 9404, 1141, 5810, 7573, 993]
c = [197605038, 197117564, 197679278, 197668786, 197239481, 197209583, 197217042, 197244960, 197132296]
d = [2665, 2754, 2638, 2670, 2796, 2830, 2768, 2861, 2811]


def sum_of_list(sum_list, list_size):
	if list_size == 0:
		return 0
	else:
		return sum_list[list_size - 1] + sum_of_list(sum_list, list_size - 1)


total_a = sum_of_list(a, len(a))
print(total_a)

total_b = sum_of_list(b, len(b))
print(total_b)

total_c = sum_of_list(c, len(c))
print(total_c)

total_d = sum_of_list(d, len(d))
print(total_d)

dalao = ["", ]


=======
from urllib import request
import random

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
link = 'ftp://ott:XX9OWGjL4ubgXSkb@101.89.132.139:18091//pic/basic/2018/01/ad9527e9-a20c-42cd-bb2f-6641c41778d3.jpg'
for i in range(100):
	try:
		random.shuffle(a)
		tempstr = ''.join(a)
		request.urlretrieve(link, 'img/%s.jpg' % tempstr)
	except:
		print("第 %s 失败" % i)
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9




