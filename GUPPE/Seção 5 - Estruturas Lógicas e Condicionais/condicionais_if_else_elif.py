"""
if e elif (encadeia uma nova condição) e else finaliza como todas a execessões
"""
idade = int(input('Qual a sua idade?'))

if idade < 18:
    print("Menor de idade")
elif idade > 18:
    print("Maior de idade")
else:
    print("Tem exatamente 18 anos se tiver informando corretamente!")

# If ternário, uma forma mais sucinta de criar um if simples
# <true> if <condição> else <false>
ternario = "Par" if 10 % 2 else "Impar"







