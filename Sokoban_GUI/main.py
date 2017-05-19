import pygame
import main_classes

def draw_objects(game_screen, object_image, objects):
	if type(objects) == list:
		for objectt in objects:
			objectt_x = objectt.x * square_width - square_width /2 + 20
			objectt_y = objectt.y * square_height - square_height /2 + 20
			game_screen.blit(object_image, (objectt_x, objectt_y))
	else:
		objectt_x = objects.x * square_width - square_width /2 + 20
		objectt_y = objects.y * square_height - square_height /2 + 20
		game_screen.blit(object_image, (objectt_x, objectt_y))

# INITIALIZE GAME
map1 = main_classes.Map(main_classes.csv_reader("game_cfg.csv"))
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("SokobanDCM")
loop = True

mario_image = pygame.image.load("sprites/mario.png")
square_image = pygame.image.load("sprites/square.png")
box_image = pygame.image.load("sprites/box.png")
storage_image = pygame.image.load("sprites/gate.png")
win_announce = pygame.image.load("sprites/win.png")

square_width = square_image.get_width()
square_height = square_image.get_height()

col_count = map1.width
row_count = map1.height

mario_row = map1.chaien.y
mario_col = map1.chaien.x
next_mario_row = 0
next_mario_col = 0
move = 0

COLOR = (250, 250 ,250)
clock = pygame.time.Clock()
time = 0

right_pressed = False
left_pressed = False
up_pressed = False
down_pressed = False

while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				#up_pressed = True
				move = "W"
			if event.key == pygame.K_DOWN:
				#down_pressed = True
				move = "S"
			if event.key == pygame.K_LEFT:
				#left_pressed = True
				move = "A"
			if event.key == pygame.K_RIGHT:
				#right_pressed = True
				move = "D"


	# GAME LOGIC PROCESSING
			map1.process_input(move)

	# RE-DRAW THE MAP
	screen.fill(COLOR)

	for row in range(col_count):
		for col in range(row_count):
			#row, col
			x = col * square_width - square_width /2 + 20
			y = row * square_height - square_height /2 + 20
			screen.blit(square_image, (x,y))

	draw_objects(screen, mario_image, map1.chaien)
	draw_objects(screen, box_image, map1.boxes)
	draw_objects(screen, storage_image, map1.storages)

	if map1.boxes == []:
		screen.blit(win_announce, (col_count * square_width / 2, row_count * square_height / 2))
		loop = False
	pygame.display.flip()
	clock.tick(60)
pygame.quit()