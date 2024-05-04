import pygame

pygame.init()

SCREEN_WIDTH = 564
SCREEN_HEIGHT = 322

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Fight")

clock = pygame.time.Clock()

#character stats and positioning
class player(object):
	def __init__ (self, x ,y ,width ,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.isJump = False
		self.jumpCount = 10
		self.left = False
		self.right = False
		self.walkCount = 0

	def draw(self ,screen):
		
		if self.walkCount + 1 >= 27:
			self.walkCount = 0

		if self.left:
			screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
			self.walkCount += 1

		elif self.right:
			screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
			self.walkCount += 1

		else:
			screen.blit(char, (self.x,self.y))



man= player(50 , 220 ,64, 64)


#image rendering

walkRight = [pygame.image.load('Game\R1.png'), pygame.image.load('Game\R2.png'),pygame.image.load('Game\R3.png'), pygame.image.load('Game\R4.png'), pygame.image.load('Game\R5.png'), pygame.image.load('Game\R6.png'), pygame.image.load('Game\R7.png'), pygame.image.load('Game\R8.png'), pygame.image.load('Game\R9.png')]
walkLeft = [pygame.image.load('Game\L1.png'), pygame.image.load('Game\L2.png'),pygame.image.load('Game\L3.png'), pygame.image.load('Game\L4.png'), pygame.image.load('Game\L5.png'), pygame.image.load('Game\L6.png'), pygame.image.load('Game\L7.png'), pygame.image.load('Game\L8.png'), pygame.image.load('Game\L9.png')]
bg = pygame.image.load('Game\BGstreet.jpg')
char = pygame.image.load('Game\standing.png')


#drawing on the window

def redrawGameWindow():

	screen.blit(bg , (0,0))
	man.draw(screen)

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

	if key[pygame.K_a] and man.x > man.vel:
		man.x -= man.vel
		man.left = True
		man.right = False
	elif key[pygame.K_d] and man.x < SCREEN_WIDTH - man.width - man.vel:
		man.x += man.vel
		man.left = False
		man.right = True
	else: 
		man.right = False
		man.left = False
		man.walkCount = 0

	if not (man.isJump):

		if key[pygame.K_SPACE]:
			man.isJump = True
			man.right = False
			man.left = False
			man.walkCount = 0
	else: 

		if man.jumpCount >= -10:
			
			neg = 1
			
			if man.jumpCount < 0:
				neg = -1

			man.y -= (man.jumpCount  ** 2) * 0.3 * neg 
			man.jumpCount -= 1

		else:
			man.isJump = False
			man.jumpCount = 10

	
	redrawGameWindow()

pygame.quit()