'''
14- Desenvolva um programa que extraia todas as hashtags de uma frase (palavras precedidas por #) e exiba essas hashtags em uma lista.
Entrada: frase = 'Adoro #Python e #programação!'
Saída esperada: ['#Python', '#programação']
'''
import re

frase = input('Digite uma frase com hashtags: ')
hashtags = re.findall(r'#\w+', frase)
print(hashtags)