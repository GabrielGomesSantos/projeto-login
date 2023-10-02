import pygame
import sys

pygame.quit()
pygame.init()
largura = 500
altura = 500

imagem_fundo = pygame.image.load("Img/img_painel2.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
posicao_fundo = imagem_fundo.get_rect()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Login")

cor_fundo = (255, 0, 0)  # Vermelho

executando_tela = True

# Adicione duas entradas de texto
input_caixa1 = pygame.Rect(100, 165, 300, 25)  # Ajuste as coordenadas
input_caixa2 = pygame.Rect(100, 237, 300, 25)  # Ajuste as coordenadas
fonte_input = pygame.font.Font("arial.ttf", 17)


texto_input1 = ""

texto_input2 = ""
cor_input_ativo = pygame.Color(168, 168, 255)
cor_input_inativo = pygame.Color('white')
cor_input1 = cor_input_inativo
cor_input2 = cor_input_inativo
ativo_input1 = False
ativo_input2 = False

# Defina as cores dos botões
cor_botao = (154,111,79)  # vermelho
cor_botao_clique = (172,122,87)  # vermelho escuro (quando clicado)

# Defina as dimensões e a posição do botão "Voltar"
largura_botao_voltar = 150
altura_botao_voltar = 25
posicao_botao_voltar = pygame.Rect((250 - largura_botao_voltar // 2, 300, largura_botao_voltar, altura_botao_voltar))

# Texto do botão "Voltar"
fonte_botao_voltar = pygame.font.Font(None, 15)
texto_botao_voltar = fonte_botao_voltar.render("E N T R A R", True, (255, 255, 255))  # Texto preto

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
                    
                    #Limita o tamanho do texto à largura da caixa de entrada
                    if fonte_input.size(texto_input1 + evento.unicode)[0] <= 200 - 10:  # 300 é a largura da caixa, 10 é um espaço para margem
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
                    
                    if fonte_input.size(texto_input2 + evento.unicode)[0] <= 300 - 10:  # 300 é a largura da caixa, 10 é um espaço para margem
                        texto_input2 += evento.unicode

    tela.blit(imagem_fundo, posicao_fundo)

    # Desenhe as caixas de entrada de texto
    pygame.draw.rect(tela, (255, 255, 255), input_caixa1, 0, 100)#fundo da caixa 1
    pygame.draw.rect(tela, cor_input1, input_caixa1,2, 100)
    pygame.draw.rect(tela, (255, 255, 255), input_caixa2, 0, 100)# fundo da caixa 2
    pygame.draw.rect(tela, cor_input2, input_caixa2,2, 100)
    
    texto_mascarado = "*" * len(texto_input2) #senha em "*"


    # Renderize o texto inserido nas caixas de entrada
    texto_surface1 = fonte_input.render(texto_input1, True, (47, 47, 51))
    texto_surface2 = fonte_input.render(texto_mascarado, True, (47, 47, 51))

    # Centralize verticalmente o texto nas caixas de entrada
    text_rect1 = texto_surface1.get_rect()
    text_rect1.topleft = input_caixa1.center
    tela.blit(texto_surface1, (105, 167))


    
    



    text_rect2 = texto_surface2.get_rect()
    text_rect2.center = input_caixa2.center
    tela.blit(texto_surface2, (105, 239))
      
    # Desenhe o botão "Voltar"
    pygame.draw.rect(tela, cor_botao if not botao_voltar_clicado else cor_botao_clique, posicao_botao_voltar, 0, 100)
    tela.blit(texto_botao_voltar, (largura // 2 - texto_botao_voltar.get_width() // 2, 300 + altura_botao_voltar // 2 - texto_botao_voltar.get_height() // 2))
    
    if botao_voltar_clicado and posicao_botao_voltar.collidepoint(evento.pos):
                print("Botão Sign In clicado!")
                abrir_tela_inicial()  # Chame a função para abrir a tela de login
    pygame.display.flip()

pygame.quit()