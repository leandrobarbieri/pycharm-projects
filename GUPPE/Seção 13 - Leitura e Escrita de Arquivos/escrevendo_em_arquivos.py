"""
Alterar o conteudo

1-Abrir
2-Escrever
3-Fechar

Ao abrir para leitura apenas podemos ler, e não escrever
Ao abrir par escrita não podemos ler ao mesmo tempo

Usar open() no modo:
"w": se o arquivo não existir será criado, se existir o conteúdo anterior será apagado e sobrescrito

"""

with open("texto.txt", "w") as arquivo:
    # se o arquivo não existir será criado, se existir o conteúdo anterior será apagado e sobrescrito
    # aceita somente tipo str
    arquivo.write("Escrever dados em um arquivo1.\n")
    arquivo.write("Escrever dados em um arquivo2.\n")
    arquivo.write("Escrever dados em um arquivo3.")


# tentar escrever fora do with
# arquivo.write("Escrever dados em um arquivo4.")

with open("texto2.txt", "w") as arquivo2:
    arquivo2.write("Bem vindos!\n")
    while True:
        fruta = input("Informe uma fruta ou digite S:")
        if fruta != "S":
            arquivo2.write(fruta * 3) # repete a palavra
            arquivo2.write("\n")
        else:
            break

