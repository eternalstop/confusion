# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_blue_data(file_name):
	data = pd.read_csv(file_name)
	blue_count = {
		1: 0, 2: 0, 3: 0, 4: 0,
		5: 0, 6: 0, 7: 0, 8: 0,
		9: 0, 10: 0, 11: 0, 12: 0,
		13: 0, 14: 0, 15: 0, 16: 0,
	}
	for period, value in zip(data['periods'], data['ball']):
		blue_count[value] = blue_count[value] + 1
	return blue_count


def get_red_data(file_name):
	data = pd.read_csv(file_name)
	red_count = {
		1: 0, 2: 0, 3: 0, 4: 0,
		5: 0, 6: 0, 7: 0, 8: 0,
		9: 0, 10: 0, 11: 0, 12: 0,
		13: 0, 14: 0, 15: 0, 16: 0,
		17: 0, 18: 0, 19: 0, 20: 0,
		21: 0, 22: 0, 23: 0, 24: 0,
		25: 0, 26: 0, 27: 0, 28: 0,
		29: 0, 30: 0, 31: 0, 32: 0,
	}
	for period, value in zip(data['periods'], data['ball']):
			red_count[value] = red_count[value] + 1
	return red_count


def get_view(dic, h_color='b', l_color='r', pic_name='ball'):
	ball = dic.keys()
	count = dic.values()
	if len(ball) > 16:
		n_groups = 33
		x_label = 'red ball'
	else:
		n_groups = 16
		x_label = 'blue ball'
	plt.subplots()
	index = np.arange(n_groups)
	bar_width = 0.7
	opacity = 0.5
	plt.figure(figsize=(30, 15))
	plt.bar(index, count, bar_width, alpha=opacity, color=h_color, label='count')
	plt.plot(index, ball, count, l_color)
	plt.xlabel(x_label)
	plt.ylabel('Count')
	plt.title('Two Color Ball')
	plt.xticks(index, ball)
	if len(ball) > 16:
		plt.ylim(0, 100)
		plt.legend()
		plt.tight_layout()
		plt.savefig(pic_name)
	else:
		plt.ylim(0, 170)
		plt.legend()
		plt.tight_layout()
		plt.savefig(pic_name)


if __name__ == '__main__':
	for i in range(6):
		red_dic = get_red_data('red%s.csv' % i)
		get_view(red_dic, 'r', 'k', 'red%s.jpg' % i)
	blue_dic = get_blue_data('blue.csv')
	get_view(blue_dic, pic_name='blue.jpg')

