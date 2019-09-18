# _*_coding:utf-8_*_
import requests


def login(username, password):
	token_link = "http://fruits.eternalstop.com:7788/api-token-auth/"
	params = {
		"username": username,
		"password": password,
	}
	
	reponse = requests.post(token_link, data=params)
	token = reponse.json()["token"]
	return token


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


def get_product_id(name, products):
	for product in products:
		if product["name"] in name:
			return product["id"]


def post_order_info(token, info, products):
	order_link = "http://fruits.eternalstop.com:7788/order/"
	header = {
		"Authorization": 'JWT ' + token
	}
	results_data = {}
	for i in info:
		post_data = {
			"deliverytime": '',
			"lastcheck": i["上次查询时间"],
			"ordernum": i["单号"],
			"company": "",
			"checkurl": i["链接"],
			"name": i["收货人"],
			"phonenum": i["电话"],
			"location": i["地址"],
			"product": get_product_id(name=i["产品"], products=products)
		}
		response = requests.post(url=order_link, headers=header, data=post_data)
		if response.status_code == 200:
			continue
		else:
			results_data[i["单号"]] = "Faild"
	return results_data


if __name__ == '__main__':
	getoken = login(username="admin", password="Missy@u777")
	products = get_fruit_list(getoken)
