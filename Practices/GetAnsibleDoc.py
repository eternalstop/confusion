#!/usr/local/python/bin/python
# _*_coding:UTF-8_*_
"""
从http://www.ansible.com.cn/index.html#爬取整个Ansible中文权威指南
"""
from bs4 import BeautifulSoup
import requests

catalog = {}

Header = {
	"Host": "www.ansible.com.cn",
	"Connection": "keep-alive",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Referer": "http://www.ansible.com.cn/docs/intro.html",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Upgrade-Insecure-Requests": "1"
}

URL = "http://www.ansible.com.cn/index.html"

# req = request.Request(URL, headers=Header)
# html = request.urlopen(req).read()
html = requests.get(url=URL, headers=Header).content
soup = BeautifulSoup(html, "lxml")
soup_text = soup.find('div', class_='toctree-wrapper compound').find_all('a')
for a in soup_text:
	catalog[a.get_text()] = a.get('href')
	
print(catalog)


