#!/usr/local/python/bin/python
# coding=utf-8
"""
3对情侣参加婚礼，3个新郎为A、B、C，3个新娘为X、Y、Z，
有人想知道究竟谁与谁结婚，于是就问新人中的三位，得到如下结果：
A说他将和X结婚；X说她的未婚夫是C；C说他将和Z结婚。
这人事后知道他们在开玩笑，说的全是假话。那么，究竟谁与谁结婚呢？
"""

bride = ['X', 'Y', 'Z']
groom = ['A', 'B', 'C']

for man1 in range(0, 3):
	for man2 in range(0, 3):
		for man3 in range(0, 3):
			if (man1 != 0) & (man3 != 0) & (man3 != 2) & (man1 != man3) & (man1 != man2) & (man2 != man3):
				print("新娘 %s 会嫁给新郎 %s" % (bride[man1], groom[0]))
				print("新娘 %s 会嫁给新郎 %s" % (bride[man2], groom[1]))
				print("新娘 %s 会嫁给新郎 %s" % (bride[man3], groom[2]))
