'''
Faça um programa que decida se duas strings lidas do teclado são palíndromas mútuas, ou seja, se uma é igual à outra quando lida de traz para frente.
Exemplo: amor e roma
'''


palavra1 = input('Palavra 1: ')
palavra2 = input('Palavra 2: ')

inverso1 = palavra1[::-1]
inverso2 = palavra2[::-1]
if inverso1 == palavra2 or inverso2 == palavra1:
    print ('Palíndromas mútuas')
else:
    print('Não são palíndromas mútuas')