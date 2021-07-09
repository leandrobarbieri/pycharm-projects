"""
Repetição enquanto a clausula for verdade
Parecido com for mas a condição de parada com expressão bool
Repete enquanto a expressão for verdadeira
- Expressão bool o resultado é True ou False num < 5
- Critério de parada = condição = False
"""

# importante ter atenção com a condição de parada para que não gere loop infinito
num = 0
while num <= 10:
    print(num)
    # incrementar até chegar a 10
    num += 1


# forma 2: a condição de saída é informada em tempo de exeução
saida = True
while saida:
    print("Continuar")
    out = int(input("Deseja sair? Digite 1: "))
    if out == 1:
        saida = False


# usando break
while True:
    if int(input("Deseja sair? Digite 1: ")) == 1:
        break



