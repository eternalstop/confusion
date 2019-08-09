import skvideo.io
import os
from xlrd import open_workbook
from xlutils.copy import copy

filelist = []


def get_files(path):
	exceptList = ['$RECYCLE.BIN', '8b6c2deb74629d6ce1de4183', 'System Volume Information', 'Youku Files', 'qqpcmgr_docpro']
	dirlist = os.listdir(path)
	try:
		for file in dirlist:
			if file in exceptList:
				continue
			
			filepath = os.path.join(path, file)
			if os.path.isfile(filepath):
				filelist.append(filepath)
			else:
				get_files(filepath)
		return filelist
	except:
		return "Error"
	
	
def get_durations(file):
	try:
		data = skvideo.io.ffprobe(file)
		if '@duration' in data['video'].keys():
			return data['video']['@duration'].split(".")[0]
		else:
			return data['audio']['@duration'].split(".")[0]
	except:
		return "error"
		

if __name__ == '__main__':
	# i = 0
	# path = r'H:\\'
	# rb = open_workbook(path + '\\' + 'result.xls')
	# rs = rb.sheet_by_index(0)
	# wb = copy(rb)
	# ws = wb.get_sheet(0)
	# get_files(path)
	# for f in filelist:
	# 	print(f + ":" + get_durations(f))
	# 	ws.write(i, 0, f)
	# 	ws.write(i, 1, get_durations(f))
	# 	i += 1
	# wb.save(path + '\\' + 'result.xls')
	print('2'.isdigit())