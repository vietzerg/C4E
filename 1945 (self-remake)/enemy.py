import pygame
import bullet

class Enemy:
    def __init__(self, x_start, y_start):
        self.type = "plane"
        self.image = pygame.image.load("resources/plane1.png")
        self.x = x_start - self.image.get_width() / 2
        self.y = y_start - self.image.get_height() / 2
        self.alive = True

        #gamemanager.add(self) WHY CAN'T I DO IT LIKE THIS

    def run(self):
        # HANDLE RUNNING LOGIC
        self.y += 7

    # HANDLE ONLY DRAWING OF PLAYER ON MAP
    def draw(self, screen):
        screen.blit(self.image, (self.x , self. y))

