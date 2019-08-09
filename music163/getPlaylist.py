from lxml import etree
import requests
# import time
import pymysql
from urllib import parse
from bs4 import BeautifulSoup
import execjs
import re
import random

data = {
	"tqsl": '50',
	"radio": "radio",
	"submit": "提  取"
}

proxy_api = "http://www.66ip.cn/mo.php?"
proxy_api = proxy_api + parse.urlencode(data, encoding="gb2312")


def getHtml(url, cookie=None):
	headers = {
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9",
		"Cache-Control": "max-age=0",
		"Connection": "keep-alive",
		"Host": "www.66ip.cn",
		"Referer": "http://www.66ip.cn/pt.html",
		"Upgrade-Insecure-Requests": "1",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
	}
	html = requests.get(url=url, headers=headers, timeout=30, cookies=cookie).content
	return html


def executeJS(js_func_string, arg):
	ctx = execjs.compile(js_func_string)
	func_name = js_func_string.split()[1].split("(")[0]
	return ctx.call(func_name, arg)


def parseCookie(string):
	string = string.replace("document.cookie='", "")
	clearance = string.split(';')[0]
	return {clearance.split('=')[0]: clearance.split('=')[1]}


def testProxy(proxy):
	try:
		r = requests.get(url="http://music.163.com", proxies=proxy, timeout=5)
		return r.status_code
	except:
		return 500


def getProxy():
	first_html = getHtml(proxy_api)
	js_func = ''.join(re.findall(r'(function .*?)</script>', str(first_html)))
	js_arg = ''.join(re.findall(r'setTimeout\(\"\D+\((\d+)\)\"', str(first_html)))
	js_func = js_func.replace('eval("qo=eval;qo(po);")', 'return po')
	cookie_str = executeJS(js_func, js_arg)
	cookie = parseCookie(cookie_str)
	fin_html = getHtml(proxy_api, cookie=cookie)
	soup = BeautifulSoup(fin_html, "lxml")
	# print(soup)
	temp_res = soup.find("p").get_text()
	ip_list = temp_res.split()[:-6]
	return ip_list


def totalPage(emotions):
	url_list = []
	base_url = 'http://music.163.com/discover/playlist/?order=hot&cat={}&limit=35&offset={}'
	for e in emotions:
		for i in range(0, 1300, 35):
			url = base_url.format(e, i)
			url_list.append(url)
	return url_list


def getData(urls, proxy):
	preUrl = 'http://music.163.com'
	headers = {
		'Referer': 'http://music.163.com/',
		'Host': 'music.163.com',
		# 'User-Agent': 'Mozilla/5.0 (X11: Linux *86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	}
	print(proxy)
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
		return "Error"


def listDb(name, url, hot, label):
	# connect mysql
	db = pymysql.connect(host="localhost", user="root", passwd="lucky", db="music163",
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
	proxy_pool = getProxy()
	for eve_url in all_url:
		while True:
			if len(proxy_pool) == 0:
				proxy_pool = getProxy()
			random_ip = random.choice(proxy_pool)
			proxies = {"http": random_ip}
			status = testProxy(proxies)
			if status == 200:
				return_data = getData(eve_url, proxies)
				if return_data == "Success":
					proxy_pool.remove(random_ip)
					break
				else:
					proxy_pool.remove(random_ip)
					continue
			else:
				proxy_pool.remove(random_ip)
				continue

