# Pacman Shape with Python and Turtle
# https://pythonturtle.academy/pacman-shape-with-python-and-turtle/

import turtle

screen = turtle.Screen()
screen.setup(width=500, height=500, startx=0, starty=0)

turt = turtle.Turtle()
turt.pencolor("black")
turt.fillcolor("yellow")
turt.hideturtle()

radius = 100

# move turtle to middle of screen
turt.penup()
turt.goto(-radius, radius / 2)
turt.pendown()

# orient turtle
turt.right(30)

# draw pacman
turt.begin_fill()
turt.right(90)
turt.circle(radius, -300)
turt.left(90)
turt.forward(radius)
turt.left(120)
turt.forward(radius)
turt.end_fill()

screen.exitonclick()
