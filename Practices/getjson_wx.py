#!/usr/local/python/bin/python
# coding=utf-8
import pandas as pd
from urllib import request, parse
from bs4 import BeautifulSoup
import json
import os
import wx
import time


def getid(vodcmsid):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
	          'Connection': 'keep-alive'}
	URL = 'http://125.88.99.8:8082/EPG/jsp/sysoperation/queryVODIDbyName.jsp'
	form = {
		"vodname1": "",
		"vodcmsid": vodcmsid,
		"vodid": ""
	}
	form = parse.urlencode(form).encode('utf-8')
	# noinspection PyBroadException
	try:
		req = request.Request(URL, headers=header, data=form)
		html = request.urlopen(req).read()
		soup = BeautifulSoup(html, "html.parser")
		return soup.form.contents[5].contents[3].contents[3].string.strip()
	except Exception as e:
		# print("This vodcmsID %s can not get short ID!" % vodcmsid)
		contents.SetValue("This vodcmsID %s can not get short ID!" % vodcmsid)


def get_relat(file):
	data = pd.read_excel(file, sheet_name=None)
	relat_dic = {}
	father_list = list(data["子集"]["主集ID"])
	sun_list = list(data["子集"]["子集ID"])
	for i in range(0, len(sun_list)):
		relat_dic[father_list[i]] = []

	for j in range(0, len(sun_list)):
		sun_short_id = getid(sun_list[j])
		relat_dic[father_list[j]].append({"mediaCode": sun_short_id})
		# print("(%s/%s)" % (str(j + 1), str(len(sun_list))))
		contents.SetValue("(%s/%s)" % (str(j + 1), str(len(sun_list))))
	return relat_dic


def getDic(file):
	relationship_dic = get_relat(file)
	data = pd.read_excel(file, sheet_name=None)
	img_list = []
	name_list = []
	data_dic = {"data": []}
	for father_key in data.setdefault("主集"):
		if "片名" in father_key and "图" not in father_key:
			for eve_name in data["主集"][father_key]:
				name_list.append(eve_name)

		if "图片名" in father_key:
			for eve_img in data["主集"][father_key]:
				img_list.append(eve_img)
	flag = 0
	for eve_father_id in data["主集"]["内容/主ID"]:
		father_dic = {}
		father_short_id = getid(eve_father_id)
		father_dic["mediaCode"] = father_short_id
		father_dic["childInfo"] = relationship_dic[eve_father_id]
		father_dic["imgUrl"] = img_list[flag]
		father_dic["channel"] = 2
		father_dic["name"] = name_list[flag]
		data_dic["data"].append(father_dic)
		flag += 1
	return data_dic


def getJson(event):
	# excel_file = r"E:\Codes\Python\confusion\work\getjson\list_json\list-3\list-3.xlsx"
	# excel_file = sys.argv[1]
	excel_file = file_path.GetValue()
	if os.path.exists(excel_file):
		base_path = excel_file.split(".")[0].split("\\")[-1]
		save_path = ""
		for i in excel_file.split("\\")[:-1]:
			save_path += i + "\\"
		save_path = save_path + base_path + "\\"
		dic2 = getDic(excel_file)
		if len(dic2["data"]) > 10:
			for k in range(0, len(dic2["data"]) // 10 + 1):
				if (k + 1) * 10 >= len(dic2["data"]):
					dic3 = {"data": dic2["data"][k * 10:len(dic2["data"])]}
					fin_json = json.dumps(dic3, indent=2, ensure_ascii=False)
					with open(save_path + "list_%s.json" % k, "w+") as fd:
						fd.write(fin_json)
					break
				else:
					dic3 = {"data": dic2["data"][k * 10:(k + 1) * 10]}
					fin_json = json.dumps(dic3, indent=2, ensure_ascii=False)
					with open(save_path + "list_%s.json" % k, "w+") as fd:
						fd.write(fin_json)
		else:
			fin_json = json.dumps(dic2, indent=2, ensure_ascii=False)
			with open(save_path + "list.json", "w+") as fd:
				fd.write(fin_json)
		contents.SetValue("End!")
	else:
		contents.SetValue("%s 文件不存在" % excel_file)


app = wx.App()
win = wx.Frame(None, title="Json生成", size=(900, 700))
bkg = wx.Panel(win)

file_path = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)
go_button = wx.Button(bkg, label='Go')
go_button.Bind(wx.EVT_BUTTON, getJson)

h_box = wx.BoxSizer()
h_box.Add(file_path, proportion=1, flag=wx.EXPAND)
h_box.Add(go_button, proportion=0, flag=wx.LEFT, border=5)
v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
v_box.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(v_box)
win.Show()


if __name__ == '__main__':
	app.MainLoop()

# if __name__ == '__main__':

