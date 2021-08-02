"""Cria um iteravel que agrega os elementos de cada um dos iteraveis passados
   faz um pareamento do primeiro elemento de uma lista com o primeiro da outra e assim sucessivamente
   pega um elemento de cada e forma tuplas
"""

lista1 = [1, 4, 7]
lista2 = [2, 5, 8]
lista3 = [3, 6, 9]

lista_final = list(zip(lista1, lista2, lista3))

# pega um elemento de cada e forma tuplas - [(1, 4), (2, 5), (3, 6)]
print(lista_final)

# o ZIP para de fazer o pareamento quando alcança o tamanho do menor iteravel

lista1 = [1, 4, 7]
lista2 = [2, 5, 8]
lista3 = [3, 6]

# a lista tem apenas 2 elementos, logo o zip vai parear apenas os 2 primeiros elementos das 3 tuplas
# [(1, 2, 3), (4, 5, 6)] - ignora 7 e 8

lista_final = list(zip(lista1, lista2, lista3))

print(lista_final)

# Utilizando um zip
prova1 = [9.8, 7.5, 6.9]
prova2 = [8.0, 7.3, 9.9]
alunos = ["Leandro", "Bruna", "Breno"]

# Pareando as notas com os alunos e selecionando a maior para formar um dict com o nome e a nota
nota_final = {nota[0]: max(nota[1], nota[2]) for nota in zip(alunos, prova1, prova2)}

# Lista de alunos com suas maiores notas
for i in nota_final.items():
    print(f"Nome: {i[0]} | Nota: {i[1]}")




