import json

#=-=-=-=-=-=-=-=Criando uma aba de tarefas=-=-=-=-=-=-
try:
    with open("json/tarefas.json", 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"usuarios": []}
    
user_id = user_id = len(data["usuarios"])+1 # Gere um novo ID
        
            


nova_tarefa = {"id": user_id,
    "nome": nome,
    "user": user,
    "tarefas":[
        {
            "id": 1,
            "titulo": "Nota exemplo",
            "descricao": "Umexlempo de uma nota que voce pode escrever", 
            "concluida": False
        }
    ]
}

data["usuarios"].append(nova_tarefa)


# Salve as alterações de volta no arquivo JSON
with open("json/tarefas.json", 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
