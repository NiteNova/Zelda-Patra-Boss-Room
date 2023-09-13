import pygame
import random
import math

tea = pygame.image.load('boss_img.png')
fire = pygame.image.load('fire.png')
class patra:
    def __init__(self,sx,sy):
        self.x = sx
        self.y = sy
        self.direction = random.randint(1,8)
        self.turntime = random.randint(30,300)
    def step(self, speed = 1):
        self.turntime -= 1
        
        #This will make Patra randomly turn every moment or so
        
        if self.turntime < 1:
            self.direction = random.randint(1,8)
            self.turntime = random.randint(30,300)
        if self.direction == 8 or self.direction == 1 or self.direction == 2:
            self.x += speed/2
        if self.direction == 2 or self.direction == 3 or self.direction == 4:
            self.y += speed/2
        if self.direction == 4 or self.direction == 5 or self.direction == 6:
            self.x -= speed/2
        if self.direction == 6 or self.direction == 7 or self.direction == 8:
            self.y -= speed/2
    def draw(self, scren):
        scren.blit(tea, (self.x, self.y))

#FIREBALL CLASS! THE SPINNY THING!

class fireball:
    def __init__(self, following, off: float = 0):
        self.x = following.x
        self.y = following.y
        self.angle = off
        self.what = 20
        self.am = 2
        self.tx = 0
        self.ty = 0
        self.sx = 100
        self.sy = 100
    def step(self, following):
        self.angle += self.am/360
        
        radians = self.angle*self.what/3.14
        
        self.x = self.sx*math.cos(radians+self.tx)+following.x
        self.y = self.sy*math.sin(radians+self.ty)+following.y
    def draw(self,scren):
        scren.blit(fire, (self.x, self.y))