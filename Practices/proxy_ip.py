#!/usr/local/python/bin/python
# coding=utf-8
import time
from urllib import request
from bs4 import BeautifulSoup
from json import loads

start = time.clock()
head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.84 Safari/537.36'
}

api_url = "http://www.j4.com.tw/james/remoip/"
req = request.Request(api_url, headers=head)
respone = request.urlopen(req)
html = respone.read()
soup = BeautifulSoup(html, 'lxml')
result = soup.find('div')
ip = result.contents[2].split('：')[1]
print("您的电脑IP是： %s" % ip)
check_ip_api = "http://www.chacuo.net/?m=ip&act=f&t=1&ip=" + ip
check_req = request.Request(check_ip_api, headers=head)
check_data = request.urlopen(check_req)
dic_data = loads(check_data.read())
country = dic_data['data']['country']
city = dic_data['data']['city']
isp = dic_data['data']['isp']
print("您的IP来自 %s%s%s" % (country, city, isp))

