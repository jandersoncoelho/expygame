from typing import List, Any

import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Definição das cores
cores = dict(PRETO=(0, 0, 0),
             CINZA=(150, 150, 150),
             VERMELHO=(255, 0, 0),
             BRANCO=(255, 255, 255),
             AZUL=(0, 0, 255),
             VERDE=(0, 255, 0))


def aumenta_cobrinha(tela, lista_corpo_cobrinha):
    for pos_x_y in lista_corpo_cobrinha:
        pygame.draw.rect(tela, cores['VERDE'], [pos_x_y[0], pos_x_y[1], 20, 20])


def start_game():
    try:

        lista_corpo_cobrinha: list[Any] = []
        # Inicialização do Pygame
        pygame.init()

        # Colocando música de fundo
        pygame.mixer.music.set_volume(0.01)
        pygame.mixer.music.load('sons/BoxCat Games - CPU Talk.mp3')
        pygame.mixer.music.play(-1)

        # Carrregando o som da colisão
        barulho_colisao = pygame.mixer.Sound('sons/smw_coin.wav')

        # Definição das dimensões da janela
        largura = 800
        altura = 600
        tamanho_janela = (largura, altura)
        x_cobrinha = int(largura // 2.6)
        y_cobrinha = int(altura // 2.6)
        x_maca = randint(10, 600)
        y_maca = randint(50, 430)

        # Criação da janela
        tela = pygame.display.set_mode(tamanho_janela)
        icone = pygame.image.load('imagens/snake.png')
        pygame.display.set_icon(icone)
        pygame.display.set_caption('Jogo da Cobrinha')
        relogio = pygame.time.Clock()

        # Inicializando as variáveis que vão controlar o placar
        pontos = 0
        fonte = pygame.font.SysFont('arial', 40, True, True)
        posicao_placar = (590, 10)

        # Loop principal do jogo
        while True:
            relogio.tick(10)

            # Limpe a tela
            tela.fill(cores['BRANCO'])

            # Inserindo mensagem de pontuação
            mensagem = f'Pontos: {pontos}'
            texto_formatado = fonte.render(mensagem, True, cores['PRETO'])
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            # Movimenta enquanto estiver com a tecla pressionada
            if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
                x_cobrinha -= 20
            elif pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
                x_cobrinha += 20
            elif pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
                y_cobrinha -= 20
            elif pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
                y_cobrinha += 20
            # print(f'O retângulo vemelho está nas coodenadas {x_cobrinha}, {y_cobrinha}')

            # Verifica se a cobrinha está saindo da tela
            if x_cobrinha < 0:
                x_cobrinha = 0
            elif x_cobrinha > largura - 20:  # 100 é a largura do retângulo
                x_cobrinha = largura - 20
            if y_cobrinha < 0:
                y_cobrinha = 0
            elif y_cobrinha > altura - 20:  # 100 é a altura do retângulo
                y_cobrinha = altura - 20

            # desenhando os retângulos
            cobrinha = pygame.draw.rect(tela, cores['VERDE'], [x_cobrinha, y_cobrinha, 20, 20])
            maca = pygame.draw.rect(tela, cores['VERMELHO'], [x_maca, y_maca, 20, 20])

            # Evento de colisão com a maçã
            if cobrinha.colliderect(maca):
                x_maca = randint(10, 590)
                y_maca = randint(50, 430)
                pontos += 1
                barulho_colisao.play()

                # trababalhando com o corpo da cobrinha
                lista_cabeca_cobrinha = [int(x_cobrinha), int(y_cobrinha)]
                lista_corpo_cobrinha.append(lista_cabeca_cobrinha)
                aumenta_cobrinha(tela, lista_corpo_cobrinha)
                print(lista_corpo_cobrinha)

            # Atualize a tela
            tela.blit(texto_formatado, posicao_placar)
            pygame.display.update()

    except Exception as e:
        print(f'Erro ao exibir a janela! {e}')
    finally:
        exit()


if __name__ == '__main__':
    start_game()
