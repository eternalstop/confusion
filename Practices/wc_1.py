#!/usr/local/python/bin/python
# coding=utf-8

import sys
import os

if len(sys.argv) == 1:
    data = sys.stdin.read()
else:
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Please follow a argument at %s!" % __file__)
        sys.exit()
    if os.path.exists(file_name):
        print("%s is not exist" % file_name)
        sys.exit()
    fd = open(sys.argv[1])
    data = fd.read()
    fd.close()

chars = len(data)
words = len(data.split())
lines = data.count('\n')

print("%(lines)s %(words)s %(chars)s" % locals())
