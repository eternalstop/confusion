# coding=utf-8
import random
import csv
import time
import pandas as pd


def play():
	blue_list = [random.randrange(1, 17)]
	red_list = []
	tmp_dic = {}
	ball_dic = {}
	for i in range(6):
		red_list.append(random.randrange(1, 34))
	tmp_dic['red'] = red_list
	tmp_dic['blue'] = blue_list
	ball_dic['ball'] = tmp_dic
	return ball_dic


def w_csv(ball_dic, judge):
	if judge:
		print("明天再来")
	else:
		now_time = time.strftime('%Y%m%d', time.localtime(time.time()))
		with open('play.csv', 'a+') as fd:
			writer2 = csv.writer(fd)
			for key in ball_dic:
				writer2.writerow([now_time, ball_dic[key]])


def ball_judge(file='play.csv'):
	periods = []
	data = pd.read_csv(file)
	today = time.strftime('%Y%m%d', time.localtime(time.time()))
	for period, ball in zip(data['periods'], data['ball']):
		periods.append(period)
	if not len(periods):
		return False
	else:
		last_periods = periods[-1]
		if str(today) == str(last_periods):
			return True
		else:
			return False


if __name__ == '__main__':
	dic = play()
	judge = ball_judge('play.csv')
	w_csv(dic, judge)
