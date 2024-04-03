# import files
import GameScore
import GameOver

# libraries
import pygame
import time
import random

# initialise pygame
pygame.init()

# Window size
window_x = 720
window_y = 480
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# initialise game window and title
pygame.display.set_caption("Snake Game - JH-1310")
window_display = pygame.display.set_mode((window_x, window_y))

# FPS
fps = pygame.time.Clock()

# set movement speed
movement_speed = 15

# snake default position
snake_position = [100, 50]

# first snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

munch_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10,]

munch_spawn = True

# default snake direction
direction = 'RIGHT'
change_to = direction
