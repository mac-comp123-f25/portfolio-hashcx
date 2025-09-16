import turtle
import math

def drawFiveCircles(turt, radius, centerX, centerY):
    """
    Draw 5 circles
    :param turt: Turtle object to draw the circles
    :param radius: circle radius
    :param centerX: circle center on x-axis
    :param centerY: circle center on y-axis
    :return: None
    """
    turt.up()
    turt.goto(centerX, centerY)
    turt.down()
    for i in range(5):
        turt.begin_fill()
        turt.circle(radius)
        turt.end_fill()
        turt.left(72)


def drawCenterCircle(turt, centerX, centerY):
    """
    Draw circle

    :param turt:
    :param centerX:
    :param centerY:
    :return:
    """
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

drawFiveCircles(sepalTurtle, 50, 0, 0)
drawFiveCircles(petalTurtle, 25, 0, 0)
drawCenterCircle(centerTurtle, 0, -15)
drawBee(stampTurtle, -2, 0)

drawFiveCircles(sepalTurtle, 50, 0, 220)
drawFiveCircles(petalTurtle, 25, 0, 220)
drawCenterCircle(centerTurtle, 0, 205)
drawBee(stampTurtle, -2, 220)

drawFiveCircles(sepalTurtle, 50, 220, 0)
drawFiveCircles(petalTurtle, 25, 220, 0)
drawCenterCircle(centerTurtle, 220, -15)
drawBee(stampTurtle, 218, 0)

drawFiveCircles(sepalTurtle, 50, 0, -220)
drawFiveCircles(petalTurtle, 25, 0, -220)
drawCenterCircle(centerTurtle, 0, -235)
drawBee(stampTurtle, -2, -220)

drawFiveCircles(sepalTurtle, 50, -220, 0)
drawFiveCircles(petalTurtle, 25, -220, 0)
drawCenterCircle(centerTurtle, -220, -15)
drawBee(stampTurtle, -222, 0)

win.exitonclick()
