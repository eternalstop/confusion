# coding=utf-8
import random
import csv
import time
<<<<<<< HEAD
=======
import pandas as pd
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9


def play():
	blue_list = [i for i in range(1, 17)]
	red_list = [j for j in range(1, 33)]
	tmp_dic = {}
	ball_dic = {}
	red = random.sample(red_list, 6)
	blue = random.sample(blue_list, 1)
	tmp_dic['red'] = red
	tmp_dic['blue'] = blue
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
<<<<<<< HEAD
	print(dic)
	# judge = ball_judge('play.csv')
	# w_csv(dic, judge)
=======
	judge = ball_judge('play.csv')
	w_csv(dic, judge)
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9
