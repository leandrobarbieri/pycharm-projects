"""
Reduce a partir do python 3 acima não é uma função built-in (import functools)
Recebe dois parametros (função, dados)
dados = [a1, a2, a3, ..., an]

# a função só pode receber dois parametros
def funcao(x, y):
    return x * y

- Passo 1: resultado1 = funcao(a1, a2) - aplica nos dois primeiros e passa o resultado
- Passo 2: resultado2 = funcao(resultado1, a3) - aplica a função passando o resultado do passo1 mais o terceiro elemento
.
** isso é repetido até o ultimo elemento, em cada passo aplica a função passando o argumento do resultado do elmento anterior
funcao(funcao(funcao(a1, a2), a3), a4)...)

"""
from functools import reduce
# Multiplicar todos os numeros de uma lista
dados = [1, 2, 3, 4, 10]
# funcao = lambda x, y: x * y
resultado = reduce(lambda x, y: x * y, dados)
print(resultado)








