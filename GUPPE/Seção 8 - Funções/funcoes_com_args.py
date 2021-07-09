"""
O *args é um paramtro de entrada de uma função
Pode ser qualquer nome desde que começe com *, *args é uma convenção

Utilizado em um a função para dar mais flexibilidade no numero de parametros que ela aceita
Os argumentos extras são passados para *args como uma tupla imutavel


Essa é a ordem obrigatoria: Os parametros deve estar na seguinte sequencia na assinatura da função.
- Parametros obrigatorios
- *args
- parametros default não obrigatorios
- **kwargs
"""


# Podemos passar o tanto de parametros que quiser
def soma_todos(num1=0, num2=0, num3=0, *args):
    # total_args = 0
    # for i in args:
        # total_args = total_args + i

    return f"Resultado: {(num1 + num2 + num3) + sum(args)}\n" \
           f"Valores capturados por *args: {list(args)}\n" \
           f"Valores dos parametros padrão: {(num1 + num2 + num3)}"


# soma todos os numeros. A partir do terceiro parametro, os valores são armazenados no *args
print(soma_todos(1, 2, 3, 10, 20, 30, 40, 50))
print("------------------------")

# desempacotando uma lista para passar todos os elementos como argumentos
numeros = [10, 20, 30, 40, 50]

# Usando o * o python desempacota dos os elementos de uma coleção (lista, tupla, set)
print(soma_todos(1, 2, 3, *numeros))


# funciona como *args mas trabalha com dicts
def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa.title()} é {cor}")


cores_favoritas(marcos="verde", maria="vermelho")

