# _*_coding:utf-8_*_
from lxml import etree
import requests
# import time
import pymysql
from bs4 import BeautifulSoup
import re
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
	global status, proxy
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
		with open('error.txt', 'a') as f:
			f.write(urls)
			f.write('\n')
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
	ppool = getProxyPool()
	emotion = ['伤感', '治愈', '放松', '孤独', '感动', '兴奋', '快乐', '安静', '思念']
	# emotion = ['怀旧', '清新', '浪漫', '性感', '伤感', '治愈', '放松', '孤独', '感动', '兴奋', '快乐', '安静', '思念']
	# all_url = totalPage(emotion)
	all_url = ['http://music.163.com/discover/playlist/?order=hot&cat=浪漫&limit=35&offset=945']
	for eve_url in all_url:
		status, proxies = testProxy(ppool)
		return_data = getData(eve_url, proxies)
		print(return_data)
		# break

