# _*_conding=utf-8_*_
import json
import os
from xlrd import open_workbook
from xlutils.copy import copy

nameList = []
dirname = 'video'
files = ['video/' + i for i in os.listdir('video')]

flag = 1
rb = open_workbook('results.xls')
rs = rb.sheet_by_index(0)
wb = copy(rb)
ws = wb.get_sheet(0)

for file in files:
	with open(file, 'r', encoding='utf-8') as f:
		contents = f.read()

	cdict = json.loads(contents)
	for video in cdict['content']['videos']:
		nameList.append(video['name'])
		ws.write(flag, 0, video['name'])
		flag += 1
		
wb.save('results.xls')
print(nameList)