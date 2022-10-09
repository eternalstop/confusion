import math
import re
from urllib import request, parse
import requests
from bs4 import BeautifulSoup
import json
import datetime
# 请求头
header = {
    'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63',
}
# 请求接口
url = 'https://refinitiv.h5.incker.com/nike/getShoesList'
# 当前时间：year-mouth-day 2020-02-02
today = datetime.date.today()
# 当前年份
year = today.year


def send_msg(msg="测试内容，接口可能出错", shoesName="SH001", shoesCode="L7777-001", shoesDate="2022-2-22", shoesSize="42.0"):
    send_url = "http://www.pushplus.plus/send/"
    send_headers = {'Content-Type':'application/json'}
    msgContent = {
        "名字": shoesName,
        "型号": shoesCode,
        "发售日期": shoesDate,
        "码数范围": shoesSize,
        "参考内容": msg,
        }

    msg_data = {
        "token":"0f5b680c7cf549148dd18a12f2e6bc3d",
        "title":"上海001抽签提醒",
        "content":msgContent,
        "topic": "7700",
        "template":"json"
        }
    msg_body = json.dumps(msg_data).encode(encoding='utf-8')
    print(msg_body)
    send_result = requests.post(send_url,data=msg_body,headers=send_headers)
    print(send_result.status_code, send_result.content)


try:
    # 获取发售信息
    req = request.Request(url, headers=header)
    html = request.urlopen(req).read()
    soup = BeautifulSoup(html, "html.parser")
    info = json.loads(soup.text)
    # 判断当前是否请求成功并且有发售信息
    if info['code'] != 200 or len(info['shoesList']) < 1 or int(info['shoesList'][0]['button_type']) != 1:
        print('No Shoes')
        # pass
    else:
        # 判断发短信时间
        for shoes in info['shoesList']:
            shoes_date = datetime.date(year, int(shoes['shoes_date'].split('.')[0]), int(shoes['shoes_date'].split('.')[1]))
            result = shoes_date - today
            print(result)
            # 提前两天开始发短信，时间为10:00-18:00
            if result.days == 2:
                print('{}: {}+{}+{}+{}({})'.format(shoes['shoes_name'], shoes['shoes_code'], "王 亮", "34086811", "42.0", shoes['shoes_size']))
                msg = '{}: {}+{}+{}+{}({})'.format(shoes['shoes_name'], shoes['shoes_code'], "王 亮", "34086811", "42.0", shoes['shoes_size'])
                send_msg(msg=msg, shoesName=shoes['shoes_name'], shoesCode=shoes['shoes_code'], shoesDate=shoes['shoes_date'], shoesSize=shoes['shoes_size'])
            elif result.days > 2:
                # print("{}天后再发短信：{} + {}".format(result.days-2, shoes['shoes_name'], shoes['shoes_code']))
                continue
            else:
                # print("已过期 {} 天,无需发短信：{} + {}".format(abs(result.days), shoes['shoes_name'], shoes['shoes_code']))
                continue
except Exception as e:
    print("Null")
    # pass
