# coding:utf-8
import random
import time
import urllib3
import threading
from time import sleep

# 性能测试页面
TEST_HOST = "https://10.214.5.11"

PERF_TEST_URL = [
    "/web/notice.php?platform=bilibili",
    "/web/server_list.php?platform=bilibili&acct=355220645",
    "/web/get_device_config.php?devicename_identifier=iphone13,1",
    "/web/sessionVerify.php?platform=bilibili&uid=355220645&accesskey=bda5d14b35240431890bd7dad3d11ab1&prename=bili_",
    "/web/client_version.php?platform=bilibili&version=1.0",
    "/app/fullscaleinfo?sid=0",
    "/app/processinfo?sid=0",
    "/app/seallvinfo?sid=0"
]

# 配置:压力测试
# THREAD_NUM = 10			# 并发线程总数
# ONE_WORKER_NUM = 500		# 每个线程的循环次数
# LOOP_SLEEP = 0.01		# 每次请求时间间隔(秒)

# 配置:模拟运行状态
THREAD_NUM = 10  # 并发线程总数
ONE_WORKER_NUM = 10  # 每个线程的循环次数
LOOP_SLEEP = 1.0  # 每次请求时间间隔(秒)

# 出错数
ERROR_NUM = 0


# 具体的处理函数，负责处理单个任务
def do_work(index):
    test_url = TEST_HOST + random.choice(PERF_TEST_URL)
    t = threading.currentThread()
    # print "["+t.name+" "+str(index)+"] "+PERF_TEST_URL
    http = urllib3.PoolManager()
    try:
        html = http.request('GET', test_url).read()
    except Exception as e:
        print("[" + t.name + " " + str(index) + "] ")
        print(e)
        global ERROR_NUM
        ERROR_NUM += 1


# 这个是工作进程，负责不断从队列取数据并处理
def working():
    t = threading.currentThread()
    print("[" + t.name + "] Sub Thread Begin")

    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        do_work(i)
        sleep(LOOP_SLEEP)

    print("[" + t.name + "] Sub Thread End")


def main():
    # doWork(0)
    # return
    t1 = time.time()
    threads = []

    # 创建线程
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working, name="T" + str(i))
        t.setDaemon(True)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("main thread end")

    t2 = time.time()
    print("========================================")
    print("URL:", PERF_TEST_URL)
    print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
    print("总耗时(秒):", t2 - t1)
    print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
    print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
    print("错误数量:", ERROR_NUM)


if __name__ == "__main__":
    main()
