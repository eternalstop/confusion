# _*_ coding:utf-8 _*_
# from ModDb import DataBase

# url = "http://music.163.com/playlist?id=2533909508"
# db = pymysql.connect(host="localhost", user="root", passwd="lucky", db="music163",
	                     # charset="utf8")
# label_list = ['华语', '怀旧', '浪漫']
# cursor = db.cursor()

# select_sql = "SELECT ID FROM playlist WHERE playlist_url='%s'" % url
# label = ",".join(label_list)
# up_sql = "UPDATE playlist SET playlist_label='%s' WHERE playlist_url='%s'" % (label, url)
# cursor.execute(select_sql)
# db.commit()
# results = cursor.fetchall()
# if results:
# 	print("success")
# else:
# 	print("faild")
# db.close()


# url = "http://music.163.com/playlist?id=2533909508"
# label = ",".join(["华语", "浪漫", "怀旧"])
# up_sql = "UPDATE playlist SET playlist_label='%s' WHERE playlist_url='%s'" % (label, url)
# se_sql = "SELECT ID FROM playlist WHERE playlist_url='%s'" % url
# database = DataBase()
# database.update(up_sql)
# database.closeDb()

import re
testlist = [
	'<td data-title="IP">112.14.47.6</td>',
	'<td data-title="PORT">52024</td>',
	'<td data-title="位置">浙江省宁波市  移动</td>',
	'<td data-title="IP">221.6.139.154</td>',
    '<td data-title="PORT">9000</td>',
    '<td data-title="位置">中国 江苏省 常州市 联通</td>'
]

for i in range(0, len(testlist), 3):
	tmplist = testlist[i: i + 3]
	print(re.split('<|>', tmplist[2]))
	# print(tmplist)