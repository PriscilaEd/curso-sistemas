import random

contador = 0

x = int (input ('Digite um número: '))
soma = 0
for i in range (x):
    numero_sorteado = random.randint (1,10)
    print (numero_sorteado)
    soma = numero_sorteado + soma
    
print (f'A soma é {soma}')