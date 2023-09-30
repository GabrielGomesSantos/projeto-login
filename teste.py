import json

# Crie uma lista vazia para armazenar os dados do usuário
dados = []

# Solicite ao usuário que forneça os dados
for i in range(10):  # Você pode ajustar o número de entradas desejado
    username = input(f"Digite o username {i + 1}: ")
    password = input(f"Digite a senha {i + 1}: ")

    # Crie um dicionário com os dados fornecidos pelo usuário
    usuario = {
        "username": username,
        "pass": password
    }

    # Adicione o dicionário à lista de dados
    dados.append(usuario)

# Crie um dicionário com a chave "dados" e a lista de dados
dados_json = {"dados": dados}

# Especifique o nome do arquivo onde você deseja salvar os dados JSON
nome_arquivo = "cadastro.json"

# Escreva os dados JSON no arquivo
with open(nome_arquivo, "w") as arquivo_json:
    json.dump(dados_json, arquivo_json, indent=4)

print(f"Os dados foram salvos no arquivo {nome_arquivo}")
