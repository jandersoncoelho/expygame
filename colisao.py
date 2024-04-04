import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Definição das cores
cores = dict(PRETO=(0, 0, 0),
             CINZA=(150, 150, 150),
             VERMELHO=(255, 0, 0),
             BRANCO=(255, 255, 255),
             AZUL=(0, 0, 255))


def desenhar_retangulo(tela, cor, largura=100, altura=100, pos_x=0, pos_y=0):
    return pygame.draw.rect(tela, cor, [pos_x, pos_y, largura // 8, altura // 8])


def start_game():
    try:

        # Inicialização do Pygame
        pygame.init()

        # Definição das dimensões da janela
        largura = 800
        altura = 600
        tamanho_janela = (largura, altura)
        x_vermelho = largura // 2.6
        y_vermelho = altura // 2.6
        x_azul = randint(10, 600)
        y_azul = randint(50, 430)

        # Criação da janela
        tela = pygame.display.set_mode(tamanho_janela)
        icone = pygame.image.load('imagens/icon.png')
        pygame.display.set_icon(icone)
        pygame.display.set_caption('Movimentação')
        relogio = pygame.time.Clock()

        # Inicializando as variáveis que vão controlar o placar
        pontos = 0
        fonte = pygame.font.SysFont('arial', 40, True, True)
        posicao_placar = (590, 10)

        # Loop principal do jogo
        while True:
            relogio.tick(10)

            # Limpe a tela

            # Inserindo mensagem de pontuação
            mensagem = f'Pontos: {pontos}'
            texto_fomatado = fonte.render(mensagem, True, cores['BRANCO'])
            tela.fill(cores['PRETO'])
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            # Movimenta enquanto estiver com a tecla pressionada\
            if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
                x_vermelho -= 20
            elif pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
                x_vermelho += 20
            elif pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
                y_vermelho -= 20
            elif pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
                y_vermelho += 20
            print(f'O retângulo vemelho está nas coodenadas {x_vermelho}, {y_vermelho}')

            # Verifica se o retângulo vermelho está saindo da tela
            if x_vermelho < 0:
                x_vermelho = 0
            elif x_vermelho > largura - 100:  # 100 é a largura do retângulo
                x_vermelho = largura - 100

            if y_vermelho < 0:
                y_vermelho = 0
            elif y_vermelho > altura - 75:  # 100 é a altura do retângulo
                y_vermelho = altura - 75
            # desenhando os retângulos
            ret_vermelho = desenhar_retangulo(tela, cores['VERMELHO'], largura, altura, x_vermelho, y_vermelho)
            ret_azul = desenhar_retangulo(tela, cores['AZUL'], largura, altura, x_azul, y_azul)

            if ret_vermelho.colliderect(ret_azul):
                x_azul = randint(10, 590)
                y_azul = randint(50, 430)
                pontos += 1

            # Atualize a tela
            tela.blit(texto_fomatado, posicao_placar)
            pygame.display.update()

    except Exception as e:
        print(f'Erro ao exibir a janela! {e}')
    finally:
        exit()


if __name__ == '__main__':
    start_game()
