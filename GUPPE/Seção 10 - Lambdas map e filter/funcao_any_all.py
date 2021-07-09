"""
all(): retorna True se todos os elementos do iteravel são True ou se está vazio. Se algum elemento for false retorna False
any(): Retorna True se algum elemento for True. Se o iteravel estiver vazio retorna False
"""

# False
print(all([0, 1, 1, 0]))

# True
print(all([1, 1, 1, 1]))

# False
print(all([False, True, True]))

# True
print(all([True, True, True]))

# True
print(all(["Oi", "Tudo", "Bem"]))

# Todos os nomes começam com a letra C
lista_nomes = ["Carlos", "Camila", "Carol"]
print(all([nome[0] == "C" for nome in lista_nomes]))

# Pelo menos um é verdadeiro
print(any([False, False, False]))
print(any([False, False, True]))








