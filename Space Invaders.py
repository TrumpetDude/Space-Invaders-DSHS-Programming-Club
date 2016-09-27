'''
DONE:
INITIALIZATION
ASIC MOVEMENT
OUTLINE FOR SHOOTING
BACKGROUND CREATION

TODO:
REMEMBER BACKGROUND SO WE CAN DO STARS
ENEMY DRAWING AND MOVEMENT
SHOOTING ENEMIES
SCORE SYSTEM
LOSING/WINNING
'''
import pygame, sys, time
from pygame.locals import *
from random import randint
pygame.init()
window = pygame.display.set_mode((1900,985))
window.fill((0,0,0))
pygame.key.set_repeat(1,1)
shipLocation=850
#STAR LOCATIONS NEED TO BE REMEMBERED
'''
for stars in range(1, 200):
    starX=randint(1,1885)
    starY=randint(1,980)
    starSize=randint(1,5)
    pygame.draw.rect(window, (255,255,255),((starX,starY),(starSize,starSize)),0)
pygame.display.update()
'''
while True:
    window.fill((0,0,0))
    pygame.draw.rect(window, (255,0,0), (shipLocation,935,50,50),0)#MAKE THI A SHIP
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT and shipLocation>0:
                shipLocation=shipLocation-3
            if event.key==K_RIGHT and shipLocation<1850:
                shipLocation=shipLocation+3
            if event.key==K_SPACE:
                pass
                #SHOOT
