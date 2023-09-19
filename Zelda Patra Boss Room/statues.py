import pygame
import random
import math

class enemy:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self, screen):
        pygame.draw.rect(screen, (250, 0, 50), (self.xpos, self.ypos, 40, 40))

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


    def collide(self, p_xpos, p_ypos):
        if self.isAlive == True and self.xpos == p_xpos and self.ypos == p_ypos:
            return -1
            

    def dead(self):
        self.isAlive = False
        self.xVel = 0
        self.yVel = 0