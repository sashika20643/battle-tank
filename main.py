import pygame
import math
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space figter")
icon = pygame.image.load('tank.png')
pygame.display.set_icon(icon)
# player
playerImg = pygame.image.load('player.png')
playerx = 370
playery = 480
pxincrease = 0
pyincrease = 0
protate = 0
prState = "U"

# bullet
bulletImg = pygame.image.load('bullet(1).png')
bulletx =0
bullety =0
brotate = protate
bxincrease = 0
byincrease = 0
brstate = 'U'
bstate = "ready"

#enemy
enemyImg = pygame.image.load('tank.png')
enemyx =[0,random.randint(0, 736),736,random.randint(0, 736)]
enemyy =[random.randint(0, 536),0,random.randint(0, 536),536]
exincrease =[0,0,-.1,0]
eyincrease = [0.1,.1,0,-.1]
erotate= [90,0,-90,180]
running = True


marks=2

def enemy(x, y, enemyImg2):
    screen.blit(enemyImg2, (x, y))


def player(x, y, playerImg2):
    screen.blit(playerImg2, (x, y))
    # bullet draw


def bullet(x, y, bulletImg2):
    screen.blit(bulletImg2, (x + 16, y + 16))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:

                pxincrease = -0.1

                protate = 90



            if event.key == pygame.K_RIGHT:
                pxincrease = 0.1
                protate = -90



            if event.key == pygame.K_UP:
                pyincrease = -0.1
                protate = 0
            if event.key == pygame.K_DOWN:
                pyincrease = 0.1
                protate = 180
            if event.key == pygame.K_SPACE:
                if bstate == "ready":
                    bstate = "fire"
                    bulletx = playerx
                    bullety = playery
                    brotate=protate

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pxincrease = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                pyincrease = 0
    screen.fill((130, 50, 70))
    playerImg2 = pygame.transform.rotate(playerImg, protate)
    enemyx[0]+=exincrease[0]
    enemyy[0]+=eyincrease[0]
    enemy(enemyx[0],enemyy[0],enemyImg)

    bulletImg2 = pygame.transform.rotate(bulletImg, brotate)
    playerx += pxincrease
    playery += pyincrease
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    if playery <= 0:
        playery = 0
    elif playery >= 536:
        playery = 536


    if (bstate == "fire"):
        byincrease = 0
        bxincrease = 0
        if (brotate == 0):
            byincrease = -0.5
        elif brotate == 90:
            bxincrease = -0.5
        elif brotate == -90:
            bxincrease = 0.5
        else:
            byincrease = 0.5
        bulletx += bxincrease
        bullety += byincrease
        bullet(bulletx, bullety, bulletImg2)
    if bulletx <= 0 or bulletx >= 800 or bullety <= 0 or bullety >= 600:
        bulletx = playerx
        bullety = playery
        bstate = "ready"
    player(playerx, playery, playerImg2)
    pygame.display.update()
