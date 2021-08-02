"""
Quando saber quando tratar ou não um erro
Partes do codigo que precisam de mais atenção
- entrada de dados (usuário, entrada funções)
"""

# try e except é executado sempre
try:
    num = int(input("Informe:"))
except ValueError as err:
    print("Valor incorreto, informe um numero")
# somente se não der erro
else:
    print(f"Você digitou {num}")
finally:
    print("Boa noite. Sempre é executado")


# Tratar as entradas das funções. Impede que a divisão por zero de erro
def dividir(a, b):
    try:
        return a / b
    except ValueError:
        print("Erro")
    except ZeroDivisionError:
        print("ZeroDivisionError")


print(dividir(1, 0))


# Forma resumida de tratar varios tipos de erro
def dividir1(a, b):
    try:
        return a / b
    except (ValueError, ZeroDivisionError, TypeError) as err:
        print(f"Erro {err}")


print(dividir1(1, "a"))