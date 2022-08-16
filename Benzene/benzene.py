# Rainbow benzene

import turtle
import colorsys

t = turtle.Pen()

turtle.Screen().bgcolor("black")
turtle.title("Rainbow Benzene")
root = turtle.Screen()._root
root.iconbitmap("./hexagon.ico")

t.speed(15)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

h = 0.0

for i in range(360):

    c = colors[i%6]
    t.pencolor(c)
    h += 0.01
    t.width(i//100 + 1)
    t.forward(i)
    t.left(59.5)

t.hideturtle()
turtle.done()