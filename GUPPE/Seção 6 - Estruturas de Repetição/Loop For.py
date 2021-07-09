"""
Loop com tamanho definido
Estrutura de repetição mais usada
Inicialização, Incremento, Limitador

for item in iteravel:
    // execução

- iteraveis são strings, sequencias, listas, range, tuplas, arrays
Exemplo string é um valor iteravel
- String: "Leandro"
- Lista:
    ls = [1, 2, 3]
- Range:
    numeros = range(1, 10)
"""

"""
String
Enumerate cria uma tupla para cada letra com a letra e o codigo
i representa o indice
"""

# end="-" para seração das letras
for item in "Leandro":
    print(f"{item}", end="-")


for item in "Leandro":
    print(f"Letra: -> {item}")

# gerar indice usando enumerate
for i, item in enumerate("Leandro"):
    print(f"Indice: {i} -> {item}")

# usando _ ignora o valor retornado na iteração, ou seja não pega o indice da tupla gerada pelo enumerate
for _, item in enumerate("Leandro"):
    print(f"Item: -> {item}")

# sem usar _ item irá copiar para item a tupla inteira
for item in enumerate("Leandro"):
    print(f"Item: -> {item}")

print("Tupla -> ", enumerate("Leandro"))


"""Lista"""
ls = [10, 20, 30]
for item in ls:
    print(item)
print("Lista:", ls)


"""range o valor final não é incluído: range(1, 4) vai de 1 até o 3"""
rang = range(1, 4)
for item in rang:
    print(item)
print("Lista range (1, 4): ", rang)


# iteração com tamanho variável
qtd = int(input("Quantas vezes deve rodar?"))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f"Informe o {n}/{qtd} valor"))
    soma = soma + num

print(f"A soma do acumulado é {soma}")


# Usar _ descarta o retorno. Para repetir 3 vezes iterando na lista mas sem pegar nada
for _ in range(3):
    print("Repete 3 vezes")

# usando break
for num in range(1, 10):
    if num == 6:
        break
    else:
        print(num)
