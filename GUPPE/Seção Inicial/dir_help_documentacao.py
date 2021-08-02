"""
Utilitarios para auxiliar na programação.

dir = Mostra todos os atributos funções e metodos para determinado tipo de dado ou variável
dir("leandro")
['__add__', '__class__', '__contains__'.....
"leandro".title()
'Leandro'

help = Documentação, como utilizar os atributos/propriedades e metodos disponíveis
help("Leandro".upper)

"""
numero = 1
lista = [1, 2]

# lista os atributos e metodos do obj
print("dir()----------------------------------------")
print(dir(numero))

print("dir()----------------------------------------")
print(dir(lista))

# exibe a documentação do help do obj
print("help()----------------------------------------")
lista = list(range(10))
print(help(lista))

