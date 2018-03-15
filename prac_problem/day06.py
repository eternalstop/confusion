#!/usr/local/python/bin/python
# coding=utf-8

"""
如果一个渔夫从2011年1月1日开始每三天打一次渔，两天晒一次网，
编程实现当输入2011年1月1日以后的任意一天，
输出该渔夫是在打渔还是在晒网。
"""
#!/usr/local/python/bin/python
# coding=utf-8
"""
编写一个计算天数的程序:用户从键盘中输入年、月、日，在屏幕中输出此日期是该年的第几天。
"""


def result(year, day):
	for i in range(2011, year):
		if year == 2011:
			break
		if judge_year(i):
			day += 366
		else:
			day += 365
	if 0 < day % 5 < 4:
		return 1
	else:
		return 0


def judge_year(y):
	if (y % 4 == 0) & (y % 400 != 0) | (y % 400 == 0):
		return 1
	else:
		return 0


def get_day(y, m, d):
	judge = judge_year(y)
	if judge:
		month_2 = 29
	else:
		month_2 = 28
	day_n = 0
	big_month = [1, 3, 5, 7, 8, 10, 12]
	for i in range(1, int(m)):
		if i in big_month:
			day_n += 31
		elif i == 2:
			day_n += month_2
		else:
			day_n += 30
	fin_day = day_n + d
	return fin_day


def get_data(data):
	y = int(data.split("年")[0])
	m = int(data.split("年")[1].split("月")[0])
	d = int(data.split("年")[1].split("月")[1].split("日")[0])
	return y, m, d


if __name__ == '__main__':
	data = input("请输入要查询的日期(2011年以后的任意一天)，格式xxxx年xx月xx日(例如：2011年1月1日): ")
	y, m, d = get_data(data)
	if y < 2011:
		print("请输入2011年后的任意一天")
		exit()
	else:
		day = get_day(y, m, d)
		if result(y, day):
			print("渔夫在打渔")
		else:
			print("渔夫在晒网")

