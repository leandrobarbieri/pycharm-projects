"""
Max - retorna o maior valor de um iteravel, ou o maior de 2 ou mais elementos
Min - inverso do max
"""

# Maior de um iteravel
lista_max = [10, 9, 8, 50, 100, 80]
print(max(lista_max))
print(min(lista_max))

# Maior entre os parametros passados diretamente (variaveis ou valores)
print(max(10, 20, 5, 100, 50))
print(min(10, 20, 5, 100, 50))

# Maior entre os parametros
print(max("Alex", "Paula", "Carlos"))
print(min("Alex", "Paula", "Carlos"))

# Lista de musicas
lista_musicas = [
    {"Titulo": "Musica1", "tocou": 15},
    {"Titulo": "Musica2", "tocou": 1},
    {"Titulo": "Musica3", "tocou": 60},
    {"Titulo": "Musica4", "tocou": 40}
]

# Listar a mais tocada
print(max(lista_musicas, key=lambda x: x["tocou"]))

# Listar a menos tocada
print(min(lista_musicas, key=lambda x: x["tocou"]))

# lista de dicts com tweets por usuários
usuarios = [
    {"username": "leandro", "tweets": ["Eu gosto de bolo", "Eu gosto de pizza"]},
    {"username": "bruna", "tweets": ["Eu gosto de pao", "Eu gosto de amendoin"]},
    {"username": "breno", "tweets": []},
    {"username": "samuel", "tweets": ["Muitos tweets", "Muitos tweets", "Muitos tweets", "Muitos tweets"]},
    {"username": "Alice", "tweets": []},
    {"username": "Min", "tweets": []},
]

# Usuário com mais tweets
print(max(usuarios, key=lambda x: len(x["tweets"])))

# Usuário com menos tweets
print(min(usuarios, key=lambda x: len(x["tweets"])))

# Maior e menor de dicts
dict_max_min = {"a": 10, "b": 20, "c": 1}

# Usando items, retorna com base na chave a tupla chave/valor inteira
print(max(dict_max_min.items()))
print(min(dict_max_min.items()))

# Usando somente o nome do dict, retorna com base na chave
print(max(dict_max_min))
print(min(dict_max_min))

# Usando values, retorna com base no valor
print(max(dict_max_min.values()))
print(min(dict_max_min.values()))
