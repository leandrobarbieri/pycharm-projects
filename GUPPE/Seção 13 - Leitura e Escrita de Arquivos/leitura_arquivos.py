"""
Como ler o conteúdo de um arquivo
Pode ter um texto, uma linha ou várias

1- Usa a função integrada open(): Abre o arquivo na memória
- não precisa instalar
- passamos um parametro de entrada que é o nome do arquivo que será lido: retorna um _io.TextIOWrapper para ler o arquivo

OBS: Por padrão a função open() abre o arquivo para leitura, então o arquivo deve sempre existir
"""

arquivo = open("texto.txt", encoding="utf-8")

"""
<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>: objeto para trabalhar como arquivo
mode='r': Modo de read
encoding: representa o formato pode ser UTF-8
"""
print(arquivo)

# _io.TextIOWrapper
print(type(arquivo))

# Para ler o conteúdo de um arquivo, usar a função read()
retorno = arquivo.read()
retorno_lista = retorno.split("\n")
print(retorno)
print(retorno_lista)
print(len(retorno_lista))


# Cursor: semelhante a ideia do cursor piscando no editor de texto
# Ao imprimir novamente o conteúdo do arquivo cursor de leitura está no final do texto então não imprime mais nada
print(arquivo.read())


