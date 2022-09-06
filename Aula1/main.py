# Primeiro jogo python

import pygame
from random import randint

pygame.init()

tela_x = 1600
tela_y = 1000
x = tela_x/2
y = tela_y/2
pos_x = tela_x/3
pos_y = 50
veloc = 20
veloc_outros = 30

janela = pygame.display.set_mode((tela_x, tela_y))
pygame.display.set_caption("Primeiro jogo em Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP] and y >= 50:
        y -= veloc
    if comandos[pygame.K_DOWN] and y <= tela_y-50:
        y += veloc
    if comandos[pygame.K_LEFT] and x >= 50:
        x -= veloc
    if comandos[pygame.K_RIGHT] and x <= tela_x-50:
        x += veloc
    if pos_y <= -100:
        pos_y = randint(800, 2000)

    pos_y -= veloc_outros
    #pos_x -= veloc_outros

    janela.fill((0, 0, 0))
    pygame.draw.circle(janela, (0, 255, 0), (x, y), 30)
    pygame.draw.circle(janela, (255, 0, 0), (pos_x, pos_y), 30)
    pygame.draw.circle(janela, (0, 0, 255), (pos_x+randint(100, 500), pos_y+100), 30)
    pygame.display.update()
pygame.quit()