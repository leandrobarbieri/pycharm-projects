"""
Modulo Collections: ordered dict
https://docs.python.org/3/library/collections.html#collections.OrderedDict

Por padrão nos dicionarios a ordem não é garantida
"""

dicionario = {"a": 1, "b": 2, "c": 3, "e": 4}
for chave, valor in dicionario.items():
    print(f"Chave: {chave}, Valor:{valor}")

# Usando ordered dict
from collections import OrderedDict
dicionario_ordereddict = OrderedDict({"a": 1, "b": 2, "c": 3, "e": 4})
print(dicionario_ordereddict)

# Diferença entre Dict e OrderedDict

# Para um dicionário comum a ordem não importa, por isso são iguas
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1}
print(dict1 == dict2)

# Para um dicionário OrderedDict eles não são iguas, porque um está na ordem diferente. A ordem importa
ordereddict1 = OrderedDict({"a": 1, "b": 2})
ordereddict2 = OrderedDict({"b": 2, "a": 1})
print(ordereddict1 == ordereddict2)




