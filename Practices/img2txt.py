from PIL import Image
import pytesseract
import os

os.environ['TESSDATA_PREFIX'] = r'C:\Program Files (x86)\Tesseract-OCR\tessdata'


def get_eng(img):
	code = pytesseract.image_to_string(Image.open(img), lang='eng')
	return code


def get_chi(img):
	code = pytesseract.image_to_string(Image.open(img), lang='chi_sim')
	return code


#二值化算法
def binarizing(img,threshold):
	pixdata = img.load()
	w, h = img.size
	for y in range(h):
		for x in range(w):
			if pixdata[x, y] < threshold:
				pixdata[x, y] = 0
			else:
				pixdata[x, y] = 255
	return img


# 去除干扰线算法
def depoint(img):
	pixdata = img.load()
	w, h = img.size
	for y in range(1, h-1):
		for x in range(1, w-1):
			count = 0
			if pixdata[x, y-1] > 245:
				count = count + 1
			if pixdata[x, y+1] > 245:
				count = count + 1
			if pixdata[x-1, y] > 245:
				count = count + 1
			if pixdata[x+1, y] > 245:
				count = count + 1
			if count > 2:
				pixdata[x, y] = 255
	return img


def get_identify(image):
	image = Image.open(image)
	img = image.convert('L')
	img1 = binarizing(img, 190)
	img1.show()
	code = pytesseract.image_to_string(img1)
	return code


if __name__ == "__main__":
<<<<<<< HEAD
	source = r'D:\图片\QQ图片20210603182101.png'
=======
	source = r'D:\图片\微信图片_20180815102544.png'
>>>>>>> b01c862ce99a29806808ae156c6d9774bfc2a0b9
	print(get_identify(source))
