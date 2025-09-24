import turtle


def draw_nested_squares(turt):
    for i in range(10, 80, 10):
        for j in range(4):
            turt.forward(i)
            turt.left(90)


scr = turtle.Screen()
tur = turtle.Turtle()
draw_nested_squares(tur)
scr.exitonclick()
