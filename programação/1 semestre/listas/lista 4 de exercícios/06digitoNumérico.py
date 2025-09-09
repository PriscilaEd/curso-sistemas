'''
6- Escreva um programa que conte quantos dígitos numéricos existem em uma string digitada pelo usuário.
Entrada: texto = 'A senha é 1234xyz'
Saída esperada: 4
'''

dígitos = input('Digite a senha: ')
quantidade = 0
for caractere in dígitos:
    if caractere.isdigit():
        quantidade += 1

print(f'{quantidade}')