import json
import pygame
import getpass  # Importe a biblioteca getpass

# ...

def tela_login():
    pygame.quit()
    pygame.init()
    largura = 500
    altura = 500

    # ...

    executando_tela = True

    # ...

    while executando_tela:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando_tela = False
                break
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # ...
            if evento.type == pygame.KEYDOWN:
                if ativo_input1:
                    if evento.key == pygame.K_RETURN:
                        print("Texto da Caixa 1:", User)
                        texto_caixa1 = User
                        User = ""
                    elif evento.key == pygame.K_BACKSPACE:
                        User = User[:-1]
                    else:
                        User += evento.unicode
                elif ativo_input2:
                    if evento.key == pygame.K_RETURN:
                        # Use getpass para obter a senha de forma segura
                        Pass = getpass.getpass("Senha: ")
                        print("Senha digitada")
                        texto_caixa2 = Pass
                        Pass = ""
                    elif evento.key == pygame.K_BACKSPACE:
                        Pass = Pass[:-1]
                    else:
                        Pass += evento.unicode

        # ...
