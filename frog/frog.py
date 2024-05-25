from sys import exit

import pygame
from pygame.locals import *
from lib import CoresRGB, Sapo

cores = CoresRGB()
pygame.init()

# Definição das dimensões da janela
largura = 800
altura = 600
tamanho_janela = (largura, altura)

# Criação da janela
tela = pygame.display.set_mode(tamanho_janela)
icone = pygame.image.load('../imagens/frog.png')
pygame.display.set_icon(icone)
pygame.display.set_caption('Sprite de um sapo')
cor_janela = cores.get_cor("PRETO")

try:
    todas_as_sprites = pygame.sprite.Group()
    sapo = Sapo()
    todas_as_sprites.add(sapo)

    relogio = pygame.time.Clock()

    while True:
        relogio.tick(30)
        tela.fill(cor_janela)
        # Controlando eventos do Jogo
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                sapo.atacar()

        todas_as_sprites.draw(tela)
        todas_as_sprites.update()
        pygame.display.flip()

except Exception as e:
    print(f'Erro ao exibir a janela! {e}')
finally:
    exit()
