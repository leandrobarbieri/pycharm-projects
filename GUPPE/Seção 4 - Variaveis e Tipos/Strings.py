"""
Uma string funciona como uma lista/tupla composta por letras
Tem varios metodos semelhantes a listas
Uma string pode ser convertida em lista
"""

nome_string = "Leandro"
nome_lista = ["L", "e", "a", "n", "d", "r", "o"]

# transformando uma string em lista
print(list(nome_string))
print(nome_lista)

# os 3 primeiros caracteres da string (class str)
print(nome_string[:3])
print(type(nome_string[:3]))

# os 3 primeiros caracteres da lista (class list)
print(nome_lista[:3])
print(type(nome_lista[:3]))

# operações: repete 3 vezes o mesmo conjunto de 5 primeiros elementos da string e da lista
print(nome_string[:5] * 3)
print(nome_lista[:3] * 3)


# atribuição em listas
nome_lista[0] = "B"
print(nome_lista)

# atribuição em string não é permitido: TypeError: 'str' object does not support item assignment
# porque str é tratado como uma tupla imutavel
#nome_string[0] = "B"


# METODOS PARA TRABALHAR COM STRINGS

# replace
nome_com_letras_repetidas = 'bananinha'
# substitui as letras n por letras t somente as duas primeiras ocorrências
print(nome_com_letras_repetidas.replace("n", "t", 2))

# Altera todas as letras para maiusculo
nome_com_letras_repetidas = nome_com_letras_repetidas.upper()
print(nome_com_letras_repetidas)

# acessa cada uma das letras na lista nome_lista e aplica a função upper() e retorna uma lista
nome_lista = [letra.upper() for letra in nome_lista]
print(nome_lista)

# teste logico
texto_numerico1 = '56'
texto_numerico2 = 'CINQUENTA E SEIS'
texto_numerico3 = '56anos'

print(texto_numerico1.isnumeric()) # True
print(texto_numerico2.isnumeric()) # False
print(texto_numerico3.isalnum()) # True: Verifica se é alphanumerico
print(texto_numerico2.isupper()) # True: está em maiusculo

# Buscar partes de texto
text_buscar = "a abelinha zune que zune durante a manha"

# buscar a letra "a" a partir do primeiro caracter
print(text_buscar.find("a", 0)) # encontra a primeira ocorrencia de a
print(text_buscar.find("a", 2)) # encontra a segunda ocorrencia de a

# busca uma palavra zune
print(text_buscar.find("zune", 8)) # primeira ocorrencia de "zune"
print(text_buscar.find("zune", 15)) # segunda ocorrencia de "zune"

# Se o metodo find não achar retorna -1
cpfs = ["10010100090", "103.324.123-04"]
for cpf in cpfs:
    print(f"{cpf if cpf.find('-') != -1 else 'Não é cpf'}")

# quebrando frase em palavras
frase1 = "Olá pessoal"
frase2 = "Batatinha quando nasce espalha ramas pelo chão".replace(" ", "-")
print(frase1.split())
print(frase2.split(sep="-", maxsplit=3)) # separa no máximo 3 palavras, o restante deixa junto

# lendo arquivos com varias linhas texto
with open("emails.txt", "r") as lista_emails:
    linha = lista_emails.readlines()

print(linha)

with open("emails.txt", "r") as lista_emails:
    emails = lista_emails.read().split("\n")

# lista todos os emails e extrai apenas a parte do login
# inicia no primeiro catacter e termina na posição encontrada na função quando achar o @ = email[:email.find('@')
for email in emails:
    print(f"Login: {email[:email.find('@')]}") # retorna do inicio até a posição do caracter @


# Traduzir um texto automaticamente usando a internet
from textblob import TextBlob

texto_outro_idioma = "Hello world. This text are translated by one python library called TextBlob"

# vai na internet e faz a tradução
texto_traduzido = TextBlob(texto_outro_idioma).translate(to="pt-br")

print("-------------------------------")
print(texto_traduzido)









