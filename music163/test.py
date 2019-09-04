# _*_ coding:utf-8 _*_


with open('error.txt') as f:
	errorlist = f.readlines()

print([i.strip('\n') for i in errorlist])

