from lxml import etree
import requests
# import time
import pymysql
from urllib import parse
from bs4 import BeautifulSoup
import execjs
import re
import random


def testProxy(proxy):
	try:
		r = requests.get(url="http://music.163.com/", proxies=proxy, timeout=5)
		return r.status_code
	except:
		return 500


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


def totalPage(emotions):
	url_list = []
	base_url = 'http://music.163.com/discover/playlist/?order=hot&cat={}&limit=35&offset={}'
	for e in emotions:
		for i in range(0, 1300, 35):
			url = base_url.format(e, i)
			url_list.append(url)
	return url_list


def getData(urls, proxy):
	preUrl = 'https://music.163.com'
	headers = {
		'referer': 'https://music.163.com/',
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	}
	try:
		r = requests.get(urls, headers=headers, proxies=proxy)
		print(r.text)
		html = etree.HTML(r.text)
		MFlist = html.xpath("//p[@class='dec']/a/text()")
		MFurl = html.xpath("//p[@class='dec']/a/@href")
		LisNum = html.xpath("//span[@class='nb']/text()")
		label = urls.split("&")[1].split("=")[1]
		for i in range(len(MFlist)):
			if MFlist[i] == '' or MFurl[i] == '' or LisNum[i] == '':
				continue
			listDb(MFlist[i], preUrl + MFurl[i], LisNum[i], label)
		return "Success"
	except:
		return "Error"


def listDb(name, url, hot, label):
	# connect mysql
	# db = pymysql.connect(host="localhost", user="root", passwd="lucky", db="music163",
	#                      charset="utf8")
	db = pymysql.connect(host="10.102.27.125", user="music", passwd="tysx@tv189", db="music163",
	                     charset="utf8")
	# get cursor by cursor()
	cursor = db.cursor()
	# SQL command
	insert_sql = "INSERT INTO playlist(playlist_name, playlist_url, playlist_hot, playlist_label) VALUES ('%s', '%s', '%s', '%s')" % (
		name, url, hot, label)
	select_sql = "SELECT ID FROM PLAYLIST WHERE playlist_url='%s'" % url
	cursor.execute(select_sql)
	results = cursor.fetchall()
	if results:
		pass
	else:
		try:
			cursor.execute(select_sql)
			results = cursor.fetchall()
			if results:
				pass
			else:
				cursor.execute(insert_sql)
				db.commit()
		except:
			pass
	db.close()


if __name__ == '__main__':
	emotion = ['怀旧', '清新', '浪漫', '性感', '伤感', '治愈', '放松', '孤独', '感动', '兴奋', '快乐', '安静', '思念']
	all_url = totalPage(emotion)
	proxy_pool = getProxyPool()
	proxies = getProxy(proxy_pool)
	for eve_url in all_url:
		return_data = getData(eve_url, proxies)
		print(return_data)
		break
