"""
São funções
Aprimoram o comportamento de outras funções
A função que queremos decorar recebe um decorator, aprimoramentos do comportamento padrão
São exemplos de funções de funções
Usa @ como syntax sugar
"""

# decorator como funções sem usar syntax sugar
def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer vc")
        funcao()
        print("tenha um otimo dia")
    return sendo


def saudacao():
    print("Seja bem vindo")


print("-----------")
# executar a função saudação sem decorator (primoramento)
saudacao()

print("-----------")
# decorando a função saudação com a função seja educado
teste = seja_educado(saudacao)
teste()


# Decorator com syntax sugar
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Muito prazer em conhece-lo")
        funcao()
        print("Tenha um excelente dia!")
    return sendo_mesmo


# usando decorator
@seja_educado_mesmo
def apresentando():
    print(f"Meu nome é Leandro")


apresentando()


