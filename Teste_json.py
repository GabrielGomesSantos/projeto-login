import json

# Abra o arquivo JSON
with open('cadastro.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Inicialize listas vazias para armazenar nomes de usuário e senhas
nomes_de_usuario = []
senhas = []

# Percorra os dados e extraia os nomes de usuário e senhas
for item in data['dados']:
    nomes_de_usuario.append(item['username'])
    senhas.append(item['password'])

# Agora, nomes_de_usuario e senhas contêm as informações desejadas
print("Nomes de Usuário:", nomes_de_usuario)
print("Senhas:", senhas)