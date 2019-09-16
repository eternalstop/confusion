# _*_coding:utf-8_*_
import requests
import json


fruits_link = "http://fruits.eternalstop.com:7788/fruit/"


def login(username, password):
	header = {
		"Authorization": ''
	}
	token_link = "http://fruits.eternalstop.com:7788/api-token-auth/"
	params = {
	    "username": username,
	    "password": password,
	}
	
	reponse = requests.post(token_link, data=params)
	header["Authorization"] = "JWT " + reponse.json()["token"]
	print(requests.get(fruits_link, headers=header).json())


if __name__ == '__main__':
	login(username="liang", password="Missy@u777")