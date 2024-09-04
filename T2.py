# 2 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo
# valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e retorne
# uma mensagem avisando se o número informado pertence ou não a sequência.

index = [0,1]

num = int(input("Escreva um número para conferir: "))

while index[1] <= num:
    if index[1] == num:
        print("Positivo! Número pertence a sequência de Fibonacci")
        break
    index = [ index[1], index[0]+index[1] ]
else:
    print("Negativo! Número não encontrado na sequência Fibonacci")