# _*_coding=utf-8_*_
import xmltodict
import uuid
import pandas as pd
import os
import re


def getxml(xmlfile='base.xml', evedict=None, sonpath=None):
	# 生成uuid
	evedict['TaskGUID'] = str(uuid.uuid1()).upper()
	evedict['ContentID'] = str(uuid.uuid1()).upper()
	evedict['FileGUID'] = str(uuid.uuid1()).upper()
	evedict['ClipGuid'] = str(uuid.uuid1()).upper()
	
	result = []
	if evedict is None:
		evedict = []
		
	# 解析xml例子，生成dict
	with open(xmlfile, 'rb') as fs:
		xml = fs.read()
	xmldict = xmltodict.parse(xml, encoding='UTF-8')
	
	# 判断简介字符串长度
	# print(len(evedict['Description']))
	# print(len(evedict['videosetfoucs']))
	if len(evedict['Description']) >= 200:
		evedict['Description'] = evedict['Description'][:190].join('......')
	if len(evedict['videosetfoucs']) >= 200:
		evedict['videosetfoucs'] = evedict['videosetfoucs'][:190].join('......')
	
	# dict字段替换
	xmldict['UnifiedContentDefine']['Header']['TaskCurrentGUID'] = evedict['TaskGUID']
	xmldict['UnifiedContentDefine']['ContentInfo']['ContentID'] = evedict['ContentID']
	for evefile in xmldict['UnifiedContentDefine']['ContentInfo']['ContentData']['ContentFile']['FileItem']:
		evefile['FileGUID'] = evedict['FileGUID']
		evefile['FileName']['FullPath'] = evedict['FullPath']
		evefile['FileLength'] = evedict['FileLength']
		evefile['FileOutpoint'] = evedict['FileOutpoint']
		evefile['RefOutpoint'] = evedict['RefOutpoint']
	
	for eveitem in xmldict['UnifiedContentDefine']['ContentInfo']['ContentData']['EntityData']['AttributeItem']:
		try:
			if evedict[eveitem['ItemCode']]:
				eveitem['Value'] = evedict[eveitem['ItemCode']]
		except:
			continue
	
	for evemeta in xmldict['UnifiedContentDefine']['ContentInfo']['MetaData']['Attributes']:
		for eveattr in evemeta['AttributeItem']:
			try:
				if evedict[eveattr['ItemCode']]:
					eveattr['Value'] = evedict[eveattr['ItemCode']]
			except:
				continue
	xmldict['UnifiedContentDefine']['ContentInfo']['MetaData']['Attributes'][0]['AttributeItem'][1]['Value'] = None
	xmldict['UnifiedContentDefine']['ContentInfo']['MetaData']['Attributes'][0]['AttributeItem'][0]['Value'] = '1'
	# dict解析成xml
	results = xmltodict.unparse(xmldict, pretty=True, encoding='UTF-8')
	
	# xml文件名称去特殊符号
	rep = {'.': '', ' ': '', '，': ''}
	rep = dict((re.escape(k), v) for k, v in rep.items())
	pattern = re.compile("|".join(rep.keys()))
	filename = pattern.sub(lambda m: rep[re.escape(m.group(0))], evedict['Name'])
	# print(filename)
	
	# xml写入文件，简单记录结果
	try:
		with open(sonpath + '\\' + filename + '.xml', 'w', encoding='UTF-8') as fs:
			fs.write(results)
		result.append(evedict['Name'] + ': Success')
	except:
		result.append(evedict['Name'] + ': Faild')
	return result


def getExcel(exfile):
	exList = []
	data = pd.read_excel(exfile, sheet_name=None)
	# print(len(data['Sheet1']['TaskGUID']))
	for flag in range(0, len(data['Sheet1']['TaskGUID'])):
		exDict = {}
		for eve in data.setdefault("Sheet1"):
			exDict[eve] = str(data['Sheet1'][eve][flag])
		exList.append(exDict)
	return exList


def mkdir(path):
	if not os.path.exists(path):
		os.mkdir(path)


if __name__ == '__main__':
	# 生成xml
	excelfile = r'聚精彩xml.xlsx'
	excelist = getExcel(excelfile)
	# print(excelist)
	for one in excelist:
		# 创建保存目录
		fatherdir = 'sonxml\\' + one['Name'].replace(one['Name'][-1], '')
		mkdir(fatherdir)
		
		# 获取格式和名称前缀
		# pre_fullpath = one['FullPath'].split('01')[0]
		pre_fullpath = one['FullPath'][:-4]
		# end_fullpath = one['FullPath'].split('01')[1]
		end_fullpath = one['FullPath'][-3:]
		name = one['Name'].replace(one['Name'][-1], '')
		for num in range(1, int(one['VolumnCount']) + 1):
			if num < 10:
				# one['FullPath'] = pre_fullpath + '0' + str(num) + end_fullpath
				one['FullPath'] = pre_fullpath + str(num) + end_fullpath
				one['Name'] = name + str(num)
				one['OrderNumber'] = str(num)
			else:
				one['FullPath'] = pre_fullpath + str(num) + end_fullpath
				one['Name'] = one['Name'] = name + str(num)
				one['OrderNumber'] = str(num)
			getxml(evedict=one, sonpath=fatherdir)
