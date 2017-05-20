class GameManager():
	"""docstring for GameManager"""
	def __init__(self):
		self.game_objects = []
		pass

	def add(self, game_object):
		self.game_objects.append(game_object)

	def run(self):
		for game_object in self.game_objects:
			game_object.run()

	def draw(self, screen):
		for game_object in self.game_objects:
			game_object.draw(screen)

game_manager = GameManager()