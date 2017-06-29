#!/usr/local/python/bin/python
# coding=utf-8

from subprocess import PIPE, Popen

p = Popen(['dmidecode'], stdout=PIPE)
data = p.stdout
lines = []
dmi = {}
a = True
while a:
    line = data.readline()
    if line.startswith("System Information"):
        while True:
            line = data.readline()
            if line == "\n":
                a = False
                break
            else:
                lines.append(line)

dmi_dic = dict([i.strip().split(':') for i in lines])
dmi['Serial'] = dmi_dic['Serial Number']
dmi['Product'] = dmi_dic['Product Name']
dmi['Manufacturer'] = dmi_dic['Manufacturer']
print(dmi)
