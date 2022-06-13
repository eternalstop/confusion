#!/usr/local/python3/bin/python
# coding=utf-8
import requests
import requests
import base64


# 百度ocr-python文档：https://cloud.baidu.com/doc/OCR/OCR-Python-SDK.html

# client_id 为官网获取的AK， client_secret 为官网获取的SK
def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=HdFOqrkZGddbKAshqprIyGgp&client_secret=5l5WuwO18xwzvhGTdh26HCDNaXIXShI3'
    try:
        response = requests.get(host)
        if response:
            return response.json()['access_token']
    except:
        return "error"


def get_content(path):
    """
    :api：图片文字识别高精度版
    :param path: 图片文件路径
    :return: 解析内容
    """
    # request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/doc_analysis_office"
    with open(path, 'rb') as fp:
        img = base64.b64encode(fp.read())
    params = {
        "image": img,
        "language_type": "CHN_ENG"
    }
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    try:
        response = requests.post(request_url, data=params, headers=headers)
        data = response.json()
    except:
        data = "error"
    return data


if __name__ == '__main__':
    file = r"D:\图片\QQ图片20210603182101.png"
    data = get_content(file)
    print(data)
