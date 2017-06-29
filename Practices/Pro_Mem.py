#!/usr/bin/python
# coding=utf-8
# 输出某个进程所占系统内存大小
# Write by Ali
from __future__ import division
import psutil
import sys

pid_list = list()
pro_list = psutil.pids()


def mem_total():
    total_mem = 0
    with open('/proc/meminfo') as memfd:
        for mem_lines in memfd:
            if mem_lines.startswith('MemTotal'):
                total_mem = mem_lines.split()[1]
                break
#            if mem_lines.startswith('MemFree'):
#                free = mem_lines.split()[1]
#                break
#    total_mem = "%.2f" % (int(total)/1024.0)
    return int(total_mem)


def pro_mem(pro):
    pro_total = 0
    for pid_1 in pro_list:
        if str(psutil.Process(pid_1).name()) == str(pro):
            pid_list.append(pid_1)
    # continue
    if pid_list == list():
        sys.exit()
    for pid_2 in pid_list:
        pid_path = "/proc/" + str(pid_2) + "/status"
        with open(pid_path) as memfd:
            for mem_lines in memfd:
                if mem_lines.startswith('VmRSS'):
                    pro_total += int(mem_lines.split()[1])
        memfd.close()
    print (str(pro).capitalize() + "usage memory percentage is " + "%.2f" % ((int(pro_total)/mem_total())*100) + "%")
