#!/usr/local/python/bin/python
# coding=utf-8

"""
打印出如下图案（菱形）
        *
       ***
      *****
     ******* （短棱长度）
      *****
       ***
        *
"""


def prismatic(pri_len):
<<<<<<< HEAD
    l_line = (pri_len + 1) // 2
    for i in range(1, pri_len + 1):
        if i > l_line:
            print(' ' * (i - l_line) + '*' * (pri_len * 2 + 1 - 2 * i))
        else:
            print(' ' * (l_line - i) + '*' * (i * 2 - 1))


if __name__ == "__main__":
    num = int(input("请输出棱长： "))
    if num % 2:
        prismatic(num)
    else:
        print("请输入一个大于3的奇数，Exit！")
=======
	l_line = (pri_len + 1) // 2
	for i in range(1, pri_len + 1):
		if i > l_line:
			print(' ' * (i - l_line) + '*' * (pri_len * 2 + 1 - 2 * i))
		else:
			print(' ' * (l_line - i) + '*' * (i * 2 - 1))


if __name__ == "__main__":
	num = int(input("请输出棱长： "))
	if num % 2:
		prismatic(num)
	else:
		print("请输入一个大于3的奇数，Exit！")
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9
