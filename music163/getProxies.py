#!/usr/local/python/bin/python
# conding=utf-8
import re
import requests
from bs4 import BeautifulSoup
import random


def getProxyPool():
	proxy_api = "https://www.kuaidaili.com/free/inha/{}"
	url_list = [proxy_api.format(i) for i in range(1, 6)]
	url = random.choice(url_list)
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
	}
	html = requests.get(url=url, headers=headers, timeout=30).text
	soup = BeautifulSoup(html, 'lxml')
	content = soup.find_all('td', attrs={'data-title': re.compile("IP|PORT|位置")})
	contents = []
	for i in range(0, len(content), 3):
		tmplist = content[i: i + 3]
		tmpdict = {
			'IP': re.split('<|>', str(tmplist[0]))[2],
			'PORT': re.split('<|>', str(tmplist[1]))[2],
			'LOCATION': re.split('<|>', str(tmplist[2]))[2]
		}
		contents.append(tmpdict)
	return contents
	
	
def getProxy(pool):
	while True:
		random_choice = random.choice(pool)
		proxies = {"http": random_choice["IP"] + ":" + random_choice['PORT']}
		status = testProxy(proxies)
		if status == 200:
			pool.remove(random_choice)
			# if len(pool) == 0:
			# 	pool = getProxyPool()
			break
		else:
			pool.remove(random_choice)
			if len(pool) == 0:
				pool = getProxyPool()
			continue
	return proxies


def testProxy(proxy):
	try:
		r = requests.get(url="http://music.163.com/", proxies=proxy, timeout=5)
		return r.status_code
	except:
		return 500


if __name__ == '__main__':
	proxy_pool = getProxyPool()
	proxy = getProxy(proxy_pool)
	print(proxy)