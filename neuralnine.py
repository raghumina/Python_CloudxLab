import math
from tkinter import *

ee = 0.44
x1 = y1 = y2 = 0
x2 = 10
x3 = 5
y3 = 5 * math.sqrt(3)

PrevX = 0
PrevY = 150


def scale(x, y, xx, yy):
    x = x * 20 + 100
    y = y * 20 + 100
    xx = xx * 20 + 100
    yy = yy * 20 + 100
    return (x, y, xx, yy)


root = Tk()
root.title("Trigno fun1")
canvas = Canvas(width=400, height=300, bg='white')
canvas.create_line(scale(x1, y1, x2, y2), fill='red')
canvas.create_line(scale(x2, y2, x3, y3), fill='red')
canvas.create_line(scale(x3, y3, x1, y1), fill='red')
