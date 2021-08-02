"""
Identificar os problemas no código
Clicar no botão vermelho no numero da linha
"""


# Forma resumida de tratar varios tipos de erro
def dividir1(a, b):
    print(f"Valores de entrada {a} e {b}")
    try:
        valor = a / b
        return valor
    except (ValueError, ZeroDivisionError, TypeError) as err:
        print(f"Erro {err}")


a = 1
b = 2
print(dividir1(a, b))


