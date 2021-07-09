""""LEN: Conta a quantidade de elementos que existe o iteravel"""
# String
print(len("Ola"))

# Lista
print(len([1, 2, 3]))

# tuple
print(len((1, 2, 3)))

# set
print(len({1, 2, 3}))

# Dict
print(len({"a": 1, "b": 2, "c": 3}))


"""ABS: Valor real sem o sinal"""
print(abs(-1))
print(abs(-1.5))


"""SUM: Recebe como parametro um iteravel, retorna a somata incluindo um valore inicial default=0"""
# Precisa que todos os elementos do iteravel sejam numeros
print(sum([1, 2, 3]))
print(sum([1, 2, 3], start=10))

# Sum em dict: precisa usar values() para acessar os valores
print(sum({"a": 1, "b": 2, "c": 3}.values()))

# Erro
# print(sum(["1", "2", "3"])

"""ROUND: arredonda para um determinada precisão"""
print(round(1.2323234123234, 1))
print(round(1.2923234123234, 1))

