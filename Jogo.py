import pygame

pygame.init()

screen = pygame.display.set_mode((501,392))

background = pygame.image.load('imagem/Insper-Pong.png')



runing = True

while runing:
    screen.fill((0))
    screen.blit(background,(0,0))

    pygame.display.update()