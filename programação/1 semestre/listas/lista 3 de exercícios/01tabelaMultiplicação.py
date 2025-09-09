'''
Faça um programa para montar a tabela de multiplicação de números de 1 a 10 (ex.: 1 x 1 = 1, 1 x 2 = 2, etc.)
'''

for numero in range (1,11):
    print ("="*30) 
    print (f'---Tabuada do {numero}: ')
    print ("="*30)
    for fator in range (1,11):
        tabuada = numero * fator
        print (f'{numero} x {fator} = {tabuada}')