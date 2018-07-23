#!/usr/local/python/bin/python
# coding=utf-8

test_list = []
fin_list =[]
for i in range(1, 7):
	test_list.append(i)
print(test_list)

for a in test_list:
	for b in test_list:
		for c in test_list:
			if a==b or a==c or b==c:
				continue
			else:
				fin_list.append((a, b, c))
				if (a + b + c)==15:
					print([a, b, c])

print(fin_list)