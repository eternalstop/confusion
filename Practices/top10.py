#!/usr/local/python/bin/python
# coding=utf-8
import os
import sys
import operator


def get_dic(dirs):
    l = os.walk(dirs)
    dic = {}
    for p, d, f in l:
        for i in f:
            fn_full = os.path.join(p, i)
            fn_size = os.path.getsize(fn_full)
            dic[fn_full] = fn_size
    return dic

if __name__ == "__main__":
    top_dic = get_dic(sys.argv[1])
    sorted_dic = sorted(top_dic.iteritems(), key=operator.itemgetter(1), reverse=True)
    for k, v in sorted_dic[:10]:
        print(k, "--->", v)
