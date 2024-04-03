import MainGame
import GameOver
import GameScore

import pygame
import random


# main function
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                MainGame.change_to = "UP"
            if event.key == pygame.K_DOWN:
                MainGame.change_to = "DOWN"
            if event.key == pygame.K_RIGHT:
                MainGame.change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                MainGame.change_to = "LEFT"

    # if two keys are pressed then it won't bug out
    if MainGame.change_to == 'UP' and MainGame.direction != 'DOWN':
        MainGame.direction = 'UP'
    if MainGame.change_to == 'DOWN' and MainGame.direction != 'UP':
        MainGame.direction = 'DOWN'
    if MainGame.change_to == 'LEFT' and MainGame.direction != 'RIGHT':
        MainGame.direction = 'LEFT'
    if MainGame.change_to == 'RIGHT' and MainGame.direction != 'LEFT':
        MainGame.direction = 'RIGHT'
    
    # move the snake
    if MainGame.direction == 'UP':
        MainGame.snake_position[1] -= 10
    if MainGame.direction == 'DOWN':
        MainGame.snake_position[1] += 10
    if MainGame.direction == 'LEFT':
        MainGame.snake_position[0] -= 10
    if MainGame.direction == 'RIGHT':
        MainGame.snake_position[0] += 10

    # snake growing and incremental score
    MainGame.snake_body.insert(0, list(MainGame.snake_position))
    if MainGame.snake_position[0] == MainGame.munch_position[0] and MainGame.snake_position[1] == MainGame.munch_position[1]:
        GameScore.score += 1
        MainGame.munch_spawn = False
    else:
        MainGame.snake_body.pop()
         
    if not MainGame.munch_spawn:
        MainGame.munch_position = [random.randrange(1, (MainGame.window_x//10)) * 10, 
                          random.randrange(1, (MainGame.window_y//10)) * 10]
         
    MainGame.munch_spawn = True
    MainGame.window_display.fill(MainGame.black)
     
    for pos in MainGame.snake_body:
        pygame.draw.rect(MainGame.window_display, MainGame.green, pygame.Rect(
          pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(MainGame.window_display, MainGame.white, pygame.Rect(
      MainGame.munch_position[0], MainGame.munch_position[1], 10, 10))
    
    # game over
    if MainGame.snake_position[0] < 0 or MainGame.snake_position[0] > MainGame.window_x-10:
        GameOver.game_over()
    if MainGame.snake_position[1] < 0 or MainGame.snake_position[1] > MainGame.window_y-10:
        GameOver.game_over()

    # snake body contact into game over
    for block in MainGame.snake_body[1:]:
        if MainGame.snake_position[0] == block[0] and MainGame.snake_position[1] == block[1]:
            GameOver.game_over()
    
    # displaying score continuously
    GameScore.show_score(1, MainGame.white, "calibri", 20)
     
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    MainGame.fps.tick(MainGame.movement_speed)