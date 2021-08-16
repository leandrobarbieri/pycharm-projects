"""
Listas são vetores, matrizes dinamicos, qualquer tipo de dado
Podem ter tipos de dados misturados e o tamanho pode aumentar dinamicamente

Outras linguagens:
- possuem tamanho e tipo de dado fixo

Python
- Dinâmico: não possui tamanho fixo. Criar a lista e adiciona elementos (enquanto houver memória)
- Qualquer tipo de dado: não possuem tipo de dado fixo

As listas são representadas por [ ]

"""

# lista 1: [1, 2]
lista = list(range(1, 3))
for i in lista:
    print(i)
print(type(lista))
print("---------------")

# lista 2
lista2 = [1, 2, 3]
print(lista2)
print("---------------")

# lista 3
lista3 = ["A", "B", "C"]
print(lista3)
for i in lista3:
    print(i)
print("---------------")

# lista 4 - string to list
lista4 = list("leandro")
print(lista4)
print("---------------")

# checar se determinado valor está na lista
num = 4
if num in lista2:
    print("Encontrei 4")
else:
    print("Não econtrei 4")

# checar se um determinado nome está na lista usando parte do nome
lista_nomes = ["Leandro", "Bruna", "Breno"]
print([valor for valor in lista_nomes if valor.startswith("Br")])
print("---------------")

lista4.sort()
if "e" in lista4:
    print(f"Encontrei a letra E na lista {lista4}")
else:
    print("Não encontrei a letra E")
print("---------------")

# ordenação numeros
lista5 = [10, 3, 55, 4]
lista5.sort()
print(lista5)
print("---------------")

# podemos contar o numero de ocorrencias de um valor em uma lista
lista6 = [1, 3, 1, 4, 1]

# append adiciona apenas um elemento por vez
# contar quantas vezes o numero 1 aparece
lista6.append(1)
print(f"A lista6 {lista6} tem {lista6.count(1)} numeros 1!")
print("---------------")

# append permite adicionar uma lista como elemento de uma lista
# sempre no final da lista
# lista6 [1, 3, 1, 4, 1, 1, [1, 2, 3]]
lista6.append([1, 2, 3])
print(f"A lista6 {lista6}")
print("---------------")

# procura a lista inteira como um elemento da outra lista
if [1, 2, 3] in lista6:
    print("Encontrei [1, 2, 3] a lista")
print("---------------")

# extend adiciona os elementos da lista no final da lista, mas não como um elemento da lista
# ele pega extrai da lista e inclui elemento por elemento individualmente
# com append: [1, 3, 1, 4, 1, 1, [1, 2, 3] ]
# com extend: [1, 3, 1, 4, 1, 1, 1, 2, 3]
lista7 = [1, 2, 3]
lista7.extend([4, 5, 6])
print(f"A lista7 com extend {lista7}")
print("---------------")
lista7.extend("Leandro") # [1, 2, 3, 4, 5, 6, 'L', 'e', 'a', 'n', 'd', 'r', 'o'
print(f"A lista7 com extend {lista7}")
print("---------------")

# extend não aceita valor único. valor unico usar append
# lista7.extend(4) # erro

# podemos inserir informando a posição do índice
lista8 = [1, 2, 3, 4, 5, 6]
lista8.insert(5, 99)
# [1, 2, 3, 4, 5, 99, 6]
print(lista8)
print("---------------")

# juntar duas listas, semelhante ao extend
# lista7.extend(lista8)
# [1, 2, 3, 4, 5, 6, 'L', 'e', 'a', 'n', 'd', 'r', 'o', 1, 2, 99, 3
lista9 = lista7 + lista8
print(lista9)
print("---------------")

# lista invertida: ireibraB ordnaeL
print(lista9.reverse())
nome = 'Leandro Barbieri'
# vai do do inicio ao fim com o passo -1
print(nome[::-1])
print("---------------")

# tamanho da lista len()
lista10 = list("Leandro")
print(lista10)
print(f"Tamanho da lista: {len(lista10)}")
print("---------------")

# remove o ultimo elemento de uma lista pop e o retorna
print(f"Foi removido o elemento {lista10.pop()}. Agora a lista está assim {lista10}")
print(f"Foi removido o elemento {lista10.pop()}. Agora a lista está assim {lista10}")
print(f"Foi removido o elemento {lista10.pop()}. Agora a lista está assim {lista10}")
print("---------------")

# remover pelo índice
lista11 = list("Leandro")
print(f"Foi removido o elemento na posição 2, '{lista11.pop(2)}', agora a lista está assim: {lista11}")
print("---------------")

# limpar totalmente a lista. Remover todos os elementos
lista11.clear()
print(f"A lista está assim agora: {lista11}")
print("---------------")

# repetir a inserção de elementos em uma lista
lista12 = [1, 2, 3]
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(f"A lista {lista12} pode ser repetida 3 vezez usando a multiplização lista12 * 3. Resultado: {lista12 * 3} ")
print("---------------")

# split de uma frase em palavras
lista13 = "Leandro Moraes Barbieri"
print(f"A fase {lista13} pode ser transformada em uma lista de palavras com "
      f"lista13.split(). Resultado: {lista13.split()}")

lista14 = "Programação-Em-Python".split("-")
print(lista14)
print("---------------")

# Transformar uma lista de volta para string
# pegar cada elemento da lista14 e juntar eles em uma string separada por espaço em cada junção
lista14 = " ".join(lista14)
print(lista14)
print("---------------")

# uma lista pode ter na mesma lista tipos diferentes e outras listas
lista15 = [1, "a", 1.3, True, [1, 2, 3]]
print(f'A lista15 é do tipo {type(lista15)}. Lista: {lista15} ')
print("---------------")

