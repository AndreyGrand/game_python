import turtle
from threading import Event, Thread

DEF_FONT = ["Arial", 20, "bold"]
class CounterMissiles:
    def __init__(self, x, y, color, caption):
        self.count = 0
        self.caption = caption
        title = turtle.Turtle(visible=False)
        title.speed(0)
        title.penup()
        title.setpos(x=x, y=y)
        title.color(color)
        self.title = title
        numbers = turtle.Turtle(visible=False)
        numbers.speed(0)
        numbers.penup()
        numbers.setpos(x=x, y=y-25)
        numbers.color(color)
        self.numbers = numbers

    def incCount(self):
        self.count += 1
        self.redraw()

    def redraw(self):
        self.title.clear()
        self.title.write(self.caption, align="center", font=DEF_FONT)
        self.numbers.clear()
        self.numbers.write(str(self.count), align= "center", font=DEF_FONT)

class TimeCounter(CounterMissiles, Thread):
    def __init__(self, x, y, caption, color):
        CounterMissiles.__init__(self, x=x, y=y, caption = caption, color= color)
        Thread.__init__(self)
        self.stopFlag = Event()


    def stop(self):
        self.stopFlag.set()

    def run(self):
        while not self.stopFlag.wait(timeout=1):
            self.numbers += 1