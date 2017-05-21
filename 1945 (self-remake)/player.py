import pygame
from input_manager import *
from game_manager import gamemanager
import bullet


class Player:
    def __init__(self, x_start, y_start):
        self.type = "plane"
        self.image = pygame.image.load("resources/player.png")
        self.explosheet = pygame.image.load("resources/explosion.png")
        self.x = x_start - self.image.get_width() / 2
        self.y = y_start - self.image.get_height() / 2
        self.alive = True
        self.dead_ticker = -1

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

    def extract_animations(self):
        result = []
        #self.explosheet.convert()
        for i in range(6):
            result.append(self.explosheet.subsurface((33*i, 0, 33, 33)))
        return result

    # HANDLE ONLY DRAWING OF PLAYER ON MAP
    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, (self.x , self. y))
        else:
            explo_frames = self.extract_animations()
            i = 0
            screen.blit(explo_frames[i], (self.x, self.y))

