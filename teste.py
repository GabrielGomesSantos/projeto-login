import json

try:
    with open('json/tarefas.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"usuarios": []}


# Suponhamos que você deseja adicionar uma tarefa para o usuário com ID 1
user_id = 1

# Crie uma nova tarefa
nova_tarefa = {
    "id": len(data["usuarios"][user_id - 1]["tarefas"]) + 1,  # Gere um novo ID
    "titulo": "Nova Tarefa",
    "descricao": "Esta é uma nova tarefa",
    "concluida": False
}
# Adicione a nova tarefa à lista de tarefas do usuário
data["usuarios"][user_id - 1]["tarefas"].append(nova_tarefa)


# Salve as alterações de volta no arquivo JSON
with open('json/tarefas1.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(data)