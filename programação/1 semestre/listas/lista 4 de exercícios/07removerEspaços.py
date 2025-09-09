'''
7- Crie um programa que remova espaços em excesso entre palavras de uma frase, mantendo apenas um espaço entre elas.
Entrada: texto = ' Python                 é  legal    '
Saída esperada: 'Python é legal'
'''

frase = input('Digite a frase: ')
palavras = frase.strip().split()
correção = ' '.join(palavras)

print(f'{correção}')