#!/usr/local/python/bin/python
# coding=utf-8
from __future__ import print_function
from IPy import IP
import sys


def check_ip(your_ip):
    ip_list = (
        '223.250.224.0/20', '114.63.32.0/21', '223.248.216.0/21', '114.61.248.0/21', '111.212.136.0/21',
        '223.249.40.0/21',
        '223.249.48.0/21', '114.62.32.0/21', '111.212.32.0/21', '223.249.208.0/22', '121.76.128.0/20',
        '121.76.144.0/20')
    for ip_tmp in ip_list:
        if your_ip in IP(ip_tmp):
            print(your_ip)

check_ip(sys.argv[1])
