import pygame
from pygame.locals import *

from Board import *

BG = (0,0,0)
FG = (255,255,255)

board = Board()

def game_loop(canvas):
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(20) # 20 FPS 
        for e in pygame.event.get():
            if e.type == QUIT: run = False
            elif e.type == MOUSEBUTTONDOWN:
                print("mouse is down at", pygame.mouse.get_pos())
                board.handle_click(pygame.mouse.get_pos())

        board.show(canvas)

pygame.init()
canvas = pygame.display.set_mode((960, 960))
game_loop(canvas)

# screen size: 960
