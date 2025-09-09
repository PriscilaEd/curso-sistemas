'''
3- Escreva um programa que substitua todas as ocorrências da letra 'a' por '*' em uma string fornecida pelo usuário.
Entrada: texto = 'banana'
Saída esperada: 'b*n*n*'
'''

palavra = str (input (f'Digite a palavra: '))
substituição = palavra.replace ('a', '*').replace ('A', '*')
print (f'{substituição}')