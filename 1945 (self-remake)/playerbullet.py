import pygame
import renderer
import point
import boxcollider
from physics_manager import *
from enemy import Enemy

class PlayerBullet:
    def __init__(self, plane):
        self.type = "bullet"
        self.alive = True
        self.death_ticker = None
        self.renderer = renderer.SpriteRenderer(self, "player_bullet", ["main"])
        self.position = point.Point(plane.position.x + plane.renderer.width / 2 - self.renderer.width / 2, plane.position.y - self.renderer.height)
        self.box_collider = boxcollider.BoxCollider(self.position, self.renderer.width, self.renderer.height)
        #physicsmanager.add(self.box_collider)

    def run(self):
        self.position.add_vector(0, -5)
        targeted = physicsmanager.check_collision(self.box_collider)
        if type(targeted) is Enemy and targeted is not None:
            targeted.alive = False

    def draw(self, screen):
        self.renderer.draw(screen, self.position)