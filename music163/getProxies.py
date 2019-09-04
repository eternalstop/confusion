#!/usr/local/python/bin/python
# conding=utf-8
import re
import requests
from bs4 import BeautifulSoup
import time


def getProxyPool():
	proxy_api = "https://www.kuaidaili.com/free/inha/{}/"
	url_list = [proxy_api.format(i) for i in range(1, 6)]
	contents = []
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
		"Accept-Encoding": "gzip,deflate,br",
		"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
		"Connection": "keep-alive",
		"Host": "www.kuaidaili.com",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
	}
	for url in url_list:
		try:
			html = requests.get(url=url, headers=headers, timeout=5).text
			soup = BeautifulSoup(html, 'lxml')
			# content = soup.find_all('td', attrs={'data-title': re.compile("IP|PORT|位置")})
			content = soup.tbody
			for evetr in content.find_all('tr'):
				tmplist = list(evetr)
				tmpdict = {
					'IP': re.split('<|>', str(tmplist[1]))[2],
					'PORT': re.split('<|>', str(tmplist[3]))[2],
					'LOCATION': re.split('<|>', str(tmplist[9]))[2],
					'TRYTIME': re.split('<|>', str(tmplist[13]))[2]
				}
				contents.append(tmpdict)
		except:
			continue
		time.sleep(3)
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
