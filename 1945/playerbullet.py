import pygame

class PlayerBullet(object):
	"""docstring for PlayerBullet"""
	def __init__(self):
		self.x = 0
		self.y = 0
		self.image = pygame.image.load("resources/bullet.png")

	def run(self):
		self.y -= 5

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))