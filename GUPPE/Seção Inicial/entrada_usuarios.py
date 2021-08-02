
# Entrada de dados
# print("Qual é o seu nome: ")
nome = input("Qual é o seu nome: ")

# versão antiga
print('Seja bem vindo! %s' % nome)

# versão nova
print("Seja bem vindo! {0}".format(nome))

# versão mais moderna
print(f'Seja bem vindo! {nome}')

# print('Qual a sua idade?')
# idade = input('Qual a sua idade?')
idade = int(input('Qual a sua idade?'))

print('{0} tem {1} anos'.format(nome, idade))
print(f'{nome} tem {idade} anos')

# os dados recebidos são uma string, precisamos converter quando for usar
# print(f'{nome} nasceu em {2021 - int(idade)} anos')
# dá para pra fazer cálculos ao mesmo tempo que formata a impressão
print(f'{nome} nasceu em {2021 - idade} anos')


