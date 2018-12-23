import turtle
from turtle import Turtle


class MissileCursor:
    def __init__(self, color):
        self.pen = Turtle(visible=False)
        self.color = color

    # defining shapes
    def polySquare(self, t, x, y, length):
        t.goto(x, y)
        t.setheading(270)
        t.begin_poly()
        for count in range(4):
            t.forward(length)
            t.left(90)
        t.end_poly()
        return t.get_poly()

    def polyCircle(self, t, x, y, radius):
        t.up()
        t.goto(x, y)
        t.down()
        t.hideturtle()
        t.circle(radius)
        t.end_poly()
        return t.get_poly()

    def polyRectangle(self, t, x, y, length1, length2):
        t.goto(x, y)
        t.setheading(270)
        t.begin_poly()
        for count in range(2):
            t.forward(length1)
            t.left(90)
            t.forward(length2)
            t.left(90)
        t.end_poly()
        return t.get_poly()

    def polyPoly(self, t, pl):
        t.goto(pl[0][0], pl[0][1])
        t.setheading(270)
        t.begin_poly()
        for dot in pl:
            t.goto(dot[0], dot[1])

        t.end_poly()
        return t.get_poly()

    def drawLine(self, t, x1, x2, y1, y2):
        t.up()
        t.hideturtle()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)

    def prepareMissile(self):
        temporary = turtle.Turtle()
        temporary.color(self.color)
        screen = turtle.getscreen()
        delay = screen.delay()
        screen.delay(0)
        temporary.hideturtle()
        temporary.penup()
        missile = turtle.Shape("compound")
        body = ((0, 2), (-4, 0), (-4, -12), (-8, -16), (-8, -20), (8, -20), (8, -16), (4, -12), (4, 0))
        missile.addcomponent(body, self.color, 'black')
        fire = ((-2, -20), (0, -32), (2, -20))
        missile.addcomponent(fire, 'red', 'red')
        name = 'missile_{0}'.format(self.color)
        turtle.addshape(name, shape=missile)
        del temporary
        screen.delay(delay)
