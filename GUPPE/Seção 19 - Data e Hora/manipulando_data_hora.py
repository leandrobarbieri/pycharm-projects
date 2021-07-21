"""
Datetime: modulo integrado para se trabalhar com data e hora

"""

import datetime

agora = datetime.datetime.now()
print(agora)

# partes das datas/hora
print(repr(datetime.datetime.now()))
print(datetime.datetime.now().day)
print(datetime.datetime.now().month)
print(datetime.datetime.now().year)

inicio = datetime.datetime.now()
print(inicio)

# alterar o horário
inicio = inicio.replace(hour=10)
print(inicio)

# criar um obj datatime
evento = datetime.datetime(2021, 1, 15)
print(evento)

# usando um formato string para o formato de data python
aniversario = input("Nascimento")
aniversario = aniversario.split("/")
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
print(aniversario)