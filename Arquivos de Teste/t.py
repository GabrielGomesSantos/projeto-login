import pygame
import sys
import json 
from time import sleep
import os
def cadastro(nome, user, password):
    # Variáveis
    dados2 = []
    cadastro_user = user
    users = verificar_Usuario() 
    cadastroflag = True
    
    for item in users:
        if item == cadastro_user:
            cadastroflag = False
            break
        
    if cadastroflag:
        cadastro_password = password
    
        novo_usuario = {
            "username": cadastro_user,
            "pass": cadastro_password
        }
        dados1 = carregar_json()

        dados1["dados"].append(novo_usuario)
        
        dados_json = {"dados": dados1["dados"]}
            
        with open('json/cadastro.json', 'w') as cadastro:
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
        

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=JSON=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


#banco de dados das Notask!! 

def carregar_Tarefas_json():#Carrega o nosso documento "json/tarefas.json" e salvo seus dados em uma variavels usuarios.
    with open("json/tarefas.json", 'r', encoding='utf-8') as usuario:
        dados = json.load(usuario)
        usuarios = dados['usuarios']
        
    return(usuarios)

def verificar_tarefas(): #Verifica as tarefas do usuario 
    nome_digitado = "Izaque"
    dados = carregar_Tarefas_json()

    for item in dados:
        if item['nome'] == nome_digitado:
            tarefas = (item['tarefas'])
            
            break
    return(tarefas)   

def dividir_verificar_tarefas():
    task = []
    titles = []
    for item in verificar_tarefas():     
        #print(f"---------------------------\nTitulo: {item['titulo']}\n\nDescrição: {item['descricao']}")    
        task.append(item['descricao'])
        titles.append(item['titulo'])
    return(task, titles)

def mostrar_verificar_tarefas():
    for item in verificar_tarefas():     
        print(f"---------------------------\nTitulo: {item['titulo']}\n\nDescrição: {item['descricao']}")   

def pesquisar_tarefa(busca):
    found = False
    tarefas_list = verificar_tarefas()

    write_title = busca
    
    for tarefa in tarefas_list:
        if tarefa['titulo'] == write_title:
            sleep(0.5)
            print(f"\nTarefa encontrada")
            print(f"---------------------------\nTitulo: {tarefa['titulo']}\n\nDescrição: {tarefa['descricao']}")
            found = True  # Marque como encontrada
            break

    if not found:
        print("Não foi possível encontrar a tarefa com esse nome")
  
def criar_tarefa(): #Criar uma tarefa nova
    
    try:
        with open('"json/tarefas.json"', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"usuarios": []}

    new_title = input("Digite o titulo:")
    new_txt = input("Digite sua nota:")

    # Suponhamos que você deseja adicionar uma tarefa para o usuário com ID 1
    user_id = 1

    # Crie uma nova tarefa
    nova_tarefa = {
        "id": len(data["usuarios"][user_id - 1]["tarefas"]) + 1,  # Gere um novo ID
        "titulo": new_title,
        "descricao": new_txt,
        "concluida": False
    }
    # Adicione a nova tarefa à lista de tarefas do usuário
    data["usuarios"][user_id - 1]["tarefas"].append(nova_tarefa)


    # Salve as alterações de volta no arquivo JSON
    with open('"json/tarefas.json"', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    

    
pygame.init()
largura = 1300
altura = 1000
imagem_fundo = pygame.image.load("Img/mainbg.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))
posicao_fundo = imagem_fundo.get_rect()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tela Inicial")
cor_fundo = (255, 0, 0)  # Vermelho
executando_tela = True

# Defina as cores dos botões
cor_botao = (186, 186, 186)  # Verde
cor_botao_clique = (111, 111, 111)  # Verde escuro (quando clicado)

# Defina as dimensões e a posição do botão "+"
largura_botao_add = 150
altura_botao_add = 150
posicao_botao_add = pygame.Rect((250 - largura_botao_add // 0.642, 364, largura_botao_add, altura_botao_add))

# Modifique a posição e o tamanho do botão "Sair"
largura_botao_sair = 40  # Tornando o botão um pouco menor
altura_botao_sair = 40  # Tornando o botão um pouco menor
posicao_botao_sair = pygame.Rect(largura - largura_botao_sair - 10, 10, largura_botao_sair, altura_botao_sair)

# Barra de pesquisa
largura_barra_pesquisa = 400
altura_barra_pesquisa = 30
posicao_barra_pesquisa = pygame.Rect((largura // 2 - largura_barra_pesquisa // 2, 50, largura_barra_pesquisa, altura_barra_pesquisa))
fonte_barra_pesquisa = pygame.font.Font(None, 36)
busca = ""  # Variável para armazenar o texto da pesquisa

fonte1 = pygame.font.Font(None, 200)
fonte = pygame.font.Font(None, 36)
texto_botao_add = fonte1.render("+", True, (0, 0, 0))  # Texto preto
texto_botao_sair = fonte.render("X", True, (255, 255, 255))  # Texto branco

botao_add_clicado = False
botao_sair_clicado = False
barra_pesquisa_ativa = False

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
            elif posicao_barra_pesquisa.collidepoint(evento.pos):
                barra_pesquisa_ativa = True
            else:
                barra_pesquisa_ativa = False
        elif evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            if botao_add_clicado and posicao_botao_add.collidepoint(evento.pos):
                print("Botão + clicado!")
            if botao_sair_clicado and posicao_botao_sair.collidepoint(evento.pos):
                print("Botão Sair clicado!")
                pygame.quit()
            botao_add_clicado = False
            botao_sair_clicado = False
        elif evento.type == pygame.KEYDOWN:
            if barra_pesquisa_ativa:
                if evento.key == pygame.K_RETURN and busca != "":  # Quando Enter é pressionado na barra de pesquisa
                    print(f"Texto da pesquisa: {busca}")
                    pesquisar_tarefa(busca)
                elif evento.key == pygame.K_BACKSPACE:  # Backspace para apagar um caractere
                    busca = busca[:-1]
                else:
                    busca += evento.unicode

    tela.blit(imagem_fundo, posicao_fundo)

    # Desenhe os elementos
    pygame.draw.rect(tela, (255, 255, 255), posicao_barra_pesquisa, 2)  # Caixa de pesquisa
    texto_barra_pesquisa = fonte_barra_pesquisa.render(busca, True, (0, 0, 0))
    tela.blit(texto_barra_pesquisa, (posicao_barra_pesquisa.x + 5, posicao_barra_pesquisa.y + 5))

    pygame.draw.rect(tela, (255, 255, 255), posicao_botao_add, 0, 55)  # Botão "+"
    tela.blit(texto_botao_add, (posicao_botao_add.centerx - texto_botao_add.get_width() // 2, posicao_botao_add.centery - texto_botao_add.get_height() // 2))

    pygame.draw.rect(tela, (255, 0, 0), posicao_botao_sair, 0, 55)  # Botão "Sair"
    tela.blit(texto_botao_sair, (posicao_botao_sair.centerx - texto_botao_sair.get_width() // 2, posicao_botao_sair.centery - texto_botao_sair.get_height() // 2))

    pygame.display.update()

pygame.quit()