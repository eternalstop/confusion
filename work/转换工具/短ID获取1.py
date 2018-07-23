# -*- coding: utf-8 -*-
import urllib
import urllib2
import sys
from bs4 import BeautifulSoup
reload(sys)   
sys.setdefaultencoding('utf8')  


def getid(vodcmsid):
	URL='http://125.88.99.8:8082/EPG/jsp/sysoperation/queryVODIDbyName.jsp'
	form={
		"vodname1": "",
		"vodcmsid": vodcmsid,
		"vodid": ""
	}

	html=urllib2.urlopen(urllib2.Request(URL, urllib.urlencode(form))).read().decode("gbk").encode("utf-8")
	soup=BeautifulSoup(html, "html.parser")
	return soup.form.contents[5].contents[3].contents[3].string


# fp=open('outupt.txt', 'w')
# a=[]
# text=open('list.txt', 'r').readlines()
# total=len(text)
# count=0
# for i in text:
# 	count=count+1
# 	i=i.replace('\n', '')
# 	print "(%s/%s)" % (count, total)
# 	a.append(getid(i).replace(" ", "")+'\n')
# fp.writelines(a)

if __name__ == '__main__':
	with open(r'output.txt', 'w') as fd:
		a=[]
		text=open('list.txt', 'r').readlines()
		total=len(text)
		count=0
		for i in text:
			count=count+1
			i=i.replace('\n', '')
			print("(%s/%s)" % (count, total))
			# a.append(getid(i).replace(" ", "")+'\n')
			fd.write(getid(i) + '\n')
