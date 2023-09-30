import json 
    
    #=-=-=PARTE DE CADASTRO=-=-=
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
    with open('Arquivos.json/cadastro.json', 'r', encoding='utf-8') as usuario:
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

def verificar_login():  
    
    # Variaveis 
    flaguser = True
    usuario = False
    senha = False
    user = verificar_Usuario()
    pas = verificar_senha()
    user_digitado = input("Digite o nome de usuario:")
    pass_digitado = input("Digite sua senha: ")
    
    #Verificacao de usuario
    
    for item in user:
        
        if item == user_digitado:
            usuario = True
            pos = user.index(item) #pegar posicao do vetor apartir do valor dele
            break
        
        else:
            usuario = False 
            
    #verificacao da senha 
    
    if pas[pos] == pass_digitado:
        senha = True
        
    else:
        senha = False   
    
    if usuario and senha:
        print(f"Bem Vindo {item}!!!")     
    else:
        print("Usuario ou senha invalidos!!")

cadastro()
verificar_login()