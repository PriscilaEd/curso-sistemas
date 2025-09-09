'''
5- Faça um programa que leia um nome completo e exiba as iniciais de cada nome, separadas por ponto.
Entrada: nome = 'João Carlos da Silva'
Saída esperada: 'J. C. d. S.'
'''

nome = input('Digite seu nome completo: ')
partes = nome.split()
iniciais = [parte[0] + '.' for parte in partes]
resultado = ' '.join(iniciais)
print (f'{resultado}')