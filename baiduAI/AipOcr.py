#!/usr/local/python3/bin/python
# coding=utf-8
from aip import AipOcr


# 百度ocr-python文档：https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html

def get_txt(img):
	APP_ID = '11678143'
	API_KEY = 'HdFOqrkZGddbKAshqprIyGgp'
	SECRET_KEY = '5l5WuwO18xwzvhGTdh26HCDNaXIXShI3'
	my_client = AipOcr(appId=APP_ID, apiKey=API_KEY, secretKey=SECRET_KEY)

	options = {"detect_direction": "true", "probability": "false"}
	contents = my_client.basicAccurate(img, options)
	return contents


def get_file_content(img):
	with open(img, 'rb') as fp:
		return fp.read()


if __name__ == '__main__':
	image = r'D:\图片\Saved Pictures\5G11.png'
	results = get_txt(get_file_content(image))
	results_list = results['words_result']
	for i in results_list:
		print(i['words'])
