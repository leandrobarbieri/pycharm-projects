"""
Utilizando lambdas
Conhecidas como expressões lambdas, funções sem nome, funções anonimas

- padrao de função em python
    def soma(a, b):
        return a + b

lambda <parameto>: <expressao_retorno>

"""


# Função em python padrão
def minha_funcao(x):
    return x * 3 + 1


print(minha_funcao(2))
print(minha_funcao(4))

# A mesma função acima implementada em lambda
# lambda <parameto>: <expressao_retorno>
calc = lambda x: x * 3 + 1

# Calc vira um obj que pode ser utilizado, mas essa não é o cenário de utilização
print(calc(2))
print(calc(4))

# lambdas com múltiplos parametros de entrada
nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo("leAndrO", " BARbieri"))

# Podemos ter nenhum ou vários parametros e entrada
nenhuma_entrada = lambda: "Como não amar python"
uma_entrada = lambda x: 3 * x + 1
varias_entradas = lambda x, y, z: (x * y * z)

print(nenhuma_entrada(), uma_entrada(2), varias_entradas(1, 2, 3))


# Ordenar pelo sobrenome
lista_autores = ["Pedro Bial", "Youval Del Harary", "J. K Holling", "Augusto Curi", "Isaac Asimov"]
print(f"Antes: {lista_autores}")

# O sort ordena a lista, x é o parametro com os nomes da lista (poderia ser qualquer nome), percorre a lista toda
# aplicando o split onde tem espaço e pega a ultima palacra -1, ou seja, o último sobrenome
lista_autores.sort(key=lambda x: x.split(" ")[-1].lower())
print(f"Depois: {lista_autores}")


# Usando lambda no retorno de uma função, retorna apenas a definição, não o resultado
def geradora_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


# Função lambda parametrizada
funcao_gerada = geradora_funcao_quadratica(3, 0, -5)

# Utilizando a lambda gerada/parametrizada. Passar apenas um parametro, lambda gerada aceita apenas um
print(f"Geradora 1: {funcao_gerada(2)}")

# Poderia fazer diretamente passando os paramtros para a geradora e depois o valor para execução da lambda
print(f"Geradora 2: {geradora_funcao_quadratica(3, 0, -5)(2)}")






