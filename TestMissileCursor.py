from turtle import Turtle
import turtle

from MissileCursor import MissileCursor

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