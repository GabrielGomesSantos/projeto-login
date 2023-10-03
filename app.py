import pygame
import sys
import json 
import pygame_gui
    
# =-=-=-=-=-=-=-=-=-=-=-=-PARTE DE CADASTRO =-=-=-=-=-=-=-=-=-=-=-=-
def cadastro():
    # Variáveis
    dados2 = []
    cadastro_user = input("User:")
    user = verificar_Usuario() 
    cadastroflag = True
    
    for item in user:
        if item == cadastro_user:
            cadastroflag = False
            break
        
    if cadastroflag:
        cadastro_password = input("Password:")
    
        novo_usuario = {
            "username": cadastro_user,
            "pass": cadastro_password
        }
        dados1 = carregar_json()

        dados1["dados"].append(novo_usuario)
        
        dados_json = {"dados": dados1["dados"]}
            
        with open('Arquivos.json/cadastro.json', 'w') as cadastro:
            json.dump(dados_json, cadastro, indent=4)
            
        print(f"Usuário {cadastro_user} cadastrado com sucesso!!")
    else:
        print("Usuário já cadastrado")

    #=-=-=PARTE DE VERIFICACAO DE LOGIN=-=-=

def carregar_json():
    with open('json/cadastro.json', 'r', encoding='utf-8') as usuario:
        dados = json.load(usuario)

    return(dados)

def verificar_Usuario():
    
    dados = carregar_json()
    nomes_de_usuario = []
    
    for item in dados['dados']:
        nomes_de_usuario.append(item['username'])
    return(nomes_de_usuario)

def verificar_senha():
    
    dados = carregar_json()
    senhas = []
    
    for item in dados['dados']:
        senhas.append(item['pass'])
    return(senhas)

def verificar_login(User, Pass ):  
    
    # Variaveis 
    flaguser = True
    usuario = False
    senha = False
    user = verificar_Usuario()
    pas = verificar_senha()
    user_digitado = User
    pass_digitado = Pass
    
    #Verificacao de usuario
    
    for item in user:
        
        if item == user_digitado:
            usuario = True
            pos = user.index(item) #pegar posicao do vetor apartir do valor dele
            break
        
        else:
            usuario = False 
            
    #verificacao da senha 
    if usuario:
        if pas[pos] == pass_digitado:
            senha = True
        
        else:
            senha = False   
    
    if usuario and senha:
        print(f"Bem Vindo {item}!!!")
        tela_main()
          
    else:
        print("Usuario ou senha invalidos!!")
        tela_login()
        
# =-=-=-=-=-=-=-=-=-=-=-=-INTERFACE =-=-=-=-=-=-=-=-=-=-=-=-

def abrir_tela_e_fechar():
    pygame.quit()  # Fecha a tela atual
    tela_inicial()  # Abre a tela inicial

def fechar():
    pygame.quit()

