import json 


#banco de dados das Notas!! 

#Carrega o nosso documento tarefas.json e salvo seus dados em uma variavels usuarios.
def carregar_json():
    with open('json/tarefas.json', 'r', encoding='utf-8') as usuario:
        dados = json.load(usuario)
        usuarios = dados['usuarios']
        
    return(usuarios)

#Verifica as tarefas do usuario 
def tarefas(): 
    nome_digitado = "Izaque"
    dados = carregar_json()

    for item in dados:
        if item['nome'] == nome_digitado:
            tarefas = (item['tarefas'])
            
            break
    return(tarefas)   

def dividir_tarefas():  
    tas = []
    for item in tarefas():     
        print(f"---------------------------\nTitulo: {item['titulo']}\n\nDescrição: {item['descricao']}")    
        tas.append(item['descricao'])   
    return(tas)
