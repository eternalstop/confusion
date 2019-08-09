#!/usr/local/python/bin/python
# coding=utf-8
from optparse import OptionParser
import os
import sys


def opt():
    parser = OptionParser()
    parser.add_option("-H", "--Human",
                      dest="Human",
                      action="store_true",
                      default=False,
                      help="print sizes in human readable format")
    options, args = parser.parse_args()
    return options, args


def get_filename(dirs):
    l = os.walk(dirs)
    for path, dirs, files in l:
        for i in files:
            yield os.path.join(path, i)


def get_size(option, fl):
    size = os.path.getsize(fl)
    if not option:
        return str(size)
    else:
        if size >= 1024000000:
            return str(size/1024/1024/1024) + "G"
        elif size >= 1024000:
            return str(size/1024/1024) + "M"
        elif size >= 1024:
            return str(size/1024) + "K"
        else:
            return str(4.0) + "K"


def main():
    option, args = opt()
    try:
        paths = args[0]
    except IndexError:
        print("%s follow a directory" % __file__)
        sys.exit()
    for fn in get_filename(paths):
        size = get_size(option.Human, fn)
        print(size)


if __name__ == '__main__':
    main()
