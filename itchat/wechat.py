#!/usr/local/python/bin
# coding=utf-8
import itchat
from bs4 import BeautifulSoup
from urllib import parse, request
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


# @itchat.msg_register(itchat.content.TEXT)
# def test(msg):
# 	print(msg['Text'])


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_reply(msg):
	group_name = msg['User']['NickName']
	from_user = msg['ActualNickName']
	group_id = msg['FromUserName']
	print(group_name, from_user, group_id, msg['Text'])

	if group_name == '胡店长和他的伙计们' and from_user == "随性，":
		itchat.send("test from group %s from user %s" % (group_name, from_user), toUserName=group_id)


itchat.auto_login(True)
itchat.run()
