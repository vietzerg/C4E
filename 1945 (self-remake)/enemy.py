import pygame
#import playerbullet
import time
import point
import renderer
import boxcollider
from physics_manager import *

class Enemy:
    def __init__(self, x_start, y_start):
        self.type = "plane"
        self.alive = True
        self.death_ticker = 0
        self.renderer = renderer.SpriteRenderer(self, "enemy", ["main", "explosion"])
        self.position = point.Point(x_start, y_start)
        self.constraints = None
        self.box_collider = boxcollider.BoxCollider(self.position, self.renderer.width, self.renderer.height)
        physicsmanager.add(self)
        #gamemanager.add(self) WHY CAN'T I DO IT LIKE THIS

    def delete(self):
        del self

    def run(self):
        # HANDLE RUNNING LOGIC
        self.renderer.alive = self.alive
        if not self.alive:
            self.death_ticker = min(self.death_ticker + 1, 36)
        self.renderer.death_ticker = self.death_ticker
        self.position.add_vector(0, 3)

    # HANDLE ONLY DRAWING OF PLAYER ON MAP
    def draw(self, screen):
        self.renderer.draw(screen, self.position)

