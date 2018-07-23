#!/usr/local/python/bin/python
# -*- coding: utf-8 -*-
from urllib import request, parse
from bs4 import BeautifulSoup
from http import cookiejar
import json
import sys

head = {
    'Proxy-Connection': 'keep-alive',
    'Origin': 'http://172.25.116.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://172.25.116.7/iptvsmp/login.do',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cookie': 'UserName=dxty1;JSESSIONID=535C1205A6BF518201BE6D5D2EB0F61C;COOKIE.STAFF.TOKEN=3e1d35cede7140b0bb252749c7782c29'
}

base_url = 'http://172.25.116.7/iptvsmp/login.do'
tv_search_url = 'http://172.25.116.7/iptvsmp/content/seriesQuery.do'
movie_search_url = 'http://172.25.116.7/iptvsmp/content/programQuery.do'

login_parm = {
    'userName': 'dxty1',
    'password': 'dxty1'
}

tv_search_parm = {
	'name': 'name',
    'query_value': '',
    'vspid': '-1',
    'status': '-1',
    'stockoutflag': '-1',
    'labeltype': '-1',
    'contentproviderid': '-1',
}

movie_search_parm = {
    'fields': 'name',
    'fields_value': '',
    'vspid': '14',
    'status': '-1',
    'stockoutflag': '-1',
    'labeltype': '-1',
    'contentproviderid': '-1',
}

def get_cookie():
	post_data = parse.urlencode(login_parm).encode('utf8')
	cookie = cookiejar.CookieJar()
	handler = request.HTTPCookieProcessor(cookie)
	opener = request.build_opener(handler)
	req1 = request.Request(url=base_url, data=post_data, headers=head)
	response = opener.open(req1)
	temp_list = []
	for item in cookie:
		str = item.name + '=' + item.value
		temp_list.append(str)
	Cookie = ';'.join(temp_list)
	return Cookie

def get_tv_code(tv_name, vspid):
    tv_search_parm['query_value'] = tv_name
    tv_search_parm['vspid'] = vspid
    post_data = parse.urlencode(tv_search_parm).encode('utf8')
    req = request.Request(tv_search_url, headers=head, data=post_data)
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    result_list = json.loads(str(soup.contents[0]))['adaptedRows']
    if len(result_list) < 1:
    	return "Null"
    else:
    	code = eval(str(result_list[0]))['code']
    	return code


def get_movie_code(movie_name, vspid):
	movie_search_parm['fields_value'] = movie_name
	movie_search_parm['vspid'] = vspid
	post_data = parse.urlencode(movie_search_parm).encode('utf8')
	req = request.Request(movie_search_url, headers=head, data=post_data)
	html = request.urlopen(req).read()
	soup = BeautifulSoup(html, 'html.parser')
	result_list = json.loads(str(soup.contents[0]))['adaptedRows']
	if len(result_list) < 1:
		return "Null"
	else:
		code = eval(str(result_list[0]))['code']
		return code

def write_file(content):
	with open('result.txt', 'a+') as fd:
		fd.write(content + '\n')

if __name__ == '__main__':
	head['Cookie'] = get_cookie()
	with open('tv.txt', 'r') as fd:
		for tv_name in fd:
			if get_tv_code(tv_name.strip(), '14') == 'Null':
				tmp_str = tv_name.strip() + ': ' + get_tv_code(tv_name.strip(), '2')
				write_file(tmp_str)
			else:
				tmp_str = tv_name.strip() + ': ' + get_tv_code(tv_name.strip(), '14')
				write_file(tmp_str)
	with open('movie.txt', 'r') as fd:
		for movie_name in fd:
			if get_movie_code(movie_name.strip(), '14') == 'Null':
				tmp_str = movie_name.strip() + ': ' + get_movie_code(movie_name.strip(), '2')
				write_file(tmp_str)
			else:
				tmp_str = movie_name.strip() + ': ' + get_movie_code(movie_name.strip(), '14')
				write_file(tmp_str)