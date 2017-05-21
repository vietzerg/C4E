import pygame
import background as bg
from player import *
from game_manager import *
from enemy import *


def setup_screen():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("1945")
    return screen

def handle_exit(event):
    if event.type == pygame.QUIT:
        return False
    return True

def run():
    gamemanager.run()
    levelmanager.check_hit()

def draw():
    screen.fill((0,0,0))
    gamemanager.draw(screen)

screen = setup_screen()
clock = pygame.time.Clock()
loop = True

gamemanager.add(bg.Background())
plr = Player(300, 400)
plr.main = True
gamemanager.add(plr)

n = 300

while loop:
    # HANDLE EVENTS + EXIT EVENT
    events = pygame.event.get()
    for event in events:
        loop = handle_exit(event)

    # RUN CORE LOGIC
    n-= 1
    if n == 0:
        levelmanager.generate_enemies(screen, 2)
        n = 150

    inputmanager.run(events)
    run()

    # DRAW GRAPHICS
    draw()

    # CONSTRAINT FRAMERATE
    #print (len(gamemanager.planes))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()