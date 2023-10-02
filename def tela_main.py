import pygame
import sys

def fechar():
    pygame.quit()

def desenhar_botao(tela, texto, cor, retangulo, cor_clique, clicado):
    pygame.draw.rect(tela, cor if not clicado else cor_clique, retangulo, 0, 55)
    tela.blit(texto, (retangulo.centerx - texto.get_width() // 2, retangulo.centery - texto.get_height() // 2))

def tela_login():
    pygame.quit()
    pygame.init()
    largura = 1920
    altura = 1080

    imagem_fundo = pygame.image.load("Img/Ex. Notion.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
    posicao_fundo = imagem_fundo.get_rect()

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Tela Inicial")

    cor_fundo = (255, 0, 0)  # Vermelho

    executando_tela = True

    cor_botao = (186, 186, 186)  # Verde
    cor_botao_clique = (111, 111, 111)  # Verde escuro (quando clicado)

    largura_botao = 150
    altura_botao = 150
    posicao_botao_add = pygame.Rect((250 - largura_botao // 0.642, 364, largura_botao, altura_botao))

    # Modifique a posição e o tamanho do botão "Sair"
    largura_botao_sair = 40  # Tornando o botão um pouco menor
    altura_botao_sair = 40  # Tornando o botão um pouco menor
    posicao_botao_sair = pygame.Rect(largura - largura_botao_sair - 10, 10, largura_botao_sair, altura_botao_sair)

    fonte1 = pygame.font.Font(None, 200)
    fonte = pygame.font.Font(None, 36)
    texto_botao_add = fonte1.render("+", True, (0, 0, 0))  # Texto preto

    # Modifique a cor do texto do botão "Sair" para branco
    texto_botao_sair = fonte.render("X", True, (255, 255, 255))  # Texto branco

    botao_add_clicado = False
    botao_sair_clicado = False

    while executando_tela:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando_tela = False
                break
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if posicao_botao_add.collidepoint(evento.pos):
                    botao_add_clicado = True
                elif posicao_botao_sair.collidepoint(evento.pos):
                    botao_sair_clicado = True
            elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                if botao_add_clicado and posicao_botao_add.collidepoint(evento.pos):
                    print("Botão Login clicado!")
                if botao_sair_clicado and posicao_botao_sair.collidepoint(evento.pos):
                    print("Botão Sair clicado!")
                    fechar()
                botao_add_clicado = False
                botao_sair_clicado = False

        tela.blit(imagem_fundo, posicao_fundo)

        desenhar_botao(tela, texto_botao_add, (255, 255, 255, 128), posicao_botao_add, cor_botao_clique, botao_add_clicado)
        desenhar_botao(tela, texto_botao_sair, (255, 0, 0), posicao_botao_sair, cor_botao_clique, botao_sair_clicado)  # Alterando a cor do botão

        pygame.display.update()

    pygame.quit()

tela_login()
