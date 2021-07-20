"""
Trabralhar com cursor nos ajuda a manipular a partir de onde será lido ou escrito
seek() movimentar o cursor no arquivo, alterar a posição

"""


arquivo = open("texto.txt", encoding="utf-8")
print(arquivo.read())

# Ao ser lido pela segunda vez o cursor está no final do texto,
# então não imprime novamente
print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek
# seek(): recebe um parametro indicando a posição para colocar o cursor
arquivo.seek(20)
print("-------------")
# a leitura inicia a partir da posição 20
print(arquivo.read())

arquivo.seek(0)
print("-------------")
# Limita a leitura aos 10 primeiros caracteres
print(arquivo.read(10))

print("-------------")
arquivo.seek(0)
"""ReadLine: Para ler o arquivo linha a linha"""
print(arquivo.readline())

print("-------------")
arquivo.seek(0)

print("-------------")
arquivo.seek(0)
"""ReadLines(): retorna as linhas com uma lista de linhas"""
lista_linhas = arquivo.readlines()
print(lista_linhas)
print(f"Quantidade de linhas: {len(lista_linhas)}")

# a ligação entre o arquivo no disco e o programa é chamado de streaming
# close() fecha o streaming para avisar o SO que não está mais usando o arquivo, remove o lock no arquivo
if arquivo.closed:
    print(f"Arquivo fechado {arquivo.closed}")
else:
    print(f"Arquivo fechado {arquivo.closed}")
    arquivo.close()


