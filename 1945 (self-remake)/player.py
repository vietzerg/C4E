import pygame
from input_manager import *
from game_manager import gamemanager
import playerbullet
import point
import renderer

class Player:
    def __init__(self, x_start, y_start):
        self.type = "plane"
        self.alive = True
        self.death_ticker = -1
        self.renderer = renderer.SpriteRenderer(self, "player", ["main", "explosion"])
        self.position = point.Point(x_start - self.renderer.width / 2, y_start)
        self.constraints = None

        #gamemanager.add(self) WHY CAN'T I DO IT LIKE THIS

    def shoot(self):
        if inputmanager.space_pressed:
            #print ("SPACE")
            a_bullet = playerbullet.PlayerBullet(self)
            gamemanager.add(a_bullet)

    def move(self):
        if inputmanager.up_pressed:
            self.position.add_vector(0, -5)
        if inputmanager.down_pressed:
            self.position.add_vector(0, 5)
        if inputmanager.left_pressed:
            self.position.add_vector(-5, 0)
        if inputmanager.right_pressed:
            self.position.add_vector(5, 0)
        # LIMIT PLANE IN MAP BORDER
        if self.constraints is not None:
            self.constraints.constrain(self.position)

    def run(self):
        self.move()
        self.shoot()

    # HANDLE ONLY DRAWING OF PLAYER ON MAP
    def draw(self, screen):
        self.renderer.draw(screen, self.position)
