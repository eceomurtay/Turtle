import turtle
import colorsys

dist = 400
h = 0

def triangle():

    global dist, h
    
    for i in range(40):
    
        col = colorsys.hsv_to_rgb(h, 1, 0.6)
        h += (1/100)
        t.color(col)
        # move the turtle forward by dist
        t.forward(dist)
        # change the direction of turtle by 120 degrees to the left
        t.left(120)
        
        dist -= 10


t = turtle.Turtle()

root = turtle.Screen()._root
root.iconbitmap("./tri.ico")

turtle.title("Triangle")
t.screen.bgcolor("black")

t.penup()
t.goto(-200, -100)
t.pendown()
t.speed(10)

triangle()
triangle()

t.hideturtle()

turtle.up()
turtle.setpos(0, -300)
turtle.down()

turtle.hideturtle()
turtle.color("white")
turtle.write("Done !", move=False, align="center", font=('Verdana', 20))

turtle.done()
