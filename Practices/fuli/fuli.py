# coding=utf-8
import re
import requests
import csv
import collections
from bs4 import BeautifulSoup


def get_html(url):
    html = requests.get(url)
    return html.text


def get_link_list(base_html):
    reg = r'https://kaijiang.500.com/shtml/ssq/.+?.shtml'
    urlre = re.compile(reg)
    urllist = re.findall(urlre, base_html)
    return urllist[::-1]


def get_red(index_html):
    reg = r'[\d][\d][ ][\d][\d][ ][\d][\d][ ][\d][\d][ ][\d][\d][ ][\d][\d]'
    red_ball = re.findall(reg, index_html, re.I | re.M)
    if red_ball:
        return red_ball[0].split()


def get_blue(html):
    soup = BeautifulSoup(html, 'lxml')
    soup_text = soup.find('li', class_='ball_blue').text
    return soup_text


def w_csv(b_dict, file_name):
    with open(file_name, 'a+') as fd:
        writer2 = csv.writer(fd)
        for key in b_dict:
            writer2.writerow([key, b_dict[key]])


if __name__ == '__main__':
    flag = 1
    base_link = "https://kaijiang.500.com/shtml/ssq/03001.shtml"
    base_html = get_html(base_link)
    link_list = get_link_list(base_html)
    # print(link_list)
    dic_list = ['red0', 'red1', 'red2', 'red3', 'red4', 'red5', 'blue']
    for num in range(1, len(link_list), 1):
        for i in range(7):
            dic_list[i] = collections.OrderedDict()
        link = link_list[num]
        html = get_html(link)
        red_list = get_red(html)
        blue = get_blue(html)
        for i in range(7):
            if i < 6:
                # pass
                dic_list[i][num] = red_list[i]
                w_csv(dic_list[i], 'red%s.csv' % i)
            else:
                dic_list[i][num] = blue
                w_csv(dic_list[i], 'blue.csv')
        flag = + 1
        if flag == 3:
            break
