# -*- coding:utf-8 -*-
import os

in_path = r'D:\video\wanmen\temp\\'
out_path = r'D:\video\wanmen\3.3.mp4'
files = [
	{"1.1": "http://media.wanmen.org/1654750e-46d3-4f99-974c-c15c593a392e_mobile_low.m3u8?sign=a0b2c3c2d7530c51dcfb2c37e4deddd4&t=5cb943b2&r=63ab4942ccaa90f1dd68e6101594bfc7"},
	{"1.2": "http://media.wanmen.org/d221ffab-48a5-4c93-9e78-a3fd8f0242b7_mobile_low.m3u8?sign=c21ea2b79e947f7c75c330b49b06b7ec&t=5cb943c8&r=4ee7e9aad85d71a4694084c46b3bc2cf"},
	{"1.3": "http://media.wanmen.org/e40ce12a-b8d1-4fed-9605-ef93c4bf216c_mobile_low.m3u8?sign=6de9dd437555c07fdfca5a42b0f7630d&t=5cb943c8&r=4ee7e9aad85d71a4694084c46b3bc2cf"},
	{"1.4": "http://media.wanmen.org/5f6823b0-a841-4efb-a9ec-d5fd88655a3f_mobile_low.m3u8?sign=7dbbf2670012a3106ba8728b9066e516&t=5cb943c8&r=4ee7e9aad85d71a4694084c46b3bc2cf"},
	{"1.5": "http://media.wanmen.org/d4e86f14-655a-44ca-800a-200292464e6d_mobile_low.m3u8?sign=802d476bf038a87fdbedd2c6e505b53f&t=5cb943c8&r=4ee7e9aad85d71a4694084c46b3bc2cf"},
	{"1.6": "http://media.wanmen.org/ec5807bf-4d23-4ce0-a2d0-50f047b08e51_mobile_low.m3u8?sign=b35231acfb634ca8da7036ee8d4dc679&t=5cb943c8&r=4ee7e9aad85d71a4694084c46b3bc2cf"},
	{"1.7": "http://media.wanmen.org/fec83b97-a571-447a-b6c5-3fcc721c4ae2_mobile_low.m3u8?sign=aabd7dd41097a44ec4aecdc9974beb24&t=5cb943c8&r=4ee7e9aad85d71a4694084c46b3bc2cf"},
	{"1.8": "http://media.wanmen.org/175061ab-83d3-4b0b-9290-b2952431d30e_mobile_low.m3u8?sign=88c4a061de9ad37393927875cc5c7dfd&t=5cb943c8&r=4ee7e9aad85d71a4694084c46b3bc2cf"},
	{"1.9": "http://media.wanmen.org/49d5e291-9635-4d3a-b7dd-c7c11bd4c620_mobile_low.m3u8?sign=e2bbf1c2678a7f52dc0292a83d81f7b5&t=5cb943c8&r=4ee7e9aad85d71a4694084c46b3bc2cf"}
]
for file in os.listdir(path=in_path):
	files.append(in_path + file)

input_arg = '|'.join(files)
m3u8 = in_path + 'ace7bfd9-9425-4f72-b935-391d329c77c0_mobile_low.m3u8'
# print(input_arg)
command = 'ffmpeg -i "%s" -vcodec copy -acodec copy -absf aac_adtstoasc %s' % (m3u8, out_path)
os.system(command)