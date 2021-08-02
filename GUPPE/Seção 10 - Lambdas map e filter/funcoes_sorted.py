"""
Essa função sorted podemos usar em qualquer iteravel
Não confundir com a função sort que existe em listas
"""

# sorted de lista exclusivo para listas
lista1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# antes de printar tem que imprimir, não funciona ordenar e imprimir ao mesmo tempo,
# ordena internamente, mas não retorna
lista1.sort()
print(lista1)

# existe sorted para os outros objetos iteraveis
tupla1 = (9, 8, 7, 6, 5, 4, 3, 2, 1)

# sorted retorna um novo iteravel ordenado, mas não orderna ele internamente. Mantém a lista original intacta
print(sorted(tupla1))
print(tupla1)

# Alterando a forma de ordenação, reverse, ordena e depois reverte
print(sorted(tupla1, reverse=True))

# Sempre retorna uma lista, se precisar basta converter
print(f"Isso é uma list {sorted(tupla1)}")
print(f"Isso é uma tuple {tuple(sorted(tupla1))}")


# lista de dicts
usuarios = [
    {"username": "leandro", "tweets": ["Eu gosto de bolo", "Eu gosto de pizza"]},
    {"username": "bruna", "tweets": ["Eu gosto de pao", "Eu gosto de amendoin"]},
    {"username": "breno", "tweets": []},
    {"username": "samuel", "tweets": ["Muitos tweets", "Muitos tweets", "Muitos tweets", "Muitos tweets"]},
    {"username": "Alice", "tweets": []},
    {"username": "Min", "tweets": []},
]

# Não consegue iterar neste dicionário, com dicionário temos que informar o key
# Para cada usuário no dict aplica a lambda para acessar uma chave que será usada na ordenação

# Min vem primeiro porque len retona o nome com menor numero de caracteres
print(sorted(usuarios, key=lambda x: len(x["username"])))

# Alice vem primeiro, porque está em ordem alfabetica
print(sorted(usuarios, key=lambda x: x["username"]))

# Samuel vem primeiro, porque a quantidade de tweets na lista é maior
print(sorted(usuarios, key=lambda x: len(x["tweets"]), reverse=True))

# Lista de musicas
lista_musicas = [
    {"Titulo": "Musica1", "tocou": 15},
    {"Titulo": "Musica2", "tocou": 1},
    {"Titulo": "Musica3", "tocou": 60},
    {"Titulo": "Musica4", "tocou": 40}
]

# Listar as mais tocadas
print(sorted(lista_musicas, key=lambda x: x["tocou"], reverse=True))







