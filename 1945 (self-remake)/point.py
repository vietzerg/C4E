import pygame

class Point:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start

    def add_vector(self, dx, dy):
        self.x += dx
        self.y += dy