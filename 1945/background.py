import pygame

class Background():
	"""docstring for Background"""
	def __init__(self):
		self.image = pygame.image.load("resources/background.png")
		self.x = 0
		self.y = 0
		self.y2 = -self.image.get_height()

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y2))
		screen.blit(self.image, (self.x, self.y))
		self.y += 5
		self.y2 += 5
		if self.y2 >= 0:
			self.y = 0
			self.y2 = -self.image.get_height()

	def run(self):
		pass