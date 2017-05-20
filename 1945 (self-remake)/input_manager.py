import pygame

class InputManager:
    def __init__(self):
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

    def run(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.up_pressed = True
                elif event.key == pygame.K_DOWN:
                    self.down_pressed = True
                elif event.key == pygame.K_LEFT:
                    self.left_pressed = True
                elif event.key == pygame.K_RIGHT:
                    self.right_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up_pressed = False
                elif event.key == pygame.K_DOWN:
                    self.down_pressed = False
                elif event.key == pygame.K_LEFT:
                    self.left_pressed = False
                elif event.key == pygame.K_RIGHT:
                    self.right_pressed = False