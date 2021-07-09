"""
Conjuntos em Python são chamados de Sets
Listas com valores únicos (teoria dos conjuntos da matemática)
Não garante ordenação mas garante valores únicos
É como se fosse um dicionário apenas com as Keys (keys precisam ser únicas)
Elementos não são acessados via índice - não são indexados
São bons para utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação

São referenciados com {}
"""

# Definindo um conjunto
s1 = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9})
print(type(s1))
print(s1)

# Converter uma string para um set
lista1 = list("leandro")
s2 = set(lista1)
# A lista não está ordenada
print(s2)

# Checar se um elemento está na lista
if "X" in s2:
    print("Está na lista")
else:
    print("Não está na lista")

# Tipos de dados misturados em Sets
s3 = {1, "a", True, 1.9, (1, 2)}
for i in s3:
    print(type(i))

# Iterando um um set
for valor in s3:
    print(f"Valor set: {valor}")

# Lista de visitantes em um museu
cidades = []
while True:
    cidade = (input("Informe a cidade"))
    if cidade == "sair":
        break
    elif cidade == "s":
        break
    cidades.append(cidade)

# lista de cidade únicas
print(f"Pessoas: {len(cidades)}, Cidades : {len(set(cidades))}, Lista: {set(cidades)}")

# Acicionando elementos (conjuntos são mutáveis)
s = {"A", "B", "C"}
s.add("D")
s.add("D") # duplicidade não gera erro
print(s)

# Remover elementos

# Se o valor não for encontrado gera erro
s.remove("D")
print(s)

# Não gera erro se não houver o valor
s.discard("D")
print(s)

# Copiando um conjunto para outro. Deep
conjunto = {"X", "Y"}
s = conjunto.copy()
s.add("W")
print(s)
print(conjunto)

# Shallow
s = conjunto
s.add("#")
print(s)
print(conjunto)

# remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos matemáticos de conjunto
estudantes_python = {"leandro", "ana", "joao"}
estudantes_dax = {"leandro", "maria", "pedro"}

# union: Alguns alunos que estão em um conjunto estão no outro
# unicos = estudantes_python.union(estudantes_dax)
unicos = estudantes_dax.union(estudantes_python)
print(unicos)

# fazendo union utiliando pipe |
unicos2 = estudantes_python | estudantes_dax
print(unicos2)

# Intersection: estudantes que estudam em ambos conjuntos
ambos = estudantes_dax.intersection(estudantes_python)
print(ambos)
ambos2 = estudantes_python & estudantes_dax
print(ambos2)

# Except: estão em um conjunto mas não estão no outro
exclusivo = estudantes_dax.difference(estudantes_python)
print(exclusivo)

# Soma
conj = {1, 2, 3, 4, 5, 6}
print(f"Max: {max(conj)}, Min: {min(conj)}, Sum: {sum(conj)}, Qtd:{len(conj)}")










