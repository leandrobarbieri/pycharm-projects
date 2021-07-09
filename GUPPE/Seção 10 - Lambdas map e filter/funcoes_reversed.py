"""
Não confundir com a função reverse de listas
Inverte o iteravel
"""

lista1 = [1, 2, 3, 4, 5]
reversed_list = reversed(lista1)

# Não imprime, pois retorna um obj chamado list_reversed iterator
# Precisamos converter para qualque interável
print(tuple(reversed_list))

# depis que usa é apagado. Não retona valores
print(set(reversed_list))
print(list(reversed_list))

# Precisa executar o reversed sempre que for usar
print(set(reversed(lista1)))
print(list(reversed(lista1)))

# Iterar sob um reversed
for letra in reversed("Leandro"):
    print(letra, end=" ")

# Join transfora uma lista de strings em uma string novamente.
print(" ".join(list(reversed("Leandro"))))

# loop for reverso: contagem regressiva
for n in reversed(range(0, 10)):
    print(n)

# loop for reverso: contagem regressiva
for n in range(9, -1, -1):
        print(n)