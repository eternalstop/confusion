#!/usr/local/python/bin/python
# coding=utf-8
import os
import hashlib
import sys


def md5_sum(f):
    m = hashlib.md5()
    with open(f) as fd:
        while True:
            data = fd.read(4096)
            if data:
                m.update(data)
            else:
                break
    return m.hexdigest()

l = os.walk(sys.argv[1])
for dp, dn, fn in l:
    for i in fn:
        full_name = os.path.join(dp, i)
        fn_md5 = md5_sum(full_name)
        print(fn_md5 + "  " + i)
