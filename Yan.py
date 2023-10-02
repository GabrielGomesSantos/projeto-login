import pygame
import sys

def abrir_tela_inicial():
    pygame.quit()  # Fecha a tela atual
    tela_inicial()  # Abre a tela inicial

def tela_login():
    pygame.quit()
    pygame.init()
    largura = 500
    altura = 500

    imagem_fundo = pygame.image.load("Img/Img_painel.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
    posicao_fundo = imagem_fundo.get_rect()

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Login")

    cor_fundo = (255, 0, 0)  # Vermelho

    executando_tela = True

    # Adicione duas entradas de texto
    input_caixa1 = pygame.Rect(150, 200, 200, 30)  # Ajuste as coordenadas
    input_caixa2 = pygame.Rect(150, 250, 200, 30)  # Ajuste as coordenadas
    fonte_input = pygame.font.Font(None, 32)
    texto_input1 = ""
    texto_input2 = ""
    cor_input_ativo = pygame.Color('dodgerblue2')
    cor_input_inativo = pygame.Color('lightskyblue3')
    cor_input1 = cor_input_inativo
    cor_input2 = cor_input_inativo
    ativo_input1 = False
    ativo_input2 = False

    # Defina as cores dos botões
    cor_botao = (186, 186, 186)  # Verde
    cor_botao_clique = (111, 111, 111)  # Verde escuro (quando clicado)

    # Defina as dimensões e a posição do botão "Voltar"
    largura_botao_voltar = 200
    altura_botao_voltar = 25
    posicao_botao_voltar = pygame.Rect((250 - largura_botao_voltar // 2, 300, largura_botao_voltar, altura_botao_voltar))

    # Texto do botão "Voltar"
    fonte_botao_voltar = pygame.font.Font(None, 36)
    texto_botao_voltar = fonte_botao_voltar.render("Voltar", True, (0, 0, 0))  # Texto preto

    botao_voltar_clicado = False

    while executando_tela:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando_tela = False
                break
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if input_caixa1.collidepoint(evento.pos):
                    ativo_input1 = not ativo_input1
                    ativo_input2 = False
                elif input_caixa2.collidepoint(evento.pos):
                    ativo_input2 = not ativo_input2
                    ativo_input1 = False
                elif posicao_botao_voltar.collidepoint(evento.pos):
                    botao_voltar_clicado = True
                else:
                    ativo_input1 = False
                    ativo_input2 = False
                cor_input1 = cor_input_ativo if ativo_input1 else cor_input_inativo
                cor_input2 = cor_input_ativo if ativo_input2 else cor_input_inativo
            if evento.type == pygame.KEYDOWN:
                if ativo_input1:
                    if evento.key == pygame.K_RETURN:
                        print("Texto da Caixa 1:", texto_input1)
                        # Salve o texto inserido na variável correspondente
                        texto_caixa1 = texto_input1
                        # Limpe a entrada de texto
                        texto_input1 = ""
                    elif evento.key == pygame.K_BACKSPACE:
                        texto_input1 = texto_input1[:-1]
                    else:
                        texto_input1 += evento.unicode
                elif ativo_input2:
                    if evento.key == pygame.K_RETURN:
                        print("Texto da Caixa 2:", texto_input2)
                        # Salve o texto inserido na variável correspondente
                        texto_caixa2 = texto_input2
                        # Limpe a entrada de texto
                        texto_input2 = ""
                    elif evento.key == pygame.K_BACKSPACE:
                        texto_input2 = texto_input2[:-1]
                    else:
                        texto_input2 += evento.unicode

        tela.blit(imagem_fundo, posicao_fundo)

        # Desenhe as caixas de entrada de texto
        pygame.draw.rect(tela, cor_input1, input_caixa1, 2)
        pygame.draw.rect(tela, cor_input2, input_caixa2, 2)

        # Renderize o texto inserido nas caixas de entrada
        texto_surface1 = fonte_input.render(texto_input1, True, (0, 0, 0))
        texto_surface2 = fonte_input.render(texto_input2, True, (0, 0, 0))

        # Centralize verticalmente o texto nas caixas de entrada
        text_rect1 = texto_surface1.get_rect()
        text_rect1.center = input_caixa1.center
        tela.blit(texto_surface1, text_rect1.topleft)

        text_rect2 = texto_surface2.get_rect()
        text_rect2.center = input_caixa2.center
        tela.blit(texto_surface2, text_rect2.topleft)

        # Desenhe o botão "Voltar"
        pygame.draw.rect(tela, cor_botao if not botao_voltar_clicado else cor_botao_clique, posicao_botao_voltar, 0, 100)
        tela.blit(texto_botao_voltar, (largura // 2 - texto_botao_voltar.get_width() // 2, 300 + altura_botao_voltar // 2 - texto_botao_voltar.get_height() // 2))
        if botao_voltar_clicado and posicao_botao_voltar.collidepoint(evento.pos):
                    print("Botão Sign In clicado!")
                    abrir_tela_inicial()  # Chame a função para abrir a tela de login
        pygame.display.flip()

    pygame.quit()

def tela_inicial():
    pygame.quit()
    pygame.init()
    largura = 500
    altura = 500

    imagem_fundo = pygame.image.load("Img/Img_painel.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
    posicao_fundo = imagem_fundo.get_rect()

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Tela Inicial")

    cor_fundo = (255, 0, 0)  # Vermelho

    executando_tela = True

    # Defina as cores dos botões
    cor_botao = (186, 186, 186)  # Verde
    cor_botao_clique = (111, 111, 111)  # Verde escuro (quando clicado)

    # Defina as dimensões e a posição do botão "Login"
    largura_botao = 200
    altura_botao = 25
    posicao_botao_login = pygame.Rect((250 - largura_botao // 2, 200, largura_botao, altura_botao))

    # Defina as dimensões e a posição do botão "Sign In"
    posicao_botao_signin = pygame.Rect((250 - largura_botao // 2, 250, largura_botao, altura_botao))

    # Texto dos botões
    fonte = pygame.font.Font(None, 36)
    texto_botao_login = fonte.render("Login", True, (0, 0, 0))  # Texto preto
    texto_botao_signin = fonte.render("Sign In", True, (0, 0, 0))  # Texto preto

    botao_login_clicado = False
    botao_signin_clicado = False

    while executando_tela:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando_tela = False
                break
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if posicao_botao_login.collidepoint(evento.pos):
                    botao_login_clicado = True
                elif posicao_botao_signin.collidepoint(evento.pos):
                    botao_signin_clicado = True
            elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                if botao_login_clicado and posicao_botao_login.collidepoint(evento.pos):
                    print("Botão Login clicado!")
                    tela_login()  # Chame a função para abrir a tela de login
                if botao_signin_clicado and posicao_botao_signin.collidepoint(evento.pos):
                    print("Botão Sign In clicado!")
                    tela_login()  # Chame a função para abrir a tela de login
                botao_login_clicado = False
                botao_signin_clicado = False

        tela.blit(imagem_fundo, posicao_fundo)

        pygame.draw.rect(tela, cor_botao if not botao_login_clicado else cor_botao_clique, posicao_botao_login, 0, 100)
        tela.blit(texto_botao_login, (largura // 2 - texto_botao_login.get_width() // 2, 200 + altura_botao // 2 - texto_botao_login.get_height() // 2))

        pygame.draw.rect(tela, cor_botao if not botao_signin_clicado else cor_botao_clique, posicao_botao_signin, 0, 100)
        tela.blit(texto_botao_signin, (largura // 2 - texto_botao_signin.get_width() // 2, 250 + altura_botao // 2 - texto_botao_signin.get_height() // 2))

        pygame.display.update()

    pygame.quit()

# Inicialize o Pygame
pygame.init()

# Chame a função para abrir a tela inicial
tela_inicial()