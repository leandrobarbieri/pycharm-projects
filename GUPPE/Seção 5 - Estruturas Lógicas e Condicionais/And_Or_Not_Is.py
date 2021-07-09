"""
Todos operadores lóogicos: AND, OR, NOT, IS
- Operadores Unários: not (inverte o valor), is
- Operadores Binários: and, or
"""

ativo = not False
logado = False

if ativo or logado:
    print("Bem vindo usuário ativo/logado")
else:
    print("Você precisa ativar para logar")

ativo = True
logado = True

if ativo and logado:
    print("Bem vindo usuário ativo/logado")
else:
    print("Você precisa ativar para logar")

"""is checa o valor binário"""
print(ativo is False)
print("ativo".isnumeric())
print("ativo".islower())
print("ativo".isprintable())





