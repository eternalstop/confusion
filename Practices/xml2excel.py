# _*_coding=utf-8_*_

from xml.etree import ElementTree
import xlrd
import xlwt
import re


# 读取xml
filepath = r'E:\QQReceive\叶问3.xml'
text=open(filepath, encoding='UTF-8').read()
text=re.sub(u"[\x00-\x08\x0b-\x0c\x0e-\x1f]+", u"", text)
root = ElementTree.fromstring(text)


print(len(root[2][1][0][0]))