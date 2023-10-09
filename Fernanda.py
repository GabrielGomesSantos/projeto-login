import pygame
import sys
import pygame_gui
def cadastro():
    pygame.init()

    largura = 500
    altura = 500

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Painel de Login')
    gerenciador_ui = pygame_gui.UIManager((largura, altura))

    imagem_fundo = pygame.image.load("Img/Img_painel_black.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
    posicao_fundo = imagem_fundo.get_rect()

    cor_botao = (154,111,79)
    cor_botao_clique = (172,122,87)
    cor_texto = (47, 47, 51)

    largura_caixa_texto = 350
    altura_caixa_texto = 30

    # Variáveis para armazenar as entradas do usuário
    entrada_nome = "Nome:"
    entrada_user = "User:"
    entrada_password = "Password:"
    entrada_confirme = "Confirme:"

    # Limites de caracteres
    limite_caracteres = 16  
    limite_caracteres_senha= 20

    # Caixa de texto para o nome 
    posicao_caixa_texto_nome = pygame.Rect((largura // 2 - largura_caixa_texto // 2, altura // 2 - 152, largura_caixa_texto, altura_caixa_texto))

    # Caixa de texto para o usuário
    posicao_caixa_texto_user = pygame.Rect((largura // 2 - largura_caixa_texto // 2, posicao_caixa_texto_nome.bottom + 10, largura_caixa_texto, altura_caixa_texto))

    # Caixa de texto para a senha
    posicao_caixa_texto_password = pygame.Rect((largura // 2 - largura_caixa_texto // 2, posicao_caixa_texto_user.bottom + 10, largura_caixa_texto, altura_caixa_texto))

    # Caixa de texto para confirmar a senha 
    posicao_caixa_texto_confirme = pygame.Rect((largura // 2 - largura_caixa_texto // 2, posicao_caixa_texto_password.bottom + 10, largura_caixa_texto, altura_caixa_texto))

    # Verificando se algo foi inserido na caixa de texto
    editando_caixa_texto_nome = False
    editando_caixa_texto_user = False
    editando_caixa_texto_password = False
    editando_caixa_texto_confirme = False

    # Variável para controlar a visibilidade da senha
    senha_oculta = True

    # Variável para controlar a visibilidade da confirmação da senha
    confirme_oculto = True

    # Defina as dimensões e a posição do botão "Cadastrar"
    largura_botao = 200
    altura_botao = 25
    posicao_botao_cadastrar = pygame.Rect((largura // 2 - largura_botao // 2, posicao_caixa_texto_confirme.bottom + 50, largura_botao, altura_botao))

    # Defina as dimensões e a posição do botão "Voltar"
    posicao_botao_voltar = pygame.Rect((largura // 2 - largura_botao // 2, posicao_botao_cadastrar.bottom + 20, largura_botao, altura_botao))

    # Defina as dimensões e a posição do botão de visibilidade da senha
    botao_visibilidade_senha = pygame.Rect(363, 298, 30, 25)

    # Defina as dimensões e a posição do botão de visibilidade da confirmação da senha
    botao_visibilidade_confirme = pygame.Rect((posicao_caixa_texto_confirme.right + 10, posicao_caixa_texto_confirme.y, 30, altura_caixa_texto))

    # Variável para controlar o estado do botão "Cadastrar"
    botao_cadastrar_clicado = False

    # Variável para controlar o estado do botão "Voltar"
    botao_voltar_clicado = False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            gerenciador_ui.process_events(evento)

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

                if posicao_caixa_texto_nome.collidepoint(evento.pos):
                    editando_caixa_texto_nome = True
                    if entrada_nome == "Nome:":
                        entrada_nome = ""
                else:
                    editando_caixa_texto_nome = False

                if posicao_caixa_texto_user.collidepoint(evento.pos):
                    editando_caixa_texto_user = True
                    if entrada_user == "User:":
                        entrada_user = ""
                else:
                    editando_caixa_texto_user = False

                if posicao_caixa_texto_password.collidepoint(evento.pos):
                    editando_caixa_texto_password = True
                    if entrada_password == "Password:":
                        entrada_password = ""
                else:
                    editando_caixa_texto_password = False

                if posicao_caixa_texto_confirme.collidepoint(evento.pos):
                    editando_caixa_texto_confirme = True
                    if entrada_confirme == "Confirme:":
                        entrada_confirme = ""
                else:
                    editando_caixa_texto_confirme = False
                
                # Verificando se algo foi digitado 
                if not entrada_nome and not editando_caixa_texto_nome:
                    entrada_nome = "Nome:"

                if entrada_user == "" and editando_caixa_texto_user == False: 
                    entrada_user = "User:"
                
                if entrada_password == "" and editando_caixa_texto_password == False:
                    entrada_password = "Password:"

                if entrada_confirme == "" and editando_caixa_texto_confirme == False:
                    entrada_confirme = "Confirme:"
                    
                # Verificando se o botão "Cadastrar" foi clicado
                if posicao_botao_cadastrar.collidepoint(evento.pos):
                    botao_cadastrar_clicado = True

                    # Salvando o conteúdo em variáveis quando o botão de cadastro é clicado 
                    nome = entrada_nome
                    user = entrada_user
                    password = entrada_password
                    confirme = entrada_confirme
                    if (password == confirme and entrada_nome != "Nome:" and entrada_user != "User:"):
                        cadastro(nome, user, password)
                        print(nome)
                        print(user)
                        print(password)
                        print(confirme)
                        # Teste lógico para cadastrar 
                    else:
                        # Teste lógico para NÃO cadastrar 
                        print("Verifique a confirmação! ")
                else:
                    botao_cadastrar_clicado = False

                # Verificando se o botão "Voltar" foi clicado
                if posicao_botao_voltar.collidepoint(evento.pos):
                    botao_voltar_clicado = True
                    tela_inicial()
                    print("Voltar")
                else:
                    botao_voltar_clicado = False

                # Verificando se o botão de visibilidade da senha foi clicado
                if botao_visibilidade_senha.collidepoint(evento.pos):
                    senha_oculta = not senha_oculta

                # Verificando se o botão de visibilidade da confirmação da senha foi clicado
                if botao_visibilidade_confirme.collidepoint(evento.pos):
                    confirme_oculto = not confirme_oculto

            if evento.type == pygame.KEYDOWN:

                if editando_caixa_texto_nome:
                    if evento.key == pygame.K_BACKSPACE:
                        entrada_nome = entrada_nome[:-1]
                    elif len(entrada_nome) < limite_caracteres:
                        entrada_nome += evento.unicode
                
                if editando_caixa_texto_user:
                    if evento.key == pygame.K_BACKSPACE:
                        entrada_user = entrada_user[:-1]
                    elif len(entrada_user) < limite_caracteres:
                        entrada_user += evento.unicode

                if editando_caixa_texto_password:
                    if evento.key == pygame.K_BACKSPACE:
                        entrada_password = entrada_password[:-1]
                    elif len(entrada_password) < limite_caracteres_senha:
                        entrada_password += evento.unicode 

                if editando_caixa_texto_confirme:
                    if evento.key == pygame.K_BACKSPACE:
                        entrada_confirme = entrada_confirme[:-1]
                    elif len(entrada_confirme) < limite_caracteres_senha:
                        entrada_confirme += evento.unicode

        tela.blit(imagem_fundo, posicao_fundo)

        fonte = pygame.font.SysFont(None, 25)
        pygame.draw.rect(tela, (255, 255, 255), posicao_caixa_texto_user, 0, 11)
        texto_surface_user = fonte.render(entrada_user, True, cor_texto)
        tela.blit(texto_surface_user, (posicao_caixa_texto_user.x+10, posicao_caixa_texto_user.y+8))

        pygame.draw.rect(tela, (255, 255, 255), posicao_caixa_texto_nome, 0, 11)
        texto_surface_nome = fonte.render(entrada_nome, True, cor_texto)
        tela.blit(texto_surface_nome, (posicao_caixa_texto_nome.x+10, posicao_caixa_texto_nome.y+8))

        pygame.draw.rect(tela, (255, 255, 255), posicao_caixa_texto_password, 0, 11)


        # Senha oculta 
        if senha_oculta:
            confirme_renderizado = "•" * len(entrada_confirme)
            senha_renderizada = "•" * len(entrada_password)
            imagem_mostrar_senha = pygame.image.load("Img/senha_off.png") #Carrega a imagem para mostrar senha
            imagem_mostrar_senha = pygame.transform.scale(imagem_mostrar_senha, (23, 25)) #Escala o tamnho da imagem para o tamanho do botao
            
        elif senha_oculta== False:
            senha_renderizada = entrada_password
            imagem_mostrar_senha = pygame.image.load("Img/senha_on.png") #carrega a imagem para nao mostrar senha
        
            confirme_renderizado = entrada_confirme
            imagem_mostrar_senha = pygame.transform.scale(imagem_mostrar_senha, (23, 25)) #escalona a imagem

        if entrada_password == "Password:":
            senha_renderizada = "Password:"

        if entrada_confirme == "Confirme:":
            confirme_renderizado = "Confirme:"
            
        texto_surface_password = fonte.render(senha_renderizada, True, cor_texto)
        tela.blit(texto_surface_password, (posicao_caixa_texto_password.x+10, posicao_caixa_texto_password.y+8))
        
        
        pygame.draw.rect(tela, (255, 255, 255), posicao_caixa_texto_confirme, 0, 11)
        
        # Confirmação oculta 
        texto_surface_confirme = fonte.render(confirme_renderizado, True, cor_texto)
        tela.blit(texto_surface_confirme, (posicao_caixa_texto_confirme.x+10, posicao_caixa_texto_confirme.y+8))

        pygame.draw.rect(tela, cor_botao if not botao_cadastrar_clicado else cor_botao_clique, posicao_botao_cadastrar, 0, 100)
        fonte_botao = pygame.font.Font(None, 15)
        texto_botao_cadastrar = fonte_botao.render("C A D A S T R A R", True, (255, 255, 255))
        tela.blit(texto_botao_cadastrar, (posicao_botao_cadastrar.x+60, posicao_botao_cadastrar.y+7))

        pygame.draw.rect(tela, cor_botao if not botao_voltar_clicado else cor_botao_clique, posicao_botao_voltar, 0, 100)
        fonte_botao = pygame.font.Font(None, 15)
        texto_botao_voltar = fonte_botao.render("V O L T A R", True, (255, 255, 255))
        tela.blit(texto_botao_voltar, (posicao_botao_cadastrar.x+74, posicao_botao_voltar.y+7))

        # Desenhe o botão de visibilidade da senha
        pygame.draw.rect(tela, cor_botao, botao_visibilidade_senha, 0, 11)
        texto_visibilidade_senha = fonte_botao.render("", True, cor_texto) if senha_oculta else fonte_botao.render("", True, cor_texto)
        tela.blit(texto_visibilidade_senha, (botao_visibilidade_senha.x+8, botao_visibilidade_senha.y+8))
        tela.blit(imagem_mostrar_senha, (367, 299))
        # Desenhe o botão de visibilidade da confirmação da senha


        gerenciador_ui.update(0.01)
        gerenciador_ui.draw_ui(tela)

        pygame.display.update()


