"""
Passa uma lista/dict para o arquivo
Tem os mesmos metodos de leitura/escrita

reader/writer

writerow

"""
from csv import writer, DictWriter, reader


# writerow para escrever a linha
with open('filmes.csv', 'w') as arquivo:
    filme = None
    escritor_csv = writer(arquivo)
    escritor_csv.writerow(["Titulo", "Genero", "Duracao"])
    while filme != "sair":
        filme = input("Filme:")
        if filme != "sair":
            genero = input("Genero:")
            duracao = input("Duraca:")

        # escreve no arquivo1
        escritor_csv.writerow([filme, genero, duracao])

# DictWriter para escrever a linha
with open('filmes_dict.csv', 'w') as arquivo:
    cabecalho = ["Titulo", "Genero", "Duracao"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != "sair":
        filme = input("Filme:")
        if filme != "sair":
            genero = input("Genero:")
            duracao = input("Duraca:")

        # escreve no arquivo1
        escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})


with open("filmes.csv", encoding="UTF-8") as arquivo2:
    dados = reader(arquivo2)
    for linha in dados:
        print(dados[0])

