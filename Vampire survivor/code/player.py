from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('5games/Vampire survivor/images/player/down/1.png').convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.speed = 250
        self.direction = pygame.math.Vector2()

    def input(self):
        self.keys = pygame.key.get_pressed()
        self.direction.x = self.keys[pygame.K_RIGHT] - self.keys[pygame.K_LEFT]
        self.direction.y = self.keys[pygame.K_DOWN] - self.keys[pygame.K_UP]
    
    def move(self,dt):
        self.direction.normalize() if self.direction else self.direction
        # # normalise vector so there isnt a speed increase when moving on diagonal
        # the if else statement checks that there is a non zero value in direction
        #otherwise we get an error as normalize wont accept (0,0)

        self.rect.center += self.direction * self.speed * dt

    def update(self,dt):
        self.input()
        self.move(dt)

