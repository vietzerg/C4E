import pygame
import bullet
import time

class Enemy:
    def __init__(self, x_start, y_start):
        self.type = "plane"
        self.image = pygame.image.load("resources/plane1.png")
        self.explosheet = pygame.image.load("resources/explosion.png")
        self.x = x_start - self.image.get_width() / 2
        self.y = y_start - self.image.get_height() / 2
        self.alive = True
        self.dead_ticker = -1

        #gamemanager.add(self) WHY CAN'T I DO IT LIKE THIS

    def delete(self):
        del self

    def run(self):
        # HANDLE RUNNING LOGIC
        if not self.alive:
            self.dead_ticker += 1
        self.y += 3

    def extract_animations(self):
        step = self.explosheet.get_width() / 6
        result = []
        #self.explosheet.convert()
        for i in range(1, 7):
            frame = self.explosheet.subsurface((step*(i-1) + 1, 1, 32, 32))
            frame.set_colorkey((255,255,255))
            frame.convert_alpha()
            result.append(frame)
        return result

    # HANDLE ONLY DRAWING OF PLAYER ON MAP
    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, (self.x , self. y))
        else:
            explo_frames = self.extract_animations()
#            if self.dead_ticker >= 5:
#                self.dead_ticker = 5
            screen.blit(explo_frames[self.dead_ticker], (self.x, self.y))
            #print (len(explo_frames))

