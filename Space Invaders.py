'''
DONE:
INITIALIZATION
BASIC MOVEMENT
OUTLINE FOR SHOOTING
BACKGROUND

TODO:
ENEMY DRAWING AND MOVEMENT
SHOOTING ENEMIES
SCORE SYSTEM
LOSING/WINNING
'''

# Import Pygame
import pygame, sys, time
from pygame.locals import *
from random import randint

# Setup the display of the screen
pygame.init()
window = pygame.display.set_mode((1900,985))
window.fill((0,0,0))

# Set the key repeat
pygame.key.set_repeat(1,1)

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

'''
This is background drawing just in case we lose the image somehow. This does not need to be executed.
for stars in range(1, 200):
    starX=randint(1,1885)
    starY=randint(1,980)
    starSize=randint(1,5)
    pygame.draw.rect(window, (255,255,255),((starX,starY),(starSize,starSize)),0)
pygame.display.update()
'''
# Set the Ship's Location
shipLocation=850

#Import Background
background=pygame.image.load("starBackground.GIF")
pygame.display.update()

# Main while Loop
while True:
    # Redraw the Background
    window.blit(background,(1,1))
    # Create the ship rectangle
    pygame.draw.rect(window, (GREEN), (shipLocation,935,50,50),0)
    # Update the Display
    pygame.display.update()
    
    # Checks for events
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT and shipLocation>0:
                shipLocation=shipLocation-3
            if event.key==K_RIGHT and shipLocation<1850:
                shipLocation=shipLocation+3
            if event.key==K_UP:
                # Shooting Key
                pass
