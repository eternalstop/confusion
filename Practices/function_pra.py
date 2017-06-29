# coding=utf-8
from __future__ import print_function


def num_fun():
    a_num = input("Please input a number :  ")
    try:
        if isinstance(int(a_num), type(1)):
            print ("%s is a number! " % a_num)
    except:
        print("%s is not a number! " % a_num)


def is_num(s):
    for i in s:
        if i in "0123456789":
            pass
        else:
            print ("%s is not a number!" % s)
            break
    else:
        print ("%s is a number!" % s)


def is_nnum(d):
    if d.isdigit():
        return True
    return False

if is_nnum('1ab'):
    print ("It is a number!")
else:
    print ("It is not a number!")
# num_fun()
# is_num("122")
