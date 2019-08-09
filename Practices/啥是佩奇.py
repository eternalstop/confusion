# _*_coding=utf-8_*_

import turtle as t
import math as m


def big_circle(x, y):
	t.color(220, 220, 220)
	t.penup()
	t.goto(x, y)
	t.seth(90)
	t.pd()
	t.circle(200, -360)
	t.begin_fill()
	t.color(0, 0, 255)
	t.seth(0)
	
	
def circle(x, y):
	t.color(0, 0, 0)
	t.penup()
	t.goto(x, y)
	t.seth(90)
	t.pd()
	t.circle(192, -360)
	t.begin_fill()
	t.color(0, 0, 255)
	t.seth(0)
	

def face(x, y):
	t.color(0, 0, 0)
	t.penup()
	t.goto(x, y)
	t.seth(90)
	t.pd()
	t.circle(160, -60)
	t.circle(160, -60)
	t.begin_fill()
	t.color(0, 0, 255)
	t.seth(0)
	t.pu()
	t.fd(160)
	t.seth(-90)
	t.fd(140)
	t.pd()
	t.bk(140)
	
	
def nose(x, y):
	t.pensize(5)
	t.colormode(255)
	t.color((255, 0, 0), (255, 0, 0))
	t.hideturtle()
	t.penup()
	t.goto(x, y)
	t.seth(90)
	t.pd()
	t.begin_fill()
	t.circle(20, -360)
	t.seth(0)
	t.end_fill()
	
	t.pu()
	t.bk(16)
	t.seth(90)
	t.fd(6)
	t.begin_fill()
	t.color(255, 250, 250)
	t.circle(7, -360)
	t.seth(0)
	t.end_fill()
	
	
def setting():
	t.pensize(8)
	t.hideturtle()
	t.colormode(255)
	t.setup(800, 600)
	t.speed(10)
	

if __name__ == '__main__':
	setting()
	big_circle(200, 0)
	circle(192, 0)
	face(160, 0)
	nose(30, 50)
	t.done()
