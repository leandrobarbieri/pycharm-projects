"""
Generators são iterators:
- podem ser criados com funções geradoras

Diferemças entre funções normais e funções generators

Funções:
- usar return
- retorna uma vez apenas

Generators func:
- utilizam yield (não return)
- retorna um generator

** São estruturas mais otimizadas
"""


# exemplo de generator function
def conta_ate(valor_max):
    contador = 1
    while contador <= valor_max:
        # retorna mas não sai, aguarda até que uma função next() seja chamada
        yield contador
        contador += 1


# <class 'generator'>
print(type(conta_ate(5)))

generator = conta_ate(5)
print(next(generator))
print(next(generator))
print(next(generator))

print("-----------------")
# Não começa do inicio, contínua a partir dos next() acima
for num in generator:
    print(num)


# transformar em uma lista gera automaticamente todos os elmentos
print("-----------------")
lista_gerada = list(conta_ate(10))
print(lista_gerada)


# lista sequencia de fibonaci
def fib_lista(quantidade_elementos):
    nums = []
    a, b = (0, 1)
    while len(nums) < quantidade_elementos:
        nums.append(b)
        a, b = b, b + a
    return nums


print(fib_lista(20))


# Generator expression: usar parenteses, se parece com um list comprehension
gen2 = (num for num in range(1, 10))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))


# Comparando o tempo entre um generator e uma lista padrão
import time

# generator
gen_inicio = time.time()
print(sum(num for num in range(100_000_000)))
gen_tempo = time.time() - gen_inicio

# list comprehension
ls_inicio = time.time()
print(sum([num for num in range(100_000_000)]))
ls_tempo = time.time() - ls_inicio

print(f"Generator: {gen_tempo}\n")
print(f"List comprehension: {ls_tempo}")

















