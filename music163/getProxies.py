#!/usr/local/python/bin/python
# conding=utf-8
import re
import requests
from bs4 import BeautifulSoup
import random


def getProxyPool():
	contents = []
	proxy_api = "https://www.kuaidaili.com/free/inha/{}/"
	url_list = [proxy_api.format(i) for i in [1, 100]]
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
	}
	for url in url_list:
		print(url)
		html = requests.get(url=url, headers=headers, timeout=30).text
		soup = BeautifulSoup(html, 'lxml')
		content = soup.find_all('td', attrs={'data-title': re.compile("IP|PORT|位置")})
		for i in range(0, len(content), 3):
			tmplist = content[i: i + 3]
			tmpdict = {
				'IP': re.split('<|>', str(tmplist[0]))[2],
				'PORT': re.split('<|>', str(tmplist[1]))[2],
				'LOCATION': re.split('<|>', str(tmplist[2]))[2]
			}
			contents.append(tmpdict)
		print(contents)
	return contents


def testProxy(proxy_pool):
	global proxy, status
	for eve in proxy_pool:
		proxy = {'http': eve['IP'] + ":" + eve['PORT']}
		try:
			r = requests.get(url="http://music.163.com/", proxies=proxy, timeout=5)
			status = r.status_code
			break
		except:
			status = 500
			continue
	return status, proxy
	

if __name__ == '__main__':
	ppool = getProxyPool()
	print(ppool)
	# print(testProxy(ppool))

