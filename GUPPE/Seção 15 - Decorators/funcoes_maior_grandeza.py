"""
Funções de maior grandeza: Higher Order Funcions

Funções que retorna outras funções ou usam funções como parametros/argumentos ou criar variaveis do tipo de funções

"""


# definido funções
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Passar o nome da função sem aspas como parametro e sem os parenteses
print(calcular(1, 1, diminuir))
print(calcular(1, 1, somar))


"""Nested/inner functions"""
# Funções dentro de funções

from random import choice

def cumprimento(pessoa):
    def humor():
        # aleatoriamento seleciona uma opção da tupla
        return choice(("E ai", "Como vai", "so se for pra vc", "Legal pessoal", "Olha só quem está aqui"))

    return humor() + " " + pessoa


print(cumprimento("leandro"))
print(cumprimento("bruna"))
print(cumprimento("breno"))



print("---------------")


# retornando a função sem executar
def cumprimento2(pessoa):
    def humor():
        # aleatoriamento seleciona uma opção da tupla
        hm = choice(("E ai", "Como vai", "so se for pra vc", "Legal pessoal", "Olha só quem está aqui"))
        return f"{hm} {pessoa}"

    # retorna a função
    return humor


# primeiro pega a função e cria um obj com ela para depois conseguir executar
x = cumprimento2("Leandro")
print(x())




















