#!/usr/local/python/bin/python
# coding=utf-8
from subprocess import PIPE, Popen


def getIfconfig():
    p = Popen('ifconfig', stdout=PIPE)
    data_all = p.stdout.read().split('\n\n')
    data_need = [i for i in data_all if i and not i.startswith('lo')]
    return data_need


def parsIfconfig(data):
    dic_need = {}
    for lines in data:
        line_list = lines.split('\n')
        devname = line_list[0].split()[0]
        hwaddr = line_list[0].split()[-1]
        ipaddr = line_list[1].split()[1].split(':')[1]
        dic_need[devname] = [hwaddr, ipaddr]
    return dic_need


if __name__ == '__main__':
    datas = getIfconfig()
    print(parsIfconfig(datas))
