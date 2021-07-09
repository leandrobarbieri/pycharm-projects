"""
filter(): Filtrar dados de uma coleção com base em uma função que retorna True/False
"""
import statistics

valores = (1.5, 2.7, 3.8, 4.6, 5.4, 6.1)
medida1 = sum(valores) / len(valores)
medida2 = statistics.mean(valores)
print(f"Tradicional {medida1}, Usando Mean: {medida2}")

# filtrar acima da média: o primeiro parametro uma função que retorna True/False
acima_da_media = filter(lambda x: x > medida2, valores)
print(list(acima_da_media))
# após ser utilizado é removido da memória. Esse print retorna True
print(list(acima_da_media))

# Dados faltantes
paises = ['', 'argentina', 'brasil', '', 'colombia', '', 'uruguai']
# Filtros para remover dados faltantes
print(list(filter(lambda x: "" != x, paises)))
print(list(filter(lambda x: len(x) > 0, paises)))
print(list(filter(None, paises)))

# diferença entre map e filter é:
# - map(): recebe dois parametros, uma função e um iteravel e aplica a função em cada iteravel
# - filter(): recebe dois parametros, uma função e um iteravel e filtra os elementos de acordo com a função True/False

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

# map(, filter): O segundo parametro de map filtra e o primeiro aplica uma função nos nomes filtrados
lista_nomes = list(map(lambda nome_instrutora: f"Sua instrutora é {nome_instrutora}",
                       filter(lambda nome_instrutora: len(nome_instrutora) < 5, nomes)))






