from urllib import request, parse
from bs4 import BeautifulSoup
from http import cookiejar

login_url = 'http://172.25.116.7/iptvsmp/login.do'

head = {
    'Proxy-Connection': 'keep-alive',
    'Origin': 'http://172.25.116.7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://172.25.116.7/iptvsmp/login.do',
    'Accept-Language': 'zh-CN,zh;q=0.9',
	}

login_parm = {
    'userName': 'dxty1',
    'password': 'dxty1'
	}

post_data = parse.urlencode(login_parm).encode('utf8')
cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
req1 = request.Request(url=login_url, data=post_data, headers=head)
response = opener.open(req1)
Cookie = []
for item in cookie:
	str = item.name + '=' + item.value
	Cookie.append(str)

Cookie.remove('domain_cook=0')
print(';'.join(Cookie))
