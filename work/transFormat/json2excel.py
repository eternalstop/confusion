import json
from xlrd import open_workbook
from xlutils.copy import copy


def json2xls(inFile, outFile='data/results.xls', flag=1):
	"""
	:param inFile: 需要转成excel的json文件
	:param outFile: 最后生成的excel文件名，包括路径
	:param flag: 从哪一列开始生成数据
	:return: 返回一个“Success”结果或者处理异常
	"""
	try:
		rb = open_workbook(outFile)
		# rs = rb.sheet_by_index(0)
		wb = copy(rb)
		ws = wb.get_sheet(0)
		
		with open(inFile, 'r', encoding='utf-8') as f:
			contents = f.read()
		
		dataDict = json.loads(contents)
		# print(dataDict['tabs'][0])
		
		ws.write(0, 0, 'coverBig')
		ws.write(0, 1, 'cover')
		ws.write(0, 2, 'title')
		ws.write(0, 3, 'clickType')
		ws.write(0, 4, 'clickParam')
		ws.write(0, 5, 'liveId')
		ws.write(0, 6, 'ContentType')
		
		for lives in dataDict['tabs']:
			for live in lives['data']:
				ws.write(flag, 0, live['coverBig'])
				ws.write(flag, 1, live['cover'])
				ws.write(flag, 2, live['title'])
				ws.write(flag, 3, live['clickType'])
				ws.write(flag, 4, live['clickParam'])
				ws.write(flag, 5, live['liveId'])
				ws.write(flag, 6, lives['name'])
				flag += 1
		wb.save(outFile)
		return "Success"
	except Exception as e:
		return e
	
	
def xls2json(inFile, outFile):
	try:
		tabs_list = []
		type_list = []
		work_book = open_workbook(inFile)
		sheet = work_book.sheets()[0]
		table_key = sheet.row_values(0)
		for x in range(1, sheet.nrows):
			row_dict = dict(zip(table_key, sheet.row_values(x)))
			if row_dict['ContentType'] not in type_list:
				type_list.append(row_dict['ContentType'])
				dict_tmp = {
					'name': row_dict['ContentType'],
					'data': []
				}
				tabs_list.append(dict_tmp)
		
		for data in tabs_list:
			for x in range(1, sheet.nrows):
				row_dict = dict(zip(table_key, sheet.row_values(x)))
				if row_dict['ContentType'] == data['name']:
					row_dict.pop('ContentType')
					data['data'].append(row_dict)
		
		final_dict = {
			'tabs': tabs_list,
			'areaCode': "32"
		}
		with open(outFile, 'w+', encoding='utf-8') as f:
			f.write(json.dumps(final_dict, indent=4, ensure_ascii=False))
		return "Success"
	except Exception as e:
		return e
	
	
if __name__ =='__main__':
	jsonFile = 'data/live1.json'
	outJson = 'data/outJson.json'
	excelFile = 'data/results.xls'
	print(json2xls(inFile=jsonFile, outFile=excelFile))
	# print(xls2json(inFile=excelFile, outFile=outJson))