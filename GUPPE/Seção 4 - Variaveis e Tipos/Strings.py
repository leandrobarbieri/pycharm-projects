"""
"""
nome_string = "Leandro"
lista_string = ["L", "e", "a", "n", "d", "r", "o"]

print(list(nome_string))
print(lista_string)

# os 3 primeiros caracteres
print(lista_string[:3])
print(nome_string[:3])

# operações
print(lista_string[:3] * 3)
print(nome_string[:3] * 3)

# atribuição
lista_string[0] = "B"
print(lista_string)

# Metodos


# replace
nome_com_letras_repetidas = 'banana'
print(nome_com_letras_repetidas.replace("n", "t", 2))

nome_string = nome_string.upper()
print(nome_string)

nome_string = [letra.upper() for letra in lista_string]
print(nome_string)

# teste logico
texto_numerico1 = '56'
texto_numerico2 = 'CINQUENTA E SEIS'
texto_numerico3 = '56anos'

print(texto_numerico1.isnumeric())
print(texto_numerico2.isnumeric())
print(texto_numerico3.isalnum())

print(texto_numerico2.isupper())

# Buscar partes de texto
text_buscar = "a abelinha zune que zune durante a manha"
print(text_buscar.find("a", 0)) # primeiro a
print(text_buscar.find("a", 2)) # segundo a
print(text_buscar.find("a", 8)) # terceiro a

# Se não achar retorna -1
cpfs = ["10010100090", "103.324.123-04"]
for cpf in cpfs:
    print(f"{cpf if cpf.find('-') != -1 else 'Não é cpf'}")

# quebrando frase em palavras
frase1 = "Olá pessoal"
frase2 = "Batatinha quando nasce espalha ramas pelo chão".replace(" ", "-")
print(frase1.split())
print(frase2.split(sep="-", maxsplit=2))

# lendo arquivos com varias linhas texto
with open("emails.txt", "r") as lista_emails:
    linha = lista_emails.readlines()

print(linha)

with open("emails.txt", "r") as lista_emails:
    emails = lista_emails.read().split("\n")

for email in emails:
    print(f"Login: {email[:email.find('@')]}")


# Format strings









