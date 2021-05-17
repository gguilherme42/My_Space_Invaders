import pygame
import os
import time
import random

from pygame import key


# The font object needs to be initialized
pygame.font.init()

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
BG =  pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x_position, y_position, health=100):
        self.x = x_position
        self.y = y_position
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
    
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    player_velocity = 5
    ship = Ship(300, 300)

    clock = pygame.time.Clock()


    
    def redraw_window():
        # Starts  with the BG to fill the others images
        WINDOW.blit(BG, (0, 0))
        # Draw text 
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        ship.draw(WINDOW)
        
        pygame.display.update()
    

    while run:
        clock.tick(FPS)

        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  


        keys = pygame.key.get_pressed() # returns a dict of all the keys and tells weather they're pressed or not at the current time
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # left
            ship.x -= player_velocity
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # right
            ship.x += player_velocity
        if keys[pygame.K_w] or keys[pygame.K_UP]: # up
            ship.y -= player_velocity
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: # down
            ship.y += player_velocity

main()