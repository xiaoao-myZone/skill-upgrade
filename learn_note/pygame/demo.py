#-*- coding: utf-8 -*-
import sys
import time
import pygame
from maze import MAZE, search_path, start_point, end_point
from pygame.locals import QUIT, K_q

#color define
BLACK = (5 ,5, 5)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (200, 50, 20)

#size
SCREEN = (402, 402)
REC  = (40, 40)

iter_point = search_path(start_point, end_point)

pygame.init()
screen = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("Demo")

rect_array = []
for y, x_list in enumerate(MAZE):
    x_rect = []
    for x, value in enumerate(x_list):
        rect = (x*REC[0], y*REC[1], REC[0], REC[1])
        if value:
            m = pygame.draw.rect(screen, BLACK, rect)
        else:
            m = pygame.draw.rect(screen, WHITE, rect)
        x_rect.append(m)
    rect_array.append(x_rect)


finish = False
x, y = -1, -1
while True:
    for event in pygame.event.get():
        if event.type == QUIT: #点击控件上的“X”
            print("exit")
            sys.exit()
        if event.type == K_q:
            print("q")
    
    if not finish:
        # ans = input()
        # if ans:
        #     sys.exit()
        time.sleep(0.5)
        try:
            # if not (x<0 or y<0):
            #     pygame.draw.rect(screen, RED, rect_array[y][x])
            input_point, x, y = next(iter_point)
            if input_point:
                pygame.draw.rect(screen, GREEN, rect_array[y][x])
                
            else:
                print("draw red")
                pygame.draw.rect(screen, RED, rect_array[y][x])
            
        except:
            finish = True
    time.sleep(0.02)
            
    pygame.display.update()