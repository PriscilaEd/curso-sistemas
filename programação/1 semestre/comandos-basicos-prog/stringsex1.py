'''
Faça um programa que leia uma frase e retorne o número de palavras que ela contém.
Considere que a palavra pode começar e/ou terminar por espaços.
'''

frase = input("Frase: ").strip ()
frase_separada = frase.split (' ') 
print ('frase_separada')
qntd = len(frase_separada)
print (f'A frase tem {qntd} palavras.')