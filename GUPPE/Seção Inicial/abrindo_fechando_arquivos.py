"""
Abrir e fechar, ler e escrever em arquivos
O arquivo é aberto na memoria e pode ser trabalhado

Modos de abertura de arquivo:
w= escrever no arquivio -> usamos o write()
r= ler o arquivo
a= append, adiciona o conteudo. Diferente de write porque write sobrescreve tudo

https://www.youtube.com/watch?v=ad8toeTUXZs
https://www.pythonprogressivo.net/2018/10/Como-EscreverArquivo-write-Modo-Abertura.html

"""

# abrindo sem with: usando apenas a função open
arquivo1 = open("arquivo.txt", "w")  # w significa write
arquivo1.writelines("Opa! Olha! Escrevendo a primeira linha\n")
arquivo1.writelines("Opa! Olha! Escrevendo a segunda linha")

# temos sempre que lembrar de fechar o arquivo para liberar o recurso. Usando with não precisaria
arquivo1.close()

# Lendo o arquivo cin with
with open("arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines()

# cada linha vira um elemento de uma lista
for linha in linhas:
    print(linha)

# Usando with. Fecha o arquivo automaticamente
# Escrevendo em um arquivo
with open("arquivo_novo.txt", "w") as arquivo:
    #   linhas = arquivo.readlines
    arquivo.write("Escrevendo no with!\n")


# Usando a opçãp "a" append para adicionar conteúdo sem apagar o anterior
with open("arquivo_novo.txt", "a") as arquivo:
    arquivo.write("Adicionando conteúdo")


# lendo o conteúdo adicionado
with open("arquivo_novo.txt", "r") as arq:
    print(arq.readlines())
