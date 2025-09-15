import turtle

def turtle_square(sqTurt, side_length):
    for i in range(4):
        sqTurt.forward(side_length)
        sqTurt.left(90)


win = turtle.Screen()
tt = turtle.Turtle()
turtle_square(tt, 50)
turtle_square(tt, 10)
turtle_square(tt, 73)
win.exitonclick()
