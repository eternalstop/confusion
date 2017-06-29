# coding=utf-8
import random

hh = random.randrange(20)
for i in range(1, 7, 1):
    ll = int(input("Please Guess The Number(1-20): "))
    if ll > hh:
        print ('猜大了！')
        continue
    elif ll < hh:
        print ("猜小了！")
        continue
    elif ll == hh:
        print ("猜对了！你赢了！")
        break
else:
    print ("你输了！")
