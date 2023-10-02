import pygame
import sys

# Inicializa o pygame
pygame.init()

# Configuração da tela
altura = 500
largura = 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Login")  # Defina um título para a janela

# Carrega a imagem de fundo e a dimensiona para a tela
imagem_fundo = pygame.image.load("Img/Img_painel.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
posicao_fundo = imagem_fundo.get_rect()

# Configuração do botão LOGIN
cor_botao = (233, 53, 136)  # Cinza
cor_botao_clique = (181, 42, 106)  # Cinza escuro
largura_botao = 150
altura_botao = 25
posicao_botao = pygame.Rect((160 - largura_botao // 2, 310 - altura_botao // 2, largura_botao, altura_botao))

#Botao registrar
cor_botao_clique_r = (181, 42, 106)
posicao_botao_registrar = pygame.Rect((343 - largura_botao // 2, 310 - altura_botao // 2, largura_botao, altura_botao))

#Entrys
fonte_entry = pygame.font.Font(None, 25)
texto_digitado= ""
largura_entry = 300
altura_entry = 25
posicao_entry_login = pygame.Rect((500 // 2 - largura_entry // 2, 180 - altura_entry // 2, largura_entry, altura_entry))
texto_entry_senha = ""
posicao_entry_senha = pygame.Rect((500 // 2 - largura_entry // 2, 250 - altura_entry // 2, largura_entry, altura_entry))



#texto entry
fonte_textos = pygame.font.Font(None, 27)
texto_login = fonte_textos.render("EMAIL", True, (255, 255, 255))

#texto login entry
texto_senha = fonte_textos.render("SENHA", True, (255, 255, 255))



# Configuração da fonte do botão LOGIN
fonte = pygame.font.Font(None, 15)
texto_botao = fonte.render("L O G I N", True, (255, 255, 255)) 
texto_botao_registrar = fonte.render("R E G I S T R A R", True, (255, 255, 255))



# Variável para controlar o estado do botão
botao_clicado = False
botao_clicado_registrar = False

# Loop principal do aplicativo
loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Texto digitado:", texto_digitado)
                texto_digitado = ""
                texto_entry_senha = ""
            elif event.key == pygame.K_BACKSPACE:
                texto_digitado = texto_digitado[:-1]
                texto_entry_senha = texto_entry_senha[:-1]
            else:
                # Limita o tamanho do texto à largura da caixa de entrada
                if fonte_entry.size(texto_digitado + event.unicode)[0] <= 300 - 10:  # 300 é a largura da caixa, 10 é um espaço para margem
                    texto_digitado += event.unicode
                if fonte_entry.size(texto_entry_senha + event.unicode)[0] <= 300 - 10:  # 300 é a largura da caixa, 10 é um espaço para margem
                    texto_entry_senha += event.unicode
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if posicao_botao.collidepoint(event.pos):
                botao_clicado = True
            elif posicao_botao_registrar.collidepoint(event.pos):
                botao_clicado_registrar = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if botao_clicado and posicao_botao.collidepoint(event.pos):
                print("Botão Clique-me clicado!")
                print("Texto digitado:", texto_digitado)
                texto_digitado = ""
            botao_clicado = False
            if botao_clicado_registrar and posicao_botao_registrar.collidepoint(event.pos):
                    print(texto_digitado)
                    texto_digitado = ""
            botao_clicado_registrar = False
       
        
    
    # Desenha a imagem de fundo
    tela.blit(imagem_fundo, posicao_fundo)

    

    # Desenha a caixa de entrada
    pygame.draw.rect(tela, (255, 255, 255, 11),posicao_entry_login, 0, 100)
    pygame.draw.rect(tela, (255, 255, 255), posicao_entry_senha, 0, 100)
    
    #Renderiza o texto digitado
    text_surface = fonte_entry.render(texto_digitado, True, (0, 0, 0))
    tela.blit(text_surface, (104, 171))
    text_surface_senha = fonte_entry.render(texto_entry_senha, True, (0, 0, 0))
    tela.blit(text_surface_senha, (104, 242))
    

    #Texto login
    tela.blit(texto_login, (250  - texto_login.get_width() // 2, 155 - texto_login.get_height() // 2))
    tela.blit(texto_senha, (250 - texto_senha.get_width() // 2, 220 - texto_senha.get_height () // 2))


    # Desenha o botao na tela
    pygame.draw.rect(tela, cor_botao if not botao_clicado else cor_botao_clique, posicao_botao, 0, 100)
    tela.blit(texto_botao, (160 - texto_botao.get_width() // 2, 310 - texto_botao.get_height() // 2))


    #Desenha o botao registrar
    pygame.draw.rect(tela, cor_botao if not botao_clicado_registrar else cor_botao_clique, posicao_botao_registrar, 0, 100)
    tela.blit(texto_botao_registrar, (343 - texto_botao_registrar.get_width() // 2, 310 - texto_botao_registrar.get_height() // 2))


    pygame.display.update()
