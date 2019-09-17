# _*_coding:utf-8_*_
import requests


def get_fruit_list(token):
	fruits_link = "http://fruits.eternalstop.com:7788/fruit/"
	header = {
		"Authorization": 'JWT ' + token
	}
	reponse = requests.get(fruits_link, headers=header)
	if reponse.status_code == 401:
		return "Error"
	else:
		results = requests.get(fruits_link, headers=header).json()["results"]
		return results


def login(username, password):
	token_link = "http://fruits.eternalstop.com:7788/api-token-auth/"
	params = {
		"username": username,
		"password": password,
	}
	
	reponse = requests.post(token_link, data=params)
	token = reponse.json()["token"]
	return token


if __name__ == '__main__':
	getoken = login(username="admin", password="Missy@u777")
	print(get_fruit_list(getoken))
