# coding=utf-8
import os
import sys


def file_print(path):
    list_files = os.listdir(path)
    dirs = [i for i in list_files if os.path.isdir(os.path.join(path, i))]
    files = [i for i in list_files if os.path.isfile(os.path.join(path, i))]
    if dirs:
        for d in dirs:
            file_print(os.path.join(path, d))
    if files:
        for f in files:
            print (os.path.join(path, f))

file_print(sys.argv[1]) 