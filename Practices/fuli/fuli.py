# coding=utf-8

import re
import urllib
import urllib2
import csv
import collections
from bs4 import BeautifulSoup


def get_html(url):
	page = urllib.urlopen(url)
	html = page.read()
	# soup = BeautifulSoup(html, 'lxml')
	return html


def get_red(index_html):
	reg = r'[\d][\d][ ][\d][\d][ ][\d][\d][ ][\d][\d][ ][\d][\d][ ][\d][\d]'
	red_ball = re.findall(reg, index_html, re.I | re.M)
	if red_ball:
		return red_ball[0].split()


def get_blue(link):
	tmp_list = []
	head = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) '
		              'AppleWebKit/535.19 (KHTML, like Gecko) '
		              'Chrome/18.0.1025.166  '
		              'Safari/535.19'}
	req = urllib2.Request(link, headers=head)
	response = urllib2.urlopen(req)
	html = response.read()
	soup = BeautifulSoup(html, 'lxml')
	soup_text = soup.find('em', class_='blue-txt')
	if soup_text:
		for i in soup_text.children:
			tmp_list.append(str(i))
	return tmp_list


def get_link_list(base_html):
	reg = r'http://kaijiang.500.com/shtml/ssq/.+?.shtml'
	urlre = re.compile(reg)
	urllist = re.findall(urlre, base_html)
	return urllist[::-1]


def w_csv(b_dict, file_name):
	with open(file_name, 'ab+') as fd:
		writer2 = csv.writer(fd)
		for key in b_dict:
			writer2.writerow([key, b_dict[key]])


if __name__ == '__main__':
	base_link = "http://kaijiang.500.com/shtml/ssq/03001.shtml"
	base_html = get_html(base_link)
	link_list = get_link_list(base_html)
	dic_list = ['red0', 'red1', 'red2', 'red3', 'red4', 'red5', 'blue']
	# for i in range(7):
	# 	dic_list[i] = collections.OrderedDict()
	# 	dic_list[i]['periods'] = 'ball'

	# for num in range(0, 3, 1):
	for num in range(2182, len(link_list), 1):
		# if num == 0:
		# 	for i in range(7):
		# 		dic_list[i] = collections.OrderedDict()
		# 		dic_list[i]['periods'] = 'ball'
		# 		if i < 6:
		# 			w_csv(dic_list[i], 'red%s.csv' % i)
		# 		else:
		# 			w_csv(dic_list[i], 'blue.csv')
		for i in range(7):
			dic_list[i] = collections.OrderedDict()
		link = link_list[num]
		html = get_html(link)
		red_list = get_red(html)
		blue_list = get_blue(link)
		print(link_list[num])
		print(red_list)
		print(blue_list)
		for i in range(7):
			if i < 6:
				# pass
				dic_list[i][num] = red_list[i]
				w_csv(dic_list[i], 'red%s.csv' % i)
			else:
				dic_list[i][num] = blue_list[0]
				w_csv(dic_list[i], 'blue.csv')
		print(num)
