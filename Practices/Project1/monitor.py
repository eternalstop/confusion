# coding=utf-8
from __future__ import print_function
import time
import MySQLdb as mysql

db = mysql.connect(user="monitor", passwd="monitor", db="memory", host="192.168.1.178")
db.autocommit(True)
cur = db.cursor()


def getmem():
    f = open('/proc/meminfo')
    total = int(f.readline().split()[1])
    free = int(f.readline().split()[1])
    buffers = int(f.readline().split()[1])
    cache = int(f.readline().split()[1])
    mem_use = total - free - buffers - cache
    t = int(time.time())
    sql = 'insert into memory (memory,time) value (%s,%s)' % (mem_use / 1024, t)
    cur.execute(sql)
    #print(mem_use / 1024)
    # print 'ok'


while True:
    time.sleep(1)
    getmem()
