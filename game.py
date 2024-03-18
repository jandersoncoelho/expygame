import pygame
from pygame.locals import *
from sys import exit

largura = 800
altura = 600
try:
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    icone = pygame.image.load('imagens/icon.png')
    pygame.display.set_icon(icone)
    pygame.display.set_caption('Meu primeiro jogo!')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        pygame.display.update()
except Exception as e:
    print(f'Erro ao exibir a janela! {e}')
finally:
    exit()
