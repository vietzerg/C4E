# TEST ANIMATION
import pygame

pygame.init()
screen = pygame.display.set_mode((300,400))

framesheet = pygame.image.load("resources/explosion.png")
result = []

for i in range(1, 7):
    step = framesheet.get_width() / 6
    frame = framesheet.subsurface((step*(i-1) + 1, 1, 32, 32))
    frame.set_colorkey((255,255,255))
    frame.convert_alpha()
    result.append(frame)

clock = pygame.time.Clock()

loop = True
interval = 0.5
cycletime = 0
i = 0
while loop:
    milliseconds = clock.tick(60)
    seconds = milliseconds / 1000.0
    cycletime += seconds
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    if cycletime > interval:
        frame = result[i]
        screen.fill((0,0,0))
        screen.blit(frame, (150,200))
        i += 1
        if i > 5:
            i = 0
        cycletime = 0

    pygame.display.flip()

pygame.quit()