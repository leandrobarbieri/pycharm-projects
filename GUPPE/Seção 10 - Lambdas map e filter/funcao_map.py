"""
Mapear um dado de uma lista para uma função aplicar a função em cada elemento da lista
Aplica a função em todos os elementos da lista
A função usada no map só pode receber um parametro
"""
import math


def area_circulo(raio):
    """Calcula a area de um circulo com o raio r"""
    return math.pi * (raio ** 2)


print(area_circulo(2))
print(area_circulo(3.8))

lista_raios = [2, 3, 5, 6, 8]

# Forma tradicional
resultados = []
for r in lista_raios:
    resultados.append(area_circulo(r))

print(resultados)

# Map recebe o nome da função e um iteravel (list, tupla, set, dict)
# Só pode ter um parametro de entrada
areas = map(area_circulo, lista_raios)

# Converte o map object para uma lista para que seja impressa
print(list(areas))

# Map com lambda: para cada item na lista lista_raios aplica a função lambda com raio como parametro e a expressão
resultado_map = list(map(lambda raio: math.pi * (raio ** 2), lista_raios))
resultado_map2 = list(map(lambda raio: math.pi * (raio ** 2), lista_raios))
print(resultado_map)


# Exemplo
cidades = [('Vitória', 29), ('Serra', 27), ('Viana', 19)]


# converter para faherit: f = 9/5 * c + 32
# dado[0] = nome da cidadde
# dado[1] = temperatura
celcius_faheint = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(celcius_faheint, cidades)))























