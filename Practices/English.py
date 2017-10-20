#!/usr/bin/python
# coding=utf-8
import re
import urllib


def get_html(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html


def get_img(index_html):
	# reg = r'href="//v.youku.com/v_show/.+?\.html" data-from'
	reg = r'href="http://keben.100qingda.com/.+?\.jpg"'
	urlre = re.compile(reg)
	urllist = re.findall(urlre, index_html)
	return urllist


html = get_html("http://www.qingda100.cn/show/2227.html")
img_url = get_img(html)
x = 0
for ulist in img_url:
	# print(ulist.split('"')[1])
	ulist = ulist.split('"')[1]
	urllib.urlretrieve(ulist, r'C:\Users\ty\Documents\English class\major 5\%s.jpg' % x)
	x += 1
	# print(ulist['U'])
	# play_output = open('output/playurl.txt', 'a')
	# play_output.write(ulist['U'])
	# play_output.write("\n")
	# play_output.close()
