# _*_ coding:utf8 _*_
"""
使用方法:
	1.在主程序中实例化此类
	2.db = DataBaseClass() db.fetch_all("sql语句")
"""
import pymysql
import configparser
import os


config = configparser.ConfigParser()
file = os.path.split(os.path.realpath(__file__))[0] + r'\config'
config.read(file)
DBHOST = config.get("database", "host")
DBPORT = int(config.get("database", "port"))
DBNAME = config.get("database", "name")
DBUSER = config.get("database", "user")
DBPWD = config.get("database", "password")
DBCHAR = config.get("database", "charset")


class DataBase:
	def __init__(self):
		self._dbhost = DBHOST
		self._dbport = DBPORT
		self._dbname = DBNAME
		self._dbuser = DBUSER
		self._dbpwd = DBPWD
		self._dbchar = DBCHAR
		self._dbconn = self.connDb()
		if self._dbconn:
			self._dbcursor = self._dbconn.cursor()
	
	# Connect Database
	def connDb(self):
		try:
			conn = pymysql.connect(
				host=self._dbhost,
				port=self._dbport,
				user=self._dbuser,
				passwd=self._dbpwd,
				db=self._dbname,
				charset=self._dbchar,
			)
		except:
			conn = False
		return conn
	
	def fetchAll(self, sql):
		s_results = False
		if self._dbconn:
			try:
				self._dbcursor.execute(sql)
				s_results = self._dbcursor.fetchall()
			except:
				s_results = False
		return s_results
	
	def update(self, sql):
		u_results = False
		if self._dbconn:
			try:
				self._dbcursor.execute(sql)
				self._dbconn.commit()
				u_results = True
			except:
				u_results = False
		return u_results
	
	def closeDb(self):
		if self._dbconn:
			try:
				if type(self._dbcursor) == 'object':
					self._dbcursor.close()
				if type(self._dbconn) == 'object':
					self._dbconn.close()
			except:
				pass