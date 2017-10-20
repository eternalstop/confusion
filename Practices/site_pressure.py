# coding:utf8
# !/usr/bin/env python

import threading
import time
import urllib2

'''
class :RequestThread  请求URL
func :request_url(self) 创建各个线程任务
'''


class RequestThread(threading.Thread):
	def __init__(self, thread_name):
		threading.Thread.__init__(self)
		self.error_num = 0
		self.url_num = 0
		self.thread_name = thread_name

	def run(self):
		print("%s---time is %s " % (threading.currentThread(), time.ctime(),))
		time.sleep(10)
		self.request_url()

	# 单个线程的任务

	def request_url(self):
		try:
			file_name = open('urls.txt', 'r')
			for line in file_name.readlines():
				self.url_num += 1
				url = line.strip()
				html = urllib2.urlopen(url).read()
		except urllib2.URLError as e:
			print(e)
			self.error_num += 1


'''
func: start_thread(thread_num) 生成多个处理线程
int thread_num :传入并发的线程个数
return:
    time_total 多个并发进程完成一次循环所用时间
    error_num  请求失败的页面数
    url_num   请求的url数
'''


def start_thread(thread_num):
	time_start = time.time()
	threads = []
	for i in range(thread_num):
		thread = RequestThread('thread' + str(i))
		thread.setDaemon(True)
		threads.append(thread)

	for t in threads:
		t.start()

	for t in threads:
		t.join()
	time_end = time.time()
	time_total = time_end - time_start
	print("每个循环耗时%s秒" % (time_total))

	# 获取类属性
	error_num = thread.error_num
	url_num = thread.url_num
	return time_total, error_num, url_num


'''
func: work(work_num) 每个线程做同一个任务循环的次数
int work_num: 任务循环次数
int thread_num:需要并发的进程数
'''


def work(work_num, thread_num):
	time_all = 0
	i = 0
	while i < work_num:
		i += 1
		time_total, error_num, url_num = start_thread(thread_num)
		#        print time_total
		time.sleep(2)
		time_all = time_all + time_total
		print("第 %s 次循环结束" % i)

	print("*****************************************************")
	print("总共运行耗时:%f秒" % (time_all))
	print("错误数:%s" % (error_num))
	print("总计请求了%s个页面" % (work_num * thread_num * url_num))


if __name__ == "__main__":
	# thread_num,创建并发线程的数量
	thread_num = 10
	work_num = 2
	#    start_thread(thread_num)
	work(work_num, thread_num)
