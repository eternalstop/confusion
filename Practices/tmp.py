# import pickle
import json

test_dic = {'a': 4, 'b': 5, 'c': 6}

# with open(r'E:\Codes\Python\confusion\temp\test.pickle', 'wb+') as fd:
# 	pickle.dump(test_dic, fd)
#
# with open(r'E:\Codes\Python\confusion\temp\test.pickle', 'rb') as fd:
# 	a = pickle.load(fd)
#
# print(a)

with open(r'E:\Codes\Python\confusion\temp\test.json', 'w') as fd:
	json.dump(test_dic, fd)

with open(r'E:\Codes\Python\confusion\temp\test.json') as fd:
	b = json.load(fd)
print(b)
