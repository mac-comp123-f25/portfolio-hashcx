import turtle


def drawAll():
    win = turtle.Screen()
    win.bgcolor("light sky blue")

    sepalTurtle = turtle.Turtle()
    sepalTurtle.speed(0)
    sepalTurtle.color("dark green", "spring green")
    sepalTurtle.hideturtle()

    petalTurtle = turtle.Turtle()
    petalTurtle.speed(0)
    petalTurtle.color('dark red', 'light coral')
    petalTurtle.hideturtle()

    centerTurtle = turtle.Turtle()
    centerTurtle.speed(0)
    centerTurtle.color('purple4')
    centerTurtle.hideturtle()

    stampTurtle = turtle.Turtle()
    stampTurtle.color("gold")
    stampTurtle.speed(0)
    stampTurtle.shape("turtle")
    stampTurtle.hideturtle()

    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 0)
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, 220)
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 220, 0)
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, 0, -220)
    drawFlower(sepalTurtle, petalTurtle, centerTurtle, stampTurtle, -220, 0)

    win.exitonclick()


def drawFlower(sepalTurt, petalTurt, centerTurt, stampTurt, centerX, centerY):
    drawFiveCircles(sepalTurt, 50, centerX, centerY)
    drawFiveCircles(petalTurt, 25, centerX, centerY)
    drawCenterCircle(centerTurt, centerX, centerY - 15)
    drawBee(stampTurt, centerX - 2, centerY)


def drawFiveCircles(turt, radius, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)


def drawCenterCircle(turt, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.begin_fill()
    turt.circle(15)
    turt.end_fill()


def drawBee(turt, centerX, centerY):
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    turt.stamp()


drawAll()
