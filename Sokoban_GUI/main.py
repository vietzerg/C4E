import pygame
import main_classes

# INITIALIZE GAME
map1 = main_classes.Map(main_classes.csv_reader("game_cfg.csv"))
pygame.init()

#screen = pygame.display.set_mode((map1.width * 10, map1.height * 10))
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

# WILL BE REPLACED BY A LIST OF BOXES
#box_row = 3
#box_col = 3

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
		# elif event.type == pygame.KEYUP:
		# 	if event.key == pygame.K_RIGHT:
		# 		right_pressed = False
		# 	if event.key == pygame.K_LEFT:
		# 		left_pressed = False
		# 	if event.key == pygame.K_UP:
		# 		up_pressed = False
		# 	if event.key == pygame.K_DOWN:
		# 		down_pressed = False


	# GAME LOGIC PROCESSING
			map1.process_input(move)
			mario_col = map1.chaien.x
			mario_row = map1.chaien.y


	# RE-DRAW THE MAP
	screen.fill(COLOR)

	for row in range(col_count):
		for col in range(row_count):
			#row, col
			x = col * square_width - square_width /2 + 20
			y = row * square_height - square_height /2 + 20
			screen.blit(square_image, (x,y))

	mario_x = mario_col * square_width - square_width /2 + 20
	mario_y = mario_row * square_height - square_height /2 + 20

	screen.blit(mario_image, (mario_x, mario_y))

	for box in map1.boxes:
		box_x = box.x * square_width - square_width /2 + 20
		box_y = box.y * square_height - square_height /2 + 20
		screen.blit(box_image, (box_x, box_y))

	for storage in map1.storages:
		storage_x = storage.x * square_width - square_width /2 + 20
		storage_y = storage.y * square_height - square_height /2 + 20
		screen.blit(storage_image, (storage_x, storage_y))

	if map1.boxes == []:
		screen.blit(win_announce, (col_count * square_width / 2, row_count * square_height / 2))
		loop = False
	pygame.display.flip()
	clock.tick(60)
pygame.quit()

	# time += 1
	# if time > 5:
	# 	time = 0
	# NEXT MARIO POSITION
	# if right_pressed:
	# 	d_row, d_col = 0, 1
	# 	next_mario_col, next_mario_row = min(mario_col + d_col, col_count - 1), mario_row + d_row
	# elif left_pressed:
	# 	d_row, d_col = 0, -1
	# 	next_mario_col, next_mario_row = max(mario_col + d_col, 0), mario_row + d_row
	# elif up_pressed:
	# 	d_row, d_col = -1, 0
	# 	next_mario_row, next_mario_col = max(mario_row + d_row, 0), mario_col + d_col
	# elif down_pressed:
	# 	d_row, d_col = 1, 0
	# 	next_mario_row, next_mario_col = min(mario_row + d_row, row_count - 1), mario_col + d_col


	# # CHECK IF MARIO PUSHES BOX
	# if (next_mario_row, next_mario_col) == (box_row, box_col):
	# 	if d_col == 1:			
	# 		box_col = min(box_col + d_col, col_count - 1)
	# 		mario_col = min(next_mario_col, box_col - d_col)
	# 	elif d_col == -1:			
	# 		box_col = max(box_col + d_col, 0)
	# 		mario_col = max(next_mario_col, box_col - d_col)
	# 	elif d_row == 1:			
	# 		box_row = min(box_row + d_row, row_count - 1)
	# 		mario_row = min(next_mario_row, box_row - d_row)
	# 	elif d_row == -1:		
	# 		box_row = max(box_row + d_row, 0)
	# 		mario_row = max(next_mario_row, box_row - d_row)
	# else:
	# 	mario_row = next_mario_row
	# 	mario_col = next_mario_col