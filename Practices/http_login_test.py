# coding=utf-8

import sys
import time
import thread
import httplib
import urllib
import random
import uuid
import logging
import traceback

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='测试脚本日志.log',
                    filemode='w')


def log_uncaught_exceptions(exception_type, exception, tb):
    logging.critical(''.join(traceback.format_tb(tb)))
    logging.critical('{0}: {1}'.format(exception_type, exception))


sys.excepthook = log_uncaught_exceptions


# 网关地址
addr = "172.18.2.4"
port = 8080
thread_count = 15
# 单次并发数量
request_interval = 10
# 请求间隔(秒)
test_count = sys.maxsize
# sys.maxsize  # 指定测试次数


param_list = [{"login": "user1",
               "password": "qwe12"
               }]

now_count = 0
lock_obj = thread.allocate()


def send_http():
    global now_count
    http_clt = None
    try:
        for user in param_list:
            tmp_user = user["login"]
            if tmp_user.strip() == '':
                tmp_user = str(uuid.uuid1()) + str(random.random())
            print(tmp_user)
            params = urllib.urlencode({"operationData": [{"login": tmp_user, "password": user["password"]}]})
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

            http_clt = httplib.HTTPConnection(addr, port, timeout=5)
            http_clt.request("POST", "/simple/spider.task.distribute", params, headers)

            response = http_clt.getresponse()
            print('发送数据: ' + params)
            print('返回码: ' + str(response.status))
            print('返回数据: ' + response.read())

            logging.info('发送数据: ' + params)
            logging.info('返回码: ' + str(response.status))
            logging.info('返回数据: ' + response.read())
            # print response.getheaders() #获取头信息
            sys.stdout.flush()
            now_count += 1
    except Exception as e:
        print(e)
        logging.info(e)
    finally:
        if http_clt:
            http_clt.close()


def test_func(run_count):
    global now_count
    global request_interval
    global lock_obj
    cnt = 0
    while cnt < run_count:
        lock_obj.acquire()
        print('')
        print('***************************请求次数:' + str(now_count) + '*******************************')
        print('Thread:(%d) Time:%s\n' % (thread.get_ident(), time.ctime()))

        logging.info(' ')
        logging.info('***************************请求次数:' + str(now_count) + '*******************************')
        logging.info('Thread:(%d) Time:%s\n' % (thread.get_ident(), time.ctime()))
        cnt += 1
        send_http()
        sys.stdout.flush()
        lock_obj.release()
        time.sleep(request_interval)


def test(ct):
    global thread_count
    for i in range(thread_count):
        thread.start_new_thread(test_func, (ct,))


if __name__ == '__main__':
    global test_count
    test(test_count)
    while True:
        time.sleep(100)
