"""Dicionário
As vezes também são conhecidas como mapas
Dicionários são coleções como as outras
Mapeamento de chave-valor
São representados por {}
Não permitem chaves repetidas.
"""
# <class 'dict'>
print(type({}))
paises = {"br": "Brasil", "eua": "Estados Unidos da America", "eng": "Inglaterra"}
print(paises)

# Outra forma de criar um dicionario
paises2 = dict(br="Brasil", eua="Estados Unidos", eng="Inglaterra")
print(paises2)

# Acessando elementos usando a Key.
# Não são indexados a partir do zero, é a partir do valor da chave definida, não importa a posição
print(paises2["br"])
# Caso utilizarmos uma chave que não existe gera um KeyError
# print(paises2["AA"])

# Usando get. Forma recomendada de acesso. Retorna None se não existe. Não dá erro
print(paises2.get("br"))

# Retorna None se não tiver o valor da chave. None é sempre igual a False
if paises2.get("AA"):
    print(paises2.get("AA"))
else:
    print("Elemento não encontrado")

# get aceita valor padrão caso não encontrar a chave não informada
print(paises2.get("AAA", "Elemento não encontrado"))

# Verificar se existe uma chave específica no dicionário. A busca é pela chave não o valor
if "br" in paises2:
    print(f"br existe no dicionário paises2")

# As chaves podem ser qualquer tipo de dado (int, float, list, tuple, dict...)
# usando tuplas como chaves
localidades = {
    (35.000, 39.000): "Estritório em Ny",
    (34.111, 38.111): "Estritório em Sp",
    (33.222, 37.222): "Estritório em Vix",
    (32.333, 36.333): "Estritório em Rj"
}
# Todas as coordenadas das localidades
for escritorio in localidades:
    lat, long = escritorio
    print(f"Nome do Escritório: {localidades.get(escritorio)} \nLatitude: {lat}, Longitude: {long}")

# Acicionar elementos em um dict
receita = {"jan": 100, "fev": 120, "mar": 300}

# Forma 1: mais comum
receita["abr"] = 350
print(receita)

# Forma 2: Atualizando e adicionando. Se a chave já existe então atualiza, senão adiciona
# adiciona
receita.update({"mai": 500})
print(receita)
# atualiza
receita.update({"abr": 600})
print(receita)

# Acessando Dict
for chave in receita:
    print(f"Chave: {chave}, Valor: {receita[chave]}")

print(f"Valores do dicionário: {receita.values()}")
print(f"Chaves do dicionário: {receita.keys()}")

# Outra forma de iterar usando apenas a lista de chaves
for chave in receita.keys():
    print(f"Modo pytônico: Chave: {chave}, Valor: {receita[chave]}")

# Desempacotamento de dicts: itens retorna uma tupla (chave, valor)
for chave, valor in receita.items():
    print(f"Desempacotamento: Chave: {chave}, Valor: {valor}")

# Soma, Max, Min
print(f"Resumo do Dict: \n"
      f"Soma: {sum(receita.values())} \n"
      f"Max: {max(receita.values())} \n"
      f"Min: {min(receita.values())} \n"
      f"Qtd Itens: {len(receita.values())}")

# Criar um dict zerado passando uma lista de chaves
dicionario = {}.fromkeys(['jan', 'fev', 'mar', 'abr'], 0)
print(f"Dicionário criado a partir de uma lista de chaves {dicionario}")

# Remover dados: informar a chave. Se não houver um KeyError é retornado

# Forma 1: pop remove e retorna o valor
removido = receita.pop("mai")
print(receita)

# Forma 2: somente remove, não retorna valor
del receita["jan"]
print(receita)

# Metodos de dicts
print(dir({}))

# Copiando um dicionário para outro
novo_dict = receita.copy()
print(novo_dict)

print(receita.values())
print(receita.keys())

# Limpar o dicionário
print(receita.clear())







