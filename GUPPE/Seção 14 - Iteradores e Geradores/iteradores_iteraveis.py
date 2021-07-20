"""
Diferença entre iterators (iteradores) e iterables (iteravel)

iterator: tupla, list, dict
- elemento que pode ser iterado
- retorna um elemento por vez quando uma função next() é chamada por baixo dos panos
- retorna uma informação/dado

iterable:
- retorna um iterator
- Não retorna um dado

"""

nome_iterable = "Leandro"
numeros = [1, 2, 3]

# TypeError: 'str' object is not an iterator
# print(next(nome_iterable))

# Cria um iterator a partir de um iteravel
iterator1 = iter(nome_iterable)
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))

# Iterando no iteravel numeros
iterator2 = iter(numeros)
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))

# o for faz isso implicitamente: 1-Cria um iter, 2-Faz um next() até o final
for letra in nome_iterable:
    print(f"Letra> {letra}")

print("---------------")


# 1-iter na lista: iter([1, 2, 4, 5])
# 2-num: next(iter([1, 2, 4, 5]))
for num in [1, 2, 4, 5]:
    print(f"Letra: {num}")


# criando a propria versão do loop for para entender o que acontece com os iterable
def meu_for(meu_iteravel):
    # transforma em iterator
    it = iter(meu_iteravel)
    while True:
        try:
            # percorre o iterator
            print(next(it))

        # quando chegar ao fim gera esse erro
        except StopIteration:
            break


# Usando meu_for
numeros = [9, 8, 7]
meu_for(numeros)


# iterador customizado. precisa ter pelo menos a função iter e next
class Contador:
    # construtor da classe. self representa o proprio objeto da classe
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    # convert para um iterable
    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            num1 = self.menor
            self.menor = self.menor + 1
            return num1
        raise StopIteration


print("--------")
for n in Contador(1, 4):
    print(n)
















