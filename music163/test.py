# _*_ coding:utf-8 _*_
from ModDb import DataBase


url = "http://music.163.com/playlist?id=2533909508"
label = ",".join(["华语", "浪漫", "怀旧"])
up_sql = "UPDATE playlist SET playlist_label='%s' WHERE playlist_url='%s'" % (label, url)
se_sql = "SELECT ID FROM playlist WHERE playlist_url='%s'" % url
database = DataBase()
database.update(up_sql)
database.closeDb()

