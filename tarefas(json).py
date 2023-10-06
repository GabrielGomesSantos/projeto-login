import json 
from time import sleep
import os
#banco de dados das Notask!! 

def carregar_Tarefas_json():#Carrega o nosso documento json/tarefas.json e salvo seus dados em uma variavels usuarios.
    with open('json/json/tarefas.json', 'r', encoding='utf-8') as usuario:
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

def pesquisar_tarefa():
    tarefas_list = verificar_tarefas()

    write_title = input("Qual o título da sua nota:")
    
    for tarefa in tarefas_list:
        if tarefa['titulo'] == write_title:
            sleep(0.5)
            print(f"Tarefa encontrada")
            print(f"---------------------------\nTitulo: {tarefa['titulo']}\n\nDescrição: {tarefa['descricao']}")
            found = True  # Marque como encontrada
            break

    if not found:
        print("Não foi possível encontrar a tarefa com esse nome")
  
def criar_tarefa(): #Criar uma tarefa nova
    
    try:
        with open('json/tarefas.json', 'r') as file:
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
    with open('json/tarefas.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

        
criar_tarefa()

