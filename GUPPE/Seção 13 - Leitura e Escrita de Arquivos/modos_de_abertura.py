"""
modos:
# "r": padrão. abre o arquivo para a leitura
# "w": abre para escrita, se o arquivo não existir cria, se existir sobrescreve
# "x": abre para a escrita somente se o arquivo não existir
# "a": abre para escrita e faz um append no final do arquivo. Se o arquivo não existe, será criado
# "+": abre para leitura e escrita ao mesmo tempo
"""

# abrindo com o modo "x"
try:
    with open("teste_abertura_modo_x.txt", "x") as arquivo3:
        arquivo3.write("Só escreve a primeira vez, depois que o arquivo é criado não pode mais ser aberto opção 'x'")
except FileExistsError:
    print("O arquivo não pode ser alterado, ele já existe!")


# abrindo com o modo "a": append, não sobrescreve
with open("fruta.txt", "a") as arquivo4:
    arquivo4.write("Bem vindos!\n")
    while True:
        fruta = input("Informe uma fruta ou digite S:")
        if fruta != "S":
            arquivo4.write(fruta)
            arquivo4.write("\n")
        else:
            break
