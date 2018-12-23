import os

from Base import Building

class DestroyableBase(Building):
    def __init__(self, name,window, x, y, health):
        Building.__init__(self, name=name, x=x, y=y, window=window, health=health)

    def get_img_name(self):
        return f"{self.name}_{self.img}.gif"

    def check_impact(self, x, y, enemy_missile_radius):
        result = Building.check_impact(self, x, y, enemy_missile_radius)
        if result:
            img_num = self.img
            if self.health * 0.5 >= self.health > 0:
                img_num = 2
            elif self.health == 0:
                img_num = 3
            if img_num != self.img:
                self.img = img_num
                pic_path = os.path.join(self.BASE_PATH, "images", self.get_img_name())
                self.window.register_shape(pic_path)
                self.pen.shape(pic_path)
        return result