#!/usr/local/python/bin/python
# coding = utf-8
from subprocess import PIPE, Popen


def getDmi():
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


def dmiDic():
    data = getDmi()
    dmi_dic = {}
    lines = parsDmi(data)
    dmi = dict([i.strip().split(': ')for i in lines])
    dmi_dic['vendor'] = dmi['Manufacturer']
    dmi_dic['Product'] = dmi['Product Name']
    dmi_dic['SN'] = dmi['Serial Number']
    return dmi_dic

if __name__ == '__main__':
    print(dmiDic())
