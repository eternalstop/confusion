# _*_coding=utf-8_*_
import xmltodict
import uuid
import pandas as pd
from xlrd import open_workbook
from xlutils.copy import copy
import jieba
from pypinyin import pinyin, Style
import re


def getxml(xmlfile='base.xml', excelist=None):
	result = []
	if excelist is None:
		excelist = []
	with open(xmlfile, 'rb') as fs:
		xml = fs.read()
	xmldict = xmltodict.parse(xml, encoding='UTF-8')
	if len(excelist) == 0:
		return 'Null'
	else:
		for evecont in excelist:
			# 判断简介字符串长度
			# print(len(evecont['Description']))
			# print(len(evecont['videosetfoucs']))
			if len(evecont['Description']) >= 200:
				evecont['Description'] = evecont['Description'][:190].join('......')
			if len(evecont['videosetfoucs']) >= 200:
				evecont['videosetfoucs'] = evecont['videosetfoucs'][:190].join('......')
			
			xmldict['UnifiedContentDefine']['Header']['TaskCurrentGUID'] = evecont['TaskGUID']
			xmldict['UnifiedContentDefine']['ContentInfo']['ContentID'] = evecont['ContentID']
			for evefile in xmldict['UnifiedContentDefine']['ContentInfo']['ContentData']['ContentFile']['FileItem']:
				evefile['FileGUID'] = evecont['FileGUID']
				evefile['FileName']['FullPath'] = evecont['FullPath']
				evefile['FileLength'] = evecont['FileLength']
				evefile['FileOutpoint'] = evecont['FileOutpoint']
				evefile['RefOutpoint'] = evecont['RefOutpoint']
			
			for eveitem in xmldict['UnifiedContentDefine']['ContentInfo']['ContentData']['EntityData']['AttributeItem']:
				try:
					if evecont[eveitem['ItemCode']]:
						eveitem['Value'] = evecont[eveitem['ItemCode']]
				except:
					continue
			
			for evemeta in xmldict['UnifiedContentDefine']['ContentInfo']['MetaData']['Attributes']:
				for eveattr in evemeta['AttributeItem']:
					try:
						if evecont[eveattr['ItemCode']]:
							eveattr['Value'] = evecont[eveattr['ItemCode']]
					except:
						continue
			xmldict['UnifiedContentDefine']['ContentInfo']['MetaData']['Attributes'][0]['AttributeItem'][1]['Value'] = None
			results = xmltodict.unparse(xmldict, pretty=True, encoding='UTF-8')
			
			# xml文件名称去特殊符号
			rep = {'.': '', ' ': '', '，': ''}
			rep = dict((re.escape(k), v) for k, v in rep.items())
			pattern = re.compile("|".join(rep.keys()))
			filename = pattern.sub(lambda m: rep[re.escape(m.group(0))], evecont['Name'])
			# print(filename)
			try:
				with open('xml\\' + filename + '.xml', 'w', encoding='UTF-8') as fs:
					fs.write(results)
				result.append(evecont['Name'] + ': Success')
			except:
				result.append(evecont['Name'] + ': Faild')
	return result


def getExcel(file):
	exList = []
	data = pd.read_excel(file, sheet_name=None)
	# print(len(data['Sheet1']['TaskGUID']))
	for flag in range(0, len(data['Sheet1']['TaskGUID'])):
		exDict = {}
		for eve in data.setdefault("Sheet1"):
			exDict[eve] = str(data['Sheet1'][eve][flag])
			exDict['TaskGUID'] = str(uuid.uuid1()).upper()
			exDict['ContentID'] = str(uuid.uuid1()).upper()
			exDict['FileGUID'] = str(uuid.uuid1()).upper()
			exDict['ClipGuid'] = str(uuid.uuid1()).upper()
		exList.append(exDict)
	return exList


def get1pinyin(instr, upper=False):
	agstr = []
	pylist = [i for i in jieba.cut(instr, cut_all=False)]
	for word in pylist:
		[agstr.append(j[0]) for j in pinyin(word, style=Style.FIRST_LETTER)]
		
	if upper:
		return ''.join(agstr).upper()
	else:
		return ''.join(agstr)


def writExcel(file):
	rb = open_workbook(file)
	wb = copy(rb)
	ws = wb.get_sheet(0)
	resDict = {}
	data = pd.read_excel(file, sheet_name='字段信息')
	for flag in range(0, len(data['影片名称'])):
		name = data['影片名称'][flag].replace(' ', '')
		py = get1pinyin(name, upper=True)
		resDict[data['影片名称'][flag]] = py
		ws.write(flag + 1, 1, name)
		ws.write(flag + 1, 2, py)
	wb.save(file)
	return resDict


if __name__ == '__main__':
	# 生成xml
	# excelfile = r'xml电影2.xlsx'
	# excelist = getExcel(excelfile)
	# print(getxml(excelist=excelist))
	
	# 生成首字母
	excelfile = r'videoList2.xls'
	print(writExcel(excelfile))
	# print(get1pinyin('提出了解决方案', upper=True))