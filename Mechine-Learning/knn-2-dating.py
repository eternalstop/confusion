#!/usr/local/python/bin/python
# coding=utf-8
import operator
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import matplotlib.lines as mlins

"""
函数说明：打开并解析文件，并对数据进行分类：1代表不喜欢，2代表魅力一般，3代表极具魅力

Parameters：
	filename文件名

returns：
	returnMat -- 特征矩阵
	classLabelVector -- 分类Label向量
"""


def classify0(inX, dataSet, label, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances ** 0.5
	sortedDistIndices = distances.argsort()

	classCount = {}
	for i in range(k):
		voteIlabel = label[sortedDistIndices[i]]
		classCount[voteIlabel] =classCount.get(voteIlabel, 0) + 1
		sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
		return sortedClassCount[0][0]


def data2matrix(filename):
	# 打开文件
	fr = open(filename)
	# 读取内容
	arrayOfLines = fr.readlines()
	numberOfLines = len(arrayOfLines)
	# 解析数据生成矩阵：numberOfLines行，3列
	returnmat = np.zeros((numberOfLines, 3))
	# 标签向量
	classLabelVactor = []
	# 行索引
	index = 0
	for line in arrayOfLines:
		line.strip()
		listFromline = line.split('\t')
		listFromline = [i.strip() for i in listFromline]
		returnmat[index, :] = listFromline[0:3]
		# 根据文本中标记的喜欢的程度进行分类,1代表不喜欢,2代表魅力一般,3代表极具魅力
		if listFromline[-1] == 'didntLike':
			classLabelVactor.append(1)
		elif listFromline[-1] == 'smallDoses':
			classLabelVactor.append(2)
		elif listFromline[-1] == 'largeDoses':
			classLabelVactor.append(3)
		index +=1
	return returnmat, classLabelVactor


def showdatas(datingdatamat, datinglabel):
	font = FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc', size=10)
	fig, axs = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False, figsize=(13, 9))
	numberOfLabels = len(datinglabel)
	LabelsColor = []
	for i in datinglabel:
		if i == 1:
			LabelsColor.append('black')
		elif i == 2:
			LabelsColor.append('orange')
		elif i == 3:
			LabelsColor.append('red')
	# 画出散点图，以datingdatamat矩阵的第一（飞行常客里程）、第二列（玩游戏）数据画散点数据，散点大小为15，透明度为0.5
	axs[0][0].scatter(x=datingdatamat[:, 0], y=datingdatamat[:, 1], color=LabelsColor, s=15, alpha=.5)
	axs0_title_text = axs[0][0].set_title('每年获得的飞行常客里程数与玩视频游戏所消耗时间占比', FontProperties=font)
	axs0_xlabel_text = axs[0][0].set_xlabel('每年获得的飞行常客里程数', FontProperties=font)
	axs0_ylabel_text = axs[0][0].set_ylabel('玩视频游戏所消耗时间占比', FontProperties=font)
	plt.setp(axs0_title_text, size=9, weight='bold', color='red')
	plt.setp(axs0_xlabel_text, size=7, weight='bold', color='black')
	plt.setp(axs0_ylabel_text, size=7, weight='bold', color='black')

	# 画出散点图，以datingdatamat矩阵的第一（飞行常客里程）、第三列（冰淇淋）数据画散点数据，散点大小为15，透明度为0.5
	axs[0][1].scatter(x=datingdatamat[:, 0], y=datingdatamat[:, 2], color=LabelsColor, s=15, alpha=.5)
	axs0_title_text = axs[0][1].set_title('每年获得的飞行常客里程数与每周消耗的冰淇淋公升数占比', FontProperties=font)
	axs0_xlabel_text = axs[0][1].set_xlabel('每年获得的飞行常客里程数', FontProperties=font)
	axs0_ylabel_text = axs[0][1].set_ylabel('每周消耗的冰淇淋公升数', FontProperties=font)
	plt.setp(axs0_title_text, size=9, weight='bold', color='red')
	plt.setp(axs0_xlabel_text, size=7, weight='bold', color='black')
	plt.setp(axs0_ylabel_text, size=7, weight='bold', color='black')

	# 画出散点图，以datingdatamat矩阵的第二（玩视频游戏）、第三列（冰淇淋）数据画散点数据，散点大小为15，透明度为0.5
	axs[1][0].scatter(x=datingdatamat[:, 0], y=datingdatamat[:, 2], color=LabelsColor, s=15, alpha=.5)
	axs0_title_text = axs[1][0].set_title('玩视频游戏所消耗时间占比与每周消耗的冰淇淋公升数占比', FontProperties=font)
	axs0_xlabel_text = axs[1][0].set_xlabel('玩视频游戏所消耗时间占比', FontProperties=font)
	axs0_ylabel_text = axs[1][0].set_ylabel('每周消耗的冰淇淋公升数', FontProperties=font)
	plt.setp(axs0_title_text, size=9, weight='bold', color='red')
	plt.setp(axs0_xlabel_text, size=7, weight='bold', color='black')
	plt.setp(axs0_ylabel_text, size=7, weight='bold', color='black')

	# 图例
	didntlike = mlins.Line2D([], [], color='black', marker='.', markersize=6, label='didntlike')
	smalldoses = mlins.Line2D([], [], color='orange', marker='.', markersize=6, label='smalldoses')
	largedoses = mlins.Line2D([], [], color='red', marker='.', markersize=6, label='largedoses')

	axs[0][0].legend(handles=(didntlike, smalldoses, largedoses))
	axs[0][1].legend(handles=(didntlike, smalldoses, largedoses))
	axs[1][0].legend(handles=(didntlike, smalldoses, largedoses))

	# 显示图片
	plt.show()


