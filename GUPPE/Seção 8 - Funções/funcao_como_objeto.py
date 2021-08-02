"""
Funções podem ser passadas como parametro como se fossem objetos e depois serem chamadas pelo nome
"""

# Exemplo: função para limpeza e tratamento de strings

# expressões regulares
import re

# Strings que precisam de tratamento
lista1 = ["#TesTe1!", "#tEste1#", "?TeSte1?"]


# Primeira forma: Iterar sob a lista de palavras e aplicar os métodos de tratamento definidas na função
def tratar_strings(lista):
    strings_tratadas = []
    for texto in lista:
        texto = texto.strip()
        texto = re.sub("[!#?]", "", texto)
        texto = texto.upper()
        strings_tratadas.append(texto)
    return strings_tratadas


print(tratar_strings(lista1))


# Segunda Forma: Usando funções como parâmetros


# Define uma função auxiliar para aplicar uma expressão regular
def remover_pontuacao(texto):
    return re.sub("[!#?]", "", texto)


# Receber uma lista de funções de tratamento em tempo de execução para aplica-las em um for
def tratar_strings2(lista, funcoes):
    strings_tratadas = []
    for texto in lista:
        for funcao in funcoes:
            texto = funcao(texto)
        strings_tratadas.append(texto)
    return strings_tratadas


# Usando a segunda forma: Passar uma lista com o nome de todas as funções de tratamento. Tratamento dinâmico
lista_funcoes = [str.strip, remover_pontuacao, str.upper]
lista2 = ["#TesTe2!", "#tEste2#", "?TeSte2?"]

tratar_strings2(lista2, lista_funcoes)
