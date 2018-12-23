import os
import turtle

BASE_PATH = os.path.dirname(__file__)
MISSILE_PATH = os.path.join(BASE_PATH, "images", "missile.gif")

class Missile:
    def __init__(self, x, y, color, x2, y2):
        self.x = x
        self.y = y
        self.color = color

        pen = turtle.Turtle(visible=False)
        missile_conf = 'missile_{0}'.format(color)
        pen.shape(missile_conf)

        pen.speed(0)
        pen.color(color)
        pen.penup()
        pen.setpos(x=x, y=y)
        pen.pendown()
        towards = pen.towards(x2, y2)
        # pen.right(90)
        pen.setheading(towards)
        pen.showturtle()
        self.pen = pen

        self.state = 'launched'
        self.target = x2, y2
        self.radius = 0

    def step(self):
        if self.state == 'launched':
            self.pen.forward(4)

            if self.pen.distance(x=self.target[0], y=self.target[1]) < 20:
                self.state = 'explode'
                self.pen.shape('circle')
        elif self.state == 'explode':
            self.radius += 1
            if self.radius > 5:
                self.pen.clear()
                self.pen.hideturtle()
                self.state = 'dead'
            else:
                self.pen.shapesize(self.radius)
        elif self.state == 'dead':
            self.pen.clear()
            self.pen.hideturtle()

    @property
    def get_x(self):
        return self.pen.xcor()

    @property
    def get_y(self):
        return self.pen.ycor()

    def distance(self, x, y):
        return self.pen.distance(x, y)