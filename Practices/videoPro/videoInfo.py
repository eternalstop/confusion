# _*_ coding:utf-8 _*_
import skvideo.io
import cv2
import os
import time


class VideoPro(object):
	def __init__(self, video_file, path_out, out_prefix="frame", initial_extract_time=0, end_extract_time=None, extract_time_interval=-1, jpg_quality=100):
		self.video_file = video_file
		self.path_out = path_out
		self.initial_extract_time = int(initial_extract_time)
		self.end_extract_time = int(end_extract_time)
		self.extract_time_interval = extract_time_interval
		self.out_prefix = out_prefix
		self.jpg_quality = int(jpg_quality)
		
		"""
		:param video_file:视频的路径，比如：D:\video\yijing.mp4
		:param path_out:设定提取的图片保存在哪个文件夹下，比如：D:\video\screenshot。如果该文件夹不存在，函数将自动创建它
		:param initial_extract_time:提取的起始时刻，单位为秒，默认为0（即从视频最开始提取）
		:param end_extract_time:提取的终止时刻，单位为秒，默认为None（即视频终点）
		:param extract_time_interval:提取的时间间隔，单位为秒，默认为-1（即输出时间范围内的所有帧）
		:param out_prefix:图片的前缀名，默认为frame，图片的名称将为frame_01.jpg、frame_02.jpg、frame_03.jpg......
		:param jpg_quality:设置图片质量，范围为0到100，默认为100（质量最佳）
		"""
	
	def videoInfo(self):
		info = []
		metadata = skvideo.io.ffprobe(self.video_file)
		if '@width' in metadata['video'].keys():
			info.append(metadata['video']['@width'])
		else:
			info.append("Non-Exist")
		if '@height' in metadata['video'].keys():
			info.append(metadata['video']['@height'])
		else:
			info.append("Non-Exist")
		if '@codec_name' in metadata['video'].keys():
			info.append(metadata['video']['@codec_name'])
		else:
			info.append("Non-Exist")
		if '@bits_per_raw_sample' in metadata['video'].keys():
			info.append(metadata['video']['@bits_per_raw_sample'])
		else:
			info.append("Non-Exist")
		# if '@duration' in metadata['video'].keys():
		# 	info.append(metadata['video']['@duration'])
		# else:
		# 	info.append("Non-Exist")
		return info
		# return json.dumps(metadata['video'], indent=4)
	
	def video2img(self):
		cap = cv2.VideoCapture(self.video_file)  # 打开视频文件
		n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 视频的帧数
		# video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 视频宽度
		# video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 视频高度
		fps = cap.get(cv2.CAP_PROP_FPS)  # 视频的帧率
		duration = n_frames / fps  # 视频的时间
		format_dur = time.strftime("%Hh%Mm%Ss", time.gmtime(duration))
		
		if self.initial_extract_time > duration:
			raise NameError('initial extract time is larger than the video duration....')
		if self.end_extract_time is not None:
			if self.end_extract_time > duration:
				raise NameError('end extract time is larger than the video duration....')
			if self.initial_extract_time > self.end_extract_time:
				raise NameError('end extract time is less than the initial extract time....')
		
		# 判断提取时间间隔设置是否符合要求
		if 0 < self.extract_time_interval < 1 / fps:
			raise NameError('extract_time_interval is less than the frame time interval....')
		elif self.extract_time_interval > (n_frames / fps):
			raise NameError('extract_time_interval is larger than the duration of the video....')
		
		# 时间范围内每隔一段时间输出一张图片
		else:
			try:
				os.mkdir(self.path_out)
			except OSError:
				pass
			# print('Converting a video into frames......')
			if self.end_extract_time is not None:
				N = (self.end_extract_time - self.initial_extract_time) / self.extract_time_interval + 1
				success = True
				count = 0
				while success and count < N:
					cap.set(cv2.CAP_PROP_POS_MSEC, (self.initial_extract_time * 1000 + count * self.extract_time_interval * 1000))
					success, image = cap.read()
					if success:
						cv2.imwrite(os.path.join(self.path_out, "{}-{:02d}.jpg".format(self.out_prefix, count + 1)), image,
						            [int(cv2.IMWRITE_JPEG_QUALITY), self.jpg_quality])  # save frame as JPEG file
						count = count + 1
			else:
				success = True
				count = 0
				while success:
					cap.set(cv2.CAP_PROP_POS_MSEC, (self.initial_extract_time * 1000 + count * self.extract_time_interval * 1000))
					success, image = cap.read()
					if success:
						cv2.imwrite(os.path.join(self.path_out, "{}-{:02d}.jpg".format(self.out_prefix, count + 1)), image,
						            [int(cv2.IMWRITE_JPEG_QUALITY), self.jpg_quality])  # save frame as JPEG file
						count = count + 1
		return format_dur

	# start_time = time.clock()
	# file = r"D:\video\展示：高清内容生产制作.ts"
	# save_path = r"D:\video\screenshot"
	# prefix = file.split("\\")[-1].split(".")[0]
	#
	# print(video2frames(path_in=file,
	#                    path_out=save_path,
	#                    initial_extract_time=3,
	#                    end_extract_time=5,
	#                    extract_time_interval=1,
	#                    output_prefix=prefix))
	# print(getInfo(file))
	# end_time = time.clock()
	# print(end_time - start_time)
