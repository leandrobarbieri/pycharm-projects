"""
Usa a palavra return
- Finaliza a função sai da execução
- Pode ter diferentes returns em escopos diferentes
- O codigo tem que conseguir chegar a pelo menos um return
- Pode retornar qualquer tipo de dado
"""

numeros = [1, 2, 3]

# Com retorno
retorno = numeros.pop()
print(f"A função pop retorna o svalor {retorno}")

# Sem retorno: print não retorna valor, por isso não pode ser atribuida a uma variavel
retorno_print = print(numeros)
print(f"A função print não retorna nada {retorno_print}")


# imprimindo o quadrado de 7.
# Não é um retorno é um print.
def quadrado_de_7():
    print(7 * 7)


# a função acima não pode ser usada para atribuição de valores porque não tem um return
retorno_quadrado_de_7 = quadrado_de_7()

# quando não retorna nenhum valor o retorno é None
print(retorno_quadrado_de_7)


# Para retornar é necessário usar return
def quadrado_de_7_com_retorno():
    return 7 * 7


retorno_quadrado_de_7 = quadrado_de_7_com_retorno()
print(f"Retorno da função {retorno_quadrado_de_7}")


# apos o retorno nada é executado
def depois_do_retorno():
    print("Antes do retorno")
    return "Oi"
    print("Nunca será executado")


depois_do_retorno()


# Vários retornos: o fluxo do código somente pode chegar até um
def varios_returns():
    variavel = False
    if variavel:
        return True
    elif variavel is False:
        return False
    else:
        return None


print(varios_returns())


# Retornar múltiplos valores
def multiplos_retornos():
    return 1, 2, 3, 4, 5


# desempacotando
a, b, c, d, e = multiplos_retornos()

for i in list([a, b, c, d, e]):
    print(i)


# Tanto o pacote quanto a função tem o mesmo nome
from random import random


# Exemplo: Função jogar moeda
def jogar_moeda():
    # gera um numero randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return "Cara"
    else:
        return "Coroa"


cara = 0
coroa = 0
# executa 1Mi de vezes a função e conta quantas caras e coroas
for _ in range(1_000_000):
    if jogar_moeda() == "Cara":
        cara += 1
    else:
        coroa += 1

print(f"Total Cara: {cara} - Total Coroa: {coroa}")
print(f"% Cara: {cara/1_000_000} - % Coroa: {coroa/1_000_000}")


def he_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else:
        return False


print(he_impar())









