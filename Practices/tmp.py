# import pickle
import json
import csv

test_dic1 = {'a': 1, 'b': 2, 'c': 3}
test_dic2 = {'e': 4, 'f': 5, 'g': 6}
# with open(r'E:\Codes\Python\confusion\temp\test.pickle', 'wb+') as fd:
# 	pickle.dump(test_dic, fd)
#
# with open(r'E:\Codes\Python\confusion\temp\test.pickle', 'rb') as fd:
# 	a = pickle.load(fd)
#
# print(a)

# with open(r'E:\Codes\Python\confusion\temp\test.json', 'w') as fd:
# 	json.dump(test_dic, fd)
#
# with open(r'E:\Codes\Python\confusion\temp\test.json') as fd:
# 	b = json.load(fd)
# print(b)


def w_csv(b_dict, file_name):
	with open(file_name, 'wb+') as fd:
		writer2 = csv.writer(fd)
		for key in b_dict:
			writer2.writerow([key, b_dict[key]])


if __name__ == '__main__':
	name_list = [test_dic1, test_dic2]
	for i in range(2):
		w_csv(name_list[i], 'test_dic1')
