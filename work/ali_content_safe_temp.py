# coding=utf-8
# 以下代码用于调用图片同步检测接口并实时返回检测结果。
from imp import reload

from aliyunsdkcore import client
from aliyunsdkgreen.request.v20180509 import ImageSyncScanRequest
from aliyunsdkgreenextension.request.extension import ClientUploader
from aliyunsdkgreenextension.request.extension import HttpContentHelper
import json
import uuid
import sys

# 设置编码规则，以便支持本地中文路径。
# Python2中添加以下内容，Python3无需添加。
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')

# 请使用您自己的AccessKey信息。
clt = client.AcsClient("LTAI5tEp9ZiZKBAUq7bnwrQB", "H2CxATZLDtK8sr3RaMXOg4hA8CTFlG", "cn-shanghai")
# 每次请求时需要新建request，请勿复用request对象。
request = ImageSyncScanRequest.ImageSyncScanRequest()
request.set_accept_format('JSON')

# 请修改成您自己的本地文件路径。
# 上传本地文件到服务端。
uploader = ClientUploader.getImageClientUploader(clt)
url = uploader.uploadFile('bb.jpg')

# 获取上传后的URL进行检测。
task = {"dataId": str(uuid.uuid1()),
         "url":url
        }

# 设置待检测的图片，一张图片对应一个检测任务。
# 多张图片同时检测时，处理时间由最后一张处理完的图片决定。
# 通常情况下批量检测的平均响应时间比单任务检测长，一次批量提交的图片数越多，响应时间被拉长的概率越高。
# 代码中以单张图片检测作为示例，如果需要批量检测多张图片，请自行构建多个任务。
# 一次请求中可以检测多张图片，每张图片支持检测多个风险场景，计费按照单图片单场景检测叠加计算。
# 例如，检测2张图片，场景传递porn和terrorism，则计费按照2张图片鉴黄和2张图片暴恐检测计算。
request.set_content(HttpContentHelper.toValue({"tasks": [task], "scenes": ["porn"]}))
response = clt.do_action_with_exception(request)
print(response)
result = json.loads(response)
if 200 == result["code"]:
    taskResults = result["data"]
    for taskResult in taskResults:
        if (200 == taskResult["code"]):
            sceneResults = taskResult["results"]
            for sceneResult in sceneResults:
                # 根据scene和suggetion设置后续操作。
                # 根据不同的suggestion结果做业务上的不同处理。例如，将违规数据删除等。
                scene = sceneResult["scene"]
                suggestion = sceneResult["suggestion"]