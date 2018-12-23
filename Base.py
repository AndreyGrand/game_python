import os
import turtle

class Building:
    def get_img_name(self):
        None

    def draw(self):
        pic_name = self.get_img_name()
        pic_path = os.path.join(self.BASE_PATH, "images", pic_name)
        if self.pen.shape() != pic_path:
            self.window.register_shape(pic_path)
            self.pen.shape(pic_path)

    def __init__(self, name, x, y, window, health=500):
        self.BASE_PATH = os.path.dirname(__file__)
        self.initial_health = health
        self.window = window
        self.health = health
        self.name = name
        self.img = 1
        building = turtle.Turtle()
        building.hideturtle()
        building.speed(0)
        building.penup()
        building.setpos(x=x, y=y)
        pic_path = os.path.join(self.BASE_PATH, "images", self.get_img_name())
        self.window.register_shape(pic_path)
        building.shape(pic_path)
        building.showturtle()
        self.pen = building
        title = turtle.Turtle(visible=False)
        title.speed(0)
        title.penup()
        title.setpos(x=x, y=y - 85)
        title.color('white')
        title.write(str(self.health), align="center", font=["Arial", 20, "bold"])
        self.title = title

    @property
    def x(self):
        return self.pen.xcor()

    @property
    def y(self):
        return self.pen.ycor()

    def is_dead(self):
        return self.health <= 0

    def check_impact(self, x, y, enemy_missile_radius):
        targeted = False
        if self.pen.distance(x, y) < enemy_missile_radius * 10:
            targeted = True
            self.health -= 100
            self.title.clear()
            self.title.write(str(self.health), align="center", font=["Arial", 20, "bold"])

        return targeted


class Base(Building):
    # def get_img_name(self):
    #     return f"{self.name}.gif"
    def __init__(self, name, x, y, window, health=500):
        self.our_missiles = []
        Building.__init__(self, name=name, window=window, x=x, y=y, health=health)
        print(len(self.missiles))

    def get_img_name(self):
        for missile in self.missiles:
            if missile.distance(self.x, self.y) < 80:
                pic_name = f"{self.name}_opened.gif"
                break
        else:
            pic_name = f"{self.name}.gif"
        return pic_name

    @property
    def missiles(self):
        return self.our_missiles