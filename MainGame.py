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

########################################################################

# main function
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"

    # if two keys are pressed then it won't bug out
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    
    # move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # snake growing and incremental score
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == munch_position[0] and snake_position[1] == munch_position[1]:
        GameScore.score += 1
        munch_spawn = False
    else:
        snake_body.pop()
         
    if not munch_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                          random.randrange(1, (window_y//10)) * 10]
         
    munch_spawn = True
    window_display.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(window_display, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(window_display, white, pygame.Rect(
      munch_position[0], munch_position[1], 10, 10))
    
    # game over
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        GameOver.game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        GameOver.game_over()

    # snake body contact into game over
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            GameOver.game_over()
    
    # displaying score continuously
    GameScore.show_score(1, white, "calibri", 20)
     
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(movement_speed)