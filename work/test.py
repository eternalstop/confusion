#!/usr/local/python/bin/python
# coding=utf-8

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




