# -*- coding: utf-8 -*-

import json
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup

domain=['music.163.com']
discover_start_url = ['http://music.163.com/#/discover/playlist/?cat=']
playlist_start_url = ['http://music.163.com/#/playlist?id=']
keyword=['怀旧', '清新', '浪漫', '性感', '伤感', '治愈', '放松', '孤独' '感动', '兴奋', '快乐', '安静', '思念']

Cookie = {
	'iuqxldmzr_': 32,
	'_ntes_nnid': 'ab3f8070ee5d1d561bcc4410b43703af,1527050155650',
	'_ntes_nuid': 'ab3f8070ee5d1d561bcc4410b43703af',
	'__utmz': '94650624.1527050156.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
	'__f_': '1527156036724',
	'WM_TID': 'RhLKgOni0xuhx%2FzfWCxIO7UcO4DyOXjx',
	'mail_psc_fingerprint': '98f54c84f40073551f228bfb7de47b28',
	'UM_distinctid': '16444e505ab2e7-03a824eee1c78-47e1039-100200-16444e505ad24d',
	'vjuids': '-dbf4a310e.16444e50b20.0.22069f278f4d2',
	'vjlast': '1530164219.1530164219.30',
	'vinfo_n_f_l_n3': '7ef7259bd0408d42.1.0.1530164218687.0.1530164244042',
	'usertrack': 'ezq0pFtHEtFDN0+tB9hqAg==',
	'Province': '021',
	'City': '021',
	'_ga': 'GA1.2.233174814.1531384528',
	'_gid': 'GA1.2.11154915.1531384528',
	'__utmc': '94650624',
	'playerid': '10990632', 'NNSSPID': '9a78ab00a1c4401fbcc2c0e334edab89',
	'NTES_hp_textlink1': 'old',
	'WM_NI': '5XX06Thml2hbtb0xS4CIbO%2Fw9AgVIyHjS0omhvYf6vCtxTtN0GJrR3Yei4i%2BXuEmqqvOTK6Qfph96ZF6B1M9Tpa6Nsx78coDkTrhgHLKNPuZjeDyzZUSawXTA7YHYfBEMW4%3D',
	'WM_NIKE': '9ca17ae2e6ffcda170e2e6ee8fae41ae9b8ad8d180aaa7968cfc44b5b2badac964f59989b5f459f3b3aaaaea2af0fea7c3b92af78898d1b560acb3a4d3eb6ab8be0099d2408197aeb0ae7dfb9fa9b7cc738cb69dd1ee67acaa9787b57e81acb8b5f746f4998693d1399bbba7d5ec219cab8b8ef47bb6919cacb55ba6b0a8dab55286ea8ed2d03398b0afd7cd79bce9f884ee50a98cbe89e644909582b1f852aabb8c9af952978daf98db6083e997a9dc6e829b83b8b737e2a3',
	'__utma': '94650624.1046391035.1527050156.1531466144.1531468775.26',
	'JSESSIONID-WYYY': 'yvBjz%2FUGbNMG7iwYi%5C%2BxsYDDdEfzSaeTTuIW%2BqtbrtNxbz9ZjNyjxwbl1vT%5C3sfmdFlCpHrGNC8v0mP8lnuTEuF8%2B5Y2PPE71d7c8%2Fm2l7aFaQ1x4uOidXpxNrX2VMl%2BinzU60fSN0wYbIQDl2v%5CPapVHt9S4HqXG%2FgHOfjNc2gvskMT%3A1531471319622',
	'__utmb': '94650624.7.10.1531468775'
}

head = {
	'Host': 'music.163.com',
	'Proxy-Connection': 'keep-alive',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	# 'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
}


def get_playlist():
	playlist = []
	for label in keyword:
		curlurl = discover_start_url[0] + parse.quote(label)
		print(curlurl)
		req = request.Request(curlurl, headers=head)
		response = request.urlopen(req)
		html = response.read()
		# print(html)
		soup = BeautifulSoup(html, 'lxml')
		print(soup)
		# body_ul = soup.find_all('li', class_='m-cvrlst f-cb')
		# print(body_ul)
		# for li in body_ul:
		# 	playlist_id = li.find('div', class_='u-cover u-cover-1').find('a')
		# 	playlist_type = label
		# 	print(playlist_id)
		break


if __name__ == '__main__':
	get_playlist()