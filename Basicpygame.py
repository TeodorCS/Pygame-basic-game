import pygame

pygame.init()

SCREEN_WIDTH = 564
SCREEN_HEIGHT = 322

clock = pygame.time.Clock()

#character stats and positioning
x=50
y=220
width = 64
height = 64
vel = 5

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Fight")

walkRight = [pygame.image.load('Game\R1.png'), pygame.image.load('Game\R2.png'),pygame.image.load('Game\R3.png'), pygame.image.load('Game\R4.png'), pygame.image.load('Game\R5.png'), pygame.image.load('Game\R6.png'), pygame.image.load('Game\R7.png'), pygame.image.load('Game\R8.png'), pygame.image.load('Game\R9.png')]
walkLeft = [pygame.image.load('Game\L1.png'), pygame.image.load('Game\L2.png'),pygame.image.load('Game\L3.png'), pygame.image.load('Game\L4.png'), pygame.image.load('Game\L5.png'), pygame.image.load('Game\L6.png'), pygame.image.load('Game\L7.png'), pygame.image.load('Game\L8.png'), pygame.image.load('Game\L9.png')]
bg = pygame.image.load('Game\BGstreet.jpg')
char = pygame.image.load('Game\standing.png')

isJump = False
jumpCount = 10
left = False	
right = False	
walkCount = 0

#drawing on the window

def redrawGameWindow():
	global walkCount

	screen.blit(bg , (0,0))
	
	if walkCount + 1 >= 27:
		walkCount = 0

	if left:
		screen.blit(walkLeft[walkCount//3], (x,y))
		walkCount += 1

	elif right:
		screen.blit(walkRight[walkCount//3], (x,y))
		walkCount += 1

	else:
		screen.blit(char, (x,y))

	pygame.display.update()


#main loop

run = True 
while run:

	clock.tick(27)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	#movement features

	key = pygame.key.get_pressed()

	if key[pygame.K_a] and x > vel:
		x -= vel
		left = True
		right = False
	elif key[pygame.K_d] and x < SCREEN_WIDTH - width - vel:
		x += vel
		left = False
		right = True
	else: 
		right = False
		left = False
		walkCount = 0

	if not (isJump):

		if key[pygame.K_SPACE]:
			isJump = True
			right = False
			left = False
			walkCount = 0
	else: 

		if jumpCount >= -10:
			
			neg = 1
			
			if jumpCount < 0:
				neg = -1

			y -= (jumpCount  ** 2) * 0.5 * neg 
			jumpCount -= 1

		else:
			isJump = False
			jumpCount = 10

	
	redrawGameWindow()

pygame.quit()