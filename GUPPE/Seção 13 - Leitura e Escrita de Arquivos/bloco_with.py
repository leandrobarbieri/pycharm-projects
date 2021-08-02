"""
Passos para trabalhar com arquivos

1-Abrir
2-Manipular
3-Fechar a conexão com o arquivo no disco streaming

# with cria um contexto de trabalho com o arquivos
os recursos utilizados são fechados após o término do bloco
"""

# abre um contexto para o arquivo na memoria e fecha automaticamente
with open("texto.txt") as arquivo:
    print(f"O aquivo está fechado? { arquivo.closed}")

print(f"O aquivo está fechado? { arquivo.closed}")
# dá erro poque já está fechado
# arquivo.read()


