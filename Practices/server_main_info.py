#!/usr/local/python/bin/python
# coding=utf-8

"""
收集主机信息：
主机名：hostname
IP地址：ip
操作系统版本：OS version
服务器厂商：vendor
服务器型号：product
服务器序列号：SN
CPU型号：cpu_mode
CPU核数：cpu_num
内存大小：memory
"""
from subprocess import PIPE, Popen


def getHostname():
    h_dic = {}
    p = Popen('hostname', stdout=PIPE)
    hname = p.stdout.read()
    h_dic['hostname'] = [hname]
    return h_dic


def getOs():
    os_list = []
    dic_os = {}
    with open('/etc/issue') as os_info:
        for line in os_info:
            os_list.append(line)
    dic_os['os'] = [os_list[0]]
    return dic_os


def dmiData():
    p = Popen(['dmidecode'], stdout=PIPE)
    data = p.stdout.read()
    return data


def parsDmi(data):
    lines = []
    line_in = False
    dmi_list = [i for i in data.split('\n') if i]
    for line in dmi_list:
        if line.startswith('System Information'):
            line_in = True
            continue
        if line_in:
            if not line[0].strip():
                lines.append(line)
            else:
                break
    return lines


def getDmi():
    data = dmiData()
    dmi_dic = {}
    lines = parsDmi(data)
    dmi = dict([i.strip().split(': ')for i in lines])
    dmi_dic['vendor'] = dmi['Manufacturer']
    dmi_dic['Product'] = dmi['Product Name']
    dmi_dic['SN'] = dmi['Serial Number']
    return dmi_dic


def getMem():
    total_mem = ''
    dic_mem = {}
    with open('/proc/meminfo') as memfd:
        for mem_lines in memfd:
            if mem_lines.startswith('MemTotal'):
                total_mem = mem_lines.split()[1]
                break
    dic_mem['memory'] = [str(int(total_mem)/1024) + ' ' + 'MB']
    return dic_mem


def getCpu():
    cpumod = ''
    cpucore = []
    dic_cpuinfo = {}
    with open('/proc/cpuinfo') as cpufd:
        for i in cpufd:
            if i.startswith('processor'):
                cpucore.append(i)
            if i.startswith('model name'):
                cpumod = i.split(':')[1]
    cpunum = len(cpucore)
    dic_cpuinfo['cpunum'] = [cpunum]
    dic_cpuinfo['cpumodel'] = [cpumod]
    return dic_cpuinfo


def getIfconfig():
    p = Popen('ifconfig', stdout=PIPE)
    data_all = p.stdout.read().split('\n\n')
    data_need = [i for i in data_all if i and not i.startswith('lo')]
    return data_need


def getIp(data):
    dic_need = {}
    for lines in data:
        line_list = lines.split('\n')
        devname = line_list[0].split()[0]
#        hwaddr = line_list[0].split()[-1]
        ipaddr = line_list[1].split()[1].split(':')[1]
        dic_need[devname] = [ipaddr]
        break
    return dic_need


if __name__ == "__main__":
    system_dic = {}
    hostname_dic = getHostname()
    os_dic = getOs()
    dmidecode_dic = getDmi()
    mem_dic = getMem()
    cpu_dic = getCpu()
    ip_data = getIfconfig()
    ip_dic = getIp(ip_data)
    system_dic.update(hostname_dic)
    system_dic.update(os_dic)
    system_dic.update(dmidecode_dic)
    system_dic.update(mem_dic)
    system_dic.update(cpu_dic)
    system_dic.update(ip_dic)
    print(system_dic)
