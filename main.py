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
        window.blit(self.ship_img, (self.x, self.y))

    
    def get_width(self):
        return self.ship_img.get_width()

   
    def get_height(self):
        return self.ship_img.get_height()

    

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


class Enemy(Ship):
    def __init__(self, x, y, color, health=100):
        COLOR_MAP = {
            "red": (RED_SPACE_SHIP, RED_LASER),
            "green": (GREEN_SPACE_SHIP, GREEN_LASER),
            "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
        }
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    
    def move(self, velocity):
        self.y += velocity
        

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    
    enemies = []
    wave_length = 5
    enemy_velocity = 1

    player_velocity = 5
    
    player_ship = Player(300, 300)

    clock = pygame.time.Clock()


    
    def redraw_window():
        # Starts  with the BG to fill the others images
        WINDOW.blit(BG, (0, 0))
        # Draw text 
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))

        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        
        for enemy in enemies:
            enemy.draw(WINDOW)

        player_ship.draw(WINDOW)

        
        
        pygame.display.update()
    

    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy_ship = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["green", "blue", "red"]))

                enemies.append(enemy_ship)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  


        keys = pygame.key.get_pressed() # returns a dict of all the keys and tells weather they're pressed or not at the current time
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]): # left
            if player_ship.x - player_velocity < 0:
                player_ship.x = WIDTH
            else:
                player_ship.x -= player_velocity
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]): # right
            if player_ship.x + player_velocity > WIDTH:
                player_ship.x = 0
            else:
                player_ship.x += player_velocity
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player_ship.y - player_velocity  > 0: # up
            player_ship.y -= player_velocity
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player_ship.y + player_velocity + player_ship.get_height() < HEIGHT: # down
            player_ship.y += player_velocity
        
        for enemy in enemies[:]:
            enemy.move(enemy_velocity)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)


        redraw_window()
        

main()