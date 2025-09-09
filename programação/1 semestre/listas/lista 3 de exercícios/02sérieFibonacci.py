'''
Faça um programa para calcular a série de Fibonacci para um número informado pelo usuário, sendo F0 = 0, F1 = 1 e Fn= Fn-1+Fn-2
Por exemplo, caso o usuário informe o número 9, o resultado seria:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
'''

print ("====Fibonacci====")
n = int (input ('Digite o valor de n: '))
for i in range (n+1):
    if i == 0:
        atual = ultimo = penultimo = 0
    elif i == 1:
        atual = ultimo = 1
    else: 
        atual = penultimo + ultimo
        penultimo = ultimo
        ultimo = atual
    print (atual, end = ' ')

print ("\n==============")

