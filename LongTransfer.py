#!/usr/local/python3/bin/python
# coding=utf-8
import sys

from aip import AipOcr
import wx
import os
import pandas as pd


# path_name = r"D:\文档\ALi\long"
try:
    path_name = sys.argv[1]

    if os.path.isdir(path_name):
        file_list = os.listdir(path_name)
        for one_file in file_list:
            # xlsx to csv
            file_end = one_file.split(".")[1]
            if file_end == "xlsx":
                csv_name = path_name + "\\" + one_file.split(".")[0] + ".csv"
                new_name = path_name + "\\" + one_file.split(".")[0][0:13] + ".csv"
                if os.path.exists(new_name):
                    print("‘{}’   {}".format(new_name, "文件已存在,开始删除重新生成"))
                    os.remove(new_name)
                print("'{}'  {}  '{}'".format(one_file, "开始转换为csv并重命名", new_name))
                data_xls = pd.read_excel(path_name + "\\" + one_file, index_col=0)
                # print(csv_name)
                data_xls.to_csv(csv_name, encoding='utf-8')
                # rename
                os.renames(csv_name, new_name)
            else:
                continue
except:
    print("usage: transfer 完整目录路径")


