# -*- coding: utf-8 -*-
import urllib,urllib2,sys
from bs4 import BeautifulSoup
reload(sys)   
sys.setdefaultencoding('utf8')  


def getid(vodcmsid):
	URL='http://125.88.99.8:8082/EPG/jsp/sysoperation/queryVODIDbyName.jsp'
	form={
		"vodname1":"",
		"vodcmsid":vodcmsid,
		"vodid":""
	}

	html=urllib2.urlopen(urllib2.Request(URL,urllib.urlencode(form))).read().decode("gbk").encode("utf-8")
	soup=BeautifulSoup(html,"html.parser")
	#print soup.form.contents[5].contents[3].contents[1].string
	return soup.form.contents[5].contents[3].contents[3].string
	#print soup.form.contents[5].contents[3].contents[5].string

#print getid("10000100000000010000000004636066")
fp=open('outupt.txt','w')
a=[]
text=open('list.txt', 'r').readlines()
total=len(text)
count=0
for i in text:
	count=count+1
	i=i.replace('\n','')
	#print i
	print "(%s/%s)"%(count,total)
	a.append(getid(i).replace(" ","")+'\n')
fp.writelines(a)



