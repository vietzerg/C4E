import pygame
from input_manager import *
from game_manager import gamemanager
import bullet


class Player:
    def __init__(self, x_start, y_start):
        self.type = "plane"
        self.image = pygame.image.load("resources/player.png")
        self
        self.x = x_start - self.image.get_width() / 2
        self.y = y_start - self.image.get_height() / 2
        self.alive = True

        #gamemanager.add(self) WHY CAN'T I DO IT LIKE THIS

    def run(self):
        # HANDLE INPUT HERE
        if self.main == True:
            if inputmanager.up_pressed:
                self.y -= 3
            if inputmanager.down_pressed:
                self.y += 3
            if inputmanager.left_pressed:
                self.x -= 3
            if inputmanager.right_pressed:
                self.x += 3
            if inputmanager.space_pressed:
                a_bullet = bullet.Bullet(self)
                gamemanager.add(a_bullet)

    # HANDLE ONLY DRAWING OF PLAYER ON MAP
    def draw(self, screen):
        screen.blit(self.image, (self.x , self. y))

