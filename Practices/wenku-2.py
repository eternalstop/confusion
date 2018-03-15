#!/usr/local/python/bin/python
# coding=utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import time

opentions = webdriver.ChromeOptions()
opentions.add_argument('User-Agent="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"')
driver = webdriver.Chrome(chrome_options=opentions)
driver.get('https://wenku.baidu.com/view/8edce2e068dc5022aaea998fcc22bcd126ff4227.html')

continue_button = driver.find_element_by_xpath('//div[@class="flod-button"]')
continue_button.click()

for i in range(0, 7):
	html = driver.page_source
	soup = BeautifulSoup(html, 'lxml')
	soup_text = soup.find_all(class_='txt')
	with open(r'E:\leaf.txt', 'ab') as fd:
		for eme in soup_text:
			# print(eme.string)
			fd.write(str(eme.string).encode('utf-8'))
	continue_button = driver.find_element_by_xpath('//div[@class="sf-edu-wenku-id-pageNext flod-pager"]')
	continue_button.click()
	time.sleep(10)
print("结束")

