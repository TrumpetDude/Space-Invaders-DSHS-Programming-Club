import pygame, sys, time
from pygame.locals import *
from random import randint
pygame.init()
window = pygame.display.set_mode((1900,985))
window.fill((0,0,0))
pygame.key.set_repeat(1,1)
for stars in range(1, 200):
    starX=randint(1,1885)
    starY=randint(1,980)
    starSize=randint(1,5)
    pygame.draw.rect(window, (255,255,255),((starX,starY),(starSize,starSize)),0)
pygame.display.update()
while True:
    for event in pygame.event.get():
        # Determine if the user has closed the window or pressed escape
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            # Quit the program
            pygame.quit()
            sys.exit()
    
