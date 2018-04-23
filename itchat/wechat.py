#!/usr/local/python/bin
# coding=utf-8
import itchat


# @itchat.msg_register(itchat.content.TEXT)
# def test(msg):
# 	print(msg['Text'])


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_reply(msg):
	group_name = msg['User']['NickName']
	from_user = msg['ActualNickName']
	group_id = msg['FromUserName']
	print(group_name, from_user)

	# if group_name == '胡店长和他的伙计们':
	# itchat.send("test from group %s from user %s" % (group_name, from_user), toUserName="胡店长和他的伙计们")
	itchat.send("为什么这个组正常", toUserName="test")
	itchat.send("为什么这个组正常", toUserName=group_name)


itchat.auto_login(True)
itchat.run()
