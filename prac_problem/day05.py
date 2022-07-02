#!/usr/local/python/bin/python
# coding=utf-8

"""
中国古代数学家张丘建在他的《算经》中提出了一个著名的“百钱买百鸡问题”，
鸡翁一，值钱五，鸡母一，值钱三，鸡雏三，值钱一，
百钱买百鸡，问翁、母、雏各几何？
"""
plan = 1
for cock in range(0, 21):
	for hen in range(0, 34):
		for chick in range(3, 99):
			if (chick % 3 == 0) & (cock + hen + chick == 100) & (cock * 5 + hen * 3 + chick // 3 == 100):
				print("方案%s: 翁 %s 只，母 %s 只，雏 %s 只" % (plan, cock, hen, chick))
				plan += 1
<<<<<<< HEAD
=======

>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9
