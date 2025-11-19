import turtle

screen = turtle.Screen()

turt = turtle.Turtle()
turt.color("red")

turt.begin_fill()
for i in range(3):
    turt.forward(100)
    turt.left(120)
turt.end_fill()

screen.exitonclick()
