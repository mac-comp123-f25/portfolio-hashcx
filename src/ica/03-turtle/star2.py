import turtle

screen = turtle.Screen()

tur = turtle.Turtle()
tur.color("red")
tur.shape("turtle")

for i in range(5):
    tur.forward(100)
    tur.left(180-36)

tur2 = turtle.Turtle()
tur2.color("blue")
tur2.shape("turtle")
tur2.penup()
tur2.goto(0,-100)
tur2.pendown()

for i in range(5):
    tur2.forward(100)
    tur2.left(180-36)

screen.exitonclick()
