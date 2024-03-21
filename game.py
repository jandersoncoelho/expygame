import pygame
from pygame.locals import *
from sys import exit


def desenhar_carrinho() -> object:
    # Desenhe o corpo do carrinho (retângulo)
    pygame.draw.rect(tela, CINZA, [largura // 4, altura // 3, largura // 2, altura // 4])

    # Desenhe as rodas do carrinho (círculos)
    pygame.draw.circle(tela, PRETO, (largura // 3, altura // 2 + 60), 40)
    pygame.draw.circle(tela, PRETO, (largura // 1.5, altura // 2 + 60), 40)

    # Desenhe as janelas do carrinho (retângulos)
    pygame.draw.rect(tela, BRANCO, [largura // 3.2, altura // 3.2, largura // 530, altura // 45])
    pygame.draw.rect(tela, BRANCO, [largura // 1.7, altura // 3.2, largura // 1, altura // 8])


# Definição das cores
PRETO = (0, 0, 0)
CINZA = (150, 150, 150)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

try:
    # Inicialização do Pygame
    pygame.init()

    # Definição das dimensões da janela
    largura = 800
    altura = 600
    tamanho_janela = (largura, altura)

    # Criação da janela
    tela = pygame.display.set_mode(tamanho_janela)
    icone = pygame.image.load('imagens/icon.png')
    pygame.display.set_icon(icone)
    pygame.display.set_caption('Meu Jogo')

    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # Limpe a tela
        tela.fill(BRANCO)

        # desenhando o carrinho
        desenhar_carrinho()

        # Atualize a tela
        pygame.display.update()

except Exception as e:
    print(f'Erro ao exibir a janela! {e}')
finally:
    exit()
