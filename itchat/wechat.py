#!/usr/local/python/bin
# coding=utf-8
import itchat
from bs4 import BeautifulSoup
from urllib import parse, request
import random
from pypinyin import lazy_pinyin
import Pinyin2Hanzi
from Pinyin2Hanzi import DefaultDagParams, dag
from itertools import chain


def get_chengyu(word):
	bigger_list = []
	if Pinyin2Hanzi.is_chinese(word):
		word_pinyin = lazy_pinyin(word)
		dagParams = DefaultDagParams()
		word_list = []
		result = dag(dagParams, word_pinyin, path_num=4, log=True)
		for item in result:
			word_list.append(item.path[0])

		for avg_word in word_list:
			bigger_list.append(find_chengyu(avg_word))

		heiheihei = list((chain(*bigger_list)))
		max_len = len(heiheihei) - 1
		flag = random.randint(0, max_len)
		return heiheihei[flag]
	else:
		return "Null"


def find_chengyu(end_str):
	temp_list = []
	end_str = end_str.encode('gb2312')
	header = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
		'Useragent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
		'Connection': 'keep-alive',
		'Host': 'www.51bc.net'
	}
	base_url = 'http://www.51bc.net/cy/serach.php'
	post_args = {'f_key': end_str, 'f_type': 'chengyu', 'f_type2': '1'}
	post_args = parse.urlencode(post_args).encode('gb2312')
	req = request.Request(base_url, headers=header, data=post_args)
	html = request.urlopen(req).read()
	soup = BeautifulSoup(html, 'html.parser', from_encoding="gb18030")
	big_list = soup.find_all("")
	[big_list.remove(i) for i in big_list if i == '\n']
	for j in big_list:
		temp_list.append(str(j).split('u', 1)[1].split('>')[1].split('<')[0].strip())
	fin_list = temp_list[:]
	for k in temp_list:
		if k[0].encode('gb2312') != end_str:
			fin_list.remove(k)
	# print(fin_list)
	if len(fin_list) == 0:
		return "Null"
	else:
		return fin_list


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_reply(msg):
	group_name = msg['User']['NickName']
	from_user = msg['ActualNickName']
	group_id = msg['FromUserName']
	print(group_name, from_user, group_id, msg['Text'])
	print(msg['Text'][-1])
	temp_str = msg['Text'][-1]


	# if group_name == 'test' and from_user == '我是我':
	# if group_name == 'test' and from_user == 'ali777':

	if group_name == '张店长和他的伙计们' and from_user == '倩酱粉丝后援团团长':
		# itchat.send("test from group %s from user %s" % (group_name, from_user), toUserName=group_id)
		send_msg = get_chengyu(temp_str)
		if send_msg != "Null":
			itchat.send(send_msg, toUserName=group_id)

itchat.auto_login(True)
itchat.run()
