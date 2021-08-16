"""
List comprehension: Uma das features mais poderasas de python!
Permite gerar listas a partir de outro iteravel aplicando uma expressão e iterando em cada item
Sintaxe: [ <expressao> for <dado> in <interavel> ] retorna um list
"""

numeros = [1, 2, 3, 4, 5]
nova_lista1 = [num * 10 for num in numeros]
nova_lista2 = [num / 10 for num in numeros]

print(nova_lista1)
print(nova_lista2)


def exponencial(base, potencia=2):
    return base ** potencia


# Aplicando uma expressão em cada valor
nova_lista3 = [exponencial(valor, potencia=3) for valor in numeros]
print(nova_lista3)

# List comprehension vs Looping
# Fazendo a mesma coisa de cima mas com looping
nova_lista3_1 = []
for valor in numeros:
    nova_lista3_1.append(exponencial(valor, potencia=3))
print(nova_lista3_1)

# Outro exemplo
numeros2 = [1, 2, 3, 4, 5]
numeros_dobrados = []
for num in numeros2:
    numeros_dobrados.append(num * 2)
print(numeros_dobrados)

# Com list comprehension
nova_lista4 = [valor * 2 for valor in numeros2]
print(nova_lista4)

nome = "Leandro Barbieri"
print([letra.upper() for letra in nome])

# Primeira letra em maiúsculo
nova_lista5 = ["leandro", "bruna", "breno"]
print([pessoa.replace(pessoa[0], pessoa[0].upper()) for pessoa in nova_lista5])

# Imprimir de 0 a 90
print([num * 10 for num in range(10)])

# Estruturas condicionais logicas
# Faz um filtro na condição if e só retorna se verdadeiro
numeros_pares = [num for num in range(100) if num % 2 == 0]
numeros_impares = [num for num in range(100) if num % 2 != 0]
print(f"Impares: {len(numeros_impares)}, Pares: {len(numeros_pares)}")

# Neste caso não faz filtro, retorna tudo mas avalia caso a caso e aplica uma condição
# Dobra de valor apenas os numeros pares e divide os numeros ímpares
print([num * 2 if num % 2 == 0 else num / 2 for num in range(10)])

# List comprehension em listas aninhadas (listas de listas)
# Matriz de 3 x 3
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas[2][1])

# Iterando em uma lista aninhada
nova_lista6 = []
for lista in listas:
    for i in lista:
        nova_lista6.append(i)
print(nova_lista6)

# Usando list comprehension dupla com dois for
print([i for lista in listas for i in lista])