import pygame

class Background:
    def __init__(self):
        self.type = "background"
        self.image = pygame.image.load("resources/background.png")
        self.x = -5
        self.y = -5
        self.y2 = -self.image.get_height()

    # RUN CORE LOGIC FIRST, x, y POSITIONS
    def run(self):
        self.y += 5
        self.y2 += 5
        if self.y2 >= 0:
            self.y = - 5
            self.y2 = -self.image.get_height()

    # HANDLE ONLY DRAWINGS ON MAP
    def draw(self, screen):
        screen.blit(self.image, (self.x , self. y))
        screen.blit(self.image, (self.x , self. y2))