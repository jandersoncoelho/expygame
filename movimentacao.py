import pygame
from pygame.locals import *
from sys import exit

# Definição das cores
PRETO = (0, 0, 0)
CINZA = (150, 150, 150)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)


def desenhar_retangulo(tela, largura=100, altura=100, pos_x=0, pos_y=0):
    pygame.draw.rect(tela, VERMELHO, [pos_x, pos_y, largura // 4, altura // 4])



def start_game():
    try:

        # Inicialização do Pygame
        pygame.init()

        # Definição das dimensões da janela
        largura = 800
        altura = 600
        x = largura // 2.6
        y = 0
        tamanho_janela = (largura, altura)

        # Criação da janela
        tela = pygame.display.set_mode(tamanho_janela)
        icone = pygame.image.load('imagens/icon.png')
        pygame.display.set_icon(icone)
        pygame.display.set_caption('Movimentação')
        relogio = pygame.time.Clock()

        # Loop principal do jogo
        while True:
            relogio.tick(100)
            tela.fill(PRETO)
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            # Limpe a tela

            # desenhando o carrinho
            desenhar_retangulo(tela, largura, altura, x, y)
            if y >= altura:
                y = 0
            y += 1
            # Atualize a tela
            pygame.display.update()

    except Exception as e:
        print(f'Erro ao exibir a janela! {e}')
    finally:
        exit()


if __name__ == '__main__':
    start_game()
