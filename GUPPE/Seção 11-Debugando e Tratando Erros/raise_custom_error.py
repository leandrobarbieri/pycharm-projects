"""
raise:
Criar os proprios tipos de erros de acordo com a necessidade
Regras de negócio que lança exptions
Proprias mensagens de erro

Nada após o raise é executado
"""

# raise ValueError("Esse é uma mensagem de erro lançada pelo programador!")
# raise KeyError("Esse é uma mensagem de erro lançada pelo programador!")


def tipo_cor(texto, cor):
    cores_disponiveis = ["Red", "Blue"]
    if type(texto) is not str:
        raise TypeError("O texto precisa ser uma string")
    elif type(cor) is not str:
        raise TypeError("A cor precisa ser uma string")
    elif cor not in cores_disponiveis:
        raise ValueError("A cor não está na lista de cores disponíveis")
    print(f"O texto {texto} está na cor {cor}")


print(tipo_cor("Leandro Barbieri", "Red"))

# print(tipo_cor("Leandro Barbieri", "Yellow"))

# TypeError: O texto precisa ser uma string
# print(tipo_cor(1, 1))

