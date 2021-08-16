"""
Criar partes para executar tarefas específicas
Pode ou não receber entradas de dados
Reaproveitamento de código
Procure escrever funções simples: Funções que realizam varias tarefas não são recomendáveis
DRY: Dont repeat yourself

def nome_da_funcao(parametros_de_entrada):
    bloco da função

- nome da função sempre com letras minusculas: nome_funcao
- parametros de entrada sao opcionais, tendo mais de um separados por vígulas
- bloco da função: onde o processamento acontece, pode ou não ter um retorno

"""

cores = ["Azul", "Preto", "Branco"]

# função built-in do python, print() podem ser chamadas diretamente sem a sintax de ponto
print(cores)

# função que faz parte do tipo de objeto (lista). Chamada a partir do ponto (agregada ao tipo)
cores.append("Roxo")

# funções que não recebem dados de entrada
cores.clear()


# primeira função
def hello_world():
    """Esta é a documentação da função hello world
       aparece quando usamos um help"""
    print("Oi")
    # printa o comentário acima
    help(hello_world)


# Usar a função: nunca esqueça de usar o parenteses para usar a função
hello_world()


# sem parametro e sem retorno
def cantar_parabens():
    print("Parabens para você\n"
          "Desta data querida")


# usando a função dentro de um for
for n in range(0, 5, 1):
    cantar_parabens()
print("-------------")


# função como objeto: executa uma lista de funções
funcoes_criadas_ate_agora = [hello_world, cantar_parabens]
for funcao in funcoes_criadas_ate_agora:
    funcao()










