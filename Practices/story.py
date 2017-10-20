from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
	url = 'http://www.136book.com/fanyiguan-1/'
	head = {
		'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) '
		              'AppleWebKit/535.19 (KHTML, like Gecko) '
		              'Chrome/18.0.1025.166  '
		              'Safari/535.19'}
	req = request.Request(url, headers=head)
	response = request.urlopen(req)
	html = response.read()
	soup = BeautifulSoup(html, 'lxml')
	soup_texts = soup.find('div', id='book_detail', class_='box1').find_next('div')
	soup_title_texts = soup.find('h1')
	name = str(soup_title_texts).split(">")[1].split("<")[0]

	with open(r'C:\Users\ty\Documents\story\%s.txt' % name, 'w') as fp:
		for link in soup_texts.ol.children:
			if link != '\n':
				cap_url = link.a.get('href')
				req = request.Request(cap_url, headers=head)
				response = request.urlopen(req)
				html = response.read()
				cap_soup = BeautifulSoup(html, 'lxml')
				cap_soup_text = cap_soup.find('div', id='content')
				cap_soup_text = cap_soup_text.text.split('\n')[1]
				fp.write(link.text + '\n\n')
				fp.write(cap_soup_text + '\n\n')

	# soup_text = soup.find('div', id='content')
	# print(soup_text.text.split('\n')[1])
