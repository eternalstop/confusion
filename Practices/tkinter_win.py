#!/usr/local/python/bin/python
# coding=utf-8

from Tkinter import *


def hello():
	print("hello world")


win = Tk()
win.title('hello tkinter')
win.geometry('200x100')
btn = Button(win, text='hello', command=hello)
btn.pack(expand=YES, fill=BOTH)

if __name__ == '__main__':
	mainloop()
