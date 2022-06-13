#!/usr/local/python/bin/python
# coding=utf-8
"""
编写一个计算天数的程序:用户从键盘中输入年、月、日，在屏幕中输出此日期是该年的第几天。
"""
big_month = [1, 3, 5, 7, 8, 10, 12]


# 闰年判断
def judge_year(y):
	if (y % 4 == 0) & (y % 400 != 0) | (y % 400 == 0):
		return 1
	else:
		return 0


# 计算天数
def get_day(y, m, d):
	judge = judge_year(y)
	# 判断是否为2月
	if judge:
		month_2 = 29
	else:
		month_2 = 28
	day_n = 0
	for i in range(1, int(m)):
		if i in big_month:
			day_n += 31
		elif i == 2:
			day_n += month_2
		else:
			day_n += 30
	fin_day = day_n + d
	return fin_day


# 截取年、月、日
def get_data(data):
	y = int(data.split("年")[0])
	m = int(data.split("年")[1].split("月")[0])
	d = int(data.split("年")[1].split("月")[1].split("日")[0])
	return y, m, d


if __name__ == '__main__':
	data = input("请输入要查询的日期，格式xxxx年xx月xx日(例如：1999年9月9日): ")
	y, m, d = get_data(data)
	# 判断日期的正确性
	print(get_day(y, m, d))
