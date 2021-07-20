"""
StringIO: Utilizado para ler e criar arquivos em memória

"""

from io import StringIO

mensagem = "String normal com qualquer valor"

# é a mesma coisa que fazer arquivo = open("arquivo_stringIO.txt", w)
arquivo_stringIO = StringIO(mensagem)

print(f"{arquivo_stringIO.read()} \n----------------")

arquivo_stringIO.write("\nNova linha no texto")

arquivo_stringIO.seek(0)
print(arquivo_stringIO.read())

