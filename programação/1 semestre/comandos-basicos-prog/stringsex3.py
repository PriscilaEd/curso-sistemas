'''
Faça um programa que leia duas strings do teclado e verifique se são palíndromas mútuas,
ou seja, se uma é igual à outra quando lida de trás para frente.
Exemplo: "amor" e "roma".
'''
'''
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
palindromo = True

ultimo = len(palavra1)-1
if len(palavra1) == len(palavra2):
    for indice in range (len(palavra2)):
        if palavra1[indice] != palavra2[ultimo-indice]:
            print("As strings são palíndromas mútuas.")
            palindromo = False
else:
    print("As strings NÃO são palíndromas mútuas.")
    palindromo = False
'''

palavra1 = input('Palavra 1: ')
palavra2 = input('Palavra 2: ')

inverso1 = palavra1[::-1]
inverso2 = palavra2[::-1]
if inverso1 == palavra2 or inverso2 == palavra1:
    print ('Palindromo')
else:
    print('Não palindromo')