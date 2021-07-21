"""
Diferenças entre data inicial e data final
Intervalos de tempo: dado que representa tempo
"""
import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(1985, 10, 14)

tempo_decorrido = data_hoje - aniversario

print(type(tempo_decorrido))
print(repr(tempo_decorrido))
print(f"Já viveu {tempo_decorrido.days} dias e {tempo_decorrido.seconds // 3600} horas.")

# adicionar dias
regra_boleto = datetime.timedelta(days=3)
data_compra = datetime.datetime.now()
data_pagamento = data_compra + regra_boleto

print(f"Data Compra: {data_compra} - Data pagamento: {data_pagamento}")



