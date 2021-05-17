import pygame
import os
import time
import random


WIDTH, HEIGHT = 650, 600
# Pygame surfice
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Backgorund
BG =  pygame.image.load(os.path.join("assets", "background-black.png"))


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    
    def redraw_window():
        # Starts  with the BG to fill the others images
        WINDOW.blit(BG, (0, 0))
        
        # refresh the display
        pygame.display.update()
    

    while run:
        clock.tick(FPS)

        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  

main()