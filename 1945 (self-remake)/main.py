import pygame
import background as bg
import player as plr
import input_manager


def setup_game():
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("1945")
    return screen

def handle_exit(event):
    if event.type == pygame.QUIT:
        return False
    return True

def run():
    background.run()
    player.run()


def draw():
    background.draw(screen)
    player.draw(screen)

screen = setup_game()
clock = pygame.time.Clock()
loop = True

background = bg.Background()
player = plr.Player()
inputmanager = input_manager.InputManager()

while loop:
    # HANDLE EVENTS + EXIT EVENT
    events = pygame.event.get()
    for event in events:
        loop = handle_exit(event)

    # RUN CORE LOGIC
    run()

    # DRAW GRAPHICS
    draw()

    # CONSTRAINT FRAMERATE
    pygame.display.flip()
    clock.tick(60)

pygame.quit()