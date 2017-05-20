import pygame
from gamemanager import *
from InputManager import *
from player import *
from background import *

loop = True

def setup_pygame():
	pygame.init()
	screen = pygame.display.set_mode((600, 800))
	pygame.display.set_caption("1945 War")
	return screen

def handle_exit_event(events):
	for event in events:
		if event.type == pygame.QUIT:
			return False
	return True

def run():
	game_manager.run()

def draw(screen):
	screen.fill((0, 0, 0))
	game_manager.draw(screen)

screen = setup_pygame()
clock = pygame.time.Clock()
game_manager.add(Background())
game_manager.add(Player())
                

while loop:
	# WE CAN ONLY GET EVENTS ONCE IN A LOOP
	events = pygame.event.get()

	# HANDLE QUIT EVENT
	for event in events:
		loop = handle_exit_event(events)

	input_manager.run(events)

	## UPDATE LOGIC
	run()

	## UPDATE GRAPHICS
	draw(screen)

	## DELAY BY FRAMERATE
	pygame.display.flip()
	clock.tick(120)

pygame.quit()