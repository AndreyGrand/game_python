from turtle import *
from turtle import Turtle
import turtle

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
        t.goto(pl[0][0],pl[0][1])
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
        body = self.polyRectangle(temporary, 0,0,20,8)
        missile.addcomponent(body, self.color, 'black')
        left_eleron = ((-4,-20),(0,-20),(0,-12),(-4,-16))
        missile.addcomponent(left_eleron, self.color, 'black')
        right_eleron = ((12,-20),(8,-20),(8,-12),(12,-16))
        missile.addcomponent(right_eleron, self.color, 'black')
        nouse = ((0,0),(4,4),(8,0))
        missile.addcomponent(nouse, self.color, 'black')
        fire = ((2,-20),(4,-32),(6,-20))
        missile.addcomponent(fire, 'red', 'red')
        name = 'missile_{0}'.format(self.color)
        turtle.addshape(name, shape = missile)
        del temporary
        screen.delay(delay)

yellowMissile = MissileCursor('yellow')

def moveforward():    #I cannot get this function to work
    yellowMissile.left(90)
    yellowMissile.forward(40)

def movebackward():    #I cannot get this function to work
    yellowMissile.left(90)
    yellowMissile.backward(40)

def moveright():
    yellowMissile.forward(40)

def moveleft():
    yellowMissile.backward(40)


yellowMissile.prepareMissile()  # creates and registers the "missile" cursor shape
msl = turtle
msl.shape("missile_yellow")

blueMissile =  MissileCursor('blue')
blueMissile.prepareMissile()

turtle.up()  # get rid of the ink
screen = turtle.Screen()

t = Turtle()
#Background color
t.screen.bgcolor("green")
# t.penup()
# t.goto(0,0)
# t.pendown()
# t.color('red')
# t.goto(40,10)
# Movement of tank
screen = turtle.Screen()
# screen.onkeypress(lambda : turtle.right(90), "Right")
# screen.onkeypress(lambda : turtle.left(90), "Left")
# screen.onkeypress(lambda : turtle.forward(40), "Up")
# screen.onkeypress(lambda : turtle.backward(40), "Down")
#
# turtle.listen()

turtle.forward(100)
msl.shape("missile_blue")
turtle.forward(100)
turtle.mainloop()