"""
Tuplas: Listas com enumerables, não mutaveis. são parecidas com listas.
Diferenças:
# Tuplas são representadas por parênteses, ou podem apenas estar separadas por ,
# Tuplas são imutaveis. Toda operação em uma tupla gera uma nova tupla

# Atenção:
- São represetadas por parenteses ()
- Tuplas são definidas pelo uso de vírgula isso não é tupla (4),
- isso (4, ) ou isso é 4, É tupla:
    ()
    (1, 2, 3)
    1, 2, 3
    1,
Não é tupla:
    (1)

# Métodos de adição e remoção de elementos em tuplas não existem
# Existem: soma, maximo, min, tamanho (len)

Dicas de utilização: sempre que não precisarmos mudar os dados de uma coleção. Evitar inconsistências
- Lista de Meses: Jan, Fev, Mar, Abr, Mai....

Porque utilizar tuplas?
São mais rapidas do que listas
Deixa seu código mais seguro. Elementos imutáveis trazem mais segurança para o seu código
"""

# Tupla vazias
print(type(()))

# Tupla normal
tupla1 = (1, 2, 3, 4, 5)

# Tipo : <class 'tuple'>, Valor: (1, 2, 3, 4, 5)
print(f"Tipo : {type(tupla1)}, Valor: {tupla1}")

# sem parenteses pode
tupla2 = 1, 2, 3, 4, 5, 6
print(f"Tipo : {type(tupla2)}, Valor: {tupla2}")

# Isso não é uma tupla, é um inteiro, pra ser uma tupla precisa de uma vírgula
tupla3 = (6)
# Tipo : <class 'int'>, Valor: 6
print(f"Tipo : {type(tupla3)}, Valor: {tupla3}")

tupla3 = (6,)
# Tipo : <class 'tuple'>, Valor: (6,)
print(f"Tipo : {type(tupla3)}, Valor: {tupla3}")

# convertendo um range em uma tuple (ímpares)
tupla4 = tuple(range(1, 101, 2))
print(f"Tipo : {type(tupla4)}, Valor: {tupla4}")

# desempacotamento de tupla (número de elementos da tupla precisa ser igual a quantidade de variáveis)
tupla5 = ("Leandro", "Bruna", "Breno")
pai, mae, filho = tupla5
print(f"Pai: {pai}, Mãe: {mae}, Filho: {filho}")

# Métodos de agregação - ímpares de 1 a 100. Somente para valores inteiros ou reais
tupla6 = tuple(range(1, 101, 2))
print(f"Soma: {sum(tupla6)}")
print(f"Max: {max(tupla6)}")
print(f"Min: {min(tupla6)}")
print(f"Quantidade: {len(tupla6)}")

# concatenação de tuplas. usar sinal de + para concatenar
tupla7 = ("Leandro", "Barbieri")
tupla8 = ("Bruna", "Moraes", "Barbieri")
print(f"A tupla {tupla7} foi concatenada com a tupla {tupla8} e ficou assim: {tupla7 + tupla8}")

# zip: pareando tuplas. Primeiro elemento de uma com o primeiro elemento da outra...
print(f"A tupla { tupla7 } foi pareada com a tupla { tupla8 }. Esse é o "
      f"resultado: { list(zip(tupla7, tupla8)) }")

for i, (pai, mae) in enumerate(zip(tupla7, tupla8)):
    print(f"Índice> {i}, Pai: {pai}, Mae: {mae}")

# unzip: despareando tuplas.
lista1 = list(zip(tupla7, tupla8))
leandro, bruna = zip(*lista1)

print(f"A lista { lista1 } foi despareada. Esse é o "
      f"resultado: Pai: { leandro }, Mae: { bruna}")

for i, (firstName, lastName) in enumerate(zip(*lista1)):
    print(f"Índice> {i}, FirstName: {firstName}, LastName: {lastName}")


# Acessando valores. Valores podem ser acessados, o que não pode é adicionar, remover
# Igual a lista informa o índice tupla9[1]
tupla9 = (1, 2, 3)
print(f"Tupla: {tupla9}. Acesando o segundo elemento pelo índice:  {tupla9[1]}")

# buscar uma elemento dentro da tupla
n = 3 # input("Digite o número que deseja buscar na tupla")
tupla10 = tuple(range(1, 11, 2))
print(f"O número {n} está na tupla {tupla10}? Resultado: {int(n) in tupla10}")

# iterando em uma tupla
for n in tupla10:
    print(n)
for i, n in enumerate(tupla10):
    print(f"I: {i}, n: {n}")

# contando quantas ocorrências de um elemento
tupla11 = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
print(f"Existem {tupla11.count(4)} com o número 4.")

tupla12 = tuple("Leandro Barbieri")
print(f"Existe {tupla12.count('e')} ocorrências da letra e na tupla {tupla12}.")


# while
i = 0
meses = ("Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul")
while i < len(meses):
    print(meses[i])
    i += 1

print(f"Tupla: {meses}")
# iniciando no elmento 0 e terminando no 6
print(f"Qual o índice do mês Jun na tupla?: {meses.index('Jun', 0, 6)}")

# slicing. Semelhante ao tratamento em listas
# tupla[inicio:fim:passo]
print(meses[3:6:1])
# ('Abr', 'Mai', 'Jun')

# copiando uma tupla para outra
tupla13 = (1, 2, 3)

# Não cria referencia, cópia por valor
novaTupla = tupla13 + (4, 5)

print(f"Atual: {tupla13}, Nova: {novaTupla}")

