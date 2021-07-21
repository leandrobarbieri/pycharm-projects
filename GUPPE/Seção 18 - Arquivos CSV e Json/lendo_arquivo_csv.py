"""
CSV: comma separeted values: usa vírgula ou ponto e vírgula em geral são usados para separar o conteúdo das colunas
sempre tem um padrão de separação em todas as colunas

- reader -> itera sob linhas de um arquivo
- DictReader -> itera sob as linhas como  OrderedDicts

"""


# Lendo com OPEN padrão sem usar as classes acima
print("\n---------------------------------------- lendo com open()")
with open("lutadores.csv", encoding="UTF-8") as arquivo:
    dados = arquivo.read()
    dados = dados.split(",")
    print(dados)


# Lendo com CSV.READER
print("\n----------------------------------------- lendo com reader()")
from csv import reader

with open("lutadores.csv", encoding="UTF-8") as arquivo:
    dados = reader(arquivo, delimiter=",")
    # pula a primeira linha para não imprimir os dados do cabeçalho
    next(dados)
    for linha in dados:
        # cada linha é uma lista, como elemento é uma coluna
        print(f"Nome: {linha[0]}, Pais: {linha[1]}")


# Lendo com CSV.DICTREADER
print("\n----------------------------------------- lendo com dictreader()")
from csv import DictReader

with open("lutadores.csv", encoding="UTF-8") as arquivo:
    dados = DictReader(arquivo, delimiter=",")

    # cada linha do arquivo se transforma em um dict com as chaves com o cabeçalho
    for dict1 in dados:
        print(dict1)


print("\n----------------------------------------- lendo com pandas")
# usando pandas
import pandas as pd

dados = pd.read_csv("lutadores.csv")
print(dados)

print("---------------------- lendo com pandas")
print(dados[["Nome", "País"]])

print("----------------------")
print(dados[dados["Altura (em cm)"] > 190])

