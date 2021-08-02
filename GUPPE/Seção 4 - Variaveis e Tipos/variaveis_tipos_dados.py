"""
Tipos Numéricos:
"""

# 16
print(4 * 4)

# 2.5
print(5/2)

# 2
print(5//2)
print(int(5/2))

# Resto da divisão. 1-Impar, 0-Par
print(5 % 2)

# Potencia, elevado
print(2 ** 2)
print(2 ** 10)

# Limpar console Ctrl + L

# permite usar underline no lugar dos separados de milhar sem deixar de considerar com numero
print(1_000_000)

num = 10
# num = num + 1
num += 1
print(num)
# num = num * 2
num *= 2
print(num)

# type informa o tipo <class 'int'>
print(type(num))


"""Separador de casas decimais é ponto e não vírgula"""
num = 1.4
print(num)

"""Errado: ele acha que é uma tupla com dois elementos (1, 4)"""
num = 1,4
print(type(num))

"""Dupla atribuição: permitido porque é como se estivesse desempacotando uma tupla"""
valor1, valor2 = 1, 4
print('{0}, {1}'.format(valor1, valor2))

# invertendo o valor de duas variaveis
var1 = 10
var2 = 20
print(f"var1: {var1}, var2: {var2}")
var1, var2 = var2, var1
print(f"var1: {var1}, var2: {var2}")

"""Tipo booleano: verdadeiro True, Falso: False"""
var1 = True
var2 = False
if var1 != var2:
    print(f"Diferente {var1} e {var2}")

"""Negação: not"""
var2 = not var2
print(var2)
if var1 == var2:
    print("A negação tornou verdadeiro")

"""Or And"""
n1 = 10
n2 = 20
if n1 < 10 or n2 > 10:
    print("Um dos dois é maior que 10")

if n1 < 10 and n2 > 10:
        print("Um dos dois não é True")

"""Tipo String:
É considerado uma string sempre que o texto estiver entre 'Texto' ou "Texto" ou '''Texto''' 
"""
print(type("Gina's Bar".lower()))
print(type('Nome'.upper()))

# lista de strings
print(type("""Gina's Bar""".split()))
print("""Gina's Bar""".split())

# slice de string
nome = 'Leandro Barbieri'
print(nome[0:4])
print(nome[:10])

# Duas listas separadas pelo espaço 'Leandro', 'Barbieri']
nome = 'Leandro Barbieri'.split()
print(nome[1][0:4])

# Começa no primeiro vai até o ultimo :: e muda o sentido +1 para -1, ou seja caminha ao contrario
nome = 'Leandro Barbieri'
print(nome[::-1])

# replace
nome = 'Leandro'
print(nome.replace('L', 'B'))







