import pygame
import input_manager

class Player:
    def __init__(self):
        self.image = pygame.image.load("resources/player.png")
        self.x = 300 - self.image.get_width() / 2
        self.y = 400 - self.image.get_height() / 2

    def run(self):
        # HANDLE INPUT HERE
        pass

    # HANDLE ONLY DRAWING OF PLAYER ON MAP
    def draw(self, screen):
        screen.blit(self.image, (self.x , self. y))