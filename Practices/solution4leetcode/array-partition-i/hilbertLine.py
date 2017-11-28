# encoding=utf-8

from tkinter import *


def show_order(startx, starty, shape, order):
    global segx, segy
    if order == 1:
        if shape == 1:
            canvas.create_line(10 + startx * segx, 10 + starty * segy,
                               10 + startx * segx, 10 + (starty + 1) * segy,
                               tags="pic")
            canvas.create_line(10 + startx * segx, 10 + (starty + 1) * segy,
                               10 + (startx + 1) * segx, 10 + (starty + 1) * segy,
                               tags="pic")
            canvas.create_line(10 + (startx + 1) * segx, 10 + (starty + 1) * segy,
                               10 + (startx + 1) * segx, 10 + starty * segy,
                               tags="pic")
        elif shape == 2:
            canvas.create_line(10 + startx * segx, 10 + starty * segy,
                               10 + (startx + 1) * segx, 10 + starty * segy,
                               tags="pic")
            canvas.create_line(10 + (startx + 1) * segx, 10 + starty * segy,
                               10 + (startx + 1) * segx, 10 + (starty + 1) * segy,
                               tags="pic")
            canvas.create_line(10 + (startx + 1) * segx, 10 + (starty + 1) * segy,
                               10 + startx * segx, 10 + (starty + 1) * segy,
                               tags="pic")
        elif shape == 3:
            canvas.create_line(10 + startx * segx, 10 + (starty + 1) * segy,
                               10 + startx * segx, 10 + starty * segy,
                               tags="pic")
            canvas.create_line(10 + startx * segx, 10 + starty * segy,
                               10 + (startx + 1) * segx, 10 + starty * segy,
                               tags="pic")
            canvas.create_line(10 + (startx + 1) * segx, 10 + starty * segy,
                               10 + (startx + 1) * segx, 10 + (starty + 1) * segy,
                               tags="pic")
        elif shape == 4:
            canvas.create_line(10 + (startx + 1) * segx, 10 + starty * segy,
                               10 + startx * segx, 10 + starty * segy,
                               tags="pic")
            canvas.create_line(10 + startx * segx, 10 + starty * segy,
                               10 + startx * segx, 10 + (starty + 1) * segy,
                               tags="pic")
            canvas.create_line(10 + startx * segx, 10 + (starty + 1) * segy,
                               10 + (startx + 1) * segx, 10 + (starty + 1) * segy,
                               tags="pic")
    else:
        if shape == 1:
            show_order(startx, starty, 2, order-1)
            canvas.create_line(10 + startx * segx, 10 + (starty + EXP[order-1] - 1) * segy,
                               10 + startx * segx, 10 + (starty + EXP[order-1]) * segy,
                               tags="pic")
            show_order(startx, starty + EXP[order-1], 1, order-1)
            canvas.create_line(10 + (startx + EXP[order-1] - 1) * segx, 10 + (starty + EXP[order-1]) * segy,
                               10 + (startx + EXP[order-1]) * segx, 10 + (starty + EXP[order-1]) * segy,
                               tags="pic")
            show_order(startx + EXP[order-1], starty + EXP[order-1], 1, order-1)
            canvas.create_line(10 + (startx + EXP[order] - 1) * segx, 10 + (starty + EXP[order-1]) * segy,
                               10 + (startx + EXP[order] - 1) * segx, 10 + (starty + EXP[order-1] - 1) * segy,
                               tags="pic")
            show_order(startx + EXP[order-1], starty, 4, order-1)
        elif shape == 2:
            show_order(startx, starty, 1, order-1)
            canvas.create_line(10 + (startx + EXP[order-1] - 1) * segx, 10 + starty * segy,
                               10 + (startx + EXP[order-1]) * segx, 10 + starty * segy,
                               tags="pic")
            show_order(startx + EXP[order-1], starty, 2, order-1)
            canvas.create_line(10 + (startx + EXP[order-1])*segx, 10 + (starty + EXP[order-1] - 1) * segy,
                               10 + (startx + EXP[order-1])*segx, 10 + (starty + EXP[order-1]) * segy,
                               tags="pic")
            show_order(startx + EXP[order-1], starty + EXP[order-1], 2, order-1)
            canvas.create_line(10 + (startx + EXP[order-1] - 1) * segx, 10 + (starty + EXP[order] - 1)*segy,
                               10 + (startx + EXP[order-1]) * segx, 10 + (starty + EXP[order] - 1) * segy,
                               tags="pic")
            show_order(startx, starty + EXP[order-1], 3, order-1)
        elif shape == 3:
            show_order(startx, starty + EXP[order-1], 2, order-1)
            canvas.create_line(10 + startx * segx, 10 + (starty + EXP[order-1]) * segy,
                               10 + startx * segx, 10 + (starty + EXP[order-1] - 1) * segy,
                               tags="pic")
            show_order(startx, starty, 3, order-1)
            canvas.create_line(10 + (startx + EXP[order-1] - 1) * segx, 10 + (starty + EXP[order-1] - 1) * segy,
                               10 + (startx + EXP[order-1]) * segx, 10 + (starty + EXP[order-1] - 1) * segy,
                               tags="pic")
            show_order(startx + EXP[order-1], starty, 3, order-1)
            canvas.create_line(10 + (startx + EXP[order] - 1) * segx, 10 + (starty + EXP[order-1] - 1) * segy,
                               10 + (startx + EXP[order] - 1) * segx, 10 + (starty + EXP[order-1]) * segy,
                               tags="pic")
            show_order(startx + EXP[order-1], starty + EXP[order-1], 4, order-1)
        elif shape == 4:
            show_order(startx + EXP[order-1], starty, 1, order-1)
            canvas.create_line(10 + (startx + EXP[order-1])*segx, 10 + starty*segy,
                               10 + (startx + EXP[order-1] - 1) * segx, 10 + starty * segy,
                               tags="pic")
            show_order(startx, starty, 4, order-1)
            canvas.create_line(10 + (startx + EXP[order-1] - 1) * segx, 10 + (starty + EXP[order-1] - 1) * segy,
                               10 + (startx + EXP[order-1] - 1) * segx, 10 + (starty + EXP[order-1]) * segy,
                               tags="pic")
            show_order(startx, starty+EXP[order-1], 4, order-1)
            canvas.create_line(10 + (startx + EXP[order-1] - 1) * segx, 10 + (starty + EXP[order] - 1) * segy,
                               10 + (startx + EXP[order-1]) * segx, 10 + (starty + EXP[order] - 1) * segy,
                               tags="pic")
            show_order(startx + EXP[order-1], starty + EXP[order-1], 3, order-1)


def display():
    if ord1.get() == "":
        return

    canvas.delete("pic")
    global segx, segy
    segx = (WIDTH - 20) / (EXP[int(ord1.get())] - 1)
    segy = (HEIGHT - 20) / (EXP[int(ord1.get())] - 1)
    show_order(0, 0, 1, int(ord1.get()))


segx = None
segy = None
EXP = 10 * [1]
for i in range(1, 10):
    EXP[i] = EXP[i-1] * 2
WIDTH = 700
HEIGHT = 700
window = Tk()
window.title("希尔伯特曲线")
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
frame = Frame(window)
frame.pack(anchor=W)
lbl1 = Label(frame, text="Enter the order: ")
lbl1.pack(side=LEFT)
ord1 = StringVar()
entry1 = Entry(frame, textvariable=ord1, width=10)
entry1.pack(side=LEFT)
but1 = Button(frame, text="Display", command=display)
but1.pack()
window.mainloop()
