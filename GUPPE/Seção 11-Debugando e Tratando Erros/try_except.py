"""
Capiturar os erros lançados
Fazer o tratamento adequado para impedir que o programa tenha que parar de funcionar
try:
    //tente fazer isso, mas se tiver algum erro lançado
except:
    //Faça isso se tivel algum erro lançado no try
"""


# 1- Tratamento de Erros GENÉRICO: pega qualquer tipo
# mesmo com uma função que não existe, o programa não quebra
try:
    funcao_indefinida()
except:
    print("Deu algum problema no bloco try acima")

# mesmo com uma função que não existe, o programa não quebra
try:
    len(2)
except:
    print("O tipo passado para a função não está correto")


# 2- Tratando um erro específico NameError
try:
    funcao_indefinida()
except NameError as err:
    print(f"Você está usando uma função inexistente - {err}")

# 3- Tratando um erro específico TypeError
try:
    len(3)
    # print(int("A")) # Não vai capiturar porque lança: ValueError: invalid literal for int() with base 10: 'A'
except TypeError as err:
    print(f"O tipo passado para a função não está correto - {err}")

# 4- Tratando um erro específico TypeError
try:
    print(int("A"))
except ValueError as err:
    print(f"O tipo não é o esperado  - {err}")


# Capiturando vários tipos no mesmo try
try:
    print(int("A"))
except ValueError as err:
    print(f"O tipo não é o esperado  - {err}")
except NameError as err:
    print(f"Você está usando uma função inexistente - {err}")
except TypeError as err:
    print(f"O tipo passado para a função não está correto - {err}")
# Genérico: se não for nenhum desses acima
except:
    print("O tipo passado para a função não está correto")


# Dentro de um função
def pega_valor_dict(dicionario, chave):
    try:
        return dicionario[chave]
    except IndexError as err1:
        print(f"IndexError: {err1}")
    except KeyError as err2:
        print(f"KeyError: {err2}")
    except:
        print("Outro tipo de erro")


meu_dicionario = {"a": 1, "b": 2, "c": 3}

# print(pega_valor_dict(meu_dicionario, "b"))

# KeyError
print(pega_valor_dict(meu_dicionario, "y"))







