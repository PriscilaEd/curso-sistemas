# Programa que imprime a soma de todos os números pares entre dois números quaisquer, incluindo-os

num_inicial = int (input ('Digite o primeiro valor: '))
num_final = int (input ('Digite o segundo valor: '))
soma = 0
num = num_inicial
while num <= num_final:
    # ver se é par
    if num % 2 == 0:
        soma = soma + num
        print (f'soma parcial = {soma}')
    num +=1   # num recebe num + 1
print ('='*20)
print (f'soma final = {soma}')