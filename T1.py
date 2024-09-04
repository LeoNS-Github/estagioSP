# 1 - Observe o trecho de código abaixo:
# int INDICE = 13, SOMA = 0, K = 0; 
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA); 

index = 13
sum = 0
k = 0

while k < index:
    k = k + 1
    sum = sum + k

print(sum)