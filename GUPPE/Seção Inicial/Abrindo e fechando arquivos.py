"""Vídeo: https://www.youtube.com/watch?v=ad8toeTUXZs"""

# abrindo sem with: usando apenas a função open
arquivo1 = open("arquivo.txt", "w")  # w significa write
arquivo1.write("Opa! Olha!")
arquivo1.close()

# Usando with. Fecha o arquivo automativamente
# Escrevendo
with open("arquivo.txt", "w") as arquivo:
    #   linhas = arquivo.readlines
    arquivo.write("Escrevendo no with!")

# Lendo o arquivo
with open("arquivo.txt", "r") as arquivo:
    linhas = arquivo.readlines()

print(linhas)