# iteração sob listas utilizando FOR
soma = 0
lista16 = list(range(1, 5))
for i in lista16:
    print(i)
    soma += i

print(type(lista16))
print(soma)
print("---------------")

# iteração utilizando While
carrinho = []
produto = ''
while produto != 'sair':
    produto = input("Adicione um produto, ou digite sair: ").lower()
    if produto != 'sair':
        carrinho.append(produto)
# carrinho.pop()

for produto in carrinho:
    print(f" Produto: {produto}")
print(f"Todos os produtos: {carrinho}, total: {len(carrinho)} produtos cadastrados.")
print("---------------")

# criar listas utilizando variáveis
cor1 = "Verde"
cor2 = "Azul"
cor3 = "Vermelho"

cores = [cor1, cor2, cor3]
print(cores[0], cores[1], cores[2])
print("---------------")

# acessando pelo indice reverso
print(cores[-3], cores[-2], cores[-1])
print("---------------")

# loop com for
for cor in cores:
    print(cor)
print("---------------")

# loop com while
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1
print("---------------")

# capturar indice em um for
# enumerate gera par de chave-valor tuple para os itens da lista
for i, cor in enumerate(cores):
    print(f"A cor da posição {i} é {cor}.")

print(f"Lista completa de cores no formato de enumerate: {list(enumerate(cores))}")
print("---------------")

# lista podem ter valores repetidos. Algumas estruturas não permitem
lista17 = []
lista17.append(1)
lista17.append(1)
lista17.append(2)
lista17.append(2)
print(lista17)
print("---------------")

# encontrar um elemento na lista. retorna a primeira ocorrência
# em qual indice está o valor C?
lista18 = ["A", "B", "C", "D", "I", "O", "C", "B", "W", "X", "C"]
print(lista18)
print(lista18.index("C"))
print("---------------")

# senão tiver dá erro
# print(lista18.index("X"))

# Definir a busca a partir de um ponto específico
# inicia a busca a partir do terceiro elemento da lista
# neste caso ele retornou o segundo C
print(lista18.index("C", 3))
print("---------------")

# buscando o indice do segundo C de forma dinamica
print(lista18.index("C", lista18.index("C")+1))

# buscando o indice do terceiro C de forma dinamica/recursiva
print(f"Buscando o terceiro C: Posição -> {lista18.index('C', lista18.index('C', lista18.index('C')+1)+1)}")
print("---------------")

# busca dentro de um range do index 2 até 6
print(lista18.index("C", 2, 6))
print("---------------")

# SLICES
# range(inicio, fim, passo)
# lista[inicio:fim:passo]
lista19 = [1, 2, 3, 4, 5]

# Iniciando no elemento 2 até o final. Quando não tem nada assume o valor padrão do tamanho da lista
print(lista19[2:])
print("---------------")

# Inicia no índice 0 e termina em 2
print(lista19[:2])
print("---------------")

# pegar todos os elemento do inicio ao fim
print(lista19[:])
print("---------------")

# Começa em 1 vai até o final com passo 2: lista[inicio:final:passo]
print(lista19[1::2])
print("---------------")

# intertendo valores de uma lista - desempacotando, atribuição multipla
nomes = ["Leandro", "Barbieri"]
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
print("---------------")

# invertendo lista com reverse
nomes.reverse()
print(nomes)
print("---------------")

# analisando valores da lista: soma, maximo, minimo, tamanho
lista20 = [1, 2, 3, 4, 5]
print(f"Soma: {sum(lista20)}")
print(f"Max: {max(lista20)}")
print(f"Min: {min(lista20)}")
print(f"Quantidade: {len(lista20)}")
print("---------------")

# Transformar uma lista em tupla
tupla = tuple(lista20)
# repete 2 vezes a tupla
print(tupla * 2)
print("---------------")

# desempacotamento. Se tiver mais elementos do que variaveis para receber os valores da ERRO
n1, n2, n3, n4, n5 = tupla
# n1, n2, n3, n4, n5 = tupla[0], tupla[1],  tupla[2],  tupla[3],  tupla[4]
print(n1, n2, n3, n4, n5)
print("---------------")

# Copiando uma lista dentro da outra
# Shallow Copy e Deep Copy
lista21 = [1, 2, 3, 4, 5]
print(lista21)

# Não cria referencia. DeepCopy copia completamente os valores
novaLista = lista21.copy()
print(novaLista)
novaLista.append(6)

# toda nova modificação em uma lista copiada com .copy() não afeta a lista anterior.
print(lista21)
print(novaLista)
print("---------------")

# Shallow copy. Copia apenas a referencia
lista22 = [1, 2, 3, 4, 5]
print(lista22)

# Esse tipo de copia cria referencia, alterando uma altera a outra
novaLista = lista22
novaLista.append(6)

print(lista22)
print(novaLista)
print("---------------")

# Copiando os elementos DeppCopy
lista23 = [1, 2, 3]
listanova = lista23[:] # usando essa sintax com dois pontos faz uma copia por valor, não cria referencia
listanova.append(4)

print(lista23)
print(listanova)
print("---------------")

# Para lista de listas a copia de elemtos cria referencia (shalowcopy)
produtos = [
    ["Ipad", 5000],
    ["Smartphone", 2000],
    ["PC", 7000]
]

# As duas opções abaixão não funcionam para lista de listas, cria cópia shadow
# produtos2 = produtos[:]
# produtos2 = produtos.copy()

# Importar uma biblioteca que força a deepcopy das listas de listas
import copy

produtos2 = copy.deepcopy(produtos)

# Alterando o preço do Ipad somente na lista nova
produtos2[0][1] = 9999

print(produtos)
print(produtos2)



































