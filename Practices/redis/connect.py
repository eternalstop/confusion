#!/usr/local/python/bin/python
# coding=utf-8
import os
import configparser
import random
import time
import redis

configfile = "config.txt"


def w_config(cfile):
	HOST = "127.0.0.1"
	PORT = "6379"
	NAME = ""
	PASSWORD = ""
	conf = configparser.ConfigParser()
	with open(cfile, 'w') as fd:
		conf.add_section("Connect_Config")
		conf.set("Connect_Config", "hostname", HOST)
		conf.set("Connect_Config", "port", PORT)
		conf.set("Connect_Config", "name", NAME)
		conf.set("Connect_Config", "passwd", PASSWORD)
		conf.add_section("End_Config")
		conf.write(fd)


def r_config(cfile):
	if os.path.exists(cfile):
		conf = configparser.ConfigParser()
		conf.read(cfile)
		host = conf.get("Connect_Config", "hostname")
		port = conf.get("Connect_Config", "port")
		name = conf.get("Connect_Config", "name")
		password = conf.get("Connect_Config", "passwd")
		return host, port, name, password


def c_connect(host, port):
	pool = redis.ConnectionPool(host=host, port=port)
	client = redis.StrictRedis(connection_pool=pool)
	# p = client.pipeline()
	# for i in range(7):
	# 	p.lpush(i, i)
	# p.execute()
	return client


def play():
	blue_list = [random.randrange(1, 17)]
	red_list = []
	tmp_dic = {}
	for i in range(6):
		red_list.append(random.randrange(1, 34))
	tmp_dic['red'] = red_list
	tmp_dic['blue'] = blue_list
	return tmp_dic


if __name__ == '__main__':
	w_config(configfile)
	host, port, name, password = r_config(configfile)
	p = c_connect(host, port)
	value = play()
	time = time.strftime('%Y%m%d', time.localtime(time.time()))
	p.set(time, value)

