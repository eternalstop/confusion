# coding=utf-8
for i in range(1, 10):
    for j in range(1, i+1):
        print('%sx%s=%s' % (j, i, i*j) + '\t', end='')
    print()


