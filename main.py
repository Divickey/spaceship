import pygame
import time

pygame.init()

pygame.display.set_caption("funky space rocket")
screen=pygame.display.set_mode((600,600))
player_x=100
player_y=10
#     up     left   down   right
keys=[False, False, False, False]

space=pygame.image.load("space.png")
tspace=pygame.transform.scale(space,(600,600))
player=pygame.image.load("rocket.png")

while player_y<400:
    screen.blit(space,(0,0))
    screen.blit(player,(player_x,player_y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN: #pressed
            if event.key == pygame.K_UP:
                keys[0]=True
            if event.key == pygame.K_LEFT:
                keys[1]=True
            if event.key == pygame.K_DOWN:
                keys[2]=True
            if event.key == pygame.K_RIGHT:
                keys[3]=True
        if event.type == pygame.KEYUP: #released
            if event.key == pygame.K_UP:
                keys[0]=False
            if event.key == pygame.K_LEFT:
                keys[1]=False
            if event.key == pygame.K_DOWN:
                keys[2]=False
            if event.key == pygame.K_RIGHT:
                keys[3]=False
    if keys[0]: #up
        if player_y > -20:
            player_y -=10
    if keys[1]: #left
        if player_x > -20:
            player_x -=10
    if keys[2]: #down
        if player_y < 470:
            player_y +=10
    if keys[3]: #right
        if player_x < 470:
            player_x +=10
    player_y += 5
    time.sleep(0.05)