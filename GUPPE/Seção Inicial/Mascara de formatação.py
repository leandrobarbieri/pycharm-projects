"""Mascara de formatação serve para preparar a saída para exibição controlando as casas decimais"""
faturamento = 1500
custo = 500
lucro = faturamento - custo

# Controlando a string dinâmica
print(f"O lucro foi {lucro}")

# Controlar a mascara de formatação. Usa dois pontos iniciar a definição
# Vírgula representa separador de milhar
print(f"O lucro foi {lucro: ,}")

# Casa decinal .2f (float com duas casa)
print(f"O lucro foi R${lucro: ,.2f}")

margem = lucro / faturamento
print(margem)

# Formatação em Percentual com duas casas decimais
print(f"A margem foi:{margem: .2%}")

# Formatar para o padrão brasileiro em reais
# Usar o underline como separador de milhar pq se usar . irá conflitar com o . do separador decimal padrão

# 1 passo: alterar o separador de milhar para _ (underscore)
texto_lucro = f"R${lucro: _.2f}"

# 2 passo: alterar o . (ponto) para vírgula, e depois o _ (underscore) para .
texto_lucro = texto_lucro.replace(".", ",").replace("_", ".")
print(f"O lucro foi {texto_lucro}")
