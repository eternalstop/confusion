import itchat
from urllib import request
from bs4 import BeautifulSoup
import json
import datetime


def get_msg():
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

    try:
        # 获取发售信息
        req = request.Request(url, headers=header)
        html = request.urlopen(req).read()
        soup = BeautifulSoup(html, "html.parser")
        info = json.loads(soup.text)
        # json格式参考
        # info = {
        #     'code': 200,
        #     'shoesList':
        #         [
        #             {
        #                 'id': '244',
        #                 'shoes_name': 'AIR JORDAN 1 HI 85',
        #                 'shoes_code': 'BQ4422-100',
        #                 'shoes_size': '35.5-47.5',
        #                 'shoes_date': '2.10',
        #                 'shoes_order': '1',
        #                 'button_type': '1',
        #                 'create_time': '1612631242',
        #                 'update_time': '1612631242',
        #                 'del_flg': '0',
        #                 'button_name': '短信抽签',
        #                 'is_show': '是'
        #             },
        #             {
        #                 'id': '245',
        #                 'shoes_name': 'AIR JORDAN 14  LOW SP-ED',
        #                 'shoes_code': 'DC9857-200',
        #                 'shoes_size': '40.0-47.5',
        #                 'shoes_date': '2.11',
        #                 'shoes_order': '2',
        #                 'button_type': '1',
        #                 'create_time': '1612735571',
        #                 'update_time': '1612735571',
        #                 'del_flg': '0',
        #                 'button_name': '短信抽签',
        #                 'is_show': '是'
        #             }
        #         ]
        # }
        # 判断当前是否请求成功并且有发售信息
        if info['code'] != 200 or len(info['shoesList']) < 1 or int(info['shoesList'][0]['button_type']) != 1:
            msg = '无发售计划'
            # pass
        else:
            # 判断发短信时间
            for shoes in info['shoesList']:
                shoes_date = datetime.date(year, int(shoes['shoes_date'].split('.')[0]),
                                           int(shoes['shoes_date'].split('.')[1]))
                result = shoes_date - today
                # 提前两天开始发短信，时间为10:00-18:00
                if result.days == 2:
                    msg = '{}: {}+{}+{}+{}+{}({})'.format(
                        shoes['shoes_name'],
                        shoes['shoes_code'],
                        "姓名（单名中间需要加空格）",
                        "身份证前四后四", "同名信用卡前四后四",
                        "码数",
                        shoes['shoes_size']
                    )
                else:
                    msg = "{}天后再发短信".format(result.days - 2)
    except Exception as e:
        msg = "无发售计划"
        # pass
    return msg


# itchat.auto_login(hotReload=True)
# friendList = itchat.get_friends()
# send_message = get_msg()
# print(friendList)
# for friend in friendList:
    # 如果是演示目的，把下面的方法改为print即可
    # itchat.send(send_message % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
    # print(send_message % (friend['DisplayName'] or friend['NickName']), friend['UserName'])

