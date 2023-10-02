import sys
import pygame
import pygame_gui

pygame.init()

largura = 500
altura = 500

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Painel de Login')
gerenciador_ui = pygame_gui.UIManager((largura, altura))

imagem_fundo = pygame.image.load("Img/Img_painel.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
posicao_fundo = imagem_fundo.get_rect()

cor_botao = (211, 211, 211)
cor_botao_clique = (211, 211, 211)
cor_texto = (0, 0, 0)

largura_caixa_texto = 300
altura_caixa_texto = 18

# Variáveis para armazenar as entradas do usuário
entrada_nome = ""
entrada_user = ""
entrada_password = ""
entrada_confirme = ""

# Caixa de texto para o nome 
posicao_caixa_texto_nome = pygame.Rect((largura // 2 - largura_caixa_texto // 2, altura // 2 - 82, largura_caixa_texto, altura_caixa_texto))

# Caixa de texto para o usuário
posicao_caixa_texto_user = pygame.Rect((largura // 2 - largura_caixa_texto // 2, posicao_caixa_texto_nome.bottom + 10, largura_caixa_texto, altura_caixa_texto))

# Caixa de texto para a senha
posicao_caixa_texto_password = pygame.Rect((largura // 2 - largura_caixa_texto // 2, posicao_caixa_texto_user.bottom + 10, largura_caixa_texto, altura_caixa_texto))

# Caixa de texto para confirmar a senha 
posicao_caixa_texto_confirme = pygame.Rect((largura // 2 - largura_caixa_texto // 2, posicao_caixa_texto_password.bottom + 10, largura_caixa_texto, altura_caixa_texto))

# Verificando se algo foi inserido na caixa de texto
editando_caixa_texto_user = False
editando_caixa_texto_password = False
editando_caixa_texto_nome = False
editando_caixa_texto_confirme = False

# Defina as dimensões e a posição do botão "Cadastrar"
largura_botao = 100
altura_botao = 25
posicao_botao_cadastrar = pygame.Rect((largura // 2 - largura_botao // 2, posicao_caixa_texto_confirme.bottom + 20, largura_botao, altura_botao))

# Variável para controlar o estado do botão "Cadastrar"
botao_cadastrar_clicado = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        gerenciador_ui.process_events(evento)

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            
            if posicao_caixa_texto_user.collidepoint(evento.pos):
                editando_caixa_texto_user = True
                entrada_user = ""
            else:
                editando_caixa_texto_user = False

            if posicao_caixa_texto_password.collidepoint(evento.pos):
                editando_caixa_texto_password = True
                entrada_password = ""
            else:
                editando_caixa_texto_password = False

            if posicao_caixa_texto_nome.collidepoint(evento.pos):
                editando_caixa_texto_nome = True
                entrada_nome = ""
            else:
                editando_caixa_texto_nome = False

            if posicao_caixa_texto_confirme.collidepoint(evento.pos):
                editando_caixa_texto_confirme = True
                entrada_confirme = ""
            else:
                editando_caixa_texto_confirme = False

            if posicao_botao_cadastrar.collidepoint(evento.pos):
                botao_cadastrar_clicado = True
                print("Botão Cadastrar foi clicado")
            else:
                botao_cadastrar_clicado = False

        if evento.type == pygame.KEYDOWN:
            if editando_caixa_texto_user:
                if evento.key == pygame.K_BACKSPACE:
                    entrada_user = entrada_user[:-1]
                else:
                    entrada_user += evento.unicode

            if editando_caixa_texto_password:
                if evento.key == pygame.K_BACKSPACE:
                    entrada_password = entrada_password[:-1]
                else:
                    entrada_password += evento.unicode

            if editando_caixa_texto_nome:
                if evento.key == pygame.K_BACKSPACE:
                    entrada_nome = entrada_nome[:-1]
                else:
                    entrada_nome += evento.unicode

            if editando_caixa_texto_confirme:
                if evento.key == pygame.K_BACKSPACE:
                    entrada_confirme = entrada_confirme[:-1]
                else:
                    entrada_confirme += evento.unicode

    if not editando_caixa_texto_user and entrada_user == "":
        entrada_user = "User: "

    if not editando_caixa_texto_password and entrada_password == "":
        entrada_password = "Password: "

    if not editando_caixa_texto_nome and entrada_nome == "":
        entrada_nome = "Nome: "

    if not editando_caixa_texto_confirme and entrada_confirme == "":
        entrada_confirme = "Confirme: "

    tela.blit(imagem_fundo, posicao_fundo)

    pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_user, 0, 11)
    fonte = pygame.font.SysFont("comic-sans", 13, True, True)
    texto_surface_user = fonte.render(entrada_user, True, cor_texto)
    tela.blit(texto_surface_user, (posicao_caixa_texto_user.x+7, posicao_caixa_texto_user.y))

    pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_password, 0, 11)
    texto_surface_password = fonte.render(entrada_password, True, cor_texto)
    tela.blit(texto_surface_password, (posicao_caixa_texto_password.x+7, posicao_caixa_texto_password.y))

    pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_nome, 0, 11)
    texto_surface_nome = fonte.render(entrada_nome, True, cor_texto)
    tela.blit(texto_surface_nome, (posicao_caixa_texto_nome.x+7, posicao_caixa_texto_nome.y))

    pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_confirme, 0, 11)
    texto_surface_confirme = fonte.render(entrada_confirme, True, cor_texto)
    tela.blit(texto_surface_confirme, (posicao_caixa_texto_confirme.x+7, posicao_caixa_texto_confirme.y))

    pygame.draw.rect(tela, cor_botao if not botao_cadastrar_clicado else cor_botao_clique, posicao_botao_cadastrar, 0, 100)
    fonte_botao = pygame.font.Font(None, 22)
    texto_botao_cadastrar = fonte_botao.render("Cadastrar", True, (0, 0, 0))
    tela.blit(texto_botao_cadastrar, (posicao_botao_cadastrar.x+13, posicao_botao_cadastrar.y+7))

    gerenciador_ui.update(0.01)
    gerenciador_ui.draw_ui(tela)

    pygame.display.update()


# Armazenar os dados do usuário em uma variável
# Adicionar o botão de sair ao canto superior 
# Mudar o fundo