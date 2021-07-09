"""
Implementações alternativas as coleções builtin do python
Counter - Recebe um iteravel com parametro e cria um obj do tipo Counter que é parecido com um dict

Cria um obj do tipo chave valor:
Chave: Elemento
Valor: Quantidade de ocorrências dos elmentos da colection recebida
https://pymotw.com/2/collections/counter.html
"""

from collections import Counter
lista1 = ["Leandro", "Leandro", "Leandro", "Leandro", "Bruna", "Bruna", "Bruna", "Breno", "Breno"]

# utilizando o counter
counter1 = Counter(lista1)
print(counter1)

# Counter direto de uma string
print(Counter("araraquara"))

# Contando letras e palavras
poema = "O Cabral foi um navio de guerra do tipo corveta encouraçada ou, simplesmente, encouraçado, operado pela Armada Imperial Brasileira entre anos de 1866 e 1882. A embarcação foi construída no estaleiro da empresa britânica J. and G. Rennie em Greenwich, Inglaterra, e era líder de sua classe, que também contava com o Colombo. Foi lançado ao mar em 1865 e incorporado à armada em 15 de setembro"

# Quantidade de vezes que uma letra aparece
print(Counter(poema))

# Quantidade de vezes que a palavra aparece
palavras = poema.split()
print(Counter(palavras))

# 5 palavras com mais ocorrências
print(Counter(palavras).most_common(5))

# itenando em um Counter
for key, val in Counter(palavras).items():
    print(f"Chave: {key}, Valor: {val}")

counter2 = Counter(palavras)
for palavra in palavras:
    print(f"Palavra: {palavra} - Quantidade: {counter2[palavra]}")




