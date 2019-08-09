import requests
from bs4 import BeautifulSoup


def get_content(playlist):
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
	req = requests.session()
	res = BeautifulSoup(req.get(playlist, headers=headers).content, "html.parser")
	music_dict = {}
	label_list = []
	song_result = res.find('ul', {'class': 'f-hide'}).find_all('a')
	label_result = res.find('div', {'class': 'tags f-cb'}).find_all('i')
	for label in label_result:
		label_list.append(label.text)
	for music in song_result:
		music_dict[music['href'].strip("/song?id=")] = music.text
	return music_dict, label_list


if __name__ == '__main__':
	url = 'https://music.163.com/playlist?id=2547626265'
	print(get_content(url))
