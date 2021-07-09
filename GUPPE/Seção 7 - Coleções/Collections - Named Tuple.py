"""
Named Tuple: são tuplas onde especificamos nomes e parametros
É como se estivessemos criando um tipo de dado customizado
"""
# tupla padrão
tupla1 = ("A", "B", "C")
print(tupla1[1])

# declarando os parametros da named tuple
from collections import namedtuple
# Forma 1
cachorro = namedtuple("cachorro", "idade raca nome")
# Forma 2
cachorro = namedtuple("cachorro", "idade, raca, nome")
# Forma 3
cachorro = namedtuple("cachorro", ["idade", "raca", "nome"])
#print(cachorro)

# criando a named tuple usando a declaração acima
canil = []
canil.append(cachorro(idade=2, raca="ViraLata", nome="SharlokDog"))
canil.append(cachorro(idade=3, raca="ViraLata", nome="Bingo"))

# Desempacotando
for idade, raca, nome in canil:
    print(f"Idade: {idade}, Raça: {raca}, Nome: {nome}")

# Acesando pelo indice
for cao in canil:
    print(f"Cão: {cao[2]}\n"
          f"Idade: {cao[0]}, Raça: {cao[1]}")

# Acessando pela nome da variavel da tupla
for cao in canil:
    print(f"Cão: {cao.nome}\n"
          f"Idade: {cao.idade}, Raça: {cao.raca}")
