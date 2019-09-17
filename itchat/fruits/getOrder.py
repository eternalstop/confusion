# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup
import re
import time


def getHtml(headers, url):
	html = requests.get(url=url, headers=headers, timeout=5).text
	soup = BeautifulSoup(html, 'lxml')
	return soup


def getAllOrder(url, phone):
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
		"Accept-Encoding": "gzip,deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
		"Connection": "keep-alive",
		"Host": "fzxzgy.dh.cx",
		"Referer": "http://fzxzgy.dh.cx",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
	}
	params = {
		"action": "home_query",
		"query_str": phone
	}
	response = requests.post(headers=headers, data=params, url=url)
	results = response.json()
	if results["count"] < 2:
		link_list = results["data"]
	else:
		link_list = [i["url"] for i in results["data"]]
	return link_list


def getInfo(link, phone):
	info_list = []
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
		"Accept-Encoding": "gzip,deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
		"Connection": "keep-alive",
		# "Host": "fzxzgy.dh.cx",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
	}
	for url in link:
		info_dict = {}
		soup = getHtml(url=url, headers=headers)
		compony = soup.find_all('span', attrs={"id": "result-company"})[0].a.contents[0]
		content = soup.find_all('ul', attrs={"class": "list-inline"})[0]
		all_info = content.find_all('li')
		for info in all_info:
			info_dict[info.strong.contents[0]] = info.contents[1].strip("：").strip()
		info_dict["链接"] = url
		info_dict["快递公司"] = compony
		info_dict["电话"] = phone
		info_list.append(info_dict)
		time.sleep(1)
	return info_list
		

def getLink(apilist):
	link_list = []
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
		"Accept-Encoding": "gzip,deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
		"Connection": "keep-alive",
		"Host": "fzxzgy.dh.cx",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
	}
	for url in apilist:
		soup = getHtml(headers=headers, url=url)
		panel_box = soup.find_all('div', class_="panel-box")
		if len(panel_box) > 2:
			num_li = panel_box[1].find_all('li', attrs={"class": re.compile('col-md-6 col-lg-4')})
			for eve in num_li:
				link_list.append(eve.a.get('href'))
		else:
			link_list.append(url + "/0/")
	return link_list


if __name__ == '__main__':
	# test_link = ['http://fzxzgy.dh.cx/c2d52/18655660717/0']
	check_api = "http://apis.dh.cx/query/json"
	home_url = "http://fzxzgy.dh.cx/"
	phonenum = '18655660717'
	all_api = getAllOrder(home_url, phonenum)
	all_link = getLink(all_api)
	# print(all_link)
	results = getInfo(all_link, phonenum)
	print(results)
