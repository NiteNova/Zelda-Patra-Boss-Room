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

#fireball CLASS! THE SPINNY THING!

class fireball:
    def __init__(self, following, rad, off: float = 0):
        self.x = following.x
        self.y = following.y
        self.angle = off
        self.what: float = 20
        self.am: float = 2
        self.tx: float = 0
        self.ty: float = 0
        self.sx: float = rad
        self.sy: float = rad
        self.hp: int = 2
    def step(self, following: "patra|fireball"):
        if self.hp > 0:
            self.angle += self.am/360
            
            radians = self.angle*self.what/3.14
            
            self.x = self.sx*math.cos(radians+self.tx)+following.x
            self.y = self.sy*math.sin(radians+self.ty)+following.y
    def draw(self,scren):
        scren.blit(fire, (self.x, self.y))


def firestyle(balls: list[fireball],style: int,ger: float,rgr: float,boss_man: patra,A: float,B: float, time: float) -> list:
    for i, fireballs in enumerate(balls):
        if style == 0: # Style 0: do nothing, become normal
            A = 0
            B = 0
            fireballs.tx = 0
            fireballs.ty = 0
            fireballs.sx = ger
            fireballs.sy = ger
            fireballs.step(boss_man)
        elif style == 1: # Style 1: do the cool swaying
            fireballs.tx = time/2
            if A == 1:
                fireballs.sy -= 1
                if fireballs.sy <= 0-ger:
                    A = 2
            elif A == 2:
                fireballs.sy += 1
                if fireballs.sy >= ger:
                    A = 0
                    B = 1
            if B == 1:
                fireballs.sx -= 1
                if fireballs.sx <= 0-ger:
                    B = 2
            elif B == 2:
                fireballs.sx += 1
                if fireballs.sx >= ger:
                    A = 1
                    B = 0
            fireballs.step(boss_man)
        elif style == 2: # Style 2: 3 orbiting 2
            if i % 4 == 0:
                fireballs.step(boss_man)
                fireballs.sx = ger
                fireballs.sy = ger
                B = i
            else:
                fireballs.am = 3/(len(balls)//4)
                fireballs.sx = ger/4
                fireballs.sy = ger/4
                fireballs.what = 25 * (len(balls)//4)
                    
                fireballs.step(balls[int(B)])
        elif style == 3: # Style 3: Mario Firebar
            if B < len(balls):
                B += 1
                fireballs.angle = 0
                fireballs.sx = (ger/5)*i+20
                fireballs.sy = (ger/5)*i+20
            fireballs.step(boss_man)
        elif style == 4: # Style 4: The Cooler Mario Firebar
            if B < len(balls):
                B += 1
                fireballs.angle = 0
                fireballs.what = time*i*10-20
                fireballs.sx = (ger/5)*i+20
                fireballs.sy = (ger/5)*i+20
            fireballs.step(boss_man)
        elif style == 5: #Style 5: Wings
            if B < len(balls):
                B += 1
                if i % 2 == 1:
                    fireballs.angle = 1/2
                    fireballs.am = 1
                    fireballs.what = (time)*(i//2)*10-20
                else:
                    fireballs.angle = 0
                    fireballs.am = -1
                    fireballs.what = (0-time)*(i//2)*10+20
                fireballs.sx = (i//2)*30+30
                fireballs.sy = (i//2)*30+30
            fireballs.step(boss_man)
        elif style == 6: # Style 6: Cool Swirl (Accident)
            if B < len(balls):
                if B < len(balls)/2:
                    B += 1
                    fireballs.sx = len(balls)*10-(i*20)
                    fireballs.sy = i*20
                else:
                    fireballs.sx = i*20
                    fireballs.sy = len(balls)*10-(i*20)
            fireballs.step(boss_man)
        elif style == 7: # Style 7: Some other cool swirls (Also an Accident)
            if B < len(balls):
                fireballs.am = 2
                B += 1
                if B < len(balls)/2:
                    if i % 2 == 1:
                        fireballs.sy = i*20
                    else:
                        fireballs.sy = i*-20
                else:
                    fireballs.sy = balls[len(balls)-i].sy
            fireballs.step(boss_man)
        elif style == 8: # Style 8: Have half of the balls orbit counterclock wise
            fireballs.sx = ger
            fireballs.sy = ger
            if B < len(balls):
                B += 1
                if i % 2 == 1:
                    fireballs.am = 0-fireballs.am
            fireballs.step(boss_man)
        elif style == 9: # Style 9: Revolving Horizontally
            if B < len(balls):
                B += 1
                if i % 2 == 1:
                    fireballs.sx = 0-ger
            else:
                fireballs.tx = time/2
                if A == 1:
                    if i % 2 == 1:
                        fireballs.sx -= 1
                    else:
                        fireballs.sx += 1
                        if fireballs.sx <= 0-ger:
                            A = 2
                elif A == 2:
                    if i % 2 == 1:
                        fireballs.sx += 1
                        
                    else:
                        fireballs.sx -= 1
                        if fireballs.sx >= ger:
                            A = 1
            fireballs.step(boss_man)
        elif style == 10: # Style 10: Revolving Vertically
            if B < len(balls):
                B += 1
                if i % 2 == 1:
                    fireballs.sy = 0-ger
            else:
                fireballs.tx = time/2
                if A == 1:
                    if i % 2 == 1:
                        fireballs.sy -= 1
                        
                    else:
                        fireballs.sy += 1
                        if fireballs.sy >= ger:
                            A = 2
                elif A == 2:
                    if i % 2 == 1:
                        fireballs.sy += 1
                        
                    else:
                        fireballs.sy -= 1
                        if fireballs.sy <= 0-ger:
                            A = 1
        elif style == 11: # Style 11: In and Out
            if fireballs.sx > 0:
                B -= 0.01
            else:
                B += 0.01
            fireballs.sx += B
            fireballs.sy += B
            if fireballs.sx > rgr+50:
                fireballs.sx = rgr+50
                fireballs.sy = rgr+50
                B = 0
            elif fireballs.sx < 0-(rgr+50):
                fireballs.sx = 0-(rgr+50)
                fireballs.sy = 0-(rgr+50)
                B = 0
            fireballs.step(boss_man)
        elif style == 12: # Style 12: E G G
            if fireballs.y < boss_man.y:
                fireballs.sy = ger*1.25
            else:
                fireballs.sy = ger*0.75
            fireballs.sx = ger
            fireballs.step(boss_man)
        elif style == 13: # Style 13: Crumbling
            if fireballs.am < 0:
                fireballs.am += 0.01
            else:
                fireballs.am -= 0.01
            fireballs.sx += random.randint(-3,1)
            fireballs.sy += random.randint(-3,1)
            fireballs.step(boss_man)
            if fireballs.am < 0.1 and fireballs.am > -0.1:
                style = 14
        elif style == 14: # Style 14: Blowing up
            fireballs.sx += 5
            fireballs.sy += 5
            if abs(fireballs.x+500) > 700 or abs(fireballs.y+500) > 700:
                fireballs.hp = 0
            fireballs.step(boss_man)
        elif style == 15: # Style 15: Pengilum or whatever it is
            fireballs.am = 0
            fireballs.what = time
            fireballs.step(boss_man)
        elif style == 16: # Style 16: Preparing!
            ger = rgr
            if time >= 0 and A == 1:
                time = 0
                A = 0
            fireballs.am = 0
            fireballs.what = time
            fireballs.step(boss_man)
            if time >= 20:
                for j in balls:
                    j.am = 2
                    j.what = 20
                style = random.randint(0,12)
                time = 0
                A = 1
    
    return [balls,style,ger,A,B,time]