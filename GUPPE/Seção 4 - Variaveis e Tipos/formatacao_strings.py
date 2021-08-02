"""Mascara de formatação serve para preparar a saída para exibição controlando as casas decimais
   Permite definir strings dinâmicas com variaveis como parte da saída
"""

faturamento = 1500
custo = 500
lucro = faturamento - custo

# string dinâmica inserindo variaveis como parte da saída
# usar a letra "f" no inicio da string
print(f"O lucro foi {lucro}")

# Controlar a mascara de formatação.
# Usar dois pontos iniciar a definição
# Vírgula representa que terá separador de milhar
print(f"O lucro foi {lucro: ,}")

# Adicionar casa decinal ".2f" (float com duas casa) depois da vírgula
print(f"O lucro foi R${lucro: ,.2f}")

# Sem formatação de percentual
margem = lucro / faturamento
print(margem)

# Formatação em Percentual com duas casas decimais
print(f"A margem foi:{margem: .2%}")

# Formatar para o padrão brasileiro em reais
# Usar o underline como separador de milhar pq se usar . irá conflitar com o . do separador decimal padrão

# 1 passo: alterar o separador de ponto milhar para _ (underscore)
texto_lucro = f"R${lucro: _.2f}"

# 2 passo: alterar o . (ponto) quer representa decinal para vírgula,
# e depois o _ (underscore) que representa milhar para .
texto_lucro = texto_lucro.replace(".", ",").replace("_", ".")
print(f"O lucro foi {texto_lucro}")
