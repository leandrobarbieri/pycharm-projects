"""
PEP8 Python Enhancements 8
Propostas de melhorias para a linguagem. Escrever códigos python de forma pytônica
import this: digitar no console imprime o poema que descreve as melhores práticas

[1] - Utiliza CamelCase para nomes de classes
    class Calculadora:
        pass

    class CalculadoraCientifica:
        pass

[2] - Utilize nomes em minúsculo separados com _ para funções ou variáveis
    def soma():
        pass

    def soma_dois():
        pass
        numero = 1
        numero1 = 2

[3] - Utilize 4 espaços para identitação. Evite usar o tab
    if 'a' in 'banana':
        print('tem')

[4] - Linhas em branco: Quantidade correta de linhas separando classes.
Duas linhas entre classes, funções
Uma linha de separação entre metodos

[5] - Imports.No topo do arquivo
Devem ser sempre feitos em linhas separadas para modulos inteiros
import pandas as pd

* para import de pacotes específicos. mesma linha
from types import StringType, ListType
from pandas import DataFrame

[6] - Espaços em expressões
Não deixar espaços entre as chaves, parenteses
Errodo: nome_funcao( algo[ 1 ], { outro: 2 } )
Certo: nome_funcao(algo[1], {outro:2})

[7] - Termine uma instrução sempre com uma nova linha

"""
from pandas import DataFrame
d = DataFrame()

def nome_funcao():
    print(__name__)

# algo = [1]
# outro = [1, 2]

nome_funcao()

