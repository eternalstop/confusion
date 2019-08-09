from xlrd import open_workbook
from xlwt import Workbook


relateDict = {
	'版权ID': '版权ID',
	'公司': '公司',
	'节目名': '节目名',
	'许可证号/批号': '许可证号/批号',
	'类型（大类）': '类型',
	'类型（细分）': '二级分类',
	'集数': '集数',
	'主演': '主演',
	'导演': '导演',
	'出品年份': '出品年份',
	'地区': '国家/地区',
	'版权开始日期': '版权开始日期',
	'版权结束日期': '版权结束日期',
	'节目登记时间': '节目登记时间',
	'授权书到位时间': '授权书到位时间',
	'介质到位时间': '介质到位时间',
	'可上线时间': '可上线时间',
	'收费期限': '收费期限',
	'使用条件': '使用条件',
	'版权链文件有无': '版权链文件有无'
}


def writeXls(data, name):
	workbook = Workbook(encoding='utf-8')
	sheet = workbook.add_sheet('Sheet1')
	sheet.write(1, 0, 'test')
	workbook.save(name)
	
	
def readXls(filename):
	workbook = open_workbook(filename)
	table = workbook.sheet_by_name('Sheet1')
	cols = table.ncols
	dataDict = {}
	for i in range(0, cols):
		tmpList = table.col_values(i)
		keyName = tmpList.pop(0)
		dataDict[keyName] = tmpList
	return dataDict
	
	
if __name__ == '__main__':
	infile = 'data/in190808.xlsx'
	data = readXls(infile)
	print(data)