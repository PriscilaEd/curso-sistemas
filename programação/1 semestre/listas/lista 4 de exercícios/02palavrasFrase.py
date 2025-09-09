'''
2- Desenvolva um programa que leia uma frase e retorne quantas palavras existem nela, considerando palavras separadas por espaços.
Entrada: frase = 'Aprender Python é muito legal!'
Saída esperada: 5
'''

frase = input ('Digite a frase: ')
palavras = frase.split ()
quantidade = len(palavras)

print (f'{quantidade}')
