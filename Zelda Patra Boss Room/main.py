import pygame
import boss
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
boss_patra = boss.patra(250, 250)


#MAP: 1 is grass, 2 is brick
map = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 0,2],
       [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,2 ,2, 2,2]]

#Link = pygame.image.load('link.png') #load your spritesheet
metal = pygame.image.load('./metal.png') #load your spritesheet
brick = pygame.image.load('./brick.png')
PotatoPic = pygame.image.load("./potato1.jpg")
#Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#start of player variables --------------------#
xpos = 400 #xpos of player
ypos = 400 #ypos of player
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
fire = [boss.fireball(boss_patra),boss.fireball(boss_patra,1/4),boss.fireball(boss_patra, 1/2),boss.fireball(boss_patra,3/4),boss.fireball(boss_patra,1/8),boss.fireball(boss_patra,3/8),boss.fireball(boss_patra, 5/8),boss.fireball(boss_patra,7/8)]




while not gameover:
    clock.tick(60) #FPS
    
   
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
    if keys[SHOOT] == True:
        sword.shoot(xpos, ypos, direction)

    sword.move()


    xpos+=vx #update player xpos
    ypos+=vy

   
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
    if xpos + frameWidth > 800:
        xpos-=3
    if xpos + frameHeight < 0:
        xpos+=3
    #END PLAYER TO WALL COLLISION---------------------------------------------------------#


    #START OF ANIMATION-------------------------------------------------------------------#
    # Update Animation Information
    if movingx == True or movingy == True: #animate when moving
        ticker+=1
        if ticker % 10 == 0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum > 7:
           frameNum = 0
    #END OF ANIMATION-----------------------------------------------------------------#

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
    pygame.display.flip()#this actually puts the pixel on the screen
    #END OF RENDER--------------------------------------------------------------------#


#end game
#loop------------------------------------------------------------------------------
pygame.quit()