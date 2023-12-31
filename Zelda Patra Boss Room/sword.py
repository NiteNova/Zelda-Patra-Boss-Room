import pygame
import math
#CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SHOOT = 4
#Hi
class throw_sword:
    def __init__(self):
        self.xpos = -10 #draw offscreen when not in use
        self.ypos = -10
        self.isAlive = False
        self.direction = RIGHT
    def shoot(self, x, y, dir):
        self.xpos = x + 20
        self.ypos = y + 20
        self.isAlive = True
        self.direction = dir
    def move(self):
        if self.direction == RIGHT:
            self.xpos+=10
        elif self.direction == LEFT:
            self.xpos-=10
        elif self.direction == UP:
            self.ypos-=10
        elif self.direction == DOWN:
            self.ypos+=10
        #add other directions here
    def draw(self, screen):
        pygame.draw.circle(screen, (250, 0, 0), (self.xpos, self.ypos), 10)
        pygame.draw.circle(screen, (250, 250, 0), (self.xpos, self.ypos), 5)
    def kill(self):
        self.isAlive = False    
    