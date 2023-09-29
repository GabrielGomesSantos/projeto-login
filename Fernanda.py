import pygame
import sys
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
cor_botao_clique = (75, 0, 130)
cor_texto = (0, 0, 0)

# Caixa de Texto para o usuário
largura_caixa_texto = 300
altura_caixa_texto = 30
posicao_caixa_texto_user = pygame.Rect((largura // 2 - largura_caixa_texto // 2, altura // 2 - 50, largura_caixa_texto, altura_caixa_texto))
texto_caixa_texto_user = "User: "

# Caixa de Texto para a senha
posicao_caixa_texto_password = pygame.Rect((largura // 2 - largura_caixa_texto // 2, posicao_caixa_texto_user.bottom + 10, largura_caixa_texto, altura_caixa_texto))
texto_caixa_texto_password = "Password: "

editando_caixa_texto_user = False
editando_caixa_texto_password = False

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            
            if posicao_caixa_texto_user.collidepoint(evento.pos):
                editando_caixa_texto_user = True
                texto_caixa_texto_user = ""
            else:
                editando_caixa_texto_user = False

            if posicao_caixa_texto_password.collidepoint(evento.pos):
                editando_caixa_texto_password = True
                texto_caixa_texto_password = ""
            else:
                editando_caixa_texto_password = False

        elif evento.type == pygame.KEYDOWN:
            if editando_caixa_texto_user:
                if evento.key == pygame.K_RETURN:
                    editando_caixa_texto_user = False
                elif evento.key == pygame.K_BACKSPACE:
                    texto_caixa_texto_user = texto_caixa_texto_user[:-1]
                else:
                    texto_caixa_texto_user += evento.unicode

            if editando_caixa_texto_password:
                if evento.key == pygame.K_RETURN:
                    editando_caixa_texto_password = False
                elif evento.key == pygame.K_BACKSPACE:
                    texto_caixa_texto_password = texto_caixa_texto_password[:-1]
                else:
                    texto_caixa_texto_password += evento.unicode

    if not editando_caixa_texto_user and texto_caixa_texto_user == "":
        texto_caixa_texto_user = "User: "

    if not editando_caixa_texto_password and texto_caixa_texto_password == "":
        texto_caixa_texto_password = "Password: "

    tela.blit(imagem_fundo, posicao_fundo)

    pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_user, 0, 11)
    fonte = pygame.font.SysFont("comic-sans", 15, True, True)
    texto_surface_user = fonte.render(texto_caixa_texto_user, True, cor_texto)
    tela.blit(texto_surface_user, (posicao_caixa_texto_user.x + 5, posicao_caixa_texto_user.y + 5))

    pygame.draw.rect(tela, cor_botao, posicao_caixa_texto_password, 0, 11)
    texto_surface_password = fonte.render(texto_caixa_texto_password, True, cor_texto)
    tela.blit(texto_surface_password, (posicao_caixa_texto_password.x + 5, posicao_caixa_texto_password.y + 5))

    gerenciador_ui.update(0.01)
    gerenciador_ui.draw_ui(tela)

    pygame.display.update()