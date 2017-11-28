#!/usr/local/python/bin/python
# coding=utf-8

from tkinter import *


def hello():
	print("hello world")


win = Tk()
win.title('hello tkinter')
win.geometry('700x700')
btn = Button(win, text='查询', command=hello)
btn.pack(expand=YES, fill=BOTH)


if __name__ == '__main__':
	mainloop()
