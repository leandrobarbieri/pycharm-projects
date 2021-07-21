"""
JSON
Java script object notation

Muito usados em apis de empresas

rl = 'https://dados.es.gov.br/api/3/action/datastore_search?resource_id=976edd20-dda6-4eeb-bd94-9f59a2991723&limit=5'
fileobj = request.urlopen(url)
dados = fileobj.read()

print(dados["result"])


"""

import pandas as pd
from urllib import request
import json
import jsonpickle

dados1 = ["produto", {"PlayStation": ["Jogo1", "2TB"], "xBox": ["Jogo1", "1TB"]}]

# dumps prepara objs python list, dict para o formato padrão json (próximo do padrão python)
dados2 = json.dumps(dados1)

print(type(dados2))
print(dados2)

# salvando em json
with open("animais.json", "w") as arq:
    dados3 = jsonpickle.encode(dados1)
    arq.write(dados3)


# lendo em json
print("---------------------------------------lendo em json")
with open("animais.json", "r") as arq:
    conteudo = arq.read()
    dados4 = jsonpickle.decode(conteudo)
    print(dados4)














