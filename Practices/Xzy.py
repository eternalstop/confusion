#!/usr/local/python/bin/python
# coding=utf-8

from urllib import request
from urllib import parse

cookie = "Hm_lvt_37d45a923596e471fdbdeaac7b686beb=1511516250; h5_cuserid=1511851971676686; c_a_id=115020310185; channelID=01833310; c_cookie_id=2914c51e546e7907642e4576ea708d0d; PHPSESSID=f6hkc1hpd25vhmtfs82ut0pc33; c_u_i=63a4ee903c25d555b86f2f5b6001a0dee21aa9be34f33be490f790d0ba25e0f4a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22c_u_i%22%3Bi%3A1%3Ba%3A9%3A%7Bs%3A5%3A%22token%22%3Bs%3A32%3A%222914c51e546e7907642e4576ea708d0d%22%3Bs%3A3%3A%22uid%22%3Bs%3A21%3A%22104200105510660171124%22%3Bs%3A9%3A%22accountNo%22%3Bs%3A21%3A%2218655660717%40tv189.com%22%3Bs%3A8%3A%22nickName%22%3Bs%3A6%3A%22%E7%8E%8B%E4%BA%AE%22%3Bs%3A7%3A%22headUrl%22%3Bs%3A0%3A%22%22%3Bs%3A8%3A%22userType%22%3Bi%3A2%3Bs%3A7%3A%22subType%22%3Bi%3A1%3Bs%3A10%3A%22provinceId%22%3Bs%3A0%3A%22%22%3Bs%3A6%3A%22cityId%22%3Bs%3A0%3A%22%22%3B%7D%7D; c_a_l_i=f1c60d9b90373939e9bd20f1bd63cc93825803a2831d25c4716c053fc309e48da%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22c_a_l_i%22%3Bi%3A1%3Ba%3A2%3A%7Bs%3A4%3A%22uuid%22%3Bs%3A93%3A%2258rrbcln4ip1q64s3cd9l6or30dph6t078thh70sisorfdlu34v1h64qj0chg6coj0c9o6lu32ctg0eev0fgu9rmlcrnc%22%3Bs%3A3%3A%22uid%22%3Bs%3A21%3A%22104200105510660171124%22%3B%7D%7D"
head = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
	              'AppleWebKit/537.36 (KHTML, like Gecko) '
	              'Chrome/63.0.3239.84 Safari/537.36',
	'Cookie': cookie
}

urlink = "http://h5.nty.tv189.com/zt/default/xzydetail?id=0033"

req = request.Request(urlink, headers=head)
respones = request.urlopen(req)
html = respones.read()
print(html)