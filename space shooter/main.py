import pygame
from os.path import join
import random
from random import uniform

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("5games/space shooter/images/player.png").convert_alpha()
        self.rect =  self.image.get_frect(center = (win_W /2, win_H /2))
        self.direction = pygame.math.Vector2()
        self.speed = 300 

    # cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400
    
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

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
        if self.recentKeys[pygame.K_SPACE] and self.can_shoot:
            Laser(laserSurf, self.rect.midtop, allSprites)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        self.laser_timer()

        #console debug
        # print("ship is being updated")
        # print("ship location", self.rect.center)
        # print("Direction: ", self.direction)

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center= ((random.randint(0, win_W)),(random.randint(0, win_H))))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()
        

class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = ((random.randint(0, win_W)), 0))
        self.createTime = pygame.time.get_ticks()
        self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed = random.randint(400,500)

    def update(self, dt):
        current_time = pygame.time.get_ticks()
        self.rect.center += self.direction * self.speed * dt
        if self.rect.top > win_H or self.rect.right < 0 or self.rect.left > win_W:
            self.kill()
        if current_time - self.createTime > 2000:
            self.kill()

#--------------------------------------------------------------------------------------------------------------------------      
#general setup ------------------------------------------------------------------------------------------------------------

pygame.init()
pygame.display.set_caption("Space Shooter")

win_W, win_H = 1280, 720
displaySurf = pygame.display.set_mode((win_W, win_H))
running = True
clock = pygame.time.Clock()

#imports
allSprites = pygame.sprite.Group()
#sprite group allows us to draw all sprites in the group at once instead of using blit method.

meteorSurf = pygame.image.load("5games/space shooter/images/meteor.png").convert_alpha()
laserSurf = pygame.image.load("5games/space shooter/images/laser.png").convert_alpha()
starSurf = pygame.image.load("5games/space shooter/images/star.png").convert_alpha()
#importing star image prior to initialising 20 versions of the star object 
#This improves performance by importing once instead of 20 times.

for i in range(20):
    Star(allSprites, starSurf) 
#creates 20 stars

player = Player(allSprites)

#Custom event -> Meteor event
meteor_event = pygame.event.custom_type() #creates custom event
pygame.time.set_timer(meteor_event,500) # uses our custom event to trigger a timer
  
#game loop ------------------------------------------------------------------------------------------------

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
        if event.type == meteor_event:
            Meteor(meteorSurf,allSprites)

    

    allSprites.update(dt)

    #draw the game 
    displaySurf.fill("dark grey")
    
    
    # for each set of coordinates generated draw a star
   # for pos in randPos: displaySurf.blit(starSurf, pos)   

    
    
  
    allSprites.draw(displaySurf)
   
    
    pygame.display.update()


pygame.quit()