def desenhar_botao(tela, texto, cor, retangulo, cor_clique, clicado):
    pygame.draw.rect(tela, cor if not clicado else cor_clique, retangulo, 0, 55)
    tela.blit(texto, (retangulo.centerx - texto.get_width() // 2, retangulo.centery - texto.get_height() // 2))

def tela_main():
    pygame.quit()
    pygame.init()
    largura = 1920
    altura = 1080

    imagem_fundo = pygame.image.load("Img/mainbg.png")
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

def tela_inicial():
    pygame.quit()
    pygame.init()
    largura = 500
    altura = 500

    imagem_fundo = pygame.image.load("Img/Img_painel_black.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
    posicao_fundo = imagem_fundo.get_rect()

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Tela Inicial")

    cor_fundo = (255, 0, 0)  # Vermelho

    executando_tela = True

    # Defina as cores dos botões
    cor_botao = (154,111,79)  # Verde
    cor_botao_clique = (172,122,87)  # Verde escuro (quando clicado)

    # Defina as dimensões e a posição do botão "Login"
    largura_botao = 200
    altura_botao = 25
    posicao_botao_login = pygame.Rect((250 - largura_botao // 2, 200, largura_botao, altura_botao))

    # Defina as dimensões e a posição do botão "Sign In"
    posicao_botao_signin = pygame.Rect((250 - largura_botao // 2, 250, largura_botao, altura_botao))

    # Texto dos botões
    fonte = pygame.font.Font(None, 15)
    texto_botao_login = fonte.render("L O G I N", True, (255, 255, 255))  # Texto preto
    texto_botao_signin = fonte.render("R E G I S T R A R - S E", True, (255, 255, 255))  # Texto preto

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
                    tela_cadastro()  # Chame a função para abrir a tela de login
                botao_login_clicado = False
                botao_signin_clicado = False

        tela.blit(imagem_fundo, posicao_fundo)

        pygame.draw.rect(tela, cor_botao if not botao_login_clicado else cor_botao_clique, posicao_botao_login, 0, 100)
        tela.blit(texto_botao_login, (largura // 2 - texto_botao_login.get_width() // 2, 200 + altura_botao // 2 - texto_botao_login.get_height() // 2))

        pygame.draw.rect(tela, cor_botao if not botao_signin_clicado else cor_botao_clique, posicao_botao_signin, 0, 100)
        tela.blit(texto_botao_signin, (largura // 2 - texto_botao_signin.get_width() // 2, 250 + altura_botao // 2 - texto_botao_signin.get_height() // 2))

        pygame.display.update()

    pygame.quit()

def tela_login():
    usuario = True
    senha = True

    pygame.quit()
    pygame.init()
    largura = 500
    altura = 500

    imagem_fundo = pygame.image.load("Img/img_painel_black.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
    posicao_fundo = imagem_fundo.get_rect()

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Login")

    cor_fundo = (255, 0, 0)  # Vermelho

    executando_tela = True

    # Adicione duas entradas de texto
    input_caixa1 = pygame.Rect(100, 165, 300, 25)  # Ajuste as coordenadas
    input_caixa2 = pygame.Rect(100, 237, 300, 25)  # Ajuste as coordenadas
    fonte_input = pygame.font.Font("Fonts/arial.TTF", 17)
    fonte_senha = pygame.font.Font("Fonts/arial.TTF", 25)
    User = ""
    Pass = ""
    mostrar_senha= pygame.Rect(350, 300, 30, 25)
    cor_input_ativo = pygame.Color(168, 168, 255)
    cor_input_inativo = pygame.Color('white')
    cor_input1 = cor_input_inativo
    cor_input2 = cor_input_inativo
    ativo_input1 = False
    ativo_input2 = False
    maximo_senha = 20
    maximo_user = 16
    
    mostrar_senha_ativo = False

    # Defina as cores dos botões
    cor_botao = (154,111,79)  # vermelho
    cor_botao_clique = (172,122,87)  # vermelho escuro (quando clicado)

    # Defina as dimensões e a posição do botão "Voltar"
    largura_botao_entrar = 200
    altura_botao_entrar = 25
    posicao_botao_entrar = pygame.Rect((250 - largura_botao_entrar // 2, 300, largura_botao_entrar, altura_botao_entrar))

    # Texto do botão "Voltar"
    fonte_botao_entrar = pygame.font.Font(None, 15)
    texto_botao_entrar = fonte_botao_entrar.render("E N T R A R", True, (255, 255, 255))  # Texto branco


    mostrar_senha= pygame.Rect(360, 300, 30, 25)

    #Variavel que regula a quantidade de caracteres


    botao_entrar_clicado = False

    while executando_tela:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando_tela = False
                break
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if mostrar_senha.collidepoint(evento.pos):
                    
                    mostrar_senha_ativo = not mostrar_senha_ativo

                elif input_caixa1.collidepoint(evento.pos):
                    ativo_input1 = not ativo_input1
                    ativo_input2 = False
                elif input_caixa2.collidepoint(evento.pos):
                    ativo_input2 = not ativo_input2
                    ativo_input1 = False
                elif posicao_botao_entrar.collidepoint(evento.pos):
                    botao_entrar_clicado = True
                else:
                    ativo_input1 = False
                    ativo_input2 = False
                cor_input1 = cor_input_ativo if ativo_input1 else cor_input_inativo
                cor_input2 = cor_input_ativo if ativo_input2 else cor_input_inativo
            if evento.type == pygame.KEYDOWN:
                if ativo_input1:
                    if evento.key == pygame.K_RETURN:
                        print("Texto da Caixa 1:", User)
                        ativo_input2 = not ativo_input2
                        ativo_input1 = False
                        cor_input1 =  pygame.Color('lightskyblue3')
                        cor_input2 =  pygame.Color('dodgerblue2')
                        # Limpe a entrada de texto
                    elif evento.key == pygame.K_BACKSPACE:
                        User = User[:-1]
                    elif len(User) < maximo_user:
                        User += evento.unicode
                    
                elif ativo_input2:
                    if evento.key == pygame.K_RETURN:
                        print("Texto da Caixa 2:", Pass)
                        texto_caixa1 = User
                        texto_caixa2 = Pass
                        verificar_login(User, Pass)
                        Pass = ""
                        User = ""

                    elif evento.key == pygame.K_BACKSPACE:
                        Pass = Pass[:-1]
                    elif len(Pass) < maximo_senha:
                        Pass += evento.unicode
                    

        tela.blit(imagem_fundo, posicao_fundo)

        # Desenhe as caixas de entrada de texto
        pygame.draw.rect(tela, (255, 255, 255), input_caixa1, 0, 100)#fundo da caixa 1
        pygame.draw.rect(tela, cor_input1, input_caixa1,2, 100)
        pygame.draw.rect(tela, (255, 255, 255), input_caixa2, 0, 100)# fundo da caixa 2
        pygame.draw.rect(tela, cor_input2, input_caixa2,2, 100)
        pygame.draw.rect(tela, cor_botao if not mostrar_senha_ativo else cor_botao_clique, mostrar_senha, 0, 100)

        #Faz a senha ficar em mascara "*"
        if not mostrar_senha_ativo:
            texto_mascarado = "*" * len(Pass)
            texto_surface2 = fonte_senha.render(texto_mascarado, True, (47, 47, 51))
            

        # Renderize o texto inserido nas caixas de entrada
        texto_surface1 = fonte_input.render(User, True, (47, 47, 51))
        if mostrar_senha_ativo:
            texto_surface2 = fonte_input.render(Pass, True, (47, 47, 51))

        # Centralize verticalmente o texto nas caixas de entrada
        text_rect1 = texto_surface1.get_rect()
        text_rect1.topleft = input_caixa1.center
        tela.blit(texto_surface1, (105, 167))

        text_rect2 = texto_surface2.get_rect()
        text_rect2.topleft = input_caixa2.center
        tela.blit(texto_surface2, (105, 239))

        # Desenhe o botão "Voltar"
        pygame.draw.rect(tela, cor_botao if not botao_entrar_clicado else cor_botao_clique, posicao_botao_entrar, 0, 100)
        tela.blit(texto_botao_entrar, (largura // 2 - texto_botao_entrar.get_width() // 2, 300 + altura_botao_entrar // 2 - texto_botao_entrar.get_height() // 2))
        if botao_entrar_clicado and posicao_botao_entrar.collidepoint(evento.pos):
            while botao_entrar_clicado and posicao_botao_entrar.collidepoint(evento.pos):
                    print("Botão entrar clicado!")
                    botao_entrar_clicado= False
                    verificar_login(User, Pass)
                # Chame a função para abrir a tela de login
        pygame.display.flip()

    pygame.quit()

def tela_cadastro():
    
    pygame.init()

    largura = 500
    altura = 500

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Painel de Login')
    gerenciador_ui = pygame_gui.UIManager((largura, altura))

    imagem_fundo = pygame.image.load("Img/Img_painel_black.png")
    imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
    posicao_fundo = imagem_fundo.get_rect()

    cor_botao = (255, 255, 255)
    cor_botao_clique = (255, 255, 255)
    cor_texto = (0, 0, 0)

    largura_caixa_texto = 350
    altura_caixa_texto = 30

    # Variáveis para armazenar as entradas do usuário
    entrada_nome = "Nome: "
    entrada_user = "User: "
    entrada_password = "Password: "
    entrada_confirme = "Confirme: "

    # Limites de caracteres
    limite_caracteres = 25

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
    largura_botao = 150
    altura_botao = 40
    posicao_botao_cadastrar = pygame.Rect((largura // 2 - largura_botao // 2, posicao_caixa_texto_confirme.bottom + 50, largura_botao, altura_botao))

    # Defina as dimensões e a posição do botão "Voltar"
    posicao_botao_voltar = pygame.Rect((largura // 2 - largura_botao // 2, posicao_botao_cadastrar.bottom + 20, largura_botao, altura_botao))

    # Defina as dimensões e a posição do botão de visibilidade da senha
    botao_visibilidade_senha = pygame.Rect((posicao_caixa_texto_password.right + 10, posicao_caixa_texto_password.y, 30, altura_caixa_texto))

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
                    if entrada_nome == "Nome: ":
                        entrada_nome = ""
                else:
                    editando_caixa_texto_nome = False

                if posicao_caixa_texto_user.collidepoint(evento.pos):
                    editando_caixa_texto_user = True
                    if entrada_user == "User: ":
                        entrada_user = ""
                else:
                    editando_caixa_texto_user = False

                if posicao_caixa_texto_password.collidepoint(evento.pos):
                    editando_caixa_texto_password = True
                    if entrada_password == "Password: ":
                        entrada_password = ""
                else:
                    editando_caixa_texto_password = False

                if posicao_caixa_texto_confirme.collidepoint(evento.pos):
                    editando_caixa_texto_confirme = True
                    if entrada_confirme == "Confirme: ":
                        entrada_confirme = ""
                else:
                    editando_caixa_texto_confirme = False
                
                # Verificando se algo foi digitado 
                if not entrada_nome and not editando_caixa_texto_nome:
                    entrada_nome = "Nome: "

                if entrada_user == "" and editando_caixa_texto_user == False: 
                    entrada_user = "User: "
                
                if entrada_password == "" and editando_caixa_texto_password == False:
                    entrada_password = "Password: "

                if entrada_confirme == "" and editando_caixa_texto_confirme == False:
                    entrada_confirme = "Confirme: "
                    
                # Verificando se o botão "Cadastrar" foi clicado
                if posicao_botao_cadastrar.collidepoint(evento.pos):
                    botao_cadastrar_clicado = True

                    # Salvando o conteúdo em variáveis quando o botão de cadastro é clicado 
                    nome = entrada_nome
                    user = entrada_user
                    password = entrada_password
                    confirme = entrada_confirme
                    if (password == confirme):
                        cadastro(nome, user, password, confirme)
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
                    elif len(entrada_password) < limite_caracteres:
                        entrada_password += evento.unicode

                if editando_caixa_texto_confirme:
                    if evento.key == pygame.K_BACKSPACE:
                        entrada_confirme = entrada_confirme[:-1]
                    elif len(entrada_confirme) < limite_caracteres:
                        entrada_confirme += evento.unicode

        tela.blit(imagem_fundo, posicao_fundo)

        fonte = pygame.font.SysFont(None, 27)
        pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_user, 0, 11)
        texto_surface_user = fonte.render(entrada_user, True, cor_texto)
        tela.blit(texto_surface_user, (posicao_caixa_texto_user.x+10, posicao_caixa_texto_user.y+8))

        pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_nome, 0, 11)
        texto_surface_nome = fonte.render(entrada_nome, True, cor_texto)
        tela.blit(texto_surface_nome, (posicao_caixa_texto_nome.x+10, posicao_caixa_texto_nome.y+8))

        pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_password, 0, 11)
        
        # Senha oculta 
        if senha_oculta:
            senha_renderizada = "*" * len(entrada_password)
        else:
            senha_renderizada = entrada_password
        
        texto_surface_password = fonte.render(senha_renderizada, True, cor_texto)
        tela.blit(texto_surface_password, (posicao_caixa_texto_password.x+10, posicao_caixa_texto_password.y+8))

        pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_confirme, 0, 11)
        
        # Confirmação oculta 
        if confirme_oculto:
            confirme_renderizado = "*" * len(entrada_confirme)
        else:
            confirme_renderizado = entrada_confirme
        
        texto_surface_confirme = fonte.render(confirme_renderizado, True, cor_texto)
        tela.blit(texto_surface_confirme, (posicao_caixa_texto_confirme.x+10, posicao_caixa_texto_confirme.y+8))

        pygame.draw.rect(tela, cor_botao if not botao_cadastrar_clicado else cor_botao_clique, posicao_botao_cadastrar, 0, 100)
        fonte_botao = pygame.font.Font(None, 30)
        texto_botao_cadastrar = fonte_botao.render("Cadastrar", True, (0, 0, 0))
        tela.blit(texto_botao_cadastrar, (posicao_botao_cadastrar.x+25, posicao_botao_cadastrar.y+10))

        pygame.draw.rect(tela, cor_botao if not botao_voltar_clicado else cor_botao_clique, posicao_botao_voltar, 0, 100)
        fonte_botao = pygame.font.Font(None, 30)
        texto_botao_voltar = fonte_botao.render("Voltar", True, (0, 0, 0))
        tela.blit(texto_botao_voltar, (posicao_botao_voltar.x+45, posicao_botao_voltar.y+10))

        # Desenhe o botão de visibilidade da senha
        pygame.draw.rect(tela, cor_botao, botao_visibilidade_senha, 0, 11)
        texto_visibilidade_senha = fonte_botao.render("", True, cor_texto) if senha_oculta else fonte_botao.render("", True, cor_texto)
        tela.blit(texto_visibilidade_senha, (botao_visibilidade_senha.x+8, botao_visibilidade_senha.y+8))

        # Desenhe o botão de visibilidade da confirmação da senha
        pygame.draw.rect(tela, cor_botao, botao_visibilidade_confirme, 0, 11)
        texto_visibilidade_confirme = fonte_botao.render("", True, cor_texto) if confirme_oculto else fonte_botao.render("", True, cor_texto)
        tela.blit(texto_visibilidade_confirme, (botao_visibilidade_confirme.x+8, botao_visibilidade_confirme.y+8))

        gerenciador_ui.update(0.01)
        gerenciador_ui.draw_ui(tela)

        pygame.display.update()
# Inicialize o Pygame
pygame.init()

# Chame a função para abrir a tela inicial
tela_inicial()