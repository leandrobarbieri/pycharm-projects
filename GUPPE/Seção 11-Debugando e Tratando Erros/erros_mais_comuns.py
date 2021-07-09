"""
Importante para saber corrigir os bugs mais comuns
Aprender a ler as saidas de erros
https://docs.python.org/3/library/exceptions.html
"""

"""1- NameError: name 'printf' is not defined"""
# printf("Teste")

"""2- SyntaxError  python não reconhece como parte a linguagem"""
# SyntaxError: invalid syntax

# def minha_funcao:
#   print("Precisa abrir e fechar os parenteses ao definir a função")

# Não pode usar None, def, return porque são palavras reservadas
# None = 1
# def = 1


"""3- NameError: Ocorre quando uma variavel ou função não foi definida"""
# NameError: name 'funcao_nao_definida' is not defined
# print(funcao_nao_definida)
# funcao_nao_definida()

a = 1
if a >= 10:
    msg = "A é maior ou igual a 10"

# a variavel não existe porque não entrou no if
# NameError: name 'msg' is not defined
# print(msg)


"""4- TypeError: uma função aplicada a um tipo incompatível"""
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# soma = 1 + "a"
# print(soma)

# len aplica somente em iteráveis
print(len("leandro"))

# TypeError: object of type 'float' has no len()
# print(len(2.9))


"""5- IndexError: Tentando acessar um elemento em uma lista com um índice inválido"""
lista1 = [["Leandro", "Barbieri"], ["Bruna", "Moraes"]]
print(lista1[1][1])

# IndexError: list index out of range
# print(lista1[2][1])

"""6- ValueError: Um função integrada recebe tipo correto mas o valor inapropiado"""
# OM
print(int(42))
# OK
print(int("42"))
# Tipo certo, mas valor inapropiado
# print(int("A")) # ValueError: invalid literal for int() with base 10: 'A'

"""7- KeyError: Tenta acessar uma chave que não existe"""
dic = {"chave1": 100, "chave2": 200}
print(dic["chave2"])

# KeyError: 'chave3'
# print(dic["chave3"])

"""AttributeError: quando uma variavel não tem um atributo ou função"""
tupla = (1, 2, 4, 5)

# AttributeError: 'tuple' object has no attribute 'sort'
# print(tupla.sort())














