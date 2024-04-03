import MainGame
import GameScore
import pygame
import time

def game_over():

    # create font object
    my_font = pygame.font.SysFont("calibri", 50)

    # create text surface
    game_over_surface = my_font.render("Your score is : " + str(GameScore.score), True, MainGame.red)

    # create a rectangular object for the next surface object
    game_over_rect = game_over_surface.get_rect()

    # setting posotion of text
    game_over_rect.midtop = (MainGame.window_x/2, MainGame.window_y/4)

    # draw text on screen
    MainGame.window_display.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 3 seconds will quit
    time.sleep(3)

    # deactivating pygame
    pygame.quit()

    # quit game
    quit()