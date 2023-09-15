import pygame
import boss
import random
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

#Link = pygame.image.load('link.png') #load your spritesheet
metal = pygame.image.load('./metal.png') #load your spritesheet
brick = pygame.image.load('./brick.png')
#Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

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
potato = True
#           animation variables variables
frameWidth = 32
frameHeight = 46
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN
#end of player variables ---------------------#

#start of patra variables --------------------#
fire = []
balls = 16
for i in range(balls):
    j = i/balls-1/balls
    fire.append(boss.fireball(boss_patra,j))
firetimer = 0
style = 16
stylevarA = 1
stylevarB = 0
stylevarC = 0


while not gameover:
    clock.tick(60) #FPS
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
            y_offset+=3
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
    if keys[SHOOT] == True and sword.isAlive == False:
        
        sword.shoot(xpos, ypos, direction)
    sword.move()

    if sword.xpos <= 50 or sword.xpos >= 800 or sword.ypos <= 50 or sword.ypos >= 850:
        sword.kill()

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

    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos + frameWidth > 850:
        xpos-=3
    if xpos + frameHeight < 0:
        xpos+=3
    #END PLAYER TO WALL COLLISION---------------------------------------------------------#

    #START OF BOSS MOVEMENT

    if boss_patra.hp <= 0 and bossalive:
        bossalive = False
        style = 13
    
    if style != 16:
        boss_patra.step()

    #START OF FIREBALL MOVEMENT------------------------------------------------------#
    for i in range(len(fire)):
        
        if style == 0: # Style 0: do nothing, become normal
            stylevarA = 0
            stylevarB = 0
            fire[i].tx = 0
            fire[i].ty = 0
            fire[i].sx = 200
            fire[i].sy = 200
            fire[i].step(boss_patra)
        elif style == 1: # Style 1: do the cool swaying
            fire[i].tx = firetimer/2
            if stylevarA == 1:
                fire[i].sy -= 1
                if fire[i].sy <= -200:
                    stylevarA = 2
            elif stylevarA == 2:
                fire[i].sy += 1
                if fire[i].sy >= 200:
                    stylevarA = 0
                    stylevarB = 1
            if stylevarB == 1:
                fire[i].sx -= 1
                if fire[i].sx <= -200:
                    stylevarB = 2
            elif stylevarB == 2:
                fire[i].sx += 1
                if fire[i].sx >= 200:
                    stylevarA = 1
                    stylevarB = 0
            fire[i].step(boss_patra)
        elif style == 2: # Style 2: 3 orbiting 2
            if i % 4 == 0:
                fire[i].step(boss_patra)
                stylevarB = i
            else:
                fire[i].am = 3/(len(fire)//4)
                fire[i].sx = 50
                fire[i].sy = 50
                fire[i].what = 25 * (len(fire)//4)
                    
                fire[i].step(fire[int(stylevarB)])
        elif style == 3: # Style 3: Mario Firebar
            if stylevarB < len(fire):
                stylevarB += 1
                fire[i].angle = 0
                fire[i].sx = 20*i+20
                fire[i].sy = 20*i+20
            fire[i].step(boss_patra)
        elif style == 4: # Style 4: The Cooler Mario Firebar
            if stylevarB < len(fire):
                stylevarB += 1
                fire[i].angle = 0
                fire[i].what = firetimer*i*10-20
                fire[i].sx = 20*i+20
                fire[i].sy = 20*i+20
            fire[i].step(boss_patra)
        elif style == 5: #Style 5: Wings
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fire[i].angle = 1/2
                    fire[i].am = 1
                    fire[i].what = (firetimer)*(i//2)*10-20
                else:
                    fire[i].angle = 0
                    fire[i].am = -1
                    fire[i].what = (0-firetimer)*(i//2)*10+20
                fire[i].sx = (i//2)*30+30
                fire[i].sy = (i//2)*30+30
            fire[i].step(boss_patra)
        elif style == 6: # Style 6: Cool Swirl (Accident)
            if stylevarB < len(fire):
                if stylevarB < len(fire)/2:
                    stylevarB += 1
                    fire[i].sx = len(fire)*10-(i*20)
                    fire[i].sy = i*20
                else:
                    fire[i].sx = i*20
                    fire[i].sy = len(fire)*10-(i*20)
            fire[i].step(boss_patra)
        elif style == 7: # Style 7: Some other cool swirls (Also an Accident)
            if stylevarB < len(fire):
                fire[i].am = 2
                stylevarB += 1
                if stylevarB < len(fire)/2:
                    if i % 2 == 1:
                        fire[i].sy = i*20
                    else:
                        fire[i].sy = i*-20
                else:
                    fire[i].sy = fire[len(fire)-i].sy
            fire[i].step(boss_patra)
        elif style == 8: # Style 8: Have half of the balls orbit counterclock wise
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fire[i].am = 0-fire[i].am
            fire[i].step(boss_patra)
        elif style == 9: # Style 9: Revolving Horizontally
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fire[i].sx = -100
            else:
                fire[i].tx = firetimer/2
                if stylevarA == 1:
                    if i % 2 == 1:
                        fire[i].sx -= 1
                    else:
                        fire[i].sx += 1
                        if fire[i].sx <= -200:
                            stylevarA = 2
                elif stylevarA == 2:
                    if i % 2 == 1:
                        fire[i].sx += 1
                        
                    else:
                        fire[i].sx -= 1
                        if fire[i].sx >= 100:
                            stylevarA = 1
            fire[i].step(boss_patra)
        elif style == 10: # Style 10: Revolving Vertically
            if stylevarB < len(fire):
                stylevarB += 1
                if i % 2 == 1:
                    fire[i].sy = -100
            else:
                fire[i].tx = firetimer/2
                if stylevarA == 1:
                    if i % 2 == 1:
                        fire[i].sy -= 1
                        
                    else:
                        fire[i].sy += 1
                        if fire[i].sy >= 200:
                            stylevarA = 2
                elif stylevarA == 2:
                    if i % 2 == 1:
                        fire[i].sy += 1
                        
                    else:
                        fire[i].sy -= 1
                        if fire[i].sy <= -200:
                            stylevarA = 1
        elif style == 11: # Style 11: In and Out
            if fire[i].sx > 0:
                stylevarB -= 0.01
            else:
                stylevarB += 0.01
            fire[i].sx += stylevarB
            fire[i].sy += stylevarB
            if fire[i].sx > 250:
                fire[i].sx = 250
                fire[i].sy = 250
                stylevarB = 0
            elif fire[i].sx < -250:
                fire[i].sx = -250
                fire[i].sy = -250
                stylevarB = 0
            fire[i].step(boss_patra)
        elif style == 12: # Style 12: E G G
            if fire[i].y < boss_patra.y:
                fire[i].sy = 250
            else:
                fire[i].sy = 175
            fire[i].step(boss_patra)
        elif style == 13: # Style 13: Crumbling
            if fire[i].am < 0:
                fire[i].am += 0.01
            else:
                fire[i].am -= 0.01
            fire[i].sx += random.randint(-3,1)
            fire[i].sy += random.randint(-3,1)
            fire[i].step(boss_patra)
            if fire[i].am < 0.1 and fire[i].am > -0.1:
                style = 14
        elif style == 14: # Style 14: Blowing up
            fire[i].sx += 5
            fire[i].sy += 5
            if abs(fire[i].x+500) > 700 or abs(fire[i].y+500) > 700:
                fire[i].alive = False
            fire[i].step(boss_patra)
        elif style == 15: # Style 15: Pengilum or whatever it is
            fire[i].am = 0
            fire[i].what = firetimer
            fire[i].step(boss_patra)
        elif style == 16: # Style 16: Preparing!
            if firetimer >= 0 and stylevarA == 1:
                firetimer = 0
                stylevarA = 0
            fire[i].am = 0
            fire[i].what = firetimer
            fire[i].step(boss_patra)
            if firetimer >= 20:
                for j in range(len(fire)):
                    fire[j].am = 2
                    fire[j].what = 20
                style = 1
                firetimer = 0
                stylevarA = 1
    #END OF FIREBALL MOVEMENT--------------------------------------------------------#


    #START OF ANIMATION-------------------------------------------------------------------#

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
    boss_patra.draw(screen)
    for i in range (len(fire)):
        fire[i].draw(screen)


    pygame.display.flip()#this actually puts the pixel on the screen
    


    #END OF RENDER--------------------------------------------------------------------#


#end game
#loop------------------------------------------------------------------------------
pygame.quit()