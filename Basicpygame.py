import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

x=50
y=50
width = 20
height = 30
vel = 0.2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



run = True 

while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	key = pygame.key.get_pressed()
	if key[pygame.K_a] and x > vel:
		x -= vel
	if key[pygame.K_d] and x < SCREEN_HEIGHT - width - vel:
		x += vel
	if key[pygame.K_w] and y > vel:
		y -= vel
	if key[pygame.K_s] and y < SCREEN_WIDTH - height - vel:
		y += vel

	screen.fill ((0, 0, 0))

	pygame.draw.rect(screen, (0, 120 , 255), (x, y, width ,height))	

	pygame.display.update()


pygame.quit()