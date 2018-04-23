#!/usr/local/python/bin/python
# coding=utf-8
from urllib import parse, request
from bs4 import BeautifulSoup
import random


def get_chengyu(end_str):
	temp_list = []
	end_str = end_str.encode('gb2312')
	header = {'Useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	          'Connection': 'keep-alive',
	          'Host': 'cy.5156edu.com'}
	base_url = 'http://cy.5156edu.com/serach.php'
	post_args = {'f_key': end_str, 'f_type': 'chengyu', 'f_type2': '1'}
	post_args = parse.urlencode(post_args).encode('gb2312')
	req = request.Request(base_url, headers=header, data=post_args)
	html = request.urlopen(req).read()
	soup = BeautifulSoup(html, 'html.parser', from_encoding="gb2312")
	big_list = soup.table.contents[1].contents[1].contents[1].contents[11].contents[2:]
	[big_list.remove(i) for i in big_list if i == '\n']
	for j in big_list:
		temp_list.append(str(j).split('u', 1)[1].split('>')[1].split('<')[0].strip())
	max_len = len(temp_list) - 1
	flag = random.randint(0, max_len)
	return temp_list[flag]


if __name__ == '__main__':
	print(get_chengyu("二"))
