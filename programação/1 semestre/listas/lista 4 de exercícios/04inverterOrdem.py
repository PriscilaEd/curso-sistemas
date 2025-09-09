'''
4- Crie um programa que leia uma frase e inverta a ordem das palavras.
Entrada: frase = 'Eu gosto de Python'
Saída esperada: 'Python de gosto Eu'
'''

frase = input (f'Digite uma frase: ')
palavras = frase.split()
invertida = palavras[::-1]
frase_invertida = ' '.join(invertida)

print(frase_invertida)