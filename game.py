import os
import random
import threading
import turtle

from Base import Base
from DestroyableBase import DestroyableBase
from Missile import Missile, MISSILE_PATH

BASE_PATH = os.path.dirname(__file__)
window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.screensize(1200, 800)
window.tracer(n=2)

BASE_X, BASE_Y = 0, -300
ENEMY_Y = 400
ENEMY_COUNT = 5
BASES = {
    "base": {'x': BASE_X, 'y': BASE_Y, 'health': 1000},
}

BUILDINGS = {
    "house": {'x': BASE_X - 400, 'y': BASE_Y, 'health': 300},
    "kremlin": {'x': BASE_X - 200, 'y': BASE_Y, 'health': 2000},
    "nuclear": {'x': BASE_X + 400, 'y': BASE_Y, 'health': 700},
    "skyscraper": {'x': BASE_X + 200, 'y': BASE_Y, 'health': 500}
}


class Game:
    global window

    def __init__(self):
        self.our_missiles = []
        self.enemy_missiles = []
        self.our_base = []
        self.rocket_base = None

    def create_missile(self, color, x, y, x2, y2):
        return Missile(x=x, y=y, color=color, x2=x2, y2=y2)

    def fire_enemy_missile(self, x, y):
        target_position = random.randint(1, len(self.our_base))
        target = self.our_base[target_position - 1]
        self.enemy_missiles.append(self.create_missile('red', x, y, target.x, target.y))

    def move_missile(self, missiles):
        for missile in missiles:
            missile.step()
            if missile.state == 'dead':
                missile.pen.clear()
                missile.pen.hideturtle()

    def clear_dead(self, missiles_collection):
        dead_missiles = [info for info in missiles_collection if info.state == 'dead']
        for dead in dead_missiles:
            missiles_collection.remove(dead)

    def check_interceptions(self, ):
        for our_info in self.our_missiles:
            if our_info.state != 'explode':
                continue
            for enemy_info in self.enemy_missiles:
                enemy_missile = enemy_info.pen
                if enemy_missile.distance(our_info.pen.xcor(), our_info.pen.ycor()) < (our_info.radius * 10):
                    enemy_info.state = 'dead'

    def check_impact(self, ):
        for enemy_missile in self.enemy_missiles:
            if enemy_missile.state != 'explode':
                continue
            for building in self.our_base:
                if building.check_impact(enemy_missile.get_x, enemy_missile.get_y, enemy_missile.radius):
                    enemy_missile.state = 'dead'
                    break

    def game_over(self, ):
        return len(self.our_base) == 0

    def clear_destroyed_buildings(self, ):
        for building in self.our_base:
            if building.is_dead():
                self.our_base.remove(building)

    def check_enemy(self, ):
        if len(self.enemy_missiles) < 5:
            x_enemy = random.randint(-600, 600)
            self.fire_enemy_missile(x_enemy, ENEMY_Y)

    def draw_buildings(self, ):
        for building in self.our_base:
            building.draw()

    def fire_missile(self, x, y):
        if (len(self.enemy_missiles) > 2* len(self.our_missiles) and not self.rocket_base.is_dead() ):
            self.our_missiles.append(self.create_missile('white', BASE_X, BASE_Y + 30, x, y))
        # threading.Thread(name='buildings', target=draw_buildings).run()

    def base_set_up(self):
        window.clear()
        window.register_shape(MISSILE_PATH)
        window.bgpic(os.path.join(BASE_PATH, "images", "background.png"))
        # for build_name, build_prop in BASES.items():
        base = Base(name="base", x=BASE_X, y=BASE_Y, health=1000,
                    window=window, )
        self.rocket_base=base
        self.our_base.append(base)
        self.our_missiles = base.missiles

        for build_name, build_prop in BUILDINGS.items():
            self.our_base.append(DestroyableBase(name=build_name, x=build_prop.get('x'), y=build_prop.get('y'),
                                            health=build_prop.get('health'), window= window))

    def run(self):
        # window.tracer(n=2)
        window.onclick(self.fire_missile)
        while True:
            window.update()

            if self.game_over():
                break

            self.draw_buildings()
            self.check_impact()
            # check_enemy()
            threading.Thread(name='buildings', target=self.draw_buildings).run()
            threading.Thread(name='fire_enemy', target=self.check_enemy).run()
            threading.Thread(name='check_interceptions', target=self.check_interceptions).run()

            # check_interceptions()
            self.clear_destroyed_buildings()
            threading.Thread(name='our_missiles', target=self.move_missile, args=[self.our_missiles]).run()
            threading.Thread(name='enemy_missiles', target=self.move_missile, args=[self.enemy_missiles]).run()
            # move_missile(our_missiles)
            # move_missile(enemy_missiles)

            self.clear_dead(self.our_missiles)
            self.clear_dead(self.enemy_missiles)

        pen = turtle.Turtle(visible=False)
        pen.speed(0)
        pen.penup()
        pen.color('white')
        pen.write('Game over', align="center", font=["Arial", 80, "bold"])

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
        turtle.addshape("missile", shape=missile)
        del temporary
        screen.delay(delay)

while True:
    game = Game()
    game.base_set_up()
    game.run()
    answer = window.textinput(title='Привет!', prompt='Хотите сыграть еще? д/н')
    if answer.lower() not in ('д', 'да', 'y', 'yes'):
        break
