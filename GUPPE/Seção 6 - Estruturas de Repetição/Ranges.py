"""
Gera uma lista, sequencias numericas de forma específicadas
Conhecer for para usar range e para trabalhar com for

range(valor de parada) --não inclusive

incio Zero incremento de 1 em 1
"""

# forma 1 - incio Zero incremento de 1 em 1 (não inclusive)
for num in range(11):
    print(num)
print("------------")

# forma 2: com início 4 e valor de parada 10, incremento 1
for num in range(4, 10):
    print(num)
print("------------")

# forma 3: range(valor de inicio 1, valor de parada 9, passo 2)
for num in range(1, 10, 2):
    print(num)
print("------------")

# forma 4: igual a 3 mais INVERSO, REGRESSIVO
# range(valor inicio, valor de parada, passo)
for num in range(10, 0, -1):
    print(num)
print("------------")

# para gerar uma lista com range precisa transformar o range em lista. Não gera diretamente
lista = list(range(10))
for num in lista:
    print(num)

print(lista)





