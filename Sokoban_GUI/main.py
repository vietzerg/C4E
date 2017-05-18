import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("SokobanDCM")
loop = True
mario_image = pygame.image.load("sprites/mario.png")
square_image = pygame.image.load("sprites/square.png")
box_image = pygame.image.load("sprites/box.png")

square_width = square_image.get_width()
square_height = square_image.get_height()

col_count = 5
row_count = 5

# mario_x = 50
# mario_y = 100
mario_row = 0
mario_col = 0
next_mario_row = 0
next_mario_col = 0

box_row = 3
box_col = 3

BLACK = (250, 250 ,250)
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
				up_pressed = True
			if event.key == pygame.K_DOWN:
				down_pressed = True
			if event.key == pygame.K_LEFT:
				left_pressed = True
			if event.key == pygame.K_RIGHT:
				right_pressed = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				right_pressed = False
			if event.key == pygame.K_LEFT:
				left_pressed = False
			if event.key == pygame.K_UP:
				up_pressed = False
			if event.key == pygame.K_DOWN:
				down_pressed = False

	time += 1
	if time > 5:
		time = 0
		# NEXT MARIO POSITION
		if right_pressed:
			d_row, d_col = 0, 1
			next_mario_col, next_mario_row = min(mario_col + d_col, col_count - 1), mario_row + d_row
		elif left_pressed:
			d_row, d_col = 0, -1
			next_mario_col, next_mario_row = max(mario_col + d_col, 0), mario_row + d_row
		elif up_pressed:
			d_row, d_col = -1, 0
			next_mario_row, next_mario_col = max(mario_row + d_row, 0), mario_col + d_col
		elif down_pressed:
			d_row, d_col = 1, 0
			next_mario_row, next_mario_col = min(mario_row + d_row, row_count - 1), mario_col + d_col


	# CHECK IF MARIO PUSHES BOX
	if (next_mario_row, next_mario_col) == (box_row, box_col):
		if d_col == 1:			
			box_col = min(box_col + d_col, col_count - 1)
			mario_col = min(next_mario_col, box_col - d_col)
		elif d_col == -1:			
			box_col = max(box_col + d_col, 0)
			mario_col = max(next_mario_col, box_col - d_col)
		elif d_row == 1:			
			box_row = min(box_row + d_row, row_count - 1)
			mario_row = min(next_mario_row, box_row - d_row)
		elif d_row == -1:		
			box_row = max(box_row + d_row, 0)
			mario_row = max(next_mario_row, box_row - d_row)
	else:
		mario_row = next_mario_row
		mario_col = next_mario_col


	# RE-DRAW THE MAP
	screen.fill(BLACK)
	for row in range(col_count):
		for col in range(row_count):
			#row, col
			x = col * square_width - square_width /2 + 20
			y = row * square_height - square_height /2 + 20
			screen.blit(square_image, (x,y))

	mario_x = mario_col * square_width - square_width /2 + 20
	mario_y = mario_row * square_height - square_height /2 + 20

	box_x = box_col * square_width - square_width /2 + 20
	box_y = box_row * square_height - square_height /2 + 20

	#screen.blit(square_image, (20,20))
	screen.blit(mario_image, (mario_x, mario_y))
	screen.blit(box_image, (box_x, box_y))
	pygame.display.flip()
	clock.tick(60)
pygame.quit()