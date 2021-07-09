"""
Lista de listas
Podem ser de qualquer tipo dentro da mesma lista, misturado
Arrays multidimensionais

ListedLists
"""

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)

# Acessar os dados
print(listas[0][0])
print(listas[0][1])
print(listas[0][2])

# loops em lista aninhadas
for i in listas:
    for j in i:
        print(j)

# usando listcomprehension
print([num for lista in listas for num in lista if num > 4])

