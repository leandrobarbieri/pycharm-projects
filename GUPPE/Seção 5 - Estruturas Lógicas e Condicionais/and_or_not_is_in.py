"""
Operadores lógicos: AND, OR, NOT, IS, IN
- Operadores Unários: not (inverte o valor), is (checa se é True)
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


# Checa se um valor pertence a uma lista
print(f"X in XUXA:  {'x' in 'xuxa'}")
print(f"Z in XUXA:  {'z' in 'xuxa'}")

# Checar em lists
print(f"0 in [1, 2, 3, 4]:  {0 in [1, 2, 3, 4]}")
print(f"1 in [1, 2, 3, 4]:  {1 in [1, 2, 3, 4]}")

# Checagem em dict
estados = {"ES": 1, "RJ": 2, "SP": 3}
res = {'ES' in estados}
print(f"ES in ES, RJ, SP:  { res}")
print(f"ES in ES, RJ, SP:  { 'ES' in estados}")
print(f"RS in ES, RJ, SP:  { 'RS' in estados}")

