import pygame
import background as bg
from player import *
from game_manager import *
from enemy import *
import constraints
from physics_manager import *


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

gamemanager.add(bg.Background(-5, -5))
plr = Player(300, 400)
plr.constraints = constraints.Constraints(0, 600, 0, 800, plr)
gamemanager.add(plr)

n = 120

while loop:
    # HANDLE EVENTS + EXIT EVENT
    events = pygame.event.get()
    for event in events:
        loop = handle_exit(event)

    # RUN CORE LOGIC
    n-= 1
    if n == 0:
        levelmanager.generate_enemies(screen, 2)
        n = 120

    inputmanager.run(events)
    run()

    # DRAW GRAPHICS
    draw()

    # CLEANUP DESTROYED OBJECTS
    #levelmanager.cleanup()

    # CONSTRAINT FRAMERATE
    #print (len(gamemanager.planes))
    pygame.display.flip()
    #print (physicsmanager.box_colliders)
    clock.tick(60)

pygame.quit()