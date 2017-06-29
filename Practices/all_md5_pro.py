#!/usr/local/python/bin/python
# coding=utf-8

"""1.计算某个目录下每个文件的md5sum
   2.计算某个目录的md5sum
   3.找到目录中内容相同的文件
   4.计算整个目录的文件大小
   注：第四题，使用python处理文件元
   信息（os.path.getsize()），
   脚本接受-H选项，把文件大小加上适当的单位。"""

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


def file_md5(top_dir):
    a = os.walk(top_dir)
    for p, d, f in a:
        for b in f:
            fn = os.path.join(p, b)
            md5 = md5_sum(fn)
            yield "%s %s" % (md5, fn)


def get_dic(top_dir):
    md5_dic = {}
    a = os.walk(top_dir)
    for p, d, f in a:
        for b in f:
            fn = os.path.join(p, b)
            md5 = md5_sum(fn)
            if md5 in md5_dic:
                md5_dic[md5].append(fn)
            else:
                md5_dic[md5] = [fn]
    return md5_dic

if __name__ == '__main__':
    md5dic = get_dic(sys.argv[1])
    for k, v in md5dic.items():
        if len(v) > 1:
            print(k, v)
# if __name__ == '__main__':
#    lines = ''
#    try:
#        topdir = sys.argv[1]
#    except IndexError:
#        print("%s follow a dir" % __file__)
#        sys.exit()
#    gen = file_md5(topdir)
#    for i in gen:
#        lines += i + "\n"
#    print(hashlib.md5(lines).hexdigest())
#        print(i)


# l = os.walk(sys.argv[1])
# for dp, dn, fn in l:
#   for i in fn:
#        full_name = os.path.join(dp, i)
#        fn_md5 = md5_sum(full_name)
#        print(fn_md5 + "  " + i)
