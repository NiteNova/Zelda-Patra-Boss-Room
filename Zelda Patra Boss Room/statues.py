import pygame
import random
import math


statue = pygame.image.load("statue.png")
statue2 = pygame.image.load("statue2.png")

class enemy:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self, screen, style):
        if style == 0:
            screen.blit(statue2, (self.xpos, self.ypos))
        elif style == 1:
            screen.blit(statue, (self.xpos, self.ypos))

class enemy_fireball:
    def __init__ (self, xpos, ypos):
        self.isAlive = False
        self.xVel: float = 0
        self.yVel: float = 0
        self.xpos: float = xpos
        self.ypos: float = ypos

    def draw(self, screen):
        if self.isAlive == True:
            pygame.draw.circle(screen, (250, 0, 0), (self.xpos, self.ypos), 10)
            pygame.draw.circle(screen, (250, 250, 0), (self.xpos, self.ypos), 5)

    def movement(self, p_xpos, p_ypos):
        self.xpos += self.xVel
        self.ypos += self.yVel

    def collide(self):
        print("hit")
        return -1
    
    def dead(self):
        self.isAlive = False
        self.xVel = 0
        self.yVel = 0