"""
Identificar os problemas no código
"""


# Forma resumida de tratar varios tipos de erro
def dividir1(a, b):
    print(f"Valores de entrada {a} e {b}")
    try:
        return a / b
    except (ValueError, ZeroDivisionError, TypeError) as err:
        print(f"Erro {err}")


a = 1
b = 2
print(dividir1(a, b))


