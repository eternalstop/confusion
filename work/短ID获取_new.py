#!/usr/local/python/bin/python
# coding=utf-8
from bs4 import BeautifulSoup
from urllib import request, parse


def getid(vodcmsid):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
	          'Connection': 'keep-alive'}
	URL = 'http://125.88.99.8:8082/EPG/jsp/sysoperation/queryVODIDbyName.jsp'
	form = {
		"vodname1": "",
		"vodcmsid": vodcmsid,
		"vodid": ""
	}
	form = parse.urlencode(form).encode('utf-8')
	try:
		# html=urllib2.urlopen(urllib2.Request(URL, urllib.urlencode(form))).read().decode("gbk").encode("utf-8")
		req = request.Request(URL, headers=header, data=form)
		html = request.urlopen(req).read()
		soup = BeautifulSoup(html, "html.parser")
		return soup.form.contents[5].contents[3].contents[3].string
	except:
		return "Null"


if __name__ == '__main__':
	with open(r'output.txt', 'w') as fd:
		a=[]
		text=open('list.txt', 'r').readlines()
		total=len(text)
		count=0
		for i in text:
			if not i:
				continue
			count=count+1
			i=i.replace('\n', '')
			if getid(i).strip() == "Null":
				print('This vodcmsid(%s) connot get short id!' % i)
				fd.write(i + '\n')
				continue
			else:
				print("(%s/%s)" % (count, total))
				print(getid(i).strip())
				# a.append(getid(i).replace(" ", "")+'\n')
				fd.write(getid(i).strip() + '\n')
