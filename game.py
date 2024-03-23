import pygame
from pygame.locals import *
from sys import exit


def desenhar_carrinho(pos_x) -> object:
    # Desenhe o corpo do carrinho (retângulo)
    pygame.draw.rect(tela, cores['CINZA'], [pos_x, altura // 3, largura // 2, altura // 4])

    # Desenhe as rodas do carrinho (círculos)
    pygame.draw.circle(tela, cores['PRETO'], (pos_x + 30, altura // 2 + 60), 40)
    pygame.draw.circle(tela, cores['PRETO'], (pos_x + 360, altura // 2 + 60), 40)

    # Desenhe as janelas do carrinho (retângulos)
    pygame.draw.rect(tela, cores['BRANCO'], [pos_x, altura // 3.2, largura // 3.25, altura // 8])


# Definição das cores
cores = {'PRETO': (0, 0, 0),
         'CINZA': (150, 150, 150),
         'VERMELHO': (255, 0, 0),
         'BRANCO': (255, 255, 255),
         'AZUL': (0, 0, 255)
         }
try:
    # Inicialização do Pygame
    pygame.init()

    # Definição das dimensões da janela
    largura = 800
    altura = 600
    tamanho_janela = (largura, altura)
    posicao_x = largura // 4

    # Criação da janela
    tela = pygame.display.set_mode(tamanho_janela)
    icone = pygame.image.load('imagens/icon.png')
    pygame.display.set_icon(icone)
    relogio = pygame.time.Clock()
    pygame.display.set_caption('Meu Jogo')

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # Limpe a tela
        relogio.tick(100)
        tela.fill(cores['BRANCO'])

        # desenhando o carrinho
        desenhar_carrinho(posicao_x)

        # Atualiza a posição do carrinho
        posicao_x += 1

        if posicao_x > largura:
            posicao_x = 0
        # Atualize a tela
        pygame.display.update()

except Exception as e:
    print(f'Erro ao exibir a janela! {e}')
finally:
    exit()
