# coding=utf-8
from urllib.request import urlretrieve
import requests
import os
import wx

"""
函数说明:下载《英雄联盟盒子》中的英雄图片
Parameters:
	url - GET请求地址，通过Fiddler抓包获取
	header - headers信息
Returns:
	无
Author:
	Jack Cui
Blog:
	http://blog.csdn.net/c406495762
Modify:
	2017-11-23 by ALi
Modify contents: add GUI
"""


def hero_imgs_download(url, header):
	req = requests.get(url=url, headers=header).json()
	hero_num = len(req['list'])
	print('一共有%d个英雄' % hero_num)
	hero_images_path = 'hero_images'
	for each_hero in req['list']:
		hero_photo_url = each_hero['cover']
		hero_name = each_hero['name'] + '.jpg'
		filename = hero_images_path + '/' + hero_name
		if hero_images_path not in os.listdir():
			os.makedirs(hero_images_path)
		urlretrieve(url=hero_photo_url, filename=filename)


"""
函数说明:打印所有英雄的名字和ID
Parameters:
	url - GET请求地址，通过Fiddler抓包获取
	header - headers信息
Returns:
	无
Author:
	Jack Cui
Blog:
	http://blog.csdn.net/c406495762
Modify:
	2017-08-07
"""


def hero_list(event):
	# print('*' * 100)
	# print('\t\t\t\t欢迎使用《王者荣耀》出装助手！')
	# print('*' * 100)
	hero_str = ''
	hero_str += '*' * 170 + '\n'
	hero_str += '\t\t\t\t\t\t欢迎使用《王者荣耀》出装助手！\n'
	hero_str += '*' * 170 + '\n'
	req = requests.get(url=heros_url, headers=headers).json()
	flag = 0
	for each_hero in req['list']:
		flag += 1
		# print('%s的ID为:%-7s' % (each_hero['name'], each_hero['hero_id']), end='\t\t')
		hero_str += '%s的ID为:%-5s' % (each_hero['name'], each_hero['hero_id']) + '\t\t'
		if flag == 5:
			# print('\n', end='')
			hero_str += '\n\n'
			flag = 0
	contents.SetValue(hero_str)


"""
函数说明:根据equip_id查询武器名字和价格
Parameters:
	equip_id - 武器的ID
	weapon_info - 存储所有武器的字典
Returns:
	weapon_name - 武器的名字
	weapon_price - 武器的价格
Author:
	Jack Cui
Blog:
	http://blog.csdn.net/c406495762
Modify:
	2017-08-07
"""


def seek_weapon(equip_id, weapon_info):
	for each_weapon in weapon_info:
		if each_weapon['equip_id'] == str(equip_id):
			weapon_name = each_weapon['name']
			weapon_price = each_weapon['price']
			return weapon_name, weapon_price


"""
函数说明:获取并打印出装信息
Parameters:
	url - GET请求地址，通过Fiddler抓包获取
	header - headers信息
	weapon_info - 存储所有武器的字典
Returns:
	无
Author:
	Jack Cui
Blog:
	http://blog.csdn.net/c406495762
Modify:
	2017-08-07
"""


def hero_info(event):
	hero_url = "http://gamehelper.gm825.com/wzry/hero/detail?" \
	           "hero_id={}&" \
	           "channel_id=90009a&" \
	           "app_id=h9044j&" \
	           "game_id=7622&" \
	           "game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&" \
	           "vcode=12.0.3&" \
	           "version_code=1203&" \
	           "cuid=2654CC14D2D3894DBF5808264AE2DAD7&" \
	           "ovr=6.0.1&" \
	           "device=Xiaomi_MI+5&" \
	           "net_type=1&" \
	           "client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&" \
	           "info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&" \
	           "info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&" \
	           "mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&" \
	           "info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&" \
	           "mcc=0&" \
	           "clientversion=&" \
	           "bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&" \
	           "os_level=23&" \
	           "os_id=dc451556fc0eeadb&" \
	           "resolution=1080_1920&" \
	           "dpi=480&" \
	           "client_ip=192.168.0.198&" \
	           "pdunid=a83d20d8".format(hero_id.GetValue())
	req = requests.get(url=hero_url, headers=headers).json()
	all_str = ''
	# print('\n历史上的%s:\n    %s' % (req['info']['name'], req['info']['history_intro']))
	all_str = '\n历史上的%s:\n    %s' % (req['info']['name'], req['info']['history_intro'])
	for each_equip_choice in req['info']['equip_choice']:
		# print('\n%s:\n   %s' % (each_equip_choice['title'], each_equip_choice['description']))
		all_str += '\n%s:\n   %s' % (each_equip_choice['title'], each_equip_choice['description']) +'\n'
		total_price = 0
		flag = 0
		for each_weapon in each_equip_choice['list']:
			flag += 1
			weapon_name, weapon_price = seek_weapon(each_weapon['equip_id'], weapon_info_dict)
			# print('%s:%s' % (weapon_name, weapon_price), end='\t')
			all_str += '%s:%s' % (weapon_name, weapon_price)
			if flag == 3:
				# print('\n', end='')
				all_str += '\n'
				flag = 0
			total_price += int(weapon_price)
		# print('神装套件价格共计:%d' % total_price)
		all_str += '神装套件价格共计:%d' % total_price +'\n'
	contents.SetValue(all_str)


