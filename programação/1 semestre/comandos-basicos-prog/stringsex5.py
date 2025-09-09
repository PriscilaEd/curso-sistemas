
'''
Um anagrama é uma palavra que é feita a partir da transposição de outra palavra ou frase. Por exemplo, "Iracema" é um anagrama para "America". Escreva um programa que decida se uma string é um anagrama de outra string, ignorando os espaços em branco. O programa deve considerar maiúsculas e minúsculas como sendo caracteres iguais, ou seja, "a" = "A".
'''


palavra1 = input('Palavra 1: ').upper ()
palavra2 = input('Palavra 2: ').upper ()
palavra1 = palavra1.upper()
palavra2 = palavra2.upper ()

palavra1 = sorted (palavra1)
palavra2 = sorted (palavra2)
print (f'Palavra 1 ordenada: {palavra1}')
print (f'Palavra 2 ordenada: {palavra2}')
if palavra1 == palavra2:
    print ('São anagramas.')
else: 
    print ('Não são anagramas.')