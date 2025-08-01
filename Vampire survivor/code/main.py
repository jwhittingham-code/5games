from settings import *
from player import Player 

#---------------------------------------
#classes




class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Vampire survivor")
        self.dispaysurf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ))
        self.running = True
        self.clock = pygame.time.Clock()

        #Groups
        self.allSprites = pygame.sprite.Group()
        
        #Sprites
        self.player = Player((WINDOW_WIDTH /2 , WINDOW_HEIGHT /2 ),self.allSprites)

    #game loop        
    def run(self):
        while self.running:

            dt = self.clock.tick()/ 1000
            # delta time
            #clock.tick grabs the frame rate
            #dividing by 1000 gives us the milliseconds
            #using this in enitity movement helps keep a consistent predictable speed regardless of frame rate.

            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game.running = False

            #update
            self.allSprites.update(dt)

            #Draw
            self.dispaysurf.fill('black')
            self.allSprites.draw(game.dispaysurf)
            
            pygame.display.update()

        pygame.quit()
#-----------------------------------------
#imports
if __name__ == '__main__':
    game = Game()
    game.run()