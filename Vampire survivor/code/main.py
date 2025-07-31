from settings import *


#---------------------------------------
#classes

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('5games/Vampire survivor/images/player/down/1.png')
        self.rect = self.image.get_frect()
        self.speed = 250
        self.direction = pygame.math.Vector2()
    def update(self,dt):
        
        self.keys = pygame.key.get_pressed()
        self.direction.x = self.keys[pygame.K_RIGHT] - self.keys[pygame.K_LEFT]
        self.direction.y = self.keys[pygame.K_DOWN] - self.keys[pygame.K_UP]
        self.direction.normalize() if self.direction else self.direction
        # # normalise vector so there isnt a speed increase when moving on diagonal
        # the if else statement checks that there is a non zero value in direction
        #otherwise we get an error as normalize wont accept (0,0)

        self.rect.center += self.direction * self.speed * dt


#-----------------------------------------
#setup
pygame.init()
pygame.display.set_caption("Vampire survivor")
dispaysurf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ))
running = True
clock = pygame.time.Clock()
allSprites = pygame.sprite.Group()

player = Player(allSprites)

#-----------------------------------------
#game loop
while running:

    dt = clock.tick()/ 1000
    # delta time
    #clock.tick grabs the frame rate
    #dividing by 1000 gives us the milliseconds
    #using this in enitity movement helps keep a consistent predictable speed regardless of frame rate.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dispaysurf.fill('black')

    allSprites.draw(dispaysurf)
    allSprites.update(dt)
    pygame.display.update()

pygame.quit()