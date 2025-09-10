import turtle

screen = turtle.Screen()
screen.setup(width=500, height=500, startx=0, starty=0)

turt = turtle.Turtle()
turt.color("red")

turt.begin_fill()
n = 5
for i in range(n):
    turt.forward(100)
    turt.left(360 / n)
turt.end_fill()

screen.exitonclick()
