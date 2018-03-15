#!/usr/local/python/bin/python
# coding=utf-8

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# boswer = webdriver.Chrome()
# boswer.get("http://www.baidu.com")
#  elem = boswer.find_element_by_name('wd')
# elem.send_keys('python')
# elem.send_keys(Keys.RETURN)
# print(boswer.page_source)

opentions = webdriver.ChromeOptions()
opentions.add_argument('User-Agent="Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"')
driver = webdriver.Chrome(chrome_options=opentions)
driver.get('https://wenku.baidu.com/view/8edce2e068dc5022aaea998fcc22bcd126ff4227.html')

try:
	continue_button = driver.find_element_by_xpath('//div[@class="flod-button"]')
	continue_button.click()
except Exception as e:
	pass

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
try:
	soup_page = soup.find_all('div', class_='page_mark')[0].string
	page = int(soup_page.split('/')[1][:-1])
	next_times = page // 5
	next_judge = page % 5
	flag = 1
	if next_judge == 0:
		next_times = next_times - 1

	if next_times == 0:
		html = driver.page_source
		soup = BeautifulSoup(html, 'lxml')
		soup_text = soup.find_all(class_='txt')
		for eme in soup_text:
			print(eme.string)
			with open(r'E:\leaf.txt', 'w') as fd:
				fd.write(eme.string)
		print("结束")
	else:
		for i in range(0, next_times + 1):
			html = driver.page_source
			soup = BeautifulSoup(html, 'lxml')
			soup_text = soup.find_all(class_='txt')
			for eme in soup_text:
				print(eme.string)
				with open(r'E:\leaf.txt', 'w') as fd:
					fd.write(eme.string)
			if flag > next_times:
				break
			else:
				next_page = driver.find_element_by_xpath('//div[@class="sf-edu-wenku-id-pageNext flod-pager"]')
				next_page.click()
			flag += 1
			time.sleep(5)
except IndexError as e:
	pass
finally:
	html = driver.page_source
	soup = BeautifulSoup(html, 'lxml')
	soup_text = soup.find_all(class_='txt')
	for eme in soup_text:
		print(eme.string)
		with open(r'E:\leaf.txt', 'w') as fd:
			fd.write(eme.string)
	print("结束")

