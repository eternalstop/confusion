#!/bin/env python3
# coding=utf-8
import requests
import json
import time
import random


def send_msg(ball={'ball': {'red': [1, 7, 9, 10, 20, 30], 'blue': [12]}}):
    send_url = "http://www.pushplus.plus/send/"
    send_headers = {'Content-Type':'application/json'}
    now_time = time.strftime('%Y%m%d', time.localtime(time.time()))
    msgContent = {
        "期数": now_time,
        "红球": "，".join(ball["ball"]["red"],),
        "蓝球": ball["ball"]["blue"]
        }

    msg_data = {
        "token":"0f5b680c7cf549148dd18a12f2e6bc3d",
        "title":"双色球推荐",
        "content":msgContent,
        "topic": "7700",
        "template":"json"
        }
    msg_body = json.dumps(msg_data).encode(encoding='utf-8')
    # print(msg_body)
    send_result = requests.post(send_url,data=msg_body,headers=send_headers)
    print(send_result.status_code, send_result.content)


def play():
	blue_list = [i for i in range(1, 17)]
	red_list = [j for j in range(1, 33)]
	tmp_dic = {}
	ball_dic = {}
	red = random.sample(red_list, 6)
	blue = random.sample(blue_list, 1)
	tmp_dic['red'] = [str(i) for i in red]
	tmp_dic['blue'] = [str(j) for j in blue]
	ball_dic['ball'] = tmp_dic
	return ball_dic


if __name__ == "__main__":
    ball_dict = play()
    print(ball_dict)
    # send_msg(ball_dict)