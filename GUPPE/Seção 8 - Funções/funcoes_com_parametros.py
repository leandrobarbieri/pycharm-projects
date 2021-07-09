"""
Funções que recebem dados para serem processados dentro da função
- funções podem ter n parametros de entrada
- os parametros podem ser obrigatorios ou não
"""


def quadrado(num):
    # return num * num
    return num ** 2


for i in range(5):
    print(f"O quadrado de {i} é {quadrado(i)}")

# Esse tipo de função o parametro é obrigatório - TypeError
# quadrado()


def soma(n1, n2):
    return n1 + n2


def multiplica(valor1, valor2):
    return valor1 * valor2


def outra(a1, b2, c3):
    return (a1 + b2) * c3


# A ordem que os parametros são informados é a ordem dos argumentos recebidos na função
# Se passar um numero errado de parametros TypeError
print(soma(2, 2))
print(soma(5, 5))
print("-------------------")
print(multiplica(2, 2))
print(multiplica(5, 5))
print("-------------------")
print(outra(2, 2, 2))
print(outra(5, 5, 5))


# Nomeando parametros
def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {nome} {sobrenome}"


# Com argumentos nomeados a ordem não importa
print(nome_completo(nome="Leandro", sobrenome="Barbieri"))
print(nome_completo(sobrenome="Barbieri", nome="Leandro"))


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista_numeros = [1, 2, 3, 4, 5]
print(soma_impares(lista_numeros))


# Função com parametro padrão: a passagem de parametro é opcional

# Se não informar a potencia faz o calculo ao quadrado (Informar o valor no parametro faz dele opcional "potencia=2")
def exponencial_opcional(num, potencia=2):
    return num ** potencia


print("-------------------")
print(exponencial_opcional(2, 4))

print("-------------------")
print(exponencial_opcional(4))


# Os parametros com valores default devem estar no final da lista de parametros da função
# ERRO!
# def exponencial_opcional(potencia=2 , num):
#    return num ** potencia


def soma_opcional(num1=0, num2=0):
    return num1 + num2


print(soma_opcional(1, 1))


def mostra_informacao(nome="Leandro", instrutor=False):
    if nome == "Leandro" and instrutor:
        return f"Bem vindo {nome}"
    elif nome == "Leandro":
        return "Pensei que fosse instrutor"
    else:
        return f"Olá {nome}"


print(mostra_informacao("Leandro", True))
print(mostra_informacao("Leandro"))
print(mostra_informacao("Outro"))


# Escopo de função

# Variaveis globais
tipo_de_variavel = "Global"


def escopo_de_variaveis():
    # ignora a variavel global e usa a local
    tipo_de_variavel = "Local"
    return f"Tipo de variavel {tipo_de_variavel}"


print(escopo_de_variaveis())


# Forçar o uso da variavel global quando tiver o mesmo nome
# Variaveis globais
total = 0


def escopo_de_variaveis2():
    # utilizar uma variavel global
    global total
    total = total + 1
    return total


# Funções declaradas dentro de funções
def fora():
    contador = 0

    def dentro():
        # variavel que está na função de cima
        nonlocal contador
        contador = contador + 1
        return contador

    return dentro()


print(fora())


















