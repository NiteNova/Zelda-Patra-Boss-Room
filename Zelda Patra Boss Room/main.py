import pygame
import random

pygame.init()
pygame.display.set_caption("Boss Room")
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

gameover = False
timer = 0;

xpos = 500
ypos = 500