def autoNorm(dataSet):
	maxVal = dataSet.max(0)
	minVal = dataSet.min(0)
	ranges = maxVal - minVal
	normalDataSet = np.zeros(np.shape(dataSet))
	m = dataSet.shape[0]
	normalDataSet = dataSet - np.tile(minVal, (m, 1))
	normalDataSet = dataSet/np.tile(ranges, (m, 1))
	return normalDataSet, ranges, minVal


def dataTest():
	filename = 'files\datingTestSet.txt'
	datingMat, datingLabels = data2matrix(filename)
	hoRedio = 0.10
	normalMat, ranges, minVals = autoNorm(datingMat)
	m = normalMat.shape[0]
	testDataNum = int(m * hoRedio)
	errCnt = 0.00

	for i in range(0, testDataNum):
		classTestResult = classify0(normalMat[i, :], normalMat[testDataNum:m, :], datingLabels[testDataNum:m], 4)
		print("分类结果：%d\t, 真实结果：%d" % (classTestResult, datingLabels[i]))
		if classTestResult != datingLabels[i]:
			errCnt += 1.00
	print("错误率为：%s%%" % (errCnt / float(m) * 100))


def classifyPerson():
	result = ['讨厌', '有些喜欢', '很喜欢']
	percentTats = float(input("玩视频游戏所占时间比： "))
	ffMiles = float(input("每年获得的飞行常客里程数： "))
	iceCream = float(input("每周消耗的冰激凌公升数： "))
	filename = 'files\datingTestSet.txt'
	datingMat, datingLabels = data2matrix(filename)
	normalDataSet, ranges, minVals = autoNorm(datingMat)
	inArr = np.array([percentTats, ffMiles, iceCream])
	normInArry = (inArr - minVals) / ranges
	classifyResult = classify0(normInArry, datingMat, datingLabels, 3)
	print("你很可能%s这个人" % result[classifyResult - 1])


if __name__ == '__main__':
	# file = 'files\datingTestSet.txt'
	# datingmat, datinglabels = data2matrix(file)
	# normaldataset, ranges, minvals= autoNorm(datingmat)
	# print(normaldataset)
	# print(ranges)
	# print(minvals)
	classifyPerson()
