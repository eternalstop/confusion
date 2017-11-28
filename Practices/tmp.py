import pickle
import json
import csv
import re
import random
import difflib

test_dic1 = {'a': 1, 'b': 2, 'c': 3}
test_dic2 = {'e': 4, 'f': 5, 'g': 6}


def tmp1(test_dic):
	with open(r'E:\Codes\Python\confusion\temp\test.pickle', 'wb+') as fd:
		pickle.dump(test_dic, fd)

	with open(r'E:\Codes\Python\confusion\temp\test.pickle', 'rb') as fd:
		a = pickle.load(fd)

	print(a)

	with open(r'E:\Codes\Python\confusion\temp\test.json', 'w') as fd:
		json.dump(test_dic, fd)

	with open(r'E:\Codes\Python\confusion\temp\test.json') as fd:
		b = json.load(fd)
	print(b)


def w_csv(b_dict, file_name):
	with open(file_name, 'wb+') as fd:
		writer2 = csv.writer(fd)
		for key in b_dict:
			writer2.writerow([key, b_dict[key]])


data = '{ reason= score=0.0 activetime=2016-11-11 20:34:00 feature={"timestamp":"1510230659436","longitude":39.806193,"latitude":116.490655,"cityid":"1"} uuid=B320173637BA90F740BEB610460DDEE47A95D32A51D4D44167BB4B4D48E03E2A isnew=false}'


def tmp2(data):
	data = data.split()
	if '{' in data:
		data.remove('{')
	elif '}' in data:
		data.remove('}')
	data[-1] = data[-1].split("}")[0]
	data[2] = data[2] + ' ' + data[3]
	data.remove(data[3])
	data_dic = {}
	for i in data:
		eme = i.split("=")
		data_dic[eme[0]] = eme[1]
	return data_dic


def tmp3(data):
	seq = re.compile(r'\w+=')
	keys = seq.findall(data)
	keys = map(lambda _: _[0: -1], keys)
	values = seq.split(data)[1:]
	values[-1] = values[-1].split("}")[0]
	info_map = dict(zip(keys, values))
	return info_map


def tmp4():
	count = 0
	while True:
		print(random.choice('/\\'), end='')
		count += 1
		if count % 50 == 0:
			print()
		if count == 1000:
			break


def tmp5():
	s1 = 'agtcgtaatgc'
	s2 = "cgaa"
	mch = difflib.SequenceMatcher(a=s1, b=s2)
	m = mch.find_longest_match(0, len(s1), 0, len(s2))
	print(s1[m.a:m.a + m.size], s2[m.b:m.b + m.size])


if __name__ == '__main__':
	tmp5()

# tmplist = [1, 2, 3, 4, 5]
# e1 = enumerate(tmplist, 4)
# for i in e1:
# 	print(i)
# s = 'ABCD'
# m = re.findall(r'.*$', s)
# if m:
# 	print(m)


