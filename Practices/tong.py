#!/usr/local/python/bin/python
# coding=utf-8
import csv
import re
import requests


def picTest(file):
	results = {
		'200': [],
		'error': [],
		'other': []
	}

	with open(csvFile, 'r') as fp:
		for i in csv.reader(fp):
			try:
				url = re.findall(r'(https.*(\.png|\.jpeg|\.jpg|\.HEIC))', i[0])[0][0]
				code = requests.get(url).status_code
				if code == 200:
					results['200'].append(url)
				else:
					results['error'].append(url)
			except Exception as e:
				results['other'].append(url)
	return results


if __name__ == '__main__':
	csvFile = r'E:\Wchat\WeChat Files\www19920717\Files\qulang_images.csv'
	print(len(picTest(csvFile)['200']))
