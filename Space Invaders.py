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
TITLE SCREEN
OBASTACLES
'''

# Import Pygame
import pygame, sys, time, random
from pygame.locals import *

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Setup the display of the screen
pygame.init()
window = pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
window.fill(BLACK)

# Set the key repeat
pygame.key.set_repeat(1,1)

# Set the Ship's Location
shipLocation = 850
shipX = 914
shipY = 900

#Import Ship
ship=pygame.image.load("ship.PNG")

# Main while Loop
while True:
    
    # Redraw the Background
    window.fill(BLACK)
    
    #Draw the ship
    window.blit(ship,(shipX, shipY))
    
    # Update the Display
    pygame.display.update()
    
    # Checks for events
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT and shipX > 0:
                shipX = shipX - 3
            if event.key == K_RIGHT and shipX < 1814:
                shipX = shipX + 3
            if event.key == K_UP:
                # Shooting Key
                pass
