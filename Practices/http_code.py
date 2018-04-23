#!/usr/local/python/bin/python
# coding=utf-8
import requests
import time


def test_uri(uri):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
	          'Connection': 'keep-alive'}
	html = requests.head(uri, headers=header)
	return html.status_code


if __name__ == '__main__':
	flag = 1
	while True:
		try:
			test_url = r'http://182.106.140.232:18099/ccms/'
			status_code = test_uri(test_url)
			print("第 %s 次访问，这次访问状态码是 %s " % (str(flag), str(status_code)))
		except Exception as e:
			print("第 %s 访问失败   失败原因：" % flag + str(e).split()[-1].split("'")[0])
		time.sleep(60)
		flag += 1