"""
函数说明:获取武器信息
Parameters:
	url - GET请求地址，通过Fiddler抓包获取
	header - headers信息
Returns:
	weapon_info_dict - 武器信息
Author:
	Jack Cui
Blog:
	http://blog.csdn.net/c406495762
Modify:
	2017-08-07
"""


def hero_weapon(url, header):
	req = requests.get(url=url, headers=header).json()
	weapon_info_dict = req['list']
	return weapon_info_dict


def load(event):
	contents.SetValue('test %s' % hero_id.GetValue())

headers = {
	'Accept-Charset': 'UTF-8',
	'Accept-Encoding': 'gzip,deflate',
	'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',
	'X-Requested-With': 'XMLHttpRequest',
	'Content-type': 'application/x-www-form-urlencoded',
	'Connection': 'Keep-Alive',
	'Host': 'gamehelper.gm825.com'}
weapon_url = "http://gamehelper.gm825.com/wzry/equip/list?" \
			 "channel_id=90009a&" \
			 "app_id=h9044j&" \
			 "game_id=7622&" \
			 "game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&" \
			 "vcode=12.0.3&" \
			 "version_code=1203&" \
			 "cuid=2654CC14D2D3894DBF5808264AE2DAD7&" \
			 "ovr=6.0.1&" \
			 "device=Xiaomi_MI+5&net_type=1&" \
			 "client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&" \
			 "info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&" \
			 "info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&" \
			 "mno=0&" \
			 "info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&" \
			 "info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&" \
			 "mcc=0&" \
			 "clientversion=&" \
			 "bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&" \
			 "os_level=23&" \
			 "os_id=dc451556fc0eeadb&" \
			 "resolution=1080_1920&" \
			 "dpi=480&" \
			 "client_ip=192.168.0.198&" \
			 "pdunid=a83d20d8"
heros_url = "http://gamehelper.gm825.com/wzry/hero/list?" \
			"channel_id=90009a&" \
			"app_id=h9044j&" \
			"game_id=7622&" \
			"game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&" \
			"vcode=12.0.3&" \
			"version_code=1203&" \
			"cuid=2654CC14D2D3894DBF5808264AE2DAD7&" \
			"ovr=6.0.1&" \
			"device=Xiaomi_MI+5&" \
			"net_type=1&" \
			"client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&" \
			"info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&" \
			"info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&" \
			"mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&" \
			"info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&" \
			"clientversion=&" \
			"bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&" \
			"os_level=23&" \
			"os_id=dc451556fc0eeadb&" \
			"resolution=1080_1920&" \
			"dpi=480&" \
			"client_ip=192.168.0.198&" \
			"pdunid=a83d20d8"
# hero_id = input("请输入要查询的英雄ID:")

app = wx.App()
win = wx.Frame(None, title="英雄查询", size=(900, 700))
bkg = wx.Panel(win)


hero_id = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
# hero_url = "http://gamehelper.gm825.com/wzry/hero/detail?" \
# 		   "hero_id={}&" \
# 		   "channel_id=90009a&" \
# 		   "app_id=h9044j&" \
# 		   "game_id=7622&" \
# 		   "game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&" \
# 		   "vcode=12.0.3&" \
# 		   "version_code=1203&" \
# 		   "cuid=2654CC14D2D3894DBF5808264AE2DAD7&" \
# 		   "ovr=6.0.1&" \
# 		   "device=Xiaomi_MI+5&" \
# 		   "net_type=1&" \
# 		   "client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&" \
# 		   "info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&" \
# 		   "info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&" \
# 		   "mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&" \
# 		   "info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&" \
# 		   "mcc=0&" \
# 		   "clientversion=&" \
# 		   "bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&" \
# 		   "os_level=23&" \
# 		   "os_id=dc451556fc0eeadb&" \
# 		   "resolution=1080_1920&" \
# 		   "dpi=480&" \
# 		   "client_ip=192.168.0.198&" \
# 		   "pdunid=a83d20d8".format(hero_id)
weapon_info_dict = hero_weapon(weapon_url, headers)
id_button = wx.Button(bkg, label='查看英雄ID')
id_button.Bind(wx.EVT_BUTTON, hero_list)
hero_button = wx.Button(bkg, label='查询英雄')
hero_button.Bind(wx.EVT_BUTTON, hero_info)
# load_button.Bind(wx.EVT_BUTTON, load)

h_box = wx.BoxSizer()
h_box.Add(hero_id, proportion=1, flag=wx.EXPAND)
h_box.Add(id_button, proportion=0, flag=wx.LEFT, border=5)
h_box.Add(hero_button, proportion=0, flag=wx.LEFT, border=5)
v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
v_box.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(v_box)
win.Show()


if __name__ == '__main__':
	app.MainLoop()

