import pygame
from os.path import join
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("5games/space shooter/images/player.png").convert_alpha()
        self.rect =  self.image.get_frect(center = (win_W /2, win_H /2))
        self.direction = pygame.math.Vector2()
        self.speed = 300 

    
        


    def pewPew(self):
        

    def update(self, dt):
        #--------------Player movement --------------------------------
        self.keys = pygame.key.get_pressed()
        self.direction.x = int(self.keys[pygame.K_RIGHT]) - int(self.keys[pygame.K_LEFT])
        self.direction.y = int(self.keys[pygame.K_DOWN]) - int(self.keys[pygame.K_UP])
        
        self.direction = self.direction.normalize() if self.direction else self.direction
        # # normalise vector so there isnt a speed increase when moving on diagonal
        # the if else statement checks that there is a non zero value in direction
        #otherwise we get an error as normalize wont accept (0,0)
        
        self.rect.center += self.direction * self.speed * dt
        #moves the player rect by adding the direction times speed times delta time
        #Note that delta time is created in the game loop below

        #-------------------------------------------------------------
        # shoot functionality
        self.recentKeys = pygame.key.get_just_pressed()
        if self.recentKeys[pygame.K_SPACE]:
            print("Ima firing my laza!!")

        #console debug
        print("ship is being updated")
        print("ship location", self.rect.center)
        print("Direction: ", self.direction)

#general setup

pygame.init()
win_W, win_H = 1280, 720
displaySurf = pygame.display.set_mode((win_W, win_H))
running = True
clock = pygame.time.Clock()

#creating a surface
surf = pygame.surface.Surface((100,100))
surf.fill('Green')

#imports
allSprites = pygame.sprite.Group()
player = Player(allSprites)

meteorSurf = pygame.image.load("5games/space shooter/images/meteor.png").convert_alpha()
meteorRect = meteorSurf.get_frect(center = (win_W /2, win_H /2))

laserSurf = pygame.image.load("5games/space shooter/images/laser.png").convert_alpha()
laserRect = laserSurf.get_frect(bottomleft = (20, win_H-20))

starSurf = pygame.image.load("5games/space shooter/images/star.png").convert_alpha()

pygame.display.set_caption("Space Shooter")

# generate random coordinates for stars to be displayed

randPos = [(((random.randint(0,win_W)),(random.randint(0,win_H)))) for i in range(20)]
    

#game loop
while running:

    dt = clock.tick()/ 1000
    # delta time
    #clock.tick grabs the frame rate
    #dividing by 1000 gives us the milliseconds
    #using this in enitity movement helps keep a consistent predictable speed regardless of frame rate.


    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    

    allSprites.update(dt)

    #draw the game 
    displaySurf.fill("dark grey")
    
    
    # for each set of coordinates generated draw a star
    for pos in randPos: displaySurf.blit(starSurf, pos)   

    displaySurf.blit(meteorSurf, meteorRect)
    displaySurf.blit(laserSurf, laserRect)
  
    allSprites.draw(displaySurf)
    
    
    pygame.display.update()


pygame.quit()