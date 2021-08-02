"""

"""
from datetime import datetime, timedelta

# now permite manipular o timezone
print(f"Agora: {datetime.now()}")
print(f"Agora: {datetime.utcnow()}")

# today não tem especificação de timezone
print(f"Hoje: {datetime.today()}")

# mudanças ocorrento a meia-noite: usar metodo combine()

# combine cria uma data usando os paramtros: passar datetime.time() sem parametros cria um time zerado
# essa data exibe o proximo dia com o horário zerado
manutencao = datetime.combine(datetime.now() + timedelta(days=1), time=datetime.time(datetime.now()))

print(f"Data atual: {datetime.now()} \n"
      f"Amanhã: {timedelta(days=1)}\n"
      f"Manutenção: {manutencao}")

# Dia da semana: weekday. Começam em Zero=Segunda feira
# 0=Segunda, 1=Terça, 2=Quarta, 3=Quinta, 4-Sexta, 5-Sabado, 6-Domingo
dict(sd="Teste", asd="teste")

# usar tupla porque essa lista é imutavel
dias = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo")

print(dias[manutencao.weekday()])

print(f"Nasci: {dias[datetime(day=14, month=10, year=1985).weekday()]}")


# Formatação para o padrão Brasil: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
hoje = datetime.now()
print(f"Hoje (sem formatação): {hoje}")

hoje_formatado = hoje.strftime("%d/%m/%Y")
print(f"Hoje (formatado): {hoje_formatado}")

hoje_formatado = hoje.strftime("%d/%m/%y")
print(f"Hoje (formatado): {hoje_formatado}")

hoje_formatado = hoje.strftime("%d/%B/%y")
print(f"Hoje (formatado): {hoje_formatado}")


# versao 1
def formata_data(data):
    if data.month == 1:
        return f"{data.day} de Jan de {data.year}"
    elif data.month == 2:
        return f"{data.day} de Fec de {data.year}"
    elif data.month == 3:
        return f"{data.day} de Mar de {data.year}"
    elif data.month == 4:
        return f"{data.day} de Abr de {data.year}"
    elif data.month == 5:
        return f"{data.day} de Mai de {data.year}"
    elif data.month == 6:
        return f"{data.day} de Jun de {data.year}"
    elif data.month == 7:
        return f"{data.day} de Jul de {data.year}"
    elif data.month == 8:
        return f"{data.day} de Ago de {data.year}"
    elif data.month == 9:
        return f"{data.day} de Set de {data.year}"
    elif data.month == 10:
        return f"{data.day} de Out de {data.year}"
    elif data.month == 11:
        return f"{data.day} de Nov de {data.year}"
    elif data.month == 12:
        return f"{data.day} de Dez de {data.year}"


# versao 2
from textblob import TextBlob


def formata_data_2(data):
    # vai na internet e faz a tradução
    return f'{data.day} de {TextBlob(data.strftime("%B")).translate(to="pt-br")}'


hoje_formatado = formata_data(hoje)
print(f"Hoje (formatado): {hoje_formatado}")

hoje_formatado = formata_data_2(hoje)
print(f"Hoje (formatado): {hoje_formatado}")

# Convert uma string para uma data. É diferente de strftime()
nascimento = datetime.strptime("10/31/2021", "%m/%d/%Y")
print(nascimento)

#horario = datetime.time(12, 30, 0)
#print(horario)

# Contando tempo decorrido

import timeit, functools

# marcando o tempo de execução de uma parte do código
# number define a quantidade de vezes que o codigo no primeiro parametro e executado

# usando generator
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# usando list
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# usando list
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print("-----------------")

# informa o nome da função "teste" e o parametro "2"
tempo = timeit.timeit(functools.partial(teste, 2), number=10000)
print(tempo)

