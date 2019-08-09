import copy

a = [1, 2, 3, 4, ['a', 'b', 'c']]

b = a
c = copy.copy(a)
d = copy.deepcopy(a)


a.append(5)
a[4].append('d')

print(a)
print(b)
print(c)
print(d)