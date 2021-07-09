"""
São dicionários mas com novas funções
As diferenças entre o dict padrão:
- Padrão: se não achar a chave dá KeyError
- Default Dict: Informa o valor padrão caso não ache o valor
https://docs.python.org/3/library/collections.html#collections.defaultdict
"""

# Tratamento do dict padrão para chaves não encontradas
dicionario = {"curso": "Python"}
# print(dicionario["aaa"])
if "aaa" in dicionario:
    print(dicionario["aaa"])
else:
    print("Não encontrado")

# Usando Default Dict não precisa de tratamento (possui valor padrão)
from collections import defaultdict

# Se não econtrar adiciona um elemento novo
dicionario_defaultdict = defaultdict(lambda: 0)
dicionario_defaultdict["curso"] = "Python"
print(dicionario_defaultdict)
print(dicionario_defaultdict["aaaa"])
print(dicionario_defaultdict)











