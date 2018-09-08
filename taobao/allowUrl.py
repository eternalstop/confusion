#!/usr/local/python/bin/python
# coding=utf-8
"""
获取淘宝可用爬虫爬取的url，返回一个字典
{'搜索引擎': [url, ...],...}
{'Baiduspider': [article, ...],...}
"""
from urllib import request
from bs4 import BeautifulSoup


def getAllow():
	robotsUrl = 'https://www.taobao.com/robots.txt'
	header = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
		'Accept': 'text/html',
		'Connection': 'keep-alive',
	}

	req = request.Request(robotsUrl, headers=header)
	html = request.urlopen(req).read()
	soup = BeautifulSoup(html, "html.parser")
	soup_list = str(soup).splitlines(keepends=False)
	tempList = soup_list[:]
	[tempList.remove(i) for i in soup_list if "Disallow" in i]
	[tempList.remove(i) for i in soup_list if "*" in i]
	[tempList.remove(i) for i in tempList if len(i) < 1]
	allowDict = {}
	for x in range(len(tempList)):
		if tempList[x].startswith("User"):
			allowDict[tempList[x].split(":")[1].strip()] = []
			flag = x
		else:
			allowDict[tempList[flag].split(":")[1].strip()].append(tempList[x].split("/")[1].strip())

	return allowDict


