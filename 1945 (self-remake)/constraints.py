import pygame

def clamp1(value, upper, lower):
    value = min(value, upper)
    value = max(value, lower)
    return value

class Constraints:
    def __init__(self, x_min, x_max, y_min, y_max, an_object):
        self.x_min = x_min
        self.x_max = x_max - an_object.renderer.images["main"].get_width()
        self.y_min = y_min
        self.y_max = y_max - an_object.renderer.images["main"].get_height()

    # PICK THE MIDDLE VALUE OF A SET OF 3 NUMBERS
    def clamp(self,value, lower, upper):
        value = max(value, lower)
        value = min(value, upper)
        return value

    def constrain(self, position):
        position.x = self.clamp(position.x, self.x_min, self.x_max)
        position.y = self.clamp(position.y, self.y_min, self.y_max)