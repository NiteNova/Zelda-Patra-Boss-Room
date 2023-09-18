import pygame
import random
import math

tea = pygame.image.load("boss_img.png")
sadtea = pygame.image.load("boss_defeat.png")
fire = pygame.image.load("fire.png")
class patra:
    def __init__(self,sx,sy):
        self.x = sx
        self.y = sy
        self.hp = 16
        self.direction = random.randint(1,8)
        self.turntime = random.randint(30,300)
    def step(self, speed = 1):
        if self.hp > 0:
            self.turntime -= 1
            
            #This will make Patra randomly turn every moment or so
            
            if self.turntime < 1:
                self.direction = random.randint(1,8)
                self.turntime = random.randint(30,300)
            
            #Makes sure this doesn't drift off-screen
            
            if self.x > 800:
                if self.y < 100:
                    self.direction = 6
                elif self.y > 800:
                    self.direction = 4
                else:
                    self.direction = 5
                self.turntime = random.randint(150,450)
            elif self.y > 800:
                if self.x < 100:
                    self.direction = 8
                elif self.x > 800:
                    self.direction = 6
                else:
                    self.direction = 7
                self.turntime = random.randint(150,450)
            elif self.x < 100:
                if self.y < 100:
                    self.direction = 2
                elif self.y > 800:
                    self.direction = 8
                else:
                    self.direction = 1
                self.turntime = random.randint(150,450)
            elif self.y < 100:
                if self.x < 100:
                    self.direction = 4
                elif self.x > 800:
                    self.direction = 2
                else:
                    self.direction = 3
                self.turntime = random.randint(150,450)
            
            #What actually moves 
            
            if self.direction == 8 or self.direction == 1 or self.direction == 2:
                self.x += speed/2
            if self.direction == 2 or self.direction == 3 or self.direction == 4:
                self.y += speed/2
            if self.direction == 4 or self.direction == 5 or self.direction == 6:
                self.x -= speed/2
            if self.direction == 6 or self.direction == 7 or self.direction == 8:
                self.y -= speed/2
    def draw(self, scren):
        if self.hp > 0:
            scren.blit(tea, (self.x, self.y))
        else:
            scren.blit(sadtea, (self.x, self.y))

#FIREBALL CLASS! THE SPINNY THING!

class fireball:
    def __init__(self, following, rad, off: float = 0):
        self.x = following.x
        self.y = following.y
        self.angle = off
        self.what = 20
        self.am = 2
        self.tx = 0
        self.ty = 0
        self.sx = rad
        self.sy = rad
        self.hp = 2
    def step(self, following):
        if self.hp > 0:
            self.angle += self.am/360
            
            radians = self.angle*self.what/3.14
            
            self.x = self.sx*math.cos(radians+self.tx)+following.x
            self.y = self.sy*math.sin(radians+self.ty)+following.y
    def draw(self,scren):
        scren.blit(fire, (self.x, self.y))
