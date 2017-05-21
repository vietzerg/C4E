import pygame


class Bullet:
    def __init__(self, plane):
        self.type = "bullet"
        self.image = pygame.image.load("resources/bullet.png")
        self.x = plane.x + plane.image.get_width() / 2 - 6
        self.y = plane.y - self.image.get_height() + 6

    def run(self):
        self.y -= 5

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))