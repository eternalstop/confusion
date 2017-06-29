# coding=utf-8
import re


s = '[F]内的文字新建一行秒自动对齐[C]右边的文字'
ptn = re.compile(r'\[([^]]+)\]([^[]+)')
ss = ''
t = ''
for x, y in ptn.findall(s):
    ss += ('{:<%d}' % len(y.decode('utf-8'))).format(x)
    t += y
print(ss, t, "\n")
