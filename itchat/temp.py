#!/usr/local/bin/python
# coding=utf-8
from pypinyin import pinyin, lazy_pinyin, Style
import Pinyin2Hanzi
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag


def pinyin_2_hanzi(word):
	if Pinyin2Hanzi.is_chinese(word):
		word_pinyin = lazy_pinyin(word)
		dagParams = DefaultDagParams()
		word_list = []
		result = dag(dagParams, word_pinyin, path_num=3, log=True)
		for item in result:
			word_list.append(item.path[0])
		return word_list
	else:
		return "Null"


if __name__ == '__main__':
	print(pinyin_2_hanzi("666"))


# print(pinyin('好'))
# print(lazy_pinyin('好'))
# print(lazy_pinyin('好'))
