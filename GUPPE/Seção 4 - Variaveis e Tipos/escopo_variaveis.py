"""
Define a limitação da variavel
Limita onde ela será reconhecida no programa

Variaveis Globais:
Reconhecidas em todoo progrma

Variaveis Locais:
Limitado ao bloco que foi declarada

Declaração:
nome_da_variavel = valor_da_variavel

Python é de tipagem dinâmica: ao declarar uma variavel não é colocado o tipo de dado, o tipo é inferido ao atribuir
"""

"""Variavel Global"""
num = 1
if num < 11:
    """Variavel local"""
    nova = 0
    nova = num + 1

# conseguimos acessar a variavel global alterada no escopo do if
print(nova)
