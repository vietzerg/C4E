import pygame
import renderer
import point

class Background:
    def __init__(self, x_start, y_start):
        self.alive = True
        self.type = "background"
        self.death_ticker = None
        self.position = point.Point(x_start, y_start)
        self.renderer = renderer.SpriteRenderer(self, "background", ["main"])
        self.position1 = point.Point(x_start, - self.renderer.images["main"].get_height())

    # RUN CORE LOGIC FIRST, x, y POSITIONS
    def run(self):
        self.position.add_vector(0, 5)
        self.position1.add_vector(0, 5)
        if self.position1.y >= 0:
            self.position.y = - 5
            self.position1.y = -self.renderer.images["main"].get_height()

    # HANDLE ONLY DRAWINGS ON MAP
    def draw(self, screen):
        self.renderer.draw(screen, self.position)
        self.renderer.draw(screen, self.position1)