import pygame

#general setup

pygame.init()
win_W, win_H = 1280, 720
displaySurf = pygame.display.set_mode((win_W, win_H))
running = True


pygame.display.set_caption("Space Shooter")
#game loop

while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game 
    displaySurf.fill(pygame.color.Color(250,50,100))
    pygame.display.update()


pygame.quit()