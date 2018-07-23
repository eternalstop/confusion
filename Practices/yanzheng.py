from PIL import Image, ImageDraw, ImageFont
from urllib import request, parse
import urllib
import time
import re

head = {
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Cache-Control": "max-age=0",
	"Connection": "keep-alive",
	# "Cookie": "PHPSESSID=knteilr57cn8bt8vsnlctfhmg2; wxd_openid=o9YHRvpSvp6N6vdvQD9k7cRZHZsg; td_cookie=1102058391; clicaptcha_text=%E8%83%B8%2C%E5%87%8F",
	"Host": "anhui.246.miduoshang.com",
	# "Referer": "http://anhui.246.miduoshang.com/d.php?g=Wap&m=Vote&a=detail&token=Eioa5C5oj3S32qhH&id=1&zid=4",
	"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}

t = int(time.time())
# image_url = "http://anhui.246.miduoshang.com/validation/clicaptcha.php?%s" % t
image_url = "http://anhui.246.miduoshang.com/validation/clicaptcha.php?1530528721210"
req = request.Request(url=image_url, headers=head)
resp = request.urlopen(req)
set_cookie = resp.getheader(name="Set-Cookie")
text = parse.unquote(re.split('[,;=]', str(set_cookie))[5])
# print(text)

img_stream = resp.read()

try:
    with open(r"C:\Users\ty\Desktop\test.jpg", "wb") as jpg:
        jpg.write(img_stream)
except IOError:
    print("IO Error\n")

im=Image.open(r'C:\Users\ty\Desktop\test.jpg')
draw=ImageDraw.Draw(im)
newfont=ImageFont.truetype('simkai.ttf', 20)
draw.text((50, 5), '请依次点击 “%s”、 “%s”' % (text[0], text[2]), (0, 0, 0), font=newfont)
im.show()
# im.save(r'C:\Users\ty\Desktop\test.jpg')

