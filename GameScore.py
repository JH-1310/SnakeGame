import MainGame
import pygame

# initial score
score = 0

# display score
def show_score(choice, color, font, size):

    # create font
    score_font = pygame.font.SysFont(font, size)

    # create display surface object
    score_surface = score_font.render("Score : " + str(score), True, color)

    # create rectangular object for the surface object
    score_rect = score_surface.get_rect()

    # display text
    MainGame.window_display.blit(score_surface, score_rect)