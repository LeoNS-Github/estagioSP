# 4 - Dado o valor de faturamento mensal de uma distribuidora, 
# detalhado por estado: 
# •	SP – R$67.836,43 
# •	RJ – R$36.678,66 
# •	MG – R$29.229,88 
# •	ES – R$27.165,48 
# •	Outros – R$19.849,53 

# Escreva um programa na linguagem que desejar onde calcule o percentual de
# representação que cada estado teve dentro do valor total mensal da 
# distribuidora.  

earnings = {
  "SP": 67836.43,
  "RJ": 36678.66,
  "MG": 29229.88,
  "ES": 27165.48,
  "Outros": 19849.53,
}

states = earnings.keys()

values = [str(v).split('.') for v in earnings.values()] # Usando lógica pura para poder somar os
values = [int(v[0])*100+(int(v[1])) for v in values] # números fracionados sem problema de memória

total = sum(values)
for state, value in zip(states, values):
  print("===============")
  print(f"No estado {state}:")
  print(f"Rendimento: {value/100} - {value*100/total:.2f}% da renda total")