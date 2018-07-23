#!/usr/local/python/bin/python
# coding=utf-8
import pandas as pd
from urllib import request, parse
from bs4 import BeautifulSoup
import json
import sys
import os
import time


def getid(vodcmsid):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
	          'Connection': 'keep-alive'}
	URL = 'http://125.88.99.8:8082/EPG/jsp/sysoperation/queryVODIDbyName.jsp'
	form = {
		"vodname1": "",
		"vodcmsid": vodcmsid.strip(),
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
		print_str = "%s can not get short ID! 3秒后继续!\n" % vodcmsid
		print(print_str)
		with open("error.txt", "a+") as errfd:
			errfd.write(print_str)
		time.sleep(3)
		return "Null"


def get_relat(file):
	data = pd.read_excel(file, sheet_name=None)
	relat_dic = {}
	father_list = [k.strip() for k in list(data["子集"]["主集ID"])]
	sun_list = [j.strip() for j in list(data["子集"]["子集ID"])]
	for i in range(0, len(sun_list)):
		relat_dic[father_list[i]] = []

	for j in range(0, len(sun_list)):
		sun_short_id = getid(sun_list[j])
		relat_dic[father_list[j]].append({"mediaCode": sun_short_id})
		print("(%s/%s)" % (str(j + 1), str(len(sun_list))))
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
				name_list.append(eve_name.strip())

		if "图片名" in father_key:
			for eve_img in data["主集"][father_key]:
				img_list.append(eve_img)
	flag = 0
	for eve_father_id in [x.strip() for x in list(data["主集"]["内容/主ID"])]:
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


def mkdir(path):
	if not os.path.exists(path):
		os.mkdir(path)


if __name__ == '__main__':
	excel_file = r"E:\Codes\Python\confusion\work\2018-2-2\list-1.xlsx"
	save_path = excel_file.split("\\")[-1].split(".")[0]
	mkdir(save_path)
	print(os.getcwd() + "\\" + save_path + "\\")
	# excel_file = input("请输入完整的文件路径： ")
	# excel_file = sys.argv[1]
	if os.path.exists(excel_file):
		pass
	else:
		print("This excel file is not exist,Please check it and reload the program!")

	if len(sys.argv) > 2:
		print("Usage: Please follow complete path.Only one argument")
	else:
		# save_path = excel_file.split("\\")[-1].split(".")[0]
		# mkdir(save_path)
		# for i in excel_file.split("\\")[:-1]:
		# 	save_path += i + "\\"

		dic2 = getDic(excel_file)
		if len(dic2["data"]) > 10:
			for k in range(0, len(dic2["data"]) // 10 + 1):
				if (k + 1) * 10 >= len(dic2["data"]):
					dic3 = {"data": dic2["data"][k*10:len(dic2["data"])]}
					fin_json = json.dumps(dic3, indent=2, ensure_ascii=False)
					with open(os.getcwd() + "\\" + save_path + "\\" + "list-%s.json" % str(k + 1), "w+", encoding="UTF-8") as fd:
						fd.write(fin_json)
					break
				else:
					dic3 = {"data": dic2["data"][k*10:(k+1)*10]}
					fin_json = json.dumps(dic3, indent=2, ensure_ascii=False)
					with open(os.getcwd() + "\\" + save_path + "\\" + "list-%s.json" % str(k + 1), "w+", encoding="UTF-8") as fd:
						fd.write(fin_json)
		else:
			fin_json = json.dumps(dic2, indent=2, ensure_ascii=False)
			with open(os.getcwd() + "\\" + save_path + "\\" + "list-1.json", "w+", encoding="UTF-8") as fd:
				fd.write(fin_json)
	print("结束！")

