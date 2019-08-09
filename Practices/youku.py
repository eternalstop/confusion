#!/usr/bin/python
# coding=utf-8
import re
import urllib
import json


def get_html(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html


def get_video(index_html):
	# reg = r'http://v.qq.com/cover/.+?\.html'
	reg = r'href="//v.youku.com/v_show/.+?\.html" data-from'
	urlre = re.compile(reg)
	urllist = re.findall(urlre, index_html)
	return urllist


def get_play(play_html):
	reg = r'"U":"http://.+?\.[flv|mp4]"'
	urlre = re.compile(reg)
	playlist = re.findall(urlre, play_html)
	return playlist


# html = get_html("http://v.youku.com/v_show/id_XMjk4ODAyMzIyOA==.html?" +
#                "spm=a2htv.20009910.m_86852.5~5!2~5~5~5~5~5~5!2~A")
# urllist = get_video(html)
# for videourl in urllist:
# 	videourl = "http:" + videourl.split()[0].split('"')[1]
# 	flvcdurl = "http://vpstream.5233game.com/parse_pc.php?url=" + videourl + "&format=super"
# 	videoPro = open('videoPro/urllist.txt', 'a')
# 	videoPro.write(flvcdurl)
# 	videoPro.write("\n")
# 	videoPro.close()


play_url = urllib.urlopen('http://vpstream.5233game.com/parse_pc.php?' +
                          'url=http://v.youku.com/v_show/id_XMjk4ODAyMzIyOA==.html&format=super')
play_json = json.load(play_url)['V']
for ulist in play_json:
	# print(ulist['U'])
	play_output = open('videoPro/playurl.txt', 'a')
	play_output.write(ulist['U'])
	play_output.write("\n")
	play_output.close()
