"""
Aplica um filtro a uma lista passada como parametro
filter(): Filtrar dados de uma coleção com base em uma função que retorna True/False

-> diferença entre map e filter é:
-> map(): recebe dois parametros, uma função e um iteravel e aplica a função em cada iteravel (e como se fosse a parte do retorno de um liscomprehension)
-> filter(): recebe dois parametros, uma função e um iteravel e filtra os elementos de acordo com a função True/False (é como se fosse a parte if do listcomprehension)

"""
import statistics

valores = (1.5, 2.7, 3.8, 4.6, 5.4, 6.1)
medida1 = sum(valores) / len(valores)
medida2 = statistics.mean(valores)
print(f"Tradicional {medida1}, Usando Mean: {medida2}")

# filtrar acima da média: o primeiro parametro uma função que retorna True/False
acima_da_media = filter(lambda x: x > medida2, valores)
print(list(acima_da_media))

# usando listcomprehension
acima_da_media_listcomprehension = [val for val in valores if val > medida2]
print(list(acima_da_media_listcomprehension))

# após ser utilizado é removido da memória. Esse print retorna vazio
print(list(acima_da_media))

# Dados faltantes
paises = ['', 'argentina', 'brasil', '', 'colombia', '', 'uruguai']

# Filtros para remover dados faltantes
print(list(filter(lambda x: "" != x, paises)))
print(list(filter(lambda x: len(x) > 0, paises)))
print(list(filter(None, paises)))

# usando listcomprehension
print([pais for pais in paises if len(pais) > 0])

# diferença entre map e filter é:
# map(): recebe dois parametros, uma função e um iteravel e aplica a função em cada iteravel
# filter(): recebe dois parametros, uma função e um iteravel e filtra os elementos de acordo com a função True/False
# map manipula todos os elementos, filter não altera nada nos valores apenas filtra

# lista de dicts
usuarios = [
    {"username": "leandro", "tweets": ["Eu gosto de bolo", "Eu gosto de pizza"]},
    {"username": "bruna", "tweets": ["Eu gosto de pao", "Eu gosto de amendoin"]},
    {"username": "breno", "tweets": []},
    {"username": "samuel", "tweets": []}
]

# Filtrar usuários inativos, não tweetou
inativos = list(filter(lambda x: len(x["tweets"]) == 0, usuarios))

print("Usuários que não tweetaram:")
for nome in inativos:
    print(f"Nome: {dict(nome)['username']}")

# Uso combinado de filter e map

# Criar uma lista com nomes desde que o nome tenha menos de 5 caracteres
nomes = ["Ana", "Paula", "Clementina"]

# usando map junto com filter
# map(, filter): O segundo parametro de map filtra e o primeiro aplica uma função nos nomes filtrados
lista_nomes = list(map(lambda nome_instrutora: f"Sua instrutora é {nome_instrutora}",
                       filter(lambda nome_instrutora: len(nome_instrutora) < 5, nomes)))

print(lista_nomes)

# listcomprehension
listcomprehension = [f"Sua instrutora é {nome}" for nome in nomes if len(nome) < 5]
print(listcomprehension)






