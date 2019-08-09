#!/usr/local/python/bin/python
# coding=utf-8
import base64
import binascii
import json
import random
import requests

from Crypto.Cipher import AES
# from Crypto.PublicKey import RSA
from string import ascii_letters, digits

_charset = ascii_letters + digits


def rand_char(num=16):
	return ''.join(random.choice(_charset) for _ in range(num))


def aes_encrypt(msg, key, iv='0102030405060708'.encode('utf-8')):
	def padded(msg):
		pad = 16 - len(msg) % 16
		return msg + pad * chr(pad)

	msg = padded(msg)
	cryptor = AES.new(key, IV=iv, mode=AES.MODE_CBC)
	text = cryptor.encrypt(msg.encode('utf-8'))
	text = base64.b64encode(text)
	return text.decode('utf-8')


def gen_params(d, i):
	text = aes_encrypt(d, '0CoJUm6Qyw8W8jud'.encode('utf-8'))
	text = aes_encrypt(text, i.encode('utf-8'))
	return text


def rsa_encrypt(msg):
	msg = binascii.b2a_hex(msg[::-1].encode('utf-8'))
	msg = int(msg, 16)
	text = 1
	for _ in range(0x10001):
		text *= msg
		text %= 0x00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
	return format(text, 'x')


def encrypt(query):
	query = json.dumps(query)
	rand_i = rand_char(16)
	params = gen_params(query, rand_i)
	enc_sec_key = rsa_encrypt(rand_i)
	data = {
		'params': params,
		'encSecKey': enc_sec_key
	}
	return data


def getLyric(song_id):
	url = 'http://music.163.com/weapi/song/lyric?csrf_token='
	# url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(music_id)
	headers = {
		'Accept': '*/*',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
		'Connection': 'keep-alive',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Host': 'music.163.com',
		'Origin': 'http://music.163.com',
		'Referer': 'http://music.163.com/',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
	}
	querys = {
		'id': song_id,
		'lv': -1,
		'tv': -1,
		'csrf_token': ''
	}
	
	datas = encrypt(querys)
	
	r = requests.post(url, data=datas, headers=headers)
	result_dic = r.json()
	if "nolyric" in result_dic.keys():
		if result_dic['nolyric']:
			return "Nolyric"
	else:
		source_list = [i for i in result_dic['lrc']['lyric'].split("\n") if i != '']
		lyric_list = [words.split("]")[1].strip() for words in source_list]
		return lyric_list


if __name__ == '__main__':
	music_id = '92939'
	print(getLyric(music_id))





