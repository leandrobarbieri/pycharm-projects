"""
String com aspas triplas
Usar dentro das funções
"""


# função com docstrings
def hello_world():
    """Esta é a documentação da função hello world"""
    print("Oi")


# Exibir a documentação do metodo hello_word
print(help(hello_world))

# Usando a propriedade do da função como objeto para var a docstring
print(hello_world.__doc__)
print("---------------------------")


def exponencial(numero, potencia=2):
    """
    Função que faz o calculo exponencial de uma base por uma potencia
    :param numero: valor de base para o calculo da potencia
    :param potencia: a potencia utilizada. Valor padrão 2
    :return: numero elevado pela potencia
    """
    return numero ** potencia


print(exponencial.__doc__)


# os parametros obrigatorios no inicio, args (dinamicos) em segundo e por ultimo os param com valores default
def minha_funcao(a, *args, b=1):
    """
    :param a: primeiro parametro obrigatorio
    :param args: lista de parametros dinamicos
    :param b: parametro opcional
    :return: soma de todos
    """
    return a + sum(args) + b


print(minha_funcao(1, 2, 3, 4, b=2))
