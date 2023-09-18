import pygame
import boss
import random
import statues
from sword import throw_sword
pygame.init()  
pygame.display.set_caption("Zelda Game")  # sets the window title
screen = pygame.display.set_mode((850, 900))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SHOOT = 4

sword = throw_sword()
boss_patra = boss.patra(425, 450)
bossalive = True

#MAP: 1 is grass, 2 is brick
map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2]]


metal = pygame.image.load('./metal.png') #load your spritesheet
brick = pygame.image.load('./brick.png')


#start of player variables --------------------#
xpos = 200 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
x_offset = 0
y_offset = 0
keys = [False, False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
movingx = False
movingy = False
#           animation variables variables
frameWidth = 32
frameHeight = 46
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN
#end of player variables ---------------------#

#start of statue variables -------------------#
stone_statues = [statues.enemy(350,500),statues.enemy(500,500)]
stone_fire = [statues.enemy_fireball(350,500),statues.enemy_fireball(500,500)]

#end of statue variables ---------------------#

#start of patra variables --------------------#
fire = []
balls = 16
generalradius = 120 # how far the fireballs will be from the tea- I mean patra
gr = generalradius # saves the original radius
inout = True
for i in range(balls):
    j = i/balls-1/balls
    fire.append(boss.fireball(boss_patra,generalradius,j))
firetimer = 0
style = 16
stylevarA = 1
stylevarB = 0
stylevarC = 0
rate_limit = 0

#end of patra variables--------------------------#

while not gameover:
    delta = clock.tick(60)/1000 #FPS
    firetimer += 1/10
    

    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
     
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT] = True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            elif event.key == pygame.K_UP:
                keys[UP] = True
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = True
            elif event.key == pygame.K_SPACE:
                keys[SHOOT] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT] = False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            elif event.key == pygame.K_UP:
                keys[UP] = False
            elif event.key == pygame.K_DOWN:
                keys[DOWN] = False
            elif event.key == pygame.K_SPACE:
                keys[SHOOT] = False
         
    #LEFT MOVEMENT
    if keys[LEFT] == True:
        if xpos > 400:
            vx = -3
        elif x_offset < 0:
            x_offset+=3
            vx = 0
        else:
            vx = -3
        RowNum = 0
        direction = LEFT
        movingx = True
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        if xpos < 400:
            vx = 3
        elif x_offset > 800:
            x_offset-=3
            vx = 0
        else:
            vx = 3
        RowNum = 1
        direction = RIGHT
        movingx = True
    else:
        vx = 0
        movingx = False
    #DOWN MOVEMENT
    if keys[DOWN] == True:
        if ypos < 400:
            vy = 3
        elif y_offset > 800:
            y_offset-=3
            vy = 0
        else:
            vy = 3
        RowNum = 1
        RowNum = 3
        direction = DOWN
        movingy = True
    #UP MOVEMENT
    elif keys[UP] == True:
        if ypos > 400:
            vy = -3
        elif y_offset < 0:
            y_offset+=6
            vy = 0
        else:
            vy = -3
        RowNum = 0
        RowNum = 2
        direction = UP
        movingy = True
    else:
        vy = 0
        movingy = False

    

    #check space for shooting
    if keys[SHOOT] == True:
        if sword.isAlive == False and rate_limit <= 0:
            rate_limit = 0.75
            sword.shoot(xpos, ypos, direction)

    rate_limit -= delta
    sword.move()

    if sword.xpos <= 50 or sword.xpos >= 800 or sword.ypos <= 50 or sword.ypos >= 850:
        sword.kill()
    
    #if enemy_fireball.xpos <= 50 or enemy_fireball.xpos >= 800 or enemy_fireball.ypos <= 50 or enemy_fireball.ypos >= 850:
    #    enemy_fireball.dead()
    if len(stone_statues) == len(stone_fire): #to avoid errors, it checks if the lists have the same length, since logically each statue would have it's own fireball
        for p in range(len(stone_statues)):
            stone_fire[p].movement(xpos, ypos)
            if random.randint(0,100) == 0 and stone_fire[p].isAlive == False:
                stone_fire[p].isAlive = True
                stone_fire[p].xVel = xpos - stone_statues[p].xpos 
                stone_fire[p].yVel = ypos - stone_statues[p].ypos 
                stone_fire[p].xpos = stone_statues[p].xpos
                stone_fire[p].ypos = stone_statues[p].ypos
    else:
        print("Statues won't work :(")


    xpos+=vx #update player xpos
    ypos+=vy #update player ypos

   
    #START PLAYER TO WALL COLLISION---------------------------------------------------------#
   
    #down collision
    if map[int((ypos - y_offset + frameHeight - 5) / 50)][int((xpos - x_offset + frameWidth / 2) / 51)] == 2:
        ypos-=3
    
    #up collision
    if map[int((ypos - y_offset) / 50)][int((xpos - x_offset + frameWidth / 2) / 50)] == 2:
        ypos+=3
    
    #left collision
    if map[int((ypos - y_offset + frameHeight - 10) / 50)][int((xpos - x_offset - 5) / 50)] == 2 :
        xpos+=3
    
    #right collision
    if map[int((ypos - y_offset) / 50)][int((xpos - x_offset + frameWidth + 5) / 51)] == 2:
        xpos-=3     

    #END PLAYER TO WALL COLLISION---------------------------------------------------------#

    #START OF BOSS MOVEMENT

    if boss_patra.hp <= 0 and bossalive:
        bossalive = False
        style = 13
    
    if style != 16:
        boss_patra.step()

    #START OF FIREBALL MOVEMENT------------------------------------------------------#hihihihi
    
    if inout:
        generalradius += 2
        if generalradius > gr*1.5:
            inout = False
    else:
        generalradius -= 2
        if generalradius < gr*0.5:
            inout = True
    
    for i, fireball in enumerate(fire):
        if style == 0: # Style 0: do nothing, become normal
            stylevarA = 0
            stylevarB = 0
            fireball.tx = 0
            fireball.ty = 0
            fireball.sx = generalradius
            fireball.sy = generalradius
            fireball.step(boss_patra)
        elif style == 1: # Style 1: do the cool swaying
            fireball.tx = firetimer/2
            if stylevarA == 1:
                fireball.sy -= 1
                if fireball.sy <= 0-generalradius:
                    stylevarA = 2
            elif stylevarA == 2:
                fireball.sy += 1
                if fireball.sy >= generalradius:
                    stylevarA = 0
                    stylevarB = 1
            if stylevarB == 1:
                fireball.sx -= 1
                if fireball.sx <= 0-generalradius:
                    stylevarB = 2
            elif stylevarB == 2:
                fireball.sx += 1
                if fireball.sx >= generalradius:
                    stylevarA = 1
                    stylevarB = 0
            fireball.step(boss_patra)
        elif style == 2: # Style 2: 3 orbiting 2
            if i % 4 == 0:
                fireball.step(boss_patra)
                fireball.sx = generalradius
                fireball.sy = generalradius
                stylevarB = i
            else:
                fireball.am = 3/(len(fire)//4)
                fireball.sx = generalradius/4
                fireball.sy = generalradius/4
                fireball.what = 25 * (len(fire)//4)
                    
                fireball.step(fire[int(stylevarB)])
        elif style == 3: # Style 3: Mario Firebar
            if stylevarB < len(fire):
                stylevarB += 1
                fireball.angle = 0
                fireball.sx = (generalradius/5)*i+20
                fireball.sy = (generalradius/5)*i+20
            fireball.step(boss_patra)
        elif style == 4: # Style 4: The Cooler Mario Firebar
            if stylevarB < len(fire):
                stylevarB += 1
                fireball.angle = 0
                fireball.what = firetimer*i*10-20
                fireball.sx = (generalradius/5)*i+20
                fireball.sy = (generalradius/5)*i+20
            fireball.step(boss_patra)
        elif style == 5: #Style 5: Wings
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fireball.angle = 1/2
                    fireball.am = 1
                    fireball.what = (firetimer)*(i//2)*10-20
                else:
                    fireball.angle = 0
                    fireball.am = -1
                    fireball.what = (0-firetimer)*(i//2)*10+20
                fireball.sx = (i//2)*30+30
                fireball.sy = (i//2)*30+30
            fireball.step(boss_patra)
        elif style == 6: # Style 6: Cool Swirl (Accident)
            if stylevarB < len(fire):
                if stylevarB < len(fire)/2:
                    stylevarB += 1
                    fireball.sx = len(fire)*10-(i*20)
                    fireball.sy = i*20
                else:
                    fireball.sx = i*20
                    fireball.sy = len(fire)*10-(i*20)
            fireball.step(boss_patra)
        elif style == 7: # Style 7: Some other cool swirls (Also an Accident)
            if stylevarB < len(fire):
                fireball.am = 2
                stylevarB += 1
                if stylevarB < len(fire)/2:
                    if i % 2 == 1:
                        fireball.sy = i*20
                    else:
                        fireball.sy = i*-20
                else:
                    fireball.sy = fire[len(fire)-i].sy
            fireball.step(boss_patra)
        elif style == 8: # Style 8: Have half of the balls orbit counterclock wise
            fireball.sx = generalradius
            fireball.sy = generalradius
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fireball.am = 0-fireball.am
            fireball.step(boss_patra)
        elif style == 9: # Style 9: Revolving Horizontally
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fireball.sx = 0-generalradius
            else:
                fireball.tx = firetimer/2
                if stylevarA == 1:
                    if i % 2 == 1:
                        fireball.sx -= 1
                    else:
                        fireball.sx += 1
                        if fireball.sx <= 0-generalradius:
                            stylevarA = 2
                elif stylevarA == 2:
                    if i % 2 == 1:
                        fireball.sx += 1
                        
                    else:
                        fireball.sx -= 1
                        if fireball.sx >= generalradius:
                            stylevarA = 1
            fireball.step(boss_patra)
        elif style == 10: # Style 10: Revolving Vertically
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fireball.sy = 0-generalradius
            else:
                fireball.tx = firetimer/2
                if stylevarA == 1:
                    if i % 2 == 1:
                        fireball.sy -= 1
                        
                    else:
                        fireball.sy += 1
                        if fireball.sy >= generalradius:
                            stylevarA = 2
                elif stylevarA == 2:
                    if i % 2 == 1:
                        fireball.sy += 1
                        
                    else:
                        fireball.sy -= 1
                        if fireball.sy <= 0-generalradius:
                            stylevarA = 1
        elif style == 11: # Style 11: In and Out
            if fireball.sx > 0:
                stylevarB -= 0.01
            else:
                stylevarB += 0.01
            fireball.sx += stylevarB
            fireball.sy += stylevarB
            if fireball.sx > gr+50:
                fireball.sx = gr+50
                fireball.sy = gr+50
                stylevarB = 0
            elif fireball.sx < 0-(gr+50):
                fireball.sx = 0-(gr+50)
                fireball.sy = 0-(gr+50)
                stylevarB = 0
            fireball.step(boss_patra)
        elif style == 12: # Style 12: E G G
            if fireball.y < boss_patra.y:
                fireball.sy = generalradius*1.25
            else:
                fireball.sy = generalradius*0.75
            fireball.sx = generalradius
            fireball.step(boss_patra)
        elif style == 13: # Style 13: Crumbling
            if fireball.am < 0:
                fireball.am += 0.01
            else:
                fireball.am -= 0.01
            fireball.sx += random.randint(-3,1)
            fireball.sy += random.randint(-3,1)
            fireball.step(boss_patra)
            if fireball.am < 0.1 and fireball.am > -0.1:
                style = 14
        elif style == 14: # Style 14: Blowing up
            fireball.sx += 5
            fireball.sy += 5
            if abs(fireball.x+500) > 700 or abs(fireball.y+500) > 700:
                fireball.alive = False
            fireball.step(boss_patra)
        elif style == 15: # Style 15: Pengilum or whatever it is
            fireball.am = 0
            fireball.what = firetimer
            fireball.step(boss_patra)
        elif style == 16: # Style 16: Preparing!
            generalradius = gr
            if firetimer >= 0 and stylevarA == 1:
                firetimer = 0
                stylevarA = 0
            fireball.am = 0
            fireball.what = firetimer
            fireball.step(boss_patra)
            if firetimer >= 20:
                for j in range(len(fire)):
                    fire[j].am = 2
                    fire[j].what = 20
                style = random.randint(0,12)
                firetimer = 0
                stylevarA = 1
    #END OF FIREBALL MOVEMENT--------------------------------------------------------#


    #START OF RENDER------------------------------------------------------------------#       
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
   
    #draw map
    for i in range(18):
        for j in range(17):
            if map[i][j] == 1:
                screen.blit(brick, (j * 50 + x_offset, i * 50 + y_offset), (0, 0, 50, 50))
            if map[i][j] == 2:
                screen.blit(metal, (j * 50 + x_offset, i * 50 + y_offset), (0, 0, 50, 50))
    #draw fireball
    if sword.isAlive == True:
        sword.draw(screen)
    #draw player
    pygame.draw.rect(screen, (255, 255, 255), (xpos, ypos, 20, 40))

    #draw enemy and fireballs
    for o in range(len(stone_statues)):
        stone_statues[o].draw(screen)
        stone_fire[o].draw(screen)
    boss_patra.draw(screen)
    for fireball in fire:
        fireball.draw(screen)


    pygame.display.flip()#this actually puts the pixel on the screen
    


    #END OF RENDER--------------------------------------------------------------------#


#end game
#loop------------------------------------------------------------------------------
pygame.quit()