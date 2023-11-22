import os
import pygame
from classes import *

pygame.init()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

screen = pygame.display.set_mode((501, 392))

background = pygame.image.load(r'imagem/Insper-Pong.png')

fps = pygame.time.Clock()

running = True

ButtonGroups = pygame.sprite.Group()

Button_1 = Botao(ButtonGroups)
Button_1.rect.center = (280, 280)

Button_2 = Botao(ButtonGroups)
Button_2.rect.center = (280, 280)

while running:
    fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0))
    screen.blit(background, (0, 0))

    ButtonGroups.update()
    ButtonGroups.draw(screen)

    pygame.display.update()
