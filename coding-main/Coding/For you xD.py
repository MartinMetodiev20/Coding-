# turtle.write('Love')
# turtle.color('red')
#style = ('Courier', 30, 'italic')
#turtle.write('Love' , front=style, align='center')

import turtle

t = turtle. Turtle()
t.penup()
t.goto(-95, 190)
t.pendown()
t.color('black')
style = ('Courier', 60, 'italic')
t.write('Love', font= style, align='left',move=True)
t.hideturtle()

import turtle

turtle.speed(3)
turtle.bgcolor('White')
turtle.pensize(3)


def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)


turtle.color('black', 'red')
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)

func()
turtle.left(120)
func()
turtle.forward(111.6)
turtle.end_fill()
turtle.hideturtle()
turtle.done()
import turtle 
canvas= t.getscreen().getcanvas()
canvas.postscript(file="turtle_img.ps")



