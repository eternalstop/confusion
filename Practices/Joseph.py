#!/usr/local/python/bin/python
# coding=utf-8


def joseph(n, k):
	link = list(range(1, n + 1))
	ind = 0
	for i in range(n - 1):
		ind = (ind + k) % len(link)
		ind -= 1
		print("kill: %s" % link[ind])
		del link[ind]
		if ind == -1:
			# the last element of link
			ind = 0
	print("survice: %s" % link[0])


if __name__ == '__main__':
	joseph(100, 7)
