"""
Não existe Tuple Comprehencions, elas se chamam Generators
Generator ocupa menos recursos em memória
Não gera a lista em memória (gera um obj), só gera a lista quando for executada
"""

# retorna a quantidade de bytes do elemento passado como parametro
from sys import getsizeof

nomes = ["Carlos", "Camila", "Cassio"]

# Listcomprehension
print(any([nome[0] == "x" for nome in nomes]))

# Generators: ao usar parenteses o python cria um generator, ao invés de retorna uma lista
gen = (nome[0] == "C" for nome in nomes)
# <class 'generator'>
print(type(gen))
print(gen)

# Para usar o conteúdo de um generator precisamos iterar sob ele
print("-------Iterando em um generator")
[print(x) for x in gen]
print("-------Fim generator")

# usando colchetes
list_comprehencions = [nome[0] == "C" for nome in nomes]
print(f"List: {getsizeof(list_comprehencions)}")
print(f"Generator: {getsizeof(gen)}")


# <class 'list'>
print(type(list_comprehencions))

# Generator: Removi os colchetes e continua funcionando porque agora funciona como um generator
print(any(nome[0] == "C" for nome in nomes))





