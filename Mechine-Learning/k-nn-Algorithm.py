#!/usr/local/python/bin/python
# coding=utf-8
"""
 k近邻法(k-nearest neighbor, k-NN)是1967年由Cover T和Hart P提出的一种基本分类与回归方法。
 它的工作原理是：存在一个样本数据集合，也称作为训练样本集，并且样本集中每个数据都存在标签，
 即我们知道样本集中每一个数据与所属分类的对应关系。
 输入没有标签的新数据后，将新的数据的每个特征与样本集中数据对应的特征进行比较，然后算法提取样本最相似数据(最近邻)的分类标签。
 一般来说，我们只选择样本数据集中前k个最相似的数据，这就是k-近邻算法中k的出处，通常k是不大于20的整数。
 最后，选择k个最相似数据中出现次数最多的分类，作为新数据的分类
"""
import operator
import numpy as np

"""
函数说明：数据集

Returns：
	group -- 数据集
	labels -- 分类标签
"""


def createDataSet():
	group = np.array([[1, 101], [5, 91], [87, 7], [120, 5]])
	labels = ["爱情片", "爱情片", "动作片", "动作片"]
	return group, labels


"""
函数说明：k-nn算法，分类器


Parameters：
	inX：用于分类的数据（测试集）
	dataSet：用于训练的数据（训练集）
	label：分类标签
	k：knn算法参数，选择距离最小的k个点
	
Returns：
	sortedClassCount[0][0]
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


if __name__ == '__main__':
	group, labels = createDataSet()
	test = [80, 20]
	test_class = classify0(test, group, labels, 3)
	print(test_class)