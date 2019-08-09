#!/usr/local/python/bin/python
# conding=utf-8
import re
import requests
from bs4 import BeautifulSoup
import random


def getProxy(url):
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


def testProxy(proxy):
	try:
		r = requests.get(url="http://music.163.com/", proxies=proxy, timeout=5)
		return r.status_code
	except:
		return 500
	

if __name__ == '__main__':
	proxy_api = "https://www.kuaidaili.com/free/inha/{}"
	url_list = [proxy_api.format(i) for i in range(1, 6)]
	for url in url_list:
		print(getProxy(url))
		break
		
	# proxy_pool = getProxy()
	# print(proxy_pool)
	# while True:
	# 	random_ip = random.choice(proxy_pool)
	# 	proxies = {"http": random_ip}
	# 	status = testProxy(proxies)
	# 	if status == 200:
	# 		proxy_pool.remove(random_ip)
	# 		if len(proxy_pool) == 0:
	# 			proxy_pool = getProxy()
	# 		break
	# 	else:
	# 		proxy_pool.remove(random_ip)
	# 		if len(proxy_pool) == 0:
	# 			proxy_pool = getProxy()
	# 		continue
	# print(proxy_pool)
	# print(proxies)
