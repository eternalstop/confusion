import os
from aip import AipSpeech
from tinytag import TinyTag

"""百度APPID  AK  SK"""

APP_ID = "16219594"
API_KEY = "n9cG4TPbYhxwcONpG1wkQ6XG"
SECRET_KEY = "EVhgOsnZTjb0W31VIV1kiRCvcpnPp7N4"

client = AipSpeech(appId=APP_ID, apiKey=API_KEY, secretKey=SECRET_KEY)


def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()


def mp32pcm(infile, outfile="16k.pcm"):
	"""
	-acodec pcm_s16le pcm_s16le 16bits 编码器
	-f s16le 保存为16bits pcm格式
	-ac 1 单声道
	-ar 16000 16000采样率
	"""
	command = "ffmpeg -y -i %s -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s" % (infile, outfile)
	result = os.system(command)
	return result


def splitaudio(infile):
	tag = TinyTag.get(infile)
	for spltm in range(0, int(tag.duration), 50):
		outfile = r'./audio/' + str(spltm) + '.pcm'
		command = "ffmpeg -ss %s -t 50 -y -i %s -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s" % (spltm, infile, outfile)
		os.system(command)
	

# splitaudio(r"./audio/how.m4a")
recive_data = client.asr(get_file_content(r'./audio/0.pcm'), 'pcm', 16000, {'dev_pid': 1536, })
print(recive_data)
