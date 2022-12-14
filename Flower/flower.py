# Rainbow flower

import turtle
import colorsys

t = turtle.Turtle()

turtle.Screen().bgcolor("black")
turtle.title("Flower")
root = turtle.Screen()._root
root.iconbitmap("./flo.ico")

t.pensize(1)
h = 0.0
turtle.tracer(2)

for i in range(100):

    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    h += 0.1
    t.circle(i*2, 100)
    t.right(90)

    for j in range(4):
        t.right(40)

t.hideturtle()
turtle.done()