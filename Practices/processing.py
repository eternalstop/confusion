# coding=utf-8
import multiprocessing
import os


def test_func(num):
	print('process', os.getpid(), os.getppid())


if __name__ == '__main__':
	for i in range(5):
		p = multiprocessing.Process(target=test_func, args=(i,))
		p.start()
