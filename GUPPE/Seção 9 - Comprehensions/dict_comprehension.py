"""
Muito parecido com listcomprehension
Muda a sintax de [] para {} e permite obter nas expressões tanto a chave quanto o valor

Lista = [1, 2, 3]
Tupla = (1, 2, 3) ou 1, 2, 3
Set = {1, 2, 3}
Dict = {"a":1, "b":2, "c": 3}

"""
dict1 = {"a": 1, "b": 2, "c": 3}

nova = {print(f"Chave: {chave}, Valor: {valor}") for chave, valor in dict1.items()}
print(nova)

# podemos tanto alterar a chave (upper) quanto o valor ** 2 na parte das expressões
quadrado = {chave.upper(): valor ** 2 for chave, valor in dict1.items()}
print(quadrado)

# mistrurar duas listas e transformar em um dict
chaves = "abcde"
valores = [1, 2, 3, 4, 5]
dict2 = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(dict2)

# condicional






