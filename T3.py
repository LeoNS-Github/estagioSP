# 3 - Dado um vetor que guarda o valor de faturamento diário de uma 
# distribuidora, faça um programa, na linguagem que desejar, 
# que calcule e retorne: 
# O menor valor de faturamento ocorrido em um dia do mês; 
# O maior valor de faturamento ocorrido em um dia do mês; 
# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 
# IMPORTANTE: 
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
# Estes dias devem ser ignorados no cálculo da média; 


# A página da Gupy não apresentava JSON nenhum :/

import json

JSON = '''
{
  "data": [
    {"day": 1, "value": 1000.0},
    {"day": 2, "value": 1500.5},
    {"day": 3, "value": 850.3},
    {"day": 4, "value": 1220.1},
    {"day": 5, "value": 900.0},
    {"day": 6, "value": 0.0},
    {"day": 7, "value": 0.0},
    {"day": 8, "value": 930.2},
    {"day": 9, "value": 1120.0},
    {"day": 10, "value": 0.0}
  ]
}
'''
data = json.loads(JSON)
earnings = [d['value'] for d in data['data'] if d['value'] > 0]
lower = min(earnings)
higher = max(earnings)
average = sum(earnings) / len(earnings)
daysOverAverage = sum(1 for value in earnings if value > average)
result = {
    "Valor mais baixo": lower,
    "Valor mais alto": higher,
    "Dias acima da media mensal": daysOverAverage
}
print(json.dumps(result, indent=2))
