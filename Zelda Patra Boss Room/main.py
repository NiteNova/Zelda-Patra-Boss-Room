import pygame
import math
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

    
    xpos+=vx #update player xpos
    ypos+=vy #update player ypos
    #check space for shooting
    if keys[SHOOT] == True:
        if sword.isAlive == False and rate_limit <= 0:
            rate_limit = 0.75
            sword.shoot(xpos, ypos, direction)

    rate_limit -= delta
    sword.move()

    if sword.xpos <= 50 or sword.xpos >= 800 or sword.ypos <= 50 or sword.ypos >= 850:
        sword.kill()


    #START OF STATUE AND ITS FIREBALL MOVEMENT----------------------------------------------#
    def normalize(x, y):
        l = math.sqrt(x**2 + y**2)
        return x/l, y/l
    if len(stone_statues) == len(stone_fire): #to avoid errors, it checks if the lists have the same length, since logically each statue would have it's own fireball
        for p in range(len(stone_statues)):
            stone_fire[p].movement(xpos, ypos)
            if stone_fire[p].xpos <= 50 or stone_fire[p].xpos >= 800 or stone_fire[p].ypos <= 50 or stone_fire[p].ypos >= 850:
                stone_fire[p].dead()
            if random.randint(0,100) == 0 and stone_fire[p].isAlive == False:
                stone_fire[p].isAlive = True
                stone_fire[p].xpos = stone_statues[p].xpos
                stone_fire[p].ypos = stone_statues[p].ypos
                fire_direction = normalize(xpos -stone_statues[p].xpos, ypos - stone_statues[p].ypos)
                stone_fire[p].xVel = (fire_direction[0]) * delta * 350
                stone_fire[p].yVel = (fire_direction[1]) * delta * 350
    else:
        print("Statues won't work :(")

    #END OF STATUE AND ITS FIREBALL MOVEMENT------------------------------------------------#
   
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
    
    Zed = boss.firestyle(fire,style,generalradius,gr,boss_patra,stylevarA,stylevarB,firetimer)
    
    style = Zed[1]
    generalradius = Zed[2]
    stylevarA = Zed[3]
    stylevarB = Zed[4]
    firetimer = Zed[5]
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

    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render('LIVES:', False, (255, 0, 0))

   

    screen.blit(text_surface, (0,0))

    pygame.display.flip()#this actually puts the pixel on the screen
    


    #END OF RENDER--------------------------------------------------------------------#


#end game
#loop------------------------------------------------------------------------------
pygame.quit()