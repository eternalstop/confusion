#!/usr/local/python/bin/python
# coding=utf-8
from PIL import Image


output = "E:\test.txt"
WIDTH = 80
HEIGHT = 80


def get_gray(x, y):
	pix = im.load()
	# width = im.size[0]
	# height = im.size[1]
	r, g, b = pix[x, y]
	# pic_gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	pic_gray = int(r*0.299 + g*0.587 + b*0.114)
	return pic_gray


def get_ascii_char():
	char_str = ''
	for num in xrange(32, 127):
		char_str += chr(num)
	char_list = list(char_str)
	return char_list


def get_char(x, y, alpha=256):
	if alpha == 0:
		return ' '
	char_list = get_ascii_char()
	length = len(get_ascii_char())
	unit = (256.0 + 1) / length
	gray = get_gray(x, y)
	return char_list[int(gray / unit)]


if __name__ == "__main__":
	im = Image.open(r'E:\test.png')
	# width = im.size[0]
	# height = im.size[1]
	im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
	count = ""
	for i in xrange(WIDTH):
		for j in xrange(HEIGHT):
			count += get_char(j, i)
		count += "\n"
	# print count

	with open(r'E:/test.txt', 'w') as f:
			f.write(count)
