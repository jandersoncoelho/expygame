from random import randint
from sys import exit

import pygame
from pygame.locals import *

# Definição das cores
cores = dict(PRETO=(0, 0, 0),
             CINZA=(150, 150, 150),
             VERMELHO=(255, 0, 0),
             BRANCO=(255, 255, 255),
             AZUL=(0, 0, 255),
             VERDE=(0, 255, 0))

# Inicialização do Pygame
pygame.init()

# Colocando música de fundo
pygame.mixer.music.set_volume(0.1)
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

velocidade: int = 20
x_controle = velocidade
y_controle = 0

x_maca = randint(10, 600)
y_maca = randint(50, 430)

# Inicializando as variáveis que vão controlar o placar
pontos: int = 0
fonte = pygame.font.SysFont('arial', 40, True, True)
posicao_placar = (590, 10)

# Criação da janela
tela = pygame.display.set_mode(tamanho_janela)
icone = pygame.image.load('imagens/snake.png')
pygame.display.set_icon(icone)
pygame.display.set_caption('Jogo da Cobrinha')
relogio = pygame.time.Clock()

# Criando variável que controla o corpo da cobrinha
lista_corpo_cobrinha = []
comprimento_incial_cobrinha = 5

# Inicicializando variável que trata do "Game Over" do jogo
morreu = False


def aumenta_corpo_cobrinha(corpo_cobrinha: list):
    """

    Função que desenha o corpo da cobrinha conforme o tamanho da lista fornecida
    :corpo_cobrinha: list
    """
    for pos_x_y in corpo_cobrinha:
        pygame.draw.rect(tela, cores['VERDE'], [pos_x_y[0], pos_x_y[1], 20, 20])


def reiniciar_jogo():
    global pontos, comprimento_incial_cobrinha, x_cobrinha, y_cobrinha, lista_corpo_cobrinha, lista_cabeca_cobrinha, \
        x_maca, y_maca, morreu
    pontos = 0
    comprimento_incial_cobrinha = 5
    x_cobrinha = int(largura // 2.6)
    y_cobrinha = int(altura // 2.6)
    lista_corpo_cobrinha = []
    lista_cabeca_cobrinha = [x_cobrinha, y_cobrinha]
    x_maca = randint(10, 590)
    y_maca = randint(50, 430)
    morreu = False


try:

    # Loop principal do jogo
    while True:
        relogio.tick(10)

        # Limpe a tela
        tela.fill(cores['BRANCO'])

        # Inserindo mensagem de pontuação
        mensagem = f'Pontos: {pontos}'
        texto_formatado = fonte.render(mensagem, True, cores['PRETO'])

        # Controlando eventos do Jogo
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            # Controlando os movimentos da cobrinha
            if event.type == KEYDOWN:
                if event.key == K_a:
                    # Fazendo com que a cobrinha vá somente para a direita
                    if x_controle == velocidade:
                        pass
                    else:
                        x_controle = -velocidade
                        y_controle = 0
                elif event.key == K_d:
                    # Fazendo com que a cobrinha vá somente para a esquerda
                    if x_controle == -velocidade:
                        pass
                    else:
                        x_controle = velocidade
                        y_controle = 0
                elif event.key == K_w:
                    # Fazendo com que a cobrinha vá somente para cima
                    if y_controle == velocidade:
                        pass
                    else:
                        y_controle = -velocidade
                        x_controle = 0
                elif event.key == K_s:
                    # Fazendo com que a cobrinha vá somente para baixo
                    if y_controle == -velocidade:
                        pass
                    else:
                        y_controle = velocidade
                        x_controle = 0

        x_cobrinha = x_cobrinha + x_controle
        y_cobrinha = y_cobrinha + y_controle

        # Verifica se a cobrinha está saindo da tela e faz ela aparecer do lado oposto
        if x_cobrinha < 0:
            x_cobrinha = largura
        elif x_cobrinha > largura:
            x_cobrinha = 0
        if y_cobrinha < 0:
            y_cobrinha = altura
        elif y_cobrinha > altura:
            y_cobrinha = 0

        # desenhando os retângulos
        cobrinha = pygame.draw.rect(tela, cores['VERDE'], [x_cobrinha, y_cobrinha, 20, 20])
        maca = pygame.draw.rect(tela, cores['VERMELHO'], [x_maca, y_maca, 20, 20])

        # Evento de colisão com a maçã
        if cobrinha.colliderect(maca):
            x_maca = randint(10, 590)
            y_maca = randint(50, 430)
            pontos += 1
            barulho_colisao.play()
            comprimento_incial_cobrinha += 1

        # trabalhando com o corpo da cobrinha
        lista_cabeca_cobrinha = [x_cobrinha, y_cobrinha]
        lista_corpo_cobrinha.append(lista_cabeca_cobrinha)

        # Tratando o Game Over
        if lista_corpo_cobrinha.count(lista_cabeca_cobrinha) > 1:
            fonte2 = pygame.font.SysFont('arial', 20, True, True)
            mensagem = 'Game over! Pressione a tecla R para jogar novamente'
            texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
            ret_texto = texto_formatado.get_rect()
            print('MORREU!!')
            morreu = True
            while morreu:
                tela.fill(cores["BRANCO"])
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                    # Controlando os movimentos da cobrinha
                    if event.type == KEYDOWN:
                        if event.key == K_r:
                            reiniciar_jogo()
                    else:
                        break
                    ret_texto.center = (largura // 2, altura // 2)
                    tela.blit(texto_formatado, ret_texto)
                    pygame.display.update()
        # Controlando o tamanho da cobrinha
        if len(lista_corpo_cobrinha) > comprimento_incial_cobrinha:
            del lista_corpo_cobrinha[0]

        aumenta_corpo_cobrinha(lista_corpo_cobrinha)
        print(lista_corpo_cobrinha)

        # Atualize a tela
        tela.blit(texto_formatado, posicao_placar)
        pygame.display.update()

except Exception as e:
    print(f'Erro ao exibir a janela! {e}')
finally:
    exit()
