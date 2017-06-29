#!/usr/local/python/bin/python
# conding=utf-8
from math import sqrt

for i in range(99, 0, -1):
    root = sqrt(i)
    if root == int(root):
        print(i)
        break
