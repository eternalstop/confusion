#!/usr/local/python/bin/python
# coding=utf-8
"""
输出杨辉三角
<<<<<<< HEAD
"""


def triangles():
    line = [1]
    while True:
        yield line
        line = [sum(i) for i in zip([0]+line, line+[0])]


for j in triangles():
    print(j)
    if len(j) > 10:
        break
=======
"""
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9
